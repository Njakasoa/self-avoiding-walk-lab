# M3 automaton scout — age-aware retention and the geometry-only obstruction

Status: **candidate method / priority unresolved**.  This is a bounded scout,
not a claim of a new connective-constant bound.  The producer files were read
at source commit `4a324867c950e8cd27470277cfe36dcfe238916b` together with
`NORMALIZATION.md`, `NEXT.md`, `proofs/DISCOVERY_MEMORY.md`,
`DISCOVERY_REPORT.md`, and the primary finite-memory descriptions by
Pönitz--Tittmann and Couronné.  The pre-implementation scout input hashes were:

```text
NORMALIZATION.md                         37849ff3ddc245d187c1418a75f4d2a65d438c1b181a3effa25dbfe0d5741ec7
NEXT.md                                   afe5e3886826802e4420f87ef63fecd71cb5f5db923153006304a595d5e1dd8a
src/discovery_memory.py                   4f5e2da90e788819b02c58b9c616abc436fdda2c93c724369f54ff011aba3dee
proofs/DISCOVERY_MEMORY.md                2765ad7652d07df8f99b0c95634849a4d89b4f75f4d4a38730dd8680e15e9673
DISCOVERY_REPORT.md                       27bb4c6dd0283ec63947cbc3b95cf6fb0ee6b94bef9de09e225ec3944796926e
references/couronne-2211.16146.txt        ce79419954fe9a3a83e33baf29356589f8b72c7e847d87ae340124107e88e92f
experiments/m3_deadline_probe.py          463aa7a2a29bd9c6adae8f2a2821fa8506ddc160b7bfaf50eb5732525c6cbbaf
```

The reproducible direct probe is
`experiments/m3_deadline_probe.py`.  It stores endpoint-relative
`(x,y,deadline)` triples, keeps all startup states in the full graph, and
uses the exact depth-`m` layer as the memory graph for the certificate.  Raw
image and transition checks are enabled through `m=9`; direct BFS and exact
positive-vector certificates reach `m=13`.  No producer source was changed.
The historical pre-export (runtime-excluded) output digest for the scout default run was
`bd5a52d60f57c94a957e5294d13d9421c04169301d7ef44c79c6566df3ef4071`.

## Candidate A: deadline-safe selective retention

The usual square-lattice state is an ordered suffix

\[
 P=(p_0,p_1,\ldots,p_m),
 \qquad e=p_m,
\]

where a move checks the complete suffix and then shifts it left.  At the
current state, `p_i` is checked on transitions `1,...,i+1` and is absent before
transition `i+2`.  Write this remaining check deadline as

\[
 \tau_i=i+1.
\]

On the square lattice let

\[
 d_i=\lVert e-p_i\rVert_1.
\]

If `d_i > tau_i`, retain no copy of `p_i` in the state.  The reduced state is
the endpoint and the set of deadline-labelled vertices

\[
 R(P)=\{(p_i,\tau_i):d_i\leq\tau_i\}.
\]

On a move to a neighbor `q`, decrement every retained deadline, discard zero
deadlines, append `(q,m+1)`, and apply the same distance filter from `q`.
The candidate move is rejected if it is one of the retained vertices.  This
uses an age label, so it is not the occupied set alone.

### Exactness lemma

For every raw suffix state `P`, the deadline-filtered transition system has the
same continuation words as the raw memory-`m` system, after mapping each raw
state to `R(P)`.

Indeed, after `t` steps an omitted vertex `p_i` has at most deadline
`tau_i-t`, while the endpoint has moved by `t` unit edges.  The triangle
inequality gives

\[
 \lVert e_t-p_i\rVert_1\geq d_i-t>\tau_i-t
 \quad (0\leq t\leq\tau_i).
\]

Thus no continuation can reach that vertex while the raw suffix still checks
it.  After `tau_i` shifts it is absent before the next transition, exactly as
in the raw queue.  The same
argument applies to every omitted vertex simultaneously; a path that would
use an omitted vertex before its deadline would contradict the displayed
inequality.  Induction on continuation length proves that the retained move
sets and the mapped successor states agree.  Equivalently, the map
`P -> R(P)` is a strong weighted lumping of the raw path-window graph, not an
empirical equality of a few counts.  D4 normalization commutes with the map
because coordinates change but deadlines do not.

The rule is valid on any graph with a unit-edge metric satisfying the same
one-step Lipschitz inequality; `L1` is the square-lattice instance.  It also
has a useful implementation consequence: the deadline-labelled states can be
canonicalized and transitions generated after the raw-to-reduced map, rather
than refining a full matrix with an ordinary equitable partition.

### Bounded falsification pass

The direct probe independently enumerates all rooted square-lattice suffixes
through `m=9`, maps each to `R(P)`, and checks that all raw paths mapping to one
reduced state have the same successor multiset.  It also compares those
multisets with direct transitions from the deadline-labelled state.  All
assertions pass: raw image equals the exact depth-`m` startup layer,
disagreement and row-mismatch counts are zero.  Direct startup BFS and exact
`(A+I)^60` positive-vector certificates reach `m=13`; the full direct graph
includes startup transients, while the certificate uses the closed depth-`m`
memory layer.  Exact vector inequalities are checked internally; each output
also exports the exact states, rows and positive integer vector, together with a SHA-256 digest of that vector.

| `m` | raw suffixes checked | depth-`m` memory states | full direct states | memory row entries | exact `U_60` (decimal) |
|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 1 | 2 | 1 | 3.000000000000 |
| 2 | 12 | 1 | 2 | 1 | 3.000000000000 |
| 3 | 36 | 3 | 5 | 7 | 2.831177207208 |
| 4 | 100 | 3 | 5 | 7 | 2.831177207208 |
| 5 | 284 | 12 | 17 | 29 | 2.775591142351 |
| 6 | 780 | 12 | 17 | 29 | 2.775591142351 |
| 7 | 2,172 | 56 | 74 | 132 | 2.744458210180 |
| 8 | 5,916 | 55 | 74 | 130 | 2.744458210180 |
| 9 | 16,268 | 277 | 364 | 635 | 2.724799017564 |
| 10 | — | 270 | 364 | 621 | 2.724799017564 |
| 11 | — | 1,441 | 1,907 | 3,237 | 2.711252338670 |
| 12 | — | 1,397 | 1,907 | 3,148 | 2.711252338670 |
| 13 | — | 7,812 | 10,397 | 17,333 | 2.701374268103 |

The existing D4 path-window counts are 5, 13, 36, 98, 272, 740, 2,034,
5,513, 15,037 at memories 3 through 11, so the depth-layer age map removes a
substantial state set.  The equal `U` values on each odd/even pair are a
control, not a new parity claim: the current repository already identifies
that language plateau.  The table does not establish a best fixed-budget
bound, and the full direct graph still includes startup transients.

### Direct-start proof obligations

The seed is the singleton endpoint `(0,0)` with deadline `m+1`.  A vertex
inserted at startup depth `t` has exactly the deadline it would have in the
depth-`m` suffix after `m-t` further moves.  The distance inequality above
shows that filtering cannot permit a repeated vertex before depth `m`; hence
every startup path of length `m` is a legal full self-avoiding suffix.  At
depth `m`, its filtered state is exactly `R(P)` for that suffix `P`.

Conversely, every legal rooted `m`-edge suffix supplies its own direction word.
Following those `m` directions from the singleton seed reaches its filtered
image, so the depth-`m` layer is exactly the set of raw images.  From that
layer, one-step transitions are closed on the memory-state set, while the
states outside the depth-`m` layer are transient in the full direct graph; some shorter startup states may already coincide with memory states.
Therefore they do not add a recurrent component or change the growth rate;
the certificate is computed on the closed depth-`m` layer.  The probe asserts
these layer equalities for `m<=9` and checks the exact vector inequalities for
all completed cases through `m=13`.

### Literature overlap and next falsification

Pönitz--Tittmann (EJC 7, R21, 2000, §§2 and the automated construction on
PDF pp. 6--7) already keeps a representative suffix and removes initial
steps when they cannot participate in a loop of the memory cutoff.  They also
mention replacing an obstacle-aware shortest-path test by the Manhattan
distance as a deliberately loose check.  Couronné (arXiv:2211.16146v2,
§§3.1--3.5 and §4) already has oldest-vertex deletion, small/large bridge and
small-loop simplifications, plus planar future-connectivity checks.  Therefore
the present rule must be described as an **age-labelled preconstruction
quotient candidate**, with priority unresolved; it is not safe to call it a
new theorem or a new connective-constant method yet.

The direct BFS is still a bounded implementation probe.  It has not been
benchmarked against a production raw generator at a fixed memory/RAM budget,
and no larger-memory or weighted target has been audited here.

## Candidate B: why geometry-only pruning is not an exact state invariant

For a full finite-memory automaton, the occupied set and endpoint do not
determine the next state because the oldest vertex is the one removed.  This
is true even with a fixed root and no symmetry quotient.  The first small
collision found by exhaustive rooted enumeration is memory `m=8`, with the
two valid suffixes

```text
p = (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2)
q = (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2)
```

They have the same occupied set (the whole `3 x 3` square) and the same
endpoint `(0,2)`, but different age order.  The direction word
`left, down, right` is accepted from `p` and rejected from `q`:

```text
p:  left -> (-1,2), down -> (-1,1), right -> (0,1)   accepted
q:  left -> (-1,2), down -> (-1,1), right -> (0,1)   rejected
```

After the first two moves, `(0,1)` has expired from `p` but is still in the
remembered queue for `q`.  Thus merging by `(occupied set, endpoint)` is not a
strong lumping of the finite-memory graph.  The endpoint together with each
retained vertex's remaining deadline is a sufficient exact invariant for the
deadline map; the raw ordered suffix is one representation, while `R(P)` is a
smaller certified one.

There is a related obstruction to treating a finite-memory state as a static
accessible component.  Let `m=13` and use the boundary suffix

```text
(2,0),(3,0),(4,0),(4,1),(4,2),(4,3),(3,3),(2,3),
(1,3),(0,3),(0,2),(0,1),(0,0),(1,0).
```

The occupied vertices form the boundary of a `5 x 4` rectangle and the
endpoint is `(1,0)`.  A finite-memory continuation is

```text
(1,0) -> (1,1) -> (2,1) -> (2,0) -> (2,-1).
```

The first two points are inside the rectangle.  The oldest boundary point
`(2,0)` expires after the first move, so the walk can return to it on the
third move and then leave the rectangle.  A true SAW cannot do this because it
revisits `(2,0)`, but the memory-13 overlanguage can.  Consequently, deleting
finite-pocket or cut information as though it were a permanent topological
obstruction changes the exact finite-memory language.  Such deletion can be a
valid *upper-bound* pruning only with an explicit inclusion proof that all
discarded paths are non-SAW (Couronné's §4.2 is a known planar instance); it
cannot be presented as an exact geometry-only quotient.

The age-labelled boundary/cut deadlines supply the information needed to decide
when a currently blocking vertex can cease to block.  That timing is absent
from occupied-set-only or static-component keys.

## Scout verdict

The strongest bounded result is Candidate A: a singleton-seeded direct BFS
reaches a 1,441-state D4 memory layer at `m=11`, 1,397 at `m=12`, and 7,812
at `m=13`, with exact vector certificates checked internally and exported with states and rows for independent replay.  Its literature
overlap with Pönitz--Tittmann and Couronné is substantial, so no priority claim
is made.  Candidate B is a falsifiable negative result: an occupied-set/
endpoint or static-accessibility key cannot preserve the exact finite-memory
transition system; deadline timing is the missing information.
