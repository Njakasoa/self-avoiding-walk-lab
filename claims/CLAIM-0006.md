# CLAIM-0006 — Non-D-finiteness of irreducible NE-prudent ramps

Status: **proved in the internally reviewed M3 candidate**. Publication
priority: **UNRESOLVED**. This supersedes the infinite noncancellation
obligation in CLAIM-0005, without changing its historical finite certificates.

Let P,H be the NE-prudent-ramp and hook-ramp generating functions defined by
Bacher–Beaton (2014). Then J=(P-H)/(1+P) is not D-finite.

The proof uses the published exact formulas and meromorphic continuation.
After exact moment regularization, a Gamma-product factorization gives a
phase-uniform critical limit. Its crossing singularity has exponent
1/sqrt(2)<1 and its far tail is exponentially bounded. Exact interval
arithmetic certifies opposite signs of 1+P_0 at phases 0.30 and 0.35 and a
strictly positive value of 1+H_0 throughout the interval. Uniform convergence
then gives infinitely many noncancelled zeros of 1+P and hence poles of J.
A D-finite analytic germ has only finitely many possible finite singularities.

Evidence: proofs/M3_NON_DFINITE_CANDIDATE.md; independent analytic review in
results/m3-non-dfinite-review.md; independent arithmetic audit in
proofs/M3_CRITICAL_QUADRATURE_AUDIT.md; four source-frozen critical receipts at
dbf8e65; primary-source priority audit references/M3_NON_DFINITE_PRIORITY.md.
M3_ACCEPTANCE.md maps every requested gate to its evidence.

No claim is made about non-D-finiteness of the further bridge quotient W,
an effective first phase index, uniqueness or simplicity of the constructed
zeros, or any exact square-lattice connective constant. Review is internal and
AI-assisted; external peer review and priority determination remain open.
