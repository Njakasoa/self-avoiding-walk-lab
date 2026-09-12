"""Exact e-derivative box for B with delta held fixed; analytic transfer separate."""
import json
from fractions import Fraction as F
from proofs.m7_finite_poles import I384, SCALE
from proofs.m8_finite_derivatives import Jet384 as J


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited interval guards required')
    sigma=I384(2).sqrt()-1
    t=J(I384(sigma.lo-I384(F(1,8*180**2)).hi,sigma.hi,raw=True),
        I384(-F(1,7*180),0))
    qbox=I384(F(359,360),1)
    q=J(qbox,-qbox/2)
    delta=J(I384(0,F(7,100)),0)
    C=q-t; D=1-t*q; g=t-D*q
    C.x.positive('C'); D.x.positive('D'); (-g.x).positive('-gq')
    h=t*q/C
    (1-h).x.positive('1-h'); (1-t*h).x.positive('1-th')
    fh=h/(1-t*h); fq=q/(1-t*q); L1=fh/(1-h)
    S0=-t*D*D/g
    B1=C/g+L1*S0
    HB=t*t*(fq*C/g+fh*L1*S0)
    B=(1-t+2*delta)*B1-4*HB-(3+t)+2*delta
    claims={
        'B_lower_gt_minus_2': B.x.lo>-2*SCALE,
        'B_upper_lt_minus_7_over_5': F(B.x.hi,SCALE)<-F(7,5),
        'B_e_lower_gt_minus_7': B.d.lo>-7*SCALE,
        'B_e_negative': B.d.hi<0,
        'B1_plus_one_positive': (1+B1).x.lo>0,
        'phase_allowance': 7*F(17,100)<F(6,5),
    }
    if not all(claims.values()):
        raise ArithmeticError('boundary derivative allowance failed')
    return {'status':'pass','claims':claims,
            'jets':{name:box.record() for name,box in
                    [('t',t),('q',q),('delta_fixed',delta),('B1',B1),('t_squared_B2',HB),('B',B)]},
            'B_theta_upper_allowance':'6/(5*N^2)',
            'scope':'boundary component only; phase transfer and directed sign separate',
            'full_F_phase_sign':'NOT PROVED'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
