# Optimized exact enumerator

`src/optimized_enumerator.cpp` computes the rooted, oriented square-lattice
self-avoiding-walk counts `c_0, ..., c_N` as exact integers.  It fixes the
first edge to `+x`, enumerates that one representative, and multiplies every
positive-length coefficient by four.  The four choices are related by lattice
rotations, while the reported object still counts all orientations separately.

## Occupancy and boundary invariant

The depth-first search stores occupancy in a packed `uint64_t` bitset.  A cell
at board index `y * side + x` is represented by one bit; setting and clearing
that bit is the only mutation used by collision tests.  For a requested
maximum length `N`, the board has side `2N+3`, with the root at
`(N+1,N+1)`.  Every prefix of length at most `N` has both coordinates in
`[-N,N]` relative to the root, so at least one unused border cell remains on
every side.  Thus a
neighbor outside the allocated board cannot occur for a valid continuation;
the explicit bounds checks are still retained.

The non-backtracking bound `c_N <= 4 * 3^(N-1)` holds for `N >= 1`.  At
`N <= 80`, its value is strictly below the maximum of `unsigned __int128`, so
every increment and the final factor four are exact under the documented cap.

## Optional small exact memoization

`--memo-small` enables the memoized path and is capped at N <= 12.
`--memo` is accepted as an alias.  The default path remains the direct packed
bitset DFS; this is the production path because the small-state memo key and
continuation vectors add work and memory, and the memo mode is intentionally
limited to small checks.

For a current endpoint `e`, let `S` be the complete set of occupied vertices
of the current walk, including `e`.  The memo key is

\[
  (r,\;\operatorname{canon}_{D_4}(S-e)),
\]

where `r = N - depth` is the remaining length.  `S-e` translates the whole
occupied set so that the endpoint is `(0,0)`.  The implementation
applies all eight rotations/reflections in (D_4), sorts the transformed
coordinates, and stores the lexicographically least list.  The key contains
the full occupied set, rather than only the endpoint, depth, or the traversal
order.

The value stored for a key is a vector `V[0], ..., V[r]`, where `V[j]` is the
exact number of valid continuations of exactly `j` additional edges.
The invariant is

\[
  V[0]=1,\qquad
  V[j]=\sum_{u\notin S,\;u\sim e} V_{S\cup\{u\},u}[j-1].
\]

The child state is marked in the same packed bitset before its recursive call
and cleared after it returns.  Therefore every summand tests precisely the
current occupied set.  At the initial fixed `+x` state, its vector is copied
to coefficients `c_(1+j)`, followed by the usual factor four.

The quotient is sound because translating or applying an element of `D_4`
is a bijection of the square lattice and preserves adjacency and distinctness.
For a fixed endpoint, all future validity tests refer only to whether a
candidate neighbor belongs to the occupied set; the order in which the set
was reached has no further effect.  The remaining length `r` is part of the
key because the same occupied geometry has different continuation vectors at
different truncation depths.  These facts prove that a memo hit returns the
same vector as a fresh recursive enumeration.

The finite board does not invalidate this quotient.  A state at depth `d` is
only queried for continuations through depth `d + j <= N`; its endpoint and
every such future vertex remain at least one cell inside the allocated border.
Consequently the continuation count depends on the translated occupied set,
not on its absolute board location.

For a reproducible local sanity check:

```text
g++ -std=c++20 -O3 -DNDEBUG src/optimized_enumerator.cpp -o saw_enum
./saw_enum --json 12
./saw_enum --json --memo-small 12
```

Both commands emit

```text
[1,4,12,36,100,284,780,2172,5916,16268,44100,120292,324932]
```

On the development machine, the direct bitset path completed the `N=20`
run in about 1.35 seconds; the `N=12` memo run was about 0.05 seconds and
used about 16 MB resident memory, while the direct `N=12` run rounded below
0.01 seconds and used about 4 MB.  Timings are machine-dependent, but they
justify keeping memoization explicit and opt-in.
