"""Exact critical-phase signs for the weakly prudent bridge quotient W.

The computation encloses limiting integrals only. The uniform transfer and
directed-ramp limit are separate analytic obligations in W_NON_DFINITE.md.
"""
import json
from fractions import Fraction

from proofs.m3_prudent_intervals import I, SCALE
from proofs.m3_critical_integrals import integrals, pi_interval, sine, compact


def certify(values):
    rt = I(2).sqrt()
    sigma, eta = rt-1, 1/rt
    A, d = 1/(sigma*sigma), 1-sigma
    phases = (Fraction(4, 5), Fraction(9, 10))
    if not (eta.hi < I(phases[0]).lo < I(phases[1]).lo < SCALE):
        raise ArithmeticError('Phase interval must lie strictly between eta and 1')
    if not all(value.lo > 0 for row in values for value in row):
        raise ArithmeticError('The four moment integrals must be positive')
    pi = pi_interval()
    rows = []
    for theta in phases:
        B = A*sine(pi*I(theta))/sine(pi*(eta-I(theta)))
        if B.hi >= 0:
            raise ArithmeticError('Connection amplitude must be negative')
        P = -d-A*values[0][0]+B*values[1][0]
        H = sigma*sigma*(-3-A*values[0][1]+B*values[1][1])
        F = d*P-4*H-(3+sigma)
        rows.append({'theta': str(theta), 'B': B.record(),
                     'P_plus_one': (P+1).record(), 'F0': F.record(),
                     'F0_display': compact(F),
                     'P_plus_one_display': compact(P+1)})
    # On the entire phase interval B<0 and J_1,post>0. Hence
    # 1+P_0 <= sigma - A*J_1,pre, an upper bound, not an equality.
    upper = sigma-A*values[0][0]
    if upper.hi >= -2*SCALE:
        raise ArithmeticError('Uniform exclusion of 1+P=0 was not certified')
    if int(rows[0]['F0']['lower_numerator']) <= 0:
        raise ArithmeticError('Left limiting F sign failed')
    if int(rows[1]['F0']['upper_numerator']) >= 0:
        raise ArithmeticError('Right limiting F sign failed')
    return {'classification': 'EXACT W LIMIT SIGNS; analytic transfer is separate',
            'phases': rows, 'P0_plus_one_upper_bound': upper.record(),
            'P0_plus_one_upper_bound_display': compact(upper),
            'integrals': [[x.record() for x in row] for row in values]}


def produce(bins=2048, power_bits=16):
    if not __debug__:
        raise RuntimeError('Run without -O: the interval engine requires assertions')
    result = certify(integrals(bins, power_bits))
    result.update({'bins': bins, 'power_bits': power_bits})
    return result


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2, sort_keys=True))
