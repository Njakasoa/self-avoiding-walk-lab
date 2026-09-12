# NEXT programme: E1–E3 and discovery engine

The planned E1, E2 and E3 experiments are complete. M2 now exposes the requested
parameter families, records certificates/costs and generates observations from
the computed data. The selected structural observation survived independent
falsification, but the priority audit identifies standard mathematical
ingredients. M3 scientific novelty and M4 publication remain UNRESOLVED.
This completes the scoped NEXT experimental programme, not the original
research mission's requirement for a new mathematical contribution.

The original plan is retained verbatim in environment/NEXT_GOAL_BRIEF.md.
Instructions and runnable configurations are in DISCOVERY_ENGINE.md and
examples/discovery/. All M1 outputs remain historical, without rewriting.

## E1 — Exact compression and construction cost

Every completed raw/orbit/equitable comparison preserves exactly the same
rational upper certificate. Independent geometry reconstruction verifies
AP=PB, lifted positive vectors and17 further continuation steps. Invalid
partitions are rejected in the independent tests.

| Memory | D4 states | Equitable classes | U, approximate display |
|---:|---:|---:|---:|
| 3 | 5 | 3 | 2.8311772072 |
| 4 | 13 | 3 | 2.8311772072 |
| 5 | 36 | 11 | 2.7755911424 |
| 6 | 98 | 11 | 2.7755911424 |
| 7 | 272 | 47 | 2.7444582102 |
| 8 | 740 | 47 | 2.7444582102 |
| 9 | 2034 | 207 | 2.7247990176 |
| 10 | 5513 | 204 | 2.7247990176 |
| 11 | 15037 | 983 | 2.7112523387 |

The unsymmetrized memory11 graph exceeds the100000state cap; its case has no
certificate. All26 other configurations complete. The equitable memory11
matrix fits a1000class certificate budget, but its15037state graph must still
be constructed. The synthesis reports these two budgets separately. It does
not claim compression avoids the construction peak or improves the radius.

E1 automatically detected the207→204 drop. The line-graph explanation predicts
an unseen958classes at memory12 from983classes minus25 source-only classes at
memory11. Independent reconstruction finds40617 D4 states,958classes and the
predicted quotient isomorphism. Even-memory and triangular generalizations are
falsified. Details, scope and priority: CLAIM_SELECTION.md, claims/CLAIM-0003.md,
proofs/ODD_EVEN_LINEGRAPH.md, references/LINEGRAPH_PRIOR_AUDIT.md.

## E2 — Length/span dictionaries at equal cost

Twenty cases cover length cutoffs12,14,16,18 and span caps1,2,3,4,unbounded.
All coefficients through each cutoff are retained. Direct geometric cuts and
bivariate renewal inversion agree. Span nesting preserves coefficients and
increases rational lower bounds. The longest unrestricted case takes about
16seconds locally; the five-minute cap is not approached.

| DFS prefix budget | Selected length/span | Certified L, approximate display | Best tested unbounded-span baseline |
|---:|---|---:|---:|
| 10000 | 14 / 2 | 2.5133103735 | no eligible case |
| 100000 | 14 / 3 | 2.5320469517 | 2.5169419014 |
| 1000000 | 18 / 3 | 2.5489746304 | 2.5325080864 |
| 3000000 | 18 / 4 | 2.5537947816 | 2.5325080864 |
| 30000000 | 18 / unbounded | 2.5538998098 | 2.5538998098 |

These are selections over the finite declared sweep, not optimality over all
dictionaries. Deterministic DFS-node budgets complement machine-dependent
times. The payload also retains the Pareto frontier and dominated cases.

The known span1 control has I(z)=z(1+z)/(1−z), giving1+sqrt(2). Its finite
dictionary approaches this value from below. The prescribed full-start
order≤5 rational recurrence screen finds the span1 control and passes held-out
lengths15–18. The six span2–4 exact/cumulative families have no unique fit in
this screen; failures are archived and no nonrationality conclusion is drawn.
Independent tests compare bridge conventions and attack concatenation collisions.

## E3 — Anisotropy, held-out points and physical scope

Independent prefix enumeration reproduces six symbolic Table1 cases of He
(SAW/SAT at(1,2),(1,3),(1,4)). All48 specialized matrices have independently
replayed exact rational spectral certificates and root brackets. The memory
sweep has32cases: memories3,5,7,9 at ratios1/4,1/2,1,2,4 and held-out2/3,3/2,7/5.
The best tested memory is9 at all eight ratios. Off isotropy, the symmetry group
has order4 and the quotient has413classes; at isotropy it has207classes.

Scaling by3/2 and exchanging axes preserve the certificates exactly in the
additional controls. The invalid anisotropic D4 mutant is rejected. All tested
geometric triples satisfy the finite log-convexity inequality, which is expressly
not a theorem about arbitrary selected certificates. Near-axis samples1/100,
1/1000,1/10000 have decreasing certificate gaps above the exact axial mu=1.
The finite-iteration certificate at the axis still exceeds1 by a positive
rational amount below10^−18; it is not relabelled equality or a convergence proof.

For positive targets, log(mu)≤log(U) and z_c≥1/U; a lower L gives the opposite
inequalities. These express entropy/free energy per step and critical fugacity,
without estimating critical exponents. The pointwise comparison is to small
reproduced He cases, not to the strongest available He computation or literature.

## Validation and limits

The complete suite passes49tests, including independent small geometry, weighted
quotient mutants, bridge collisions, finite connectivity transfer versus occupied
set transfer/DFS, and the existing C++/sanitizer checks. The independent discovery
verifier checks all completed saved spectral inequalities, full E1 geometry,
all48 He matrices, bivariate renewal/root intervals and frozen source receipts.
Astra's final review is results/discovery-astra-review.md.

Canonical payloads: results/e1-compression-v1, results/e2-spans-v1,
results/e3-weights-v1, results/m2-variants-v2, results/discovery-findings-v1,
results/linegraph-candidate-v1. Earlier m2-variants-v1 is retained. Source commits
are96ced5c,5d9f711,6096543,0166e6f,eed1923 as recorded by each receipt.
Tests were run on source eed1923; the final validation receipt freezes evidence
and verifies its hashes. Process RSS scopes are explicit: E2 reports cumulative
producer peak; memory cases use isolated children. Timings can vary under load.

For the unrestricted square target, convenient outward-rounded local bounds are
2.553899≤mu≤2.711253. These are weaker than known literature bounds and make no
frontier claim. The line-graph explanation is a known consequence; exact finite
class-count priority is unresolved. The broader research mission remains open.
