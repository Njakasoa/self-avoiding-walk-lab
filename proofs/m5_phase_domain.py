"""Exact real phase-domain bounds and an explicit directed-log threshold."""
import json
from fractions import Fraction as F

from proofs.m3_prudent_intervals import I, SCALE
from proofs.m3_critical_integrals import compact
from proofs.m5_critical_pole import logarithm


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: the interval engine requires assertions')
    sigma = I(2).sqrt()-1
    e = I(0, F(1,100))
    # Physical branch: sigma-t <= epsilon²/8, 1-epsilon/2 <= q <= 1.
    t = I(sigma.lo-SCALE//80000-1, sigma.hi, raw=True)
    q = I(F(199,200), 1)
    # t_e=sinh(e/2)/F'(t), F'(t)<=-4, sinh(e/2)<=e.
    te, qe = I(F(-1,400), 0), -q/2
    d = 1-t*q
    de = -te*q-t*qe
    v = q*(d-t*t)/(d*(1-t*t))
    sg = -logarithm(v)
    sg_prime = -(qe/q+(de-2*t*te)/(d-t*t)-de/d+2*t*te/(1-t*t))
    s_star = -logarithm(I(F(1,2))+(sigma+1)/4)
    inverse_margin = sg-e*sg_prime
    ratio = sg/s_star*I(F(200,209), 1)
    if not (v.lo>0 and v.hi<SCALE and sg.lo>0 and inverse_margin.lo>0):
        raise ArithmeticError('Physical phase domain or monotonicity failed')
    if not (100*sg.hi<20*SCALE and ratio.lo>SCALE//2 and ratio.hi<2*SCALE):
        raise ArithmeticError('N>=20 uniform inverse enclosure failed')
    Cstar = 80+3/sigma
    log_offset = -logarithm(s_star)+logarithm(I(2))
    if log_offset.hi >= 3*SCALE:
        raise ArithmeticError('Phase logarithm offset exceeds three')
    threshold = 2*sigma*(1+Cstar)
    log_N0 = 108*logarithm(I(2))
    error_constant = 2*sigma*sigma*(1+Cstar)
    if not (log_N0.lo>threshold.hi and error_constant.hi<31*SCALE):
        raise ArithmeticError('Explicit directed-log threshold failed')

    def record(x):
        return {'exact':x.record(), 'display':compact(x)}

    return {
        'classification':'EXACT REAL PHASE DOMAIN AND DIRECTED-TERM THRESHOLD; not a W pole N0',
        'epsilon_domain':['0','1/100'], 'phase_domain':['4/5','9/10'],
        'phase_first_N':20, 'directed_log_first_N':str(2**108),
        'directed_log_first_N_power_of_two':108,
        'v_g':record(v), 's_g':record(sg), 's_g_prime':record(sg_prime),
        's_g_minus_e_s_g_prime':record(inverse_margin),
        'N_e_over_s_star':record(ratio), 's_star':record(s_star),
        'phase_log_offset_upper':record(log_offset),
        'log_N0':record(log_N0), 'required_log_threshold':record(threshold),
        'reciprocal_error_constant':record(error_constant),
        'consequence':'For N>=2^108 and real theta in [.8,.9], |1-D_I-sigma/logN|<31/log²N, conditional on independently checked directed-log bound80.',
    }


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
