"""Exact and bounded numerical checks for the BB2014 D/D_I series.

The checks use the physical kernel branch q=U(t,1), where

    t*(q + 1/q) = 1 - t + t**2 + t**3.

They verify the closed form for G_k, the critical repeated-root formula,
and a few high-precision partial sums.  The proof of local holomorphy and
the limit D_I -> 1 is in proofs/W_DIRECTED_RAMPS.md; this script is not a
substitute for that proof.
"""

from __future__ import annotations

import json
from typing import Any

import mpmath as mp
import sympy as sp


def _zero_mod_kernel(expression: sp.Expr, relation: sp.Expr, q: sp.Symbol) -> bool:
    """Return whether a rational expression vanishes modulo relation(q)."""
    numerator = sp.together(expression).as_numer_denom()[0]
    remainder = sp.rem(sp.Poly(sp.expand(numerator), q), sp.Poly(relation, q))
    return sp.expand(remainder.as_expr()) == 0


def _numeric_q(t: mp.mpf) -> mp.mpf:
    a = 1 - t + t * t + t * t * t
    return (a - mp.sqrt(a * a - 4 * t * t)) / (2 * t)


def _numeric_partial_sum(t: mp.mpf, terms: int) -> mp.mpf:
    q = _numeric_q(t)
    beta = (1 - t - t * q) / (1 - q * q)
    gamma = q * (t - q * (1 - t)) / (1 - q * q)
    return mp.fsum(
        t * q**k / (beta + gamma * q ** (2 * k))
        for k in range(terms + 1)
    )


def produce() -> dict[str, Any]:
    t, q = sp.symbols("t q", nonzero=True)
    a = 1 - t + t**2 + t**3
    relation = sp.expand(t * q**2 - a * q + t)
    beta = (1 - t - t * q) / (1 - q**2)
    gamma = q * (t - q * (1 - t)) / (1 - q**2)

    def closed(k: int) -> sp.Expr:
        return (t / q) ** k * (beta + gamma * q ** (2 * k))

    checks: dict[str, bool] = {}
    checks["kernel_relation_is_cleared"] = sp.expand(
        relation - (t * q**2 - (1 - t + t**2 + t**3) * q + t)
    ) == 0
    checks["G_minus_one"] = sp.simplify(closed(-1) - 1) == 0
    checks["G_zero"] = sp.simplify(closed(0) - (1 - t)) == 0
    checks["beta_plus_gamma"] = sp.simplify(beta + gamma - (1 - t)) == 0
    for k in range(1, 8):
        checks[f"recurrence_k_{k}"] = _zero_mod_kernel(
            closed(k) - a * closed(k - 1) + t**2 * closed(k - 2),
            relation,
            q,
        )
        checks[f"summand_identity_k_{k}"] = sp.simplify(
            t ** (k + 1) / closed(k)
            - t * q**k / (beta + gamma * q ** (2 * k))
        ) == 0

    sigma = sp.sqrt(2) - 1

    def critical(k: int) -> sp.Expr:
        return sigma**k * ((1 - sigma) + (1 - 2 * sigma) * k)

    critical_checks = {
        "G_minus_one": sp.simplify(critical(-1) - 1) == 0,
        "G_zero": sp.simplify(critical(0) - (1 - sigma)) == 0,
    }
    for k in range(1, 8):
        critical_checks[f"recurrence_k_{k}"] = sp.simplify(
            critical(k)
            - 2 * sigma * critical(k - 1)
            + sigma**2 * critical(k - 2)
        ) == 0

    mp.mp.dps = 70
    sigma_mp = mp.sqrt(2) - 1
    critical_partial_sums = {
        str(n): mp.nstr(
            mp.fsum(
                sigma_mp
                / ((1 - sigma_mp) + (1 - 2 * sigma_mp) * k)
                for k in range(n + 1)
            ),
            30,
        )
        for n in (10, 100, 1000, 10000)
    }
    sample_rows = []
    for t_value in ("0.1", "0.3", "0.4", "0.414"):
        t_mp = mp.mpf(t_value)
        q_mp = _numeric_q(t_mp)
        sample_rows.append(
            {
                "t": t_value,
                "q": mp.nstr(q_mp, 30),
                "partial_D_200": mp.nstr(_numeric_partial_sum(t_mp, 200), 30),
            }
        )

    if not all(checks.values()) or not all(critical_checks.values()):
        raise AssertionError("an exact recurrence check failed")

    return {
        "classification": "EXACT RECURRENCE IDENTITIES; BOUNDED NUMERICAL CHECKS",
        "kernel_relation": sp.sstr(relation),
        "checks": checks,
        "critical_checks": critical_checks,
        "critical_formula": "G_k(sigma)=sigma^k*((1-sigma)+(1-2*sigma)*k)",
        "critical_partial_sums": critical_partial_sums,
        "samples": sample_rows,
        "scope": (
            "The proof file establishes positivity, local holomorphy, and "
            "the uniform D_I limit; these finite checks do not establish a "
            "non-D-finiteness theorem for W by themselves."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
