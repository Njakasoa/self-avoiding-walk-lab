# M5 directed derivative and W transfer review

Status: **ACCEPTED at the internal mathematical-draft gate for the directed
derivative bound and non-effective W transfer statements**, following
verification of the requested wording corrections.
This is internal AI review, not external peer review or acceptance of an
explicit W first index.

## Verdict by assertion

| Assertion | Review outcome |
| --- | --- |
| Directed derivative bound1500/e | Accepted; constants and local differentiation justification checked. |
| Directed phase derivative30000/N | Valid consequence of the derivative bound and accepted phase certificate for N>=20. |
| Logarithmic phase displacement | Valid conditional on accepted moment/logarithmic inputs; minus sign verified. |
| Eventual unique simple pole per phase band | Accepted using the completed directed derivative lemma; no effective threshold supplied. |
| Negative limiting residue coefficient | Formula and sign verified. |
| Residue error O(N^-3/logN) | The proved directed bound O(1/N) already suffices, together with accepted moment derivative rate. |
| Spatial logarithmic correction | Expansion and signs verified. |
| Explicit W N0 or finite512 validation | Not established or accepted by this review. |

## Directed derivative estimates

The algebraic rewrite d_k=r*a*b(e k)/(k(1+u_k)) is exact. The elementary
parameter bounds imply |r_e|<7, |c_e|<13, |a_e|<1 safely; no tight constant
is required. For k<=floor(1/e), differentiating u_k gives the terms
c_e(1-e^-e)w, c e^-e w and c(1-e^-e)w' k. Their stated bound29/(e k)
is conservative. The derivative of d_k is bounded by10/k+3+90/(e k²),
whose sum is less than200/e.

For the tail, |u_k'|<=16(1+x)e^-x is valid because e<=.1. The three
derivative contributions to d_k are bounded respectively by
20e e^(-x/2),18(1+x)e^(-x/2), and at most
9.6(1+x)e^(-x/2); hence the displayed coefficient28 is sufficient.
The geometric bounds yield80+1008/e<=1016/e<1020/e.
Together with the initial derivative,1500/e is safely above the sum.

The phase-certificate margin gives |e_theta|<=20e², and e<1/N for
N>=20. Therefore |D_theta|<=30000/N and positivity of D gives the same
bound for |(D_I)_theta|. With the accepted large-N logarithmic lower bound,
the extra factor4sigma²/(logN)² is valid. No asymptotic differentiation
of a merely O(1) directed remainder has been used.

### Requested correction, now verified

The sentence following equation (2) says positivity makes differentiation
legitimate and that the estimates are summable uniformly as e decreases
to zero. Positivity alone does not justify differentiation, and the bound
1500/e is not uniform at zero. The needed valid statement is that (13)
gives a summable derivative majorant on every compact
[e0,1/10], e0>0. The derivative series therefore converges uniformly there
and may be differentiated termwise; the resulting parameter-dependent
inequality then holds for each positive e. This local justification is
sufficient and follows from the estimates already written.

Also, s_g is the prudent g-zero phase coordinate used in the accepted
moment construction; calling it the phase of a "directed singularity"
is inaccurate. Both corrections are now present and have been verified.
Neither changes any numerical estimate. The transfer text now explicitly
cites 30000/N and its o(log^-2 N) consequence for the derivative remainder.
The discussion above records the original concern and its resolution.

## W transfer details

The exact decomposition adds2(1-D_I)(1+P_N) to the D_I=1 expression.
The accepted algebraic moment rate is eventually O(log^-2 N), yielding
F_N=F0+2sigma(1+P0)/logN+O(log^-2 N) uniformly. The strict negative
limiting derivative first locates every root within O(1/logN) of theta*,
and Taylor expansion gives

    theta_N=theta* - [2sigma(1+P0(theta*))/F0'(theta*)]/logN
                     +O(log^-2 N).

The coefficient in brackets is positive; the negative displacement is
essential. Uniform derivative convergence makes F_N strictly decreasing
on the whole band eventually, so the root is unique and simple there.
This uses the already accepted exclusion of source poles on late bands
and the nonzero numerator. The signs e_theta<0 and t_e<0 imply t_theta>0.

Changing coordinates in the simple-pole residue gives exactly

    Res W=-(1+P_N)*t_theta/F_N'.

Since t_theta=s*²/(8N³)+O(N^-4), its limiting coefficient is
-(1+P0(theta*))s*²/(8F0'(theta*))<0. For the sharper error, the directed
O(1/N) phase derivative already implies an O(log^-2 N) derivative
remainder. The stronger directed logarithmic estimate is sufficient but
unnecessary. Taylor variation of the limiting numerator and derivative
over the O(1/logN) phase shift then gives O(N^-3/logN).

Direct differentiation of the inverse-kernel expression at e=0 gives
s_g'(0)=sigma/(2(1-sigma))=eta/2. The e expansion and t=sigma-e²/16+O(e⁴)
therefore yield the stated spatial expansion, including the positive
2K*C_shift/(N³logN) term. An O(N^-4) remainder is absorbed in
O(N^-3/log²N). No unknown second derivative of s_g enters the displayed
N^-3 coefficients.

## Numerical implementation and scope

The independent diagnostic code evaluates the same kernel inverse and
positive directed sum, with a valid analytic expression for a positive
truncation-tail bound. Its centered differences and floating-point tail
values are appropriately described as diagnostics, not derivative
certificates. No heavy run was repeated during this proof review.

The conjectural additive directed constant is explicitly marked unused;
this review does not accept it. It is not needed for the derivative or
transfer results.

## Provenance

Observed source HEAD: `8232d82e372860319b5562fef33a5982293ddbca`.
Reviewed final SHA-256 values:

| File | SHA-256 |
| --- | --- |
| proofs/M5_DIRECTED_REFINED.md | `08668a0ddbba107c2f56cc88e0d5f1b549c9ddec92490f4d35ba5f4e4005e38a` |
| experiments/m5_directed_refined_check.py | `2877c0bd9595f2f4cbb3bf7d1ca08abb031fb2005b3b998cbef7c90dc2c370af` |
| proofs/M5_W_QUANTITATIVE.md | `2dc1dee4dae9a0fb58604f7c6d0b630f0410d7074732e1b1c9c202463608763f` |

No new numerical output was produced by this bounded review. Acceptance
uses the separately reviewed moment rate, directed logarithmic theorem,
phase-domain certificate and critical coefficient certificate. Their
combination proves the non-effective eventual statements here, not an
explicit W threshold. Subsequent mathematical changes require reviewing
the changed text.
