"""Exact arithmetic at the last step of the effective W existence bound.

This verifies arithmetic and frozen critical enclosures, not the analytic
moment estimate: that estimate needs independent mathematical review.
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def produce():
    p = json.loads((ROOT / 'results/m5-critical-v1/payload.json').read_text())

    def enclosure(key):
        x = p[key]['exact']
        d = 2 ** x['denominator_power_of_two']
        return F(int(x['lower_numerator']), d), F(int(x['upper_numerator']), d)

    left = enclosure('F0_left')
    right = enclosure('F0_right')
    numerator = enclosure('P0_plus_one_at_root')
    checks = {
        'critical_left_margin': left[0] > F(7, 10000),
        'critical_right_margin': right[1] < -F(3, 10000),
        'critical_numerator_entire_bracket': -5 < numerator[0] <= numerator[1] < -4,
        # Three positive terms of the atanh expansion are a lower bound.
        'log2_lower_bound': 2 * (F(1, 3) + F(1, 81) + F(1, 1215)) > F(69, 100),
    }
    log_n_lower = F(69, 100) * 10**120
    log_error_upper = 10**60 - log_n_lower / 20
    checks.update({
        'effective_moment_domain': log_n_lower > 10**100,
        'directed_domain': 10**120 > 108,
        'moment_log_error': log_error_upper < -1000,
        # exp(3)>1+3+9/2+27/6>10, hence log10<3.
        'log10_upper_bound': 1+3+F(9, 2)+F(27, 6) > 10,
        'moment_error_below_1e_100': 1000 > 100*3,
        'directed_reciprocal_simplification': F(415, 1000)+31/log_n_lower < 1,
        'directed_error_below_1e_100': log_n_lower > 10**100,
        'total_F_error_below_1e_90': 30*F(1, 10**100) < F(1, 10**90),
        'F_error_below_sign_margins': F(1, 10**90) < F(3, 10000),
        'noncancellation': -4+F(1, 10**100) < -3,
    })
    if not all(checks.values()):
        raise ArithmeticError({k:v for k,v in checks.items() if not v})
    return {
        'classification':'EXACT FINAL ARITHMETIC; analytic effective moment estimate requires separate proof review',
        'first_index_expression':'2^(10^120)',
        'scope':'Existence and noncancellation, not an effective uniqueness or simplicity threshold',
        'critical_phase_bracket':p['unique_theta_star_bracket'],
        'checks':checks,
        'log_N_lower_bound':str(log_n_lower),
        'log_moment_error_upper_bound':str(log_error_upper),
        'status':'pass',
    }


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2, sort_keys=True))
