"""Exact arithmetic allowances for M7 auxiliary complex/derivative lemmas.

These checks support the displayed analytic arguments; they do not prove
holomorphy, continuation or the moment bound by themselves.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]

def produce():
    checks={}
    def require(name,condition):
        if not bool(condition):raise ArithmeticError(name)
        checks[name]=True
    t,v=sp.symbols('t v')
    a=1+t*t-t*v+t**3*v
    delta=sp.expand(a*a-4*t*t)
    def norm(poly):return sum(abs(c) for c in sp.Poly(poly,t,v).coeffs())
    require('a_coefficient_norm_at_most_4',norm(a)<=4)
    require('a_total_degree_at_most_4',sp.Poly(a,t,v).total_degree()<=4)
    require('discriminant_coefficient_norm_at_most_20',norm(delta)<=20)
    require('discriminant_total_degree_at_most_8',sp.Poly(delta,t,v).total_degree()<=8)
    for x in (t,v):
        require(f'discriminant_first_{x}_norm_at_most_160',norm(sp.diff(delta,x))<=160)
        for y in (t,v):
            require(f'discriminant_second_{x}_{y}_norm_at_most_1280',norm(sp.diff(delta,x,y))<=1280)
    e0=F(1,10**8);R=F(5,10**4)
    require('even_t_remainder_coefficient_below_1e6',F(1,10)/(R*R*(1-F(1,4)))<10**6)
    require('t_derivative_below_e0',2*e0/8+16*10**6*(2*e0)**3<e0)
    require('real_t_deficit_above_1_over_17',F(1,16)-10**6*e0**2>F(1,17))
    require('complex_t_deficit_above_1_over_20',F(1,17)-e0>F(1,20))
    require('real_discriminant_slope_above_point005',2*F(8,10)*F(4,10)*F(8,10)/100>F(5,1000))
    require('real_discriminant_perturbation_below_point001',24000*e0<F(1,1000))
    require('polynomial_real_perturbation_coefficient',160+1280+5440*4<24000)
    reciprocal_sum=1/F(78,100)**2+1/F(78,100)+1/F(8,100)**2+1/F(8,100)
    require('complex_product_reciprocal_square_sum_below_172',reciprocal_sum<172)
    require('complex_product_factor_below_2',F(25,24)<2)
    require('pre_crossing_product_coefficient_below_12',3*F(25,7)<12)
    require('post_crossing_product_coefficient_below_300',192/F(7,10)<300)
    require('compact_mass_below_1e4',1500+3000*F(1,5)<10**4)
    require('kernel_tail_upper_solution',F(2,100)*F(415,1000)*F(425,1000)/(1-F(415,1000)*F(1,100)/F(82,100))<F(1,100))
    require('u_h_perturbation_coefficient_below_5',1/F(58,100)+F(415,1000)*2/F(58,100)**2<5)
    require('V1_modulus_below_14',(3+5)/F(58,100)<14)
    require('V2_modulus_below_26',(10+5)/F(58,100)<26)
    require('Q_coefficient_below_point425',F(18,100)*2*F(118,100)<F(425,1000))
    require('compact_plus_tail_joint_norm_below_1e10',8*10**7+48*10**5+100<10**10)
    require('exterior_root_linear_coefficient_below_5e8',2*10**7/F(49,1000)+F(71,100)*48/(F(49,1000)*F(5,100))<5*10**8)
    require('exterior_g_linear_coefficient_below_4e8',200/F(9,10000)+F(3,10)*1000/(F(9,10000)*F(1,1000))<4*10**8)
    require('exterior_log_remainder_coefficient_below_5e6',4*(1/F(49,1000)**2+1/F(9,10000)**2)<5*10**6)
    require('exterior_total_coefficient_below_1e9',5*10**8+4*10**8+5*10**6<10**9)
    require('crossing_total_coefficient_below_2e12',8*10**11+4*10**10*8<2*10**12)
    require('compact_log_sum_below_half_at_N1e120',10**14*F(1,10**60)<F(1,2))
    raw=json.loads((ROOT/'results/m5-critical-v1/payload.json').read_text())
    bounds=[F(1,2),F(7,10),F(1,2),F(3,5)]
    for i,(entry,bound) in enumerate(zip([x for row in raw['integrals'] for x in row],bounds)):
        scale=2**entry['denominator_power_of_two']
        require(f'critical_integral_{i}_positive_bounded',0<F(int(entry['lower_numerator']),scale)<=F(int(entry['upper_numerator']),scale)<bound)
    require('critical_joint_modulus_below_100',F(466,10)+F(18,100)*(3+6*F(7,10)+86*F(3,5))<100)
    require('cauchy_second_derivative_below_1e16',2*(10**10+100)/F(1,100)**2<10**16)
    require('real_error_below_2e_minus_21',F(1,10**21)+F(1,10**39)+F(1,10**106)<F(2,10**21))
    derivative=2*F(2,10**21)/F(1,10**18)+10**16*F(1,10**18)/2
    require('interpolation_derivative_equals_point009',derivative==F(9,1000))
    require('conditional_derivative_error_below_1',derivative<1)
    return {'status':'pass','classification':'EXACT AUXILIARY ARITHMETIC; analytic arguments separately reviewed',
            'checks':checks,'reciprocal_square_sum':str(reciprocal_sum),
            'conditional_derivative_error':str(derivative),
            'required_analytic_input_for_effective_uniqueness':'explicit holomorphic moment bound and its review'}

if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
