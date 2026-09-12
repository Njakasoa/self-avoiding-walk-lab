# Validation and reproduction

This directory is a standalone local publication candidate. Priority is
UNRESOLVED. No external submission or peer review has occurred.

Install the pinned Python environment from requirements-lock.txt. Then run:

```text
python reproduce.py
```

This checks the source manifest, recomputes the exact integral certificate,
checks rational identities in two independent implementations, verifies five
finite singularity brackets, reproduces geometric coefficients through12,
and regenerates the scientific figure. The critical integral checker itself
uses only Python's standard library:

```text
python proof-checkers/critical_integrals.py
```

The full manuscript can additionally be compiled locally with Tectonic0.17.0:

```text
python reproduce.py --pdf --tectonic /path/to/tectonic
```

The compiler may download standard TeX resources on its first run. It compiles
locally; it does not upload the manuscript. Subsequent runs use the local
cache. The compiler archive provenance is recorded in TOOLCHAIN.json.

VALIDATION.json is generated only after all requested stages pass. A missing
compiler is an error when --pdf is requested. The source manifest covers the
manuscript, bibliographic inputs, checker sources, expected certificate and
reproduction code. Generated figures and PDF have their hashes recorded in
VALIDATION.json. The checked dyadic integral payload is byte-for-byte the
mathematical record frozen in the research repository at source dbf8e65;
PROVENANCE.json documents the sole local-import adaptation of its checker.

Historical producer text in expected-integrals.json says that the computation
alone does not prove scaling convergence. The analytic convergence proof is
provided separately in the manuscript and ANALYTIC_REVIEW.md. Neither the
replay command nor its green status is presented as a formal verification of
all real/complex analysis.

The exact signs are conservatively:

- 1+P_0(0.30) lies between -0.193 and -0.166.
- 1+P_0(0.35) lies between0.163 and0.192.
- 1+H_0(theta)>0.310 on the whole phase interval[0.30,0.35].

The last statement combines an exact endpoint enclosure with the proved
monotonicity of B(theta) and positivity of the post integral. Uniform
convergence in the manuscript transfers these margins to all sufficiently
large phase intervals. No effective first index is claimed.

QUADRATURE_REVIEW.md records an independent density/substitution audit,
repeated exact run and separate high-precision integration. ANALYTIC_REVIEW.md
records the independent attack on all limiting arguments. These are internal
AI-assisted research reviews, not external journal acceptance.
