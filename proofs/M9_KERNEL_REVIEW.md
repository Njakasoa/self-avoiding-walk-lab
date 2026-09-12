# Independent M9 product and complex-kernel review

Verdict: the two analytic estimates are valid with the inherited hypotheses
specified below. This review accepts the finite-variation product estimate
and the complex moment domain N>=10^15. It does not establish an improved
real moment error, a new uniqueness threshold, low-index coverage, or novelty.

## Critical variation and real product

M6_SHARP_KERNEL.md supplies all required estimates on 0<e<=10^-8:
its equations (22), (28), (35), and (37) give the middle derivative bound,
exterior separation, scalar estimate, and uniform logarithmic estimate.
Its final sign discussion explicitly extends the older real concavity
argument to this domain. Thus the smaller domain in the historical
M6_EFFECTIVE_PRODUCT.md does not invalidate this use.

At the critical parameter the positive-series proof makes g0 increasing;
the explicit kernel is smooth for s>0 away from its removable expressions.
The exterior integral of g0'/g0^2 is consequently controlled by reciprocal
endpoint values. The improper endpoint at zero is legitimate: g0 is
continuous and bounded away from zero there even though g0' can diverge.
The stated endpoint values -sigma^2 and sigma^2 are correct. The middle
removable value is analytic by the inherited divided-difference construction,
so the middle variation estimate applies across s*. Gluing the pieces gives
TV(psi)<3*10^9+27+625<4*10^9. In particular no endpoint Lipschitz hypothesis
has been introduced.

The one-cell rectangle error follows directly from the definition of total
variation. Variation is additive on adjacent intervals, so summation gives
e*TV rather than n*e*TV. Adding n pointwise Taylor errors and the scalar
logarithm error gives e*(4*10^9+2B*x). Both full exponents are <=-x;
the real exponential mean-value bound therefore retains exp(-x) for every
n>=0, without any restriction that x be small. The claimed
3B*e*(1+x)*exp(-x) bound follows for B>=10^12. This is solely a product
estimate and cannot be differentiated or promoted to a moment rate without
additional work.

## Linear complex kernel and enlarged domain

The inherited M7 sector applies on 0<e0<=10^-8,
|e-e0|<=e0^2 and s=n*e with 0<=Re(s)<=4. On this domain the complex
square root has positive real part and the critical square root is real
nonnegative. Thus the modulus of their sum is at least the modulus of
the complex root, exceeding .06*sqrt(e0^2+x). Polynomial subtraction gives
320*e0*(e0+x); division is legitimate even at x=0. The elementary inequality
(e0+x)/sqrt(e0^2+x)<=1+sqrt(x)<=3 proves the 16000*e0 root comparison.
The inherited .8 denominator margins then give the 25000*e0 kernel bound.

For the phase inverse, use exactly
Omega={theta: .78<Re(theta)<.92, |Im(theta)|<.02}
and e0=e_N(Re(theta)), as in M8_COMPLEX_DOMAIN.md. The M7 fixed-point
construction applies for N>=10^6 and provides |e|<1/N, |e-e0|<e0^2.
At N>=10^15, the resulting 16000*e0 bound on |g_e-g0| preserves the
.0009 exterior margin. The .049 root margin, crossing half-tube, eta range,
scalar damping and far-tail contraction all retain strict slack. The
crossing comparison is the already derived 2*10^12*e0 estimate, and is
linear before the older argument enlarged it to a square-root bound.

One sharper constant deserves an explicit derivation. The new note uses a
5*10^6*e0 logarithm remainder, while the old M7 text used 4*10^7*e0.
On the new domain |eta_e|<1 and |delta/e|<.301, so the two fractions have
moduli below 21 and 335 using .049 and .0009. Therefore
2*|e|*(21^2+335^2)<450664*e0<5*10^6*e0.
This verifies the new constant rather than inheriting it without proof.
The exterior g-fraction coefficient is 48002000000/9<6*10^9;
together with the 5*10^8 root coefficient and this remainder it is below
10^13. Multiplying by |e|<2e0 and fewer than 5/e0 prefix factors gives
Re(sum ell)<10^14*e0<.1, hence every needed prefix has |Pi|<2.

The bare-product assumptions are unchanged: real eta in [.70,.72], the
same phase rectangle, and epsilon*(Re(a)+1)<.2. Source-pole exclusion,
positive kernel majorant and the common 60N cutoff with ratio exp(-.07/N)
therefore still prove normal convergence, not just pointwise boundedness.
The inherited compact/tail/boundary norm ledger is
80000000+4800000+100=84800100<10^8. Thus holomorphy and this joint norm
hold on Omega for every integer N>=10^15. This is a domain improvement;
it alone supplies no useful real approximation or uniqueness threshold.

## Provenance and arithmetic

Observed source commit: 0a62a455d75d1880ab73ef7bae91cc3492d9d82e.
The exact Fraction arithmetic replay gave Vg=36225/58<625,
quotient coefficient 4183718750001/200000000<25000,
exterior g coefficient 48002000000/9<6*10^9, and log remainder 450664.
These checks support arithmetic only; the analytic arguments above carry
the proof. Source hashes at review:

| Source | SHA-256 |
|---|---|
| M9_PRODUCT_VARIATION.md | 4830bf678a5733af94a927db275dda1f9ca61ab5e52d66daac4ac13b700a1ab8 |
| M9_COMPLEX_KERNEL_LINEAR.md | df7c023bd83ceb9a766547e1bf7a88b4d8426d1a2d575eefa40d43f55bae6312 |
| M6_SHARP_KERNEL.md | 8717a3a191eb9f958f4b6a68d4066ae41bb8c13bc051985f3fe0791499158487 |
| M6_SHARP_KERNEL_REVIEW.md | 06cb7019929de6aa1739ea081ce1d314c1e50f6468c4461b9f07d2e442d1c568 |
| M6_EFFECTIVE_PRODUCT.md | a3b6b878102cfbe022aada6477c78c8641edc5d25b813ea7030f032fce96c522 |
| M6_ACCEPTANCE.md | 6ee93e1e27984dfda45d6932b943ea953e2953e7bfb10da31dcf65abdc8914a6 |
| M7_COMPLEX_KERNEL_SECTOR.md | 0c1b006aa6d202bc89345b9d0ba194ce8502c504497061007acdca548d59bfe3 |
| M7_COMPLEX_SCALARS.md | 53fa59586ba44673d5904190f4ee3fc556b826677c6053f6ddc08e5a82060c38 |
| M7_EFFECTIVE_DERIVATIVE.md | e79045816d8ec87313584ba8bc960ff09833e299071013c9cf84fae1903df7d1 |
| M7_COMPLEX_PRODUCT_DOMINATION.md | c366bb558d128ecdeb8f43de5c1c261df1d1807f3559c6a5d50a76e1b796864c |
| M8_COMPLEX_DOMAIN.md | f0805eb13495486eed4a9c8809d4bebfba2dac16e4dc65345da905a17eac6283 |

The four M6 hashes match the product note's ledger. No frozen scientific
source or producer was edited by this review.

Post-review clarification: M9_COMPLEX_KERNEL_LINEAR.md now explicitly defines
Omega and derives its logarithm allowance using the fraction bounds 21 and
335, as recommended above. Updated SHA-256:
cb383687009961812dbed481071b48ad9c86a1cfc78de424fd8a927b6219ce52.
These clarifications preserve the accepted argument and constants.
