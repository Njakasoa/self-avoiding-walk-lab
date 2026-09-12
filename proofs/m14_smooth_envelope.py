"""Exact ledger for the M14 fixed-s smooth-product envelope.

The analytic companion note uses the reviewed inverse-kernel factorization
of M11.  This file checks only the rational implications and the two small
I384 scalar derivative boxes needed to control the odd root separation and
the even phase-centre shift.  It does not scan indices or evaluate a phase
endpoint.
"""

from __future__ import annotations

import json
from fractions import Fraction as F

from proofs.m10_beta_real import Jet3, j3
from proofs.m7_finite_poles import I384


BITS = 384
SCALE = 1 << BITS

if not __debug__:
    raise RuntimeError("run without -O: I384 and exact ledger guards are required")


def _log_second(value: Jet3) -> I384:
    value.x.positive("log-second denominator")
    return value.d2 / value.x - (value.d1 / value.x) ** 2


def _log_third(value: Jet3) -> I384:
    value.x.positive("log-third denominator")
    return (
        value.d3 / value.x
        - 3 * value.d2 * value.d1 / (value.x**2)
        + 2 * value.d1**3 / (value.x**3)
    )


def _scalar_jets() -> dict[str, Jet3 | I384]:
    """Rebuild the signed M10 scalar jets without modifying M10 sources."""
    sigma = I384(2).sqrt() - 1
    t_box = I384(
        sigma.lo - I384(F(1, 8 * 180**2)).hi,
        sigma.hi,
        raw=True,
    )
    q_box = I384(F(359, 360), F(1003, 1000))

    t0 = j3(Jet3(t_box, I384(0), I384(0), I384(0)))
    q = Jet3(q_box, -q_box / 2, q_box / 4, -q_box / 8)
    a1 = -1 / (t0.x**2) + 1 + 2 * t0.x
    a2 = 2 / (t0.x**3) + 2
    a3 = -6 / (t0.x**4)
    sinh = (1 / q.x - q.x) / 2
    cosh = (q.x + 1 / q.x) / 2
    t1 = sinh / a1
    t2 = (cosh / 2 - a2 * t1 * t1) / a1
    t3 = (sinh / 4 - a3 * t1 * t1 * t1 - 3 * a2 * t1 * t2) / a1
    t = Jet3(t_box, t1, t2, t3)

    D = 1 - t * q
    C = q - t
    t_sq = t * t
    f_c = D - t_sq
    f_one = 1 - t_sq
    for name, value in (
        ("q", q.x),
        ("D-t^2", f_c.x),
        ("D", D.x),
        ("C", C.x),
        ("1-t^2", f_one.x),
    ):
        value.positive(name)

    s_g_1 = (
        -q.d1 / q.x
        - f_c.d1 / f_c.x
        + D.d1 / D.x
        + f_one.d1 / f_one.x
    )
    s_g_2 = (
        -_log_second(q)
        - _log_second(f_c)
        + _log_second(D)
        + _log_second(f_one)
    )
    s_g_3 = (
        -_log_third(q)
        - _log_third(f_c)
        + _log_third(D)
        + _log_third(f_one)
    )
    u_g = t / D
    return {
        "sigma": sigma,
        "t": t,
        "q": q,
        "C": C,
        "D": D,
        "s_g_1": s_g_1,
        "s_g_2": s_g_2,
        "s_g_3": s_g_3,
        "u_g": u_g,
    }


def produce() -> dict:
    checks: dict[str, bool] = {}
    input_compatibility: dict[str, bool] = {}

    def require(name: str, condition: bool) -> None:
        if not condition:
            raise ArithmeticError(name)
        checks[name] = True

    def require_input_compatibility(name: str, condition: bool) -> None:
        """Check rational compatibility without certifying an analytic box."""
        if not condition:
            raise ArithmeticError(name)
        input_compatibility[name] = True

    E = F(17, 51200)  # .17/512, the practical large-N domain
    t_l, t_h = F(207, 500), F(83, 200)
    q_l = F(359, 360)
    ug_l, ug_h = F(7, 10), F(71, 100)
    eta_l, eta_h = F(7, 10), F(17, 24)
    p_min = ug_l * (1 - ug_h)
    p0_min = eta_l * (1 - eta_h)

    require("e_upper_lt_1_over_1000", E < F(1, 1000))
    require("e_upper_lt_1_over_100", E < F(1, 100))
    require("critical_eta_upper", 2 * 17**2 > 24**2)
    # 3*eta_h is the rational endpoint; the strict radical check above gives
    # 3*eta<3*eta_h=17/8.
    require("critical_tv_rational_endpoint_eq_17_over_8", 3 * eta_h == F(17, 8))
    require("critical_tv_upper_lt_9_over_4", 3 * eta_h < F(9, 4))
    # These are only compatibility checks for inherited M5/M10 boxes.  The
    # analytic box statements are inputs, so they are kept out of `checks`.
    require_input_compatibility("t_box_lower_compatibility", t_l > F(2, 5))
    require_input_compatibility("t_box_upper_compatibility", t_h <= F(83, 200))
    require_input_compatibility("q_box_lower_compatibility", 1 - E / 2 > q_l)
    require_input_compatibility(
        "weight_box_compatibility",
        ug_l >= F(7, 10) and ug_h <= F(71, 100),
    )
    require("positive_common_denominator", p_min == F(203, 1000))
    require("critical_common_denominator_above_p_min", p0_min > p_min)

    jets = _scalar_jets()
    s_g_2 = jets["s_g_2"]
    s_g_3 = jets["s_g_3"]
    u_g = jets["u_g"]
    ug_3 = u_g.d3
    require("scalar_sg_second_abs_lt_1_over_20", s_g_2.lo > -F(1, 20) * SCALE and s_g_2.hi < F(1, 20) * SCALE)
    require("scalar_sg_third_abs_lt_414_over_1000", s_g_3.lo > -F(414, 1000) * SCALE and s_g_3.hi < F(414, 1000) * SCALE)
    require("scalar_ug_third_abs_lt_3_over_10", ug_3.lo > -F(3, 10) * SCALE and ug_3.hi < F(3, 10) * SCALE)
    require("scalar_ug_first_box", u_g.d1.lo > -F(26, 100) * SCALE and u_g.d1.hi < 0)

    # The exact odd/even Taylor consequences used in the fixed-s comparison.
    d_over_e_error = F(1, 10) * E * E  # |(h-u_g)/e - 1/2| <= e^2/10
    midpoint_error = E * E / 40
    beta_error = F(7, 50) * E * E
    require("odd_root_separation_error", d_over_e_error / p_min < F(1, 2) * E)
    require("even_beta_error_coefficient", F(7, 50) < F(1, 5))
    eta_tight = F(99, 140)
    require("critical_eta_tight_upper", eta_tight * eta_tight > F(1, 2))
    require("beta_upper_below_eta_h", eta_tight + beta_error < eta_h)
    require("root_midpoint_error", midpoint_error < E * E / 39)

    # The elementary U_t monotonicity proof gives |u_e(s)-u_0(s)|<e/2,
    # including s=0.  Its rational core is checked independently here.
    half = F(1, 2)
    v_half = (half - t_h) * (1 - t_h * half) / (
        t_h * (1 - t_h * t_h) * half
    )
    require("kernel_half_level_v_gt_3_over_8", v_half > F(3, 8))
    require(
        "exp_one_positive_series_lower",
        F(1) + F(1) + F(1, 2) + F(1, 6) == F(8, 3),
    )
    # All factors in the U_tv numerator are recorded separately.  The
    # A_t endpoint is only 39/10 on this deliberately widened t-box.
    a_t_lower = 1 / t_h**2 - 1 - 2 * t_h
    c_t_lower = 1 - t_h**2
    b_zero_upper = 1 / t_l + t_l
    delta_upper = b_zero_upper**2 - 4
    require("kernel_A_t_lower_gt_39_over_10", a_t_lower > F(39, 10))
    require("kernel_c_t_lower_gt_4_over_5", c_t_lower > F(4, 5))
    require("kernel_B_zero_upper_lt_29_over_10", b_zero_upper < F(29, 10))
    require("kernel_delta_upper_lt_41_over_10", delta_upper < F(41, 10))
    require("kernel_two_t_upper_le_83_over_100", 2 * t_h <= F(83, 100))
    require(
        "kernel_monotonicity_margin",
        F(39, 10) * F(4, 5) * 2 > F(83, 100) * F(41, 10),
    )

    # Fixed-s factorization: combine the two rational factors before taking
    # logs.  This keeps the cancellation in h-u_g instead of paying two
    # independent logarithm bounds.
    c_a_low = F(51, 100) / (ug_l * (1 - ug_h))
    c_a_high = F(51, 100) / (ug_l * (1 - half * ug_h))
    c_m_low = F(18, 25) * F(3, 5)
    c_m_high = F(18, 25)
    c_low = c_a_low + c_m_low
    c_high = c_a_high + c_m_high
    require("low_s_A_coefficient", c_a_low == F(510, 203))
    require("high_s_A_coefficient", c_a_high == F(340, 301))
    require("M_density_low_s_lt_3_over_5", c_m_low == F(54, 125))
    require("logR_over_e_low_s_lt_3", c_low < 3)
    require("logR_over_e_high_s_lt_37_over_20", c_high < F(37, 20))

    # Critical Taylor comparison.  p_e=u_g(1-u h), p_0=eta(1-u_0 eta).
    p_motion = F(4, 5)  # |p_e-p_0|<4e/5 from the kernel half-e bound
    p_inverse_term = F(1, 2) * p_motion / (p_min * p_min)
    d_inverse_term = d_over_e_error / p_min / E
    log_remainder = F(1, 2) * c_a_low * c_a_low
    require("denominator_motion_lt_10", p_inverse_term < 10)
    require("odd_separation_term_lt_half", d_inverse_term < F(1, 2))
    require("log_remainder_lt_4", log_remainder < 4)
    require("A_motion_terms_lt_11", p_inverse_term + d_inverse_term < 11)
    A_error = F(15)  # 11e from denominators/separation and 4e from log remainder

    M_error = F(7, 50) * E + eta_h * (F(9, 200) + E / 160)
    require("M_average_error_lt_1_over_5", M_error < F(1, 5))
    smooth_error = A_error + F(1, 5)
    require("normalized_logR_error_lt_16e", smooth_error < 16)

    # Scalar geometric factor: r=1-(1-exp(-e))/D and lambda=1/(1-sigma).
    d_box = F(29, 50)
    d_variation = F(21, 100)
    ratio_error = F(1, 2) / d_box + d_variation / (d_box * d_box)
    r_log_remainder = F(1, 2) / (d_box * (d_box - E))
    require("D_variation_coefficient", F(83, 400) + F(1, 800) < d_variation)
    require("r_small_parameter_lt_1_over_1000", E / d_box < F(1, 1000))
    require("r_ratio_error_lt_3_over_2", ratio_error < F(3, 2))
    require("r_log_remainder_lt_2", r_log_remainder < 2)
    require("normalized_log_r_error_lt_4e", ratio_error + r_log_remainder < 4)

    # Rectangle variation and the resulting product envelope.
    logK_x_coefficient = F(16) + F(4)
    logK_constant = F(17, 8)
    require("logK_x_coefficient_eq_20", logK_x_coefficient == 20)

    return {
        "classification": "EXACT I384 PLUS FRACTION M14 SMOOTH ENVELOPE",
        "status": "pass",
        "domain": {
            "e": "0<e<=17/51200=0.17/512",
            "s": "s>=0",
            "x": "x=ne for integer n>=0",
        },
        "analytic_hypotheses": [
            "M11 inverse-kernel factorization and 0<R_e(s)<=1",
            "M11 real boxes .414<t<.415, .997<q<1, .70<u_g,h<.71",
            "physical inverse-kernel transfer |U(t,e^-s)-U(sigma,e^-s)|<e/2, including s=0",
            "critical identity psi=-eta-u_0/[2(1-eta*u_0)]+eta*partial_a log M(s,c)",
            "critical profile monotonicity gives TV(psi)<17/8",
        ],
        "fraction_bounds": {
            "e_upper": str(E),
            "p_min": str(p_min),
            "d_over_e_error": str(d_over_e_error),
            "beta_error": str(beta_error),
            "midpoint_error": str(midpoint_error),
            "logR_low_s_upper": str(c_low),
            "logR_high_s_upper": str(c_high),
            "A_normalized_error_upper": str(A_error),
            "M_normalized_error_upper": str(M_error),
            "normalized_logR_error_upper": str(smooth_error),
            "normalized_log_r_error_upper": str(ratio_error + r_log_remainder),
            "critical_TV_upper": str(logK_constant),
            "logK_x_coefficient": str(logK_x_coefficient),
        },
        "input_compatibility": input_compatibility,
        "claims": {
            "fixed_s_logR_low_s": True,
            "fixed_s_logR_high_s": True,
            "normalized_logR_critical_error_lt_16e": True,
            "normalized_log_r_critical_error_lt_4e": True,
            "logK_critical_envelope_error": True,
            "endpoint_s_zero_included_without_derivative": True,
            "no_index_scan": True,
            "no_full_F_claim": True,
        },
        "envelope": {
            "critical_profile": "K0(x)=exp(-lambda*x+integral_0^x psi(s) ds)",
            "log_error": "|log K_e,n-log K0(ne)| < e*(17/8+20*ne)",
            "equivalent": "K0(ne)*exp(-e*(17/8+20*ne)) < K_e,n < K0(ne)*exp(e*(17/8+20*ne))",
            "direct_fixed_s": {
                "0<=s<=1": "-log R_e(s)/e < 74712/25375 < 3",
                "s>=1": "-log R_e(s)/e < 13918/7525 < 37/20",
            },
        },
        "checks": checks,
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
