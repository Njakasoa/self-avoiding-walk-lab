"""Exact arithmetic checks for the M11 smooth-factor phase bound.

The analytic note proves the inverse-kernel factorization and reduces the
mesh derivative to elementary rational allowances.  This checker reuses the
signed I384 phase box from m10_beta_real for the only nontrivial scalar
boxes: s_g'(e), u_g(e), and u_g'(e).  It does not scan N or theta.
"""

from __future__ import annotations

import json
from fractions import Fraction as F

from proofs.m10_beta_real import Jet3, j3
from proofs.m7_finite_poles import I384


BITS = 384
SCALE = 1 << BITS

if not __debug__:
    raise RuntimeError("run without -O: I384 assertions are required")


def _lt(value: I384, bound: F) -> bool:
    return value.hi < bound * SCALE


def _gt(value: I384, bound: F) -> bool:
    return value.lo > bound * SCALE


def _build_scalar_jets() -> dict[str, Jet3 | I384]:
    """Rebuild the signed M10 t/q jets and the needed first derivatives."""

    sigma = I384(2).sqrt() - 1
    t_box = I384(
        sigma.lo - I384(F(1, 180**2 * 8)).hi,
        sigma.hi,
        raw=True,
    )
    q_box = I384(F(359, 360), F(1003, 1000))

    t0 = j3(Jet3(t_box, I384(0), I384(0), I384(0)))
    q = Jet3(q_box, -q_box / 2, q_box / 4, -q_box / 8)
    a1 = -1 / (t0.x ** 2) + 1 + 2 * t0.x
    a2 = 2 / (t0.x ** 3) + 2
    a3 = -6 / (t0.x ** 4)
    sinh = (1 / q.x - q.x) / 2
    cosh = (q.x + 1 / q.x) / 2
    t1 = sinh / a1
    t2 = (cosh / 2 - a2 * t1 * t1) / a1
    t3 = (sinh / 4 - a3 * t1 * t1 * t1
          - 3 * a2 * t1 * t2) / a1
    t = Jet3(t_box, t1, t2, t3)

    d = 1 - t * q
    c = q - t
    t_sq = t * t
    f_c = d - t_sq
    f_one = 1 - t_sq

    # s_g=-log(q)-log(D-t^2)+log(D)+log(1-t^2).
    s_g_e = (-q.d1 / q.x
             - f_c.d1 / f_c.x
             + d.d1 / d.x
             + f_one.d1 / f_one.x)
    u_g = t / d
    h_direct = t * q / c
    return {
        "sigma": sigma,
        "t": t,
        "q": q,
        "C": c,
        "D": d,
        "s_g_e": s_g_e,
        "u_g": u_g,
        "h_direct": h_direct,
        "u_g_e": u_g.d1,
        "h_direct_e": h_direct.d1,
        "ratio_coefficient": t_sq.x / (c.x * d.x),
    }


def produce() -> dict:
    x = _build_scalar_jets()
    sigma = x["sigma"]
    t = x["t"]
    q = x["q"]
    c = x["C"]
    d = x["D"]
    c_value = c.x
    d_value = d.x
    s_g_e = x["s_g_e"]
    u_g = x["u_g"]
    u_g_e = x["u_g_e"]
    ratio_coefficient = x["ratio_coefficient"]

    # The h(e)=u_g(-e) symmetry transfers the u_g boxes to h and reverses
    # the derivative sign.  The direct h interval is retained diagnostically;
    # its independent t/q dependency is too loose for the .71 upper box.
    h_by_symmetry = u_g.x
    h_e_by_symmetry = -u_g_e

    anchor_ratio = 2 * F(26, 100) / F(70, 100)
    anchor_direct = 2 * F(26, 100) / F(29, 100)
    anchor_mesh = (
        F(51, 100) / F(29, 100) ** 2 * F(61, 100)
    )
    kernel_t_part = F(6, 7 * 180)
    kernel_v_part = F(3, 5)
    kernel_u_e_scaled = kernel_t_part + kernel_v_part
    # This bound is for the physical e>0 branch, where q<=1; it does not
    # reuse the signed q box (which necessarily also contains q>1).
    physical_t_e_coarse = F(1, 7 * 180)
    log_r_e_upper = (
        F(1, 2)
        + (F(1, 2) + F(1, 400)) / F(57, 100)
        + (F(1, 400) + F(83, 400)) / F(58, 100)
    )
    m_anchor = F(4, 5)
    m_mesh = F(18, 100) * F(102, 10)
    per_factor = (
        F(75, 100) + F(18, 10) + F(3721, 1000)
        + m_anchor + m_mesh
    )
    pi_phase_coefficient = F(9) * F(60) * F(17, 100)
    r_phase_coefficient = F(2) * F(60) * F(17, 100)
    smooth_k_coefficient = pi_phase_coefficient + r_phase_coefficient
    weight_coefficient = F(11)
    total_coefficient = smooth_k_coefficient + weight_coefficient
    postcrossing_margin = F(1435, 342) - total_coefficient / 32

    claims = {
        "t_lower_gt_0.414": _gt(t.x, F(414, 1000)),
        "q_lower_gt_0.99": _gt(q.x, F(99, 100)),
        "C_lower_gt_0.57": _gt(c_value, F(57, 100)),
        "D_lower_gt_0.58": _gt(d_value, F(58, 100)),
        "s_g_e_lower_gt_0.3": _gt(s_g_e, F(3, 10)),
        "s_g_e_upper_lt_0.4": _lt(s_g_e, F(2, 5)),
        "u_g_lower_gt_0.70": _gt(u_g.x, F(7, 10)),
        "u_g_upper_lt_0.71": _lt(u_g.x, F(71, 100)),
        "u_g_e_negative": u_g_e.hi < 0,
        "u_g_e_abs_lt_0.26": (
            u_g_e.lo > -F(26, 100) * SCALE
            and u_g_e.hi < F(26, 100) * SCALE
        ),
        "h_symmetry_lower_gt_0.70": _gt(h_by_symmetry, F(7, 10)),
        "h_symmetry_upper_lt_0.71": _lt(h_by_symmetry, F(71, 100)),
        "h_e_symmetry_positive": h_e_by_symmetry.lo > 0,
        "h_e_symmetry_abs_lt_0.26": (
            h_e_by_symmetry.hi < F(26, 100) * SCALE
        ),
        "h_minus_ug_coefficient_lt_0.51": (
            _lt(ratio_coefficient, F(51, 100))
        ),
        "physical_t_e_coarse_lt_1_over_400": (
            physical_t_e_coarse < F(1, 400)
        ),
        "log_r_e_upper_lt_2": log_r_e_upper < F(2),
        "kernel_u_e_scaled_lt_0.61": kernel_u_e_scaled < F(61, 100),
        "ug_over_h_log_derivative_lt_0.75": (
            anchor_ratio < F(75, 100)
        ),
        "anchor_direct_term_lt_1.8": (
            anchor_direct < F(18, 10)
        ),
        "anchor_mesh_term_lt_3.721": (
            anchor_mesh < F(3721, 1000)
        ),
        "M_anchor_term_le_0.8": m_anchor <= F(8, 10),
        "M_mesh_term_le_1.836": m_mesh <= F(1836, 1000),
        "per_factor_lt_9": per_factor < F(9),
        "pi_phase_coefficient_eq_91.8": pi_phase_coefficient == F(918, 10),
        "r_phase_coefficient_eq_20.4": r_phase_coefficient == F(204, 10),
        "smooth_K_coefficient_eq_112.2": (
            smooth_k_coefficient == F(1122, 10)
        ),
        "conditional_total_coefficient_eq_123.2": (
            total_coefficient == F(1232, 10)
        ),
        "conditional_postcrossing_margin_gt_0.345": (
            postcrossing_margin > F(345, 1000)
        ),
    }
    if not all(claims.values()):
        raise ArithmeticError(f"failed claims: {claims}")

    return {
        "classification": "EXACT I384 PLUS FRACTION M11 SMOOTH PHASE BOUNDS",
        "bits": BITS,
        "boxes": {
            "sigma": sigma.record(),
            "t": t.x.record(),
            "q": q.x.record(),
            "C": c_value.record(),
            "D": d_value.record(),
            "s_g_e": s_g_e.record(),
            "u_g": u_g.x.record(),
            "u_g_e": u_g_e.record(),
            "h_by_symmetry": h_by_symmetry.record(),
            "h_e_by_symmetry": h_e_by_symmetry.record(),
            "h_direct_diagnostic": x["h_direct"].x.record(),
            "h_direct_e_diagnostic": x["h_direct_e"].record(),
        },
        "fraction_bounds": {
            "ratio_h_minus_ug_over_e_upper": str(
                F(51, 100)
            ),
            "kernel_t_part": str(kernel_t_part),
            "kernel_v_part": str(kernel_v_part),
            "kernel_u_e_scaled_upper": str(kernel_u_e_scaled),
            "physical_t_e_coarse": str(physical_t_e_coarse),
            "log_r_e_upper": str(log_r_e_upper),
            "anchor_ratio_upper": str(anchor_ratio),
            "anchor_direct_upper": str(anchor_direct),
            "anchor_mesh_upper": str(anchor_mesh),
            "M_anchor_upper": str(m_anchor),
            "M_mesh_upper": str(m_mesh),
            "per_factor_upper": str(per_factor),
            "pi_phase_coefficient": str(pi_phase_coefficient),
            "r_phase_coefficient": str(r_phase_coefficient),
            "smooth_K_coefficient": str(smooth_k_coefficient),
            "conditional_total_coefficient": str(total_coefficient),
            "conditional_postcrossing_margin": str(postcrossing_margin),
        },
        "claims": claims,
        "status": "pass",
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
