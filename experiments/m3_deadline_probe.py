"""Bounded direct BFS for the deadline-labelled finite-memory states.

The seed is one endpoint at the origin with deadline ``memory + 1``.  During
the first ``memory`` moves this is an empty-history startup presentation; the
deadline argument shows that every state on the depth-``memory`` layer is the
image of a legal full suffix.  After that layer the BFS is the closed reduced
memory automaton.  This probe is intentionally independent of the producer
automaton and uses only exact integer arithmetic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, deque
from fractions import Fraction
from time import monotonic


DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
D4 = tuple(
    (swap, sx, sy)
    for swap in (False, True)
    for sx in (-1, 1)
    for sy in (-1, 1)
)


class ResourceLimit(RuntimeError):
    """A direct case did not finish, so it has no complete matrix result."""


def _canonical(entries: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    """Canonicalize endpoint-relative deadline triples under D4."""

    variants = []
    for swap, sx, sy in D4:
        transformed = []
        for x, y, deadline in entries:
            a, b = (y, x) if swap else (x, y)
            transformed.append((sx * a, sy * b, deadline))
        variants.append(tuple(sorted(transformed)))
    return min(variants)


def _reduce_raw(path: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    """Map a raw m-edge suffix to endpoint-relative deadline triples."""

    ex, ey = path[-1]
    entries = []
    for index, (x, y) in enumerate(path):
        deadline = index + 1
        if abs(ex - x) + abs(ey - y) <= deadline:
            entries.append((x - ex, y - ey, deadline))
    return _canonical(tuple(entries))


def _advance(
    state: tuple[tuple[int, int, int], ...], memory: int, direction: tuple[int, int]
) -> tuple[tuple[int, int, int], ...] | None:
    """Apply one reduced transition, returning None for a forbidden move."""

    qx, qy = direction
    if any((x, y) == direction for x, y, _deadline in state):
        return None

    entries = [
        (x - qx, y - qy, deadline - 1)
        for x, y, deadline in state
        if deadline > 1
    ]
    entries.append((0, 0, memory + 1))
    entries = [
        (x, y, deadline)
        for x, y, deadline in entries
        if abs(x) + abs(y) <= deadline
    ]
    return _canonical(tuple(entries))


def _rows(
    states: list[tuple[tuple[int, int, int], ...]], memory: int
) -> list[dict[int, int]]:
    index = {state: i for i, state in enumerate(states)}
    result = []
    for state in states:
        row = Counter()
        for direction in DIRECTIONS:
            target = _advance(state, memory, direction)
            if target is not None:
                if target not in index:
                    raise AssertionError("closed BFS omitted a successor")
                row[index[target]] += 1
        result.append(dict(sorted(row.items())))
    return result


def _certificate(rows: list[dict[int, int]], iterations: int) -> tuple[Fraction, list[int]]:
    vector = [1] * len(rows)
    for _ in range(iterations):
        vector = [
            value + sum(weight * vector[j] for j, weight in row.items())
            for value, row in zip(vector, rows)
        ]
    image = [sum(weight * vector[j] for j, weight in row.items()) for row in rows]
    return max((Fraction(a, b) for a, b in zip(image, vector)), default=Fraction(0)), vector


def _verify_certificate(rows: list[dict[int, int]], vector: list[int], upper: Fraction) -> bool:
    if len(vector) != len(rows) or not vector or any(value <= 0 for value in vector):
        return False
    return all(
        sum(weight * vector[j] for j, weight in row.items()) <= upper * vector[i]
        for i, row in enumerate(rows)
    )


def _raw_paths(memory: int) -> list[tuple[tuple[int, int], ...]]:
    layer = [((0, 0),)]
    for _ in range(memory):
        next_layer = []
        for path in layer:
            x, y = path[-1]
            for dx, dy in DIRECTIONS:
                point = (x + dx, y + dy)
                if point not in path:
                    next_layer.append(path + (point,))
        layer = next_layer
    return layer


def _raw_row_signatures(
    paths: list[tuple[tuple[int, int], ...]], memory: int
) -> tuple[set[tuple[tuple[int, int, int], ...]], dict[tuple[tuple[int, int, int], ...], Counter], int]:
    """Return raw images, their transition signatures, and disagreement count."""

    signatures: dict[tuple[tuple[int, int, int], ...], list[tuple[tuple[tuple[int, int, int], ...], ...]]] = {}
    for path in paths:
        state = _reduce_raw(path)
        successors = []
        x, y = path[-1]
        for dx, dy in DIRECTIONS:
            point = (x + dx, y + dy)
            if point in path:
                continue
            successors.append(_reduce_raw(path[1:] + (point,)))
        signatures.setdefault(state, []).append(tuple(sorted(successors)))

    disagreements = 0
    rows: dict[tuple[tuple[int, int, int], ...], Counter] = {}
    for state, alternatives in signatures.items():
        if len(set(alternatives)) != 1:
            disagreements += 1
        rows[state] = Counter(alternatives[0])
    return set(signatures), rows, disagreements


def _build_direct_graph(
    memory: int, *, max_states: int, max_seconds: float
) -> tuple[
    list[tuple[tuple[int, int, int], ...]],
    list[dict[int, int]],
    list[tuple[tuple[int, int, int], ...]],
    list[dict[int, int]],
    list[int],
    float,
    set[tuple[tuple[int, int, int], ...]],
]:
    """Build the startup layer and closed graph from the singleton seed."""

    started = monotonic()
    seed = _canonical(((0, 0, memory + 1),))
    layer = {seed}
    layer_counts = [1]

    def check_budget(count: int) -> None:
        if count > max_states:
            raise ResourceLimit(f"state cap {max_states} exceeded")
        if monotonic() - started > max_seconds:
            raise ResourceLimit(f"time cap {max_seconds} exceeded")

    for _depth in range(memory):
        next_layer = set()
        for state in sorted(layer):
            for direction in DIRECTIONS:
                target = _advance(state, memory, direction)
                if target is not None:
                    next_layer.add(target)
                    check_budget(len(next_layer))
        layer = next_layer
        layer_counts.append(len(layer))
        check_budget(len(layer))

    # Every state at this depth is an image of a legal m-edge suffix.  Keep
    # startup states in the direct presentation as transients, then build the
    # memory-layer closure separately for the finite-memory certificate.
    memory_states = set(layer)
    states = {seed}
    queue = deque([seed])
    while queue:
        state = queue.popleft()
        for direction in DIRECTIONS:
            target = _advance(state, memory, direction)
            if target is not None and target not in states:
                states.add(target)
                queue.append(target)
                check_budget(len(states))
        check_budget(len(states))

    ordered = sorted(states)
    rows = _rows(ordered, memory)
    ordered_memory = sorted(memory_states)
    rows_memory = _rows(ordered_memory, memory)
    return (
        ordered,
        rows,
        ordered_memory,
        rows_memory,
        layer_counts,
        monotonic() - started,
        memory_states,
    )


def build_direct(
    memory: int, *, max_states: int, max_seconds: float, iterations: int
) -> dict:
    ordered, rows, ordered_memory, rows_memory, layer_counts, runtime, _startup_layer = _build_direct_graph(
        memory, max_states=max_states, max_seconds=max_seconds
    )
    upper, vector = _certificate(rows_memory, iterations)
    if not _verify_certificate(rows_memory, vector, upper):
        raise AssertionError("exact positive-vector certificate failed")
    return {
        "status": "CERTIFIED",
        "memory": memory,
        "state_count": len(ordered_memory),
        "direct_state_count": len(ordered),
        "transition_entries": sum(len(row) for row in rows),
        "memory_transition_entries": sum(len(row) for row in rows_memory),
        "startup_layer_counts": layer_counts,
        "states": ordered_memory,
        "rows": rows_memory,
        "certificate": {
            "vector": vector,
            "iterations": iterations,
            "upper": str(upper),
            "verified": True,
            "vector_sha256": hashlib.sha256(
                json.dumps(vector, separators=(",", ":")).encode()
            ).hexdigest(),
        },
        "runtime_seconds": runtime,
    }


def probe_case(
    memory: int,
    *,
    max_states: int,
    max_seconds: float,
    iterations: int,
    compare_raw: bool,
) -> dict:
    ordered, direct_rows, ordered_memory, rows_memory, layer_counts, runtime, startup_layer = _build_direct_graph(
        memory,
        max_states=max_states,
        max_seconds=max_seconds,
    )
    upper, vector = _certificate(rows_memory, iterations)
    if not _verify_certificate(rows_memory, vector, upper):
        raise AssertionError("exact positive-vector certificate failed")
    result = {
        "status": "CERTIFIED",
        "memory": memory,
        "state_count": len(ordered_memory),
        "direct_state_count": len(ordered),
        "transition_entries": sum(len(row) for row in direct_rows),
        "memory_transition_entries": sum(len(row) for row in rows_memory),
        "startup_layer_counts": layer_counts,
        "states": ordered_memory,
        "rows": rows_memory,
        "certificate": {
            "vector": vector,
            "iterations": iterations,
            "upper": str(upper),
            "verified": True,
            "vector_sha256": hashlib.sha256(
                json.dumps(vector, separators=(",", ":")).encode()
            ).hexdigest(),
        },
        "runtime_seconds": runtime,
    }
    if compare_raw:
        paths = _raw_paths(memory)
        raw_states, raw_rows, disagreements = _raw_row_signatures(paths, memory)
        direct_index = {state: i for i, state in enumerate(ordered_memory)}
        row_mismatches = 0
        for state, expected in raw_rows.items():
            index = direct_index.get(state)
            if index is None:
                row_mismatches += 1
                continue
            actual = Counter({ordered_memory[j]: weight for j, weight in rows_memory[index].items()})
            if actual != expected:
                row_mismatches += 1
        if disagreements or row_mismatches or raw_states != startup_layer:
            raise AssertionError(
                "raw/direct comparison failed: "
                f"disagreements={disagreements}, row_mismatches={row_mismatches}, "
                f"startup_equal={raw_states == startup_layer}"
            )
        result.update(
            {
                "raw_suffix_count": len(paths),
                "raw_image_state_count": len(raw_states),
                "startup_layer_state_count": len(startup_layer),
                "raw_image_equals_startup_layer": raw_states == startup_layer,
                "raw_image_subset_direct_states": raw_states <= set(ordered),
                "raw_row_disagreements": disagreements,
                "direct_row_mismatches": row_mismatches,
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-memory", type=int, default=13)
    parser.add_argument("--compare-max-memory", type=int, default=9)
    parser.add_argument("--max-states", type=int, default=100_000)
    parser.add_argument("--case-seconds", type=float, default=60.0)
    parser.add_argument("--iterations", type=int, default=60)
    args = parser.parse_args()
    if args.max_memory < 1 or args.compare_max_memory < 0:
        raise SystemExit("memory limits must be positive")

    cases = []
    for memory in range(1, args.max_memory + 1):
        try:
            cases.append(
                probe_case(
                    memory,
                    max_states=args.max_states,
                    max_seconds=args.case_seconds,
                    iterations=args.iterations,
                    compare_raw=memory <= args.compare_max_memory,
                )
            )
        except ResourceLimit as error:
            cases.append(
                {
                    "status": "RESOURCE_LIMIT",
                    "memory": memory,
                    "reason": str(error),
                }
            )

    print(
        json.dumps(
            {
                "method": "singleton-seeded direct deadline BFS",
                "parameters": vars(args),
                "cases": cases,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
