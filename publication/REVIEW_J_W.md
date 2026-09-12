# Reading guide for external review: J and W

Prepared 12 September 2026. Status: **review packet prepared; no external
review requested or received**. Publication priority is **UNRESOLVED**.
This guide begins the next editorial stage after the internally accepted W
proof. It does not record an external endorsement or a new theorem.

## Exact scope and reading order

The model is that of [Bacher–Beaton (2014)](https://doi.org/10.46298/dmtcs.2445),
two-sided weakly prudent self-avoiding bridges. It is not the unrestricted
square-lattice walk model or the different weakly directed model.

1. Read [normalization](../NORMALIZATION.md) and the published BB formulas.
2. Read the [J manuscript PDF](main.pdf), with [LaTeX source](main.tex).
   This 11-page manuscript proves non-D-finiteness of irreducible NE-prudent
   ramps J=(P-H)/(1+P), including the critical product and uniform moment
   argument used by the W extension.
3. Read the [W extension](../proofs/W_NON_DFINITE.md) and independent
   [directed-ramp lemma](../proofs/W_DIRECTED_RAMPS.md). The extension proves
   non-D-finiteness of W=I/(1-I), I=4J-2D_I-t, by its own denominator zeros.
4. Consult the [W evidence map](../W_ACCEPTANCE.md),
   [analytic review](../proofs/W_ASTRA_REVIEW.md),
   [final integration review](../results/w-final-review.md), and
   [finite exploration](../proofs/W_PHASE_EXPLORATION.md).

The J manuscript has not yet been rewritten as a combined J/W article.
The complete W proof currently lives in the linked supplement.

## Questions requiring mathematical review

| Point | Check required |
| --- | --- |
| Source transcription | P, H, J, D_I and W must match BB2014 with the same bridge orientation and irreducibility convention. |
| Critical crossing | Check the exact moment regularization, Gamma-product normalization, integrable crossing bound and uniform exponential tail in the J proof. |
| New W sector | At phase [4/5,9/10], a and b lie in the same integer interval. Check every Gamma argument, reflection sign and phase-uniform bound; the post-crossing amplitude is negative. |
| Directed-ramp series | Verify positivity below sigma, normal convergence in complex neighborhoods, critical harmonic divergence and uniform D_I->1 on the approaching phase families. |
| Sign certificate | Check the outward interval engine, four integral enclosures, endpoint F_0 signs and the uniform negative bound on 1+P_0. |
| Actual W poles | Check holomorphy of I at the selected F zeros, numerator noncancellation, disjoint bands and continuation from the original W germ. |
| D-finite obstruction | Check that the infinite pole family belongs to that germ's continuation and contradicts a polynomial-coefficient linear ODE. |

For each point, a useful review outcome is either a justified acceptance or
a specific gap with its location and the additional lemma required. Numerical
agreement alone cannot resolve a uniform-limit or continuation objection.

## Reproduction and known limits

From a public clone with the documented Python dependencies:

```sh
.venv/bin/python scripts/check_public_snapshot.py
.venv/bin/python publication/reproduce.py
.venv/bin/python publication/reproduce_w.py
.venv/bin/python -m pytest -q
```

The original research history is private; historical commit IDs need not
resolve in the public snapshot. These portable replay commands do not use
that history or redistributed third-party PDFs. Root SOURCE_MANIFEST.json
checks exported bytes, not scientific correctness or authorship.

The finite W data retain negative F(0.8) at N=8,16 and positive values at
N=32,64. Setting D_I=1 prematurely changes the finite signs. The proof gives
eventual poles, without an effective first index, simplicity or residues.

## Priority and later research

The [W-specific checkpoint](../references/W_PRIORITY_NOTE.md) and
[earlier priority audit](../references/M3_NON_DFINITE_PRIORITY.md) document
bounded searches and distinguish the weakly prudent and weakly directed
models. A broader citation/version audit remains necessary. The 2015 author
slides still label W non-D-finiteness as a conjecture; that fact does not
establish priority for this dossier.

After the proof audit, the next quantitative research target is an explicit
uniform remainder incorporating the directed-ramp term, leading to a
certified first phase index N_0. Root simplicity and residues need additional
derivative estimates. The current proof does not already provide these.
