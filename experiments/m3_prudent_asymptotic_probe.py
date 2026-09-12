"""Bounded high-index numerical probe for the Bacher--Beaton prudent poles.

The existing kernel, evaluation formula, and pole locator are reused without
modification.  For each selected index ell, the script solves the truncated
equation P_N(t) = -1 between the consecutive poles a_ell and a_(ell+1), then
repeats with doubled summand counts.  The output is numerical evidence only:
the infinite iterated sum, the all-index pole family, and noncancellation are
not certified here.

The useful scaled observables are

    phase_ell = (r_ell-a_ell)/(a_(ell+1)-a_ell)

and the hook value 1 + H(r_ell).  The last-term magnitude and successive
drifts are retained because q^(2n) approaches one as ell grows.
"""

from __future__ import annotations

import argparse
import json
import time
from typing import Any, Iterable

import mpmath as mp

from experiments.m3_prudent_singularity_probe import evaluate, kernel, pole


DEFAULT_INDICES = (8, 16, 32)
DEFAULT_TERMS = (400, 800, 1600, 3200)
DEFAULT_DPS = 100
DEFAULT_POLE_DPS = 120
DEFAULT_BISECTION = 52


def _s(value: mp.mpf, digits: int = 60) -> str:
    """Stable decimal rendering for a numerical receipt."""

    return mp.nstr(value, digits)


def _mp(value: str | mp.mpf | int | float) -> mp.mpf:
    return mp.mpf(value)


def _remaining(deadline: float) -> None:
    if time.perf_counter() >= deadline:
        raise TimeoutError("prudent asymptotic probe exceeded max_seconds")


def _p_plus_one(t: mp.mpf, terms: int, dps: int) -> mp.mpf:
    return _mp(evaluate(t, terms=terms, dps=dps)["P"]) + 1


def _root_for_terms(
    left_pole: mp.mpf,
    right_pole: mp.mpf,
    terms: int,
    dps: int,
    *,
    bisection_steps: int,
    deadline: float,
) -> dict[str, Any]:
    """Locate a root of the truncated P_N+1 in one pole interval."""

    width = right_pole - left_pole
    # Keep a small margin from the poles, where the finite truncation is least
    # reliable.  The signs are checked rather than assumed.
    low = left_pole + width * mp.mpf("0.001")
    high = left_pole + width * mp.mpf("0.999")
    f_low = _p_plus_one(low, terms, dps)
    f_high = _p_plus_one(high, terms, dps)
    if not f_low < 0 < f_high:
        raise ArithmeticError(
            f"truncated root was not bracketed at terms={terms}: "
            f"P(low)+1={_s(f_low, 20)}, P(high)+1={_s(f_high, 20)}"
        )
    for _ in range(bisection_steps):
        _remaining(deadline)
        middle = (low + high) / 2
        if _p_plus_one(middle, terms, dps) < 0:
            low = middle
        else:
            high = middle
    root = (low + high) / 2
    result = evaluate(root, terms=terms, dps=dps)
    return {
        "terms": terms,
        "dps": dps,
        "root": _s(root),
        "phase": _s((root - left_pole) / width),
        "P_plus_one": _s(_mp(result["P"]) + 1),
        "H_plus_one": _s(_mp(result["hook"]) + 1),
        "last_term_magnitude": _s(_mp(result["last_term_magnitude"])),
        "double_precision_input_terms": result["terms"],
    }


def _drift(rows: list[dict[str, Any]], key: str) -> list[dict[str, str]]:
    """Return successive absolute drifts for a selected observable."""

    output: list[dict[str, str]] = []
    for previous, current in zip(rows, rows[1:]):
        delta = abs(_mp(current[key]) - _mp(previous[key]))
        output.append(
            {
                "from_terms": str(previous["terms"]),
                "to_terms": str(current["terms"]),
                "observable": key,
                "absolute_drift": _s(delta),
            }
        )
    return output


def _linear_limit(rows: list[dict[str, Any]], key: str, indices: list[int]) -> str | None:
    """Heuristic 1/ell extrapolation from the last two high-index rows."""

    if len(rows) < 2:
        return None
    previous = _mp(rows[-2][key])
    current = _mp(rows[-1][key])
    # y_ell = c + d/ell gives c = y_ell + (y_ell-y_prev)/(ell/ell_prev-1).
    ratio = mp.mpf(indices[-1]) / indices[-2]
    return _s(current + (current - previous) / (ratio - 1))


def run(
    indices: Iterable[int] = DEFAULT_INDICES,
    terms_schedule: Iterable[int] = DEFAULT_TERMS,
    *,
    dps: int = DEFAULT_DPS,
    pole_dps: int = DEFAULT_POLE_DPS,
    bisection_steps: int = DEFAULT_BISECTION,
    max_seconds: float = 300.0,
) -> dict[str, Any]:
    """Run the bounded root/phase/convergence sweep."""

    selected = [int(index) for index in indices]
    terms = [int(value) for value in terms_schedule]
    if not selected or any(index < 0 for index in selected):
        raise ValueError("indices must be a nonempty list of nonnegative integers")
    if selected != sorted(set(selected)):
        raise ValueError("indices must be strictly increasing")
    if not terms or any(value < 1 for value in terms):
        raise ValueError("terms_schedule must be a nonempty list of positive integers")
    if terms != sorted(set(terms)):
        raise ValueError("terms_schedule must be strictly increasing")
    if type(dps) is not int or dps < 30:
        raise ValueError("dps must be an integer >= 30")
    if type(pole_dps) is not int or pole_dps < dps:
        raise ValueError("pole_dps must be >= dps")
    if type(bisection_steps) is not int or bisection_steps < 10:
        raise ValueError("bisection_steps must be >= 10")
    if type(max_seconds) not in (int, float) or max_seconds <= 0:
        raise ValueError("max_seconds must be positive")

    # Pole coordinates are returned at pole_dps precision.  Keep that
    # precision active for interval arithmetic and bisection; otherwise
    # mpmath would restore its process-default precision after the pole
    # context and silently round the root coordinates.
    mp.mp.dps = pole_dps
    started = time.perf_counter()
    deadline = started + float(max_seconds)
    with mp.workdps(pole_dps):
        sigma = mp.sqrt(2) - 1
        pole_map: dict[int, mp.mpf] = {}
        for index in selected:
            _remaining(deadline)
            pole_map[index] = pole(index, pole_dps)
            pole_map[index + 1] = pole(index + 1, pole_dps)

    cases: list[dict[str, Any]] = []
    for index in selected:
        _remaining(deadline)
        left_pole = pole_map[index]
        right_pole = pole_map[index + 1]
        width = right_pole - left_pole
        midpoint = (left_pole + right_pole) / 2
        with mp.workdps(pole_dps):
            q_mid = kernel(midpoint, 1)
            epsilon_mid = -mp.log(q_mid * q_mid)
        rows: list[dict[str, Any]] = []
        for summands in terms:
            _remaining(deadline)
            rows.append(
                _root_for_terms(
                    left_pole,
                    right_pole,
                    summands,
                    dps,
                    bisection_steps=bisection_steps,
                    deadline=deadline,
                )
            )
        cases.append(
            {
                "ell": index,
                "left_pole": _s(left_pole),
                "right_pole": _s(right_pole),
                "pole_gap": _s(width),
                "sigma_minus_left_pole": _s(sigma - left_pole),
                "midpoint_q": _s(q_mid),
                "midpoint_epsilon_minus_log_q2": _s(epsilon_mid),
                "rows": rows,
                "phase_drift": _drift(rows, "phase"),
                "H_plus_one_drift": _drift(rows, "H_plus_one"),
                "last_term_drift": _drift(rows, "last_term_magnitude"),
                "final_phase": rows[-1]["phase"],
                "final_H_plus_one": rows[-1]["H_plus_one"],
                "final_H_plus_one_sign": "positive"
                if _mp(rows[-1]["H_plus_one"]) > 0
                else "nonpositive",
            }
        )

    final_phases = [case["final_phase"] for case in cases]
    final_hooks = [case["final_H_plus_one"] for case in cases]
    heuristic_indices = [case["ell"] for case in cases]
    elapsed = time.perf_counter() - started
    if elapsed > max_seconds:
        raise TimeoutError("prudent asymptotic probe exceeded max_seconds")
    return {
        "classification": "EXPLORATORY NUMERIC ONLY",
        "status": "complete",
        "max_seconds": max_seconds,
        "runtime_seconds": elapsed,
        "indices": selected,
        "terms_schedule": terms,
        "dps": dps,
        "pole_dps": pole_dps,
        "bisection_steps": bisection_steps,
        "sigma": _s(sigma),
        "cases": cases,
        "heuristic_1_over_ell_extrapolation": {
            "phase_limit": _linear_limit(
                [{"phase": value} for value in final_phases],
                "phase",
                heuristic_indices,
            ),
            "H_plus_one_limit": _linear_limit(
                [{"H_plus_one": value} for value in final_hooks],
                "H_plus_one",
                heuristic_indices,
            ),
            "warning": (
                "last-two-point extrapolation only; no asymptotic theorem or "
                "infinite-index sign claim"
            ),
        },
        "noncancellation_target": (
            "A proof would need a uniform representation "
            "H(r_ell)+1 = c_* + o(1) with c_*>0, or any explicit positive "
            "lower bound valid for all sufficiently large ell. These finite "
            "truncated evaluations do not provide that representation."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--indices", nargs="+", type=int, default=list(DEFAULT_INDICES))
    parser.add_argument("--terms", nargs="+", type=int, default=list(DEFAULT_TERMS))
    parser.add_argument("--dps", type=int, default=DEFAULT_DPS)
    parser.add_argument("--pole-dps", type=int, default=DEFAULT_POLE_DPS)
    parser.add_argument("--bisection-steps", type=int, default=DEFAULT_BISECTION)
    parser.add_argument("--max-seconds", type=float, default=300.0)
    args = parser.parse_args()
    print(
        json.dumps(
            run(
                args.indices,
                args.terms,
                dps=args.dps,
                pole_dps=args.pole_dps,
                bisection_steps=args.bisection_steps,
                max_seconds=args.max_seconds,
            ),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
