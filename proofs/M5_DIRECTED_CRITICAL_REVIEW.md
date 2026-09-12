# M5 directed-log, phase-domain and critical-certificate review

Date: 2026-09-12. **Accepted for the internal mathematical-draft gate in
the limited scopes below.** This is internal AI review, not external peer
review. No finite W pole threshold or finite W residue is accepted here.

## Analytic directed-term bound

The exact summand reparametrization follows from alpha+beta=(1-t)(1-Q).
The physical-root bounds for e<=1/10 follow from F'(t)<=-4 and the displayed
cosh bound. The resulting bounds alpha>1/6, c<4, r<3 and d0<1 are valid;
c<4 also uses t>2/5. The estimate |r-1/sigma|<=5e safely exceeds the
displayed numerator estimate divided by sigma*alpha>1/15.

The harmonic comparison gives a total pre-cutoff deficit less than one,
tail at most eight and hence |H-log(1/e)|<=9. The regularization difference
is positive and bounded by 4 sum k^(-2)+8<15. Combining the estimates gives
1+5+27+45=78<80. Thus the real directed bound80 has explicit constants
and domain; its proof does not use the high-precision numerical checks as
interval certificates.

The reciprocal estimate is also correct: if D=logN/sigma+E with
|E|<=C*, the specified logarithmic threshold ensures
1+D>=logN/(2sigma), and subtraction of sigma/logN gives an absolute error
at most 2sigma²(1+C*)/(logN)². This statement concerns the directed term
only. The new phase-domain certificate makes its previously inherited
phase threshold effective.

## Real phase domain

The inverse-kernel expression v_g=q(d-t²)/(d(1-t²)) is correct. Its
logarithmic derivative, including the final +2t*t_e/(1-t²) inside the
brackets, has the correct sign. The bounding parameter box covers the
entire real e interval [0,1/100], including t_e in [-1/400,0].
Interval dependence enlarges enclosures but does not invalidate them.

The positive enclosure for s_g-e*s_g' makes a=s_g/e strictly decreasing.
Its value at e=1/100 is less than20 and its limit at zero is infinite;
therefore every N>=20 and theta in [.8,.9] has a unique inverse in this
domain. Multiplication by N/(N+theta) in [200/209,1] gives the stated
ratio. The logarithm-offset and reciprocal checks prove the fully
effective **directed-only** threshold N>=2^108 with error constant31.
They do not make the moment-rate constants or the W pole threshold
effective.

## Exact critical-function certificate

The implemented constant and B coefficient are the exact expansion of
F0=(1-sigma)P0-4H0-(3+sigma). The derivative B'=A*pi*sin(pi*eta)/
sin²(pi*(eta-theta)) is correct. Sector separation excludes a sine zero,
and the interval derivative is strictly negative throughout [.8,.9].
Opposite certified endpoint signs at .8695 and .872 therefore enclose
one unique zero of the limiting function.

The logarithm helper uses a uniformly convergent atanh series and an
absolute geometric bound for the first omitted odd power. Its interval
operations enclose the entire input interval, including when y is
negative; the radius bound keeps its remainder denominator positive.
The unchanged inherited dyadic power and quadrature engine supplies the
four integral enclosures at 4096 subdivisions.

At the limit root, the certificate encloses the algebraic expressions

    A_shift=2sigma(1+P0)/F0',
    A_distance=s*²/16,
    A_residue=-(1+P0)s*²/(8F0').

Their signs and enclosures are accepted as properties of the limiting
functions. For subsequent root transfer, A_shift is positive but denotes
the magnitude of a **negative** phase displacement:
theta_N=theta_* - A_shift/logN + smaller terms, if the requisite transfer
theorem is proved. No plus-sign displacement follows from this certificate.
The residue coefficient is negative. Finite poles, simplicity and
asymptotic residue transfer remain separate analytic obligations.

## Independent replay

Both root certificates were independently run in full:

- `python -m proofs.m5_phase_domain`: PASS. Phase threshold20;
  directed threshold2^108; reciprocal-error constant less than
  30.28008717<31. The required log threshold is below73.10259711,
  whereas 108log2 exceeds74.85989550.
- `python -m proofs.m5_critical_pole`: PASS at 4096 rectangles and
  16-bit exponent enclosure. Root bracket [.8695,.872]; entire-sector
  derivative upper bound -5.65241069; positive shift coefficient in
  [.38696091,.44166261]; residue coefficient in
  [-.00167097,-.00146400].
- Both module entry points reject Python `-O` before computation.

No heavy finite phase sweep was performed. These arithmetic runs do not
certify a finite W pole or an effective W first index.

## Provenance

Source base: `2893bbe27f2e65449bfc345c9f7a874faa185129`.
Reviewed SHA-256 inputs and independently replayed JSON stdout:

| File | SHA-256 |
| --- | --- |
| proofs/M5_DIRECTED_LOG.md | `fcf18e907607e185cb8dba7e4c25c58c8df3aa5088027429fc33d86677c9cf1f` |
| proofs/M5_PHASE_DOMAIN.md | `e28526758615f3d3d2279dda542b381c9a5d69313f770c5c4a6e5c57863065bf` |
| proofs/m5_phase_domain.py | `76b0b18fcb282e9d303754293258a1dedc7069514032814d9a833eba55310c97` |
| proofs/m5_critical_pole.py | `2e5920d14c891bbf9e59370f0a86e7a6eea9cb23d70b4b22cd151979e7724752` |
| Independent phase JSON | `943ced6d37580cdf8e85c889ec51036e79cacb1d1ebbe0fca2bf3c28ed22f61f` |
| Independent critical JSON | `f94823cf257ffd1c9cf6becea60c07cad100232b787e4253ba7d18681557fd8b` |

Independent outputs currently reside in `/tmp/m5-review-phase.json` and
`/tmp/m5-review-critical.json`; root owns permanent retention and canonical
source-frozen receipts. Any later scientific source change requires a
review of the change, not merely a replacement hash.
