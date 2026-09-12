"""Exact dyadic enclosures of the proposed critical-limit integrals.

Certifies only the integral signs, not the discrete-to-continuum theorem.
Real powers are enclosed between dyadic exponents using repeated square roots;
there are no floating arithmetic, logarithms, or special-function dependencies.
"""
import argparse
import json
from fractions import Fraction
from proofs.m3_prudent_intervals import I, SCALE, ceildiv


def real_power(base, exponent, bits=16):
    """Enclose x**a for x>=0, a>0 using monotonicity and dyadic powers."""
    assert base.lo >= 0 and exponent.lo > 0
    lo = exponent.lo*(1 << bits)//SCALE
    hi = ceildiv(exponent.hi*(1 << bits), SCALE)
    root = base
    for _ in range(bits):
        root = root.sqrt()
    a, b = root**lo, root**hi
    # On either side of x=1, power is monotone in a; hull covers both cases.
    return I(min(a.lo, b.lo), max(a.hi, b.hi), raw=True)


def atan_small(x, terms=100):
    total, power = I(0), x
    for n in range(terms):
        total += (-1)**n*power/(2*n+1)
        power *= x*x
    error = (power/(2*terms+1)).abs_upper().hi
    return total+I(-error, error, raw=True)


def pi_interval():
    # Machin: pi=16 atan(1/5)-4 atan(1/239); alternating-series remainders.
    return 16*atan_small(I(Fraction(1, 5)))-4*atan_small(I(Fraction(1, 239)))


def sine(x, terms=40):
    total, term = I(0), x
    for n in range(terms):
        total += (-1)**n*term
        term = term*x*x/((2*n+2)*(2*n+3))
    # Taylor Lagrange remainder: all real sine/cosine derivatives have |.|<=1.
    error = term.abs_upper().hi
    return total+I(-error, error, raw=True)


def compact(value, places=8):
    scale = 10**places
    return [str(Fraction(value.lo*scale//SCALE, scale)),
            str(Fraction(ceildiv(value.hi*scale, SCALE), scale))]


def constants(bits):
    rt = I(2).sqrt();t = rt-1;d = 1-t;us = 1/rt;eta = 1/rt
    norm = real_power(1-t, 2+rt, bits)*real_power(1/t-1, rt, bits)/real_power(1-us, eta, bits)
    common = t*t*(1-t*t)*8/norm
    deltas = [1-us, us-t]
    factors = [common*real_power(delta, 1-eta, bits) for delta in deltas]
    return rt,t,d,us,eta,deltas,factors


def integrals(bins=2048, power_bits=16):
    rt,t,d,us,eta,deltas,factors = constants(power_bits)
    totals = [[I(0), I(0)], [I(0), I(0)]]
    exponent = 8*(1-eta)-1
    L = 1/(1-us)
    for n in range(bins):
        x = I(Fraction(n,bins), Fraction(n+1,bins));x8=x**8
        xp = real_power(x, exponent, power_bits)
        for side in (0,1):
            delta=deltas[side]
            if side == 0:
                u=us+delta*x8
                ut=(us-t)+delta*x8
                one_u=delta*(1-x8)
            else:
                ut=delta*(1-x8)
                u=t+ut
                one_u=(1-us)+delta*x8
            # Exact nonnegativity of these factors permits clipping outward
            # rounding below zero at endpoints without excluding any value.
            ut=I(max(0,ut.lo),ut.hi,raw=True)
            one_u=I(max(0,one_u.lo),one_u.hi,raw=True)
            shape=(factors[side]*xp*real_power(ut,1+rt,power_bits)
                   *real_power(1/t-u,rt-1,power_bits)
                   /real_power(u,2+rt,power_bits)*one_u*(1+u))
            f=u/(1-t*u)
            divided=1/(us*(1-t*u))
            totals[side][0] += shape*(L+divided)/d/bins
            totals[side][1] += shape*(L+(f+1)*divided)/d/bins
    return totals


def produce(bins=2048, power_bits=16):
    values=integrals(bins,power_bits)
    rt=I(2).sqrt();t=rt-1;d=1-t;eta=1/rt;A=1/(t*t);pi=pi_interval()
    phases=[]
    for theta in (Fraction(3,10), Fraction(7,20)):
        B=A*sine(pi*theta)/sine(pi*(eta-theta))
        Pplus=1-d-A*values[0][0]+B*values[1][0]
        Hplus=1+t*t*(-3-A*values[0][1]+B*values[1][1])
        phases.append({'theta':str(theta),'P_plus_one':Pplus.record(),
                       'H_plus_one':Hplus.record(),'P_display':compact(Pplus),
                       'H_display':compact(Hplus)})
    assert int(phases[0]['P_plus_one']['upper_numerator']) < 0
    assert int(phases[1]['P_plus_one']['lower_numerator']) > 0
    assert all(int(p['H_plus_one']['lower_numerator'])>0 for p in phases)
    return {'classification':'EXACT LIMIT-INTEGRAL SIGNS; SCALING CONVERGENCE UNPROVED',
            'bins':bins,'power_bits':power_bits,
            'integrals':[[v.record() for v in row] for row in values],
            'integral_displays':[[compact(v) for v in row] for row in values],
            'phase_checks':phases}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bins',type=int,default=2048)
    parser.add_argument('--power-bits',type=int,default=16)
    args=parser.parse_args()
    print(json.dumps(produce(args.bins,args.power_bits),indent=2))
