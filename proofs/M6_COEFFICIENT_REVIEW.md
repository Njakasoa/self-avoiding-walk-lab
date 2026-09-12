# Review of the conditional M6 coefficient enclosure

Status: **ACCEPTED as an exact enclosure of the displayed conditional
coefficient expressions**. This does not establish the directed additive
constant theorem, the second-order asymptotic theorem without that input,
or a reduced effective threshold. Internal AI review only.

## Digamma and logarithm arithmetic

Independently checked the formula and positive-real remainder rule in
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[DLMF5.11(ii)](https://dlmf.nist.gov/5.11.ii). Retaining the Bernoulli
terms -1/(12z²),+1/(120z⁴),-1/(252z⁶) leaves a nonnegative remainder
bounded by1/(240z⁸). The code adds the interval from zero to the outward
upper endpoint of that expression, which encloses the remainder for every
positive z in the input interval.

The argument sigma+3 equals2+sqrt(2), and the shift64 keeps the asymptotic
evaluation on a positive interval. Subtracting sum_(k=0)^63 1/(x+k)
implements the digamma recurrence with the correct sign. This is a
bounded remainder argument, not an assumption that an asymptotic series
converges.

The logarithm helper's powers-of-two scaling preserves the exact identity
log(x_original)=log(x_reduced)+k log2. Interval division/multiplication
by two encloses the reduced interval, and the inherited atanh-series
helper supplies its remainder. All actual reduced arguments stay positive
and within its uniformly convergent domain. No floating-point logarithm or
digamma value enters the certificate.

## Reuse of the critical enclosure

The retained M5 critical payload has the previously reviewed hash below.
Its integral intervals and theta* bracket are recovered at384-bit dyadic
precision. The code reconstructs p,J,B,B' and C1 from those intervals;
the sine denominator and f denominator are separated from zero on the
bracket. Computing cosine as sin(pi/2+angle) is exact before interval
enclosure and does not reverse the cotangent sign.

The expression for C2 matches the independently reviewed conditional
transfer formula:

    C2=C1*(b+2sigma*post1/J)-pi*cot(pi*(eta-theta*))*C1².

Repeated occurrences of interval variables enlarge the enclosure but do
not remove possible values. The spatial second logarithmic coefficient
is -2K*C2, with the correct negative sign. The positive C2 check is a
property of this interval expression, conditional on identifying the
directed constant analytically.

## Independent replay and provenance

`python -m proofs.m6_second_coefficient` independently passed and gave

    b in [2.569062496883,2.569062496884],
    C2 in [0.844491934033,1.148455190184],
    -2K*C2 in [-0.003599521365,-0.002646830964].

Execution with `-O` failed immediately with the intended optimization
guard, before interval calculations. No finite phase data were fitted or
used in this replay.

| Input/output | SHA-256 |
| --- | --- |
| proofs/m6_second_coefficient.py | `2cb987601187cb6620a47428587e1b6549468ff5b2d6bc2076e6a5d4c561ce9e` |
| results/m5-critical-v1/payload.json | `f94823cf257ffd1c9cf6becea60c07cad100232b787e4253ba7d18681557fd8b` |
| Independent JSON stdout | `8b17975deacb8d46f6a4ef7a1a17bcbac5a6e9e973574b52ebf4056ba56d14a1` |

Independent output is retained at `/tmp/m6-review-coefficient.json` for
comparison with root's canonical receipt. Subsequent source changes
require review of those changes. The analytic directed input remains
separate from the exact computation reviewed here.
