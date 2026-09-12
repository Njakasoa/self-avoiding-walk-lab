"""Exact critical margins and final arithmetic for a conditional M7 criterion."""
import json
from fractions import Fraction as F
from pathlib import Path
from proofs.m3_prudent_intervals import I
from proofs.m3_critical_integrals import sine,pi_interval,compact

ROOT=Path(__file__).resolve().parents[1]

def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: interval engine requires assertions')
    raw=json.loads((ROOT/'results/m5-critical-v1/payload.json').read_text())
    def recover(x):
        if x['denominator_power_of_two']!=384: raise ValueError('unexpected precision')
        return I(int(x['lower_numerator']),int(x['upper_numerator']),raw=True)
    (pre1,pre2),(post1,post2)=[[recover(x) for x in row] for row in raw['integrals']]
    sigma=I(2).sqrt()-1; eta=1/(sigma+1); A=1/sigma**2
    J=(1-sigma)*post1-4*sigma**2*post2; pi=pi_interval()
    endpoints=[]
    def record(x): return {'exact':x.record(),'display':compact(x,10)}
    for theta in (F(4,5),F(9,10)):
        Bp=A*pi*sine(pi*eta)/(sine(pi*(I(theta)-eta))**2)
        endpoints.append({'theta':str(theta),'F0_prime':record(J*Bp),
                          'P0_prime':record(post1*Bp)})
    pleft=recover(endpoints[0]['P0_prime']['exact'])
    fright=recover(endpoints[1]['F0_prime']['exact'])
    if pleft.hi>=I(75).lo or pleft.lo<=0 or fright.hi>=I(-6).lo:
        raise ArithmeticError('critical derivative margins failed')
    bound=I(-6)+4+I(F(150,250))+I(F(18,10**92))+I(F(480000,10**46))
    if bound.hi>=I(-1).lo: raise ArithmeticError('final derivative margin failed')
    return {'classification':'CONDITIONAL UNIQUENESS TRANSFER; derivative error <=1 must be proved',
            'status':'pass','endpoints':endpoints,'F_N_prime_conditional_upper':record(bound),
            'conditions':['N>=10^46','sup_T(|P_N_prime-P0_prime|+|H_N_prime-H0_prime|)<=1'],
            'consequence':'exactly one simple noncancelled W pole in the entire phase band'}

if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
