# CLAIM-0003 — Odd-memory line graph and quotient source classes

Exact statement: for unweighted square-lattice ordered-suffix automata before
spatial symmetry, A_(m+1) is the directed line graph of A_m when m is odd.
Its coarsest outgoing equitable quotient is isomorphic to Q_m after deleting
classes with zero incoming multiplicity. This also describes the quotients
computed after D4 normalization. No irreducibility assumption is required.

Scope: square, unweighted, unrestricted plane, full ordered suffix and exact
transition multiplicities. Positive-indegree sinks remain. The statement is not
asserted for even m, triangular lattices, arbitrary motifs or zero-weight states.

Proof: proofs/ODD_EVEN_LINEGRAPH.md. The extra collision would close an odd walk
on a bipartite graph; line-graph refinement is determined by the edge head's
outgoing class. Removing source-only classes contributes only zero eigenvalues.

Automatic origin: results/e1-compression-v1 detects207→204 quotient classes from
m9 to m10. This is a finite state-cost observation, not a changed spectral bound.
Prediction before the unseen build: m11 has983 classes and25 source-only classes,
so m12 should have958. Independent actual result:958, with quotient isomorphism.

Independent computation: proofs/check_linegraph_candidate.py imports no producer
code; results/linegraph-candidate-v1 freezes it and records its outputs. Direct
row comparisons and cross-quotient isomorphisms hold for9→10 and11→12.
The even10→11 and triangular controls fail as predicted; a reducible graph with
sinks supports the exact scope. This is evidence beyond matching one scalar.

Closest literature: Pönitz–Tittmann finite-memory parity, standard higher-block
presentations/line graphs and equitable partitions; see the independent priority
audit references/LINEGRAPH_PRIOR_AUDIT.md. Standard consequences are not claimed
as new. Exact specialized first appearance may remain unresolved.

Validity: written finite-graph argument with independent exact computation and
adversarial Astra review. Novelty: no new contribution established. This claim
records a useful known-method explanation, not successful M3 scientific novelty.
Open objection: a more specific prior source may already state the identical
quotient bookkeeping. Publication priority: UNRESOLVED; no publication prepared.
