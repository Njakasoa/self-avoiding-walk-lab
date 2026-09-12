# Independent Astra review of the M3 checkpoint

Review date: 2026-09-12. Base commit inspected:
`4a324867c950e8cd27470277cfe36dcfe238916b`. Sources were still being prepared;
this review is not a substitute for the root's source-frozen reproduction receipt.
Reviewer owned only this file and made no core edits.

Verdict: the five finite singularity existence checks are mathematically sound
conditional on BB2014 Propositions 14/16 and Theorem 17. No arithmetic or
transcription defect was found in the interval checker. The all-index
non-D-finiteness target remains OPEN, novelty remains unestablished, and M4
must remain withheld.

## Checked finite argument

Read NORMALIZATION.md, NEXT.md, M3_RESEARCH_PLAN.md, the candidate, formula
audit, claim, archived source propositions/theorem, and both prudent scripts.
The rationalized kernel uses exactly the source's small power-series branch.
All factors and signs of A, B, and the hook summand match the archived formulas.
The geometric enumerator uses forward-ray prudence and positive height;
its north/east boundary and final northeast corner tests match this convention.

For interval arithmetic, multiplication takes all endpoint products and rounds
outward. Reciprocal is decreasing on either nonzero sign interval: dividing
SCALE squared by the upper endpoint with floor and by the lower endpoint with
ceiling is correct even for negative denominators. Square roots use exact
integer floor roots and an upper correction. Dependency overestimation affects
width but never invalidates inclusion. Domain errors fail closed.

At truncation N, the actual q is in (0,1), so every future q^(2k) is in the
computed interval [0,upper(v_N)]. Uniform interval substitution bounds all
future A, hook A, and B on the entire t bracket. The product enclosure and
beta<1 therefore give the stated geometric majorants. This also supplies
uniform convergence and continuity on that real bracket; every finite and tail
denominator is excluded from zero. Endpoint opposite signs imply a zero of
1+P. Uniform H+1>0 excludes cancellation. The known meromorphic continuation
and non-identical denominator then make each zero a genuine finite-order pole
of J. No derivative or uniqueness test is required for this existence claim.
Disjoint brackets give at least five distinct poles, not exactly five globally.

Independent standalone execution of `python3 proofs/m3_prudent_intervals.py`
completed with every assertion passing. Output SHA-256:
`c42667a1a178b69e36ee113b7a4794bb287333f749e577cb624749444beb42ca`.
Reviewed interval source SHA-256:
`a2230bdeedbefcd5550cc64f304dcdd4b887a5c60f77e4f7cac974ad71451ff1`.
Reviewed geometric reference SHA-256:
`2fbd8c664395d45a0e53cda74b840d2d2abda26e7ce4b57bda6d479fb03bd500`.
Reviewed numerical probe SHA-256:
`71722e6841ad87127847adcfdc1bca8ab815ea7b706db8734ea1c356bd30c072`.

## Finding requiring scope correction

The initial formula-audit residue paragraph omitted the sign of the prefix
product of B_j for j<l when concluding that the full P residue is negative.
A positive numerator of the tail starting at l is not enough by itself.
Further, a simple pole of the final function does not by itself establish a
simple zero of the displayed denominator without the necessary nonvanishing
local numerator and factorization justification. These are gaps in that
proposed all-index reasoning, not in the finite interval certificate. The root
was notified to remove the conclusion or make these obligations explicit.
The numerical residue values can safely remain labeled numerical evidence.

## Supporting scope

The span-two ladder note gives a coherent geometric run decomposition and
weighted rational series, with exact finite coefficient comparisons reported
separately from the proof. No novelty claim is made. The H/V partition note's
exceptional set {1/2,1,2} follows from the bounded integer signature differences;
induction through refinement correctly establishes the generic partition.
These observations do not constitute a new connective-constant result.
The claim and target audit properly distinguish absence of a later paper found
in a bounded search from proof of priority. I did not repeat the web audit.
The automaton/deadline worker had not released its final files at this pass;
those files are outside this verdict.

## Follow-up on the residue argument

The root supplied a valid repair for the omitted prefix sign. At a fixed pole
with C=q-t, D=1-tq and u_l=tq/C, one has
G_(l-1)=t-D*u_l=-t²(1-q²)/C<0. Since u_(j+1)>=u_l for j<l,
all earlier G_j are negative, as are h_j, making every earlier B_j positive.
The empty prefix at l=0 equals one.

The remaining local analyticity can be proved without uniformity in l:
U(t,0)=t, h(t,0)=t², and B(t,0)=q²C²/D²<1 because qC<D is equivalent
to q²<1. For each fixed real pole below sigma, analyticity and continuity give
a complex t neighborhood and a small complex v disc on which denominators
remain nonzero, the summands are bounded and |B|<beta<1. Shrink the neighborhood
to keep |q|<r<1. All sufficiently late q^(2j) then lie in that v disc
uniformly. The finitely many earlier tail denominators remain nonzero after
another shrink. The tail is therefore locally holomorphic by a geometric
majorant. A strictly positive extracted singular numerator and positive prefix
then make the pole order equal to the zero order of h_l; the source's simple
pole theorem forces this order to be one. With the endpoint orientation,
negative residue follows. This repairs the identified gaps if integrated
explicitly into the final proof note. It still gives no all-index
noncancellation statement for J.

Focused verification: `.venv/bin/python -m pytest tests/test_m3_intervals.py -q`
passed all 3 tests in 1.92 seconds. The system interpreter lacked pytest;
the repository virtual environment supplied it.

## Final bounded follow-up: interlacing and deadline scout

The integrated `proofs/M3_PRUDENT_INTERLACING.md` closes the residue gaps
identified above. In particular, both comparison arguments of phi are in
(0,1); t/D<1 follows from t(1+q)<2*sigma<1. The local complex tail argument
is sufficient at each fixed pole. The archived source explicitly identifies
the real poles between rho and sigma as the listed family, supplying the
continuity intervals used. Thus the deduction of negative residues and an
infinite family of zeros of 1+P passes this review conditional on the cited
source formulas/theorem. This is a real partial result; it does not prove
infinite noncancellation in J. The main M3 target is still OPEN and M4 withheld.
Reviewed interlacing note SHA-256:
`eba193f2a44f0b3f3efd45ca151d5fb152c158fd840d3f29a3cd4ccb2caa6366`.

Reviewed `experiments/m3_deadline_probe.py` and
`proofs/M3_AUTOMATON_SCOUT.md`. The deadline test is mathematically sufficient:
an omitted vertex cannot become reachable before its remaining checking time
expires. Checking the attempted move before decrementing deadlines has the
correct raw-queue convention. Singleton startup reaches exactly the full raw
suffix image at depth m, and that layer is closed. Only states outside that
layer must be transient; earlier startup states can coincide with layer states.
The detailed proof states this distinction correctly. D4 symmetry preserves
deadlines and isotropic multiplicities, so the integer quotient matrix and
positive-vector upper bound are valid. Exporting states, rows and the vector
makes the rational inequality independently replayable, unlike a hash alone.
The exact geometry-only counterexample and static-pocket obstruction are
consistent with the finite-memory convention. No new priority claim is justified.

Executed the direct probe for every memory 1 through 7 with full raw comparison.
All seven cases were certified and all raw image/row comparisons passed.
Independently re-read the JSON and checked each exported row inequality by
integer cross-multiplication against the exported rational bound; all passed.
No larger case was rerun in this bounded follow-up.
Reviewed deadline source SHA-256:
`0da719a55dc8891f23691f7644a7a618d9d16a91a3ae1ee4a263d1609f22e526`.
Reviewed scout note SHA-256:
`1193a10b2cbc4ec96b2f11bd0a865ef32a3ca232abc5e88ac8917351d5e99d8d`.
Follow-up output SHA-256 (includes runtime fields):
`72ea80c2fc2aa252739b470a28d6c66247bc44dea602dadd4055f2ac2db04667`.

The root was notified to label the scout's pre-export digest/source-hash block
as historical or replace it with the frozen receipt, and to align its shorter
startup-transient wording with the precise paragraph. These are provenance
and wording cleanups; no further mathematical defect was found. Root's final
source-frozen receipts remain the canonical reproduction evidence.

## Frozen receipt audit and finite-checkpoint acceptance

Final bounded audit used source commit
`9c6dd75fdfe19e61337439bf6079ae2cda7a1c23` (also current HEAD).
All four canonical receipt manifests resolve to this commit. Independently
checked every listed input against both current bytes and `git show` bytes,
and every payload against its output hash: deadline 4 inputs, prudent 6,
span 6, weights 5, each with one hashed output. All matched.
The 39 source hashes in `results/m3-tests.json` also match both current and
frozen bytes. That record reports 52 tests passed; I did not repeat the suite.
Its SHA-256 is
`ec8adfc007663d222356c87ceeef19ca38e764dbb69df73a9664081b78e21b47`.

Inspected and executed `proofs/check_m3.py`: PASS, 13 deadline cases,
31 ladder coefficients, 3 weighted witnesses, 5 prudent singularities.
Checker SHA-256:
`fecc450372744eb07ef117a9c044bda0b716f73c27663163f02763117a38ad13`.
The checker independently reconstructs the deadline state layers/transitions
and verifies the exported positive-vector inequalities. It independently
expands the ladder rational formula and checks univariate/bivariate rows.
Its weight checks validate witness geometry and outgoing counts, not a fresh
reconstruction of all equitable partitions or isotropic class membership.
Its prudent check deliberately replays the separately reviewed interval engine;
the listed geometric counts are compared with expected values rather than
independently re-enumerated inside this checker. These limitations are
consistent with using the checker alongside the earlier producer, geometric,
and mathematical reviews, not treating it as independent proof of every claim.

The updated scout prose SHA-256 is
`a35a200b89ffb7cce6f88f4323598cf2ef7a1dd0f60464b1feafa2f258265be6`;
this supersedes the pre-cleanup scout hash above. No remaining material defect
was found. **The finite computational checkpoint is accepted within its stated
scope.** The all-index interlacing deduction remains a conditional partial
mathematical result. The selected M3 non-D-finiteness theorem remains OPEN,
priority remains unresolved, and M4 remains withheld.
