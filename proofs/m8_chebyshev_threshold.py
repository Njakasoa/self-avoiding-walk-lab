"""Exact allowances for the M8 analytic-domain and Chebyshev threshold proof.

Arithmetic is independent of Python assertions. Analytic hypotheses need
the separate proof and its independent review.
"""
from fractions import Fraction as F
import json


def produce():
    checks = {}

    def require(name, condition):
        if not condition:
            raise ArithmeticError(name)
        checks[name] = True

    e0 = F(1, 10**30)
    require('phase_contraction_domain', 10**30 >= 10**6)
    require('kernel_sector_domain', e0 <= F(1, 10**8))
    require('eta_perturbation_below_point001', 2*10**7*e0 < F(1, 1000))
    require('exterior_root_separation', F(5,100)-48*e0 > F(49,1000))
    require('exterior_g_separation', F(1,1000)-1000*F(1,10**15) > F(9,10000))
    require('crossing_half_tube', 8*e0 < F(5,10**5))
    require('parameter_taylor_disk', e0 < F(1,2*10**5))
    require('compact_log_sum_below_half', 10**14*F(1,10**15) < F(1,2))
    require('r_damping', 4*10**6*e0 < F(6,10))
    require('delta_positive_real_part', 400*e0 < F(1,100))
    require('far_recurrence_contraction', F(405,10000)-F(804,10)*e0 > 0)
    require('complex_joint_norm_below_1e8', 8*10**7+48*10**5+100 < 10**8)
    rho = F(22,15)
    q = 1/rho
    require('ellipse_horizontal_inside_rectangle', (rho+q)/40 < F(7,100))
    require('ellipse_vertical_inside_rectangle', (rho-q)/40 < F(2,100))
    require('fourth_root_upper', F(5624,1000)**4 > 1000)
    require('square_root_upper', F(3163,1000)**2 > 10)
    E = F(5656,10**9)
    require('real_error_upper', F(5624,10**9)+F(3163,10**11)+F(1,10**43) < E)
    M = 10**8+100
    m = 92
    k = m+1
    A = 2*M*q**k/(1-q)
    B = 40*M*q**k*(k*k/(1-q)+2*k*q/(1-q)**2+q*(1+q)/(1-q)**3)
    derivative = 20*m*m*(E+A)+B
    require('derivative_error_below_1_point033', derivative < F(1033,1000))
    final = -6+4*F(1033,1000)+F(150,250)+F(18,10**114)+F(480000,10**57)
    require('F_prime_below_minus_one', final < -1)
    require('directed_reciprocal_coefficient_below_19', F(18,100)*102 < 19)
    require('phase_hat_derivative_margin', -6+F(150,250) == -F(27,5))
    require('kernel_derivative_over_e_below_one_seventh', F(1,8)+16*10**6*F(1,10**16) < F(1,7))
    phase = F(5,27)*(4*E+F(2,10**114)+F(285,114*10**57))
    require('phase_error_at_threshold_below_4_point19e_minus6', phase < F(419,10**8))
    require('spatial_error_scaled_N_cubed_below_6e_minus7', phase/7 < F(6,10**7))
    require('jacobian_error_coefficient_below_one', F(18,10)*F(37,10**4)+F(16*10**6,10**57) < 1)
    require('jacobian_normalized_lower', F(15,100)**2/8-F(1,10**57) > F(28,10**4))
    require('jacobian_normalized_upper', F(37,10**4)+F(1,10**57) < F(4,1000))
    require('critical_curvature_ratio_below_45', 8/F(18,100) < 45)
    require('resummed_second_derivative_below_1200', (26+F(150,250))*45 < 1200)
    require('residue_denominator_error_coefficient_below_point006', F(75,10)*F(37,10**4)/F(27,5) < F(6,1000))
    require('finite_F_derivative_absolute_upper_below_31', 26+4*F(1033,1000)+F(150,250)+F(18,10**114)+F(480000,10**57) < 31)
    require('normalized_residue_magnitude_lower', F(35,10)*F(28,10**4)/31 > F(1,6000))
    require('normalized_residue_magnitude_upper', 8*F(4,1000) < F(1,20))
    return {
        'status': 'pass',
        'classification': 'EXACT ARITHMETIC; analytic domain and approximation proof separately reviewed',
        'N_complex': '10^30', 'N_unique': '10^57',
        'complex_error_norm': M, 'real_error_bound': str(E),
        'rho': str(rho), 'degree': m,
        'value_tail_bound': str(A), 'derivative_tail_bound': str(B),
        'joint_derivative_bound': str(derivative),
        'joint_derivative_allowance': '1033/1000',
        'phase_error_bound_at_threshold': str(phase),
        'spatial_error_bound_times_N_cubed_at_threshold': str(phase/7),
        'F_prime_upper_bound': str(final), 'checks': checks,
    }


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2, sort_keys=True))
