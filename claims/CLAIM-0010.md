# CLAIM-0010 — Finite W poles and effective uniqueness

Status: proved in the internally reviewed M7 draft; final closure accepted
in results/m7-final-review.md.
Mathematical priority unresolved.

For the weakly prudent bridge generating series W of CLAIM-0008, the
six rational t intervals in M7_ACCEPTANCE.md each contain at least one
noncancelled pole. Their phase indices are32,64,128,256,512,1024.
The complete series tails and a uniformly nonzero numerator are included
in the exact 384-bit outward interval certificates. This finite statement
does not establish uniqueness or simplicity on those bands.

Separately, every integer N>=10^120 has exactly one simple noncancelled
W pole in the phase band theta in[4/5,9/10], where e_N solves
s_g(e_N)/e_N=N+theta and t_N is the physical kernel parameter.

The new analytic input is a holomorphic moment bound on a fixed complex
phase neighborhood, giving a genuine second-derivative bound. Combined
with the accepted M6 real moment error, it yields

    sup_[4/5,9/10](|P_N'-P0'|+|H_N'-H0'|)<9/1000

at N>=10^120. The exact denominator derivative identity then gives
F_N'<-1 on the whole phase band. M6 supplies opposite endpoint signs
and the nonzero numerator; the nondegenerate phase-to-t map transfers
simplicity to t. No real C0 remainder is differentiated.

The threshold is explicit but is not practical finite-index coverage.
Unlisted indices below it remain outside this uniqueness theorem; M6's
separate existence-only theorem continues to apply from10^46.
No conclusion about unrestricted square-lattice SAWs or their connective
constant follows from this statement.

Evidence: proofs/M7_FINITE_TAIL.md, proofs/M7_FINITE_REVIEW.md,
proofs/M7_EFFECTIVE_DERIVATIVE.md and its auxiliary lemmas,
proofs/M7_EFFECTIVE_REVIEW.md, the two canonical M7 receipts and
proofs/check_m7.py. Final scope is recorded in M7_ACCEPTANCE.md.
