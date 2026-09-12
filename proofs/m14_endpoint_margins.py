"""Exact directed lower reference and conditional endpoint-transfer margins."""

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from proofs.m3_prudent_intervals import I
from proofs.m3_critical_integrals import sine, pi_interval, compact
from proofs.m7_finite_poles import I384, SCALE, phase_data

ROOT = Path(__file__).resolve().parents[1]


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited interval guards required')
    ref = I384(F(414213556, 10**9))
    phase = phase_data(ref)
    q = phase['q']
    q2 = q*q
    beta = (1-ref-ref*q)/(1-q2)
    gamma = q*(ref-q*(1-ref))/(1-q2)
    beta.positive('directed beta')
    (beta+gamma).positive('directed endpoint denominator')
    if not (0 < q.lo <= q.hi < SCALE):
        raise ArithmeticError('directed q outside (0,1)')
    partial = I384(0)
    qp = q2p = I384(1)
    for _ in range(16384):
        den = beta+gamma*q2p
        den.positive('directed finite summand denominator')
        partial += ref*qp/den
        qp = qp*q
        q2p = q2p*q2

    source = ROOT/'results/m5-critical-v1/payload.json'
    raw = json.loads(source.read_text())
    def recover(x):
        if x['denominator_power_of_two'] != 384:
            raise ArithmeticError('unexpected critical interval precision')
        return I(int(x['lower_numerator']), int(x['upper_numerator']), raw=True)
    (pre1, pre2), (post1, post2) = [
        [recover(x) for x in row] for row in raw['integrals']]
    sigma = I(2).sqrt()-1
    eta = 1/(sigma+1)
    A = 1/(sigma*sigma)
    d = 1-sigma
    slope = d*post1-4*sigma*sigma*post2
    constant = -d*d-d*A*pre1+12*sigma*sigma+4*pre2-3-sigma
    pi = pi_interval()
    rows = []
    for theta in (F(4,5), F(9,10)):
        phase_factor = A*sine(pi*I(theta))/sine(pi*(eta-I(theta)))
        f0 = constant+slope*phase_factor
        pplus = sigma-A*pre1+post1*phase_factor
        f_affine = f0+I(0,F(1,10))*pplus
        rows.append((f0,pplus,f_affine))
    # If the joint moment error is <1/25, the coefficient allowance4
    # controls it. The t perturbation multiplies only1+P0.
    emax = F(17,100*512)
    transfer_error = F(4,25)+F(15,2)*emax**2/8
    checks = {
        'reference_positive_e_below_one_hundredth':
            0 < phase['epsilon'].lo and phase['epsilon'].hi*100 < SCALE,
        'reference_a_below_N512_left': phase['a'].hi*5 < 2564*SCALE,
        'positive_directed_partial_above_19': partial.lo > 19*SCALE,
        'critical_left_numerator_negative': rows[0][1].hi < 0,
        'critical_right_numerator_negative': rows[1][1].hi < 0,
        'critical_endpoint_numerator_abs_below_15_over_2': all(
            x[1].lo > I(F(-15,2)).hi and x[1].hi < 0 for x in rows),
        'affine_left_above_one_quarter': rows[0][2].lo > I(F(1,4)).hi,
        'affine_right_below_minus_one_fifth': rows[1][2].hi < I(F(-1,5)).lo,
        'P_coefficient_below_four': F(1)-F(207,500)+F(1,10) < 4,
        'transfer_error_below_17_over_100': transfer_error < F(17,100),
        'conditional_left_margin_positive': F(1,4)-F(17,100) > 0,
        'conditional_right_margin_negative': -F(1,5)+F(17,100) < 0,
    }
    if not all(checks.values()):
        raise ArithmeticError(checks)
    return {
        'status':'pass', 'checks':checks,
        'reference_t':'103553389/250000000',
        'phase':{k:v.record() for k,v in phase.items()},
        'directed_partial':partial.record(), 'directed_terms':16384,
        'directed_partial_display':[
            str(F(partial.lo,SCALE)),str(F(partial.hi,SCALE))],
        'critical_input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'endpoint_rows':[
            {'theta':str(theta),'F0':f.record(),'one_plus_P0':p.record(),
             'affine_delta_box':g.record(),'affine_display':compact(g,10)}
            for theta,(f,p,g) in zip((F(4,5),F(9,10)),rows)],
        'delta_uniform_upper':'1/20',
        'transfer_error_upper':str(transfer_error),
        'scope':{
            'N':'integer N>=512',
            'proven_component':'delta_D<1/20 and critical affine endpoint margins',
            'missing_hypothesis':'|P_N-P0|+|H_N-H0|<1/25 at both phase endpoints',
            'endpoint_existence':'CONDITIONAL; NOT PROVED',
            'finite_gap':'32<=N<=511 remains separate',
        },
    }


if __name__ == '__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
