# Independent adversarial review of the NEXT programme

Reviewer: Astra subagent, read-only with respect to implementation. Review source
HEAD: `609654304675da0ad4e4acb4e1bfef2b48f50231`. This report is a mathematical
and scope review, not a novelty certificate. The root owns final integration and
the authoritative full test run.

## Verdict

No critical mathematical defect was found in the inspected finite-memory
inclusion, weighted stabilizer quotient, equitable certificate transfer,
bivariate bridge renewal, or small He matrix reproduction. The evidence supports
completion of the bounded E1/E2/E3 computations and an M2 experiment engine,
subject to the integration items below. It does **not** establish a scientific
breakthrough, a novel M3 result, or readiness for M4 publication.

The review read the frozen NEXT brief, DISCOVERY_PLAN, NORMALIZATION, all six
requested implementation modules, E1/E2/E3/M2 drivers, the discovery tests, and
the relevant memory/equitable/bridge/weighted/odd-even proofs. It inspected
canonical E1 v1, E2 v1, E3 v1 and M2 variants v1 outputs. Source-file hashes were
independently checked against their recorded git commits and every corresponding
payload hash checked against its bytes; all matched. A dirty worktree flag in
these receipts does not itself invalidate source freezing: the listed source
bytes match the recorded commit. Historical runs are not reruns of later edits.

## Findings requiring accurate integration

1. **E2 equal-cost interpretation was missing from its original payload.** The
   saved tables compare span caps at fixed lengths and report DFS node costs;
   they do not themselves select the best lower bound under a common DFS budget
   across both length and span. The root has acknowledged this and is preparing
   a source-frozen synthesis. Do not describe raw same-length tables alone as
   the answer to the equal-cost NEXT question. A budget frontier from saved
   measurements is sufficient for this bounded experiment; it does not imply
   global optimality over untested families.
2. **E3 physics interpretation needs explicit bounds.** The producer reports
   rational upper certificates, not free energies or critical fugacities.
   For each positive target, state `log(mu) <= log(U)` and `z_c >= 1/U`.
   No critical exponent follows. The root has acknowledged this narrative gap.
3. **Finite axis and convexity controls have limited force.** The original E3
   run checks the exact axis formula independently and certifies one small
   positive x, while its matrix assertion only requires `U >= 1` on the axis.
   These are consistency controls, not a proof of convergence of the chosen
   finite-iteration certificate to the axis value. Likewise all geometric
   grid inequalities passing does not prove log-convexity of the selected U
   between points. Current labels correctly say tested-only. Additional epsilon
   points would still be finite evidence.
4. **Complete-case deadlines apply at the subprocess boundary.** Direct Python
   `memory_case`/`run_case` calls only enforce the constructor's budget and can
   continue through refinement/certification beyond it; canonical memory CLI
   and E1/E3 subprocess runners have outer deadlines. This is not a certificate
   soundness issue. Do not advertise a hard complete-case wall limit for all
   direct API calls. M2 variants v1 also predates the rectangle dispatch run;
   the planned variants v2 is needed as the canonical interface evidence.

## Mathematical assessment

The state stores the ordered m-edge suffix, so deletion order is preserved.
All target SAWs have valid suffixes and their extensions are accepted. Strip
and motif restrictions change the target and are correctly retained in output;
they are never upper bounds for unrestricted square SAWs by themselves. The
square/triangular stabilizer test preserves directional weights, domains and
motifs. Zero-weight historical states may loosen a bound without invalidating
it. The positive integer vector and exact `Av <= Uv` verification work without
irreducibility. Empty complete state spaces are separately handled.

Equitable refinement preserves sums into every class, not merely observed total
continuation counts. Its exact `AP=PB` relation lifts positive certificates and
all continuation vectors. Its proof also establishes equal spectral radii.
This is a weighted outgoing equitable partition, not general labelled DFA
minimization. Independent word-based tests and malformed/random partition
controls reduce shared-implementation risk; they are finite verification, not
new mathematics.

Bridge pruning by terminal span is valid because a bridge finishes at its
running maximum. The strict initial minimum/weak terminal maximum convention
makes concatenation self-avoiding and renewal cuts unique. Capped dictionaries
select pieces, whose concatenated total span remains unbounded; the resulting
renewal root has the lower-bound direction. The analytic span-one identity is
proved independently of recurrence fitting. Only the already known span-one
screen finds a recurrence; all other order-at-most-five failures are retained.

He rows divide by the fixed prefix weight, and the exponent is `1/(n-1)` for
m=1. Positive 2-by-2 matrices satisfy the stated primitive hypothesis. SAW/SAT
objects remain distinct; a SAT upper bound is also a weaker admissible SAW
upper comparator. The six symbolic invariant checks and exact rational
spectral/root-power checks support the reproduction. Comparisons use the same
anisotropy target, avoiding meaningless global minima across weight scales.

## Odd/even candidate

The proof's bipartite argument is sound: for odd m, the only additional
collision between two compatible successive windows would close an odd cycle
of length m+2. Before symmetry reduction, the next memory graph is therefore
the directed line graph. Outgoing equitable colors of an edge are inherited
from its head. Classes absent among heads have identically zero incoming
multiplicity, so their omission cannot affect refinement of the remaining
classes. D4 invariance of refinement from one initial color justifies applying
the statement after the orbit quotient.

Thus the 207-to-204 observation is consistent with deleting three source
classes, and 983 minus 25 predicts 958 at m12. Equality of that count alone is
weaker than the proposed quotient-isomorphism check. The independent m12
computation and its receipt were not yet available at this review snapshot.
The argument explains a state-cost/parity effect and does not improve a
spectral radius. Standard line-graph, higher-block and equitable-partition
ingredients make a specialized priority audit necessary; validity cannot be
substituted for novelty.

## Observed outputs and acceptance boundary

E1 has 26 certificates and one honest raw-m11 state-cap failure; D4/equitable
m11 completed. The best displayed U is about 2.711252338667645; raw construction
cost and final certificate size are correctly distinguished. E2 completed all
20 length/span cases through n18, with best displayed lower bound about
2.553899809777332. E3 completed 32 memory points and 48 He cases, reproduced six
symbolic cases, and had no failures on its finite log-convexity grid; m9 gives
the smallest tested memory certificate at all eight ratios. These finite
comparisons neither establish record bounds nor identify a new invariant that
improves the actual spectral radius.

Accept the bounded programme/M2 only with its source-frozen synthesis,
independent candidate check, and final tests recorded by the root. M3 remains
unresolved until a complete claim, importance/novelty selection, independent
attacks and literature audit support an actual new result. M4 remains
UNRESOLVED, with no external publication authorized or performed by this review.

## Final addendum — integrated evidence accepted

This addendum supersedes the pending integration conditions in the earlier
snapshot. The reviewer inspected DISCOVERY_ENGINE.md, DISCOVERY_REPORT.md,
CLAIM_SELECTION.md, CLAIM-0003, CLAIM-0004 and LINEGRAPH_PRIOR_AUDIT.md, together
with the now completed synthesis, variants v2, independent line-graph payload,
and full-suite test record.

All three new canonical receipts passed an independent hash check: listed input
bytes match their recorded commit, and saved payload bytes match their output
hash. They are `discovery-findings-v1` at `0166e6f516723c64e8b995f255832ab29f112cb2`,
`m2-variants-v2` at `609654304675da0ad4e4acb4e1bfef2b48f50231`, and
`linegraph-candidate-v1` at `eed1923e78f7cf5d0fa643e3d09b4b1826d8ff92`.

The synthesis closes the equal-cost omission: its rational comparisons select
among all completed declared length/span cases under each common DFS-node
budget and retain the Pareto frontier, dominated cases, and eligible
unrestricted-span baseline. Its implementation and saved selections support
the report's finite-sweep interpretation. It does not silently turn span pruning
into a different asymptotic target. Physical inequalities and cooperative versus
outer-process deadline semantics are now explicit in DISCOVERY_ENGINE.md.
Supplemental near-axis points and the strictly positive residual axis certificate
gap are honestly distinguished from the exact direct axial value and from any
limiting theorem. The conservative triangular-strip subgroup limitation is also
documented. Variants v2 supplies the previously missing canonical rectangle
width/bridge interface evidence.

The independently implemented line-graph check confirms 958 classes from 40617
D4 states at m12. More strongly, it verifies weighted quotient bijections for
9-to-10 and 11-to-12. Direct row comparisons have zero differing rows in both
odd-memory transitions; the even 10-to-11 control has 372 differing rows, and
triangular controls also fail. The reducible/sink example keeps positive-indegree
sinks and deletes only source-only classes. This closes the independent
candidate-computation condition; scalar agreement alone was not used.

The full-suite record reports 49 tests passed in 8.44 seconds on source
`eed1923e78f7cf5d0fa643e3d09b4b1826d8ff92`, with tested-source hashes retained.
The reviewer inspected that record; the root performed the actual full test run.
The final validation command, which the root will execute after freezing these
documents, remains a release verification step and is not pre-emptively claimed
as passed here.

**Final scope verdict:** no remaining material mathematical or requirements gap
was identified for the bounded NEXT E1–E3 experimental programme and M2 engine.
Accept that scoped completion once the root's final validation succeeds. The
post-sweep selection heuristic is disclosed rather than presented as
preregistered. The priority audit explicitly classifies the structural result
as a known consequence and exact-count first appearance as unresolved. Claims
and report maintain this distinction. M3 as a new scientific contribution and
M4 publication therefore remain UNRESOLVED; neither is implied by this
engineering/experimental acceptance.
