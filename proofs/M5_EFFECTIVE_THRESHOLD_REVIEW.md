# Review of the M5 effective existence threshold aggregation

Status: **ACCEPTED at the internal mathematical-draft gate for the explicit
real moment bound and W existence/noncancellation threshold
N0=2^(10^120)**. This does not accept an effective uniqueness or simplicity
threshold. All component inputs and requested corrections were reviewed.

## Aggregation checks completed

The ledger uses x_n=n e throughout and therefore correctly keeps Q/e as
its moment prefactor. Root-center motion is handled inside the Gamma/profile
comparison rather than by a second moving mesh. The compact absolute
product bound is exp(10B); the growing interval uses small logarithmic
*relative* errors. The tail is started at a fixed point. This avoids the
invalid exp(B S) growth that an absolute product bound at the growing
cutoff would produce.

The proposed crossing exponent .76 exceeds eta_e<=.72, and its integral
exponent is .24. At rho=e^(1/4) this gives e^.06. With eta<.71, the
Hölder quadrature term has exponent at least .0725. Their strict margins
above .05 absorb the displayed logarithmic factors for L>=10^100.
The fixed prefactor A^4=exp(4*10^54) is below exp(10^60). These power and
constant comparisons are valid, conditional on the component bounds and
the detailed ledger constants they supply.

One requested bookkeeping clarification: the relative error (R) multiplies
a *discrete* critical weighted mass. The integral mass bound in item5 is
not literally that sum. Its Hölder quadrature estimate, together with
L>=10^100, bounds the discrete mass by2A after excluding the crossing
window; stating this explicitly closes the sum-to-integral multiplication.
The same domain makes the relative logarithmic error less than .1 before
exponentiation. No growing absolute exponential should be introduced.

## Final arithmetic and scope

Independently replayed `python -m proofs.m5_effective_threshold`; every
reported exact rational check passed. Its logarithm lower bound uses
three positive atanh terms, and its log10 upper bound uses a strict
exponential-series lower bound. The directed reciprocal simplification,
critical endpoint signs and numerator enclosure are consistent with the
previously independently reviewed critical payload.

For N>=2^(10^120), logN>.69*10^120, so the proposed moment error has
logarithm below-1000 and is less than10^-100. The directed error bound
is also below10^-100. The coefficient30 in the final F-error budget is
conservative: moment errors, parameter displacement and the term
2(1-D_I)(1+P_N) all fit within it on the certified critical bracket.
The resulting endpoint margins and nonzero numerator suffice for at
least one noncancelled pole in each band. Phase/source-pole exclusions
and the previously established local analytic continuation supply the
necessary holomorphy.

This threshold, if the remaining analytic inputs pass, applies only to
existence and noncancellation. It does not make uniqueness, simplicity,
residue errors or practical finite-index validation effective. The code
correctly labels its output final arithmetic conditional on the analytic
moment bound; its success is not acceptance of that bound.

## Initially pending checks, now completed

The effective Gamma and weight domains/constants, their insertion into the
ledger, and the discrete-mass clarification were subsequently checked as
recorded below. The final accepted hashes appear at the end of this report.

## Effective Gamma and weight review

The final Gamma inequalities have been checked from the added elementary
log-convexity derivation of Wendel's inequality. The positive Gamma forms
use shifts in [0,1], with the nearest post argument at least .1; Wendel
therefore gives the explicit absolute and logarithmic ratio bounds without
an unspecified asymptotic constant. The sine multiplier is below5 and its
logarithmic derivative below13. The resulting1000 domination constant
and3/a+3/|n-a| logarithmic error are conservative. The center-shift loss
is correctly described as a multiplicative10^6 allowance, rather than
an unjustified replacement of1000 by10^6.

The ledger's fixed crossing window has been reduced from .1 to .05 to
meet the Gamma condition |x-s_g|<=s_g/2. The newly stated domain checks
also imply a>=200, sufficient distance from the crossing for the relative
formula, and a small logarithmic error before exponentiation. These
conditions are all satisfied on L>=10^100.

The weight note's explicit real kernel and divided-difference bounds were
checked, including the square-root endpoint. Its lower u_h bound now uses
tq>.4059>.4, which actually implies u_h>2/3; the earlier .4(1-e/2)
argument did not. Its off-crossing weighted Hölder constant was increased
from10^10 to10^15. This increase is necessary to follow from the stated
M' bound and the phase, weight, kernel and center-conversion factors;
10^15 safely dominates their product and remains far below A.

The explicit critical mass and exponentially decreasing tail bounds fit
the ledger with ample margin. The corrected discrete-mass bridge applies
the same Hölder estimate to the absolute weighted profile and bounds
the off-crossing discrete mass by2A. Thus relative product errors are
multiplied by a justified discrete bound, not merely an integral bound.

The rational weight-box checker was independently audited and replayed.
Fraction interval arithmetic, reciprocal ordering and first-order Jet
product/quotient rules are correct. Its V1,V2, two boundary expressions
and Q/e match the exact regularized formulas. The parameter box contains
both the physical and critical values and their connecting segments.
The replayed output SHA-256 is
`e50ff0af82b2751b94593d6255df5df62d399a7e13202d07c7ce9d686e2b7d0c`.
The weight note now explicitly applies its Jacobian bound in equations
(42)--(43) to the boundary and Q/e perturbations. Their critical values
match the accepted moment identities; the connecting parameter segments
remain inside the rational box and every coordinate changes by at most e.
The reported Jacobian bound below452 and values below5 were independently
checked in the replay output. The extra t² perturbation in H is explicitly
accounted for. This closes the final missing ledger connection.

## Final verdict and provenance

No unresolved analytic or arithmetic blocker was found for (E) on
log(1/e)>=10^100 or the resulting existence/noncancellation guarantee at
every integer N>=2^(10^120). The theorem guarantees a pole in each
specified phase band. It gives neither a practically useful first index
nor an effective uniqueness/simplicity/residue threshold. Acceptance is
internal mathematical review, not proof-assistant formalization or external
peer review.

Observed source base: `24b383916083ad18ca9b57594571bdbd37a1f588`.
Final reviewed SHA-256 values:

| Input | SHA-256 |
| --- | --- |
| proofs/M5_EFFECTIVE_KERNEL.md | `8eed3eefc97ee2fbefc09aa51f3de161c30de23d6c520303503ef7f1f8faa090` |
| proofs/M5_EFFECTIVE_GAMMA.md | `3b4464ca52bf73db69916d900d66f7c21a28a455a4bc6d5bef6a708570676f86` |
| proofs/M5_EFFECTIVE_WEIGHTS.md | `3e941af8ac231dfb1833645459dd44dbdd697fb3502ba064c5d0d6d283c4e716` |
| proofs/M5_EFFECTIVE_THRESHOLD.md | `5caf2b70e21ca0a4ec6ade19433e448e69f6b8aa13b2f0796e3043d7c9364c56` |
| proofs/m5_weight_boxes.py | `d3d4ef42411eb1ea336a7d62d0b45716a3b4181f2d0577c6580b20150a5f4e15` |
| proofs/m5_effective_threshold.py | `1f5ce269f338c91a3a41a039a61be38c3672c9184fc496ddfa6a6b06887709b8` |

Independent final-arithmetic stdout SHA-256:
`14fa94108a43eae95db544f19f4d9b1a2be6ce5fce31751f7f684fb60f1af481`.
Independent weight-box stdout SHA-256:
`e50ff0af82b2751b94593d6255df5df62d399a7e13202d07c7ce9d686e2b7d0c`.
Root owns the canonical combined source-frozen receipt and its final
comparison against these outputs. Subsequent mathematical changes require
reviewing the changes, not merely updating a hash.
