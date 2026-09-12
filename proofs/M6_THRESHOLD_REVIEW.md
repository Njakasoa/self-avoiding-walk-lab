# Review of the M6 reduced existence threshold

Status: **accepted for existence and numerator noncancellation at
N>=10^46**. The sharp kernel hypotheses B=10^12 have now been independently
accepted in M6_SHARP_KERNEL_REVIEW.md, with exact reviewed source hashes.
M6_REAL_RATE_DOMAIN.md restricts the common moment domain to e<=10^-10;
the threshold application satisfies it. No effective uniqueness or
effective simplicity threshold is asserted.

## Analytic aggregation

At e<10^-46 the three terms of the polynomial-constant moment estimate
are bounded by1/(100sqrt(10)),1/100 and10^-32. The exact interval sum
is less than1/50. Monotonicity of all three error terms in e justifies
using this domain endpoint; no floating fourth-root approximation enters.

The independently reviewed directed theorem gives c_D>3/4 and remainder
at most100e log(1/e). Since this expression increases on the small-e
domain, its largest value is bounded at10^-46 and is below10^-41.
Thus the positive additive constant dominates that remainder and
D>log(1/e)/sigma>logN/sigma. The claimed delta<1/250 follows.

The outward endpoint calculations and post1>0 imply p is increasing,
since B'>0. The endpoint hull therefore bounds the entire sector by
-7.5<p<-3.6 without direct overestimation across a broad trigonometric
interval. The moment error gives -8<1+P_N<-3.5, uniformly, which prevents
numerator cancellation on the whole band.

The F-error budget is correct: the P,H errors contribute at most4E;
the t change contributes(|P0|+1)e²/8<2e²; and the directed term contributes
at most16delta. Their sum is below .15. The limiting endpoint margins
F0(.8)>1 and F0(.9)<-.2 then give opposite finite signs. Phase separation,
nonzero physical denominators, local analyticity and disjointness of the
bands give the stated existence/noncancellation consequence, conditional
on the sharp moment input. No effective uniqueness or simplicity is
inferred.

## Domain clarification

M6_REAL_MOMENT_RATE.md states e<=10^-8, but its inherited M5 weight
lemma is stated on e<=10^-10. This review relies only on the intersection
e<=10^-10; the threshold application e<10^-46 lies well inside it.
A scope clarification should accompany the broader real-rate statement
unless the weight estimates are separately extended. No old frozen source
needs alteration for the present threshold argument. The present review
does not certify that larger e domain by implication.

## Independent exact replay

`python -m proofs.m6_threshold` passed all checks. Execution with `-O`
failed immediately at the intended assertion-engine guard. Independently
replayed enclosures include a moment budget below .013162277661 and
delta below .003910666619. Endpoint F0 intervals lie inside
[1.007818072342,1.040961172122] and
[-.223923614807,-.206386634122], respectively.

The critical source is the previously reviewed4096-rectangle M5 payload;
the coefficient helper re-encloses c_D using the reviewed digamma method.
No finite numerical root or fitted coefficient is used in this threshold
checker. The code checks final arithmetic, not the sharp analytic kernel
premise.

| Reviewed source/output | SHA-256 |
| --- | --- |
| proofs/M6_THRESHOLD.md | `80420d55c9c281fa4d2410ced688f0d9b3e6f3061807506ffe3885df6802bf00` |
| proofs/m6_threshold.py | `3ee1d185a700456f3d2d74c2ec6488f075ee18dfc8fd6757cdf8d3cec8df07c6` |
| Independent stdout | `09a23c792997b326a04bb4461b1b55d2ed13fd2fed14a06b630e2eba72c570ab` |

Independent output: `/tmp/m6-review-threshold.json`.

## Goal coverage versus theorem validity

Replacing2^(10^120) by10^46 is a substantial structural reduction arising
from a new sign argument and polynomial constants. It is more than changing
an astronomical exponent inside the same proof. Nevertheless10^46 remains
far outside feasible numerical enumeration. The M6_PLAN target of a
"useful and interpretable finite threshold" is not automatically satisfied
by calling this number useful. The final goal audit must distinguish the
proved reduction from any remaining practical-threshold objective and
must not close M6 on second-order asymptotics alone.

Root clarified the intended completion criterion as the second logarithmic
term plus a substantial structural threshold reduction, with computational
usefulness an optimization target rather than a fixed required index.
Under that scope, an accepted10^46 theorem would satisfy the reduction
axis. A computationally useful low-N threshold must still be reported as
not achieved and retained for later research; it is not claimed here.
