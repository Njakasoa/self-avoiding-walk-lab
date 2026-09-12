# Independent line-graph candidate check

This receipt is an independent falsification attempt for the proposed
square-lattice relation between consecutive finite-memory automata.  The
checker rebuilds path geometry, D4 normalization, weighted rows, and
coarsest outgoing equitable partitions using only Python's standard
library; it imports no producer from `src`.  Counts are finite exact
integer computations and do not assert novelty.

## Provenance

- Source commit: `eed1923e78f7cf5d0fa643e3d09b4b1826d8ff92`; worktree dirty: `True`.
- Command: `PYTHONPATH=. .venv/bin/python proofs/check_linegraph_candidate.py`.
- Input SHA-256: checker `0f8723bcc8f26bfb78fe86e1489f4497e0d3b82bbea1f70c6f3c77bfd918670d`, 
`NORMALIZATION.md` `37849ff3ddc245d187c1418a75f4d2a65d438c1b181a3effa25dbfe0d5741ec7`, 
`proofs/FINITE_MEMORY.md` `1f530880df261fa06518d34f26b36d385105cb57d70411aa07705fa74dc22e11`, 
`proofs/EQUITABLE_COMPRESSION.md` `fa19eb28b37a830e04832db92ac8be17315ad659f214a462cf314cf6200ffaca`.
- Deterministic result SHA-256: `b610bedb5190ef46ba6b6dba392de9dad9a0b60f87fe6ff7eace4226ea5a1189`.

## Prediction recorded before the m12 build

After independently computing m11, its quotient had `983` classes and `25` zero-indegree classes.  The line-graph candidate therefore predicted 
`q12 = 958` classes.  The actual m12 quotient after construction was `958` (`prediction_matches=True`).  This prediction was written to this report before constructing the m12 state layer.

## Square D4 geometry and partitions

Rows retain directional multiplicity after D4 orbit normalization.  `zero-in` and `zero-out` count quotient classes, not raw states.

| memory | D4 states | transition weight | stored row entries | quotient classes | zero-in | zero-out | build seconds |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 2034 | 5514 | 5512 | 207 | 3 | 1 | 0.147 |
| 10 | 5513 | 15038 | 15036 | 204 | 0 | 1 | 0.456 |
| 11 | 15037 | 40618 | 40616 | 983 | 25 | 1 | 1.489 |
| 12 | 40617 | 110189 | 110187 | 958 | 8 | 1 | 4.219 |

## Direct row-level line-graph test

For each next-memory state p'=(v0,...,v_(m+1)), the candidate row allows
extensions avoiding the suffix (v1,...,v_(m+1)); the actual row also
forbids v0.  A difference is exactly a closing walk of length m+2.

| m -> m+1 | candidate equals actual | differing rows | candidate extra weight | actual missing weight |
|---:|:---:|---:|---:|---:|
| 9 -> 10 | True | 0 | 0 | 0 |
| 10 -> 11 | False | 372 | 372 | 0 |
| 11 -> 12 | True | 0 | 0 | 0 |

## Quotient comparison without label matching

The proposed quotient for m+1 is the m quotient restricted to classes
with positive indegree.  Each comparison starts one colour on the
disjoint union, refines by exact weighted outgoing signatures, and then
checks the resulting cross-side bijection edge by edge.

| comparison | next quotient | restricted current quotient | isomorphic | refinement rounds | union blocks |
|:---|---:|---:|:---:|---:|---:|
| m9 -> m10 | 204 | 204 | True | 8 | 204 |
| m10 -> m11 | 983 | 204 | False | 0 | None |
| m11 -> m12 | 958 | 958 | True | 9 | 958 |

## Reducibility, sinks, and zero-indegree classes

The graph-theoretic reason for the restriction is local: a line-graph
vertex is an edge of the original graph, so its class is determined by
the class of its head.  A class with zero indegree contributes no line-
graph vertices and is removed.  A positive-indegree sink still contributes
vertices, whose rows are zero; reducibility therefore does not justify
dropping sinks.  A separate small reducible graph with both an unreachable
source class and sink classes gave:

`{"linegraph_quotient_vertices": 2, "original_quotient_vertices": 3, "original_vertices": 6, "positive_indegree_classes": 2, "quotient_isomorphism": {"isomorphic": true, "left_vertices": 2, "reason": "weighted refinement produced a verified bijection", "refinement_rounds": 2, "right_vertices": 2, "singleton_cross_side_blocks": true, "union_blocks": 2}, "sink_classes": 1, "zero_indegree_classes": 1}`

The synthetic line-graph quotient matched the positive-indegree
restriction exactly, including the sink class.

## Triangular negative control

The triangular lattice was rebuilt with identity normalization.  Its
triangles make the odd closing walk possible, so the same row test should
fail already at m=1 (closure length 3).

| m -> m+1 | states at m+1 | candidate equals actual | differing rows | candidate extra weight |
|---:|---:|:---:|---:|---:|
| 1 -> 2 | 30 | False | 12 | 12 |
| 2 -> 3 | 138 | False | 24 | 24 |

## Interpretation

The square odd-memory row checks and the m9/m10 and m11/m12 quotient
checks are the predicted matches; the even-memory square check and the
triangular control are negative controls.  This supports the finite
candidate and its positive-indegree bookkeeping for these exact graphs
only.  It is a standard line-graph/equitable-partition observation and
carries no novelty claim or infinite-lattice conclusion.
