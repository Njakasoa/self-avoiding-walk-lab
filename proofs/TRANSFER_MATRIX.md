# Naive occupation-state transfer matrix

This M1 implementation is a small exact baseline for a finite square-lattice
rectangle.  It is intentionally independent of the recursive reference
enumerator so that agreement is a useful implementation check.

The allowed vertices are

\[
 R_{w,h}=\{(x,y):0\le x<w,\;0\le y<h\},
\]

with root `(0, 0)`, the lower-left corner.  `width` and `height` count
vertices.  Walks are rooted and oriented; no rotation or reflection quotient
is taken.  The public API is:

```python
from src.transfer_matrix import transfer_counts

transfer_counts(width, height, max_n)  # [c_0, ..., c_max_n]
```

All returned entries are exact Python integers.  The same rectangle is
available for independent DFS comparison as
`src.reference_enumerator.rectangle_counts(width, height, max_n)`.

## State and transition

Number a vertex `(x, y)` by `i = y * width + x`.  A layer-`n` state is

\[
  (M,e),
\]

where `M` is the bitmask of all vertices visited by the walk prefix and `e`
is the endpoint index.  The initial dictionary is

\[
  D_0[(\{0\},0)] = 1.
\]

For every state `(M,e)` and every lattice neighbor `q` of `e` in the
rectangle, the transfer emits

\[
  (M\cup\{q\},q)
\]

exactly when bit `q` is absent from `M`.  Destination multiplicities are
added in a dictionary.  The count at length `n` is the sum of all values in
`D_n`.  If the dictionary becomes empty, the remaining requested entries are
zero.  A simple walk has at most `width * height - 1` edges, so this must
happen by that length.

## Correctness invariant

For every `n`, the dictionary invariant is:

> `D_n[(M,e)]` equals the number of rooted oriented length-`n` self-avoiding
> walks in `R_{w,h}` whose occupied vertex set is exactly `M` and whose
> endpoint is `e`.

The invariant holds at `n=0` because the only length-zero walk is the root.
Assume it holds at `n`.  Every valid one-edge extension chooses a neighbor of
`e`; it is valid exactly when that neighbor's bit is absent from `M`.  The
transition therefore creates every valid length-`n+1` walk, and no invalid
walk.  Removing the final vertex from any length-`n+1` walk recovers a unique
length-`n` prefix, so the predecessor/extension construction is bijective.
Adding multiplicities for equal destination states preserves the invariant.
Summing the dictionary gives the exact number of walks at that length.

This is an **EXACT INTEGER** finite-box computation.  A finite rectangle
does not provide an infinite-lattice connective-constant bound: the state
space is finite because the box is finite, and no asymptotic statement about
the unrestricted square lattice is inferred from these counts.

## Scope and limitation

The implementation retains the complete occupied mask.  It is therefore a
naive occupation-state transfer matrix, not a frontier transfer matrix.  It
does not implement connectivity labels, component partition states, or a
topological transfer matrix, and it makes no claim of frontier asymptotic
efficiency.  The complete mask is useful here because its self-avoidance
invariant is direct and independently checkable.

For a small comparison run:

```text
PYTHONPATH=. .venv/bin/python - <<'PY'
from src.reference_enumerator import rectangle_counts
from src.transfer_matrix import transfer_counts

for width in range(1, 6):
    for height in range(1, 6):
        assert rectangle_counts(width, height, 8) == transfer_counts(width, height, 8)
print("finite-box reference/TM check passed")
PY
```

The dimensions, root, boundary convention, and length cap are part of every
reported finite-box experiment.  Inputs must be positive integers for
`width` and `height`, and a nonnegative integer for `max_n`; booleans and
negative values are rejected.
