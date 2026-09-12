"""Exact arithmetic for the combined weight and finite harmonic prefix.

This script checks arithmetic and one algebraic identity, not the analytic
phase inverse or the real beta derivative certificate.
"""
from fractions import Fraction as F
from math import factorial
import json
import sympy as sp


def produce():
    checks={}
    def require(name, condition):
        if not condition:
            raise ArithmeticError(name)
        checks[name]=True
    require('sigma_lower', (1+F(4142,10000))**2<2)
    require('sigma_upper', (1+F(4143,10000))**2>2)
    require('phase_e_bound', F(17,100)/32<F(1,180))
    require('t_lower', F(4142,10000)-F(1,8*180**2)>F(414,1000))
    exp_one_upper=sum((F(1,factorial(k)) for k in range(4)),F(0))+F(1,24)/(1-F(1,5))
    require('exp_one_upper', exp_one_upper==F(87,32)<F(11,4))
    require('log180_lower', F(11,4)**5<180)
    directed=(F(12,5)-F(5,9))*5+F(3,4)
    require('directed_lower', directed==F(359,36)>9)
    require('directed_reciprocal', 1/(1+directed)==F(36,395)<F(1,10))
    t_l=F(207,500);h_l=F(353,500);h_u=F(71,100)
    require('uh_lower', t_l/(1-t_l)>h_l)
    require('uh_upper', F(4143,10000)*F(359,360)/(F(359,360)-F(4143,10000))<h_u)
    ratio=h_l/(1-t_l*h_l)+t_l*(1-h_u)/((1-t_l*t_l)*(1-t_l*t_l*h_l))
    gap=4*t_l*t_l*ratio-(1-t_l+F(1,5))
    require('combined_weight_positive_margin', gap>F(1,100))
    t,u,h,C=sp.symbols('t u h C')
    f=lambda x:x/(1-t*x)
    dd=1/((1-t*u)*(1-t*h));L1=f(h)/(1-h)
    V1=(dd+L1)/C;V2=((f(u)+f(h))*dd+f(h)*L1)/C
    identity=sp.factor(V2/V1-f(h)-f(u)*(1-h)/(1-t*u*h))
    require('exact_weight_ratio_identity', identity==0)
    inverse_square=sum((F(1,k*k) for k in range(1,6)),F(0))+F(1,5)
    require('inverse_square_sum_bound', inverse_square==F(5989,3600)<F(5,3))
    require('paired_harmonic_loss', F(2,5)/F(24,25)*F(5,3)==F(25,36))
    require('harmonic_tail_ratio', 32+1>59*F(1,5))
    exp_point7_lower=sum((F(7,10)**k/factorial(k) for k in range(5)),F(0))
    require('log2_upper', exp_point7_lower==F(482921,240000)>2)
    harmonic_lower=5-F(25,36)-F(21,5)
    require('harmonic_difference_positive', harmonic_lower==F(19,180)>F(1,10))
    S=1/(F(9,10)*F(1,5))+1/(F(19,10)*F(6,5))
    require('post_crossing_margin', F(7,10)*S==F(1435,342)>F(419,100))
    return {'status':'pass',
            'classification':'EXACT ARITHMETIC AND ALGEBRA; analytic inputs separately reviewed',
            'scope':'combined weight for N>=32; bare phase derivative only through n<=60N',
            'combined_weight_ratio_lower':str(ratio),'combined_weight_gap':str(gap),
            'directed_lower':str(directed),'harmonic_difference_lower':str(harmonic_lower),
            'post_crossing_log_derivative_upper':str(-F(1435,342)),
            'checks':checks,
            'full_F_phase_sign':'NOT PROVED',
            'full_index_coverage':'NOT PROVED'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
