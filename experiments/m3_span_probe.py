"""Exact span-two ladder probe.

This is an experiment driver, not a production transfer matrix.  It checks
the width-two irreducible-bridge decomposition against the exact bridge
enumerator.  The univariate check defaults to ``n <= 30``; a second small
DFS keeps horizontal and vertical step counts separately and checks the
bivariate formula.

The bridge convention is the strict-positive-x / weak-terminal-maximum
convention documented in ``NORMALIZATION.md`` and ``proofs/BRIDGE_SPANS.md``.
No coefficient fit is used: the expected coefficients are generated from the
explicit ladder decomposition in ``M3_SPAN_STRUCTURE_NOTES.md``.
"""

from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from fractions import Fraction
from typing import DefaultDict

from src.bridge_spans import enumerate_bridge_spans


def _poly_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    result = [0] * size
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return result


def _poly_mul(left: list[int], right: list[int], degree: int) -> list[int]:
    result = [0] * (degree + 1)
    for i, left_value in enumerate(left):
        if left_value == 0:
            continue
        for j, right_value in enumerate(right):
            if right_value == 0 or i + j > degree:
                continue
            result[i + j] += left_value * right_value
    return result


def _ladder_vertical_factors(degree: int) -> tuple[list[int], list[int], list[int]]:
    """Return ``A``, ``T`` and ``L`` through the requested vertical degree.

    ``A`` is one positive vertical run.  ``T`` handles the initial run and
    the first return to column one.  ``L`` handles the final run and its weak
    terminal vertical tail.  These are direct finite sums, so this routine
    does not infer a recurrence from data.
    """

    a = [0] * (degree + 1)
    for length in range(1, degree + 1):
        a[length] = 1

    # T = 2 A + 2 A^2 + 2 sum_{alpha>=1,beta>=alpha+1} v^(alpha+beta).
    t = [0] * (degree + 1)
    t = _poly_add(t, [2 * value for value in a])
    t = _poly_add(t, [2 * value for value in _poly_mul(a, a, degree)])
    for alpha in range(1, degree + 1):
        for beta in range(alpha + 1, degree + 1):
            if alpha + beta <= degree:
                t[alpha + beta] += 2

    # For a last column-one run of length c, the terminal column-two tail has
    # one outward choice for every t>=0 and one inward choice for 1<=t<c.
    l = [0] * (degree + 1)
    for c in range(1, degree + 1):
        for tail in range(0, degree - c + 1):
            l[c + tail] += 1
        for tail in range(1, c):
            if c + tail <= degree:
                l[c + tail] += 1
    return a, t, l


def expected_weighted(max_n: int) -> dict[int, dict[int, int]]:
    """Generate exact ``(horizontal, vertical)`` coefficients from the proof.

    If ``r >= 1`` is the number of W/E return pairs after the first 1->2
    crossing, then the horizontal degree is ``2 + 2*r``.  The vertical factor
    is ``T L (A^2)^(r-1)``.
    """

    a, t, l = _ladder_vertical_factors(max_n)
    result: DefaultDict[int, dict[int, int]] = defaultdict(dict)
    a2 = _poly_mul(a, a, max_n)
    continuation = [1] + [0] * max_n
    for r in range(1, (max_n - 2) // 2 + 1):
        vertical = _poly_mul(_poly_mul(t, l, max_n), continuation, max_n)
        horizontal = 2 + 2 * r
        for vertical_degree, count in enumerate(vertical):
            if count and horizontal + vertical_degree <= max_n:
                result[horizontal][vertical_degree] = count
        continuation = _poly_mul(continuation, a2, max_n)
    return {h: dict(sorted(row.items())) for h, row in sorted(result.items())}


def enumerate_weighted(max_n: int, deadline: float) -> dict[int, dict[int, int]]:
    """Enumerate capped width-two irreducibles, retaining H/V degrees."""

    path_x = [0, 1]
    path_y = [0, 0]
    occupied = {(0, 0), (1, 0)}
    counts: DefaultDict[int, dict[int, int]] = defaultdict(dict)
    checks = 0

    def budget() -> None:
        nonlocal checks
        checks += 1
        if checks == 1 or (checks & 2047) == 0:
            if time.perf_counter() >= deadline:
                raise TimeoutError("weighted span-two probe exceeded max_seconds")

    def record(horizontal: int, vertical: int) -> None:
        xs = path_x
        # The direct renewal test is deliberately repeated here rather than
        # inferred from the expected language.
        irreducible = True
        for k in range(1, len(xs) - 1):
            if xs[k] == max(xs[: k + 1]) and all(value > xs[k] for value in xs[k + 1 :]):
                irreducible = False
                break
        if irreducible:
            row = counts[horizontal]
            row[vertical] = row.get(vertical, 0) + 1

    def visit(x: int, y: int, depth: int, horizontal: int, vertical: int) -> None:
        budget()
        if depth and x == 2:
            record(horizontal, vertical)
        if depth == max_n:
            return
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if nx <= 0 or nx > 2:
                continue
            point = (nx, ny)
            if point in occupied:
                continue
            occupied.add(point)
            path_x.append(nx)
            path_y.append(ny)
            visit(
                nx,
                ny,
                depth + 1,
                horizontal + int(dx != 0),
                vertical + int(dy != 0),
            )
            path_y.pop()
            path_x.pop()
            occupied.remove(point)

    visit(1, 0, 1, 1, 0)
    return {h: dict(sorted(row.items())) for h, row in sorted(counts.items())}


def _univariate(rows: dict[int, dict[int, int]], max_n: int) -> list[int]:
    values = [0] * (max_n + 1)
    for horizontal, row in rows.items():
        for vertical, count in row.items():
            if horizontal + vertical <= max_n:
                values[horizontal + vertical] += count
    return values


def _solve_unique(rows: list[list[Fraction]], order: int) -> list[Fraction] | None:
    """Solve an exact recurrence fit only when its coefficient vector is unique."""

    if not rows:
        return None
    matrix = [row[:] for row in rows]
    row_count = len(matrix)
    pivot_row = 0
    pivots: list[tuple[int, int]] = []
    for column in range(order):
        pivot = next(
            (row for row in range(pivot_row, row_count) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                left - scale * right
                for left, right in zip(matrix[row], matrix[pivot_row])
            ]
        pivots.append((pivot_row, column))
        pivot_row += 1
    if any(
        all(value == 0 for value in row[:order]) and row[order] != 0
        for row in matrix
    ):
        return None
    if len(pivots) != order:
        return None
    solution = [Fraction(0) for _ in range(order)]
    for row, column in pivots:
        solution[column] = matrix[row][order]
    return solution


def recurrence_screen(
    values: list[int],
    *,
    transient_start: int = 6,
    train_end: int = 21,
    max_order: int = 12,
) -> dict:
    """Fit an exact finite-transient recurrence and test held-out values."""

    holdout_start = train_end + 1
    if len(values) - holdout_start < 4:
        raise ValueError("recurrence screen needs at least four held-out terms")
    for order in range(1, max_order + 1):
        first = transient_start + order
        if first > train_end:
            continue
        rows = [
            [Fraction(values[n - j]) for j in range(1, order + 1)]
            + [Fraction(values[n])]
            for n in range(first, train_end + 1)
        ]
        coefficients = _solve_unique(rows, order)
        if coefficients is None:
            continue
        predictions = {}
        predicted = [Fraction(value) for value in values[:holdout_start]]
        for n in range(holdout_start, len(values)):
            value = sum(coefficients[j] * predicted[n - 1 - j] for j in range(order))
            predictions[n] = value
            predicted.append(value)
        holds = all(predictions[n] == values[n] for n in predictions)
        if holds:
            return {
                "status": "exact_fit_and_holdout",
                "transient_start": transient_start,
                "train_end": train_end,
                "holdout_start": holdout_start,
                "holdout_end": len(values) - 1,
                "held_out_terms": len(predictions),
                "order": order,
                "coefficients": [str(value) for value in coefficients],
                "holdout_match": True,
                "interpretation": (
                    "diagnostic recurrence; the ladder decomposition is the proof"
                ),
            }
    raise AssertionError("no unique recurrence of order <= max_order passed holdout")


def run(max_n: int = 30, weighted_max_n: int = 18, max_seconds: float = 60.0) -> dict:
    """Run exact univariate and bivariate checks under one wall-clock cap."""

    if type(max_n) is not int or max_n < 1:
        raise ValueError("max_n must be a positive integer")
    if type(weighted_max_n) is not int or weighted_max_n < 1:
        raise ValueError("weighted_max_n must be a positive integer")
    if weighted_max_n > max_n:
        raise ValueError("weighted_max_n cannot exceed max_n")
    if type(max_seconds) not in (int, float) or max_seconds <= 0:
        raise ValueError("max_seconds must be positive")

    started = time.perf_counter()
    deadline = started + float(max_seconds)
    exact = enumerate_bridge_spans(
        max_n,
        max_span=2,
        max_seconds=max(0.01, deadline - time.perf_counter()),
    )
    observed_univariate = [row.get(2, 0) for row in exact["i_n_s"]]
    expected_all = expected_weighted(max_n)
    expected_univariate = _univariate(expected_all, max_n)
    if observed_univariate != expected_univariate:
        raise AssertionError("span-two univariate coefficients disagree")
    recurrence = recurrence_screen(observed_univariate)

    weighted_deadline = deadline
    observed_weighted = enumerate_weighted(weighted_max_n, weighted_deadline)
    expected_small = expected_weighted(weighted_max_n)
    if observed_weighted != expected_small:
        raise AssertionError("span-two H/V coefficients disagree")

    elapsed = time.perf_counter() - started
    if elapsed > max_seconds:
        raise TimeoutError("span-two probe exceeded max_seconds")
    return {
        "status": "complete",
        "classification": "EXACT INTEGER; explicit ladder decomposition check",
        "max_n": max_n,
        "weighted_max_n": weighted_max_n,
        "max_span": 2,
        "runtime_seconds": elapsed,
        "enumerator_stats": exact["stats"],
        "i_span2": observed_univariate,
        "weighted_i_span2": observed_weighted,
        "formula": {
            "A": "v/(1-v)",
            "T": "2*v*(1+v+v^2)/((1-v)^2*(1+v))",
            "L": "v*(1+v+v^2)/((1-v)^2*(1+v))",
            "I2": "2*u^4*v^2*(1+v+v^2)^2/((1-v)^2*(1+v)^2*((1-v)^2-u^2*v^2))",
            "univariate": "2*z^6*(1+z+z^2)^2/((1-z)^2*(1+z)^2*((1-z)^2-z^4))",
        },
        "checks": {
            "direct_vs_inversion": exact["stats"]["direct_inversion_match"],
            "univariate_formula": True,
            "weighted_formula": True,
            "recurrence_holdout": recurrence["holdout_match"],
            "weak_terminal_tail_included": True,
        },
        "recurrence_screen": recurrence,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=30)
    parser.add_argument("--weighted-max-n", type=int, default=18)
    parser.add_argument("--max-seconds", type=float, default=60.0)
    args = parser.parse_args()
    print(
        json.dumps(
            run(args.max_n, args.weighted_max_n, args.max_seconds),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
