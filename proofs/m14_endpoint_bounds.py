"""Exact arithmetic ledger for the M14 endpoint research reductions.

This checker contains only rational consequences of the reviewed M10--M13
boxes.  It does not evaluate a phase point, interpolate in N, or assert an
endpoint sign.  The strict inequalities involving the phase endpoints use
the open strip 7/10 < beta < 18/25.
"""

from __future__ import annotations

import json
from fractions import Fraction as F


def _positive_exp_lower(x: F, terms: int = 18) -> F:
    """Positive Taylor lower bound for exp(x)."""

    total = F(0)
    power = F(1)
    factorial = 1
    for k in range(terms + 1):
        if k:
            power *= x
            factorial *= k
        total += power / factorial
    return total


def produce() -> dict:
    if not __debug__:
        raise RuntimeError("run without -O: exact research checks are required")

    theta_left = F(4, 5)
    theta_right = F(9, 10)
    beta_lo = F(7, 10)
    beta_hi = F(18, 25)
    v_left_hi = theta_left - beta_lo       # v < 1/10
    v_left_lo = theta_left - beta_hi       # v > 2/25
    v_right_hi = theta_right - beta_lo     # v < 1/5

    # The endpoint replacements in the M13 post-crossing telescope.
    left_theta_over_v = theta_left / v_left_hi
    left_chord = (1 - theta_left) / (1 - theta_left + beta_hi)
    left_const = left_theta_over_v * left_chord

    # p=7/10 is the exponent used by the reviewed M13 telescopes.  For
    # k>=1, the endpoint version is
    #   T_(N+1+k) > (40/23) [2N/(3k)]^p;
    # for k=0 it is T_(N+1) > 8 [5N/6]^p.
    p = F(7, 10)
    post_const = left_const
    post_k0_const = left_theta_over_v
    # The tenth-power comparisons avoid evaluating a fractional power.
    # With M=floor(N/2)>=31N/64, the displayed lower sum is > (7/2)N:
    # its N coefficient is >7/2, and its N^p remainder is positive.
    coeff_tenth = (
        F(10, 3) ** 10
        * post_const ** 10
        * F(2, 3) ** 7
        * F(31, 64) ** 3
    )
    target_tenth = F(7, 2) ** 10
    remainder_positive = (
        post_k0_const ** 10 * F(5, 6) ** 7
        > F(10, 3) ** 10 * post_const ** 10 * F(2, 3) ** 7
    )

    # Insert the already reviewed M13 prefactor, kernel, weight, and phase
    # boxes.  This is a genuine endpoint-left lower bound, but not the full
    # endpoint mass needed to beat the boundary term.
    sub_mass = (
        F(41, 50) * F(1, 4) * F(3, 2) * F(7, 2) * F(48, 329)
    )

    # M13's tail value uses the exact cancellation
    # A0=J(t)*(1-exp(-e)), J(t)<5/6, followed by
    # T<151/1000, LW<2, r^n<=exp(-ne), and x_(60N+1)>87/10.
    # The last comparison is a positive rational Taylor check, not a
    # floating-point assertion.
    exp_tail_lower = _positive_exp_lower(F(87, 10))
    tail_upper = F(5, 6) * F(151, 1000) * 2 / exp_tail_lower

    claims = {
        # These are endpoint constants; the strict inequalities follow from
        # the open beta strip (v<1/10 and beta<18/25).
        "left_theta_over_v_endpoint_constant_is_8": left_theta_over_v == 8,
        "left_chord_endpoint_constant_is_5_over_23": (
            left_chord == F(5, 23)
        ),
        "left_post_constant_is_40_over_23": post_const == F(40, 23),
        "left_power_coefficient_gt_7_over_2": coeff_tenth > target_tenth,
        "left_power_remainder_positive": remainder_positive,
        "left_subwindow_mass_gt_369_over_2350": sub_mass == F(369, 2350),
        "exp_87_over_10_gt_5000": exp_tail_lower > 5000,
        "tail_value_lt_151_over_3000000": tail_upper < F(151, 3_000_000),
    }
    if not all(claims.values()):
        raise ArithmeticError("M14 endpoint arithmetic reduction failed")

    return {
        "status": "pass",
        "classification": "EXACT RATIONAL ENDPOINT REDUCTIONS; NO SIGN CLAIM",
        "claims": claims,
        "left": {
            "beta_strip": [str(beta_lo), str(beta_hi)],
            "v_open_bounds": [str(v_left_lo), str(v_left_hi)],
            "theta_over_v_endpoint_constant": str(left_theta_over_v),
            "chord_endpoint_constant": str(left_chord),
            "post_telescope_constant": str(post_const),
            "bare_subwindow_mass_lower": "> (7/2) N",
            "prefactored_subwindow_mass_lower": str(sub_mass),
        },
        "right": {
            "v_upper": str(v_right_hi),
            "T_N_lower_template": "((5*N+6)/6)^(7/10)",
            "warning": "T_N has no theta/(theta-beta) factor",
        },
        "tail": {
            "exp_lower_terms": 18,
            "exp_lower": str(exp_tail_lower),
            "upper": str(tail_upper),
            "target": str(F(151, 3_000_000)),
        },
        "scope": (
            "rational endpoint constants only; the complete positive mass, "
            "boundary refinement, and uniform F signs remain open"
        ),
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
