# M4 acceptance — local publication candidate, 2026-09-12

**M3 and M4 completed at the requested internal research level.** M3 supplied
a surviving proof candidate for non-D-finiteness of irreducible NE-prudent
ramps. M4 now supplies its full standalone manuscript and reproducible
computational evidence. Publication priority is **UNRESOLVED**. No external
submission, researcher message, priority determination or peer review occurred.

The theorem is J=(P-H)/(1+P) non-D-finite, using the exact formulas and
meromorphic continuation of Bacher–Beaton (2014). M3_ACCEPTANCE.md and
claims/CLAIM-0006.md record its evidence and scope. It is not a result about
the further bridge quotient W or an exact square-lattice connective constant.

The requested publication directory contains main.tex, figures/, proof-checkers/,
reproduce.py, requirements-lock.txt, CONTRIBUTION_REVIEW.md and VALIDATION.md.
It additionally contains the compiled eleven-page main.pdf, bibliography,
primary literature audit, analytic and arithmetic reviews, source manifest,
toolchain provenance and generated VALIDATION.json.

Validation completed:

- Astra independently reviewed the full manuscript against the proof and
  primary paper, accepted its analytic argument, and recorded the exact
  manuscript hash in results/m4-astra-review.md.
- Luna copied the standalone dossier to /tmp and replayed both independent
  symbolic implementations, the exact integral certificate, geometric counts
  through length 12 and five finite pole certificates. All passed. Generated
  figures were byte-identical. Tampered sources and Python -O were rejected.
  See results/m4-independent-reproduction.md.
- Sources were frozen at 1de09edeac5ecea908d2ce7deccb9a1d2f03229b. The canonical
  results/m4-publication-v1 receipt reran the entire computation and compiled
  the PDF locally with Tectonic 0.17.0. Its input bytes match Git; output and
  manifest hashes match the delivered files.
- Root independently checked the receipt, reviewer hashes, eleven PDF pages
  and absence of unresolved references, then visually inspected pages 1, 2,
  3, 6 and 11. One 1.5039pt keyword-line overfull warning is visually harmless.
- The final full suite passed **54 tests in 10.16s**. The integrated receipt
  and PDF checks are recorded in results/m4-final-validation.json.

The computation certifies the limiting integral signs; the analytical
uniform-limit proof is supplied and reviewed separately. No software replay
is described as formal verification of the entire theorem. No effective
first phase index, uniqueness or simplicity of the constructed zeros is
claimed. These scope limits do not leave an unmet requirement of the user's
M3/M4 publication-candidate brief.
