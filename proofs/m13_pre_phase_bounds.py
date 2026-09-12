"""Exact arithmetic checks for the M13 pre-crossing phase bound.

This is an arithmetic ledger only.  It does not evaluate a phase point or
scan over N or theta.  The analytic inputs and their scopes are recorded in
M13_PRE_CROSSING_RESEARCH.md; this file checks the rational combinations used
there.
"""

from __future__ import annotations

import json
from fractions import Fraction as F


if not __debug__:
    raise RuntimeError("m13_pre_phase_bounds.py must run without -O")


def main() -> None:
    # For n <= N, x=n e < 17/100.  The elementary square-root replacement
    # sqrt((1-exp(-x))/3) < sqrt(17/300) < 239/1000 is checked exactly.
    sqrt_gap = F(239, 1000) ** 2 - F(17, 300)
    u_scaled = F(1, 210) + F(239, 1000)

    # On the pre mesh u_n >= u_g > .70.  The reviewed M10/M11 boxes
    # t in (.414,.4143), h in (.706,.71), delta_D < .07 give a stronger
    # combined-weight gap.  These are exact rational lower/upper boxes.
    t_l, t_h = F(207, 500), F(4143, 10000)
    u_l, h_l, h_h = F(7, 10), F(353, 500), F(71, 100)
    delta_h = F(7, 100)
    r_l = h_l / (1 - t_l * h_l) + u_l * (1 - h_l) / (
        (1 - t_l * u_l) * (1 - t_l * u_l * h_l)
    )
    gap_l = 4 * t_l * t_l * r_l - (1 - t_l + 2 * delta_h)
    d = 1 - t_h
    d_h = 1 - t_h * h_h
    ru_max = (1 - h_l) * (
        1 / (d * d * d_h) + t_h * h_h / (d * d_h * d_h)
    )
    vu_max = t_h / d
    weight_u_upper = vu_max + 4 * t_h * t_h * ru_max / F(1, 5)

    # A0 has a favorable quantitative derivative.  The elementary bound
    # used in the note is minimized at N=32 and e=17/(100*32).
    n32, e32 = F(32), F(17, 3200)
    a0_c_lower = n32 / (n32 + F(3, 5)) * (1 - e32 - e32 * e32)

    # The reviewed M11 weight decomposition: h,C are favorable; t contributes
    # <1/1000/N and delta contributes <2/5/N after the stronger gap.
    weight_upper = (
        F(6, 1) * F(61, 250)
        + F(1, 1000)
        + F(2, 5)
        - F(97, 100)
    )

    # M11 Eq. (26), with the pre-mesh u-motion allowance replacing .61 by
    # .244 in the anchor term.  Sum the moving-secant mesh term directly
    # instead of taking its per-factor maximum.
    anchor_mesh = F(51, 100) / (F(29, 100) ** 2) * F(61, 250)
    c_r = F(3, 4) + F(9, 5) + anchor_mesh + F(4, 5)
    pi_upper = c_r * F(17, 100) + F(2601, 1000000)
    r_upper = 2 * F(17, 100)
    smooth_upper = pi_upper + r_upper
    pre_upper = weight_upper + smooth_upper

    claims = {
        "sqrt_17_over_300_lt_239_over_1000": sqrt_gap > 0,
        "u_theta_scaled_lt_244_over_1000": u_scaled < F(244, 1000),
        "combined_gap_gt_1_over_5": gap_l > F(1, 5),
        "ru_max_lt_1511_over_1000": ru_max < F(1511, 1000),
        "weight_u_log_upper_lt_6": weight_u_upper < F(6),
        "a0_phase_decay_gt_0.97": a0_c_lower > F(97, 100),
        "weight_upper_le_0.895": weight_upper <= F(179, 200),
        "anchor_mesh_lt_1.48": anchor_mesh < F(148, 100),
        "pi_upper_lt_0.824": pi_upper < F(103, 125),
        "r_upper_eq_17_over_50": r_upper == F(17, 50),
        "smooth_upper_lt_1.164": smooth_upper < F(291, 250),
        "pre_upper_lt_2.06": pre_upper < F(103, 50),
    }
    assert all(claims.values())

    payload = {
        "kind": "m13_pre_phase_exact_arithmetic",
        "status": "pass",
        "claims": claims,
        "fractions": {
            "sqrt_gap": str(sqrt_gap),
            "u_theta_scaled": str(u_scaled),
            "combined_gap_lower": str(gap_l),
            "ru_max": str(ru_max),
            "vu_max": str(vu_max),
            "weight_u_log_upper": str(weight_u_upper),
            "a0_phase_decay_lower": str(a0_c_lower),
            "anchor_mesh": str(anchor_mesh),
            "c_r": str(c_r),
            "weight_upper": str(weight_upper),
            "pi_upper": str(pi_upper),
            "r_upper": str(r_upper),
            "smooth_upper": str(smooth_upper),
            "pre_upper": str(pre_upper),
        },
        "decimals": {
            "u_theta_scaled": float(u_scaled),
            "combined_gap_lower": float(gap_l),
            "ru_max": float(ru_max),
            "vu_max": float(vu_max),
            "weight_u_log_upper": float(weight_u_upper),
            "a0_phase_decay_lower": float(a0_c_lower),
            "anchor_mesh": float(anchor_mesh),
            "c_r": float(c_r),
            "weight_upper": float(weight_upper),
            "pi_upper": float(pi_upper),
            "smooth_upper": float(smooth_upper),
            "pre_upper": float(pre_upper),
        },
        "scope": {
            "N": "N>=32",
            "theta": "[4/5,9/10]",
            "pre_indices": "0<=n<=N",
            "input": "reviewed M10/M11 real lemmas; no point scan",
            "inherited_kernel_lower": "u_n >= u_g > 7/10, proved analytically in the note and M11; not an arithmetic claim",
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
