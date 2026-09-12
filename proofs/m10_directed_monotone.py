"""Exact basepoint and weight allowances for directed monotonicity."""
import json
from fractions import Fraction as F
from proofs.m7_finite_poles import I384, SCALE, phase_data, directed_sum


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited interval guards required')
    t0=F(207106,500000)
    phase=phase_data(I384(t0))
    if not (0<phase['epsilon'].lo and phase['epsilon'].hi*100<SCALE):
        raise ArithmeticError('basepoint phase domain')
    if F(phase['a'].hi,SCALE)>=F(164,5):
        raise ArithmeticError('basepoint is not below first target phase')
    D,tail=directed_sum(I384(t0))
    if F(D.lo,SCALE)<=F(93,7):
        raise ArithmeticError('directed lower bound')
    tl=F(207,500);th=F(4143,10000);hl=F(353,500);hh=F(71,100)
    ratio=hl/(1-tl*hl)+tl*(1-hh)/((1-tl*tl)*(1-tl*tl*hl))
    gap=4*tl*tl*ratio-(1-tl+F(14,100))
    if gap<=F(7,100):raise ArithmeticError('combined weight margin')
    d=1-th;dh=1-th*hh
    rp=(1-hl)*(1/(d*d*dh)+th*hh/(d*dh*dh))
    log_slope=th/d+4*th*th*rp/F(7,100)
    if log_slope>=16:raise ArithmeticError('logarithmic weight slope')
    return {'status':'pass','classification':'EXACT BASEPOINT AND RATIONAL ALLOWANCES; monotonicity proof separate',
            't0':str(t0),'phase':{k:v.record() for k,v in phase.items()},
            'D_R':D.record(),'directed_tail':tail['tail'].record(),'directed_terms':tail['terms'],
            'D_R_lower_allowance':'93/7','delta_D_upper_allowance':'7/100',
            'combined_weight_gap':str(gap),'log_weight_slope_upper':str(log_slope),
            'scope':'all N>=32 via reviewed directed monotonicity and phase inverse',
            'full_F_phase_sign':'NOT PROVED'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
