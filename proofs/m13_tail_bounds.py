"""Exact arithmetic ledger for the M13 real post-60N tail bound.

The companion note ``M13_TAIL_PHASE_BOUND.md`` supplies the analytic
hypotheses separately: the M6 real secant result gives ``0 < Pi <= 1`` and
``r <= exp(-e)``, M10/M11 give the scalar, weight, beta and phase-derivative
boxes, and Wendel's inequality gives the post-crossing Gamma estimate.

This file checks only rational implications.  It deliberately does not
import the old M6 Gamma lemma whose proof assumes ``a >= 200``; the tail
estimate below uses the direct post-crossing arguments ``b+1`` and ``n-a``
which are already greater than one for every ``N >= 32``.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from math import factorial


if not __debug__:
    raise RuntimeError("run without -O: exact ledger guards are required")


def _exp_partial(x: F, degree: int) -> F:
    return sum((x**k / factorial(k) for k in range(degree + 1)), F(0))


def produce() -> dict:
    checks: dict[str, bool] = {}

    def require(name: str, condition: bool) -> None:
        if not condition:
            raise ArithmeticError(name)
        checks[name] = True

    # Phase and tail start.  The M5/M10 real phase inputs are
    # .15 < s_g < .17 and theta in [.8,.9].
    N0 = 32
    eN_lower = F(3, 20) * F(320, 329)  # .15 * 32/(32+.9)
    require("eN_lower_at_N32", eN_lower > F(29, 200))
    # N/(N+9/10) is increasing; at N=32 the cross-multiplied gap is zero,
    # and it is positive thereafter: 9N-288 >= 0.
    require("phase_ratio_monotone_from_N32", 9 * N0 - 288 >= 0)
    require("e_upper_for_N32", F(17, 100) / 32 < F(1, 180))
    require("tail_phase_lower", 60 * F(29, 200) >= F(87, 10))
    x_start_upper = 60 * F(17, 100) + F(1, 180)
    require("tail_phase_upper", x_start_upper < 11)
    require("one_over_e_lt_7N", F(200, 29) < 7)

    # Elementary exponential lower bounds used twice: x_start>8.7 implies
    # exp(-x_start)<1/5000, and finally exp(8.7)>5989.67.
    exp_87_degree15 = _exp_partial(F(87, 10), 15)
    exp_87_degree18 = _exp_partial(F(87, 10), 18)
    require("exp_87_lower_gt_5000", exp_87_degree15 > 5000)
    require("exp_87_lower_gt_final_threshold", exp_87_degree18 > F(17969, 3))

    # The scalar factor J=t(1-t^2)/(1-t-t^2) is increasing on the M11
    # physical box; the endpoint evaluation is the exact Fraction check.
    t_h = F(4143, 10000)
    J_endpoint = t_h * (1 - t_h * t_h) / (1 - t_h - t_h * t_h)
    require("J_endpoint_lt_5_over_6", J_endpoint < F(5, 6))

    # Beyond n>60N, v=exp(-ne)<1/5000 and the inverse-kernel equation gives
    # 0<u-t = v*t*(1-t^2)*u/(1-tu) < v*t*(1+t) < v.
    u_tail = t_h + F(1, 5000)
    require("u_tail_le_829_over_2000", u_tail <= F(829, 2000))

    # Tail weight box.  Here q>359/360, C=q-t, h in [.706,.71], and
    # c_W=1-t+2 delta_D > 1-t.  The displayed maxima are independent
    # positive rational upper bounds for V1 and R=V2/V1.
    q_l = F(359, 360)
    h_l = F(353, 500)
    h_h = F(71, 100)
    C_l = q_l - t_h
    dd_tail = 1 / ((1 - t_h * u_tail) * (1 - t_h * h_h))
    L1_tail = h_h / ((1 - t_h * h_h) * (1 - h_h))
    V1_tail = (dd_tail + L1_tail) / C_l
    f_u_tail = u_tail / (1 - t_h * u_tail)
    R_tail = (
        h_h / (1 - t_h * h_h)
        + f_u_tail * (1 - h_l) / (1 - t_h * u_tail * h_h)
    )
    L_tail = V1_tail * (4 * t_h * t_h * R_tail - (1 - t_h))
    require("C_tail_lower_positive", C_l > 0)
    require("V1_tail_lt_9", V1_tail < 9)
    require("R_tail_lt_6_over_5", R_tail < F(6, 5))
    require("LW_tail_lt_2", L_tail < 2)

    # Sine multiplier.  For y=1-theta in [.1,.2], and
    # v=theta-beta in [.08,.2], sin is increasing on this interval.
    # The exact sin(pi/5) identity supplies the numerator bound.  For the
    # denominator use sin x >= x-x^3/6 with 157/50 < pi < 22/7.
    sqrt5_lower = F(223, 100)
    require("sqrt5_lower_squared_lt_5", sqrt5_lower * sqrt5_lower < 5)
    sin_num_sq_upper = (5 - sqrt5_lower) / 8
    require("sin_pi_over_5_lt_59_over_100", sin_num_sq_upper < F(59, 100) ** 2)
    pi_lower = F(157, 50)
    pi_upper = F(22, 7)
    angle_lower = 2 * pi_lower / 25
    angle_upper = 2 * pi_upper / 25
    sin_den_lower = angle_lower - angle_upper**3 / 6
    require("sin_2pi_over_25_gt_31_over_125", sin_den_lower > F(31, 125))
    sine_multiplier = F(59, 100) / F(31, 125)
    require("sine_multiplier_lt_12_over_5", sine_multiplier < F(12, 5))

    # Direct post-crossing Wendel ledger, valid without a>=200.  Put
    # x=b+1 and y=n-a.  For N>=32 and n>=60N+1,
    # x/y<1/56 and beta/y<1/2000.
    require(
        "gamma_base_ratio_lt_1_over_56",
        56 * (F(32) + F(6, 5)) < 59 * F(32) + F(1, 10),
    )
    require(
        "gamma_beta_over_y_lt_1_over_2000",
        F(2000) * F(18, 25) < 59 * F(32) + F(1, 10),
    )
    require("fractional_power_56", 16**10 < 56**7)
    wendel_factor = F(2001, 2000)
    T_upper = F(12, 5) * wendel_factor / 16
    require("T_tail_lt_151_over_1000", T_upper < F(151, 1000))

    # Bare-product and harmonic derivative bounds for every post-tail n.
    # The two theta regimes bound the first pre/post terms separately; the
    # remaining reciprocal-square tails use sum_{k>=2} k^-2 < 2/3.
    S_theta_low = (
        F(125, 8) + F(400, 51) + F(5, 3) + F(3200, 2553)
    )
    S_theta_high = (
        F(2000, 221) + F(25, 2) + F(5, 3) + F(400, 297)
    )
    require("bare_S_low_theta_lt_27", S_theta_low < 27)
    require("bare_S_high_theta_lt_27", S_theta_high < 27)
    require("bare_S_uniform_lt_27", max(S_theta_low, S_theta_high) < 27)
    beta_S_upper = F(18, 25) * 27

    # H_n bound: |H_n| <= 59/4 + (9/4) log n.  With log n <= x+1/e,
    # 1/e<7N, the normalized geometric tail expectation contributes less
    # than 1/7000 to |beta_theta H_n|.
    expected_x = F(12)  # x_start<11 and e*p/(1-p)<1
    expected_x2 = F(146)  # 11^2+2*11+3
    beta_H_expected = (
        F(1, 125 * N0**3)
        * (F(59, 4) + F(9, 4) * expected_x + F(9, 4) * 7 * N0)
    )
    require("beta_H_expected_lt_1_over_7000", beta_H_expected < F(1, 7000))

    # Absolute phase-log derivative ledger.  The reviewed M11 factor bound
    # is |d_e log R_e(je)| < 7071/1000 + (18/100) je.  We use the reviewed
    # |log r|_e<2 and |d_theta log(A0 LW)|<14/N; the latter is obtained by
    # taking absolute values of the same positive-variable M11 allowances
    # (200 for t, 50 for h, 2 for C, 16 for u, 200/7 for delta, and 2 for
    # A0).  The note states the elementary derivation explicitly.
    factor_constant = F(7071, 1000)
    factor_slope = F(18, 100)
    require("factor_constant_decomposition", factor_constant == F(75, 100) + F(18, 10) + F(3721, 1000) + F(8, 10))
    require("factor_slope_eq_0_18", factor_slope == F(18, 100))
    weight_abs_upper = F(14)
    derivative_x_coefficient = F(2) + factor_constant
    derivative_x2_coefficient = factor_slope / 2
    # Absolute M11 weight ledger, after multiplying by N.  The h derivative
    # bound is checked from the displayed quotient formulas rather than
    # silently reusing the one-sided 11/N estimate.
    d_tail = 1 - t_h * h_h
    h_partial_abs = t_h / d_tail + t_h / d_tail + 1 / (1 - h_h)
    R_h_abs = 2 / (d_tail * d_tail)
    h_log_abs = h_partial_abs + 4 * t_h * t_h * R_h_abs / F(7, 100)
    require("partial_h_log_L_abs_lt_50", h_log_abs < 50)
    weight_components = {
        "t": F(200, 7) * F(1, 180) ** 2,
        "h": 50 * F(26, 100) / 180,
        "C": 2 * F(51, 100) / 180,
        "u": 16 * F(61, 100),
        "delta": F(200, 7) * F(49, 1250),
        "A0": 2,
    }
    weight_abs_sum = sum(weight_components.values(), F(0))
    require("absolute_weight_ledger_lt_14", weight_abs_sum < 14)
    expected_derivative_numerator = (
        weight_abs_upper
        + derivative_x_coefficient * expected_x
        + derivative_x2_coefficient * expected_x2
    )
    derivative_average = beta_S_upper + expected_derivative_numerator / N0 + F(1, 7000)
    require("derivative_average_lt_119_over_5", derivative_average < F(119, 5))

    # A0=J(1-exp(-e)) cancels the geometric denominator 1-exp(-e) exactly.
    # The resulting coefficient times exp(-8.7) is below 1e-3.
    final_coefficient = F(5, 6) * F(151, 1000) * 2 * F(119, 5)
    require("final_coefficient_eq_17969_over_3000", final_coefficient == F(17969, 3000))
    require("final_exp_margin", exp_87_degree18 > 1000 * final_coefficient)
    tail_upper = final_coefficient / exp_87_degree18
    require("tail_derivative_lt_1e_minus_3", tail_upper < F(1, 1000))

    return {
        "classification": "EXACT FRACTION M13 POST-60N TAIL LEDGER",
        "status": "pass",
        "scope": "real N>=32, theta in [4/5,9/10], integer n>60N",
        "analytic_hypotheses": [
            "M5 real phase inverse: .15<s_g<.17 and |e_theta|<e/N",
            "M10 beta strip: 7/10<beta<18/25 and |beta_theta|<.008/N^3",
            "M6/M11 real secant product: 0<R_e and Pi_{e,n}<=1",
            "M6 real ratio: 0<r<=exp(-e)",
            "M11 absolute per-factor bound: |d_e log R_e(je)|<7.071+.18 je",
            "M11 absolute weight ledger: |d_theta log(A0 L_W(u_n))|<14/N",
            "M10 combined-weight positivity and post-tail source-pole-free Gamma form",
        ],
        "fraction_bounds": {
            "eN_lower": str(F(29, 200)),
            "eN_upper": str(F(17, 100)),
            "x_start_lower": str(F(87, 10)),
            "x_start_upper": str(x_start_upper),
            "J_upper": str(F(5, 6)),
            "u_tail_upper": str(u_tail),
            "V1_tail_upper": str(V1_tail),
            "R_tail_upper": str(R_tail),
            "LW_tail_upper": str(L_tail),
            "sine_multiplier_upper": str(sine_multiplier),
            "T_tail_upper": str(T_upper),
            "S_low_theta_upper": str(S_theta_low),
            "S_high_theta_upper": str(S_theta_high),
            "beta_S_upper": str(beta_S_upper),
            "beta_H_expected_upper": str(beta_H_expected),
            "expected_x_upper": str(expected_x),
            "expected_x2_upper": str(expected_x2),
            "partial_h_log_L_abs_upper": str(h_log_abs),
            "absolute_weight_ledger_upper": str(weight_abs_sum),
            "derivative_average_upper": str(derivative_average),
            "tail_derivative_upper": str(tail_upper),
        },
        "checks": checks,
        "claims": {
            "absolute_tail_derivative_lt_1e_minus_3": True,
            "full_F_phase_sign": "NOT PROVED",
            "existence_or_uniqueness": "NOT PROVED",
            "new_index_scan": "NONE",
        },
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
