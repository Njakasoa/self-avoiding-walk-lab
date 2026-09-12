# M7 — finite W certificates and effective uniqueness

Status: **ACCEPTED at the internal research-draft gate**, following
results/m7-final-review.md. Work is local on
codex/w-finite-uniqueness. Internal AI review is not external peer review;
mathematical priority remains unresolved.

## Results and distinct scopes

The exact finite producer certifies at least one noncancelled W pole in
each of six rational t intervals, at the already observed phase indices
32,64,128,256,512,1024. For each interval it encloses the two endpoint
denominator values with opposite signs, keeps 1+P strictly negative on
the whole interval, excludes source singularities, and includes rigorous
complete prudent and directed tails. The arithmetic uses integers and
rationals with outward rounding at 384 bits. Diagnostic decimals supply
centers only; no numerical residual is treated as a certificate.

| N | t center | Half-width |
|---|---|---|
|32|.41421207394799683735264571222663623|10^-20|
|64|.414213185158662864277074445373505154|10^-21|
|128|.414213467408871231663879913007615537|10^-22|
|256|.414213538547559642617307852519257466|10^-23|
|512|.414213556405979324775984842665373891|10^-23|
|1024|.414213560879958311290325902232183328|10^-24|

These six finite certificates prove existence and noncancellation. They
do not establish simplicity, uniqueness on their full bands, or coverage
of unlisted indices.

The analytic result supplies a different statement: every integer
N>=10^120 has exactly one simple noncancelled W pole in its phase sector
theta in[.8,.9]. This makes the inherited eventual uniqueness theorem
effective. It does not lower M6's existence-only threshold10^46, and
neither threshold is computationally useful for exhaustive coverage.

## New analytic input

The phase inverse extends to a fixed complex neighborhood. Explicit
square-root sector bounds and a positive-coefficient majorant control
the physical kernel. An elementary finite-product estimate controls the
bare product without a complex Gamma asymptotic remainder. For the
smooth product, each complex logarithm is compared with e*psi(Re(ne));
the real sign psi<=0 gives the compact product modulus below2. The full
recurrence gives the geometric far tail. These estimates yield

    sup_Omega(|P_N|+|H_N|)<10^10, N>=10^120.

Cauchy's formula bounds the sum of second derivatives of the moment
errors by10^16. The accepted M6 real error is below2*10^-21 at this
threshold. An inward finite difference with h=10^-18 therefore gives

    sup_[.8,.9](|P_N'-P0'|+|H_N'-H0'|)<.009.

This controls derivatives without differentiating a real C0 remainder.
The exact denominator derivative identity, the certified critical margin
F0'<-6 and M6 directed bounds force F_N'<-1. Opposite endpoint signs
and a uniformly nonzero numerator finish uniqueness and simplicity.

Proofs are in M7_EFFECTIVE_DERIVATIVE and its five auxiliary notes;
M7_EFFECTIVE_REVIEW is the independent analytic gate. The conditional
wording in frozen auxiliary lemmas records their individual hypotheses;
the bridge supplies the required moment bound when accepted together.

## Reproduction and review evidence

Finite sources were frozen at fc445b3 before the canonical run; the
effective proof and arithmetic were frozen at81dcaba.
Canonical receipts are results/m7-finite-v1 and results/m7-effective-v1;
their metadata records source commits, hashes, parameters and runtime.
The exploratory full-six output is retained separately and equals
the canonical payload exactly. Independent reviewer N32 output equals
the corresponding canonical row. The canonical six-row run took252.844s;
the effective arithmetic took.067s. An original-versus-regularized
exact moment calculation at the same N32 seed has overlapping full
enclosures; that is a consistency check, not a second pole theorem.

The reviewer ran500 independent rational interval oracle cases, six
invalid-input checks and three elementary logarithm bounds. The57-test
regression suite passed in11.15s. Exact auxiliary arithmetic ran identically
with and without Python optimization; inherited assertion-based engines
are guarded against optimized execution. The integration verifier checks
receipt provenance, exact signs and tails, reviewed source hashes,
independent evidence and unchanged original M3/W/J sources.

The integration audit passed in results/m7-final-verification.json.
The inherited M6 audit was also replayed byte-for-byte unchanged.

Relevant commands, from the repository root:

    .venv/bin/python -m experiments.m7_finite_batch NEW_EXPERIMENT_ID
    .venv/bin/python -m experiments.m7_effective_batch NEW_EXPERIMENT_ID
    .venv/bin/python -m proofs.check_m7
    .venv/bin/python -m proofs.check_m7 --replay
    .venv/bin/python -m pytest -q

## Remaining research

1. Certify derivative signs over complete accessible phase bands to
   establish finite uniqueness and simplicity, including the six bands.
2. Reduce the explicit uniqueness threshold and cover intermediate
   indices with analytic bounds plus finite interval certificates.
3. Sharpen the algebraic error in the resummed phase approximation and
   investigate effective residue bounds.

No new held-out index was measured, no failed M6 prediction was removed,
and no publication or external contact took place. All results concern
the restricted weakly prudent bridge series W; they do not determine the
connective constant of unrestricted square-lattice self-avoiding walks.
