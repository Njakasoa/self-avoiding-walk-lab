# M7 — finite W certificates and effective uniqueness

Status: COMPLETE at the internal research-draft gate; see
M7_ACCEPTANCE.md and results/m7-final-review.md. User requested continuing research after M6. The previous
goal turn completed M6 and changed authoritative state (progress). This
continuation keeps both recommended research directions in scope.

Baseline: a7fa96f, M6 accepted internally. New branch:
codex/w-finite-uniqueness. No publication or external contact is requested.

## Intended results

1. Replace numerical evidence at accessible phase indices by exact finite
   pole certificates. Start with the already observed indices32,64,128,
   256,512,1024. Every claimed pole needs an outward-rounded bracket,
   opposite denominator signs, a numerator nonzero throughout the bracket,
   rigorous full tails, and exclusion of source singularities. A tiny
   numerical residual or last summand is insufficient.
2. Make the eventual uniqueness statement quantitative: obtain an explicit
   index above which each phase band contains exactly one simple W pole.
   Derive a genuine effective phase-derivative estimate or another valid
   uniqueness argument. Do not differentiate an unspecified C0 remainder.
3. Keep scopes distinct. Finite certified brackets do not cover every
   intervening index or prove global uniqueness on an entire band. A large
   effective uniqueness threshold is not practical small-index coverage.
   Retain failures and unproved optimizations.
4. Independently review analytic lemmas and arithmetic, freeze sources
   before canonical receipts, check reproducibility and relevant regressions,
   and audit both research directions before completing this step.

No new held-out numerical index is consumed without a frozen protocol.
M6's1024 is already observed and may seed a rigorous certificate; those
seed values are hints only, never proof inputs without interval verification.
All accepted M3--M6 scientific sources and receipts stay frozen.

## Roles and review

Root owns architecture, mathematical integration, thresholds and final
scope. Actual Luna/max workers m7_finite_certificate and
m7_effective_derivative own respectively the finite-tail/checker work and
the effective derivative proof. After the finite worker completed, Astra reviewer m7_review became
available. The finite implementation and tail proof passed its independent
audit, pending complete six-index execution. Complex lemmas and the
effective derivative bridge are under review. The independent review gate
remains required for both directions.

Final gate passed for both directions. All canonical receipts and reviewed
source hashes verified. Remaining research gaps are listed in M7_ACCEPTANCE.
