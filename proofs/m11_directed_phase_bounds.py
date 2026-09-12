"""Rational allowances for the M11 one-sided directed derivative bound."""
import json
from fractions import Fraction as F


def produce():
    e = F(1, 180)
    th = F(4143, 10000)
    alpha = F(17, 100)
    rprime = (e/7 + th*th/2)/(alpha*alpha)
    total = F(17, 80) + F(15, 2) + e*e/(7*(1-th)**2)
    delta = 8*F(7, 100)**2
    weight = F(200, 7)*delta
    checks = {
        'alpha_lower': 1-2*th > alpha,
        't_derivative': 1/(8*(1-e/2)) < F(1, 7),
        'r_upper': th/alpha < F(5, 2),
        'r_derivative_upper': rprime < 3,
        'exp_seven_gt_540': F(5, 2)**7 > 540,
        'one_minus_q_lower': F(1, 2)-e/8 > F(1, 3),
        'directed_e_derivative': total < 8,
        'delta_phase_coefficient': delta == F(49, 1250),
        'weight_phase_coefficient': weight == F(28, 25),
    }
    if not all(checks.values()):
        raise ArithmeticError('M11 directed derivative allowance failed')
    return {'status': 'pass', 'checks': checks,
            'r_derivative_allowance': str(rprime),
            'e_D_derivative_allowance': str(total),
            'delta_phase_allowance': str(delta),
            'directed_weight_phase_allowance': str(weight),
            'scope': 'arithmetic only; analytic summation and phase proof separate',
            'full_F_phase_sign': 'NOT PROVED'}


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2, sort_keys=True))
