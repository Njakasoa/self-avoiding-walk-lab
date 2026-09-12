"""Independent rational spot checks of outward rounding and singularity signs."""
from fractions import Fraction
import random
import pytest
from proofs.m3_prudent_intervals import I, SCALE, enclose, produce


def contains(interval, value):
    assert Fraction(interval.lo, SCALE) <= value <= Fraction(interval.hi, SCALE)


def test_outward_arithmetic_against_rationals():
    rng = random.Random(921)
    for _ in range(100):
        a, b, c, d = [Fraction(rng.randint(-100, 100), rng.randint(1, 100)) for _ in range(4)]
        a, b = sorted((a, b)); c, d = sorted((c, d))
        x, y = I(a, b), I(c, d)
        for p in (a, (a+b)/2, b):
            for q in (c, (c+d)/2, d):
                contains(x+y, p+q)
                contains(x-y, p-q)
                contains(x*y, p*q)
                if c*d > 0:
                    contains(x/y, p/q)
        if a >= 0:
            root = x.sqrt()
            assert Fraction(root.lo, SCALE)**2 <= a
            assert Fraction(root.hi, SCALE)**2 >= b


def test_invalid_domains_fail_closed():
    with pytest.raises(ArithmeticError):
        I(1)/I(-1, 1)
    with pytest.raises(ArithmeticError):
        I(-1, 1).sqrt()
    with pytest.raises(RuntimeError):
        enclose(I('0.1'), max_terms=1)


def test_five_disjoint_singularity_brackets():
    data = produce()
    assert data['count'] == 5
    previous = Fraction(0)
    for row in data['checks']:
        lo, hi = map(Fraction, row['bracket'])
        assert previous < lo < hi
        previous = hi
        assert int(row['P_plus_one_left']['upper_numerator']) < 0
        assert int(row['P_plus_one_right']['lower_numerator']) > 0
        h = row['H_plus_one_entire_bracket']
        assert Fraction(int(h['lower_numerator']), 2**h['denominator_power_of_two']) > Fraction(9, 25)
        for key in ('left_tail', 'right_tail', 'entire_bracket_tail'):
            b = row[key]['tail_B_abs']
            assert int(b['upper_numerator']) < 2**b['denominator_power_of_two']
