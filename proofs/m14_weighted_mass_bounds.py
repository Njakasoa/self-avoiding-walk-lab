"""Exact envelopes for the M14 integrated Gamma/product comparison."""

import json
from fractions import Fraction as F
from math import factorial
from proofs.m7_finite_poles import I384 as I, SCALE, kernel


def produce():
    if not __debug__:
        raise RuntimeError('Run without -O: exact interval proof guards')
    E=F(17,51200); rt=I(2).sqrt(); t=rt-1; h=1/rt; d=1-t
    def weight(u,delta):
        R=h/(1-t*h)+u*(1-h)/((1-t*u)*(1-t*u*h))
        V=(1-t*u*h)/(d*(1-t*u)*(1-t*h)*(1-h))
        return V*(4*t*t*R-(d+2*delta))
    cells=[]
    for k in range(8):
        lo=F(2,5)+F(3*k,40); hi=lo+F(3,40)
        u=I(lo,hi)
        R=h/(1-t*h)+u*(1-h)/((1-t*u)*(1-t*u*h))
        Ru=(1-h)*(1/((1-t*u)**2*(1-t*u*h))
            +t*h*u/((1-t*u)*(1-t*u*h)**2))
        gap=4*t*t*R-(d+I(F(1,10)))
        gap.positive('critical combined-weight gap')
        logu=t/(1-t*u)-t*h/(1-t*u*h)+4*t*t*Ru/gap
        if not (logu.lo>0 and logu.hi<4*SCALE):
            raise ArithmeticError('critical log-u cell failed')
        cells.append({'u':[str(lo),str(hi)],'gap':gap.record(),'log_u':logu.record()})
    w0=2*t*weight(I(1),I(0))
    u075=kernel(t,I(F(40,43)))
    u2=kernel(t,I(F(1,7)))
    Lhalf=weight(I(F(1,2)),I(0))
    beta_error=350*E*E
    ampl=1+F(84,25)*E
    near_G=(F(3,20)+F(3,10)*E)/(F(3,20)-F(2,25)-F(18,25)*E)
    translate_upper=F(84,25)*F(31,10)+2*ampl
    translate_lower=5+11*F(2,5)*F(31,10)
    exponent_integral=24*(22/F(7,25)+1/F(7,25)**2)+276
    quad_coefficient=F(1001,200)+F(43,25)*F(5,2)*5+F(43,25)*11*F(101,100)*F(16,5)
    total_gamma=107*E+350*E*E
    head_arg=E*(F(17,8)+40)
    geo_ratio=1/(F(27,10)*(1-F(27,10)*E/2))
    exp54=sum((F(27,5)**k/F(factorial(k)) for k in range(13)),F(0))
    tail=F(5,6)*F(1,2)*F(9,4)*F(1001,1000)*F(3,8)/exp54
    total=F(1,25)+F(3,200)*(3+F(1,25))+F(1,250)
    checks={
        'eight_adjacent_cells_cover_2_over_5_to_one':F(2,5)+8*F(3,40)==1,
        'critical_weight_at_zero_below_five':w0.hi<5*SCALE,
        'critical_log_density_rate_below_five':(1+h+I(F(25,8))).hi<5*SCALE,
        'critical_kernel_at_3_over_40_below_4_over_5':u075.hi<I(F(4,5)).lo,
        'kernel_s_derivative_below_3_over_2_squared':(F(4,5)*F(5,6))**2/(3*(1-F(40,43)))<F(3,2)**2,
        'critical_weight_log_density_below_eleven':5+4*F(3,2)==11,
        'near_crossing_excluded':F(2,25)+F(18,25)*E<F(3,20),
        'near_Gbar_below_5_over_2':near_G<F(5,2),
        'near_Gbeta_below_5_over_2':F(3,20)/(F(3,20)-F(2,25))<F(5,2),
        'critical_log_c_abs_below_two':sum((F(2)**k/F(factorial(k)) for k in range(6)),F(0))>F(20,3),
        'beta_variation_integral_below_2500':exponent_integral<2500,
        'beta_mass_below_31_over_10':3+beta_error<F(31,10),
        'Gamma_amplitude_coefficient':F(18,25)*(F(2,5)+F(3,10))/F(3,20)==F(84,25),
        'translated_mass_below_16_over_5':ampl*(F(31,10)+2*E)<F(16,5),
        'translation_upper_below_19':translate_upper<19,
        'translation_lower_below_19':translate_lower<19,
        'CDF_origin_density_below_1001_over_1000':1+F(36,25)*E<F(1001,1000),
        'far_convolution_segment_above_3_over_40':F(2,25)-E>F(3,40),
        'exp_eleven_E_below_101_over_100':1/(1-11*E)<F(101,100),
        'Gamma_error_linear_coefficient_below_107':quad_coefficient+19<107,
        'Gamma_quadrature_error_below_one_over_25':total_gamma<F(1,25),
        'head_K_relative_error_below_3_over_200':head_arg/(1-head_arg)<F(3,200),
        'global_K_prefactor_below_1001_over_1000':1/(1-F(17,8)*E)<F(1001,1000),
        'global_K_exponential_rate_above_27_over_10':(2+h-I(20*E)).lo>I(F(27,10)).hi,
        'post_tail_Gamma_base_below_one_tenth':(F(17,100)+F(3,10)*E)/(2-F(17,100))<F(1,10),
        'post_tail_Gamma_correction_below_one_thousandth':F(18,25)*E/(2-F(17,100))<F(1,1000),
        'Gamma_fractional_power':10**7>5**10,
        'post_tail_T_below_one_half':F(12,5)*F(1001,1000)/5<F(1,2),
        'exp_two_above_seven':sum((F(2)**k/F(factorial(k)) for k in range(5)),F(0))==7,
        'tail_kernel_below_one_half':u2.hi<I(F(1,2)).lo,
        'tail_critical_weight_below_nine_fourths':Lhalf.hi<I(F(9,4)).lo,
        'geometric_normalization_below_3_over_8':geo_ratio<F(3,8),
        'exp_27_over_5_lower_above_200':exp54>200,
        'each_discrete_tail_below_one_over_500':tail<F(1,500),
        'integrated_error_equals_56_over_625':total==F(56,625),
        'integrated_error_below_one_eighth':total<F(1,8),
    }
    if not all(checks.values()):
        raise ArithmeticError(checks)
    return {'status':'pass','checks':checks,'critical_log_u_cells':cells,
            'boxes':{'w0':w0.record(),'u075_upper':u075.record(),
                     'u2_upper':u2.record(),'L_half_upper':Lhalf.record()},
            'rational_bounds':{'exponent_derivative_integral':str(exponent_integral),
                'quad_coefficient':str(quad_coefficient),'Gamma_error_upper':str(total_gamma),
                'one_tail_upper':str(tail),'Stilde_error_upper':str(total)},
            'scope':{'N':'integer N>=512','theta':'4/5 or9/10',
                     'delta':'[0,1/20]',
                     'analytic_inputs':'critical profile, Gamma sandwich and smooth envelope require separate analytic review',
                     'finite_32_to_511':'NOT COVERED'}}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
