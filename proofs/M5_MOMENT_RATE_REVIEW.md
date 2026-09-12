# Adversarial review of the M5 moment-rate candidate

Status: **ACCEPTED at the internal mathematical-draft gate for the
non-effective moment and phase-derivative rate**, not acceptance of
an explicit N0. This is internal AI mathematical review. The older frozen
J/W proofs are unchanged.

## Findings

No conceptual obstruction was found in the proposed complex-phase route.
Unlike the old qualitative proof, the new text supplies a quantitative
endpoint modulus, tracks the growing cutoff, and obtains phase derivatives
by Cauchy's estimate after proving holomorphic uniform convergence.

1. The expansion t=sigma-e²/16+O(e⁴) follows from the kernel relation:
   its t derivative at sigma is -4 and q+1/q=2+e²/4+O(e⁴). With
   e=h+O(h²), Im e=O(h²), the nearby v branch point has positive real
   displacement of order h² and imaginary displacement O(h³). It stays
   outside the unit disk uniformly on the fixed phase neighborhood.
   Along the initial narrow ray the discriminant is comparable to
   |s|+h². This is sufficient for the stated O(h) kernel perturbation;
   no bounded s derivative at zero is needed.
2. The distant ray creates no extra endpoint singularity: large Re s makes
   |v| small, and the kernel is analytic near v=0. For intermediate s,
   compactness gives uniform bounds. Rational denominators other than g,h
   can be controlled on those same three regions. The inverse-kernel
   equations classify g,h zeros. Nonzero logarithm branches require an
   imaginary part of order |m|/h, incompatible with bounded Im a,Im b;
   the zero branch is excluded by phase separation. This rules out source
   poles for every n, not only indices below the cutoff.
3. The smooth-product estimate (2) has a credible uniform global constant:
   analytic divided differences treat a fixed disk at s*, bounded
   denominators and the O(h) endpoint perturbation treat the initial
   compact remainder, and g_e->t²q handles the remaining half-ray.
   Consequently its accumulated error is O(S h), and the global
   1/2-Hölder modulus gives O(S sqrt(h)) quadrature. No exponentially
   growing cutoff constant is hidden in this estimate.
4. The positive-real-part Gamma formulas retain the fixed split n<=N and
   n>=N+1 for complex theta. Uniform sectorial Gamma-ratio errors give
   O(h/rho); eta_e-eta produces logarithmic errors. The mesh displacement
   O(h x_n) contributes O(h/rho) near the crossing and O(h S) away from
   it. The displayed relative error (4) accounts for these contributions.
5. Complex Gamma domination is obtained by bounded complex shifts in the
   positive-argument formulas, not by applying the real inequality without
   modification. The small arguments stay a positive distance from Gamma
   poles and the sine denominator stays nonzero. The resulting crossing
   mass bound has exponent 1-eta-1/20>0, with a constant from a fixed
   neighborhood; it does not grow with S. No positivity is needed.
6. The weight comparison survives the moving mesh at s=0: a displacement
   O(h x) times a derivative O(x^(-1/2)) is O(h sqrt(x)); the n=0
   displacement vanishes. Combining this with the O(h) parameter
   perturbation yields the claimed O(h(1+S)) bound. Off the crossing,
   the weighted profile's derivative bound of order rho^(-1-eta) and
   its endpoint Hölder bound suffice for the stated quadrature error.
   Boundary cells of an excluded crossing window can be absorbed by an
   O(h) enlargement of that window.
7. The cutoff arithmetic is correct. The quadrature term gives
   h^((1-eta)/4) log(1/h), and the crossing term gives
   h^((1-eta-1/20)/4). Their exponents are strictly larger than 1/20
   because eta<3/4; logarithms are absorbed by the strict margin.
   The other terms decay faster. A fixed complex neighborhood, not one
   shrinking with N, is used throughout. Cauchy's estimate then gives
   the stated derivative rate and each fixed higher derivative rate.

## Requested repairs, now verified

- Section 4 starts the tail from equation (5) at S0. Equation (5) is only
  stated in a fixed crossing neighborhood, whereas S0 is large. Use (4)
  at the first index beyond fixed S0, or state a fixed-compact bound there.
- The moment sum uses the real mesh h. State explicitly
  Q/h=(Q/e)(e/h)=K+O(h), since the old regularized formula uses Q/e.
- Justify the critical-profile version of the tail bound by its limiting
  logarithmic derivative, -lambda-kappa/sigma²=-2/(1-sigma)<-1.

All three changes are now present in Section 4 and have been independently
checked. The tail starts from (4) at the first index beyond fixed S0, the
critical decay follows from the stated negative limiting logarithmic
derivative, and the prefactor is explicitly converted to Q/h. These close
the identified local connections. No remaining substantive blocker was
found for the non-effective O(N^(-1/20)) uniform moment rate and its fixed
theta derivatives. No finite numerical agreement substitutes for these
analytic steps.

## Scope

Even an accepted non-effective rate would not give an explicit N0. It also
does not alone establish W simplicity or residue asymptotics: the directed
term and the subsequent denominator/root argument remain separate inputs.
The review performed no heavy computation and supplies no numerical
certificate.

## Reviewed provenance

Observed HEAD: `2893bbe27f2e65449bfc345c9f7a874faa185129`.
Accepted revised `proofs/M5_MOMENT_RATE.md` SHA-256:
`9d8bdc4d72b8decbf696778ed061c635f8a216ed4440eb73a89c3de56d8fa811`.
Earlier reviewed version before the three local repairs:
`f6c91d14d67a860bba0f4d347b15403a09dc823cc19c18d520d22f781e459fa8`.
This acceptance relies on the exact factorization and regularized moments
in the frozen J/W foundation identified by the candidate. Subsequent
mathematical changes require reviewing the changed text; merely updating
a hash is not a new acceptance.
