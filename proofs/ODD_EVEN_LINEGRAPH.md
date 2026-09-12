# Odd/even memory as a directed line graph

Status: a candidate structural explanation of an automatically detected finite
observation; standard ingredients, no novelty asserted. Independent computation
and priority audit are separate files. This statement is deliberately restricted
to unweighted square-lattice walks without domain or motif modifications.

Let A_m be the translation-normalized automaton whose vertices are ordered
m-step square SAWs and whose transitions append a neighbor not among the m+1
remembered vertices, then drop the oldest vertex. Directions are distinct
transitions and multiplicities are retained. Before spatial symmetry reduction,
each edge of A_m corresponds uniquely to an (m+1)-step SAW. Translation of the
whole path fixes this correspondence without changing adjacency.

If m is odd, consider two compatible edges, represented by successive windows
(p_0,...,p_(m+1)) and (p_1,...,p_(m+2)). Both windows are self-avoiding. The only
extra collision excluded by memory m+1 would be p_(m+2)=p_0. Such a collision
would close a walk of odd length m+2 on a bipartite graph, which is impossible.
Thus A_(m+1) is the directed line graph of A_m: vertices are edges of A_m, and
an edge e may be followed by f precisely when head(e)=tail(f). This assertion
includes sinks and vertices without incoming edges. It fails in general for
even m; on a nonbipartite lattice even the first odd-m assertion can fail.

Now consider any finite directed multigraph A, with its coarsest outgoing
equitable partition started from one class. Its refinement at step k assigns
colors according to the previous color and counts of outgoing edges into each
previous color. In the line graph, every edge-vertex e receives the same color
as its head(e), up to relabeling and deletion of unused colors. This follows
inductively: outgoing edges of e are exactly all edges leaving head(e).
Colors absent among heads have no incoming edge at all, so every vertex has
zero outgoing count into them. Omitting those coordinates cannot distinguish
or merge any remaining colors at a later refinement step. Consequently:

1. Two line-graph vertices are equivalent exactly when their heads are
   equivalent in A's coarsest equitable partition.
2. The quotient of the line graph is isomorphic to the quotient of A with
   classes that have zero total incoming multiplicity removed.
3. The number of quotient classes cannot increase in this line-graph step.
4. Removing such source classes leaves the nonzero spectral data unchanged;
   the characteristic polynomial only loses zero factors. If the graph is
   empty or acyclic, both radii are zero. The general line-graph statement
   also follows from the products of tail/head incidence matrices.

The D4 action is a graph automorphism. Starting refinement from a single class
makes every refined class D4-invariant. Thus refining after the D4 orbit quotient
gives the same coarsest quotient as refining the full graph, with multiplicities
preserved. Applying the preceding result therefore gives the testable prediction
for the actual E1 implementation:

    Q_(m+1) ≅ Q_m with its zero-indegree classes deleted, for odd m.

E1's automatic state-count anomaly is 207 classes at m=9 and 204 at m=10.
There are exactly three zero-indegree classes in the saved m=9 quotient.
The m=11 quotient has 983 classes and 25 zero-indegree classes; the prediction
registered before the independent m=12 computation is 958 classes. Quotient
isomorphism, not just class-count agreement, is the stronger falsification test.

This explains a finite state-cost effect and the known odd/even language
plateau. It neither improves the spectral radius by deleting a source class nor
provides a new square-lattice connective-constant bound. Standard higher-block
presentations, line graphs and equitable partitions are the closest ingredients;
the specialized priority assessment is recorded independently.
