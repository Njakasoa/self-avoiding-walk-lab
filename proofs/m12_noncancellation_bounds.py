"""Exact scalar boxes for uniform W noncancellation; analytic proof separate."""
import json
from fractions import Fraction as F
from proofs.m7_finite_poles import I384, SCALE


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: I384 guards are required')
    sigma=I384(2).sqrt()-1
    t=I384(sigma.lo-I384(F(1,8*180**2)).hi,sigma.hi,raw=True)
    q=I384(F(359,360),1)
    C=q-t; D=1-t*q; g=t-D*q
    C.positive('C'); D.positive('D'); (-g).positive('-gq')
    h=t*q/C
    (1-h).positive('1-h'); (1-t*h).positive('1-th')
    fh=h/(1-t*h); fq=q/(1-t*q)
    L1=fh/(1-h); S0=-t*D*D/g
    B1=C/g+L1*S0
    HB=t*t*(fq*C/g+fh*L1*S0)
    th=F(4143,10000); hl=F(353,500); hh=F(71,100)
    Rmax=hh/(1-th*hh)+(1-hl)/((1-th)*(1-th*hh))
    Zmin=1+HB-t*t*Rmax*(1+B1)
    ellmax=4*th*th*Rmax-(1-th)
    if (1+B1).lo<=0 or F(Zmin.lo,SCALE)<=F(3,10) or ellmax>=F(3,5):
        raise ArithmeticError('noncancellation scalar allowance failed')
    return {'status':'pass',
            'boxes':{name:box.record() for name,box in
                     [('t',t),('q',q),('B1',B1),('t_squared_B2',HB),('Z_min',Zmin)]},
            'R_max':str(Rmax),'ell_upper':str(ellmax),
            'Z_lower_allowance':'3/10','ell_upper_allowance':'3/5',
            'numerator_upper_at_F_zero':'-2',
            'scope':'scalar inequalities only; positive averaging argument separate',
            'existence_and_uniqueness':'NOT PROVED'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
