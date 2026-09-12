# CLAIM-0007 — Non-D-finiteness of two-sided weakly prudent bridges

Status: **proved in the internally reviewed W draft**. Publication priority:
**UNRESOLVED**. Internal AI review is not external peer review.

Let W=I/(1-I), I=4J-2D_I-t, and J=(P-H)/(1+P) be exactly the series
defined by Bacher–Beaton (2014). Then W is not D-finite.

This requires its own argument. Define
F=(3-t-2D_I)P-4H-(1+t+2D_I), so W=-1-(1+P)/F. The partially directed
series has positive summands and local complex normal convergence below
sigma=sqrt(2)-1; its critical harmonic divergence gives D_I->1. Extending
the reviewed Gamma-product limit to phases [4/5,9/10] gives uniform limits
for P,H,F. Exact interval arithmetic certifies F_0(4/5)>0 and F_0(9/10)<0,
while 1+P_0<-2.26 uniformly. Every sufficiently late phase band therefore
contains an analytic zero of F with 1+P nonzero: a genuine pole of W.
The infinitely many disjoint bands accumulate at sigma and belong to the
continuation of the original germ, contradicting D-finiteness.

Evidence and full requirement audit: [W_ACCEPTANCE.md](../W_ACCEPTANCE.md).
Scientific source freeze: `9a63181dc11100fa4dfccdea510650976383ffb3`.
Proof: `proofs/W_NON_DFINITE.md`; independent analytic review:
`proofs/W_ASTRA_REVIEW.md`; final integration review:
`results/w-final-review.md`. Exact and exploratory receipts are
`w-identities-v1`, `w-critical-v1`, `w-phase-v1`, `w-phase-fine-v1`.

The N=8,16 endpoint failures remain in the evidence. No finite pole is
certified by the floating-point sweeps. The theorem needs neither an
effective N_0 nor simple or unique zeros; those quantitative refinements,
external review and priority determination remain open.

This adds the W-specific result absent from CLAIM-0006; it does not change
that earlier claim's historical scope or establish any exact connective
constant for unrestricted square-lattice self-avoiding walks.
