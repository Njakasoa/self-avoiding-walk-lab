# Bounded review of the critical-product route

Status: feasible proof route with explicit remaining analytic obligations;
NOT a proved scaling theorem or noncancellation theorem. Reviewed 2026-09-12.
Owned only this note. Inputs: M3_CRITICAL_PRODUCT.md, the exact moment checker,
and the temporary corrected numerical integral script. No web research.

## Verdict

I found no fatal sign, exponent, phase, or regularization mismatch. The proposed
connection multiplier sin(pi*theta)/sin(pi*(theta-eta)), eta=1/sqrt(2), has
the correct sign: negative on theta in [0.32,0.34]. Since z_0 tends to
-1/sigma², the limiting product is negative before the crossing and positive
after it. The temporary script uses a positive post amplitude and is consistent
with this convention. The ODE alone cannot supply that multiplier, but an
exact Gamma-product factorization can.

The exact algebraic identities and a formal solution of the ODE do not yet
justify interchanging the limit with the infinite moment sums. The proposed
numerical sign margins also need certified quadrature before theorem use.

## A useful matched-product lemma to prove

Write eps=-log(q²), s_j=eps*j, and G_eps(s)=t-D*U(t,exp(-s)).
Let s_g be its simple real zero, a=s_g/eps=N+theta. Let s_h be the zero of
G_eps(s)+delta, and b=s_h/eps=a-eta_eps. In a fixed small neighborhood of
the limiting crossing s_*, G_eps is smooth/analytic and strictly increasing.
The kernel discriminant there is bounded away from zero. Consequently one
should prove, uniformly in theta in the chosen compact interval,

    eta_eps = eta + O(eps),
    s_g -> s_*,
    dist(theta,Z), dist(theta-eta_eps,Z) >= c > 0.

The O(eps) rate matters: a bare eta_eps->eta is not sufficient to discard
factors eps^(eta_eps-eta); o(1/|log eps|) would suffice.

Factor EXACTLY on that neighborhood as

    G_eps(s_j)       = eps*(j-a)*A_eps(s_j),
    G_eps(s_j)+delta = eps*(j-b)*B_eps(s_j),

where A_eps and B_eps are positive and bounded away from zero, with controlled
smooth derivatives. The local portion of the recurrence is then

    z_(j+1)/z_j = r * (j-a)/(j-b) * A_eps(s_j)/B_eps(s_j).

The singular factor is not approximated by an Euler step. Its finite product
is exactly a ratio of Gamma functions. For integer endpoints L<R,

    product_(j=L)^(R-1) (j-a)/(j-b)
      = Gamma(R-a)/Gamma(L-a) * Gamma(L-b)/Gamma(R-b).

Reflection for the negative arguments on the pre side and uniform Gamma-ratio
asymptotics give the connection multiplier

    sin(pi*a)/sin(pi*b)
      = sin(pi*theta)/sin(pi*(theta-eta_eps)).

This identity makes the cancellation of the large integer N transparent.
There is no unexplained parity factor. Uniformity requires the distance bounds
above. Integer crossings of g or h are deliberately excluded by this phase box.

The smooth A_eps/B_eps product must then be estimated by a Riemann sum. A
sufficient local estimate is log(A_eps/B_eps)=eps*F_eps(s), with F_eps and
its needed derivatives uniformly bounded and converging on the crossing
neighborhood. Such an estimate follows from a sufficiently uniform C^3
expansion of G_eps and its shifted simple root, but should be written out,
not assumed from the formal ODE. This supplies the regular part of the ODE
and matches the same normalization on both sides. Together with the exact
Gamma factor it should yield convergence on compact sets away from s_*.

This is a proof blueprint, not an independently completed uniform estimate.
In particular, all constants must remain uniform along t solving a=N+theta.
One must also establish existence and a usable monotone local inverse for
that parameterization for all sufficiently large N. Since s_g tends to a
positive constant and eps tends to zero, a diverges, but divergence alone is
not the full uniform inverse assertion.

## Bounds sufficient to pass to the moments

A usable domination statement, for a fixed small kappa>0 with eta+kappa<1,
is

    |z_j| <= C*(|s_j-s_g|+eps)^(-eta-kappa)

on a fixed crossing neighborhood. Uniform Gamma ratio estimates and the
bounded smooth factor should imply it. This bound must include the finitely
many closest indices on BOTH sides, not just compact sets avoiding s_*.
A compact-away limit alone does not control the moment sums.

For power j=1 or 2, use R_j(u)=f(u)^j-L*(1-u), with L=2+sqrt(2) at the
critical point. Indeed f(u_*)=1 and L*(1-u_*)=1, so both remainders vanish
linearly at u_*. The exact moment identity allows this subtraction before
any limit is taken. In the crossing neighborhood,

    |R_j(u_n)| <= C*(|s_n-s_g|+eps),
    |h_n| >= c*(|s_n-s_g|+eps),

provided the compact phase exclusion and eta_eps estimate are in force.
The second estimate follows by locating the shifted h zero and using the
uniform lower distance of b from integers. Since E=O(eps), this yields a
summand bound of the form

    |W_n R_j(u_n)| <= C*eps*(|s_n-s_g|+eps)^(-eta-kappa).

Its total over a neighborhood of radius rho is O(rho^(1-eta-kappa)),
uniformly as eps tends to zero. Thus the singular region contributes no
uncontrolled atom or residual finite jump. This is the key reason the
regularization makes the proposed limit plausible. The raw unregularized
moments do not admit this domination.

The estimate R_j=O(distance+eps) uses convergence of t, f_t, the crossing
location, and the critical subtraction. Their rates should be verified;
choosing an exact t-dependent subtraction that vanishes at the current g
zero is another option and may simplify the bounds.

There are two further regions. Near s=0, the critical kernel has a square-root
endpoint, so a globally smooth Euler expansion is not justified. Here g and
h stay away from zero and the logarithmic increments are O(eps); control a
short initial interval directly and then let its length tend to zero. At
large s, q^(2n) is small and r is uniformly bounded by exp(-c*eps), while the
remaining recurrence factors are uniformly contractive on this scale. Prove
an exponential s-tail bound to control the infinite moment tail. The
fixed-t convergence proof alone does not provide a uniform critical tail.

## Final sign certification still required

The temporary quadrature is high-precision numerical evidence, not an
interval certificate. Its endpoint conventions and integrable exponent are
consistent with the proposed regularization. After the matched-product and
moment convergence theorem, certify the limiting P+1 signs at theta=0.32
and theta=0.34, and a positive lower bound for limiting H+1 throughout the
phase box. The post amplitude

    A*sin(pi*theta)/sin(pi*(eta-theta))

is strictly increasing there: its derivative is
A*pi*sin(pi*eta)/sin(pi*(eta-theta))²>0. If the relevant post integral has
certified positive sign, this reduces the H lower bound to an endpoint.
Only then does uniform convergence transfer these strict margins to every
sufficiently large N, allowing the intermediate value theorem to locate an
actual P=-1 root with H+1 nonzero. Such a completed argument would establish
the missing infinite noncancellation, but the current formal/numerical
materials do not yet do so. M3 remains OPEN and M4 remains withheld.

## Stronger exact regularization supplied by the root

The root subsequently supplied a preferable cancellation: set u_h=tq/C,
L_j=f_t(u_h)^j/(1-u_h), and R_j(u)=f_t(u)^j-L_j*(1-u).
Then h(u)=-C*(u-u_h) and, EXACTLY,

    R_j(u)/h(u)
      = -( divided_difference(f_t^j; u,u_h) + L_j ) / C.

The right side has a removable diagonal, is uniformly bounded for t near
sigma and u in [t,q], and is strictly negative. This follows from C bounded
away from zero, u_h tending to 1/sqrt(2), and the positive derivative of
f_t^j with 1-tu bounded away from zero. There is no need for a separate
lower bound on sampled h_n in the regularized moment argument. Intermediate
h poles in the product itself remain excluded by the compact phase condition.
This exact h-zero subtraction supersedes the preceding discussion of a
critical or g-zero subtraction as the preferred proof route.

With Q=q*t²*E*(1-t²) and S0=-t*D²/g(q), the resulting moments are

    P=C/g(q)+L_1*S0-Q*sum z_n*R_1(u_n)/h_n,
    H/t²=f(q)*C/g(q)+L_2*S0-Q*sum z_n*R_2(u_n)/h_n.

Thus an integrable uniform bound on z_n alone, together with its compact-away
matched limit and endpoint/tail estimates, suffices for the moments. The
limiting L_j equals 2+sqrt(2) for both powers, preserving the critical
integrals already proposed. This materially simplifies the analytic task,
but does not itself supply the still-required product convergence estimates.

Provenance at this bounded pass: base HEAD
`9087d31ddcf6c69ef6e62a7186755a3088724d6b`.
Input SHA-256 values:

- M3_CRITICAL_PRODUCT.md: `120f6ddf88d62992a02c976e02a7f2a43ad0acdf20f8c2e7dddd66c0cd631f6c`.
- m3_moment_identities.py: `da79d60772e70d2db3301ac305909e7b1df290bbf4e4ff086687dc52d9c3d98c`.
- temporary corrected integral script: `934c76d4c431aaeb8156e481b4c95e68f44bde736992680b5fcd272b80389cdd`.
