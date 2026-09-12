"""Independent analytic derivatives as oracles for interval jets."""
from fractions import Fraction as F
import random
import pytest
from proofs.m7_finite_poles import I384, SCALE
from proofs.m8_finite_derivatives import Jet384, directed_jet, kernel_jet


def test_tail_jet_is_json_serializable():
    import json
    from proofs.m8_finite_derivatives import _record_tail
    record = json.loads(json.dumps(_record_tail({'R': Jet384(F(1,2), F(3,2))})))
    assert int(record['R']['value']['lower_numerator']) == SCALE//2
    assert int(record['R']['derivative']['upper_numerator']) == 3*SCALE//2


def contains(interval, value):
    assert F(interval.lo, SCALE) <= value <= F(interval.hi, SCALE)


def test_rational_derivative_oracle():
    rng = random.Random(82026)
    for _ in range(100):
        lo = F(rng.randint(1, 100), rng.randint(1, 100))
        hi = lo + F(rng.randint(1, 10), 100)
        x = Jet384(I384(lo, hi), 1)
        y = (x*x+3*x+1)/(2*x+5)
        for p in (lo, (lo+hi)/2, hi):
            contains(y.x, (p*p+3*p+1)/(2*p+5))
            contains(y.d, (2*p*p+10*p+13)/(2*p+5)**2)


def test_log_square_root_chain_oracle():
    for lo, hi in [(F(1,100), F(1,50)), (F(1,3), F(2,3)), (F(4), F(9))]:
        y = Jet384(I384(lo, hi), 1).sqrt().log()
        contains(y.d, 1/(2*hi))
        contains(y.d, 1/(2*lo))


def test_singular_jet_inputs_rejected():
    with pytest.raises((ValueError, ArithmeticError)):
        Jet384(I384(-1,1), 1).reciprocal()
    with pytest.raises((ValueError, ArithmeticError)):
        Jet384(0, 1).sqrt()


def test_directed_derivative_against_separate_high_precision_formula():
    # A diagnostic oracle, not a proof certificate: at t=.2 the independently
    # coded 500-term formula has a negligible tail at the precision used here.
    import mpmath
    mp = mpmath.mp.clone()
    mp.dps = 80

    def directed(t):
        a = 1+t*t-t*(1-t*t)
        q = 2*t/(a+mp.sqrt(a*a-4*t*t))
        beta = (1-t-t*q)/(1-q*q)
        gamma = q*(t-q*(1-t))/(1-q*q)
        return mp.fsum(t*q**k/(beta+gamma*q**(2*k)) for k in range(500))

    t = Jet384(I384(F(1,5)), 1)
    q = kernel_jet(t, Jet384(1))
    value, tail = directed_jet(t, q)
    contains(value.x, F(str(directed(mp.mpf('0.2')))))
    contains(value.d, F(str(mp.diff(directed, mp.mpf('0.2')))))
    assert F(tail['tail_derivative'].hi, SCALE) < F(1,10**18)
