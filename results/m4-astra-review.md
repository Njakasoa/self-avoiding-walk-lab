# Independent Astra review of the M4 manuscript

Date: 2026-09-12. Review type: **internal AI scientific review**, not external
peer review. Publication priority: **UNRESOLVED**.

## Scope and verdict

The manuscript's analytic argument was independently re-read against the
candidate proof, the separate analytic and arithmetic reviews, and the locally
archived Bacher–Beaton paper. Prior acceptance was not used as a substitute for
checking the translated argument. No substantive analytic defect was found.
Final acceptance and the frozen manuscript hash are recorded below after the
writer's normalization and source-pole clarifications.

This review concerns non-D-finiteness of J=(P-H)/(1+P), using BB2014's exact
formulas and meromorphic continuation theorem. It establishes neither
non-D-finiteness of W nor a connective constant, priority, or external
publication readiness. Root owns compilation and source-frozen full replay;
this review is not a receipt for those operations.

## Scientific checks

1. BB2014 Propositions 14 and 16 match the manuscript's U, q, A, B, hook A,
   initial terms and product indexing. Equation (5) identifies the quotient
   with bridge-irreducible NE-prudent ramps, rather than r-irreducible ramps.
   The source uses vertical bridges and the endpoint-rightmost ramp condition.
   A requested explicit geometric paragraph prevents confusion with this
   repository's general horizontal-bridge normalization.
2. The kernel parameter t(eps) is analytic at zero; the crossing occurs at
   positive s*, away from the square-root endpoint. Analytic root locations
   give a'= -s*/eps²+O(1), a continuous uniform inverse phase family, and
   eta_eps=eta+O(eps). Both integer exclusions are uniform on [0.30,0.35].
3. The Gamma formulas exhaust n<=N and n>=N+1. In the first range the
   smallest b-n+1 tends to 1+theta-eta>0; in the second n-a>=1-theta>0.
   Reflection gives exactly sin(pi theta)/sin(pi(theta-eta)), without an
   extra parity sign. Gamma ratio estimates therefore remain uniform even
   at the nearest lattice sites to the crossing.
4. Positive divided differences are analytic near s*. Away from it the
   two-log formula and uniform g_eps convergence suffice, including s=0;
   no uniform derivative at the square-root endpoint is needed. The
   resulting continuous psi gives uniform partial Riemann sums.
5. The bound with exponent eta+nu<1 controls a crossing window absolutely
   by C(rho+eps)^(1-eta-nu). Thus no isolated crossing mass remains.
   For the infinite tail, fix a reference S0>s*+1: the exact recurrence
   gives a uniform bound C exp(-c(s-S0)), whose integral beyond R tends
   to zero as R tends to infinity. This also justifies the manuscript's
   tail truncation without relying on constants varying with R.
6. The h-zero regularization is an exact finite-parameter divided
   difference. Its denominator and the remaining rational factors are
   uniformly separated from zero. Boundary terms tend to -d and -3,
   Q/eps tends to K, and the V1,V2 formulas agree with f(u*)=1.
7. The raw profile has the required logarithmic derivative and normalized
   value at u=1. Smooth continuation of the nonsingular factor fixes the
   relative amplitude; the reflected Gamma multiplier supplies the sole
   sign change. The Jacobian phi'/phi is positive on (sigma,1).
   At sigma the density behaves as (u-sigma)^(1+sqrt(2)), at 1 it vanishes,
   and at u* its exponent is -eta>-1. All four integrals converge.
8. The displayed dyadic intervals agree with the independently audited
   critical integral output. The bundled critical checker differs from
   the audited checker only in its import path; its interval arithmetic
   module is byte-identical to the original. The analytic convergence proof
   and the arithmetic enclosure are separate premises, both accounted for.
9. B'(theta)>0 and the positive post moment promote the hook endpoint
   margin to the entire phase interval. Uniform convergence preserves the
   strict endpoint signs of P+1 and the hook margin for every sufficiently
   large N. The disjoint intervals give distinct zeros of P+1. Analyticity
   makes each zero finite-order (the endpoint signs exclude identically
   zero); a nonzero -1-H makes it a genuine pole of J. Infinitely many
   finite-plane poles contradict a polynomial-coefficient linear ODE.
   Neither root simplicity nor an effective first N is needed.

## Reproduction guard found and corrected

The original reproduction entry point could emit PASS under Python -O or
PYTHONOPTIMIZE while its assertion-based sign, identity, equality and count
checks were skipped. Root added an early `if not __debug__` failure in main.
I ran `.venv/bin/python -O publication/reproduce.py --no-figures` afterward:
exit status 1, with `RuntimeError: Run without -O: the proof checkers require
assertions`, before any certificate computation. Under normal Python the
returned check dictionaries are protected by assertions; the script's PASS
is explicitly limited to computational replay, not a formal analytic proof.
No further material false-PASS branch was found in this scan.

## Provenance

Base HEAD observed: `dbf8e6539817289732735a7c103b7a4b8fc64676`.
Reviewed supporting SHA-256 values:

- Candidate proof: `e184726e834116e8eaf9d83926e571f40f4f2883eda1114b05c231872ec0a627`.
- M3 analytic review: `21ec2f2166984901705bf57abebb326c33494376cec55bdfcfb44d76021aea30`.
- Quadrature audit: `317de851cd827fb1b7dbc95e9c3d6afee5753ae5da67fed92bf3aae83b5afc7d`.
- Local BB2014 text: `d9dfa12998b29a5e19fe1cb021f352debe3656a4e5a9a78767e2f29d60b1d865`.
- Bundled critical checker: `9e5c593b76a41435315be6d0f1e163fcd082a2c88b4cff0f0aaad67a23f0f2c5`.
- Bundled expected integral JSON: `060d525c2dcbe4051ae29d9e9d5dd90a6bfba862b5274e6703084823970c0c23`.
- Reproduction entry point after -O guard: `82446050879ccf56b2b8b0e1843a340d8e21af39803178b33f22a505548d5f8c`.

## Final manuscript decision

**ACCEPTED for the internal mathematical-draft gate**, conditional on the cited
BB2014 formulas and continuation theorem and the separately audited exact
integral certificate. The writer added explicit rooted, nonempty ramp
geometry, bridge irreducibility, and no symmetry quotient; the definition
now includes prudence as well as the NE boundary condition. The explicit
source-pole characterization h(u_n)=0 links the phase exclusions to
Theorem 17. The displayed profile ODE now references both the smooth and
Gamma limits, and the substituted integral exponent is correctly stated as
strictly positive. All requested scientific clarification is present.

Final reviewed manuscript `publication/main.tex` SHA-256:
`d020e1c1d58e08bc642e74d7da5a1f02df33eb42defcfd6053d1a7bf250fd0e0`.
Reviewed `publication/references.bib` SHA-256:
`c16c58db8fcddd550c6a334efcea309352a268b456552de4622f37def33b7eed`.
Any subsequent mathematical manuscript change requires reviewing the changed
text; a new hash alone is not acceptance. Full package replay, PDF build,
and output hashes are separate root-owned receipts. Novelty and publication
priority remain **UNRESOLVED**, and this is **internal AI review only**.
