# Achever la théorie de W — authoritative progress

Overall goal: **ACTIVE / NOT COMPLETE**. The coverage gap between the
accessible indices and the asymptotic theorem remains unresolved.
This file records advances toward the full obligations in W_THEORY_PLAN.

## Internally reviewed analytic advances in M8

Sources frozen at5087988. The canonical receipt is
results/m8-analytic-v1; proofs/check_m8_analytic.py replays the arithmetic,
source provenance and nine independently reviewed scientific hashes.
The independent mathematical audit is proofs/M8_ANALYTIC_REVIEW.md.

1. The sufficient uniqueness/simplicity index is reduced from10^120 to
   **10^57** for the same real W phase sector[.8,.9]. A quantitative
   complex-domain audit and Chebyshev-Markov interpolation replace the
   less efficient finite-difference derivative estimate. This threshold
   remains computationally inaccessible; this is not continuous coverage.
2. The resummed phase approximation now has the explicit bound

       abs(theta_N-theta_hat_N)
       <=(5/27)[4E(N)+2/N²+285/(N logN)],
       E(N)=10^9 N^-1/4+10^21 N^-1/2+10^14/N,

   for every selected band root at N>=10^46. Its error is O(N^-1/4).
   The corresponding full-kernel spatial error is O(N^-13/4).
   At N>=10^57 these errors are below4.19*10^-6 in phase and
   6*10^-7/N³ in t.
3. The normalized residue has a resummed approximation which is a
   reciprocal quadratic in delta_hat=sigma/(logN+b). This supplies an
   explicit recurrence for every fixed logarithmic coefficient. Its
   algebraic residual is O(N^-1/4 log²N), with a finite bound in
   M8_RESUMMED_RESIDUE. The first new coefficient is strictly negative:

       N³ Res W=r0+r1/logN+O(log^-2N),
       r1 in[-.000754845272,-.000431005922].

   Uniform coarse bounds are also proved for N>=10^57:

       -1/(20N³)<Res W<-1/(6000N³).

4. An exact discrete primitive of the bare product is proved and checked.
   It may help improve the real moment error near the crossing; the
   sharper error estimate itself is still unproved. No new moment rate
   is claimed from that identity alone.

## Certified finite derivatives and residues

M7 certified existence and noncancellation in six narrow t brackets at
N=32,64,128,256,512,1024. M8 now certifies negative F_t' on each complete
bracket using outward interval jets and both infinite derivative tails.
There is exactly one simple, noncancelled W pole in each bracket, with
a rigorous negative residue interval. The full six-row canonical receipt
results/m8-finite-v1 was produced from source0a62a45 in279.20seconds.
Independent N32 replay is identical. proofs/M8_FINITE_REVIEW.md accepts
the common analytic mechanism; proofs/check_m8_finite.py checks all six
receipts, identical M7 domains and residue division. The62-test suite
passes. Initial serialization failure and earlier review snapshots are
preserved; no unretained exploratory output is treated as a certificate.

These certificates show uniqueness only inside those narrow brackets.
They do not rule out additional poles elsewhere in the full bands or
cover unlisted indices.

## M9 analytic improvement

Independent analytic review accepts the following new arguments. Sources
are frozen at196c66c; results/m9-linear-v1 records the canonical arithmetic,
and proofs/check_m9.py replays it and checks the seven reviewed source
hashes. All82 arithmetic checks pass identically with and without Python
optimization. The full-goal completion audit remains open.

- The critical smooth factor has total variation below4*10^9. Its damped
  product error is bounded by3*10^12 e(1+x)exp(-x).
- The exact discrete primitive, integrated against the positive measure
  -d(KV), controls the crossing without discarding its nearest cells.
  The resulting full moment error is below10^21 e<=10^21/N, uniformly
  on the real phase band for e<=10^-10.
- A sharper square-root comparison extends the complex joint moment
  norm below10^8 to N>=10^15. Chebyshev degree97 then gives joint phase
  derivative error below.201 for every N>=10^27.
- New endpoint and noncancellation estimates at that threshold, together
  with F_N'<-3.9, give one simple noncancelled W pole in every band for
  N>=10^27. The old M6 theorem's10^46 threshold is not imported here.
- The resummed phase error is O(1/N), the full-kernel position error is
  O(1/N^4), and the normalized residue error is O(log²N/N). Explicit
  bounds are in proofs/M9_PHASE_RESIDUE_RATE.md. The derivative-rate
  proof uses degreeceil(4logN), so the Chebyshev tail also decays at
  least as fast as1/N. All fixed logarithmic residue coefficients remain
  those of the accepted M8 rational formula.

The threshold is30 decimal orders smaller than the M8 sufficient index,
but still inaccessible to enumeration. No integer-index coverage below
10^27 is inferred from these improvements.

## M10: full N=32 band and uniform structural lemmas

The canonical full-band producer now completed all128 adjacent rational
cells at N=32, theta in[.8,.9]. Sources were frozen at12eeca1; the run
in results/m10-full-band-v1 took504.536seconds. Each whole-cell derivative
is negative with complete prudent and directed derivative tails; its phase
coordinates exclude source poles. The frozen M7 zero belongs to this band,
so these certificates establish exactly one simple noncancelled W pole
in the full N=32 band. This does not extend full-band uniqueness to N=64
or any other unlisted index. Initial coarse-subdivision failures remain
in results/m9-coverage-diagnostics alongside the successful exploratory
128-cell scan; exploratory output is not the canonical certificate.

The structural receipt results/m10-structural-v1, frozen atce376e8,
contains independently reviewed all-N>=32 lemmas:

- A signed real third-derivative certificate gives .70<beta<.72,
  beta_theta<0 and |beta_theta|<.008/N^3.
- A positive polynomial formula for the directed denominators proves
  D_R increases with t. One exact rational basepoint then gives
  delta_D<.07 for every N>=32.
- The combined weight L_W exceeds .07V1 and its fixed-parameter
  logarithmic u derivative lies between0 and16.
- A signed harmonic comparison proves the bare product T_n decreases
  with phase through n<=60N, with logarithmic derivative below
  -1435/342 for N+1<=n<=60N.

These are component lemmas, not a full F_N derivative sign. Integration
passes in proofs/check_m10.py and results/m10-verification.json. The
independent results/m10-closure-review.md accepts this scoped checkpoint;
the62-test suite passes in10.99seconds. All128 diagnostic derivatives
and the complete independently replayed first cell match exactly. The original
first-cell review retained a pre-freeze proof-text hash; the verifier
caught the mismatch. A fresh independent first-cell replay in
results/m10-full-band-review-first-cell-final.json reproduces the same
exact result and pins the final proof. Both historical review snapshots
are retained, with final mathematical approval in
proofs/M10_FULL_BAND_FINAL_REVIEW.md.

## M11: uniform post-crossing phase decrease

Two new analytic components have passed independent review:

- The directed derivative bound improves to |D_R,e|<8/e for
  0<e<=1/180, using the favorable derivative of the summand denominator.
  Consequently |delta_D,theta|<49/(1250N), and this parameter's
  contribution to the logarithmic weight derivative is below28/(25N).
- For every n>=0, the complete regularized prefactor and weight satisfy
  partial_theta log[A0 L_W(u_n)]<11/N, where A0=Q(-z0).
  The proof includes the kernel endpoint n=0 through its positive e gap.
  With the bare product this gives a margin below-3.85 after crossing,
  before the smooth product is included.

The inverse-kernel factorization has now passed independent review. It
expresses each nonsingular factor through rational positive factors and
exponential secants. A variance bound for the secants and an e-scaled
kernel-motion bound control the endpoint. The signed scalar boxes and
29 exact arithmetic checks pass. The smooth-product logarithmic phase
error is below112.2/N for n<=60N. Including the prefactor, regularized
weight and bare product gives

    partial_theta log[A0 T_n K_n L_W(u_n)]
       < -1183/3420 < -.345,
    N>=32, theta in[.8,.9], N+1<=n<=60N.

Sources are frozen ated131f9; results/m11-phase-v1 and check_m11.py
pass. The exploratory M11_SMOOTH_PHASE_RESEARCH note's missing estimate
is superseded by this proof. Final independent closure is recorded in
results/m11-m12-closure-review.md.

A worker restored a proof snapshot lacking an explicit addition operator
after freezing. The receipt checker rejected it. The correct canonical
text was restored and approved with its final hash15e8c64e; neither
scientific code nor payload changed. The earlier snapshot is retained
in results/m11-review-history, and the review addendum records the fix.

## M12: uniform noncancellation

Positive averaging of V2/V1 gives P=B1-S, H=t^2(B2-Rbar S), and

    F=-ell(1+P)-4Z, .07<ell<.6, Z>.3.

The scalar inequalities are certified on the complete real N>=32 sector.
Therefore every zero of F there satisfies **1+P<-2** and cannot cancel
in W. This does not supply zeros, their number or their multiplicity.
Sources are frozen ata7c6fb5; results/m12-noncancellation-v1 and
check_m12.py pass. The independent M11/M12 closure validates all40
declared inputs and reproduces both root checker outputs exactly.
Optimized proof entrypoints reject execution.

## Historical target before M13

Write F=B+S_pre+S_mid+S_tail, with indices0..N, N+1..60N, and n>60N.
M11 gives S_mid,theta<-(1183/3420)S_mid. A sufficient remaining target is

    B_theta+S_pre,theta+S_tail,theta < (1183/3420)S_mid.

At the M11/M12 checkpoint this remained unproved. Stronger x-dependent post-crossing bounds before
worst-case simplification, or favorable pre-crossing signs, may help.
A one-point diagnostic near N32, theta=.85 gives derivatives+.0003819
(boundary), -.0738929 (pre), -6.4196305 (middle), and -5.75e-15
(truncated rest). The component sum matches the direct formula. This
fixed-truncation probe is NONCERTIFIED and proves no uniform sign or tail
bound. Its script/output are experiments/m11_decomposition_probe.py and
results/m11-decomposition-diagnostic.json.

Uniform endpoint signs supplying existence in every band are a separate
obligation. Neither M11 nor M12 closes the integer-index gap.

## M13: full uniform phase derivative

The component and combined analytic proofs have passed independent review.
The new theorem in proofs/M13_UNIFORM_PHASE_DERIVATIVE.md establishes

    F_N,theta < -3141/64000 < -1/25,
    every integer N>=32, theta in[4/5,9/10].

The proof combines B_theta<6/(5N^2), S_pre,theta<(2.06/N)S_pre,
S_pre<2 for32<=N<=64 and<3.1 otherwise, S_mid,theta<-9/50,
and abs(S_tail,theta)<1/1000. A polynomial times geometric bound
justifies differentiation of the infinite tail. All integer indices are
covered by the exact32..64 and65..infinity split; no interpolation of
finite measurements enters the proof.

Every band has at most one zero; any zero is simple and M12 prevents
cancellation. All six M7/M8 finite poles are therefore unique on their
entire phase bands, preserving the existing residue enclosures. M9 still
provides all-index existence only from10^27. Other intermediate-index
existence remains open. Sources are frozen atf68a84c; the canonical
results/m13-phase-v1 contains85 exact arithmetic checks across seven
components, with52 pinned inputs. Its payload matches the independent
pre-freeze replay exactly (SHA256bd5f7921ef126884c41736323ecb5ba8a8b18e3c1e39f474ab0628994711b25c).
The root and independent checker outputs are byte-identical
(SHA256bc4d5dd65aaa13c842f1aeaa4ac5c63aa72a91e07110ce8dfc621170ac7806fe).
The independent results/m13-closure-review.md accepts all eight review
tables and verifies preservation of all29 previous M3--M12 receipts.
The62-test suite passes in10.74seconds. No full-goal completion is claimed.

For the next existence step, proofs/M14_BLOCK_MASS_RESEARCH.md records
the exact primitive for every finite bare-product block, monotone
positive block-weight bounds and a tail value allowance. These identities
were checked independently, but the required effective uniform block
enclosures and endpoint signs have not yet been established.
The companion proofs/M14_ENDPOINT_RESEARCH.md specializes the lower
middle mass at theta=.8 to369/2350, and records why current uniform
envelopes remain insufficient. Its rational ledger replays successfully;
this exploratory reduction is separate from the accepted M13 certificate.

## Remaining completion audit

| Full objective obligation | Current evidence | State |
|---|---|---|
| Accessible uniqueness and simplicity | M13 proves at most one simple zero in every N>=32 band; all six known poles have full-band uniqueness | Proved, exact replay and independent closure accepted |
| All intervening indices connected to asymptotics | Uniform uniqueness; existence known for six finite bands and all N>=10^27 | Incomplete: intervening existence |
| Threshold low enough for that connection | Reduced analytically, still impractical | Incomplete |
| Quantitative phase and residue control | Six finite residues, explicit improved M9 errors and all fixed logarithmic coefficients | Substantial advance |
| Uniform noncancellation at sector zeros | M12 proves 1+P<-2 at every F zero for N>=32 | Proved component |
| Integrated final audit of the full theory | M10--M13 accepted; all-index existence coverage remains absent | Incomplete |

The goal remains incomplete. At this historical checkpoint no publication or external contact occurred;
internal AI review is not external peer review and mathematical priority
remains unresolved. All statements concern the restricted W series.

## Pause and public handoff — 2026-09-12

Research paused at the maintainer’s request; publication of the current snapshot
is authorized. See [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) for the authoritative
resumption instructions. M14 contains four internally reviewed components plus
a smooth-envelope candidate and an integrated weighted-mass candidate awaiting
completed independent review. The proposed N>=512 existence threshold is NOT
accepted. No complete M14 canonical receipt or finite 32..511 campaign exists.
The accepted M13 theorem and the completion gaps above remain unchanged.
