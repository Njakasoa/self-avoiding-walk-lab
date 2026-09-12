"""Independent algebraic tests of critical-integral enclosures."""
from fractions import Fraction
import pytest
from proofs.m3_prudent_intervals import I, SCALE
from proofs.m3_critical_integrals import real_power, pi_interval, sine


def test_rational_powers_by_integer_equations():
    # Rational exponent p/q is tested by raising the returned endpoints to q;
    # this checks inclusion without a floating real-power oracle.
    for base in (Fraction(1,100), Fraction(2,3), Fraction(1), Fraction(7,3), Fraction(10)):
        for p,q in ((1,2),(2,3),(7,5),(11,4)):
            got=real_power(I(base), I(Fraction(p,q)))
            assert Fraction(got.lo,SCALE)**q <= base**p <= Fraction(got.hi,SCALE)**q
    zero=real_power(I(0),I(Fraction(3,2)))
    assert zero.lo==zero.hi==0
    with pytest.raises(AssertionError):
        real_power(I(-1,1),I(2))


def test_machin_and_known_sine_values():
    pi=pi_interval()
    assert Fraction(314159,100000)<Fraction(pi.lo,SCALE)
    assert Fraction(pi.hi,SCALE)<Fraction(314160,100000)
    for divisor,value in ((6,Fraction(1,2)),(2,Fraction(1)),(1,Fraction(0))):
        got=sine(pi/divisor)
        assert Fraction(got.lo,SCALE)<=value<=Fraction(got.hi,SCALE)
