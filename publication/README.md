# M4 publication candidate

This standalone dossier develops the non-D-finiteness proof for irreducible
NE-prudent ramps that passed the internal M3 review. Publication priority is
**UNRESOLVED**. The draft has not been externally peer reviewed or submitted.

Read `main.pdf` (compiled manuscript) or `main.tex` (complete source), then
`CONTRIBUTION_REVIEW.md` for scope and `VALIDATION.md` for reproduction.
The theorem concerns the series J=(P-H)/(1+P) from Bacher–Beaton (2014).

Install `requirements-lock.txt` in a Python environment and run
`python reproduce.py`. To compile the manuscript as well, run
`python reproduce.py --pdf --tectonic /path/to/tectonic`.
The exact integral checker uses only Python's standard library; the full
replay also uses SymPy and Matplotlib. See `TOOLCHAIN.json` for compiler
provenance and the review files for the independent analytical and arithmetic
checks. No program here is represented as a formal proof assistant.
