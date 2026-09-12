# Self-Avoiding Walk Lab

A reproducible research companion to **Non-D-finiteness of irreducible
NE-prudent ramps**, maintained by [Njakasoa](https://github.com/Njakasoa).

**Status: internally reviewed research manuscript. Publication priority is
UNRESOLVED. No external peer review or journal/preprint submission is claimed.**

## Result and scope

For the NE-prudent-ramp and hook-ramp series P and H defined by
[Bacher and Beaton (2014)](https://doi.org/10.46298/dmtcs.2445), the manuscript
proves that the irreducible-ramp generating function

```text
J(t) = (P(t) - H(t)) / (1 + P(t))
```

is not D-finite. The proposed contribution is the infinite noncancellation
argument: a uniform Gamma-product limit and exact integral-sign certificates
produce infinitely many genuine poles of J accumulating at sqrt(2)-1.
The published kernel formulas and meromorphic continuation are cited inputs.

The result concerns J. It does not establish non-D-finiteness of the further
weakly prudent bridge series W, an exact square-lattice connective constant,
or a new record bound. An internal review is not an external priority verdict.

- [Manuscript PDF — 11 pages](publication/main.pdf)
- [LaTeX source](publication/main.tex) and [reproduction guide](publication/VALIDATION.md)
- [Contribution review](publication/CONTRIBUTION_REVIEW.md) and [priority audit](publication/PRIORITY_AUDIT.md)
- [M3 acceptance](M3_ACCEPTANCE.md), [M4 acceptance](M4_ACCEPTANCE.md), and [independent manuscript review](results/m4-astra-review.md)
- [Next research steps](RESEARCH_ROADMAP.md)

![Critical phase functions](publication/figures/critical_phase.png)

The plot illustrates the limiting functions. The proof uses exact interval
enclosures and the separately reviewed uniform-convergence argument.

## Reproduce

Use Python 3.12 from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r publication/requirements-lock.txt
.venv/bin/python scripts/check_public_snapshot.py
.venv/bin/python -m pytest -q
.venv/bin/python publication/reproduce.py
```

The focused publication command checks the frozen source manifest, replays
two independent symbolic implementations and the exact limiting-integral
certificate, verifies five finite pole brackets and geometric coefficients
through length 12, then regenerates the figure. It needs no account or API key.
Python -O is rejected because it would disable checker assertions.

The original lab's final full suite passed **54 tests**. A second isolated
copy reproduced the publication calculations and byte-identical figures;
source tampering and disabled assertions were rejected. The analytical
infinite-pole proof remains a mathematical argument, not a proof-assistant
formalization. The programs alone do not prove its convergence theorem.

For a local PDF build, install Tectonic as documented in
[TOOLCHAIN.json](publication/TOOLCHAIN.json), then run:

```sh
.venv/bin/python publication/reproduce.py --pdf --tectonic /path/to/tectonic
```

## Public snapshot and provenance

This public repository starts from a curated snapshot. The original lab's
private Git history, operational settings, session notes and third-party
paper copies are excluded. `SOURCE_MANIFEST.json` records the exported file
hashes and the original source revision. Historical experiment receipts are
retained unchanged: their source commit IDs and machine paths describe the
original lab and are not resolvable Git history in this public snapshot.

Use `publication/reproduce.py` for the portable M4 reproduction gate.
Older historical receipt checkers that call `git show` require the original
history and, in some cases, separately downloaded source papers. New local
experiments can freeze their own source commits and create fresh receipts.
The generated `publication/VALIDATION.json` is intentionally excluded from
the public snapshot manifest because each replay replaces it.

## License and citation

Project code: [MIT](LICENSE). Manuscript/figure rights and third-party scope:
[RIGHTS.md](publication/RIGHTS.md). Citation metadata: [CITATION.cff](CITATION.cff).
No DOI, arXiv identifier or external reviewer endorsement is invented.
