# Discovery engine: supported targets and reproduction

Run from the repository root with `PYTHONPATH=. .venv/bin/python -m
src.discovery_engine examples/discovery/memory.json`. The public CLI starts an
isolated process and enforces the complete-case `max_seconds` limit. The Python
`run_case(config)` interface is useful for small programmatic cases; its internal
checks are cooperative. The experiment drivers also impose their documented
outer limits, except E2's depth-first enumeration which uses cooperative checks
and rejects a completed over-budget certificate.

## Parameter contract

| Parameter | Implemented variants | Scope |
|---|---|---|
| lattice | square, triangular | memory; bridges and rectangles are square only |
| boundary | plane, strip, rectangle | a boundary changes the target |
| state_representation | memory, equitable; connectivity for rectangle | equitable refinement preserves weighted outgoing multiplicities |
| memory | positive integer | ordered suffix, with a state cap |
| forbidden_words | finite direction-index words of length at most memory+1 | a motif restriction changes the target |
| weights | nonnegative exact rationals per direction | no floating-point input; ordinary anisotropy is `[x,y,x,y]` |
| bridge restrictions | max_n, max_span | restrictions on each irreducible piece, concatenations unbounded |
| width | positive strip width; rectangle width/height | rectangle baseline retains all vertices, not a production frontier algorithm |
| symmetry | none, auto, explicit d4 | only weight/domain/motif-preserving actions; invalid D4 requests fail |

Square directions are E,N,W,S. Triangular axial directions are
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1). Strip y coordinates remain absolute.
For strips the current automatic symmetry search conservatively requires
axis-preserving linear actions. It may miss additional triangular-strip
automorphisms; this affects compression efficiency, not inclusion or validity.

Unknown parameters and unsupported combinations raise errors. A resource limit
never supplies a partial certificate. The small rectangle interface is capped
at12vertices and length11 and returns exact finite counts with no claimed
infinite-lattice bound. Its baseline is independent DFS. Memory results include
the maximum-row-sum baseline, matrix size, transition count, rational vector,
timings, process peak RSS and full target. Bridge results include a rational
root interval and unit-bridge baseline; DFS state size is not a matrix size.

## Canonical experiments

Each driver refuses source bytes that differ from its recorded Git commit and
writes a new result directory containing payload, parameters, source hashes and
output hash. Do not reuse an existing result ID.

```sh
PYTHONPATH=. .venv/bin/python experiments/e1_compression.py e1-compression-v1
PYTHONPATH=. .venv/bin/python experiments/e2_spans.py e2-spans-v1
PYTHONPATH=. .venv/bin/python experiments/e3_weights.py e3-weights-v1
PYTHONPATH=. .venv/bin/python experiments/m2_variants.py m2-variants-v2
PYTHONPATH=. .venv/bin/python proofs/check_discovery.py results/e1-compression-v1 results/e2-spans-v1 results/e3-weights-v1 results/m2-variants-v2
PYTHONPATH=. .venv/bin/python -m pytest -q
```

The last checker rebuilds E1 geometry and all small He matrices without producer
imports, checks all exact inequalities, bivariate renewal algebra and receipts.
Independent small variant/bridge geometry is covered by the test suite. A root
interval alone does not independently prove the underlying bridge enumeration.

## Interpretation

For a specified positive weighted SAW target, a certified upper U implies
`log(mu) <= log(U)` for entropy/free energy per step and `z_c >= 1/U` for
critical fugacity. A positive lower L reverses the inequalities:
`log(mu) >= log(L)` and `z_c <= 1/L`. All reciprocal bounds can be kept rational;
logarithms are explanatory transformations, not new numerical certificates.
On the square axes, direct straight-walk enumeration gives mu(0,y)=y,
mu(x,0)=x. The positive-weight theorem is not invoked on an axis. A finite
power-iteration upper certificate can exceed this exact value. Neither finite
near-axis samples nor finite log-convexity tests prove a global limiting law.
No critical exponents are inferred.

Equitable compression changes certificate cost while preserving the spectral
radius. A smaller matrix is not a stronger automaton. Full graph construction
precedes compression, so compressed-size budgets and construction budgets are
reported separately. Runtime measurements are local observations, not universal
performance guarantees. See DISCOVERY_REPORT.md for the frozen outcomes and
the distinction between M2 engineering completion and scientific novelty.
