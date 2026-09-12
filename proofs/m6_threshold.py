"""Exact arithmetic ledger for the M6 sufficient W existence threshold.

The analytic hypotheses are proved separately; this checks their aggregation.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from proofs.m3_prudent_intervals import I
from proofs.m3_critical_integrals import sine, pi_interval, compact
from proofs.m6_second_coefficient import log_reduced, produce as coefficients

ROOT=Path(__file__).resolve().parents[1]

def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: interval engine requires assertions')
    raw=json.loads((ROOT/'results/m5-critical-v1/payload.json').read_text())
    def recover(x):
        if x['denominator_power_of_two']!=384:
            raise ValueError('unexpected interval precision')
        return I(int(x['lower_numerator']),int(x['upper_numerator']),raw=True)
    (pre1,pre2),(post1,post2)=[[recover(x) for x in row] for row in raw['integrals']]
    sigma=I(2).sqrt()-1; eta=1/(sigma+1); A=1/(sigma*sigma); d=1-sigma
    J=d*post1-4*sigma*sigma*post2
    C0=-d*d-d*A*pre1+12*sigma*sigma+4*pre2-3-sigma
    pi=pi_interval()
    rows=[]
    for theta in (F(4,5),F(9,10)):
        B=A*sine(pi*I(theta))/sine(pi*(eta-I(theta)))
        rows.append((C0+J*B,sigma-A*pre1+post1*B))
    e=I(F(1,10**46))
    error=1/(100*I(10).sqrt())+I(F(1,100))+I(F(1,10**32))
    logN=46*log_reduced(I(10))
    delta=sigma/logN
    directed_remainder=100*e*logN
    cD=recover(coefficients()['directed_additive_constant']['exact'])
    checks={
        'moment_error_below_1_over_50':error.hi<I(F(1,50)).lo,
        'directed_constant_above_3_over_4':cD.lo>I(F(3,4)).hi,
        'directed_remainder_below_1e_minus_41':directed_remainder.hi<I(F(1,10**41)).lo,
        'delta_below_1_over_250':delta.hi<I(F(1,250)).lo,
        'left_F0_above_1':rows[0][0].lo>I(1).hi,
        'right_F0_below_minus_1_over_5':rows[1][0].hi<I(F(-1,5)).lo,
        'p_left_above_minus_7_point_5':rows[0][1].lo>I(F(-15,2)).hi,
        'p_right_below_minus_3_point_6':rows[1][1].hi<I(F(-18,5)).lo,
        'post1_positive':post1.lo>0,
        'J_negative':J.hi<0,
        'denominator_error_below_3_over_20':(I(F(4,50))+2*e*e+I(F(16,250))).hi<I(F(3,20)).lo,
    }
    if not all(checks.values()):
        raise ArithmeticError(checks)
    def record(x):return {'exact':x.record(),'display':compact(x,12)}
    return {'status':'pass','scope':'existence and noncancellation, not effective uniqueness',
            'N0':'10^46','kernel_B':'10^12','checks':checks,
            'moment_error':record(error),'delta_upper_bound':record(delta),
            'endpoint_rows':[{'theta':str(t),'F0':record(f),'one_plus_P0':record(p)}
                             for t,(f,p) in zip((F(4,5),F(9,10)),rows)]}

if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
