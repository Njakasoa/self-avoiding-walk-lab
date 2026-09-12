# M5: adversarial quantitative review plan

Status: **research plan, not an accepted quantitative theorem**.
The internally accepted J/W existence arguments remain unchanged. This
bounded review identifies sufficient new estimates and the limits of what
their existing proofs establish. No heavy numerical calculation was run.

## What is already available

Write e=epsilon_N(theta), a=N+theta, b=a-eta_e, with theta in a compact
interval strictly separated from 0, eta and 1. The accepted proofs provide
e~s*/N uniformly, eta_e=eta+O(e), exact Gamma factorization, uniform
convergence of the nonsingular product on each fixed compact s interval,
an integrable crossing bound with exponent p=eta+nu<1, and exponential
tails beyond a fixed reference S0. They prove uniform convergence of the
two regularized moments, but **no stated modulus of convergence**.

In particular, uniform convergence alone implies neither an error
o(1/log N) nor convergence of theta derivatives. The current proof's
successive limits e->0, rho->0, S->infinity cannot be replaced by
rho=rho(e), S=S(e) without controlling the constants. Its endpoint argument
intentionally avoids differentiating the square root at s=0.

The analytic inverse construction does give, by differentiation on a fixed
phase interval,

    e_theta=1/a'(e)=O(e²),   e_thetatheta=O(e³),
    (eta_e)_theta=O(e²),    t_theta=O(e³).

These orders follow from the analytic expansions already used, but explicit
constants and a quantified domain have not been provided.

## A sufficient real-variable rate theorem

Let E_N be the sum of the two uniform moment errors. A useful sufficient
target is a bound, for 0<e<e0, e<rho<rho0 and R>S0,

    E_N <= C[(1+R)^m e^beta rho^(-m)
              + rho^(1-p) + exp(-c R)],                 (Q)

with fixed beta,c>0, finite m, p<1, and constants uniform in theta.
The crossing and tail *forms* come from the old proof; the first term and
control of its R-dependence remain new work. If m=0 the negative rho power
is absent. Choosing rho=e^alpha with 0<alpha<beta/(m+1), and
R=L log(1/e), gives a positive power of e times logarithmic factors. This
is stronger than o(1/log N). A weaker directly logarithmic bound would also
suffice, but must still track dependence on growing R and shrinking rho.

To prove (Q), sufficient component estimates are:

1. Boundary terms and Q/e converge at an algebraic rate. Their denominators
   are separated from zero, so explicit algebraic expansions can supply it.
2. The regularized V_j factors converge uniformly at an algebraic rate,
   with a quantitative modulus in s suitable for Riemann sums. Their exact
   divided-difference formulas remove h=0 before any estimate.
3. For the nonsingular product, bound both
   log R_e(s)/e-psi(s) and the Riemann-sum error for psi quantitatively.
   A fixed-compact O(e^beta) bound is insufficient by itself for growing R;
   either establish polynomial R growth or split at a fixed S0 and use a
   separately quantified tail comparison.
4. Away from |s-s_g|<rho, use Gamma-ratio remainder bounds uniform in the
   bounded shifts. Terms of size e/rho and e|log e| are expected, the latter
   from eta_e-eta. The word "expected" is essential until remainder
   constants and arguments are written down.
5. Quantify quadrature of the limiting profile outside the crossing.
   Its derivatives grow as powers of rho^(-1); recording this growth yields
   the rho exponent in (Q). Use a fixed crossing neighborhood inside [0,S0]
   so its domination constant never depends on R.

## The endpoint s=0: manageable but not already differentiated

The explicit kernel suggests the decisive local discriminant estimate

    c1(s+e²) <= discriminant(e,s) <= c2(s+e²)

on a sufficiently small real rectangle. The s coefficient is nonzero and
positive; along s=0 the kernel-root separation is proportional to e.
This estimate, with the actual coefficients verified, gives a square-root
perturbation bound of order e and a 1/2-Hölder modulus in s. Since the
critical g_0(0) is nonzero, the two-log representation of R_e then avoids
any singular denominator at this endpoint. A Hölder Riemann-sum error of
order e^(1/2) would already be ample for (Q).

Do **not** claim a uniform bounded s derivative of the kernel: its size
near zero can grow as (s+e²)^(-1/2). For phase differentiation at fixed n,
s=n e moves and

    s_theta=n e_theta=O(e s).

The factor s suppresses this endpoint derivative; at n=0 it vanishes
exactly. This is the promising cancellation to prove explicitly. Derivative
bounds in the independent coordinates (e,s) must be combined before
discarding this factor. The comparison with s+e² and all resulting bounds
are new lemmas, not consequences of mere uniform continuity.

## Gamma crossing and C1 convergence

In either accepted compact phase sector, the exact positive-argument Gamma
formulas split at the fixed integer N: n<=N versus n>=N+1. Thus theta
differentiation does not move this index split. Small Gamma arguments stay
in a compact positive interval, including the nearest crossing sites.

For the pre-crossing logarithmic derivative, differentiating the exact
formula gives

    psi_digamma(a+1) - b_theta psi_digamma(b+1)
      + b_theta psi_digamma(b-n+1) - psi_digamma(a-n+1),

where b_theta=1-(eta_e)_theta. The post-crossing formula adds the
derivative of log|sin(pi*a)/sin(pi*b)| and uses the corresponding
digamma terms at n-a,n-b. This is the safe route. Differentiating an
unmatched continuum power |s-s*|^(-eta) termwise would falsely suggest
a nonintegrable crossing derivative.

The sine denominators stay separated from zero. Differences of digamma
terms with bounded shifts should remain bounded near the crossing and
decay at large arguments; the unequal b_theta leaves at worst logarithmic
terms multiplied by O(e²). A precise sufficient estimate on fixed compact
scales is

    |partial_theta z_n| <= C(1+|log e|)^k
                              (e+|n e-s_g|)^(-p),        (D)

with finite k and p<1. An O(1) prefactor is preferable but unnecessary if
the crossing window shrinks at an algebraic rate. The differentiated smooth
product and r^n must be included in (D); Gamma estimates alone do not prove
it. Their phase derivatives sum over O(1/e) terms, so each O(e) error cannot
be casually ignored.

For a direct C1 proof, also require:

- Differentiated off-crossing product convergence, including the B'(theta)
  connection amplitude and the moving mesh s=n e.
- Differentiated regularized weights and prefactor Q; all mesh/prefactor
  derivative contributions must be tracked in the fixed-n infinite sum.
- A summable derivative tail such as
  C(1+s)^m exp(-c s), uniformly in e and theta. The old undifferentiated
  exponential bound does not imply this by itself.
- A shrinking-window derivative estimate from (D). Avoid differentiating
  a discontinuously truncated moving window; instead bound the already
  differentiated full series or use smooth cutoffs with controlled errors.

An alternative is locally uniform holomorphic convergence in a fixed
complex theta neighborhood and Cauchy's derivative estimate on a smaller
one. This would establish C1 elegantly, but real uniform convergence does
not imply such a complex extension. One must exclude complex source poles,
control the endpoint square-root branch and obtain complex Gamma/product
domination. It is a new proof route, not an automatic corollary.

## What simplicity and residues additionally require

On the W interval the limiting denominator is affine in B(theta):

    F0(theta)=constant+B(theta)*L,
    L=(1-sigma)J_1,post-4 sigma² J_2,post.

The already certified opposite endpoint signs, together with strictly
increasing B, imply L<0. Continuity on the compact interval then makes
F0' strictly negative and bounded away from zero. For an explicit margin,
certify L and the sine-factor derivative by interval arithmetic.

C1 convergence of P,H alone is not enough for W: one also needs
partial_theta D_I(t_N(theta))->0. With that supplied by the directed-term
analysis, F_N'->F0' ensures eventual uniqueness and simplicity in each
band. Since t_theta is nonzero, a simple theta zero is a simple t zero.
The exact residue is

    Res_(t=w_N) W = -(1+P(w_N))*t_theta(theta_N)
                                  / F_N'(theta_N).

A residue asymptotic additionally uses the location limit theta_N->theta_*
and a leading expansion for t_theta; residue *error bounds* require the
quantitative versions of all these estimates. None is presently certified.

## Can an explicit first index be obtained cheaply?

The old existence proof alone cannot produce an explicit N0. It has no
numeric constants for its uniform convergence, crossing domination or
tail comparison, and finite successful endpoint tests cannot bound all
later bands. A giant but rigorous N0 may be cheaper than sharp asymptotics:
fix concrete crossing and tail cutoffs using the certified limiting margins,
then quantify only the remaining compact comparison and directed-term
error. This avoids a full optimal-rate theorem but still requires real
new inequalities and computable constants. For simplicity/residues, the
derivative obligations above remain separate even if endpoint N0 is found.

Review outcome: there is a plausible algebraic-rate route and a plausible
C1 upgrade, with the endpoint and lattice crossing explicitly addressed.
Neither upgrade has yet been proved or accepted by this review.

## Reviewed inputs

Observed HEAD: `2893bbe27f2e65449bfc345c9f7a874faa185129`.
Input SHA-256 values:

- W proof: `351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a`.
- J manuscript: `d020e1c1d58e08bc642e74d7da5a1f02df33eb42defcfd6053d1a7bf250fd0e0`.
- M3 candidate: `e184726e834116e8eaf9d83926e571f40f4f2883eda1114b05c231872ec0a627`.

This deliverable has no numerical output or certificate; it is a bounded
analytic obligation map.
