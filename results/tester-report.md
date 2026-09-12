# Independent M1 tester report

This report records the adversarial checks requested for M1.  The tests use
coordinate direction-word exhaustion, a fixed-grid integer occupation mask,
unreduced path states, and an edge-subset connectivity transfer.  They do not
reuse the production recursion to generate the independent reference data.

## Provenance

The final worktree check used source revision
`61b85b141bb642cfff961025b1a75f0994080fad`; the worktree was dirty because
the M1 changes were still being integrated.  The independent test source has
SHA-256
`492f79d90985fb10ce216aa112cf8cd5dacde608f2cdec3fdb9b261b65b83ddf`, and
`data/A001411.txt` has SHA-256
`fcfb9abf684d364632e20e34447671ff671d85895c03fd3121aff850f776c8e9`.
The canonical enumeration receipt is
`results/m1-enumeration-v1/metadata.json` (source revision above, dirty flag
true, payload hash
`a8d6f66ab288eea5d712dce01fb32c0ca8a275aab516b8be4ac3307e5f84d65b`).  The
canonical honeycomb receipt is
`results/honeycomb-control-v1/metadata.json` (same source revision and dirty
flag, payload hash
`38315f687969377fccfe053de31b7eaa12869807ddfe6e845db2e0660ec620e`).

## Results

`PYTHONPATH=. .venv/bin/pytest -q` completed with `10 passed in 3.72s`.

The independent enumeration checks are:

* All direction words of lengths 1 through 8 were checked individually.
  The fixed-grid bitmask DFS independently counted every prefix through
  length 12.  Both sequences equal the supplied A001411 data, including
  `[1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100, 120292,
  324932]`.  The production reference enumerator agrees on the same prefix.
* The C++ executable was compiled with `g++ -std=c++20 -O3 -DNDEBUG` and
  independently run with `--json` at n=12, 14, 16, 18, and 20.  Every term
  through n=20 agrees with A001411; the external n=18 value is `124658732`
  and n=20 is `897697164`.  The n=18 run took 0.16 seconds and the n=20 run
  1.19 seconds on this host, with approximately 3.6 MiB maximum resident
  memory.  The pytest check also compiles and runs the program through n=12.

The bridge checks exhaust all valid direction words through n=10 and apply
the geometry directly: `x_i > 0` for every non-root vertex and a weak final
maximum `x_n = max_i x_i`.  The independently obtained bridge coefficients
are

```text
b = [1, 1, 3, 7, 17, 41, 101, 251, 631, 1591, 4029]
i = [0, 1, 2, 2, 2, 2, 4, 10, 26, 56, 118]
```

All span histograms agree with `src.bridges.enumerate_bridges`, and every
internal cut agrees with the translated-prefix/suffix definition of a
renewal point.  Formal inversion independently reproduces `i`.  The test
also verifies the rational root interval sign conditions and `lower = 1/hi`.
The path `(0,0),(1,0),(1,1),(1,2)` confirms that the terminal span may have
been reached before the endpoint; a path beginning with `(0,1)` is rejected
by the strict initial minimum.  The renewal example
`(0,0),(1,0),(1,1),(2,1)` has the expected internal cut at index 2.

For each memory m=1 through 8, an unreduced set of all length-m SAW suffixes
was generated independently and compared with the production state set and
with every D4 orbit.  The quotient state counts are

```text
m       1   2   3    4    5    6    7    8
states  1   2   5   13   36   98  272  740
```

Continuation rows are identical for every unreduced representative in an
orbit, including directional multiplicities.  The square-lattice return
parity check finds only odd backward distances for a possible return, which
explains the exact certificate plateaus m=1/2, m=3/4, and m=5/6.  Certificate
mutations with a too-small rational upper bound, zero vector, wrong vector
length, negative edge weight, or out-of-range destination are all rejected by
`check_certificate`.  The standalone frozen verifier also passes:

```text
PASS: frozen inputs, output hashes, complete automata, exact spectral inequalities, renewal algebra and root interval
Scope: bridge geometric count validity is checked independently by tests, not inferred from this algebra alone.
```

The honeycomb control was recomputed directly in
`Q[t]/(Phi_48)`, where `Phi_48 = t**16 - t**8 + 1`.  The pair and triple
remainders and `mu**4 - 4*mu**2 + 2` are all zero; changing the phase pair to
`t**20 + t**28` gives the nonzero remainder
`-t**13 + t**12 + t**5 - 2*t**4 + t**3`.  The positive embedding selects
`mu = sqrt(2 + sqrt(2))`.  This validates the local scalar identity and its
negative control only; it does not formalize the global honeycomb boundary
argument or transfer any honeycomb result to the square lattice.

For finite rectangles, `rectangle_counts` and the occupation-state transfer
agree for every width and height from 1 through 5, through a length cap two
past the vertex bound.  An independent edge-subset degree/component transfer
also agrees on 2x3, 3x2, 3x3, 1x1, 1x4, and 4x1, including the correct
degenerate tails.  For example, the 2x2 sequence is
`[1, 2, 2, 2, 0, 0]`.  These are exact finite-box counts with a lower-left
corner root and oriented walks; they are not an infinite-lattice connective
constant estimate.

## Input-contract finding

The initial independent test deliberately checked that negative values and
booleans are rejected uniformly.  It caught that `memory_automaton(True)` and
`enumerate_bridges(True)` were accepted through Python's `bool` subclass of
`int`, while the newer enumerator and transfer APIs rejected booleans.  The
root agent changed those two guards to require an actual `int`; the final run
above passes this check.  No count or certificate value changed as a result.

## Limits

The bridge geometry was independently exhausted only through n=10; n=12 was
used for the independent unrestricted SAW bitmask count.  The automaton test
checks m through 8 and the edge transfer retains all vertices, so it makes no
frontier-efficiency claim.  The C++ agreement validates exact enumerations at
the tested finite lengths, not the asymptotic connective constant.  The
honeycomb computation is a local exact algebra check, not a new proof or
novelty claim.
