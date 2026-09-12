"""Exact allowances for the positive middle mass and its phase decrease."""
import json
from math import factorial
from fractions import Fraction as F
from proofs.m7_finite_poles import I384,SCALE


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: interval guards required')
    t=F(207,500); h=F(353,500); u=F(63,100)
    ratio=h/(1-t*h)+u*(1-h)/((1-t*u)*(1-t*u*h))
    weight=(1-t*u*h)/((1-t)*(1-t*u)*(1-t*h)*(1-h))
    gap=4*t*t*ratio-(1-t+F(14,100))
    lower_L=weight*gap
    J=t*(1-t*t)/(1-t-t*t)
    T=I384(t); v=I384(F(149,200))
    a=1-T*v+T*T+T*T*T*v
    lower_U=2*T/(a+(a*a-4*T*T).sqrt())
    x=F(1071,800)
    exp_upper=sum(x**k/F(factorial(k)) for k in range(13))+x**13/F(factorial(13))/(1-x/14)
    mass=F(31,64)*F(41,50)*F(27,41)*F(1,4)*F(3,2)*F(48,329)
    smooth=F(712,100)*F(51,200)+F(51,100)+11
    claims={
        'log_R_coefficient':F(51,70)+F(51,29)+F(18,25)<F(13,4),
        'exp_bound':exp_upper<4,
        'bare_power':F(4,3)**7>F(6,5)**10,
        'prefactor':J*F(359,360)>F(41,50),
        'kernel_lower':F(lower_U.lo,SCALE)>u,
        'positive_gap':gap>0,
        'combined_weight':lower_L>F(3,2),
        'term_count':F(31,64)==F(1,2)-F(1,64),
        'mass_lower':mass>F(1,70),
        'factor_derivative':F(7071,1000)+F(18,100)*F(51,200)<F(712,100),
        'smooth_phase':smooth<F(67,5),
        'negative_submargin':F(1435,342)-F(67,5*32)>F(15,4),
        'middle_margin':F(15,4)*F(1,70)==F(3,56),
    }
    if not all(claims.values()):
        raise ArithmeticError('middle mass allowance failed')
    return {'status':'pass','claims':claims,
            'kernel_lower':lower_U.record(),'exponential_upper':str(exp_upper),
            'combined_weight_lower':str(lower_L),'subwindow_mass_lower':str(mass),
            'subwindow_log_phase_upper_allowance':'-15/4',
            'middle_phase_upper_allowance':'-3/56',
            'scope':'middle sum only; complete F derivative remains open'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
