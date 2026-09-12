"""Exact outward dyadic interval checks for a finite BB2014 singularity set.

Every endpoint is an integer divided by 2**BITS. No floating-point arithmetic
is used for enclosure arithmetic, square roots, or geometric remainder bounds.
This certifies finite cases only; it does not prove non-D-finiteness.
"""
from fractions import Fraction
from math import isqrt
import json

BITS = 384
SCALE = 1 << BITS


def ceildiv(a, b):
    return -((-a) // b)


class I:
    def __init__(self, a, b=None, *, raw=False):
        if raw:
            self.lo, self.hi = a, b
        else:
            a, b = Fraction(a), Fraction(a if b is None else b)
            self.lo = a.numerator * SCALE // a.denominator
            self.hi = ceildiv(b.numerator * SCALE, b.denominator)
        assert self.lo <= self.hi

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        b = I.cast(other)
        return I(self.lo + b.lo, self.hi + b.hi, raw=True)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, raw=True)

    def __sub__(self, other):
        return self + -I.cast(other)

    def __rsub__(self, other):
        return I.cast(other) + -self

    def __mul__(self, other):
        b = I.cast(other)
        p = [x*y for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return I(min(p)//SCALE, ceildiv(max(p), SCALE), raw=True)

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ArithmeticError('Division interval contains zero')
        return I(SCALE*SCALE//self.hi, ceildiv(SCALE*SCALE, self.lo), raw=True)

    def __truediv__(self, other):
        return self * I.cast(other).reciprocal()

    def __rtruediv__(self, other):
        return I.cast(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result, base = I(1), self
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def sqrt(self):
        if self.lo < 0:
            raise ArithmeticError('Negative square root interval')
        lo, hi = isqrt(self.lo*SCALE), isqrt(self.hi*SCALE)
        if hi*hi < self.hi*SCALE:
            hi += 1
        return I(lo, hi, raw=True)

    def abs_upper(self):
        return I(max(abs(self.lo), abs(self.hi)), max(abs(self.lo), abs(self.hi)), raw=True)

    def record(self):
        return {'lower_numerator': str(self.lo), 'upper_numerator': str(self.hi),
                'denominator_power_of_two': BITS}


def kernel(t, v):
    a = 1-t*v+t*t+t**3*v
    return 2*t/(a+(a*a-4*t*t).sqrt())


def summands(t, q, v):
    one = 1-t*q
    a, b = kernel(t, v), kernel(t, v*q*q)
    h = t*q-(q-t)*a
    A = (q-t)*(1-t*t)*(a*one-(q*(q-t)+t*(1-q*q)*a)*b)/(one*(1-t*a)*(1-t*b)*h)
    B = q*(q-t)**2*(t-one*b)/(one**2*h)
    H = t*t*(1-t*t)*(q-t)*(one*a*a*(1-2*t*b)-(q*(q-t)-t*a*(2*q*(q-t)+t*(1-q*q)*a))*b*b)/(one*(1-t*a)**2*(1-t*b)**2*h)
    return A, H, B


def enclose(t, max_terms=4000):
    q = kernel(t, I(1))
    assert 0 < q.lo <= q.hi < SCALE
    total, hook, prod, v = I(0), I(0), I(1), I(1)
    for n in range(max_terms):
        # q**(2k) is in [0,v.hi] for all k>=n. This one interval bounds
        # every future A, H, B, giving a uniform geometric majorant.
        if n and n % 100 == 0:
            tail_v = I(0, v.hi, raw=True)
            try:
                Amax, Hmax, Bmax = (z.abs_upper() for z in summands(t, q, tail_v))
            except ArithmeticError:
                Bmax = I(2)
            if Bmax.hi < SCALE:
                ea = prod.abs_upper()*Amax/(1-Bmax)
                eh = prod.abs_upper()*Hmax/(1-Bmax)
                if max(ea.hi, eh.hi)*10**30 < SCALE:
                    total = total+I(-ea.hi, ea.hi, raw=True)
                    hook = hook+I(-eh.hi, eh.hi, raw=True)
                    one = 1-t*q
                    P = q*(1-t*t)/one+q*total
                    H = t*t*q*q*(1-t*t)/(one*one)+q*hook
                    return P, H, {'terms': n, 'tail_P_sum': ea.record(),
                                  'tail_H_sum': eh.record(), 'tail_B_abs': Bmax.record()}
        A, H, B = summands(t, q, v)
        total, hook = total+prod*A, hook+prod*H
        prod, v = prod*B, v*q*q
    raise RuntimeError('No certified geometric tail within term cap')


ROOT_CENTERS = [
    '0.41257508666590646034530112147',
    '0.41381169333386277239781975195',
    '0.41403636149110697240878112993',
    '0.41411430354223307163627536365',
    '0.41415020038700697190002708811',
]


def produce():
    results = []
    for center in ROOT_CENTERS:
        c, eps = Fraction(center), Fraction(1, 10**20)
        lo, hi = c-eps, c+eps
        left, _, left_meta = enclose(I(lo))
        right, _, right_meta = enclose(I(hi))
        _, hook, full_meta = enclose(I(lo, hi))
        assert (left+1).hi < 0 < (right+1).lo
        assert (hook+1).lo > 0
        results.append({'bracket': [str(lo), str(hi)],
                        'P_plus_one_left': (left+1).record(),
                        'P_plus_one_right': (right+1).record(),
                        'H_plus_one_entire_bracket': (hook+1).record(),
                        'left_tail': left_meta, 'right_tail': right_meta,
                        'entire_bracket_tail': full_meta})
    return {'classification': 'FINITE CERTIFIED SINGULARITIES; NOT NON-D-FINITENESS',
            'bits': BITS, 'count': len(results), 'checks': results}


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2))
