"""Exact Fraction replay of the displayed M9 linear-bound allowances.

This checker certifies arithmetic only.  The analytic hypotheses are returned
separately and remain obligations of the corresponding proof notes/reviews.
Every guard is an explicit conditional raise, so the checker also works with
python -O.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from typing import Any


def _text(value: Any) -> str:
    if isinstance(value, F):
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value.numerator}/{value.denominator}"
    return str(value)


def _entry(value: F, bound: F, relation: str) -> dict[str, str]:
    return {
        "value": _text(value),
        "bound": _text(bound),
        "relation": relation,
    }


def _less(checks: dict[str, Any], name: str, value: F, bound: F) -> None:
    if not value < bound:
        raise ArithmeticError(
            f"{name}: expected {_text(value)} < {_text(bound)}"
        )
    checks[name] = _entry(value, bound, "<")


def _leq(checks: dict[str, Any], name: str, value: F, bound: F) -> None:
    if not value <= bound:
        raise ArithmeticError(
            f"{name}: expected {_text(value)} <= {_text(bound)}"
        )
    checks[name] = _entry(value, bound, "<=")


def _greater(checks: dict[str, Any], name: str, value: F, bound: F) -> None:
    if not value > bound:
        raise ArithmeticError(
            f"{name}: expected {_text(value)} > {_text(bound)}"
        )
    checks[name] = _entry(value, bound, ">")


def _equal(checks: dict[str, Any], name: str, value: F, target: F) -> None:
    if value != target:
        raise ArithmeticError(
            f"{name}: expected {_text(value)} == {_text(target)}"
        )
    checks[name] = {
        "value": _text(value),
        "target": _text(target),
        "relation": "==",
    }


def _section(
    checks: dict[str, Any], section: str, name: str, fn, *args: F
) -> None:
    bucket = checks.setdefault(section, {})
    fn(bucket, name, *args)


def produce() -> dict[str, Any]:
    """Run the exact rational M9 arithmetic ledger and return JSON data."""

    checks: dict[str, Any] = {}

    # M9_PRODUCT_VARIATION.md: exterior and middle variation.
    sigma_lo = F(2, 5)
    sigma_hi = F(83, 200)
    sigma_sq_lo = sigma_lo * sigma_lo
    sigma_sq_hi = sigma_hi * sigma_hi
    _section(checks, "total_variation", "sigma_square_lower_reference",
             _equal, sigma_sq_lo, F(4, 25))
    _section(checks, "total_variation", "sigma_square_upper",
             _less, sigma_sq_hi, F(9, 50))
    _section(checks, "total_variation", "one_minus_sigma_lower",
             _greater, 1 - sigma_hi, F(29, 50))
    _section(checks, "total_variation", "kappa_coarse_ratio",
             _equal, F(9, 50) / F(29, 50), F(9, 29))
    kappa_from_sigma_box = sigma_sq_hi / (1 - sigma_hi)
    _section(checks, "total_variation", "kappa_upper",
             _less, kappa_from_sigma_box, F(9, 29))
    _section(checks, "total_variation", "eta_square_below_one",
             _less, F(1, 2), F(1))

    eta_exterior = F(40, 3) + F(25, 2)
    _section(checks, "total_variation", "eta_exterior",
             _less, eta_exterior, F(27))
    vg = F(9, 29) * 2 * (F(1000) + F(25, 4))
    _section(checks, "total_variation", "g_exterior",
             _less, vg, F(625))
    exterior = eta_exterior + vg
    _section(checks, "total_variation", "exterior_total",
             _less, exterior, F(700))
    middle = F(3 * 10**9)
    _section(checks, "total_variation", "middle_total",
             _equal, middle, F(3 * 10**9))
    tv_ledger = middle + F(700)
    _section(checks, "total_variation", "total_variation_bound",
             _less, tv_ledger, F(4 * 10**9))

    B = F(10**12)
    _section(checks, "total_variation", "B_dominates_TV",
             _less, F(4 * 10**9), B)
    _section(checks, "total_variation", "B_dominates_scalar_log",
             _less, F(10), B)

    # M9_COMPLEX_KERNEL_LINEAR.md: linear comparison and N>=10^15 domain.
    e0_sector = F(1, 10**8)
    e0_domain = F(1, 10**15)
    _section(checks, "complex_domain", "domain_inside_sector",
             _leq, e0_domain, e0_sector)
    _section(checks, "complex_domain", "fixed_point_threshold",
             _greater, F(10**15), F(10**6))
    _section(checks, "complex_domain", "sector_threshold",
             _leq, e0_domain, F(1, 10**8))

    x_max = F(4)
    delta_polynomial_left = F(160) * (
        e0_domain * e0_domain / 5 + 2 * e0_domain * x_max
    )
    delta_polynomial_right = F(320) * e0_domain * (e0_domain + x_max)
    _section(checks, "complex_domain", "discriminant_difference_scale",
             _leq, delta_polynomial_left, delta_polynomial_right)

    sqrt_scale = F(320) * 3 / F(6, 100)
    _section(checks, "complex_domain", "square_root_constant",
             _equal, sqrt_scale, F(16000))

    quotient_coefficient = (
        2 * (e0_sector * e0_sector / 5) / F(8, 10)
        + F(83, 100) * (F(16130) * e0_sector) / F(8, 10) ** 2
    ) / e0_sector
    _section(checks, "complex_domain", "kernel_quotient_coefficient",
             _equal, quotient_coefficient,
             F(4183718750001, 200000000))
    _section(checks, "complex_domain", "kernel_quotient_constant",
             _less, quotient_coefficient, F(25000))

    root_fraction = F(5 * 10**8)
    g_fraction = (
        F(200) / F(9, 10000)
        + F(3, 10) * F(16000) / (F(9, 10000) * F(1, 1000))
    )
    _section(checks, "complex_domain", "exterior_root_fraction",
             _less, root_fraction, F(6 * 10**9))
    _section(checks, "complex_domain", "exterior_g_fraction",
             _less, g_fraction, F(6 * 10**9))
    log_remainder = F(4) * (F(21) ** 2 + F(335) ** 2)
    _section(checks, "complex_domain", "logarithm_remainder",
             _equal, log_remainder, F(450664))
    _section(checks, "complex_domain", "logarithm_remainder_allowance",
             _less, log_remainder, F(5 * 10**6))

    common_linear = (
        F(2 * 10**12) + root_fraction + F(6 * 10**9) + F(5 * 10**6)
    )
    _section(checks, "complex_domain", "common_linear_error",
             _less, common_linear, F(10**13))
    prefix_sum = F(10**14) * e0_domain
    _section(checks, "complex_domain", "prefix_sum_at_domain",
             _leq, prefix_sum, F(1, 10))
    _section(checks, "complex_domain", "prefix_sum_below_half",
             _less, prefix_sum, F(1, 2))

    _section(checks, "complex_domain", "exterior_g_loss",
             _leq, F(16000) * e0_domain, F(16, 10**12))
    _section(checks, "complex_domain", "root_displacement",
             _equal, F(48) * e0_domain, F(48, 10**15))
    _section(checks, "complex_domain", "eta_perturbation",
             _equal, F(2 * 10**7) * e0_domain, F(2, 10**8))
    _section(checks, "complex_domain", "scalar_damping",
             _equal, F(4 * 10**6) * e0_domain, F(4, 10**9))

    omega_left = F(78, 100)
    omega_right = F(92, 100)
    _section(checks, "complex_domain", "omega_contains_real_band_left",
             _less, omega_left, F(4, 5))
    _section(checks, "complex_domain", "omega_contains_real_band_right",
             _less, F(9, 10), omega_right)
    rho = F(22, 15)
    rho_inverse = 1 / rho
    ellipse_horizontal = (rho + rho_inverse) / 40
    ellipse_vertical = (rho - rho_inverse) / 40
    _section(checks, "complex_domain", "ellipse_horizontal_margin",
             _less, ellipse_horizontal, F(7, 100))
    _section(checks, "complex_domain", "ellipse_vertical_margin",
             _less, ellipse_vertical, F(2, 100))

    complex_norm = F(80_000_000 + 4_800_000 + 100)
    _section(checks, "complex_domain", "joint_norm_ledger",
             _less, complex_norm, F(10**8))

    # M9_LINEAR_MOMENT_RATE.md: critical weights, primitive and replacement
    # ledger.  These are arithmetic checks around the stated analytic inputs.
    K_eta = F(300_000)
    _section(checks, "critical_weights", "lambda_upper",
             _less, F(1) / (1 - sigma_hi), F(2))
    weight_moment = F(40) + F(80) * F(2)
    _section(checks, "critical_weights", "weighted_variation_moment",
             _equal, weight_moment, F(200))
    local_psi = F(3, 10) * F(50) / (F(2, 5) * F(4, 100))
    _section(checks, "critical_weights", "local_psi_bound",
             _less, local_psi, F(1000))
    kernel_derivative = F(315, 1000) / F(17, 100)
    _section(checks, "critical_weights", "kernel_derivative_bound",
             _less, kernel_derivative, F(2))
    density = F(40) * (F(1000) + F(2)) + F(100)
    _section(checks, "critical_weights", "local_density_bound",
             _less, density, F(41000))

    ce_coefficient = (
        F(4, 10) / F(28, 100)
        + F(17, 100) * K_eta / (F(28, 100) * F(29, 100))
        + F(1)
    )
    _section(checks, "primitive_ledger", "boundary_constant",
             _less, ce_coefficient, 4 * K_eta)
    q_e = F(104, 10) / F(28, 100) * F(2000)
    q_cont = F(10) / F(29, 100) * F(20)
    _section(checks, "primitive_ledger", "closest_Qe",
             _less, q_e, F(75000))
    _section(checks, "primitive_ledger", "closest_Q",
             _less, q_cont, F(700))
    _section(checks, "primitive_ledger", "closest_sum",
             _less, q_e + q_cont, F(76000))

    far_local = F(41000) * F(2 * 10**4) * F(40)
    near_local = F(41000) * F(76000) * F(21)
    cell_local = F(41000) * F(80)
    _section(checks, "primitive_ledger", "far_local",
             _less, far_local, F(4 * 10**10) )
    _section(checks, "primitive_ledger", "near_local",
             _less, near_local, F(7 * 10**10))
    _section(checks, "primitive_ledger", "cell_interpolation",
             _less, cell_local, F(4 * 10**6))

    outside_weighted = F(4 * 10**5) * F(200)
    _section(checks, "primitive_ledger", "outside_weighted",
             _equal, outside_weighted, F(8 * 10**7))
    primitive_total = (
        far_local * K_eta + near_local + F(4 * 10**6)
        + outside_weighted * K_eta + F(160) * K_eta
    )
    _section(checks, "primitive_ledger", "primitive_total",
             _equal, primitive_total, F(9_864_065_488_000_000))
    _section(checks, "primitive_ledger", "primitive_total_allowance",
             _less, primitive_total, F(6 * 10**10) * K_eta)

    per_moment = (
        F(144_000_000) * B
        + F(720_000_000)
        + F(48_000_000)
        + F(600_000_000_000) * K_eta
    )
    final_coefficient = 2 * per_moment + F(10**14)
    _section(checks, "primitive_ledger", "final_coefficient",
             _equal, final_coefficient, F(288_360_100_001_536_000_000))
    _section(checks, "primitive_ledger", "final_coefficient_allowance",
             _less, final_coefficient, F(10**21))

    # M9_UNIQUENESS_THRESHOLD.md: N=10^27 Chebyshev, endpoint and slope
    # allowances, all exact rational arithmetic.
    N_unique = F(10**27)
    E = F(10**21) / N_unique
    M = F(10**8 + 100)
    q = F(15, 22)
    m = 97
    k = m + 1
    A_m = 2 * M * q**k / (1 - q)
    B_m = 40 * M * q**k * (
        F(k * k) / (1 - q)
        + F(2 * k) * q / (1 - q) ** 2
        + q * (1 + q) / (1 - q) ** 3
    )
    derivative_error = F(20 * m * m) * (E + A_m) + B_m
    _section(checks, "uniqueness_threshold", "E_at_N_1e27",
             _equal, E, F(1, 10**6))
    _section(checks, "uniqueness_threshold", "chebyshev_q",
             _equal, q, F(15, 22))
    _section(checks, "uniqueness_threshold", "chebyshev_degree",
             _equal, F(m), F(97))
    _section(checks, "uniqueness_threshold", "chebyshev_M",
             _equal, M, F(100_000_100))
    _section(checks, "uniqueness_threshold", "derivative_error",
             _less, derivative_error, F(201, 1000))

    # Directed logarithm and denominator sign ledger.
    exp2_partial = F(1) + F(2) + F(2**2, 2) + F(2**3, 6)
    exp2_tail = F(2**4, 24) / (1 - F(2, 5))
    _section(checks, "uniqueness_threshold", "exp2_upper",
             _less, exp2_partial + exp2_tail, F(10))
    exp3_partial = F(1) + F(3) + F(3**2, 2) + F(3**3, 6)
    _section(checks, "uniqueness_threshold", "exp3_lower",
             _greater, exp3_partial, F(10))
    directed_remainder = F(2700 * 3, 10**27)
    _section(checks, "uniqueness_threshold", "directed_remainder",
             _less, directed_remainder, F(3, 4))
    delta_upper = F(42, 100) / F(54)
    _section(checks, "uniqueness_threshold", "delta_sigma_over_log",
             _less, delta_upper, F(1, 125))
    _section(checks, "uniqueness_threshold", "delta_upper",
             _less, F(42, 100) / F(54), F(1, 125))

    lower_pn = -F(15, 2) - E
    upper_pn = -F(18, 5) + E
    _section(checks, "uniqueness_threshold", "numerator_lower",
             _greater, lower_pn, -F(8))
    _section(checks, "uniqueness_threshold", "numerator_upper",
             _less, upper_pn, -F(7, 2))
    f_left = F(1) - F(3, 20)
    f_right = -F(1, 5) + F(3, 20)
    _section(checks, "uniqueness_threshold", "left_endpoint",
             _greater, f_left, F(0))
    _section(checks, "uniqueness_threshold", "right_endpoint",
             _less, f_right, F(0))
    denominator_error = 4 * E + 2 * F(1, 10**54) + 16 * F(1, 125)
    _section(checks, "uniqueness_threshold", "denominator_comparison",
             _less, denominator_error, F(3, 20))
    denom_upper = F(3, 5) + F(2, 125)
    _section(checks, "uniqueness_threshold", "denominator_upper",
             _less, denom_upper, F(1))

    e2_term = F(18, 10**54)
    n_term = F(480_000, 10**27)
    derivative_upper = (
        -F(6) + 4 * F(201, 1000) + F(150, 125)
        + e2_term + n_term
    )
    _section(checks, "uniqueness_threshold", "F_prime_upper",
             _less, derivative_upper, -F(39, 10))
    _section(checks, "uniqueness_threshold", "F_prime_absolute_lower",
             _greater, F(39, 10), F(1))
    _section(checks, "uniqueness_threshold", "E1_allowance",
             _less, derivative_error, F(201, 1000))
    finite_Fprime_abs_upper = (
        F(26) + 4 * F(201, 1000) + F(150, 125)
        + e2_term + n_term
    )
    _section(checks, "uniqueness_threshold", "F_prime_absolute_upper",
             _less, finite_Fprime_abs_upper, F(29))

    # M9_PHASE_RESIDUE_RATE.md: phase, Jacobian and coarse residue ledgers.
    R_theta = F(5, 24) * (
        4 * E + 2 * F(1, 10**54) + F(285, 54 * 10**27)
    )
    _section(checks, "phase_residue_rate", "R_theta",
             _less, R_theta, F(834, 10**9))
    _section(checks, "phase_residue_rate", "R_theta_position",
             _less, R_theta / 7, F(12, 10**8))
    curvature = (F(26) + F(150, 125)) * F(45)
    _section(checks, "phase_residue_rate", "curvature",
             _less, curvature, F(1300))
    quotient = F(75, 10) * F(37, 10_000) / F(24, 5)
    _section(checks, "phase_residue_rate", "quotient_error",
             _less, quotient, F(6, 1000))
    jacobian_slack = F(18, 10) * F(37, 10_000) + F(16 * 10**6, 10**27)
    _section(checks, "phase_residue_rate", "jacobian_slack",
             _less, jacobian_slack, F(1))
    jacobian_lower = F(15, 100) ** 2 / 8 - F(1, 10**27)
    jacobian_upper = F(37, 10_000) + F(1, 10**27)
    _section(checks, "phase_residue_rate", "jacobian_normalized_lower",
             _greater, jacobian_lower, F(28, 10_000))
    _section(checks, "phase_residue_rate", "jacobian_normalized_upper",
             _less, jacobian_upper, F(4, 1000))

    # The final coarse residue signs use the displayed analytic hypotheses
    # |F_N'|<29, 3.5<|1+P_N|<8 and .0028<J_N<.004.
    residue_lower = F(35, 10) * F(28, 10_000) / F(29)
    residue_upper = F(8) * F(4, 1000) / F(39, 10)
    _section(checks, "phase_residue_rate", "coarse_residue_lower",
             _greater, residue_lower, F(1, 6000))
    _section(checks, "phase_residue_rate", "coarse_residue_upper",
             _less, residue_upper, F(1, 20))

    return {
        "status": "PASS",
        "classification": (
            "EXACT FRACTION ARITHMETIC ONLY; analytic hypotheses are "
            "listed separately and require proof/review"
        ),
        "scope": {
            "complex_domain": "N>=10^15",
            "moment_error": "|P_N-P0|+|H_N-H0|<10^21 e",
            "uniqueness_threshold": "N>=10^27",
            "phase_residue_scope": "N>=10^27",
            "novelty_claim": False,
            "frozen_sources_edited": False,
        },
        "constants": {
            "B": _text(B),
            "K_eta": _text(K_eta),
            "N_complex": "10^15",
            "N_unique": "10^27",
            "e_error": _text(E),
            "chebyshev_M": _text(M),
            "chebyshev_q": _text(q),
            "chebyshev_degree": m,
            "derivative_allowance": "201/1000",
            "F_prime_upper_allowance": "-39/10",
            "coarse_F_prime_absolute_upper": "29",
            "R_theta_upper_allowance": "834/10^9",
            "final_coefficient": _text(final_coefficient),
        },
        "analytic_hypotheses": {
            "M9_PRODUCT_VARIATION": [
                "accepted M6 monotonicity and exterior g0 separation",
                "accepted removable critical value and middle Cauchy derivative bound",
                "accepted 0<R_e<=1, psi<=0, and scalar r damping",
            ],
            "M9_COMPLEX_KERNEL_LINEAR": [
                "inherited M7 principal-root sector and polynomial derivative bounds",
                "M8 phase inverse fixed point and exterior/root separation",
                "normal convergence, source-pole exclusion, and inherited norm ledger",
            ],
            "M9_LINEAR_MOMENT_RATE": [
                "accepted M8 discrete primitive identity and positive weight measure",
                "M6 gamma/product envelopes and M9 bounded-variation product estimate",
                "Tonelli, absolute continuity, and all pointwise kernel/weight hypotheses",
            ],
            "M9_UNIQUENESS_THRESHOLD": [
                "M9 linear moment error and complex holomorphy domain",
                "M5/M6 critical endpoint margins and new M9 endpoint transfer",
                "M7 differentiated denominator identity",
                "directed logarithm bounds, source-pole exclusion, and phase Jacobian sign",
            ],
            "M9_PHASE_RESIDUE_RATE": [
                "M9 phase mean-value estimate and M8 analytic quotient decomposition",
                "Jacobian and numerator bounds, including |F_N'|<29",
                "local holomorphy and the displayed coarse residue sign hypotheses",
            ],
        },
        "checks": checks,
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
