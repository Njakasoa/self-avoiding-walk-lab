# Prior audit — odd/even finite-memory line-graph observation

Audit date: 2026-09-12. Scope: the candidate statement in
`proofs/ODD_EVEN_LINEGRAPH.md` that, for odd memory `m` on the bipartite
square lattice, the next path-window automaton is a directed line graph, and
that its outgoing coarsest equitable quotient is the previous quotient with
zero-indegree classes removed.

This is a bounded literature audit, not a priority search. I read
`NORMALIZATION.md`, `NEXT.md`, `proofs/EQUITABLE_COMPRESSION.md`,
`STATE_OF_THE_ART.md`, and the primary SAW papers below. No numerical result
was recomputed in this audit; the reported 207/204 and 983/958 counts are
treated as inputs from the candidate artifact, not as independently verified
evidence. No input/output hashes are applicable because this file records
literature only.

## Primary-source evidence

### Finite-memory SAW automata and parity

* Pönitz–Tittmann, *Improved Upper Bounds for Self-Avoiding Walks in
  \(\mathbf Z^d\)*, Electronic Journal of Combinatorics 7 (2000), R21:
  [official article page](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r21),
  [official PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r21/pdf).
  Section 1 (PDF p. 2) fixes an even memory/loop cutoff and explicitly notes
  that the square-lattice loops of length at most 4 are 2 or 4 because loops
  have an even number of steps. Section 2 (PDF pp. 2–4) constructs states as
  classes determined by the recent steps and retains transition
  multiplicities. The automated construction (PDF pp. 6–7) appends a step,
  keeps the relevant suffix, and records all state transfers. Section 3 (PDF
  pp. 8–9) obtains the growth rate from the transfer matrix.

* Couronné, *New Upper Bound for the Connective Constant for Square-Lattice
  Self-Avoiding Walks*, arXiv:2211.16146v2 (2022):
  [arXiv record](https://arxiv.org/abs/2211.16146),
  [PDF](https://arxiv.org/pdf/2211.16146).
  Section 2 (PDF pp. 1–2) recalls the Pönitz–Tittmann finite-memory
  automaton and says explicitly that a loop has an even number of steps. The
  discussion of erasing oldest vertices (PDF pp. 2–3, §3.1) is the same
  memory mechanism used by the candidate. The algorithm and state/transition
  construction are in §5 (PDF p. 6); the paper does not discuss line graphs,
  equitable refinement, or the 207/204 observation.

These sources establish that finite-memory overlanguages and the even/odd
loop control are established ingredients. They do not state the candidate's
quotient relation.

Search limits: this pass checked the cited SAW finite-memory papers and a
small set of primary higher-block, line-digraph, and equitable-refinement
sources. It did not exhaust older symbolic-dynamics, graph-algorithm, or
SAW bibliographies, and it found no source stating these exact quotient
counts or this application-specific formulation.

### Higher-block graphs, state splitting, and sources

* Brix, *Balanced strong shift equivalence, balanced in-splits, and eventual
  conjugacy*, arXiv:1912.05212v2 / *Ergodic Theory and Dynamical Systems*
  42 (2022), 19–39: [arXiv record](https://arxiv.org/abs/1912.05212),
  [PDF](https://arxiv.org/pdf/1912.05212),
  [published DOI](https://doi.org/10.1017/etds.2020.126).
  Section 2 (PDF p. 4) defines a source by `r^{-1}(v)=∅`, i.e. zero
  indegree, and a sink by `s^{-1}(v)=∅`. It then defines the `N`-th
  higher-block graph `E^[N]` (PDF p. 4, §2) to have length-`N` paths as
  edges and length-`N−1` paths as vertices, with the two shifted windows as
  source and range. Therefore `E^[N+1]` is the directed line graph of
  `E^[N]` by definition: its vertices are the edges of `E^[N]`, and its
  edges are compatible pairs. The same section gives the
  canonical higher-block conjugacy. This is the standard symbolic-dynamics
  construction behind the path-window identity.

* Severini, *On the structure of the adjacency matrix of the line digraph of
  a regular digraph*, arXiv:math/0309092v2 (2006):
  [PDF](https://arxiv.org/pdf/math/0309092).
  The definition on PDF p. 2 makes line-digraph vertices the arcs of the
  source digraph and joins two arc-vertices when the first head equals the
  second tail. This is the same overlap rule used by the path windows. The
  paper is regular-digraph focused; it is cited here only for the standard
  directed-line-graph convention, not as a source for the SAW parity claim.

### Weighted/outgoing equitable refinement

* Grohe, Kersting, Mladenov, and Selman, *Dimension Reduction via Colour
  Refinement*, arXiv:1307.5697v2 / ESA 2014:
  [arXiv record](https://arxiv.org/abs/1307.5697),
  [PDF](https://arxiv.org/pdf/1307.5697).
  The introduction (PDF p. 1) identifies iterative degree/signature
  refinement from the one-class partition with the coarsest equitable
  partition. Section 2 (PDF pp. 2–3) defines weighted matrix signatures by
  sums into each current class, states that the limit is the coarsest
  equitable partition, and explicitly notes that the same construction has a
  version for arbitrary weighted directed graphs. This is the general method
  implemented in `src/equitable.py`; the repository's exact `AP=PB` proof
  supplies the row-oriented convention and multiplicity details.

* For the standard quotient identity and line-digraph spectral check, see
  Godsil, *Association Schemes*, §5.1 (PDF pp. 43–44) and Chapter 17 (PDF
  p. 180): [author PDF](https://www.math.uwaterloo.ca/~cgodsil/pdfs/assoc2.pdf).
  Section 5.1 writes the equitable quotient relation as (AH=HB). Chapter
  17 defines the directed line graph through head/tail incidence and gives
  the incidence products for the original and line-digraph adjacency
  matrices, implying equality of nonzero eigenvalues. This supports the
  candidate's statement that deleting source-only/zero modes is a state-cost
  effect, not a new spectral bound.

## Exact comparison with the candidate statement

### 1. The odd-memory path-window identity

Let `A_m` have as vertices ordered `m`-edge SAW suffixes and as arcs the
allowed one-step shift-and-append transitions, before any spatial symmetry
quotient. An arc of `A_m` is an `(m+1)`-edge SAW window. A pair of
successive arcs in `A_m` is always a valid `(m+2)`-edge window except for
the possible new collision of the appended endpoint with the oldest vertex.
That collision closes a cycle of length `m+2`. On a bipartite graph it is
impossible when `m` is odd. Hence, for odd `m`,

\[
                       A_{m+1}=L(A_m)
\]

at the full path-window level, with the equality understood as a directed
line-graph isomorphism and with distinct transitions retained. This is a
direct corollary of the higher-block definition plus the elementary
bipartite parity fact. It is not a new finite-memory SAW method.

For even `m`, the extra collision can close an even cycle, so the line-graph
identity generally fails. On a nonbipartite lattice it can fail already for an
odd `m`. These hypotheses must remain in any statement.

### 2. The outgoing equitable quotient of a line graph

Use the repository's row convention: `A_uv` counts arcs from `u` to `v`,
and refinement compares sums into destination classes. Let π be the stable
outgoing equitable partition of a finite directed multigraph `A`, started
from one class. Give every arc of `A` its own vertex in `L(A)`. An arc `e`
of `A`, viewed as a vertex of `L(A)`, has successors exactly the arcs
leaving `head(e)`. Induction on refinement rounds therefore gives

\[
  \operatorname{color}_{L(A)}(e,t)
  =\operatorname{color}_{A}(\operatorname{head}(e),t)
\]

up to a renaming of colors, after omitting colors that occur on no head of an
arc. A color class `C` occurs on no head exactly when its total indegree is
zero. Thus the stable quotient of `L(A)` is the restriction of the stable
quotient of `A` to classes with positive total indegree:

\[
     Q(L(A)) \cong Q(A)[R,R],\qquad
     R=\{C:\text{some arc enters }C\}.
\]

There is no independent literature priority claim for this exact two-line
lemma in the SAW notation; it follows immediately from the standard
higher-block and equitable-refinement definitions. It is safe to describe it
as a **known consequence / elementary corollary**, provided the arc-expanded
multigraph convention and the outgoing refinement convention are stated.
Applying an ordinary unweighted line graph directly to an integer-weighted
quotient can be wrong: multiplicities must be represented by parallel arcs or
by an equivalent weighted incidence factorization.

The D4 action is an automorphism of the full path-window graph. Since the
refinement starts from one class, the stable classes are D4-invariant, so an
orbit quotient with transition multiplicities can be used before refinement.
This transports the above lemma to the implementation, but it should be
stated as a quotient/intertwining argument rather than as an assertion that
an arbitrary quotient operation commutes with line graphs.

### 3. The 207/204 observation

The candidate artifact reports 207 classes at `m=9`, 204 at `m=10`, and
three zero-indegree classes at `m=9`; it also records a corresponding
983-to-958 prediction for the later step. Those numbers were not recomputed
here. If the saved matrices verify the stated quotient isomorphism, the
counts are an instance of the generic corollary above.

No Pönitz–Tittmann or Couronné passage found in this audit reports these
quotient counts or the line-graph explanation. The exact numerical anomaly
should therefore be labelled **UNRESOLVED specialized observation** for
priority purposes, with no first-observation claim. Its mathematical
explanation should be labelled **KNOWN CONSEQUENCE**, not presented as a new
theorem, unless a substantially stronger invariant or a new SAW result is
added.

## Verdict and safe wording

* Finite-memory SAW overlanguages, even-loop parity, suffix-state transfer
  matrices, and symmetry compression: **KNOWN** (Pönitz–Tittmann; Couronné).
* Full path-window identity `A_{m+1}=L(A_m)` for odd `m` on a bipartite
  graph: **KNOWN CONSEQUENCE** of higher-block graphs plus bipartite parity.
* Stable outgoing equitable quotient of a line graph as the previous quotient
  with zero-indegree classes removed: **KNOWN CONSEQUENCE / elementary lemma**
  under the explicit multigraph, multiplicity, and row-refinement hypotheses.
* The particular square-lattice quotient counts and their first appearance in
  this lab: **UNRESOLVED specialized observation**. No novelty or priority
  claim is supported by this bounded audit.

Recommended claim wording:

> For the unquotiented square-lattice path-window automaton, odd-memory
> extension is the directed line-graph operation because the only additional
> collision would close an odd cycle. Under outgoing weighted equitable
> refinement, line-graph vertices inherit the color of their head, so source
> (zero-indegree) quotient classes disappear. The observed class-count drop is
> a finite implementation consequence of these standard constructions.

Do not call the drop a new spectral improvement: line-digraph incidence
factorization preserves nonzero spectral data, and the finite-memory upper
bound remains the established Pönitz–Tittmann/Couronné strategy.
