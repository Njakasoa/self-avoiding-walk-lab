# CLAIM-0004 — Certified local bounds from the NEXT sweeps

The square, unrestricted, unweighted model satisfies

    2.553899 <= mu_square <= 2.711253.

These displayed decimals are rounded outward from exact rational certificates.
The upper certificate uses memory11, D4 symmetry and983 equitable classes; the
full D4 graph has15037states. The lower certificate uses all directly enumerated
irreducible bridges of length≤18, with strict initial minimum and weak terminal
maximum. Concatenation is unique and self-avoiding.

Evidence: results/e1-compression-v1 and results/e2-spans-v1. Proofs are the
finite-memory inclusion/positive-vector inequality, AP=PB and bridge renewal
notes. proofs/check_discovery.py independently reconstructs E1 geometry and
checks the exact inequalities and bridge algebra; the test suite independently
enumerates bridge geometry through length8. Larger bridge enumeration uses
direct cuts cross-checked against exact bivariate inversion.

The weighted follow-up results/e3-weights-v1 independently reproduces all small
He Table1 SAW/SAT cases(1,2),(1,3),(1,4), and certifies memory3,5,7,9 at eight
rational ratios, including three held-out ratios. It uses D2 off isotropy and
D4 at isotropy. Axis values follow directly from straight walks; the positive
weight theorem is not applied there. The coefficient/certificate verifier also
independently rebuilds all48 small weighted matrices.

Validity: exact local certificates. Novelty: KNOWN_METHOD, neither frontier
records nor evidence of an exact square-lattice formula. Current literature
bounds are much tighter (see STATE_OF_THE_ART.md); comparisons here concern
local computational cost and reproducibility. No critical exponents inferred.
Publication priority: UNRESOLVED.
