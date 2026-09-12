# Independent review of the small directed phase derivative

Verdict: PASS for the analytic estimate and exact arithmetic. On the stated
real domain, |D_R,e|<8/e. For every N>=32 this implies
-49/(1250N)<delta_D,theta<=0 and bounds the directed-parameter contribution
to partial_theta log L_W between zero and 28/(25N). This controls only one
component; the full denominator phase sign remains unproved.

The M5 exact summand representation applies on the larger real domain
0<e<=.1. Its summable derivative majorant on each compact positive e
interval justifies termwise differentiation here. Uniform summability at
e=0 is neither available nor needed. The M10 physical scalar bounds
and signed beta/phase certificate supply 0<e<1/180 and |e_theta|<e/N.

The implicit derivative inequality |t_e|<e/7 follows from A'<=-4 and
the displayed exponential majorant. Direct differentiation gives exactly
r_e=(t_e+t^2*q_e)/alpha^2 and
c_e=(q*t_e+t*(1-t)*q_e)/alpha^2, both negative. The alpha lower bound
and scalar boxes imply r<5/2 and |r_e|<3; the latter allowance is close
but valid, with rational value 1091360287/364140000<3. The integral
formula for a gives -1/2<a_e<0 and hence |(ra)_e|<17/4.

For u_k, the identity z^k/(1+z+...+z^(k-1)) has logarithmic e derivative
-k plus the weighted mean of 0 through k-1, at most -1. Multiplication
by the positive decreasing c preserves strict decrease. Therefore the
derivative of its reciprocal denominator is positive. In the formula
for -(d_k)_e this contribution is negative and can be dropped for an
upper bound. Bounding the remaining positive reciprocal factor by one
gives equation (1). This is a one-sided estimate, not an absolute-value
bound on each derivative term.

For b, the derivative ratio is coth(x/2)/2-1/x. Its positivity follows
from y*cosh(y)>sinh(y); its strict upper bound 1/2 follows from
exp(x)>1+x. The same exponential inequality gives
x/(1-exp(-x))<1+x. The two geometric sums therefore yield
e*sum b(ke)<6 and e*sum[-b'(ke)]<3. The harmonic/logarithmic sum is
bounded by log(3/e)+2. Its product with e is increasing on the entire
stated interval and is less than 1/20 at its upper endpoint, using
log 540<7. All inequalities have the correct direction.

Including the k=0 derivative gives the exact allowance
-e*D_R,e<12001054133711/1556049806640<8.
The independently reviewed M10 monotonicity plus differentiability gives
D_R,e<=0, so this one-sided bound becomes the claimed absolute bound.
Without that sign input this last step would not follow; the note supplies
it explicitly. With e_theta<0, D_R,theta>=0 and delta_D,theta<=0.
Using delta_D<.07 then gives 8*(.07)^2=49/1250. The combined-weight gap
>.07 implies |partial_delta log L_W|<200/7, and multiplication gives
28/25 with a nonnegative phase contribution. Other parameter derivatives
are correctly left outside this conclusion.

I independently replayed the Fraction checker; all nine checks pass and
match the displayed proof formulas. Its sorted JSON SHA-256 is
410b404d2c33eda504667dde823124fb918545e65b6272203877fd27b6971103.
The checker explicitly describes arithmetic-only scope and does not
replace the analytic differentiation and summation argument.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M11_DIRECTED_PHASE_BOUND.md | efe6b4c4a57e502cb4ff9b04835aaed556463c83d7cbc5e0d86cf73b687ef08e |
| proofs/m11_directed_phase_bounds.py | 51de328cd9f840c21a40ad86da8dc7eb472c892c7dc85b3256dd96c414997e47 |

The inherited M5 derivative and M10 scalar/monotonicity inputs are covered
in M10_BETA_REVIEW.md and M10_DIRECTED_REVIEW.md. No scientific producer
or proof was edited by this reviewer.
