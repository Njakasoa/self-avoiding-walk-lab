# Independent Astra review of the W argument

Date: 2026-09-12. This is **internal AI mathematical review**, not external
peer review. Scientific priority and novelty remain **UNRESOLVED**.

## Verdict and scope

**ACCEPTED for the internal mathematical-draft gate**, conditional on the
cited BB2014 formulas and meromorphic-continuation theorem, and the reviewed
critical-product and interval-arithmetic foundations. No substantive gap was
found in the extension from the earlier moment theorem to the new phase
sector or in the construction of actual poles of W. This acceptance is for
the mathematical text whose hash appears below; subsequent mathematical
changes require review. It does not follow merely from prior acceptance of
non-D-finiteness of J.

The reviewer read NORMALIZATION.md, NEXT.md, the candidate W proof, its exact
checker, the prior candidate and manuscript, the M4 review, and the relevant
locally archived BB2014 statements. Independent tests are listed below.

## Adversarial checks

1. BB2014 equations (1)--(4) give W=I/(1-I), I=4J-2D_I-t and
   D_I=R/(1+R), with exactly the displayed G recurrence. The rational identity
   W=-1-(1+P)/F is correct. It deliberately uses zeros of the new denominator;
   old J poles alone would not prove the result.
2. The G solution satisfies both initial values, including k=-1. Its
   characteristic roots are t/q and tq. Alpha>0 and alpha+beta>0 ensure every
   real summand denominator is positive, regardless of the sign of beta.
   On a sufficiently small complex neighborhood, large-index denominators
   are uniformly separated from zero and earlier ones form a finite list.
   This gives normal convergence, not just pointwise real convergence.
3. At sigma the repeated-root formula is consistent with both initial
   values. Its reciprocal terms have a divergent positive harmonic tail.
   Finite partial sums and positivity prove the full real limit R->infinity
   without assuming monotonicity or exchanging divergent limits. Thus D_I->1.
   An ordinary one-variable limit is uniform on any uniformly approaching
   phase family, so a convergence rate is unnecessary.
4. In the new sector b=N+theta-eta_e lies between N and N+1. For n<=N,
   b-n+1 is bounded below by 1+theta-eta_e>0; for n>=N+1, n-a is at least
   1-theta>=0.1. All remaining small Gamma arguments are positive. Reflection
   contributes sin(pi*a)/sin(pi*b), with no parity sign. It is positive in
   this sector. Since z_0 tends to a negative constant, the post-crossing
   amplitude B is negative, exactly as used in the candidate.
5. The old compact-product estimates depend on separation from integers and
   positive Gamma arguments, not on the sign of B. These separations hold
   uniformly here. The same absolute crossing estimate, with eta+nu<1, and
   exponential tail bound therefore transfer both regularized moments
   uniformly. There is no extra crossing mass or independently chosen
   normalization constant on the far side of the crossing.
6. The new exact arithmetic uses the same four integrals; it does not claim
   to certify discrete-to-continuum convergence computationally. The checked
   F0 signs are strictly separated from zero. Since B<0 and J_1,post>0,
   dropping their product really does give an upper bound on 1+P0. Its
   strict negative margin holds throughout the whole phase interval.
7. Uniform convergence makes F change sign and keeps 1+P away from zero
   throughout every sufficiently late band. P,H,D_I are holomorphic there.
   A zero of F has finite order because the endpoint signs exclude identical
   vanishing; the nonzero numerator prevents cancellation. No simplicity,
   uniqueness, effective first index, or residue estimate is needed.
8. The source supplies meromorphic P,H throughout |t|<sigma. For R, its
   overlapping complex neighborhoods along the positive real interval agree
   by the common normally convergent series and attach to its origin germ.
   They can be shrunk to keep 1+R nonzero along the corridor. On any compact
   initial segment only isolated meromorphic poles of the resulting W need
   bypassing; they cannot form an interior barrier. The constructed poles
   consequently belong to the continuation of the original W germ.
9. Distinct a=N+theta bands give distinct t values. Infinitely many poles
   approaching sigma contradict the finite singular-point set of a
   polynomial-coefficient linear differential equation. The accumulation
   point itself need not lie in the continuation domain.

## Independent replay

- `.venv/bin/python -m experiments.w_exact_identities`: all three exact
  symbolic checks passed.
- `.venv/bin/python -m proofs.w_critical_certificate`: full 2048-rectangle,
  16-bit-exponent certificate passed independently. Decimal consequences:
  F0(4/5) in [0.99180337,1.05700564],
  F0(9/10) in [-0.23240630,-0.19788695], and the uniform upper-bound
  enclosure has upper endpoint -2.26608430.
- `.venv/bin/python -O -m proofs.w_critical_certificate`: failed immediately
  as intended, before certificate generation, with the assertion-engine
  optimization guard.

These tests certify the arithmetic replay, not the analytic theorem by
themselves. Small finite-N endpoint failures are compatible with the eventual
argument and must not be presented as certified poles.

## Reviewed provenance

Observed source HEAD: `c698d932ede87358382d20bdde2eded39a099241`.
SHA-256 of reviewed inputs and independently reproduced output:

| File | SHA-256 |
| --- | --- |
| proofs/W_NON_DFINITE.md | `351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a` |
| proofs/w_critical_certificate.py | `1e0de39db886294eee94331d2bc28ccdbb4ff9682f4e84d8433ec3d87fb0cfaa` |
| experiments/w_exact_identities.py | `f9235194226ebb8ba2c553952d616e60a391f4c62721bb6630cf33efad020944` |
| proofs/m3_critical_integrals.py | `da519b98367b64d29b18f50f13ecf42a2dae54550c6b3771fabbd92f8964cf16` |
| proofs/m3_prudent_intervals.py | `a2230bdeedbefcd5550cc64f304dcdd4b887a5c60f77e4f7cac974ad71451ff1` |
| publication/main.tex | `d020e1c1d58e08bc642e74d7da5a1f02df33eb42defcfd6053d1a7bf250fd0e0` |
| references/bacher-beaton-2014.txt | `d9dfa12998b29a5e19fe1cb021f352debe3656a4e5a9a78767e2f29d60b1d865` |
| Independent W JSON stdout | `ab5cbc0caf0f24f5b32e877668e87cc2d4d75cd830c62123ad450711f0c7ed6c` |

Root owns final integration, permanent retention of outputs, and verification
that the accepted mathematical content is unchanged in the final freeze.
