"""Bounded E2 experiment: bridge dictionaries indexed by length and span.

This driver is intentionally separate from the exact enumerator.  It runs the
predefined length/span-cap grid, turns each completed irreducible dictionary
into a rational renewal lower certificate, reports nesting and measured DFS
cost, and then performs a small held-out recurrence screen.  A recurrence is
an empirical falsification probe: its coefficients are fitted only on
``n <= 14`` and predictions for ``n = 15..18`` are retained whether or not
they agree.  No fitted recurrence is used as a certificate.

Canonical runs should be launched after committing all input files, for
example::

    PYTHONPATH=. .venv/bin/python experiments/e2_spans.py e2-spans-v1

``src.provenance.run_record`` refuses a dirty source file and records the
source commit and input/output hashes.  During development, ``produce()`` can
be called directly; it returns the same JSON-safe payload without writing a
receipt.
"""

from __future__ import annotations

import sys
import time
from fractions import Fraction
from typing import Any, Iterable

try:
    import resource
except ImportError:  # pragma: no cover - the canonical runner is POSIX.
    resource = None  # type: ignore[assignment]

from src.bridge_spans import enumerate_bridge_spans
from src.bridges import lower_certificate
from src.provenance import run_record


LENGTHS: tuple[int, ...] = (12, 14, 16, 18)
SPAN_CAPS: tuple[int | None, ...] = (1, 2, 3, 4, None)
CASE_SECONDS = 300.0
RECURRENCE_TRAIN_END = 14
RECURRENCE_HOLDOUT = tuple(range(15, 19))
EXACT_SPAN_FAMILIES: tuple[int, ...] = (1, 2, 3, 4)
CUMULATIVE_SPAN_FAMILIES: tuple[int, ...] = (1, 2, 3, 4)


SOURCE_MANIFEST: tuple[str, ...] = (
    "experiments/e2_spans.py",
    "src/bridge_spans.py",
    "src/bridges.py",
    "src/provenance.py",
    "NORMALIZATION.md",
    "environment/NEXT_GOAL_BRIEF.md",
    "proofs/BRIDGE_RENEWAL.md",
    "proofs/BRIDGE_SPANS.md",
    "requirements-lock.txt",
)


def _fraction_text(value: Fraction) -> str:
    """Use the canonical integer spelling for denominator-one fractions."""

    return str(value)


def _case_parameters() -> Iterable[tuple[int, int | None]]:
    for max_n in LENGTHS:
        for max_span in SPAN_CAPS:
            yield max_n, max_span


def _process_peak_rss_kib() -> int | None:
    """Read this producer process's cumulative peak RSS when available."""

    if resource is None:
        return None
    # Linux reports KiB; macOS reports bytes.  The managed runner is Linux,
    # but retaining the platform branch keeps the receipt label honest.
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform == "darwin":
        return value // 1024
    return value


def _canonical_case(result: dict[str, Any]) -> dict[str, Any]:
    """Keep exact rows and stats while dropping redundant API aliases."""

    return {
        "b_n_s": result["b_n_s"],
        "i_n_s": result["i_n_s"],
        "bridges": result["bridges"],
        "irreducibles": result["irreducibles"],
        "stats": result["stats"],
    }


def _run_case(max_n: int, max_span: int | None) -> dict[str, Any]:
    """Run one independently timed case, with no exact payload on timeout."""

    started = time.perf_counter()
    rss_before = _process_peak_rss_kib()
    try:
        result = enumerate_bridge_spans(
            max_n,
            max_span=max_span,
            max_seconds=CASE_SECONDS,
        )
    except TimeoutError as exc:
        elapsed = time.perf_counter() - started
        rss_after = _process_peak_rss_kib()
        return {
            "max_n": max_n,
            "max_span": max_span,
            "status": "timeout",
            "classification": "INCOMPLETE / NO EXACT OUTPUT",
            "runtime_seconds": elapsed,
            "max_seconds": CASE_SECONDS,
            "timeout_scope": "enumerator DFS/inversion; no coefficient payload returned",
            "peak_rss_kib_process_cumulative_before": rss_before,
            "peak_rss_kib_process_cumulative_after": rss_after,
            "peak_rss_scope": "same producer process cumulative high-water mark",
            "error": str(exc),
        }

    exact = _canonical_case(result)
    irreducibles = exact["irreducibles"]
    certificate = lower_certificate(irreducibles, bits=64)
    elapsed = time.perf_counter() - started
    if elapsed > CASE_SECONDS:
        # This should be unreachable for the predefined grid, but do not
        # label a post-enumeration over-budget result exact.
        rss_after = _process_peak_rss_kib()
        return {
            "max_n": max_n,
            "max_span": max_span,
            "status": "timeout",
            "classification": "INCOMPLETE / NO EXACT OUTPUT",
            "runtime_seconds": elapsed,
            "max_seconds": CASE_SECONDS,
            "timeout_scope": "enumeration plus rational certificate wall clock",
            "peak_rss_kib_process_cumulative_before": rss_before,
            "peak_rss_kib_process_cumulative_after": rss_after,
            "peak_rss_scope": "same producer process cumulative high-water mark",
            "error": "case exceeded max_seconds after certificate computation",
        }
    rss_after = _process_peak_rss_kib()
    dictionary_terms = sum(
        1 for row in exact["i_n_s"] for count in row.values() if count
    )
    dictionary_weight = sum(irreducibles)
    return {
        "max_n": max_n,
        "max_span": max_span,
        "status": "complete",
        "classification": "EXACT INTEGER + RIGOROUS INTERVAL",
        "runtime_seconds": elapsed,
        "max_seconds": CASE_SECONDS,
        "timeout_scope": "enumeration plus rational certificate wall clock",
        "peak_rss_kib_process_cumulative_before": rss_before,
        "peak_rss_kib_process_cumulative_after": rss_after,
        "peak_rss_scope": "same producer process cumulative high-water mark; per-case deltas are diagnostic only",
        "dictionary_terms": dictionary_terms,
        "dictionary_weight": dictionary_weight,
        "certificate": certificate,
        **exact,
    }


def _completed_cases(
    cases: list[dict[str, Any]],
) -> dict[tuple[int, int | None], dict[str, Any]]:
    return {
        (case["max_n"], case["max_span"]): case
        for case in cases
        if case["status"] == "complete"
    }


def _fraction_row(row: dict[Any, Any]) -> dict[int, int]:
    """Normalize JSON-loaded or in-memory row keys for exact comparisons."""

    return {int(span): int(count) for span, count in row.items()}


def _nesting_report(cases: list[dict[str, Any]]) -> dict[str, Any]:
    """Check cap nesting and list same-length cost/time comparisons."""

    by_key = _completed_cases(cases)
    same_length: dict[str, list[dict[str, Any]]] = {}
    nesting: dict[str, dict[str, bool]] = {}

    for max_n in LENGTHS:
        rows = []
        for cap in SPAN_CAPS:
            case = by_key.get((max_n, cap))
            if case is None:
                continue
            certificate = case["certificate"]
            rows.append(
                {
                    "max_span": cap,
                    "runtime_seconds": case["runtime_seconds"],
                    "dfs_nodes": case["stats"]["dfs_nodes"],
                    "dictionary_terms": case["dictionary_terms"],
                    "dictionary_weight": case["dictionary_weight"],
                    "lower": certificate["lower"],
                    "lower_decimal_display": certificate["lower_decimal_display"],
                }
            )
        same_length[str(max_n)] = rows

        for left, right in zip(SPAN_CAPS, SPAN_CAPS[1:]):
            a = by_key.get((max_n, left))
            b = by_key.get((max_n, right))
            if a is None or b is None:
                continue
            bridge_left_rows = a["b_n_s"]
            bridge_right_rows = b["b_n_s"]
            left_rows = a["i_n_s"]
            right_rows = b["i_n_s"]
            # A span cap is a filter on the same exact irreducible rows, so
            # every retained coefficient must be identical and every retained
            # span key must remain present in the larger cap.
            coefficient_subset = all(
                all(
                    _fraction_row(left_rows[n]).get(span, 0)
                    == _fraction_row(right_rows[n]).get(span, 0)
                    for span in _fraction_row(left_rows[n])
                )
                and set(_fraction_row(left_rows[n]))
                <= set(_fraction_row(right_rows[n]))
                for n in range(max_n + 1)
            )
            bridge_coefficient_subset = all(
                all(
                    _fraction_row(bridge_left_rows[n]).get(span, 0)
                    == _fraction_row(bridge_right_rows[n]).get(span, 0)
                    for span in _fraction_row(bridge_left_rows[n])
                )
                and set(_fraction_row(bridge_left_rows[n]))
                <= set(_fraction_row(bridge_right_rows[n]))
                for n in range(max_n + 1)
            )
            lower_monotone = Fraction(a["certificate"]["lower"]) <= Fraction(
                b["certificate"]["lower"]
            )
            nesting[f"{max_n}:{left}->{right}"] = {
                "bridge_coefficient_subset": bridge_coefficient_subset,
                "coefficient_subset": coefficient_subset,
                "lower_monotone": lower_monotone,
            }
            if not bridge_coefficient_subset or not coefficient_subset or not lower_monotone:
                raise AssertionError(
                    f"span dictionaries are not nested at n={max_n}: "
                    f"{left!r} -> {right!r}"
                )

    return {
        "cost_metric": "completed DFS prefix nodes",
        "same_length_comparisons": same_length,
        "nesting": nesting,
    }


def _rank(matrix: list[list[Fraction]]) -> tuple[int, bool]:
    """Return exact row rank and whether the augmented system is consistent."""

    if not matrix:
        return 0, True
    rows = [row[:] for row in matrix]
    columns = len(rows[0]) - 1
    pivot_row = 0
    pivot_columns: list[int] = []
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                left - factor * right
                for left, right in zip(rows[row], rows[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    consistent = not any(
        all(entry == 0 for entry in row[:columns]) and row[columns] != 0
        for row in rows
    )
    return len(pivot_columns), consistent


def _solve_unique(matrix: list[list[Fraction]], order: int) -> list[Fraction] | None:
    """Solve an exact recurrence system only when its coefficient fit is unique."""

    if not matrix:
        return None
    rank, consistent = _rank(matrix)
    if not consistent or rank != order:
        return None

    rows = [row[:] for row in matrix]
    pivot_row = 0
    pivots: list[tuple[int, int]] = []
    for column in range(order):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                left - factor * right
                for left, right in zip(rows[row], rows[pivot_row])
            ]
        pivots.append((pivot_row, column))
        pivot_row += 1

    # Every variable has a pivot because rank == order.  Read the solution
    # only after the complete RREF pass: eliminating later columns can change
    # the right-hand side of an earlier pivot row.
    solution = [Fraction(0) for _ in range(order)]
    for row, column in pivots:
        solution[column] = rows[row][-1]
    if any(
        sum(coefficient * value for coefficient, value in zip(row, solution))
        != row[-1]
        for row in matrix
    ):
        raise AssertionError("exact recurrence solver failed its own fit check")
    return solution


def _fit_recurrence(values: list[int]) -> dict[str, Any]:
    """Fit the first unique order <=5 on n=1..14, or preserve a failure."""

    training = values[1 : RECURRENCE_TRAIN_END + 1]
    for order in range(1, 6):
        if len(training) <= order:
            continue
        matrix: list[list[Fraction]] = []
        # Sequence index j corresponds to physical length n=j+1.  Start at
        # j=order so every equation uses only training values.
        for j in range(order, len(training)):
            matrix.append(
                [
                    Fraction(training[j - offset])
                    for offset in range(1, order + 1)
                ]
                + [Fraction(training[j])]
            )
        coefficients = _solve_unique(matrix, order)
        if coefficients is None:
            continue

        predicted: dict[str, Any] = {}
        work = [Fraction(value) for value in values[: RECURRENCE_TRAIN_END + 1]]
        all_match = True
        for n in RECURRENCE_HOLDOUT:
            estimate = sum(
                coefficients[offset - 1] * work[n - offset]
                for offset in range(1, order + 1)
            )
            expected = values[n]
            match = estimate == expected
            all_match = all_match and match
            predicted[str(n)] = {
                "predicted": _fraction_text(estimate),
                "expected": expected,
                "match": match,
                "predicted_integer": estimate.denominator == 1,
            }
            work.append(estimate)
        return {
            "status": "unique_fit",
            "order": order,
            "coefficients": [_fraction_text(value) for value in coefficients],
            "training_range": [1, RECURRENCE_TRAIN_END],
            "holdout_range": [RECURRENCE_HOLDOUT[0], RECURRENCE_HOLDOUT[-1]],
            "predictions": predicted,
            "all_holdout_match": all_match,
            "classification": "FALSIFICATION SCREEN / EMPIRICAL",
        }

    return {
        "status": "no_unique_fit_order_le_5",
        "order_limit": 5,
        "training_range": [1, RECURRENCE_TRAIN_END],
        "holdout_range": [RECURRENCE_HOLDOUT[0], RECURRENCE_HOLDOUT[-1]],
        "classification": "FALSIFICATION SCREEN / EMPIRICAL",
    }


def _recurrence_report(cases: list[dict[str, Any]]) -> dict[str, Any]:
    """Mine predefined exact-span and cumulative-span families."""

    by_key = _completed_cases(cases)
    full = by_key.get((max(LENGTHS), None))
    if full is None:
        return {
            "status": "blocked_by_timeout",
            "classification": "FALSIFICATION SCREEN / EMPIRICAL",
            "training_range": [1, RECURRENCE_TRAIN_END],
            "holdout_range": [RECURRENCE_HOLDOUT[0], RECURRENCE_HOLDOUT[-1]],
        }

    families: list[dict[str, Any]] = []
    for span in EXACT_SPAN_FAMILIES:
        values = [
            _fraction_row(full["i_n_s"][n]).get(span, 0)
            for n in range(max(LENGTHS) + 1)
        ]
        families.append(
            {
                "family": "exact_span",
                "span": span,
                "values": values,
                "fit": _fit_recurrence(values),
            }
        )

    for span_cap in CUMULATIVE_SPAN_FAMILIES:
        values = [
            sum(
                count
                for span, count in _fraction_row(full["i_n_s"][n]).items()
                if span <= span_cap
            )
            for n in range(max(LENGTHS) + 1)
        ]
        families.append(
            {
                "family": "cumulative_span",
                "max_span": span_cap,
                "values": values,
                "fit": _fit_recurrence(values),
            }
        )
    return {
        "status": "complete",
        "classification": "FALSIFICATION SCREEN / EMPIRICAL",
        "training_range": [1, RECURRENCE_TRAIN_END],
        "holdout_range": [RECURRENCE_HOLDOUT[0], RECURRENCE_HOLDOUT[-1]],
        "families": families,
        "fit_policy": "smallest unique exact fit of order <=5; failed fits and held-out mismatches are retained",
    }


def _self_check_recurrence_solver() -> None:
    """Exercise the exact solver on a known order-two fit with two nonzero terms."""

    values = [0, 1, 2]
    for _ in range(3, max(LENGTHS) + 1):
        values.append(2 * values[-1] + 3 * values[-2])
    fit = _fit_recurrence(values)
    assert fit["status"] == "unique_fit"
    assert fit["order"] == 2
    assert fit["coefficients"] == ["2", "3"]
    assert fit["all_holdout_match"] is True


def produce() -> dict[str, Any]:
    """Run all predefined E2 cases and return a JSON-safe experiment payload."""

    _self_check_recurrence_solver()
    cases = [_run_case(max_n, max_span) for max_n, max_span in _case_parameters()]
    report = _nesting_report(cases)
    recurrence = _recurrence_report(cases)
    return {
        "experiment": "E2 bridge span dictionaries",
        "classification": "EXACT INTEGER / RIGOROUS INTERVAL / FALSIFICATION SCREEN",
        "parameters": {
            "lengths": list(LENGTHS),
            "span_caps": list(SPAN_CAPS),
            "case_max_seconds": CASE_SECONDS,
            "renewal_certificate_bits": 64,
            "recurrence_train_end": RECURRENCE_TRAIN_END,
            "recurrence_holdout": list(RECURRENCE_HOLDOUT),
            "recurrence_order_limit": 5,
            "exact_span_families": list(EXACT_SPAN_FAMILIES),
            "cumulative_span_families": list(CUMULATIVE_SPAN_FAMILIES),
        },
        "source_manifest": list(SOURCE_MANIFEST),
        "cases": cases,
        "comparisons": report,
        "recurrence_screen": recurrence,
        "scientific_scope": {
            "dictionary_bound": "Each completed irreducible dictionary gives a lower bound for unrestricted square-lattice SAWs by free concatenation.",
            "capped_bridge_warning": "A cap on total bridge span is not substituted for an untruncated scalar renewal series.",
            "recurrence_status": "Empirical falsification only; no fitted recurrence is used as a certificate or novelty claim.",
        },
    }


if __name__ == "__main__":
    experiment_id = sys.argv[1] if len(sys.argv) > 1 else "e2-spans-v1"
    print(
        run_record(
            experiment_id,
            f"PYTHONPATH=. .venv/bin/python experiments/e2_spans.py {experiment_id}",
            {
                "lengths": list(LENGTHS),
                "span_caps": list(SPAN_CAPS),
                "case_max_seconds": CASE_SECONDS,
                "recurrence_train_end": RECURRENCE_TRAIN_END,
                "recurrence_holdout": list(RECURRENCE_HOLDOUT),
            },
            SOURCE_MANIFEST,
            produce,
        )
    )
