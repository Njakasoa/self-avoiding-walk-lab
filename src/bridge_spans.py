"""Exact bridge and irreducible-bridge coefficients indexed by span.

The convention here is the one in :mod:`src.bridges` and ``NORMALIZATION.md``:
the root is ``(0, 0)``, every later vertex has strictly positive ``x``
coordinate, and the final ``x`` coordinate is the maximum ``x`` coordinate
visited by the path.  Thus the first step is necessarily east.  A renewal cut
at ``k`` is an internal index for which the prefix is a bridge and every later
vertex has ``x > x_k``.  The direct cut test and the bivariate renewal
inversion are both performed; disagreeing exact integers are an error.

``enumerate_bridge_spans`` is deliberately an exact enumerator.  It returns
one integer dictionary per length for bridges ``b[n][span]`` and geometrically
irreducible bridges ``i[n][span]``.  ``max_span`` restricts the terminal span
of the returned bridge family.  Since a bridge's running maximum is
nondecreasing and its terminal coordinate must equal that maximum, a branch
which exceeds this cap cannot later contribute to the capped family and is
safe to prune.
"""

from __future__ import annotations

import math
import time
from numbers import Real
from typing import Any


_DIRECTIONS: tuple[tuple[int, int], ...] = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)


def _require_nonnegative_integer(name: str, value: int) -> int:
    """Validate an integer parameter without accepting ``bool`` as ``int``."""

    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _require_seconds(value: Real) -> float:
    """Return a finite, strictly positive wall-clock budget."""

    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError("max_seconds must be a positive finite real number")
    seconds = float(value)
    if not math.isfinite(seconds) or seconds <= 0.0:
        raise ValueError("max_seconds must be a positive finite real number")
    return seconds


def _copy_sorted_rows(rows: list[dict[int, int]]) -> list[dict[int, int]]:
    """Return deterministic row dictionaries with integer keys."""

    return [dict(sorted(row.items())) for row in rows]


def _totals(rows: list[dict[int, int]]) -> list[int]:
    """Collapse span rows to the ordinary length coefficients."""

    return [sum(row.values()) for row in rows]


def _nested_rows(rows: list[dict[int, int]]) -> dict[int, dict[int, int]]:
    """Copy rows into a JSON-safe dictionary keyed first by length."""

    return {length: dict(row) for length, row in enumerate(rows)}


def _renewal_inverse_rows(
    bridge_rows: list[dict[int, int]],
) -> list[dict[int, int]]:
    """Invert ``B = 1 + I B`` over exact bivariate integer rows.

    The zero coefficient is ``b[0][0] = 1`` and all positive-length pieces
    have positive span.  Solving by increasing length therefore leaves only
    already-known rows on the right-hand side.  Missing spans are zero, so a
    span-capped enumeration is inverted in the same finite formal series.
    """

    max_n = len(bridge_rows) - 1
    irreducible_rows: list[dict[int, int]] = [{} for _ in range(max_n + 1)]
    for length in range(1, max_n + 1):
        row: dict[int, int] = {}
        for span, bridge_count in bridge_rows[length].items():
            residual = bridge_count
            # The term with k == length is i[length, span] b[0, 0],
            # so all terms below use k < length.
            for piece_length in range(1, length):
                for piece_span, piece_count in irreducible_rows[piece_length].items():
                    residual -= piece_count * bridge_rows[length - piece_length].get(
                        span - piece_span, 0
                    )
            if residual < 0:
                raise AssertionError(
                    "negative coefficient in bivariate renewal inversion "
                    f"at (n, span)=({length}, {span})"
                )
            if residual:
                row[span] = residual
        irreducible_rows[length] = row
    return irreducible_rows


def enumerate_bridge_spans(
    max_n: int,
    max_span: int | None = None,
    max_seconds: Real = 300,
) -> dict[str, Any]:
    """Enumerate exact bridge and irreducible-bridge coefficients by span.

    Parameters
    ----------
    max_n:
        Largest number of edges.  The returned rows have indices ``0`` through
        ``max_n``.
    max_span:
        Optional nonnegative terminal-span cap.  Only bridges with terminal
        span at most this value are enumerated.  ``None`` keeps every span.
        The cap is a cap on each bridge/piece's own span; it is not a filter
        applied to the span of a concatenation after the fact.
    max_seconds:
        Positive finite wall-clock budget.  A timeout raises ``TimeoutError``
        and returns no partial result, so callers cannot mistake incomplete
        rows for exact coefficients.

    Returns
    -------
    dict
        ``b_n_s`` and ``i_n_s`` are sorted lists of integer dictionaries,
        with ``b_n_s[n][s] = b_{n,s}`` and ``i_n_s[n][s] = i_{n,s}``.  The
        formal-series unit is represented by ``b_n_s[0] == {0: 1}`` and
        ``i_n_s[0] == {}``.  ``bridges`` and ``irreducibles`` are the ordinary
        totals by length.  JSON-safe ``*_dict`` aliases keyed by length,
        deterministic row aliases, and enumeration statistics are included
        for experiment scripts.

    Notes
    -----
    The direct geometric cut classification is checked against the exact
    bivariate inversion.  The direct check uses prefix-record flags and a
    reverse suffix minimum, avoiding repeated path slicing.  The DFS keeps
    the first step east and rejects nonpositive x coordinates at extension
    time; these are consequences of the bridge definition, not symmetry
    quotients.
    """

    max_n = _require_nonnegative_integer("max_n", max_n)
    if max_span is not None:
        max_span = _require_nonnegative_integer("max_span", max_span)
    seconds = _require_seconds(max_seconds)

    started = time.perf_counter()
    deadline = started + seconds
    if time.perf_counter() >= deadline:
        raise TimeoutError(
            "bridge span enumeration exceeded max_seconds; "
            "no partial coefficients are returned"
        )
    bridge_rows: list[dict[int, int]] = [{} for _ in range(max_n + 1)]
    irreducible_direct: list[dict[int, int]] = [
        {} for _ in range(max_n + 1)
    ]
    # Formal-series unit.  Positive-length bridges always have positive span.
    bridge_rows[0][0] = 1

    # A zero span cap contains the series unit and no positive-length bridge.
    if max_n == 0 or max_span == 0:
        irreducible_rows = _renewal_inverse_rows(bridge_rows)
        if time.perf_counter() >= deadline:
            raise TimeoutError(
                "bridge span enumeration exceeded max_seconds; "
                "no partial coefficients are returned"
            )
        elapsed = time.perf_counter() - started
        stats = {
            "completed": True,
            "max_n": max_n,
            "max_span": max_span,
            "max_seconds": seconds,
            "runtime_seconds": elapsed,
            "runtime": elapsed,
            "dfs_nodes": 1 if max_n else 0,
            "prefixes_by_length": [1] + [0] * max_n,
            "bridge_paths": 0,
            "irreducible_paths": 0,
            "span_pruned_extensions": 0,
            "direct_inversion_match": True,
            "strict_initial_minimum": True,
            "weak_terminal_maximum": True,
            "first_step_fixed_east": True,
        }
        b_rows = _copy_sorted_rows(bridge_rows)
        i_rows = _copy_sorted_rows(irreducible_rows)
        result: dict[str, Any] = {
            "b_n_s": b_rows,
            "i_n_s": i_rows,
            "bridge_rows": b_rows,
            "irreducible_rows": i_rows,
            "bridges": _totals(b_rows),
            "irreducibles": _totals(i_rows),
            # Keep the legacy row-0 span histogram empty while b_n_s itself
            # retains the formal coefficient b[0,0] = 1.
            "span_counts": [{}] + [dict(row) for row in b_rows[1:]],
            "b_n_s_dict": _nested_rows(b_rows),
            "i_n_s_dict": _nested_rows(i_rows),
            "stats": stats,
            "runtime_seconds": elapsed,
            "runtime": elapsed,
        }
        return result

    # Mutable state used by the recursive DFS.  The bridge condition implies
    # the first step is +x, so starting there removes three impossible root
    # branches and avoids any later orientation multiplier.
    path_x = [0, 1]
    path_y = [0, 0]
    prefix_record = [True, True]
    occupied = {(0, 0), (1, 0)}
    prefixes_by_length = [0] * (max_n + 1)
    prefixes_by_length[0] = 1
    prefixes_by_length[1] = 1
    dfs_nodes = 1
    span_pruned_extensions = 0
    bridge_paths = 0
    irreducible_paths = 0
    check_counter = 0

    def check_budget() -> None:
        nonlocal check_counter
        check_counter += 1
        # Checking every node is measurably slower at n=18.  The root and
        # every 2048th extension give a tight enough safety cap while keeping
        # the exact rows independent of the check interval.
        if check_counter == 1 or (check_counter & 2047) == 0:
            if time.perf_counter() >= deadline:
                raise TimeoutError(
                    "bridge span enumeration exceeded max_seconds; "
                    "no partial coefficients are returned"
                )

    def record_bridge(depth: int, span: int) -> None:
        nonlocal bridge_paths, irreducible_paths
        row = bridge_rows[depth]
        row[span] = row.get(span, 0) + 1
        bridge_paths += 1

        # A renewal point is a prefix record whose entire later suffix lies
        # strictly to its right.  Reverse scanning maintains the minimum of
        # x coordinates after k; prefix_record[k] stores the other condition.
        suffix_min = path_x[depth]
        is_irreducible = True
        for k in range(depth - 1, 0, -1):
            if prefix_record[k] and suffix_min > path_x[k]:
                is_irreducible = False
                break
            if path_x[k] < suffix_min:
                suffix_min = path_x[k]
        if is_irreducible:
            irow = irreducible_direct[depth]
            irow[span] = irow.get(span, 0) + 1
            irreducible_paths += 1

    def visit(x: int, y: int, depth: int, running_max: int) -> None:
        nonlocal dfs_nodes, span_pruned_extensions
        check_budget()
        if depth and x == running_max:
            record_bridge(depth, x)
        if depth == max_n:
            return

        for dx, dy in _DIRECTIONS:
            nx = x + dx
            if nx <= 0:
                continue
            if max_span is not None and nx > max_span:
                span_pruned_extensions += 1
                continue
            ny = y + dy
            nxt = (nx, ny)
            if nxt in occupied:
                continue
            occupied.add(nxt)
            path_x.append(nx)
            path_y.append(ny)
            next_depth = depth + 1
            prefixes_by_length[next_depth] += 1
            dfs_nodes += 1
            prefix_record.append(nx >= running_max)
            visit(nx, ny, next_depth, max(running_max, nx))
            prefix_record.pop()
            path_y.pop()
            path_x.pop()
            occupied.remove(nxt)

    # The initial east step is already a bridge and is irreducible.  Calling
    # visit at depth one records it uniformly with all later endpoints.
    visit(1, 0, 1, 1)

    # The direct geometric dictionary is authoritative for classification;
    # inversion supplies an independent exact algebraic check.
    if time.perf_counter() >= deadline:
        raise TimeoutError(
            "bridge span enumeration exceeded max_seconds; "
            "no partial coefficients are returned"
        )
    irreducible_rows = _renewal_inverse_rows(bridge_rows)
    direct_rows = _copy_sorted_rows(irreducible_direct)
    inverted_rows = _copy_sorted_rows(irreducible_rows)
    if time.perf_counter() >= deadline:
        raise TimeoutError(
            "bridge span enumeration exceeded max_seconds; "
            "no partial coefficients are returned"
        )
    if direct_rows != inverted_rows:
        raise AssertionError(
            "geometric irreducible rows disagree with bivariate renewal "
            "inversion"
        )

    elapsed = time.perf_counter() - started
    b_rows = _copy_sorted_rows(bridge_rows)
    i_rows = direct_rows
    stats = {
        "completed": True,
        "max_n": max_n,
        "max_span": max_span,
        "max_seconds": seconds,
        "runtime_seconds": elapsed,
        "runtime": elapsed,
        "dfs_nodes": dfs_nodes,
        "prefixes_by_length": prefixes_by_length,
        "bridge_paths": bridge_paths,
        "irreducible_paths": irreducible_paths,
        "span_pruned_extensions": span_pruned_extensions,
        "direct_inversion_match": True,
        "strict_initial_minimum": True,
        "weak_terminal_maximum": True,
        "first_step_fixed_east": True,
    }
    return {
        "b_n_s": b_rows,
        "i_n_s": i_rows,
        "bridge_rows": b_rows,
        "irreducible_rows": i_rows,
        "bridges": _totals(b_rows),
        "irreducibles": _totals(i_rows),
        # Existing enumerate_bridges uses an empty row at n=0 for its
        # histogram; preserve that compatibility alias separately from the
        # formal bivariate rows above.
        "span_counts": [{}] + [dict(row) for row in b_rows[1:]],
        "b_n_s_dict": _nested_rows(b_rows),
        "i_n_s_dict": _nested_rows(i_rows),
        "stats": stats,
        "runtime_seconds": elapsed,
        "runtime": elapsed,
    }


__all__ = ["enumerate_bridge_spans"]
