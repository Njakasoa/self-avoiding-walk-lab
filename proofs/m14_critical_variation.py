"""Exact constants for the critical-factor and kernel-motion lemmas."""

import json
from fractions import Fraction as F


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: proof entrypoint guard')
    lo,hi=F(207,500),F(4143,10000)
    a_min=1/(hi*hi)-1-2*hi
    c_min=1-hi*hi
    delta_max=(1/lo+lo)**2-4
    mixed_gap=F(39,10)*F(4,5)*2-F(83,100)*F(41,10)
    checks={
        'A_t_lower':a_min>F(39,10),
        'c_t_lower':c_min>F(4,5),
        'Delta_upper':delta_max<F(41,10),
        'two_t_upper':2*hi<F(83,100),
        'mixed_kernel_sign':mixed_gap>0,
        'three_eta_below_17_over_8_squared':F(9,2)<F(17,8)**2,
        'psi_absolute_allowance':1+F(17,8)==F(25,8),
    }
    if not all(checks.values()):
        raise ArithmeticError(checks)
    return {
        'status':'pass','checks':checks,
        'allowances':{'A_t_lower':str(a_min),'c_t_lower':str(c_min),
                      'Delta_upper':str(delta_max),'mixed_kernel_gap':str(mixed_gap),
                      'critical_total_variation':'<17/8',
                      'rectangle_error':'<(17/8)*e',
                      'kernel_displacement':'<e/2'},
        'scope':'arithmetic constants only; analytic identities reviewed separately; no full moment error or existence claim',
    }


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
