"""Independent Fraction checks for the new finite-certificate arithmetic."""
from fractions import Fraction as F
import random
import pytest
from proofs.m7_finite_poles import I384, SCALE

def endpoints(box):
    return F(box.lo,SCALE),F(box.hi,SCALE)

def contains(box,values):
    lo,hi=endpoints(box)
    assert all(lo<=value<=hi for value in values)

def test_fraction_oracle_for_signed_interval_operations():
    rng=random.Random(71024)
    for _ in range(150):
        a,b=sorted(F(rng.randint(-1000,1000),rng.randint(1,1000)) for _ in range(2))
        c,d=sorted(F(rng.randint(-1000,1000),rng.randint(1,1000)) for _ in range(2))
        x,y=I384(a,b),I384(c,d)
        contains(x,[a,b]);contains(y,[c,d])
        contains(x+y,[a+c,b+d])
        contains(x-y,[a-d,b-c])
        contains(x*y,[u*v for u in (a,b) for v in (c,d)])
        if not c<=0<=d and not y.lo<=0<=y.hi:
            contains(x/y,[u/v for u in (a,b) for v in (c,d)])

def test_square_roots_enclose_rational_squares():
    for a,b in [(F(0),F(1,7)),(F(1,10**24),F(1,10**23)),
                (F(4,3),F(111,17)),(F(10**50),F(10**50)+1)]:
        root=I384(a,b).sqrt()
        lo,hi=endpoints(root)
        assert lo>=0 and lo*lo<=a and hi*hi>=b

def test_invalid_divisions_and_roots_are_rejected():
    for a,b in [(0,0),(-1,1),(-1,0),(0,1)]:
        with pytest.raises(ArithmeticError):
            I384(1)/I384(a,b)
    with pytest.raises(ArithmeticError):
        I384(-1,1).sqrt()
