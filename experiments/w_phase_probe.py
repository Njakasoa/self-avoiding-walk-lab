"""Finite numerical probe for the weakly-prudent bridge quotient W.

This module is deliberately separate from the existing prudent singularity
probes.  It evaluates the Bacher--Beaton kernel sums for ``P`` and ``H``
directly, evaluates the Proposition 8 recurrence for ``D``, and then forms

    F = (3 - t - 2*D_I)*P - 4*H - (1 + t + 2*D_I),
    D_I = D/(1 + D).

Thus ``F=(I-1)*(1+P)`` whenever the source identities are used.  The
``D_I=1`` diagnostic is retained separately because D_I approaches one only
slowly along the critical phase scaling.  Every output is finite numerical
evidence; no tail or phase-limit claim is made here.
"""

from __future__ import annotations

import argparse
import json
import time
from typing import Any, Iterable

import mpmath as mp


def kernel(t: mp.mpf, v: mp.mpf) -> mp.mpf:
    """The formal-series branch U(t,v) used by Bacher--Beaton."""

    a = 1 - t * v + t * t + t**3 * v
    return 2 * t / (a + mp.sqrt(a * a - 4 * t * t))


def phase_coordinate(t: mp.mpf) -> mp.mpf:
    """Return the critical phase coordinate a=s_g/epsilon."""

    q = kernel(t, mp.mpf(1))
    one_minus_tq = 1 - t * q
    u = t / one_minus_tq
    v = (u - t) * (1 - t * u) / (t * (1 - t * t) * u)
    return mp.log(v) / mp.log(q * q)


def phase_parameter(index: int, theta: mp.mpf, *, bisection: int = 240) -> mp.mpf:
    """Solve phase_coordinate(t)=index+theta below sigma."""

    lo = mp.mpf("0.4")
    # Keep the high endpoint below the square-root branch point at the
    # working precision.  The endpoint is only used to bracket the root.
    hi = mp.sqrt(2) - 1 - mp.mpf(10) ** (-mp.mp.dps + 12)
    target = mp.mpf(index) + mp.mpf(theta)
    if not phase_coordinate(lo) < target < phase_coordinate(hi):
        raise ArithmeticError(
            f"phase target {target} was not bracketed at dps={mp.mp.dps}"
        )
    for _ in range(bisection):
        mid = (lo + hi) / 2
        if phase_coordinate(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def prudent_sums(t: mp.mpf, terms: int) -> dict[str, mp.mpf]:
    """Evaluate the finite Proposition 14/16 sums for P and H.

    The formula is written out here rather than importing the prior probe, so
    the W experiment has an independent implementation of the continuation
    evaluation.  ``terms`` counts the n=0,...,terms-1 summands.
    """

    t = mp.mpf(t)
    q = kernel(t, mp.mpf(1))
    one = 1 - t * q
    total_p = mp.mpf(0)
    total_h = mp.mpf(0)
    product = mp.mpf(1)
    last = mp.mpf(0)
    for n in range(terms):
        v = q ** (2 * n)
        u = kernel(t, v)
        w = kernel(t, v * q * q)
        h = t * q - (q - t) * u
        A = (
            (q - t)
            * (1 - t * t)
            * (u * one - (q * (q - t) + t * (1 - q * q) * u) * w)
            / (one * (1 - t * u) * (1 - t * w) * h)
        )
        B = q * (q - t) ** 2 * (t - one * w) / (one * one * h)
        A_hook = (
            t
            * t
            * (1 - t * t)
            * (q - t)
            * (
                one * u * u * (1 - 2 * t * w)
                - (
                    q * (q - t)
                    - t * u * (2 * q * (q - t) + t * (1 - q * q) * u)
                )
                * w
                * w
            )
            / (one * (1 - t * u) ** 2 * (1 - t * w) ** 2 * h)
        )
        term_p = product * A
        term_h = product * A_hook
        total_p += term_p
        total_h += term_h
        last = max(abs(term_p), abs(term_h))
        product *= B
    P = q * (1 - t * t) / one + q * total_p
    H = t * t * q * q * (1 - t * t) / (one * one) + q * total_h
    return {"P": P, "H": H, "last_term": last, "q": q}


def directed_ramp_sum(
    t: mp.mpf,
    *,
    tolerance: mp.mpf = mp.mpf("1e-55"),
    max_terms: int = 250_000,
) -> dict[str, mp.mpf | int]:
    """Evaluate D=sum_{k>=0} t^(k+1)/G_k by the Proposition 8 recurrence."""

    t = mp.mpf(t)
    coefficient = 1 - t + t * t + t**3
    g_previous = mp.mpf(1)  # G_{-1}
    g_current = 1 - t  # G_0
    power = t  # t^(0+1)
    total = power / g_current
    last_term = abs(power / g_current)
    used = 1
    for k in range(1, max_terms):
        g_next = coefficient * g_current - t * t * g_previous
        g_previous, g_current = g_current, g_next
        power *= t
        term = power / g_current  # t^(k+1)/G_k
        total += term
        last_term = abs(term)
        used = k + 1
        if k >= 100 and last_term <= tolerance * max(1, abs(total)):
            break
    else:
        raise TimeoutError(
            f"D recurrence did not reach tolerance={tolerance} in {max_terms} terms"
        )
    return {"D": total, "terms": used, "last_term": last_term}


def _decimal(value: mp.mpf, digits: int = 32) -> str:
    return mp.nstr(value, digits)


def _case(
    index: int,
    theta: mp.mpf,
    *,
    prudent_terms: Iterable[int],
    dps: int,
    deadline: float,
) -> dict[str, Any]:
    """Evaluate one phase, retaining a term-doubling check."""

    with mp.workdps(dps):
        t = phase_parameter(index, theta)
        q = kernel(t, mp.mpf(1))
        epsilon = -mp.log(q * q)
        rows: list[dict[str, Any]] = []
        directed = directed_ramp_sum(t)
        D = mp.mpf(directed["D"])
        DI = D / (1 + D)
        for terms in prudent_terms:
            if time.perf_counter() >= deadline:
                raise TimeoutError("W phase probe exceeded its runtime budget")
            sums = prudent_sums(t, int(terms))
            P, H = sums["P"], sums["H"]
            P_plus_one = P + 1
            F = (3 - t - 2 * DI) * P - 4 * H - (1 + t + 2 * DI)
            F_D1 = (1 - t) * P - 4 * H - (3 + t)
            correction = F - F_D1
            # This is the same denominator test divided by 1+P; it is
            # recorded only when the finite sum is away from its poles.
            I_minus_one = F / P_plus_one
            rows.append(
                {
                    "prudent_terms": int(terms),
                    "P": _decimal(P),
                    "H": _decimal(H),
                    "P_plus_one": _decimal(P_plus_one),
                    "H_plus_one": _decimal(H + 1),
                    "F": _decimal(F),
                    "F_D1_diagnostic": _decimal(F_D1),
                    "D_I_correction": _decimal(correction),
                    "I_minus_one": _decimal(I_minus_one),
                    "last_prudent_term": _decimal(sums["last_term"]),
                }
            )
        final = rows[-1]
        return {
            "index": int(index),
            "theta": _decimal(mp.mpf(theta)),
            "t": _decimal(t),
            "phase_coordinate": _decimal(phase_coordinate(t)),
            "epsilon_minus_log_q2": _decimal(epsilon),
            "q": _decimal(q),
            "D": _decimal(D),
            "D_I": _decimal(DI),
            "D_recurrence_terms": int(directed["terms"]),
            "D_last_term": _decimal(mp.mpf(directed["last_term"])),
            "rows": rows,
            "doubling_drift": {
                "P": _decimal(abs(mp.mpf(rows[-1]["P"]) - mp.mpf(rows[-2]["P"])))
                if len(rows) >= 2
                else None,
                "H": _decimal(abs(mp.mpf(rows[-1]["H"]) - mp.mpf(rows[-2]["H"])))
                if len(rows) >= 2
                else None,
                "F": _decimal(abs(mp.mpf(rows[-1]["F"]) - mp.mpf(rows[-2]["F"])))
                if len(rows) >= 2
                else None,
            },
            "final_signs": {
                "F": "positive" if mp.mpf(final["F"]) > 0 else "negative",
                "F_D1_diagnostic": (
                    "positive"
                    if mp.mpf(final["F_D1_diagnostic"]) > 0
                    else "negative"
                ),
                "P_plus_one": (
                    "positive" if mp.mpf(final["P_plus_one"]) > 0 else "negative"
                ),
            },
        }


def run(
    *,
    indices: Iterable[int] = (8, 16, 32, 64),
    phases: Iterable[str] = ("0.75", "0.80", "0.85", "0.87", "0.90"),
    dps: int = 90,
    max_seconds: float = 180.0,
) -> dict[str, Any]:
    """Run the bounded phase sweep."""

    selected_indices = [int(x) for x in indices]
    if selected_indices != sorted(set(selected_indices)):
        raise ValueError("indices must be strictly increasing")
    started = time.perf_counter()
    deadline = started + float(max_seconds)
    mp.mp.dps = dps
    cases: list[dict[str, Any]] = []
    with mp.workdps(dps):
        # Parse decimal phase strings only after entering the requested
        # precision context.  Parsing before workdps silently rounded 0.80,
        # 0.87, ... to the process default precision.
        selected_phases = [mp.mpf(str(x)) for x in phases]
        if any(
            not (mp.mpf("0.7") < x < mp.mpf("0.95"))
            for x in selected_phases
        ):
            raise ValueError(
                "phases must lie in the exploratory interval (0.7,0.95)"
            )
        for index in selected_indices:
            # The first schedule is a truncation check; the larger one is the
            # reported value.  It scales mildly with epsilon and remains
            # inexpensive for the held-out index 64.
            for theta in selected_phases:
                if time.perf_counter() >= deadline:
                    raise TimeoutError("W phase probe exceeded its runtime budget")
                t_preview = phase_parameter(index, theta)
                q_preview = kernel(t_preview, mp.mpf(1))
                epsilon = -mp.log(q_preview * q_preview)
                base = max(2_000, int(mp.ceil(12 / epsilon)))
                schedule = (base, 2 * base)
                cases.append(
                    _case(
                        index,
                        theta,
                        prudent_terms=schedule,
                        dps=dps,
                        deadline=deadline,
                    )
                )
    elapsed = time.perf_counter() - started
    return {
        "classification": "FINITE NUMERICAL FALSIFICATION ONLY",
        "warning": (
            "Neither the D recurrence tail nor the prudent continuation tail is "
            "interval-certified; no finite phase sweep proves a W theorem."
        ),
        "dps": dps,
        "max_seconds": max_seconds,
        "runtime_seconds": elapsed,
        "sigma": _decimal(mp.sqrt(2) - 1),
        "eta": _decimal(1 / mp.sqrt(2)),
        "indices": selected_indices,
        "phases": [_decimal(x) for x in selected_phases],
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="write JSON to this path instead of stdout")
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--max-seconds", type=float, default=180.0)
    args = parser.parse_args()
    result = run(dps=args.dps, max_seconds=args.max_seconds)
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as stream:
            stream.write(payload)
            stream.write("\n")
    else:
        print(payload)


if __name__ == "__main__":
    main()
