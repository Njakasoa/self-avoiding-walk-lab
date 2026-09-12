"""Exact rational replay of the numerical allowances in M6_SHARP_KERNEL.

This checker deliberately covers only the arithmetic in the sharp local
box and the displayed real comparison constants.  It does not certify the
algebraic identities, branch choices, or the inherited M5 inequalities.
"""

from __future__ import annotations

from fractions import Fraction as F


def lt(name: str, value: F, bound: F) -> None:
    if not value < bound:
        raise AssertionError(f"{name}: {value} is not < {bound}")
    print(f"{name}: {value} < {bound}")


def main() -> None:
    # (7)--(8): algebraic s-derivative bounds.
    d = F(142, 100)
    a_s = F(315, 1000)
    w = F(17, 100)
    a = F(16, 10)
    lt("g_s", d * a_s / w, F(3))
    g_ss = d * (a_s / w + a_s * a_s / (w * w)
                + a * a_s * a_s / (w * w * w))
    lt("g_ss", g_ss, F(100))

    # (9)--(13): parameter and mixed derivative bounds.
    re = F(1, 100000)
    cauchy_radius = F(5, 10000)
    te = (cauchy_radius * cauchy_radius / 10) / (cauchy_radius - re)
    lt("t_e", te, F(2, 10000))
    qe = F(501, 1000)
    de = te * F(1001, 1000) + F(415, 1000) * qe
    lt("D_e", de, F(21, 100))

    wt = F(11) / (2 * w)
    lt("w_t", wt, F(33))
    ut = F(2) / F(85, 100) + (
        2 * F(415, 1000) * (F(23, 10) + F(33))
        / (F(85, 100) * F(85, 100))
    )
    lt("U_t", ut, F(45))
    ge = te + de + d * ut * te
    lt("g_e", ge, F(23, 100))

    a_se = F(2, 10000)
    u_e = F(9, 1000)
    w_e = F(66, 10000)
    g_es = (
        de * a_s / w
        + d * (a_se / w + a_s * u_e / w + a_s * w_e / (w * w))
    )
    lt("g_es", g_es, F(1))

    # (14)--(18): Rouché and crossing allowances.
    rs = F(1, 10000)
    circle = F(2, 5) * rs - F(100, 2) * rs * rs
    lt("g0_on_root_circle", F(3, 100000), circle)
    lt("root_perturbation", F(13, 1000000), circle)
    lt("s_g_shift/e", F(23, 100) / F(2, 100), F(12))
    lt("s_h_minus_s_g/e", F(3, 10) / F(2, 100), F(16))
    eta_error = F(1) / F(2, 100) + (
        F(3, 10) * F(6501) / (F(2, 100) * F(2, 5))
    )
    lt("eta_error/e", eta_error, F(300000))

    # (24)--(27): real square-root comparison, with e <= 10^-8.
    e = F(1, 100000000)
    dt = e * e / 8
    sqrt_diff = F(112, 100) * e
    lt("sqrt_delta_difference", 10 * dt, sqrt_diff * sqrt_diff)
    denominator_difference = F(24, 10) * dt + sqrt_diff
    u_difference = (
        2 * dt / F(8, 10)
        + 2 * F(415, 1000) * denominator_difference
        / (F(8, 10) * F(8, 10))
    )
    lt("U_t_minus_U_sigma", u_difference, 3 * e)
    g_difference = dt + F(22, 100) * e + F(6, 10) * (3 * e)
    lt("g_e_minus_g_0", g_difference, 3 * e)

    # Exterior logarithm ledger after the square-root comparison.
    first_linear = F(300000) / F(49, 1000) + (
        F(72, 100) * F(50) / (F(49, 1000) * F(5, 100))
    )
    second_linear = F(1) / F(99, 100000) + (
        F(3, 10) * F(3) / (F(99, 100000) * F(1, 1000))
    )
    first_remainder = 2 * (F(72, 100) / F(49, 1000)) ** 2
    second_remainder = 2 * (F(3, 10) / F(99, 100000)) ** 2
    lt("exterior_root_linear/e", first_linear, F(7000000))
    lt("exterior_kernel_linear/e", second_linear, F(2000000))
    lt("exterior_log_remainder/e", first_remainder + second_remainder,
       F(300000))

    # (35)--(36): remaining scalar P-inputs.
    d_lower = F(58, 100)
    d_error = F(22, 100)
    r_linear = F(1, 2) / d_lower + d_error / (d_lower * d_lower)
    r_remainder = 2 / (d_lower * d_lower)
    lt("(-log r)/e error coefficient", r_linear + r_remainder, F(10))
    lt("z0 error coefficient", F(52, 100) / (F(17, 100) ** 2),
       F(20))

    print("m6_sharp_kernel_boxes: PASS")


if __name__ == "__main__":
    main()
