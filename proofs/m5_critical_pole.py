"""Exact critical W pole phase, derivative and conditional asymptotic constants.

This certifies properties of the LIMIT functions. Finite pole asymptotics
require separate quantitative analytic theorems; no finite N0 is certified.
"""
import json
from fractions import Fraction

from proofs.m3_prudent_intervals import I, SCALE
from proofs.m3_critical_integrals import integrals, pi_interval, sine, compact


def logarithm(x, terms=160):
    """2*atanh((x-1)/(x+1)), with an absolute geometric tail enclosure."""
    if x.lo <= 0:
        raise ArithmeticError('Logarithm requires a positive interval')
    y = (x-1)/(x+1)
    radius = y.abs_upper()
    if radius.hi >= SCALE:
        raise ArithmeticError('Logarithm series does not converge uniformly')
    term, total = y, I(0)
    for k in range(terms):
        total += 2*term/(2*k+1)
        term *= y*y
    tail = 2*(radius**(2*terms+1))/((2*terms+1)*(1-radius*radius))
    return total+I(-tail.hi, tail.hi, raw=True)


def produce(bins=4096, power_bits=16):
    if not __debug__:
        raise RuntimeError('Run without -O: the interval engine requires assertions')
    values = integrals(bins, power_bits)
    sigma = I(2).sqrt()-1
    eta, d, A = 1/(sigma+1), 1-sigma, 1/(sigma*sigma)
    pre1, pre2 = values[0]
    post1, post2 = values[1]
    pi = pi_interval()
    slope = d*post1-4*sigma*sigma*post2
    constant = -d*d-d*A*pre1+12*sigma*sigma+4*pre2-3-sigma

    def phase(theta):
        angle = pi*(eta-theta)
        B = A*sine(pi*theta)/sine(angle)
        B_prime = A*pi*sine(pi*eta)/(sine(angle)**2)
        return constant+slope*B, sigma-A*pre1+B*post1, slope*B_prime

    # The entire real interval lies between eta and 1. Sine cannot vanish.
    sector = I(Fraction(4,5), Fraction(9,10))
    if not eta.hi < sector.lo < sector.hi < SCALE or slope.hi >= 0:
        raise ArithmeticError('Wrong sector or critical slope sign')
    _, _, global_derivative = phase(sector)
    if global_derivative.hi >= 0:
        raise ArithmeticError('Strict monotonicity not certified')
    left = right = None
    for numerator in range(8000, 9001):
        theta = Fraction(numerator, 10000)
        F, _, _ = phase(I(theta))
        if F.lo > 0:
            left = (theta, F)
        if F.hi < 0 and right is None:
            right = (theta, F)
    if left is None or right is None or not left[0] < right[0]:
        raise ArithmeticError('Unique critical root not bracketed')
    bracket = I(left[0], right[0])
    _, Pplus, derivative = phase(bracket)
    shift = 2*sigma*Pplus/derivative
    s_star = -logarithm(I(Fraction(1,2))+(sigma+1)/4)
    location = s_star*s_star/16
    residue = -Pplus*s_star*s_star/(8*derivative)
    if not (Pplus.hi < 0 and derivative.hi < 0 and shift.lo > 0
            and location.lo > 0 and residue.hi < 0):
        raise ArithmeticError('Critical coefficient sign failed')

    def record(x):
        return {'exact': x.record(), 'display': compact(x)}

    return {
        'classification': 'EXACT LIMIT-FUNCTION CERTIFICATE; finite asymptotics need analytic transfer',
        'bins': bins, 'power_bits': power_bits,
        'integrals': [[x.record() for x in row] for row in values],
        'F0_constant': record(constant), 'F0_B_coefficient': record(slope),
        'F0_prime_entire_sector': record(global_derivative),
        'unique_theta_star_bracket': [str(left[0]), str(right[0])],
        'F0_left': record(left[1]), 'F0_right': record(right[1]),
        'P0_plus_one_at_root': record(Pplus), 'F0_prime_at_root': record(derivative),
        'positive_phase_shift_coefficient': record(shift),
        'N_squared_distance_coefficient': record(location),
        'N_cubed_residue_coefficient': record(residue),
        's_star': record(s_star),
        'warning': 'No finite-N sign, uniqueness, simplicity or residue is certified by this program alone.'
    }


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2, sort_keys=True))
