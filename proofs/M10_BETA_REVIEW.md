# Independent review of the signed real beta certificate

Verdict: PASS. The signed real interval certificate proves s_g'''>0 and
s_g'''<.414 on |e|<=1/180. Its integral consequence gives .70<beta<.72
and beta_theta<0 for every N>=32, theta in [.8,.9]. This discharges the
scalar assumptions in M10_REAL_PRODUCT_REVIEW.md. It does not give a
phase-derivative sign for the full W denominator.

The t-box follows from the physical even root and the M5 bound
sigma-t<=e^2/8, available on the larger real domain |e|<=.1. The signed
q-box is essential: negative e allows q>1. The explicit exponential
bounds give 359/360<q<360/359<1.003, so the supplied box covers both
signs. Its use as an independent interval overbounds correlations safely.
The full formula for s_g remains real and analytic on the signed box
because q, D-t^2, D and 1-t^2 are all certified positive.

Differentiating A(t)=2cosh(e/2) three times gives the displayed t', t'',
t''' expressions, including the factors 1/2 and 1/4. The q derivatives
are exactly -q/2, q/4, -q/8. I checked the Jet3 product, reciprocal and
log-third formulas term by term; they propagate ordinary derivatives,
not factorial-scaled Taylor coefficients. The implementation encloses
these formulas with outward I384 arithmetic. A separate symbolic oracle
for (x^2+1)/(x+2) at x=1/3 verified its value and first three derivatives,
and the third derivative of its logarithm, inside the Jet3 intervals.

The independent producer replay passed with JSON SHA-256
7a04339811087b634dbab95557810a3e6c933571d5af60163b8a60d0e7a32734.
The recorded dyadic s_g''' interval is positive and strictly below .414.
I also compared the printed decimal inequalities in the note against the
exact endpoints: all four displayed lower/upper decimal allowances are
outward, including the beta'/e pair.

Differentiating beta(e)=integral_(-1)^1 s_g'(re)dr and subtracting the
odd constant term yields e*integral r^2*integral s_g'''(ure)du dr exactly.
The integration weight has mass 2/3, giving beta'(e)>0 for e>0 and
beta'(e)<.276e. Integrating once more gives beta(e)<eta+.138e^2.
The exact eta and increment checks imply the asserted strip over the
entire domain. The accepted phase bounds give e_theta<0,
|e_theta|<e/N and e<.17/N<1/180 for N>=32. Hence beta_theta<0 and
|beta_theta|<(2/3)*.414*.17^2/N^3=.0079764/N^3<.008/N^3.
There is no extension of the old small complex Cauchy disk involved.

The note's finite-window absolute harmonic argument is also consistent:
.008*29/32^3<10^-5, and the relevant function decreases with N.
The stronger signed harmonic argument already reviewed in
M10_REAL_PRODUCT_REVIEW.md can now use the established beta_theta sign
on all N>=32. Neither argument extends the bare-product sign to an
undamped infinite tail or controls the other factors in the W moments.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M10_BETA_REAL.md | 51b59ecaea7fa22647d76471f8ecef9e8483581fdd3941a02d56b0fb22397f80 |
| proofs/m10_beta_real.py | 8387dd9af2896cdeef4871f008a495d0507aca96c27b21399fac0960458d3231 |

The independent replay used `.venv/bin/python -m proofs.m10_beta_real`.
The script rejects -O at import and reports explicit guarded claims.
No scientific source was edited by this reviewer.
