"""Independent high-precision check of the logarithmic D(t) bound.

The analytic proof is in proofs/M5_DIRECTED_LOG.md.  This script solves the
q-parameterized kernel equation by bisection, evaluates the exact summand
rewritten with Q=q**2, and adds an elementary geometric tail bound.  It is a
numerical reproduction aid, not an interval-arithmetic certificate.
"""

from __future__ import annotations

import json
from typing import Any

import mpmath as mp


mp.mp.dps = 80
SIGMA = mp.sqrt(2) - 1
EPS0 = mp.mpf("0.1")


def solve_t(epsilon: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    q = mp.exp(-epsilon / 2)
    target = q + 1 / q

    def f(t: mp.mpf) -> mp.mpf:
        return 1 / t - 1 + t + t * t - target

    lo, hi = mp.mpf("0.4"), SIGMA
    if f(lo) <= 0 or f(hi) >= 0:
        raise ArithmeticError("kernel bracket failed")
    for _ in range(320):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    t = (lo + hi) / 2
    return t, q


def evaluate(epsilon: mp.mpf, cutoff_factor: int = 40) -> dict[str, mp.mpf | int]:
    t, q = solve_t(epsilon)
    Q = q * q
    s = 1 - Q
    alpha = 1 - t - t * q
    c = (1 - t) / alpha
    r = t / alpha
    cutoff = int(mp.ceil(cutoff_factor / epsilon))

    partial = mp.mpf("0")
    for k in range(cutoff + 1):
        Qk = Q**k
        denominator = alpha * (1 - Qk) + (1 - t) * s * Qk
        partial += t * s * q**k / denominator

    # For k > cutoff, 1-Q**k >= 1-Q**(cutoff+1).
    tail = (
        t
        * s
        * q ** (cutoff + 1)
        / (alpha * (1 - Q ** (cutoff + 1)) * (1 - q))
    )
    lower = partial
    upper = partial + tail
    leading = (1 / SIGMA) * mp.log(1 / epsilon)
    return {
        "epsilon": epsilon,
        "t": t,
        "q": q,
        "alpha": alpha,
        "r": r,
        "cutoff": cutoff,
        "D_lower": lower,
        "D_upper": upper,
        "tail_bound": tail,
        "C_lower": lower - leading,
        "C_upper": upper - leading,
        "one_minus_DI_lower": 1 / (1 + upper),
        "one_minus_DI_upper": 1 / (1 + lower),
        "leading_reciprocal": SIGMA / mp.log(1 / epsilon),
    }


def _display(value: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def produce() -> dict[str, Any]:
    rows = []
    for value in ("0.1", "0.05", "0.02", "0.01", "0.005", "0.002"):
        row = evaluate(mp.mpf(value))
        if row["C_lower"] < -80 or row["C_upper"] > 80:
            raise AssertionError("the explicit |C_D| <= 80 check failed")
        rows.append(
            {
                key: (
                    str(val)
                    if key == "cutoff"
                    else (str(value) if key == "epsilon" else _display(val))
                )
                for key, val in row.items()
            }
        )
    return {
        "classification": "HIGH-PRECISION NUMERICAL CHECK WITH GEOMETRIC TAIL",
        "domain": "0 < epsilon <= 0.1",
        "analytic_bound_checked": "|D-(1/sigma)*log(1/epsilon)| <= 80",
        "rows": rows,
        "scope": (
            "The tail bound is elementary but arithmetic is high precision, "
            "not directed interval arithmetic. The phase inverse threshold "
            "is inherited from the separate phase construction."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
