"""Exact outward enclosure of the conditional M6 second phase coefficient.

Reuses the frozen M5 critical integrals. The directed digamma constant and
C2 are enclosed without floating point. Analytic transfer is a separate proof.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from proofs.m3_prudent_intervals import I, SCALE
from proofs.m3_critical_integrals import sine, pi_interval, compact
from proofs.m5_critical_pole import logarithm

ROOT=Path(__file__).resolve().parents[1]


def log_reduced(x):
    if x.lo<=0: raise ArithmeticError('positive logarithm required')
    k=0
    while x.lo>2*SCALE:
        x=x/2; k+=1
    while x.hi<SCALE:
        x=x*2; k-=1
    return logarithm(x)+k*logarithm(I(2))


def digamma_positive(x, shift=64):
    """DLMF5.11.2, positive-real first-neglected-term bound, then recurrence.

    Terms retained: -1/(12z²)+1/(120z⁴)-1/(252z⁶).
    Next term is positive 1/(240z⁸), bounding the remainder.
    """
    if x.lo<=0 or shift<0: raise ValueError('positive x and nonnegative shift')
    z=x+shift
    main=log_reduced(z)-1/(2*z)-1/(12*z**2)+1/(120*z**4)-1/(252*z**6)
    remainder=1/(240*z**8)
    result=main+I(0,remainder.hi,raw=True)
    for k in range(shift): result-=1/(x+k)
    return result,remainder


def produce():
    if not __debug__: raise RuntimeError('Run without -O: interval engine requires assertions')
    raw=json.loads((ROOT/'results/m5-critical-v1/payload.json').read_text())
    def recover(x):
        if x['denominator_power_of_two']!=384: raise ValueError('unexpected precision')
        return I(int(x['lower_numerator']),int(x['upper_numerator']),raw=True)
    (pre1,pre2),(post1,post2)=[[recover(x) for x in row] for row in raw['integrals']]
    sigma=I(2).sqrt()-1; eta=1/(sigma+1); A=1/(sigma*sigma); d=1-sigma
    theta=I(*[F(x) for x in raw['unique_theta_star_bracket']])
    sstar=recover(raw['s_star']['exact']); pi=pi_interval()
    J=d*post1-4*sigma*sigma*post2
    angle=pi*(eta-theta)
    sin_angle=sine(angle)
    cos_angle=sine(pi/2+angle)
    B=A*sine(pi*theta)/sin_angle
    Bp=A*pi*sine(pi*eta)/(sin_angle*sin_angle)
    p=sigma-A*pre1+post1*B; f=J*Bp
    C1=2*sigma*p/f
    psi,psi_tail=digamma_positive(sigma+3)
    cD=(log_reduced(I(4))-psi)/sigma
    b=sigma*(1+cD)-log_reduced(sstar)
    C2=C1*(b+2*sigma*post1/J)-pi*cos_angle/sin_angle*C1*C1
    K=sstar*sstar/16
    spatial_second=-2*K*C2
    if C1.lo<=0 or C2.lo<=0:
        raise ArithmeticError('positive phase coefficients not certified')
    def record(x): return {'exact':x.record(),'display':compact(x,12)}
    return {'classification':'EXACT LIMIT-COEFFICIENT ENCLOSURE; second-order transfer needs separate proof',
            'critical_input':'results/m5-critical-v1/payload.json',
            'theta_star_bracket':raw['unique_theta_star_bracket'],
            'digamma_argument':'2+sqrt(2)', 'digamma_shift':64,
            'digamma':record(psi),'digamma_remainder_upper':record(psi_tail),
            'directed_additive_constant':record(cD),'renormalized_log_shift_b':record(b),
            'phase_C1':record(C1),'phase_C2':record(C2),
            'spatial_second_log_coefficient':record(spatial_second),
            'status':'pass'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
