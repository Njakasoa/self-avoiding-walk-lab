# Exact equitable compression (known construction)

This document specifies the E1 compression helper in `src/equitable.py`.
The construction is standard weighted equitable partition refinement.  It is
included to make the finite-memory certificate transfer auditable; it is a
known method and carries no novelty claim.

## Input and API

An automaton with `n` states is represented by sparse rows

```python
rows[i] = {j: weight, ...}
```

where `i` and `j` are state indices in `0, ..., n-1`.  A transition with a
repeated directional choice is represented by an integer multiplicity.  A
weighted experiment may use an exact nonnegative `fractions.Fraction`.  Bool,
float, negative, and out-of-range values are rejected; no floating conversion
is used.

The public functions are:

```python
equitable_partition(rows) -> list[int]
quotient(rows, mapping) -> list[dict[int, int | Fraction]]
verify_equitable(rows, mapping, quotient_rows) -> bool
lift_vector(mapping, vector) -> list[int | Fraction]
```

`mapping[i]` is the block containing state `i`.  Block IDs are canonical and
must be exactly `0, ..., r-1`.  `equitable_partition` starts with one block
and repeatedly refines each old block by the sparse signature

\[
  \sigma(i) = \left(\sum_{j\in C_b} A_{ij}\right)_{b=0}^{r-1}.
\]

Missing coordinates are zero and are not materialized.  Existing block order
is retained, and distinct signatures within one old block are ordered
lexicographically.  The result is therefore deterministic.  Refinement is
complete when all states in one block have the same signature.  `quotient`
uses one representative only after checking that this condition holds for
every state; it raises `ValueError` on a non-equitable mapping rather than
silently producing an unsound matrix.  `verify_equitable` performs the same
check against supplied quotient rows and returns `False` for malformed input.

## Exact matrix relation

Let `A` be the `n` by `n` matrix represented by `rows`, let `r` be the number
of blocks, and define the block-incidence matrix

\[
  P_{ia}=\begin{cases}1&i\in C_a,\\0&\text{otherwise.}\end{cases}
\]

For an equitable mapping, define the quotient `B` by

\[
  B_{ab}=\sum_{j\in C_b} A_{ij}\qquad (i\in C_a).
\]

The value is independent of the selected `i` by equitability.  Entrywise,

\[
 (AP)_{ib}=\sum_{j\in C_b}A_{ij}=B_{ab}=(PB)_{ib},
\]

so the exact identity is

\[
                         AP=PB.                 \tag{1}
\]

No transition direction is discarded: all entries with the same destination
block are added, including directional multiplicity.  The sparse quotient
has at most one entry per nonzero destination block.

Multiplying (1) repeatedly gives

\[
                         A^kP=PB^k\quad(k\ge 0).                 \tag{2}
\]

`lift_vector(mapping, vector)` is exactly `P @ vector`.  Consequently every
quotient continuation agrees with its lifted full-state continuation:

\[
 A^k\,\operatorname{lift}(v)
   = A^kPv
   = PB^kv
   = \operatorname{lift}(B^kv).                 \tag{3}
\]

This is an equality for every `k`, not a finite sample or a numerical test.

## Transfer of a rational upper certificate

Suppose `v` has strictly positive rational entries and `U=p/q` with `q>0`.
An exact quotient certificate checks

\[
                         qBv\le pv.              \tag{4}
\]

The lifted vector `w=Pv` is also strictly positive.  Applying `P` to (4) and
using (1) gives

\[
                         Aw=PBv\le U,Pv=Uw.
\]

Because `A` is nonnegative, induction gives

\[
                         A^kw\le U^kw.            \tag{5}
\]

For example, with `c=max_i(1/w_i)`, the all-ones vector satisfies
`1 <= c w`, hence `A^k 1 <= c U^k w`.  Every row-sum growth rate, and thus the
spectral-radius upper bound, is at most `U`.  The implementation and any
independent verifier should retain (4) as integer cross-multiplication; a
decimal eigenvalue is not a certificate.

## Spectral radius and row-sum growth

The quotient does not merely provide an upper bound: its spectral radius is
exactly the full matrix spectral radius, including reducible and dead-end
cases.  Since `P @ 1_r = 1_n`, (2) with the all-ones vector gives

\[
                         A^k1_n=P B^k1_r.         \tag{6}
\]

Thus row sums of `A^k` are constant within each block and equal to the
corresponding quotient row sums.  For a nonnegative matrix, the induced
infinity norm is the maximum row sum, so

\[
                         \lVert A^k\rVert_\infty
                         =\lVert B^k\rVert_\infty.
\]

The Gelfand formula then yields `rho(A) = rho(B)` by taking `k`th roots and
the limit.  This argument uses no irreducibility assumption and remains valid
when some rows are zero.

## Refinement and resource limits

Let `P_0` be the one-block partition and let `P_{t+1}` split a block by its
signature against `P_t`.  A partition `Q` that is equitable and refines
`P_t` also refines `P_{t+1}`: each `P_t` block is a union of `Q` blocks, so the
sum into each `P_t` block is determined by the equal sums into `Q` blocks.
Induction shows that every equitable refinement of `P_0` refines every `P_t`.
Once the finite sequence stabilizes, its limit is therefore the coarsest
stable equitable refinement generated by these signatures.  This is weighted
directed colour refinement, not an unproved claim about labelled language
minimization.

Rows and signatures remain sparse.  For `n` states and `E` stored row entries,
one refinement round uses `O(n+E)` working storage plus sparse signatures and
does not allocate a dense `n` by `n` array.  Sorting a row's at most `d` block
keys costs `O(d log d)` in that round; there can be at most `n-1` proper
splitting rounds.  The intended E1 budget is at most 100,000 states; runtime
still depends on the number of refinement rounds and stored transitions.

The method preserves weighted row behaviour.  It does not preserve arbitrary
transition labels, initial/final acceptance annotations, or a deterministic
labelled language, so it must not be presented as DFA minimization.  Any
symmetry quotient used before this helper remains a separate, explicitly
validated construction.

## Small exact self-check

This check exercises a nontrivial partition, rational lifting, the exact
`AP=PB` relation, and all continuation lengths in a short range:

```text
PYTHONPATH=. .venv/bin/python - <<'PY'
from fractions import Fraction

from src.equitable import (
    equitable_partition, lift_vector, quotient, verify_equitable,
)

rows = [{0: 1, 1: 1}, {0: 1, 1: 1}, {2: 2, 3: 1}, {2: 2, 3: 1}]
mapping = equitable_partition(rows)
assert mapping == [0, 0, 1, 1]
qrows = quotient(rows, mapping)
assert qrows == [{0: 2}, {1: 3}]
assert verify_equitable(rows, mapping, qrows)

def multiply(matrix, vector):
    return [sum(weight * vector[j] for j, weight in row.items())
            for row in matrix]

full = lift_vector(mapping, [Fraction(3, 2), Fraction(5, 4)])
reduced = [Fraction(3, 2), Fraction(5, 4)]
for _ in range(8):
    assert multiply(rows, full) == lift_vector(mapping, multiply(qrows, reduced))
    full = multiply(rows, full)
    reduced = multiply(qrows, reduced)
print("equitable compression self-check passed")
PY
```

This only checks the displayed finite example.  It is not a novelty result or
an independent proof of any particular finite-memory state generator.
