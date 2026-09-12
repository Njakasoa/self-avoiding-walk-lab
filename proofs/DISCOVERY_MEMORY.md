# Finite-memory model family and target discipline

A target specifies lattice, domain, rational nonnegative directional step weights,
and a set of forbidden direction words. The plane uses translation-invariant
square or triangular adjacency in integer coordinates. A strip retains absolute
y in 0…W−1 and translates only x. Initial states include every possible starting
row. All actual target SAWs have an accepted length-m suffix, then extend only
without revisiting that suffix and without adding a forbidden word. Thus the
finite-memory language contains all target SAWs. It may contain longer cycles.

Only lattice automorphisms preserving weights, domain and the forbidden-word set
can identify states. The code enumerates D4 (square) or D6 (triangular) and tests
each action. For strips, affine y-reflection is allowed only when the linear
part respects the coordinate axes and its weights/motifs. Taking one canonical
representative preserves continuation multiplicities because extension and
transformation commute. Each direction contributes its exact rational weight.

An explicit D4 request that fails these conditions raises an error. The auto
mode chooses the stabilizer; it does not silently use an invalid eightfold
quotient for anisotropic data. The entire ordered suffix, not just its occupied
set, is retained because remembering which vertex is removed next is essential.

A bound for a strip target or motif-restricted target is NOT automatically an
upper bound for all planar square SAWs. Results carry the full target, and
comparison must match targets. Width parameters on the plane and words longer
than m+1 are rejected. A cap exception never returns an incomplete certified
matrix. Empty complete state space implies no walks of length m and hence zero
asymptotic rate for that target.

For rational nonnegative A, choose q clearing denominators, B=qA and s=max row
sum(B). The vector v=(B+sI)^k1 is strictly positive if s>0; if B=0 use v=1.
Return U=max_i (Bv)_i/(q v_i). Exact comparison proves Av≤Uv and bounds the
exponential continuation rate. This works for reducible matrices and dead states.
No eigenvalue floating approximation is needed for certification.

Uniform scaling of all weights scales B and s together up to the denominator
convention. Therefore it scales v by a common factor and scales U exactly.
However neither this certificate nor a finite iteration's chosen vector is
claimed log-convex in log-weights merely because the TRUE connective constant
has that property. Finite-iteration certificate monotonicity also requires its
own argument; tests distinguish structural facts from heuristic output behavior.

This family uses known finite-memory inclusion, symmetry and Collatz bounds.
Its correctness alone is not evidence of new mathematical priority.
