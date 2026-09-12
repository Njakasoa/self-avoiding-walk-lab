# M3 research checkpoint — 2026-09-12

> **Superseded by M3_ACCEPTANCE.md and CLAIM-0006.** The complete uniform
> critical-product proof now resolves the noncancellation obligation at the
> internal research-review level. The M4 publication candidate is in
> `publication/`. Priority remains UNRESOLVED. The historical checkpoint
> below records the earlier finite-only stage and its original evidence.

**M3 remains active. M4 has not started.** The selected target is
non-D-finiteness of the irreducible NE-prudent ramp generating function J.
Its decisive infinite noncancellation step remains unproved. Publication
priority is UNRESOLVED; no publication or external submission has occurred.

## What is established at this checkpoint

Using Bacher–Beaton's explicit formulas and meromorphic continuation theorem,
`proofs/M3_PRUDENT_INTERLACING.md` proves negative residues of P at every
specified real pole, hence at least one zero of 1+P in every intervening
interval. The proof handles the formerly missing signs of the preceding B
factors and proves local holomorphy of the infinite tail at each fixed pole.
Astra reviewed this argument. It is a deduction conditional on the cited
primary theorem; its novelty has not been established.

The exact interval checker certifies **five distinct poles of J**. Each of
five disjoint rational intervals has P(left)+1<0<P(right)+1, while H+1>0.36
throughout that interval. Integer arithmetic, outward dyadic rounding and an
explicit geometric tail bound certify every sign. Independent transcription,
geometric checks and Astra review found no error in this finite result.
Infinitely many zeros of 1+P do not suffice: cancellations by 1+H may still
occur in later intervals.

Supporting results are retained without novelty claims:

- An exact bivariate formula for span-two irreducible bridges, proved from
  ladder geometry and checked through length30 (H/V degrees through18).
- A direct age/deadline automaton with7,812 memory states at m=13. Exported
  matrices and integer vectors independently certify the local upper bound
  mu_square<=2.701375, rounded outward. This is a known-method local bound,
  much weaker than published frontier bounds; it is not a record.
- Generic H/V equitable partition constancy outside possible ratios
  {1/2,1,2}, plus an explicit memory9 counterexample to reconstructing the
  weighted partition from an isotropic class and last-step axis alone.

## Reproducible evidence

Scientific sources were frozen at `9c6dd75fdfe19e61337439bf6079ae2cda7a1c23`.
The four receipts are `results/m3-span-v1`, `results/m3-weights-v1`,
`results/m3-prudent-v1`, and `results/m3-deadline-v1`. Each records command,
parameters, source commit, input/output SHA-256, runtime and environment.
No historical M1/M2 receipt was modified.

The full suite passed **52 tests in9.87s**, with tested source bytes checked
against that commit in `results/m3-tests.json`. The fresh independent checker
reconstructs all13 deadline graphs and checks their exported inequalities,
expands the ladder rational expression by a different coefficient calculation,
checks3 weighted witnesses, and replays all5 interval certificates:

```text
PYTHONPATH=. .venv/bin/python proofs/check_m3.py
```

Its recorded output is `results/m3-checker-output.json`; the final review is
`results/m3-astra-review.md`. The prudent replay uses the reviewed exact
interval engine, rather than claiming a second independently written interval
implementation. Formula auditing, rational arithmetic spot checks and the
separate mpmath/geometric controls provide the additional independent checks.

## Next mathematical obligation

Find a proof that infinitely many of the interlacing zeros r_l satisfy
1+H(r_l)!=0, or disprove the proposed noncancellation behavior. A statement
for an infinite subsequence, or an eventually positive asymptotic limit at a
suitably chosen sequence of zeros, would suffice; positivity at every zero is
not required. No uniqueness of the interlacing zeros has been proved.

The concrete starting point is the positive-prefix/tail factorization in
`proofs/M3_PRUDENT_INTERLACING.md`. Seek a sign representation for H+1 at
P=-1 or an asymptotic comparison near sigma. Any numerical exploration must
remain separate from a uniform or subsequence theorem. If this obligation is
resolved, repeat independent proof scrutiny and the priority audit before
preparing the conditional M4 publication package. Until then CLAIM-0005 is
OPEN and the active goal is not marked complete.
