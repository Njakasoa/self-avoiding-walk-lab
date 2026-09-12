# Computational proof objects

`critical_integrals.py` and `intervals.py` require only Python's standard
library. They recompute exact outward dyadic enclosures of the four integrals
and the strict phase signs used by the theorem. The arithmetic uses integers,
integer square roots, alternating/Taylor remainder bounds, and enclosing
rectangle sums. No floating numerical quadrature is part of the certificate.

`moment_identities.py` and `independent_identities.py` independently check the
rational algebra using SymPy. `reference_counts.py` supplies the small
geometric control; `intervals.py` also checks five finite singularity brackets.
The infinite-index analytic proof is in main.tex; it is a human-readable
proof, not a claim of formal verification by these programs.

PROVENANCE.json identifies the reviewed repository sources and exact copying
adaptation. expected-integrals.json is the frozen payload from the source
commit dbf8e65. Reproduction checks for exact equality with this payload.
