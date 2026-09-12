"""Rational ledger for the M14 normalized Gamma-primitive envelope.

The checker does not evaluate Gamma functions or sample an index.  It verifies
the rational domains and the Wendel constants used by the accompanying note.
"""

from __future__ import annotations

import json
from fractions import Fraction as F


def produce() -> dict:
    if not __debug__:
        raise RuntimeError("run without -O: exact M14 guards are required")

    theta_lo, theta_hi = F(4, 5), F(9, 10)
    beta_lo, beta_hi = F(7, 10), F(18, 25)
    c_lo, c_hi = 1 - beta_hi, 1 - beta_lo
    n_lo = 32
    a_lo = n_lo + theta_lo
    A_lo = a_lo + c_lo
    d_pre_lo = theta_lo
    d_post_lo = 1 - theta_hi
    x_wendel_lo = d_post_lo

    # w(x,beta)=(x/(x+beta))^(1-beta).  The base is minimized at
    # x=1/10,beta=18/25, while the exponent is <3/10.
    w_base_lo = x_wendel_lo / (x_wendel_lo + beta_hi)
    w_base_pow_check = w_base_lo ** 3 > F(1, 2) ** 10
    A_base_lo = A_lo / (A_lo + beta_hi)

    # e*A = e*a + e*c = s_g+e*c, with s_g<.17 and e<.17/N.
    e_hi = F(17, 100) / n_lo
    eA_hi = F(17, 100) + e_hi * c_hi

    phase_gap_lo = theta_lo - beta_hi
    phase_gap_hi = theta_hi - beta_lo
    sine_denominator_lower = 2 * phase_gap_lo
    sine_multiplier_upper = 1 / sine_denominator_lower
    shifted_alpha_lo = c_lo
    shifted_alpha_hi = c_hi
    block_holder = 1 / c_lo + sine_multiplier_upper / c_lo
    away_floor_constant = sine_multiplier_upper * 2 * beta_hi
    critical_sine_log_slope = F(22, 7) / sine_denominator_lower
    coefficient_log_linear = F(168, 25) + F(24, 5)
    coefficient_log_quadratic = F(69, 250)
    e_upper_below_180 = e_hi < F(1, 180)
    log_argument_relative_upper = F(14, 3) * e_hi
    holdout_n = 512
    h0_factor_upper = 1 + c_hi / holdout_n

    claims = {
        "a_ge_164_over_5": a_lo == F(164, 5),
        "A_ge_827_over_25": A_lo == F(827, 25),
        "pre_gamma_base_ge_4_over_5": d_pre_lo >= F(4, 5),
        "post_gamma_base_ge_1_over_10": d_post_lo >= F(1, 10),
        "wendel_base_ge_5_over_41": w_base_lo == F(5, 41),
        "wendel_power_lower_gt_one_half": w_base_pow_check,
        "wendel_A_factor_gt_nine_tenths": A_base_lo > F(9, 10),
        "eA_lt_nine_fiftieths": eA_hi < F(9, 50),
        "phase_gap_is_two_twenty_fifths": phase_gap_lo == F(2, 25),
        "phase_gap_upper_is_one_fifth": phase_gap_hi == F(1, 5),
        "sine_denominator_lower_is_four_twenty_fifths": (
            sine_denominator_lower == F(4, 25)
        ),
        "sine_multiplier_bound_is_25_over_4": (
            sine_multiplier_upper == F(25, 4)
        ),
        "theta_minus_beta_gt_zero": phase_gap_lo > 0,
        "shifted_alpha_in_7_25_3_10": (
            shifted_alpha_lo == F(7, 25)
            and shifted_alpha_hi == F(3, 10)
        ),
        "normalized_primitive_holder_lt_26": block_holder < 26,
        "away_floor_constant_lt_10": away_floor_constant < 10,
        "critical_sine_log_slope_lt_20": critical_sine_log_slope < 20,
        "e_upper_lt_one_over_180": e_upper_below_180,
        "log_argument_relative_lt_one_half": log_argument_relative_upper < F(1, 2),
        "h0_N512_factor_lt_1001_over_1000": h0_factor_upper < F(1001, 1000),
        "coefficient_log_bound_lt_12": (
            coefficient_log_linear + coefficient_log_quadratic * e_hi < 12
        ),
    }
    if not all(claims.values()):
        raise ArithmeticError("M14 Gamma-block rational guard failed")

    return {
        "status": "pass",
        "classification": (
            "EXACT RATIONAL WENDEL DOMAIN AND NORMALIZED-PRIMITIVE BOUNDS; "
            "NO ENDPOINT SIGN CLAIM"
        ),
        "claims": claims,
        "domain": {
            "N_min": n_lo,
            "theta": [str(theta_lo), str(theta_hi)],
            "beta": [str(beta_lo), str(beta_hi)],
            "c=1-beta": [str(c_lo), str(c_hi)],
            "a_lower": str(a_lo),
            "A=b+1_lower": str(A_lo),
            "pre_d_lower": str(d_pre_lo),
            "post_d_lower": str(d_post_lo),
        },
        "wendel": {
            "W_minus": "x^beta*(x/(x+beta))^(1-beta)",
            "W_plus": "x^beta",
            "global_T_factor_interval": ["9/10", "2"],
        },
        "crossing": {
            "normalized_primitive_holder": "26*|delta|^(7/25)",
            "crossing_block_upper": "52*(rho+e)^(7/25)",
            "sine_multiplier_upper": "25/4",
        },
        "shifted_gamma": {
            "alpha": "1-beta",
            "coefficient_interval": "s^beta <= A_e <= (s+alpha*e)^beta",
            "ratio": "(z-beta)^alpha <= Gamma(z+alpha)/Gamma(z) <= z^alpha",
            "validity": "z>beta; pre z=a-n, post z=n-a+beta",
            "floor_shift": "barQ(ne) <= e*Q_n <= barQ((n+beta)*e)",
            "holder_constant": "725/28 < 26",
            "zero_start_offset": "I[-alpha*e,0] <= h0 <= I[-e,0]",
            "zero_start_N512_upper": "h0 < 1001*e/1000",
        },
        "scope": (
            "all integer N>=32 and theta endpoint/band beta boxes; exact "
            "Gamma formulas plus Wendel inequalities, no point scan"
        ),
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
