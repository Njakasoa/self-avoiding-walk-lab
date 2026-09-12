# Independent review of the sharp M6 kernel

Status: **accepted for the stated real hypotheses (P), with B=10^12**.
The common domain for using the moment estimate is 0<e<=10^-10,
as explicitly recorded in M6_REAL_RATE_DOMAIN.md. This review does not
claim effective uniqueness or a computationally useful small threshold.

## Analytic checks

The discriminant and denominator margins in (4)--(5) select one analytic
square-root branch on the auxiliary parameter disk and s tube. The
displayed derivatives of U and g are correct. The bounds on t_e, D_e,
U_t and g_es use that same domain; the Cauchy bound for t_e follows from
a circle of radius R-|e| about e inside the larger disk of radius R.

On the root circle the critical linear term dominates its quadratic
remainder. The combined perturbation for g+delta is smaller than this
margin. Rouché therefore gives one root for each kernel, and its
multiplicity is one. The tube is convex. The real critical slope margin,
the g_ss bound and the parameter derivative bound give positive real
part of g_s on the tube, including segments joining complex roots to
complex s. Thus both divided differences have positive real part and
bounded modulus, so their principal logarithms are analytic. No division
by a vanishing kernel is hidden in this construction.

The parameter Taylor estimate gives 4*10^11 e for the normalized log
remainder. Cauchy in the fixed s tube bounds the derivative of psi,
including at the interval endpoints. The final correction to (22) writes the exact numerical equalities
20/r_e = 2*10^6 and 20/(r_e*r_s) = 2*10^10. I checked the corrected
bytes; the preceding strict function bounds are unchanged. No constant
depends on a growing cutoff.

The exterior comparison uses the square-root difference inequality and
therefore remains valid at the critical endpoint s=0. It does not
differentiate a square root at its zero. The lower bounds on the exterior
kernel and root distances justify both logarithm expansions uniformly.
The eta error is e/.02 + .3*6501e/(.02*.4), less than 300000e;
this yields the claimed [.70,.72] range. The exterior Holder bound is
the purely critical inherited estimate; gluing three intervals costs
at most sqrt(3). These estimates fit within B=10^12.

The scalar r and z0 estimates follow from their exact displayed formulas.
In particular the explicit .208e + .30e estimate closes the .52e
denominator allowance for z0. The real root ordering and positive-series
concavity argument supply 0<R<=1; taking the first parameter limit gives
psi<=0. Together with the exterior formula and local Cauchy estimate,
this supplies all (P), not merely the log remainder.

## Exact replay and provenance

The checker certifies rational arithmetic allowances only. Its header
correctly excludes branch choices, identities and inherited analytic
inequalities from machine certification. I reviewed those analytically
above. The corrected eta expression uses 1/.02=50. Both ordinary Python
and Python -O executions pass with byte-identical stdout: checks use
explicit conditional raises and remain active under optimization.

Review workspace HEAD: 411b55e4457b9a55b222506b5b303507ce61cc95.
The following file hashes, rather than that HEAD alone, identify the
reviewed newly written sources.

| Source or output | SHA-256 |
| --- | --- |
| proofs/M6_SHARP_KERNEL.md | `8717a3a191eb9f958f4b6a68d4066ae41bb8c13bc051985f3fe0791499158487` |
| proofs/m6_sharp_kernel_boxes.py | `705eac1b4ca87504094f3e1d705f0a3235f098382368ec4e75dad8a553d9ff77` |
| proofs/M6_REAL_RATE_DOMAIN.md | `fb08308744e8e273c7725da4d1f2fb862e7653ea8daf31ec425f56df6dea0588` |
| Independent stdout, ordinary and -O | `e8f5ad53d770337a82fdc08b1a96f82cce9aa8f3c574d7ea267abf76fffe66a5` |

Outputs: /tmp/m6-sharp-review.txt and /tmp/m6-sharp-review-O.txt.
The initial unavailable `python` command was retried successfully with
`python3`; the hashes above identify the successful output.

The domain note resolves the inherited M5 weight restriction without
silently extending it. Since e_N<10^-46 at the proposed threshold, the
restriction has no effect on that application. This acceptance removes
the pending sharp-kernel condition in M6_THRESHOLD_REVIEW.md.
