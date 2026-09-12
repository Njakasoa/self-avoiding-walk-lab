"""Exact allowances for the conditional direct positive-sum comparison."""

import json
from fractions import Fraction as F
from proofs.m3_prudent_intervals import I
from proofs.m14_endpoint_margins import produce as endpoint_margins


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: interval and proof guards required')
    data=endpoint_margins()
    em=F(17,51200)
    th=F(4143,10000);hh=F(71,100);dh=1-th*hh
    tl=F(207,500);hl=F(353,500)
    rmin=hl/(1-tl*hl)+tl*(1-hh)/((1-tl*tl)*(1-tl*tl*hl))
    rectangle_gap=4*tl*tl*rmin-(1-tl+F(1,10))
    h_partial=2*th/dh+1/(1-hh)
    h_log=h_partial+4*th*th*(2/(dh*dh))/F(7,100)
    prefactor=1/(2-em)+7*em/8
    weight=200*em/8+50*F(26,100)+2*F(51,100)+16*F(1,2)
    log_coefficient=weight+F(51,100)
    relative=23*em/(1-23*em)
    sigma=I(2).sqrt()-1;d=1-sigma
    B00=-d*d+12*sigma*sigma-3-sigma
    masses=[]
    for row in data['endpoint_rows']:
        def recover(x):
            return I(int(x['lower_numerator']),int(x['upper_numerator']),raw=True)
        f0=recover(row['F0'])
        masses.append(f0-B00)
    checks={
        'independent_rectangle_gap':rectangle_gap>F(7,100),
        'absolute_h_partial_below_50':h_log<50,
        'absolute_C_partial_below_2':1/(F(359,360)-th)<2,
        'normalized_prefactor_coefficient':prefactor<F(51,100),
        'normalized_weight_log_coefficient':log_coefficient<23,
        'log_error_argument_below_one':23*em<1,
        'relative_weight_error_below_one_over_125':relative<F(1,125),
        'critical_endpoint_mass_below_three':all(x.hi<I(3).lo for x in masses),
        'conditional_sum_error':(3+F(1,8))/125+F(1,8)==F(3,20),
        'boundary_plus_sum_error':F(3,20)+7*em<F(4,25),
        'conditional_left_margin':F(1,4)-F(4,25)==F(9,100),
        'conditional_right_margin':-F(1,5)+F(4,25)==-F(1,25),
    }
    if not all(checks.values()):
        raise ArithmeticError(checks)
    return {
        'status':'pass','checks':checks,
        'allowances':{'h_log_partial':str(h_log),'prefactor_log_coefficient':str(prefactor),
                      'weight_log_coefficient':str(log_coefficient),
                      'relative_weight_upper':str(relative),
                      'critical_mass_maxima':[x.record() for x in masses]},
        'scope':{'N':'integer N>=512','theta':'4/5 or9/10',
                 'remaining_hypothesis':'|Stilde_e-S0(delta)|<1/8',
                 'all_index_existence':'NOT PROVED',
                 'finite_gap':'32<=N<=511 not covered'},
    }


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
