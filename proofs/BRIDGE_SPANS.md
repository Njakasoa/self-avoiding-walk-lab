# Bivariate bridge renewal and span-indexed dictionaries

This note fixes the bridge convention used by `src/bridges.py` and
`src/bridge_spans.py`.  A path starts at `(0,0)`, has length `n` equal to its
number of edges, satisfies `x_j > 0` for every `j > 0`, and is a bridge when
its terminal coordinate is the visited maximum:

\[
  x_n = \max_{0\leq j\leq n} x_j .
\]

The terminal maximum is weak.  The path may reach its final span before its
last edge and then move vertically.  The first edge is necessarily east;
this removes an impossible branch at the root and does not identify any
rotations or reflections.

For a bridge `\omega`, an internal index `k` is a renewal point when

\[
  x_k=\max_{0\leq j\leq k}x_j
  \quad\text{and}\quad
  x_j>x_k\quad(k<j\leq n).
\]

The first condition says that the prefix ending at `k` is a bridge.  After
translating the suffix by `-\omega_k`, the second condition is its strict
initial minimum; the terminal maximum condition is inherited from the whole
bridge.  Consequently both pieces are bridges in the same convention.  A
bridge is irreducible when it has no such internal index.

## Bivariate factorization

Let `b_{n,s}` count bridges of length `n` and terminal span `s`, and let
`i_{n,s}` count geometrically irreducible bridges.  Include the formal empty
bridge with `b_{0,0}=1`, and set `i_{0,0}=0`.  If a bridge is cut at every
renewal point, the resulting irreducible factors are unique.  Conversely,
translate the next factor to the current endpoint and concatenate.  Strict
positivity of the translated factor's x coordinates makes all new vertices
strictly to the right of the joining vertex, so concatenation remains
self-avoiding.

Lengths and spans add under this translation.  Therefore, as a formal
power series in length `z` and span `u`,

\[
 B(z,u)=1+I(z,u)B(z,u),
 \qquad
 B(z,u)=\frac{1}{1-I(z,u)},
\]

where

\[
 B(z,u)=\sum_{n,s\geq0}b_{n,s}z^nu^s,
 \qquad
 I(z,u)=\sum_{n\geq1,s\geq1}i_{n,s}z^nu^s.
\]

The coefficient recurrence is

\[
 b_{n,s}=\sum_{k=1}^{n}\sum_{t=1}^{s}
          i_{k,t}b_{n-k,s-t}.
\]

Thus the exact inversion used by the implementation is

\[
 i_{n,s}=b_{n,s}-
 \sum_{k=1}^{n-1}\sum_{t=1}^{s-1}
          i_{k,t}b_{n-k,s-t}.
\]

The geometric cut count and this independent integer inversion are compared
for every returned coefficient.  A disagreement raises an assertion rather
than returning a possibly self-consistent but misclassified dictionary.

## Span caps

`enumerate_bridge_spans(max_n, max_span=S)` returns coefficients with terminal
span at most `S`.  This is a cap on each enumerated bridge or irreducible
piece's own span.  It is safe to prune a partial path as soon as its running
maximum exceeds `S`: the running maximum cannot decrease, and a valid bridge
must finish at that maximum.  The bivariate recurrence remains exact on the
cap because every positive-span factor in a concatenation with total span at
most `S` also has span at most `S`.

This distinction matters when an experiment selects a finite irreducible
dictionary by span.  The selected pieces are filtered by their own `s`, and
their freely concatenated generating function is `1/(1-I_S)`.  A total
bridge span is the sum of piece spans; it is not a replacement for the span
of each piece.  The API never labels an interrupted or partially enumerated
cap as exact: exceeding `max_seconds` raises `TimeoutError` without a result.

## Analytic span-one control

There is one span-one irreducible of length one, the edge `E`.  For every
`n\geq2`, there are exactly two: `E` followed by `n-1` vertical edges, all
north or all south.  A vertical run cannot contain a renewal point because
the later x coordinate remains equal to the current x coordinate.  Hence

\[
 i_{1,1}=1,\qquad i_{n,1}=2\ (n\geq2),
 \qquad
 I_1(z,u)=u\frac{z(1+z)}{1-z}.
\]

At `u=1`, the positive solution of `I_1(z,1)=1` is `z=\sqrt2-1`, giving the
classical control lower bound `\mu\geq1+\sqrt2`.  This identity is a
predefined analytic family, not a fit to a finite coefficient table.

## Small exact replay

The implementation was cross-checked against `src.bridges.enumerate_bridges`
and the independent word-level geometry through `n=10`.  The ordinary totals
are

\[
 b_n=(1,1,3,7,17,41,101,251,631,1591,4029),
\]

where the first entry is `b_0`, and

\[
 i_n=(0,1,2,2,2,2,4,10,26,56,118).
\]

For example, the bridge span rows at lengths 1, 2, and 3 are respectively
`{1:1}`, `{1:2, 2:1}`, and `{1:2, 2:4, 3:1}`.  The corresponding
irreducible rows are `{1:1}`, `{1:2}`, and `{1:2}`.  All entries are exact
nonnegative integers; displayed runtimes are performance metadata only and
are not part of the mathematical claim.
