# Independent Astra attack review: critical noncancellation proof

Review date: 2026-09-12. Verdict: **the analytic argument is rigorous conditional
on the stated BB2014 formulas/meromorphy and correct certified integral
bounds**. I found no remaining mathematical gap in the supplied matched-product
and moment-convergence argument. This is a mathematical review of the specified
candidate, not a novelty determination, source-frozen reproduction receipt,
or authorization to accept M3/M4 before the remaining gates.

The interval-integral implementation has a separate independent reviewer.
This review does not certify that implementation by inspecting its reported
numbers. Its valid certificate and frozen replay remain explicit premises.

## Adversarial checks of the convergence argument

Read the complete M3_NON_DFINITE_CANDIDATE.md against the earlier exact-product
and moment identities. The earlier review objections are now addressed:

1. **Parameter choice.** The kernel relation gives analytic t(e) at the
   critical point because its t derivative is nonzero. The smaller kernel
   root is q=exp(-e/2)<1. The crossing is at positive s*, away from the
   kernel endpoint branch, so its root locations are analytic in e.
   The expansion a=s*/e+c+O(e) gives a'=-s*/e²+O(1), hence the asserted
   unique small inverse and uniform phase intervals for sufficiently large N.
   Both theta and theta-eta_e avoid integers uniformly on [0.30,0.35].

2. **Constants and root shift.** Direct checks give g_0'(s*)=sigma,
   delta/e -> sigma²/(1-sigma), eta=1/sqrt(2), and
   -log(r)/e ->1/(1-sigma). The rate eta_e=eta+O(e) prevents an unnoticed
   eps-power drift in Gamma asymptotics. The h-zero is exactly the shifted
   g+delta zero, so excluding integral b excludes the actual source poles.

3. **Exact Gamma factor.** The ratio is correctly indexed from j=0 to n-1.
   For n<=N, b-n+1>=1+theta-eta_e stays positive. For n>=N+1,
   n-a>=1-theta stays positive. These ranges exhaust all indices, including
   the sign-changing step. Reflection gives sin(pi*theta)/sin(pi*(theta-eta_e)),
   with no missing integer-parity sign. The pre factor is positive and the
   post factor negative; multiplying z_0<0 gives the stated profile signs.

4. **Smooth remainder through the crossing and endpoint.** In a fixed
   neighborhood of s*, g_e is analytic and both positive divided differences
   depend smoothly on e and s after their removable values are filled in.
   At e=0 their ratio is one. Taylor expansion in e therefore makes
   log(R_e)/e converge uniformly there; off the crossing the explicit two-log
   expression identifies its limit as -kappa/g_0+eta/(s-s*).
   These two descriptions agree and remove the apparent pole. Away from the
   crossing, including s=0, uniform g_e convergence and denominators bounded
   away from zero suffice for the two-log expansion. No unjustified global
   s-derivative estimate is being assumed at the square-root endpoint.
   Uniform convergence to continuous psi is enough for uniform partial
   Riemann sums and the claimed bounded smooth product.

5. **A bound at the crossing, not merely away from it.** Positive-argument
   Gamma ratio estimates apply uniformly to both exact expressions, including
   the finitely many nearest indices because their arguments stay away from
   zero. They give the stated bound with exponent eta_e. Since
   eta_e<=eta+nu<1 for small e, the proposed bound (A) follows on compact
   s ranges after adjusting a fixed constant. This explicitly includes the
   potentially dangerous individual terms adjacent to the crossing.

6. **Tail control.** For fixed sufficiently large S, g_e is positive beyond
   S and delta>0, so the rational recurrence factor g_e/(g_e+delta) is
   between zero and one. The r factor is at most exp(-c*e). The first index
   beyond S is bounded by (A), supplying a uniform exponential bound (B).
   Thus fixed-t convergence is not being substituted for the missing uniform
   critical tail estimate.

7. **Relative profile constants.** Integrating psi and the explicit
   |s-s*|^-eta factor gives the same regular factor on both sides of the
   crossing; the sole extra constant is the reflection factor. Converting
   from s to u has the same nonzero absolute local derivative on either side,
   so it introduces no second free connection constant. Normalization at
   u=1 and z_0 ->-1/sigma² give exactly the stated -A and B(theta).

8. **Exact cancellation before taking limits.** The h-zero divided
   difference for V_(j,e) is correct and uniformly bounded: C and 1-tu stay
   away from zero and u_h tends to 1/sqrt(2). It removes the moment pole
   algebraically. The limits of the boundary terms are -d and -3, and
   Q/e tends to sigma²*(1-sigma²). The explicit critical V_1,V_2 formulas
   agree with the divided differences of f and f² because
   f(u*)=1 and 1-sigma*u*=u*.

9. **No hidden point mass.** After cancellation, the crossing contribution
   is bounded absolutely by C*(rho+e)^(1-eta-nu). This tends to zero when
   e tends to zero and then rho tends to zero, uniformly in phase. Compact
   convergence away from the crossing, ordinary Riemann sums there, and
   the exponential tail complete uniform convergence of both moments.
   The endpoint s=0 is bounded by (A) and causes no missing contribution.

## From certified margins to infinitely many poles

The positive post integral and B'(theta)>0 correctly promote an endpoint
lower bound for H_0+1 to the whole phase interval. Uniform convergence then
preserves strict P endpoint signs and a positive H+1 margin for every
sufficiently large N. The phase intervals are continuous, avoid source poles,
and are disjoint for different N. Thus each supplies a distinct zero of
P+1 with H+1 nonzero. No uniqueness, simple-root estimate, or effective first
N is needed. Since P+1 is analytic and not identically zero, its zero has
finite order; the nonzero numerator makes the corresponding singularity of
J a genuine pole. BB2014 supplies continuation from the germ to these points.
A polynomial-coefficient linear ODE permits singularities only at finitely
many finite leading-coefficient zeros, so these poles contradict D-finiteness.
This implication concerns J alone and does not silently transfer to W.

## Scope and provenance

No fresh numerical convergence probe or broad test run was used as proof.
The moment checker had passed all 11 exact identities in the preceding bounded
review. The current proof supplies the formerly missing analytic estimates;
the numerical probes remain diagnostics. Published priority is not established
by mathematical validity or by an unsuccessful bounded literature search.

Base HEAD at review: `9087d31ddcf6c69ef6e62a7186755a3088724d6b`.
Reviewed SHA-256 values:

- Candidate proof: `e184726e834116e8eaf9d83926e571f40f4f2883eda1114b05c231872ec0a627`.
- Exact product note: `120f6ddf88d62992a02c976e02a7f2a43ad0acdf20f8c2e7dddd66c0cd631f6c`.
- Integral checker observed, separately reviewed: `da519b98367b64d29b18f50f13ecf42a2dae54550c6b3771fabbd92f8964cf16`.
- Exploratory integral payload `/tmp/m3-critical-integrals.json`: `dd851e6bb29bd0b75d97703dffcd0abe3488149e8dcdeab5b2408330324f3b12`.

Final gate: obtain the separate arithmetic review and source-frozen reproduction
of the strict integral margins. Conditional on those checks, this review
supports the theorem that the irreducible NE-prudent ramp series J is
non-D-finite under the cited source formulas and meromorphy theorem.
