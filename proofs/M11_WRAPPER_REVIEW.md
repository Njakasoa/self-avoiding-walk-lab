# Independent M11 wrapper and checker mechanism review

Verdict: PASS for source freezing and canonical execution of the reviewed
phase-derivative component package. No canonical run was created during
this review. The complete W denominator phase sign and index coverage
remain OPEN.

The wrapper validates the frozen M10 structural receipt before evaluating
the three M11 components. Its source list pins the three producers and
proof notes, the relevant M10 scalar/weight/product inputs, M5 real root
and phase inputs, M6 secant-product input, interval/receipt/provenance
code, M10 structural payload/metadata, and locked dependencies. The
structural receipt links the earlier directed and scalar certificates.
The payload preserves full_F_phase_sign='NOT PROVED' and explicit
component-only scope. Imported interval code and payload reject -O.

An independent wrapper payload replay reproduced these component hashes
using sorted indented JSON with a final newline:

| Component | SHA-256 |
|---|---|
| directed | 410b404d2c33eda504667dde823124fb918545e65b6272203877fd27b6971103 |
| weight | 5c480862089b150f1acecb11586937740dc9a2522c0ac4cb2f2d0b03ff4d1125 |
| smooth | 5cb292bc44e04c659297358f427859259ad94b0d6bf409468906b29fce329987 |

The first two agree with prior independent reviews; the third agrees with
the final independent smooth replay. Combined payload SHA-256:
4f0db5f348ab7ef9dced62274068df04173cce2d42276b339daf8f3cf23daa30.

The checker validates canonical provenance, compares the retained payload
with a fresh wrapper result, and pairs each scientific/code path with its
exact hash in the designated independent review table. Its explicit
optimization guard preserves the inherited receipt assertions. It also
requires the non-theorem scope marker and returns an open full-coverage
status. This is an appropriate integration mechanism; a matching review
hash is provenance evidence rather than machine verification of the proof.
The checker cannot be fully executed before the canonical receipt exists;
that release verification remains the integrating root's step.

| Reviewed source | SHA-256 |
|---|---|
| experiments/m11_phase_batch.py | 1a90f949f299c1c855ee0d07e58342c63b69c81e5dd1cf85a40731f31e36a5f5 |
| proofs/check_m11.py | e34a0f7485a424142597118635755e763adb349fe731f136e4da5d5841b27539 |

This review approves the mechanism and exact current wrapper. It does not
create a canonical receipt, freeze sources, or assert full F_N monotonicity.
