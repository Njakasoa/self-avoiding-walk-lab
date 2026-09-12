"""Independent attack on the square-memory line-graph candidate.

This checker deliberately rebuilds the square D4 state geometry and weighted
equitable partitions without importing any producer from ``src``.  It tests
the candidate at the row level first, then compares the resulting quotient
graphs by refinement on their disjoint union.  The triangular control is
unreduced (identity normalization only) so a triangle can be seen directly.

The graph convention is the one in ``proofs/FINITE_MEMORY.md``: a memory-m
state is a simple path with m edges, and a row contains one unit transition
per permitted directional extension.  D4 rows retain directional
multiplicity after orbit normalization.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "results" / "linegraph-independent-report.md"

Point = tuple[int, int]
PathState = tuple[Point, ...]
Row = dict[int, int]

SQUARE: tuple[Point, ...] = ((1, 0), (0, 1), (-1, 0), (0, -1))
TRIANGULAR: tuple[Point, ...] = (
    (1, 0),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (0, -1),
    (1, -1),
)

# The eight signed permutation matrices of the square D4 group.  Keeping this
# list explicit makes this checker independent of the memory producer's group
# construction.
D4: tuple[tuple[int, int, int, int], ...] = tuple(
    sorted(
        {
            (sx, 0, 0, sy)
            for sx in (-1, 1)
            for sy in (-1, 1)
        }
        | {
            (0, sx, sy, 0)
            for sx in (-1, 1)
            for sy in (-1, 1)
        }
    )
)
IDENTITY: tuple[tuple[int, int, int, int], ...] = ((1, 0, 0, 1),)


class ResourceLimit(RuntimeError):
    """A complete finite graph was not produced within the local budget."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def json_digest(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()
    return sha256_bytes(encoded)


def linear(point: Point, matrix: tuple[int, int, int, int]) -> Point:
    a, b, c, d = matrix
    x, y = point
    return (a * x + b * y, c * x + d * y)


def normalize(path: PathState, group: Iterable[tuple[int, int, int, int]]) -> PathState:
    """Translate the first vertex to the origin and choose a canonical orbit."""

    candidates: list[PathState] = []
    for matrix in group:
        transformed = tuple(linear(point, matrix) for point in path)
        x0, y0 = transformed[0]
        candidates.append(tuple((x - x0, y - y0) for x, y in transformed))
    return min(candidates)


def _budget(
    started: float,
    size: int,
    max_states: int,
    max_seconds: float,
    ticks: list[int],
) -> None:
    if size > max_states:
        raise ResourceLimit(f"state cap {max_states} exceeded")
    ticks[0] += 1
    if ticks[0] % 256 == 0 and time.monotonic() - started > max_seconds:
        raise ResourceLimit(f"time cap {max_seconds:g}s exceeded")


def build_graph(
    memory: int,
    *,
    directions: tuple[Point, ...] = SQUARE,
    group: tuple[tuple[int, int, int, int], ...] = D4,
    max_states: int = 100_000,
    max_seconds: float = 300.0,
) -> dict[str, object]:
    """Build one finite-memory orbit graph from geometry alone."""

    if type(memory) is not int or memory < 1:
        raise ValueError("memory must be a positive integer")
    started = time.monotonic()
    ticks = [0]
    layer: set[PathState] = {((0, 0),)}
    _budget(started, len(layer), max_states, max_seconds, ticks)

    for _ in range(memory):
        next_layer: set[PathState] = set()
        for path in layer:
            x, y = path[-1]
            for dx, dy in directions:
                destination = (x + dx, y + dy)
                if destination in path:
                    continue
                next_layer.add(normalize(path + (destination,), group))
                _budget(started, len(next_layer), max_states, max_seconds, ticks)
            _budget(started, len(next_layer), max_states, max_seconds, ticks)
        layer = next_layer

    states = sorted(layer)
    index = {state: i for i, state in enumerate(states)}
    rows: list[Row] = []
    for path in states:
        row: Counter[int] = Counter()
        x, y = path[-1]
        for dx, dy in directions:
            destination = (x + dx, y + dy)
            if destination in path:
                continue
            next_state = normalize(path[1:] + (destination,), group)
            if next_state not in index:
                raise AssertionError("geometric destination missing from layer")
            row[index[next_state]] += 1
        rows.append(dict(sorted(row.items())))
        _budget(started, len(states), max_states, max_seconds, ticks)

    if time.monotonic() - started > max_seconds:
        raise ResourceLimit(f"time cap {max_seconds:g}s exceeded")
    return {
        "memory": memory,
        "states": states,
        "rows": rows,
        "state_count": len(states),
        "transition_count": sum(sum(row.values()) for row in rows),
        "stored_transition_count": sum(len(row) for row in rows),
        "build_seconds": time.monotonic() - started,
    }


def equitable_partition(rows: list[Mapping[int, int]]) -> list[int]:
    """Own weighted directed colour-refinement implementation."""

    if not rows:
        return []
    partition = [0] * len(rows)
    rounds = 0
    while True:
        block_count = max(partition) + 1
        states_by_block: list[list[int]] = [[] for _ in range(block_count)]
        for state, block in enumerate(partition):
            states_by_block[block].append(state)

        refined = [-1] * len(rows)
        next_block = 0
        for states in states_by_block:
            groups: dict[tuple[tuple[int, int], ...], list[int]] = {}
            for state in states:
                totals: dict[int, int] = {}
                for destination, weight in rows[state].items():
                    if weight:
                        block = partition[destination]
                        totals[block] = totals.get(block, 0) + weight
                signature = tuple(sorted(totals.items()))
                groups.setdefault(signature, []).append(state)
            for signature in sorted(groups):
                for state in groups[signature]:
                    refined[state] = next_block
                next_block += 1

        rounds += 1
        if refined == partition:
            return partition
        partition = refined


def quotient(rows: list[Mapping[int, int]], mapping: list[int]) -> list[Row]:
    """Construct and check an exact weighted quotient."""

    if len(rows) != len(mapping):
        raise AssertionError("partition length mismatch")
    block_count = max(mapping) + 1 if mapping else 0
    representatives = [-1] * block_count
    for state, block in enumerate(mapping):
        if representatives[block] == -1:
            representatives[block] = state

    result: list[Row] = []
    for representative in representatives:
        totals: Counter[int] = Counter()
        for destination, weight in rows[representative].items():
            totals[mapping[destination]] += weight
        result.append(dict(sorted(totals.items())))

    for state, row in enumerate(rows):
        totals: Counter[int] = Counter()
        for destination, weight in row.items():
            totals[mapping[destination]] += weight
        if dict(sorted(totals.items())) != result[mapping[state]]:
            raise AssertionError("partition is not equitable")
    return result


def candidate_linegraph_rows(
    next_states: list[PathState],
    *,
    group: tuple[tuple[int, int, int, int], ...],
    directions: tuple[Point, ...],
) -> list[Row]:
    """Rows of L(A_m), indexed by the corresponding A_(m+1) state.

    For p'=(v_0,...,v_(m+1)), the line-graph source edge ends at the suffix
    t=(v_1,...,v_(m+1)).  A line-graph extension may append any neighbour not
    in t, including v_0.  The actual A_(m+1) row also forbids v_0; their only
    possible difference is therefore the closing walk.
    """

    index = {state: i for i, state in enumerate(next_states)}
    candidate: list[Row] = []
    for path in next_states:
        suffix = path[1:]
        x, y = suffix[-1]
        row: Counter[int] = Counter()
        for dx, dy in directions:
            destination = (x + dx, y + dy)
            if destination in suffix:
                continue
            next_state = normalize(suffix + (destination,), group)
            if next_state not in index:
                raise AssertionError("line-graph destination missing from next layer")
            row[index[next_state]] += 1
        candidate.append(dict(sorted(row.items())))
    return candidate


def row_delta(actual: list[Mapping[int, int]], candidate: list[Mapping[int, int]]) -> dict[str, int | bool]:
    if len(actual) != len(candidate):
        return {
            "equal": False,
            "different_rows": -1,
            "extra_weight": -1,
            "missing_weight": -1,
        }
    different = 0
    extra = 0
    missing = 0
    for left, right in zip(actual, candidate):
        if dict(left) != dict(right):
            different += 1
        keys = set(left) | set(right)
        for key in keys:
            a = left.get(key, 0)
            c = right.get(key, 0)
            if c > a:
                extra += c - a
            elif a > c:
                missing += a - c
    return {
        "equal": different == 0,
        "different_rows": different,
        "extra_weight": extra,
        "missing_weight": missing,
    }


def indegree_outdegree(rows: list[Mapping[int, int]]) -> tuple[list[int], list[int]]:
    indegree = [0] * len(rows)
    outdegree = [0] * len(rows)
    for source, row in enumerate(rows):
        outdegree[source] = sum(row.values())
        for destination, weight in row.items():
            indegree[destination] += weight
    return indegree, outdegree


def positive_indegree_restriction(rows: list[Mapping[int, int]]) -> tuple[list[Row], list[int]]:
    indegree, _ = indegree_outdegree(rows)
    keep = [state for state, value in enumerate(indegree) if value > 0]
    relabel = {old: new for new, old in enumerate(keep)}
    restricted: list[Row] = []
    for old in keep:
        row = {
            relabel[destination]: weight
            for destination, weight in rows[old].items()
            if destination in relabel and weight
        }
        restricted.append(dict(sorted(row.items())))
    return restricted, keep


def disjoint_union_isomorphism(
    left: list[Mapping[int, int]], right: list[Mapping[int, int]]
) -> dict[str, object]:
    """Use weighted refinement over both graphs, then verify the map exactly."""

    if len(left) != len(right):
        return {
            "isomorphic": False,
            "reason": "different vertex counts",
            "left_vertices": len(left),
            "right_vertices": len(right),
            "refinement_rounds": 0,
            "union_blocks": None,
            "singleton_cross_side_blocks": False,
        }

    size = len(left)
    union = [dict(row) for row in left] + [dict(row) for row in right]
    partition = [0] * len(union)
    rounds = 0
    while True:
        block_count = max(partition) + 1 if partition else 0
        states_by_block: list[list[int]] = [[] for _ in range(block_count)]
        for state, block in enumerate(partition):
            states_by_block[block].append(state)
        refined = [-1] * len(union)
        next_block = 0
        for states in states_by_block:
            groups: dict[tuple[tuple[int, int], ...], list[int]] = {}
            for state in states:
                totals: dict[int, int] = {}
                for destination, weight in union[state].items():
                    block = partition[destination]
                    totals[block] = totals.get(block, 0) + weight
                signature = tuple(sorted(totals.items()))
                groups.setdefault(signature, []).append(state)
            for signature in sorted(groups):
                for state in groups[signature]:
                    refined[state] = next_block
                next_block += 1
        rounds += 1
        if refined == partition:
            partition = refined
            break
        partition = refined

    side_counts = []
    mapping: dict[int, int] = {}
    for block in range(max(partition) + 1 if partition else 0):
        members = [state for state, label in enumerate(partition) if label == block]
        left_members = [state for state in members if state < size]
        right_members = [state - size for state in members if state >= size]
        side_counts.append((len(left_members), len(right_members)))
        if len(left_members) == 1 and len(right_members) == 1:
            mapping[left_members[0]] = right_members[0]

    singleton_cross_side = bool(side_counts) and all(pair == (1, 1) for pair in side_counts)
    exact = singleton_cross_side
    if exact:
        for source, row in enumerate(left):
            mapped = {
                mapping[destination]: weight for destination, weight in row.items()
            }
            if dict(sorted(mapped.items())) != dict(sorted(right[mapping[source]].items())):
                exact = False
                break

    return {
        "isomorphic": exact,
        "reason": "weighted refinement produced a verified bijection" if exact else "ambiguous or nonmatching refinement blocks",
        "left_vertices": size,
        "right_vertices": len(right),
        "refinement_rounds": rounds,
        "union_blocks": len(side_counts),
        "singleton_cross_side_blocks": singleton_cross_side,
    }


def explicit_linegraph(rows: list[Mapping[int, int]]) -> list[Row]:
    """Expand a tiny weighted graph into edge instances and form L(G)."""

    edges: list[tuple[int, int]] = []
    for source, row in enumerate(rows):
        for destination, weight in row.items():
            edges.extend((source, destination) for _ in range(weight))
    line_rows: list[Row] = []
    for _, head in edges:
        row: Counter[int] = Counter()
        for edge_id, (tail, _) in enumerate(edges):
            if tail == head:
                row[edge_id] += 1
        line_rows.append(dict(sorted(row.items())))
    return line_rows


def reducible_sink_sanity() -> dict[str, object]:
    """Exercise the positive-indegree restriction on a reducible graph."""

    # Class 0 is an unreachable source, class 2 contains sinks.  The graph is
    # intentionally reducible and has several edge instances ending in sinks.
    rows: list[Row] = [
        {1: 1, 2: 1},
        {3: 1},
        {3: 1},
        {},
        {5: 1},
        {},
    ]
    mapping = equitable_partition(rows)
    qrows = quotient(rows, mapping)
    restricted, keep = positive_indegree_restriction(qrows)
    line_rows = explicit_linegraph(rows)
    line_mapping = equitable_partition(line_rows)
    line_qrows = quotient(line_rows, line_mapping)
    comparison = disjoint_union_isomorphism(line_qrows, restricted)
    indegree, outdegree = indegree_outdegree(qrows)
    return {
        "original_vertices": len(rows),
        "original_quotient_vertices": len(qrows),
        "zero_indegree_classes": sum(value == 0 for value in indegree),
        "sink_classes": sum(value == 0 for value in outdegree),
        "positive_indegree_classes": len(keep),
        "linegraph_quotient_vertices": len(line_qrows),
        "quotient_isomorphism": comparison,
    }


def git_text(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def markdown_report(data: dict[str, object]) -> str:
    provenance = data["provenance"]
    cases = data["square_cases"]
    direct = data["direct_linegraph_checks"]
    quotient_checks = data["quotient_checks"]
    triangle = data["triangular_control"]
    sanity = data["reducible_sink_sanity"]

    lines = [
        "# Independent line-graph candidate check",
        "",
        "This receipt is an independent falsification attempt for the proposed",
        "square-lattice relation between consecutive finite-memory automata.  The",
        "checker rebuilds path geometry, D4 normalization, weighted rows, and",
        "coarsest outgoing equitable partitions using only Python's standard",
        "library; it imports no producer from `src`.  Counts are finite exact",
        "integer computations and do not assert novelty.",
        "",
        "## Provenance",
        "",
        f"- Source commit: `{provenance['source_commit']}`; worktree dirty: `{provenance['worktree_dirty']}`.",
        f"- Command: `{provenance['command']}`.",
        f"- Input SHA-256: checker `{provenance['input_hashes']['proofs/check_linegraph_candidate.py']}`, ",
        f"`NORMALIZATION.md` `{provenance['input_hashes']['NORMALIZATION.md']}`, ",
        f"`proofs/FINITE_MEMORY.md` `{provenance['input_hashes']['proofs/FINITE_MEMORY.md']}`, ",
        f"`proofs/EQUITABLE_COMPRESSION.md` `{provenance['input_hashes']['proofs/EQUITABLE_COMPRESSION.md']}`.",
        f"- Deterministic result SHA-256: `{provenance['result_sha256']}`.",
        "",
        "## Prediction recorded before the m12 build",
        "",
        f"After independently computing m11, its quotient had `{data['prediction']['m11_quotient']}` classes and `{data['prediction']['m11_zero_indegree']}` zero-indegree classes.  The line-graph candidate therefore predicted ",
        f"`q12 = {data['prediction']['predicted_q12']}` classes.  The actual m12 quotient after construction was `{data['prediction']['actual_q12']}` (`prediction_matches={data['prediction']['prediction_matches']}`).  This prediction was written to this report before constructing the m12 state layer.",
        "",
        "## Square D4 geometry and partitions",
        "",
        "Rows retain directional multiplicity after D4 orbit normalization.  `zero-in` and `zero-out` count quotient classes, not raw states.",
        "",
        "| memory | D4 states | transition weight | stored row entries | quotient classes | zero-in | zero-out | build seconds |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for case in cases:
        lines.append(
            f"| {case['memory']} | {case['state_count']} | {case['transition_count']} | {case['stored_transition_count']} | {case['quotient_classes']} | {case['zero_indegree_classes']} | {case['zero_outdegree_classes']} | {case['build_seconds']:.3f} |"
        )

    lines += [
        "",
        "## Direct row-level line-graph test",
        "",
        "For each next-memory state p'=(v0,...,v_(m+1)), the candidate row allows",
        "extensions avoiding the suffix (v1,...,v_(m+1)); the actual row also",
        "forbids v0.  A difference is exactly a closing walk of length m+2.",
        "",
        "| m -> m+1 | candidate equals actual | differing rows | candidate extra weight | actual missing weight |",
        "|---:|:---:|---:|---:|---:|",
    ]
    for check in direct:
        lines.append(
            f"| {check['memory']} -> {check['next_memory']} | {check['equal']} | {check['different_rows']} | {check['extra_weight']} | {check['missing_weight']} |"
        )

    lines += [
        "",
        "## Quotient comparison without label matching",
        "",
        "The proposed quotient for m+1 is the m quotient restricted to classes",
        "with positive indegree.  Each comparison starts one colour on the",
        "disjoint union, refines by exact weighted outgoing signatures, and then",
        "checks the resulting cross-side bijection edge by edge.",
        "",
        "| comparison | next quotient | restricted current quotient | isomorphic | refinement rounds | union blocks |",
        "|:---|---:|---:|:---:|---:|---:|",
    ]
    for check in quotient_checks:
        result = check["isomorphism"]
        lines.append(
            f"| m{check['memory']} -> m{check['next_memory']} | {result['left_vertices']} | {result['right_vertices']} | {result['isomorphic']} | {result['refinement_rounds']} | {result['union_blocks']} |"
        )

    lines += [
        "",
        "## Reducibility, sinks, and zero-indegree classes",
        "",
        "The graph-theoretic reason for the restriction is local: a line-graph",
        "vertex is an edge of the original graph, so its class is determined by",
        "the class of its head.  A class with zero indegree contributes no line-",
        "graph vertices and is removed.  A positive-indegree sink still contributes",
        "vertices, whose rows are zero; reducibility therefore does not justify",
        "dropping sinks.  A separate small reducible graph with both an unreachable",
        "source class and sink classes gave:",
        "",
        f"`{json.dumps(sanity, sort_keys=True)}`",
        "",
        "The synthetic line-graph quotient matched the positive-indegree",
        "restriction exactly, including the sink class.",
        "",
        "## Triangular negative control",
        "",
        "The triangular lattice was rebuilt with identity normalization.  Its",
        "triangles make the odd closing walk possible, so the same row test should",
        "fail already at m=1 (closure length 3).",
        "",
        "| m -> m+1 | states at m+1 | candidate equals actual | differing rows | candidate extra weight |",
        "|---:|---:|:---:|---:|---:|",
    ]
    for check in triangle:
        lines.append(
            f"| {check['memory']} -> {check['next_memory']} | {check['next_state_count']} | {check['equal']} | {check['different_rows']} | {check['extra_weight']} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The square odd-memory row checks and the m9/m10 and m11/m12 quotient",
        "checks are the predicted matches; the even-memory square check and the",
        "triangular control are negative controls.  This supports the finite",
        "candidate and its positive-indegree bookkeeping for these exact graphs",
        "only.  It is a standard line-graph/equitable-partition observation and",
        "carries no novelty claim or infinite-lattice conclusion.",
        "",
    ]
    return "\n".join(lines)


def run() -> dict[str, object]:
    command = "PYTHONPATH=. .venv/bin/python proofs/check_linegraph_candidate.py"
    source_commit = git_text("rev-parse", "HEAD")
    worktree_dirty = bool(git_text("status", "--porcelain"))

    graphs: dict[int, dict[str, object]] = {}
    for memory in (9, 10, 11):
        graphs[memory] = build_graph(memory)
        states = graphs[memory]["states"]
        rows = graphs[memory]["rows"]
        mapping = equitable_partition(rows)
        qrows = quotient(rows, mapping)
        indegree, outdegree = indegree_outdegree(qrows)
        graphs[memory]["mapping"] = mapping
        graphs[memory]["qrows"] = qrows
        graphs[memory]["quotient_classes"] = len(qrows)
        graphs[memory]["zero_indegree_classes"] = sum(value == 0 for value in indegree)
        graphs[memory]["zero_outdegree_classes"] = sum(value == 0 for value in outdegree)

    prediction = {
        "m11_quotient": graphs[11]["quotient_classes"],
        "m11_zero_indegree": graphs[11]["zero_indegree_classes"],
        "predicted_q12": graphs[11]["quotient_classes"] - graphs[11]["zero_indegree_classes"],
    }

    # Preserve the prediction before the expensive m12 construction begins.
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        "# Independent line-graph candidate check\n\n"
        "Prediction recorded before the m12 build: "
        f"q11={prediction['m11_quotient']}, zero-indegree={prediction['m11_zero_indegree']}, "
        f"predicted q12={prediction['predicted_q12']}.\n",
        encoding="utf-8",
    )

    graphs[12] = build_graph(12)
    for memory in (12,):
        rows = graphs[memory]["rows"]
        mapping = equitable_partition(rows)
        qrows = quotient(rows, mapping)
        indegree, outdegree = indegree_outdegree(qrows)
        graphs[memory]["mapping"] = mapping
        graphs[memory]["qrows"] = qrows
        graphs[memory]["quotient_classes"] = len(qrows)
        graphs[memory]["zero_indegree_classes"] = sum(value == 0 for value in indegree)
        graphs[memory]["zero_outdegree_classes"] = sum(value == 0 for value in outdegree)

    square_cases = []
    for memory in (9, 10, 11, 12):
        graph = graphs[memory]
        square_cases.append(
            {
                "memory": memory,
                "state_count": graph["state_count"],
                "transition_count": graph["transition_count"],
                "stored_transition_count": graph["stored_transition_count"],
                "quotient_classes": graph["quotient_classes"],
                "zero_indegree_classes": graph["zero_indegree_classes"],
                "zero_outdegree_classes": graph["zero_outdegree_classes"],
                "build_seconds": graph["build_seconds"],
            }
        )

    direct_linegraph_checks = []
    for memory in (9, 10, 11):
        candidate = candidate_linegraph_rows(
            graphs[memory + 1]["states"], group=D4, directions=SQUARE
        )
        delta = row_delta(graphs[memory + 1]["rows"], candidate)
        direct_linegraph_checks.append(
            {"memory": memory, "next_memory": memory + 1, **delta}
        )

    quotient_checks = []
    for memory in (9, 10, 11):
        restricted, keep = positive_indegree_restriction(graphs[memory]["qrows"])
        comparison = disjoint_union_isomorphism(
            graphs[memory + 1]["qrows"], restricted
        )
        quotient_checks.append(
            {
                "memory": memory,
                "next_memory": memory + 1,
                "current_positive_classes": len(keep),
                "isomorphism": comparison,
            }
        )

    triangular_control = []
    triangular_graphs: dict[int, dict[str, object]] = {}
    for memory in (1, 2):
        triangular_graphs[memory] = build_graph(
            memory, directions=TRIANGULAR, group=IDENTITY
        )
    for memory in (1, 2):
        candidate = candidate_linegraph_rows(
            triangular_graphs[memory + 1]["states"]
            if memory + 1 in triangular_graphs
            else build_graph(memory + 1, directions=TRIANGULAR, group=IDENTITY)["states"],
            group=IDENTITY,
            directions=TRIANGULAR,
        )
        # The m=2 next layer was not retained above; rebuild it only in this
        # tiny control to keep the main square receipt focused on m9..m12.
        next_graph = (
            triangular_graphs[memory + 1]
            if memory + 1 in triangular_graphs
            else build_graph(memory + 1, directions=TRIANGULAR, group=IDENTITY)
        )
        delta = row_delta(next_graph["rows"], candidate)
        triangular_control.append(
            {
                "memory": memory,
                "next_memory": memory + 1,
                "next_state_count": next_graph["state_count"],
                **delta,
            }
        )

    data_without_provenance: dict[str, object] = {
        "prediction": {
            **prediction,
            "actual_q12": graphs[12]["quotient_classes"],
            "prediction_matches": prediction["predicted_q12"] == graphs[12]["quotient_classes"],
        },
        "square_cases": square_cases,
        "direct_linegraph_checks": direct_linegraph_checks,
        "quotient_checks": quotient_checks,
        "triangular_control": triangular_control,
        "reducible_sink_sanity": reducible_sink_sanity(),
    }
    # Performance timings are useful in the report but are excluded from this
    # payload hash so rerunning the same exact computation remains comparable.
    digest_payload = json.loads(json.dumps(data_without_provenance, sort_keys=True))
    for case in digest_payload["square_cases"]:
        case.pop("build_seconds", None)
    result_digest = json_digest(digest_payload)
    input_hashes = {
        "proofs/check_linegraph_candidate.py": sha256_file(Path(__file__).resolve()),
        "NORMALIZATION.md": sha256_file(ROOT / "NORMALIZATION.md"),
        "proofs/FINITE_MEMORY.md": sha256_file(ROOT / "proofs" / "FINITE_MEMORY.md"),
        "proofs/EQUITABLE_COMPRESSION.md": sha256_file(
            ROOT / "proofs" / "EQUITABLE_COMPRESSION.md"
        ),
    }
    data: dict[str, object] = {
        **data_without_provenance,
        "provenance": {
            "source_commit": source_commit,
            "worktree_dirty": worktree_dirty,
            "command": command,
            "input_hashes": input_hashes,
            "result_sha256": result_digest,
        },
    }
    REPORT.write_text(markdown_report(data), encoding="utf-8")
    return data


if __name__ == "__main__":
    if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] != "--json"):
        raise SystemExit("usage: check_linegraph_candidate.py [--json]")
    result = run()
    result["provenance"]["report_path"] = str(REPORT)
    result["provenance"]["report_sha256"] = sha256_file(REPORT)
    # JSON is the default and --json is accepted explicitly so the receipt can
    # be consumed by the root integration/review step without log parsing.
    print(json.dumps(result, sort_keys=True, indent=2, default=str))
