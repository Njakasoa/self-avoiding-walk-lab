"""Exact mass envelopes and a directed upper basepoint for32<=N<=64."""
import json
from fractions import Fraction as F
from proofs.m7_finite_poles import I384,SCALE,phase_data,directed_sum


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited interval guards required')
    ref=F(4142133,10000000)
    phase=phase_data(I384(ref))
    dr,tail=directed_sum(I384(ref))
    t=F(4143,10000);q=F(359,360)
    den=(1-t)*(q*(1-t)-t)
    ell=4*t*t/(1-t)-(1-t)
    l0=ell/den;l1=(ell-F(2,17))/den
    J=t*(1-t*t)/(1-t-t*t)
    mass0=J*F(17,100)*l0*(1+F(6,5*32))/F(28,100)
    mass1=J*F(17,100)*l1*(F(4,5)+F(11,10*32))/F(28,100)
    claims={
        'reference_phase_domain':0<phase['epsilon'].lo and phase['epsilon'].hi*100<SCALE,
        'reference_above_N64_band':F(phase['a'].lo,SCALE)>F(649,10),
        'directed_upper':dr.hi<16*SCALE,
        'denominator_positive':den>0,
        'positive_lower_envelope_numerator':ell>F(2,17),
        'weight_general':l0<F(5899,1000),
        'weight_low_indices':l1<F(1179,250),
        'bare_N_endpoint':F(5,6)**7>F(64)**3/F(4)**10,
        'mass_general':mass0<F(31,10),
        'mass_low_indices':mass1<2,
    }
    if not all(claims.values()):
        raise ArithmeticError('pre-crossing mass allowance failed')
    return {'status':'pass','claims':claims,'t_reference':str(ref),
            'phase':{k:v.record() for k,v in phase.items()},
            'directed_value':dr.record(),'directed_tail':tail['tail'].record(),
            'directed_terms':tail['terms'],
            'weight_upper_general':str(l0),'weight_upper_low_indices':str(l1),
            'mass_upper_general':str(mass0),'mass_upper_low_indices':str(mass1),
            'scope':'S_pre<3.1 forN>=32; S_pre<2 for32<=N<=64; derivative not asserted'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
