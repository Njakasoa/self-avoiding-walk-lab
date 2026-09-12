# M3 acceptance — research candidate, 2026-09-12

**M3 accepted at the requested internal research-validation level.** The
selected theorem is that the generating function J of irreducible NE-prudent
ramps is non-D-finite. The proof uses BB2014's explicit formulas and
meromorphic continuation, exact moment regularization, a uniform matched
Gamma-product limit, and certified limiting integral signs.

Publication priority remains **UNRESOLVED**. This is an internally reviewed
publication candidate, not an external peer-review or priority determination.
M4 may now be prepared under the user's explicit conditional instruction.
Nothing has been submitted or communicated to external researchers.

| Requested M3 gate | Authoritative evidence |
|---|---|
| Select substantive candidate | M3_RESEARCH_PLAN.md; references/M3_TARGET_AUDIT.md: documented BB2014 non-D-finiteness gap, chosen over known-method compression |
| Fresh independent computation | proofs/M3_PRUDENT_FORMULA_AUDIT.md; geometric counts; independently repeated integral enclosure and unsubstituted high-precision integral checks in proofs/M3_CRITICAL_QUADRATURE_AUDIT.md |
| Counterexample search | Wrong-sign coboundary/threshold ansätze retained; finite l=8,16,32 asymptotic probes and N=8,16,32 phase checks; no inference of infinity from finite checks |
| Symbolic interpretation | Two independent exact identity probes, common signed moments and exact h-zero regularization |
| Proof | proofs/M3_NON_DFINITE_CANDIDATE.md, including phase inversion, full Gamma factor, uniform crossing bound, exponential tail and uniform moment convergence |
| Certificate | results/m3-critical-integrals-v1: integer/dyadic rectangle enclosures of limiting integral signs, no floating quadrature error assumption |
| Literature audit | references/M3_NON_DFINITE_PRIORITY.md: exact-model primary-source search, no later resolution located, explicit limits and priority UNRESOLVED |
| Astra review | results/m3-non-dfinite-review.md: no remaining analytic gap; separately discharged arithmetic premise in proofs/M3_CRITICAL_QUADRATURE_AUDIT.md |
| Frozen replay | Scientific source dbf8e65; exact certificate replay and every receipt input/output hash checked; results/m3-critical-tests.json records54 passing tests and identical committed source bytes |

The proof produces at least one noncancelled pole in each of infinitely many
phase intervals. It does not give an effective first interval, uniqueness or
simplicity of the zeros, non-D-finiteness of the further weakly prudent bridge
quotient W, or an exact formula for the square-lattice connective constant.
These are outside the accepted theorem, not silently inferred consequences.

Earlier documents marked OPEN record the chronology of the discovery. Their
frozen bytes are retained. This acceptance supersedes that status through the
new complete proof and its independent reviews; the prior finite-only
certificates are not retrospectively relabeled as infinite-index proofs.
