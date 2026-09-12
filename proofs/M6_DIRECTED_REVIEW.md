# Review of the directed additive constant and remainder

Status: **ACCEPTED at the internal mathematical-draft gate** for the
additive constant and remainder100e log(1/e) on0<e<=.01. The subsidiary
arithmetic typo, display delimiter and diagnostic scope label have been
corrected and independently verified. Internal AI review only.

## Parameter estimates

The hyperbolic identity and prefactor are exact. The signs alpha>0,
beta<0 and alpha+beta>0 imply z in(0,1). The parity identity
z=q² alpha(-e)/alpha(e) yields a_e=1+[log alpha(e)-log alpha(-e)]/e,
with limiting value1+1/sigma=2+sqrt(2).

The bounds on F derivatives and the three implicit derivatives of t are
valid. Alpha derivative bounds(9) are also safe. One supporting decimal
line is wrong: the displayed sum for alpha''' is .5694, so it is not
below .45. Replacing .45 by .57 repairs it and leaves the claimed bound
3/2 unchanged. The resulting bound on(log alpha)''' is less than200.
Taylor expansion of the odd difference therefore gives the stated
67e² error for a_e, and3<a_e<4. The prefactor error25e follows from
the earlier r estimate and the elementary exponential bounds.

## Regularized sum

For g(x)=1/(2sinh(x/2))-exp(-x)/x, the derivative comparison is valid:
sinh(y)<=y cosh(y) gives the needed lower bound for -f', and the power
series of exp(x)-(1+x)cosh(x/2) has nonnegative coefficients. Thus g is
decreasing, with endpoint limits1 and0, so it is positive. The exact
primitive of f and the Euler limit of E1 give integral g=log4+gamma.
This identifies the constant, rather than fitting it from finite values.

Monotonicity controls the shifted rectangle sum by one mesh step; the
omitted initial interval costs at most4e. This gives the5e estimate.
The display after equation(17) should be closed typographically.

The exponential harmonic part is expressed by an absolutely convergent
positive integral. Subtracting the a=1 case and using the digamma
integral gives the constant -psi(a)-gamma. The missing interval costs
at most6e and the elementary logarithm correction at most e, so7e is
valid. Adding the regularized part gives12e. The trigamma series bounds
the a_e-to-c change by30e², yielding13e as stated.

Finally, |S|<=3log(1/e), the prefactor error25e and1/sigma<3 give
75e log(1/e)+39e<=100e log(1/e). All limit exchanges have a stated
monotone, positive, or quantitative-integral justification. No derivative
of a remainder is assumed.

## Diagnostic review and scope

The script's transformed and original finite sums and analytic tail
formulas match the proof. Its mpmath evaluations are not outward-rounded
intervals. The comment calling their endpoint residual a "rigorous
residual enclosure" should be replaced by a numerical upper estimate
using the analytic tail formula. The document otherwise labels this code
diagnostic correctly. No long diagnostic replay was needed for this
bounded analytic review.

The identified local corrections are now present. This theorem supplies the
missing directed input for the independently reviewed second-order and
resummed phase transfers. It still does not by itself reduce the effective
W threshold or complete both parts of M6.

Final accepted source SHA-256:

- proofs/M6_DIRECTED_CONSTANT.md:
  `b45599ada46df5d992f81b142b5285ce062f02d04ae02234e76a21afab4caab3`.
- experiments/m6_directed_constant_check.py:
  `c9e3f02bc426f5d25ab96049ca68b771edf995bc7c59dae0e6cd45fa92d1de77`.

No numerical output was produced by this proof review. Later mathematical
changes require review of the changed text rather than merely a new hash.
