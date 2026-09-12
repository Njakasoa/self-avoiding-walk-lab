# Independent review of the finite M8 derivative mechanism

The differentiated-tail mechanism is mathematically valid on the six frozen
M7 brackets, conditional on successful interval evaluation for each bracket.
The independent execution covered N=32 and the four jet tests. It does not
constitute an independent execution of the other five rows. Together with
matching frozen M7 endpoint signs and noncancellation intervals, a strictly
negative derivative certifies exactly one simple, noncancelled W pole inside
each successfully checked narrow bracket. This says nothing about entire
phase bands, intervening indices, an effective asymptotic threshold, or novelty.

## Analytic audit

The I384 arithmetic rounds both endpoints outward, including reciprocal,
square root and the atanh logarithm remainder. The jet rules are ordinary
first derivative identities applied through inclusion-preserving arithmetic.
Whole-bracket input intervals enclose every point of the rational bracket;
finite recurrence division guards rule out singularities throughout it.

For the directed tail, the affine denominator beta+gamma*q^(2k) is bounded
below by min(beta,beta+gamma)>0. Differentiation gives numerator derivative
q^k+t*k*q^(k-1)*q' and denominator derivative
beta'+gamma'*q^(2k)+2*k*gamma*q^(2k-1)*q'. In the latter contribution the
producer drops the further numerator factor q^k for the gamma terms. Since
0<q<1 this enlarges the absolute bound. Its S0 and S1 geometric sums and
explicit q factor are therefore valid; the derivative tail is uniform.
The interval mden need not be a point: its lower endpoint is the required
positive uniform denominator lower bound, and outward division remains safe.

For the prudent tail, monotonicity U_v>0 follows from a_v=-t*(1-t^2)<0 and
the physical kernel formula. Thus t<=u_n<=u_m<=q<1 after the cutoff.
The otherwise implicit bound u_n<=1 justifies dropping u_n in the term
|D'|*u_n of the stated G bound. The exact integer ratio guard makes
n*q_+^(2n-1) decrease after m; hence the displayed kernel partial bounds
cover every subsequent u_n'. Differentiating rho=r*g/(g+delta) gives
rho'=r'*g/(g+delta)+r*(delta*g'-g*delta')/(g+delta)^2.
The producer's Lambda consequently bounds |rho'| uniformly.

Induction on z_(n+1)=rho_n*z_n yields
|z'_(m+k)|<=R_+^k*(Z'+k*Z*Lambda/R_+), with R_+ a fixed positive
uniform majorant. No derivative of an inequality or derivative of R_+ is
needed. Summing this affine-in-k geometric bound with the complete weight
jets gives exactly the implemented prudent derivative tails. The H tail
also includes the derivative of t^2. These summable uniform bounds justify
termwise differentiation. The negative omitted value tails follow from
Q>0, z_n<0 and V_j>0; derivative tails correctly remain symmetric.

The frozen M7 source-pole exclusions and local holomorphy argument complete
the passage from monotonic real F to a simple holomorphic zero. At that zero,
W=-1-(1+P)/F has residue -(1+P)/F_t, which is strictly negative when both
1+P and F_t are strictly negative. Interval division of the two whole-bracket
boxes therefore encloses the residue without needing the exact root.

## Execution and provenance

The review read NORMALIZATION.md, NEXT.md, M7_FINITE_TAIL.md, the M7 interval
implementation, M8_FINITE_DERIVATIVES.md, the M8 producer and the jet tests.
The three frozen M7 hashes match those quoted in the M8 note.

Command `.venv/bin/python -m pytest -q tests/test_m8_jets.py` passed all four
tests (0.12 seconds). These are diagnostics, not substitutes for tail proofs.
Exact replay output, source commit, input SHA-256 hashes and a canonical
output SHA-256 are in `results/m8-finite-review-N32.json`.

The first replay exposed a producer serialization defect: tail['R'] was a
Jet384 but _record_tail handled only I384. The mathematical N32 evaluation
completed, but ordinary json.dumps failed. This was reported immediately to
the integrating root. The review driver uses an explicit record() fallback
so its exact output is retained independently; the receipt states this
fact. This defect must be fixed before calling the documented producer
command reproducible. The initial source hashes in the replay receipt
identify the reviewed version rather than silently attributing the replay
to later edits.

## Corrected wrapper review

The integrating root fixed _record_tail to recognize Jet384 as well as I384.
A second independent N32 replay calls experiments.m8_finite_batch.payload([32])
and uses ordinary JSON serialization successfully. Both initial and corrected
source hashes and exact outputs are retained in the review JSON, with the
corrected run under corrected_wrapper_replay. The mathematical derivative
interval is unchanged. This resolves the producer serialization finding.

The wrapper pins the M7 payload SHA-256, checks exact equality of rational
bracket strings, decodes and rechecks the endpoint signs and whole-bracket
noncancellation sign, requires the frozen source-pole flag, and rechecks the
M8 numerator and derivative signs before calculating the residue. Its formula
residue=-(1+P)/F_t and the N^3 scaling are correct in the t coordinate.
It explicitly limits claims to the listed narrow brackets. The independently
replayed N32 wrapper result passes these checks. Root must retain successful
canonical output for all six rows before reporting the six-row computation
complete; this reviewer independently executed only N32.

Final finite integration audit: the canonical six-row receipt is now retained
at results/m8-finite-v1/payload.json, SHA-256
2fbc77d8d1740f87327b00ec62101a2faf66be18ce92accf5af334dcb51d1da3.
Its metadata records source commit 0a62a455d75d1880ab73ef7bae91cc3492d9d82e
and runtime 279.20077854300325 seconds. The N32 row is exactly identical
to the independently retained corrected replay. Later changes to the M8
note describe the serialization issue; the jet tests add its regression
check. These were reviewed, all five targeted tests passed (0.09 seconds),
and another N32 replay produced the identical result. The original snapshots
remain unchanged; final_review_snapshot records the final hashes and replay.
The six-row receipt checker was reviewed for its hash validation, exact
scope, recomputed signs/residue boxes, N32 comparison and tail targets.
It is a receipt verifier, not a second independent six-row producer run.
