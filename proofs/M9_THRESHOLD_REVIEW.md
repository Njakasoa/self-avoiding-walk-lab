# Independent review of the M9 uniqueness threshold

Verdict: the N>=10^27 threshold follows from the reviewed M9 linear moment
rate and complex domain, with the inherited critical and directed estimates.
Every integer N in that range has exactly one simple noncancelled W pole
in theta in [.8,.9]. This excludes neither other poles outside the sector
nor missing indices below the threshold. It is not a claim of novelty.

## Derivative interpolation

For N>=10^27, e_N<1/N gives joint real error E=10^-6 on the whole sector.
The M9 complex domain is available already for N>=10^15, on precisely the
rectangle needed for the M8 Chebyshev argument. Its moment norm 10^8 plus
the inherited critical norm 100 yields M=10^8+100. The ellipse q=15/22
lies strictly inside that rectangle, and the joint coefficient/Markov
estimate applies because the moments are real on the real sector.

I independently recomputed the full rational expression with degree m=97
and k=98 using Fraction arithmetic. It is strictly below 201/1000;
its decimal value, solely for readability, is approximately
0.20041766721198112. No numerical derivative or derivative of a real
remainder is used. The coefficient tails converge absolutely with their
first derivatives, as required in the inherited interpolation proof.

## Directed term and new existence proof

The directed constant/remainder theorem applies on 0<e<=.01, well beyond
the new domain. With L=log(1/e), its |R|<=100eL bound is at most
2700 log(10)/10^27<8100/10^27<3/4. Thus c_D>3/4 implies
D>L/sigma. The displayed wording bounds eL even more loosely by the same
number; the required remainder inequality is valid with the factor 100.
Monotonicity of e*log(1/e) on (0,exp(-1)) justifies the uniform maximum.
The elementary exponential bounds give log(10)>2 and log(10)<3, whence
0<delta<.42/54<1/125.

The value error and frozen critical numerator bounds imply
-8<1+P_N<-3.5 everywhere in the sector. Subtracting the exact denominators
gives the claimed 4E+2e^2+16delta bound: moment errors cost at most 4E,
parameter motion costs less than 2e^2, and the directed correction uses
|1+P_N|<8. This is below .15. Consequently F_N(.8)>.85 and F_N(.9)<-.05.
This argument proves existence anew at N>=10^27; it does not invoke the
old N>=10^46 existence theorem outside its domain.

The M5 directed phase derivative estimate |delta'|<=30000/N applies
already for N>=20, as follows from the displayed derivative chain and
positive directed sum. The real phase/root bounds, eta_e in [.70,.72],
source-pole exclusion and physical local holomorphy all apply on the
new, smaller e-domain. No threshold-specific old conclusion is needed.

## Strict monotonicity and simplicity

Using the exact differentiated denominator identity, the coefficient of
the P error is below 1 and that of the H error has modulus 4. The remaining
terms are bounded by 150delta+18e^2+480000/N, using the independently
established numerator bound and the inherited parameter derivatives.
The resulting bound is
-6+4*.201+150/125+18*10^-54+480000*10^-27<-3.9.
The phase derivative is therefore strictly negative on the whole band,
so the existing zero is unique and simple. The positive nonzero
phase-to-t derivative transfers simplicity to t, and the negative
numerator guarantees noncancellation in W.

## Finite checker audit

The independent finite review is recorded in M8_FINITE_REVIEW.md. The
canonical six-row payload has been retained and its N32 row agrees exactly
with the independent replay. The checker verifies metadata provenance,
exact six-index scope, inherited endpoint/source signs, recomputed residue
boxes, strict derivative and residue signs, and directed/prudent tail
bounds against 10^-18. Its first run required the expected source snapshot
refresh for documentation and a new regression test; final_review_snapshot
now preserves that update without rewriting earlier evidence.
This checker validates a retained certificate; it is not an independent
execution of all six rows.

## Provenance

Observed source commit: 0a62a455d75d1880ab73ef7bae91cc3492d9d82e.
Reviewed threshold SHA-256:
099a6838b1afdd73806a25b6d278ba5febc17e418b8f0d8014d5c93bf42fb98d.
The M5 directed derivative source SHA-256 is
08668a0ddbba107c2f56cc88e0d5f1b549c9ddec92490f4d35ba5f4e4005e38a;
M6_DIRECTED_CONSTANT.md is
b45599ada46df5d992f81b142b5285ce062f02d04ae02234e76a21afab4caab3.
The new M9 input hashes and reviews are in M9_MOMENT_REVIEW.md and
M9_KERNEL_REVIEW.md. No scientific proof file was modified by this review.

The updated finite checker was executed independently with
`.venv/bin/python -m proofs.check_m8_finite` and passed for all six rows.
