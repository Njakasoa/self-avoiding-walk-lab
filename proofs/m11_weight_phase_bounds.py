"""Exact rational allowances for the M11 regularized weight phase bound."""
import json
from fractions import Fraction as F


def produce():
    e=F(1,180); tl=F(207,500); th=F(4143,10000)
    hl=F(353,500); hh=F(71,100); d=1-th; dh=1-th*hh
    ratio=hh/dh+(1-hl)/(d*dh)
    ratio_t=hh*hh/dh**2+(1-hl)*(1/(d*d*dh)+hh/(d*dh**2))
    log_t=1/d+hh/dh+(8*th*ratio+4*th*th*ratio_t+1)/F(7,100)
    motion=6*e/7+F(3,5)
    total=F(1,1000)+16*F(61,100)+F(28,25)
    margin=F(1435,342)-F(11,32)
    checks={
        'J_positive': 1-3*th**2>0,
        'J_log_derivative_upper': 1/tl+(1+2*th)/(1-th-th*th)<7,
        'prefactor_e_derivative_positive': 1/(2*e)-e>0,
        'C_e_negative': -F(359,360)/2+e/7<0,
        'h_e_positive': -e/7+tl*tl/2>0,
        'kernel_square_gap': 1-th*th>F(3,4),
        'kernel_t_coefficient': 1/tl**2<6,
        'inverse_sqrt_three': F(3,5)**2*3>1,
        'kernel_motion': motion<F(61,100),
        'weight_t_derivative': log_t<200,
        't_phase_contribution': 200*e*e/7<F(1,1000),
        'total_log_weight_phase': total<11,
        'post_crossing_negative_margin': margin>F(385,100),
    }
    if not all(checks.values()):
        raise ArithmeticError('M11 weight derivative allowance failed')
    return {'status':'pass','checks':checks,
            'log_weight_t_upper':str(log_t),
            'kernel_motion_upper':str(motion),
            'log_weight_phase_upper':str(total),
            'post_crossing_margin_lower':str(margin),
            'scope':'arithmetic only; analytic proof and dependencies separate',
            'full_F_phase_sign':'NOT PROVED'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
