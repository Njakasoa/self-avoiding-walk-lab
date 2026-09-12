# Candidate proof: two-sided weakly prudent bridges are non-D-finite

Status: **candidate under independent review**. Publication priority is
**UNRESOLVED**. This note addresses W itself; the previous theorem about J
does not imply this result by closure of D-finite functions under quotients.
No new result is claimed for unrestricted square-lattice walks.

The external inputs are Bacher–Beaton, *Weakly prudent self-avoiding bridges*
(FPSAC 2014), equations (1)–(5), Propositions 14/16 and Theorem 17:
https://doi.org/10.46298/dmtcs.2445. The exact moment and Gamma-product
identities are recorded in M3_NON_DFINITE_CANDIDATE.md and the reviewed
publication/main.tex. Their phase interval is extended explicitly below.

## 1. Locate the correct denominator

Use a distinct symbol R for the partially directed ramp generating function
(called D in BB2014), to avoid confusion with the kernel factor 1-tq:

    R(t)=sum_(k>=0) t^(k+1)/G_k(t),
    D_I=R/(1+R),
    G_-1=1, G_0=1-t,
    G_k=(1-t+t²+t³)G_(k-1)-t²G_(k-2).

BB2014 gives

    J=(P-H)/(1+P),  I=4J-2D_I-t,  W=I/(1-I).

Set

    F=(3-t-2D_I)P-4H-(1+t+2D_I).

Exact rational identities give

    I-1=F/(1+P),             W=-1-(1+P)/F.                 (1)

Consequently an analytic zero of F with 1+P nonzero is a genuine pole of W.
In contrast, a pole of J typically becomes removable under the second
quotient. The identities are independently checkable without numerical
evaluation in experiments/w_exact_identities.py.

## 2. The partially directed term tends to one

Put sigma=sqrt(2)-1. For real 0<t<sigma, the physical kernel root q satisfies
0<q<1 and t(q+1/q)=1-t+t²+t³. The recurrence has the exact solution

    G_k=t^k[alpha*q^(-k)+beta*q^k],
    alpha=(1-t-tq)/(1-q²),       beta=1-t-alpha.

It has the stated values for k=-1,0 and characteristic roots t/q,tq.
Here alpha>0 because t(1+q)<2sigma<1, and alpha+beta=1-t>0.
For k>=0,

    alpha+beta*q^(2k) >= min(alpha,alpha+beta)>0,
    t^(k+1)/G_k = t*q^k/(alpha+beta*q^(2k))>0.             (2)

Thus R is finite and positive at every such real t. For each fixed t_0 in
this interval, choose a small complex neighborhood on which q,alpha,beta
are analytic, |q|<rho<1 and |alpha| is bounded below. For all sufficiently
large k the denominator in (2) is separated from zero by |alpha|/2; the
finitely many earlier denominators remain nonzero after shrinking the
neighborhood. A uniform geometric bound gives normal convergence of R.
Since 1+R(t_0)>1, D_I is holomorphic near every real t_0 as well.

At t=sigma the characteristic root is repeated. Direct substitution gives

    G_k(sigma)=sigma^k[(1-sigma)+(1-2sigma)k].

All these values are positive, and the sum of the corresponding terms
sigma/[(1-sigma)+(1-2sigma)k] diverges. Positivity for t<sigma and convergence
of each fixed finite partial sum as t tends to sigma imply R(t)->+infinity:
given any bound, choose a critical partial sum exceeding it and then choose
t close enough to sigma. No exchange of divergent infinite sums is used.
It follows that

    D_I(t)->1,                       t->sigma from below.  (3)

In particular, this convergence is uniform on any family t_N(theta) tending
uniformly to sigma from below. A rate or effective first N is unnecessary.
An independent derivation and audit are requested in W_DIRECTED_RAMPS.md.

## 3. Extend the critical moment limit to the other phase sector

All notation in this section is that of the reviewed critical-product proof.
Let epsilon=-log(q²), a=s_g/epsilon=N+theta, b=a-eta_epsilon,
eta_epsilon=eta+O(epsilon), eta=1/sqrt(2). Use the NEW compact phase interval

    T_W=[4/5,9/10],                   eta<4/5<9/10<1.

The implicit phase inverse still satisfies

    epsilon_N(theta)=s_*/N+O(N^-2),
    s_*=-log(1/2+sqrt(2)/4)>0,

uniformly. For sufficiently large N, b lies in (N,N+1), whereas in the
earlier proof it lay in (N-1,N). Both a and b remain uniformly separated
from integers. No g_n or h_n vanishes. The real-pole classification in
BB2014 therefore makes P and H holomorphic at every point of these bands.

The exact recurrence and factorization are unchanged:

    z_(n+1)/z_n = r*g_e(n*epsilon)/(g_e(n*epsilon)+delta),
    z_n=z_0*r^n*T_n(a,b)*product_(j<n) R_e(j*epsilon),
    T_n=product_(j<n) (j-a)/(j-b).

The two positive-argument Gamma representations still exhaust all indices:

    n<=N:   T_n=Gamma(a+1)Gamma(b-n+1)
                 /[Gamma(b+1)Gamma(a-n+1)],

    n>=N+1: T_n=[sin(pi*a)/sin(pi*b)]
                 *Gamma(a+1)Gamma(n-a)
                 /[Gamma(b+1)Gamma(n-b)].                 (4)

At n=N, b-n+1=1+theta-eta_epsilon is bounded below by a positive constant;
at n=N+1, n-a=1-theta>=1/10. The other possibly small Gamma arguments are
also separated from zero. The sine denominator is separated from zero.
Thus the same uniform Gamma-ratio estimates apply. The nonsingular divided
differences and their compact uniform limits do not depend on which phase
sector is used. In particular, for eta+nu<1 the previous proof yields

    |z_n| <= C_S(epsilon+|n*epsilon-s_g|)^(-eta-nu),

on each fixed compact scale, and a uniform exponential bound in n*epsilon
beyond a fixed S>s_*+1. The crossing-window absolute sum is bounded by
C(rho+epsilon)^(1-eta-nu), uniformly in theta. These are the same absolute
domination estimates used for the exact h-zero regularized moments; they
do not require the post-crossing amplitude to be positive.

The one change is its SIGN. In this sector the reflection multiplier
sin(pi*theta)/sin(pi*(theta-eta)) is positive. Since z_0 tends to -1/sigma²,
the post-crossing amplitude is negative:

    A=1/sigma²,
    B(theta)=A*sin(pi*theta)/sin(pi*(eta-theta))<0.

The limiting profile is still -A*M(u) before the crossing and B(theta)*M(u)
after it, with the SAME positive normalized M and four positive integrals
J_(j,pre),J_(j,post) as in the reviewed proof. Exact h-zero regularization,
compact product convergence, integrable crossing domination and the
exponential tail therefore give, uniformly for theta in T_W,

    P(t_N(theta))->P_0(theta)
       =-(1-sigma)-A*J_(1,pre)+B(theta)*J_(1,post),
    H(t_N(theta))->H_0(theta)
       =sigma²[-3-A*J_(2,pre)+B(theta)*J_(2,post)].         (5)

This is an extension of the earlier analytic proof, not an inference from
its two earlier numerical endpoints. The changed Gamma indexing and sign
are explicitly checked in (4).

## 4. New exact limiting signs and exclusion of J poles

The new checker proofs/w_critical_certificate.py recomputes the SAME four
critical integrals with the reviewed 384-bit outward dyadic arithmetic,
2048 interval rectangles and 16-bit dyadic power enclosure. It uses the
same certified Machin-pi and sine Taylor remainder to evaluate the new
phase endpoints. It checks eta<4/5<9/10<1 and positivity of the integrals.

Combining (3) and (5), the uniform limit of F is

    F_0(theta)=(1-sigma)P_0(theta)-4H_0(theta)-(3+sigma).

The exact enclosures imply the conservative strict signs

    0.99 < F_0(4/5) < 1.06,
   -0.24 < F_0(9/10) < -0.19.                             (6)

Moreover B(theta)<0 throughout T_W. Hence the positivity of J_(1,post)
and the exact integral enclosure imply the UNIFORM bound

    1+P_0(theta) <= sigma-A*J_(1,pre) < -2.26.             (7)

The inequality is not claimed to be equality: the negative post term was
dropped to obtain an upper bound. There is no division by 1+P before its
separation from zero has been established. As all factors in F are uniformly
bounded and converge uniformly, (3),(5) indeed imply F->F_0 uniformly.

## 5. Infinitely many actual W poles

For every sufficiently large N, uniform convergence preserves (6) and makes
1+P(t_N(theta))<-2 for every theta in T_W. The continuous real function
theta->F(t_N(theta)) has opposite endpoint signs. Choose a zero at theta_N
and put w_N=t_N(theta_N). At w_N, P,H,D_I and J are holomorphic, F=0 and
1+P is nonzero. The endpoint signs exclude F being identically zero on the
band; analyticity makes every selected zero finite-order. Equation (1)
then shows that W has a non-removable pole at w_N, with no cancellation.

The parameter bands for different integers N are disjoint since
a=N+theta and T_W is strictly contained in (0,1). Thus these are infinitely
many distinct poles, and w_N->sigma. BB2014's P,H continuation and the
overlapping neighborhoods in Section 2 continue the original W germ to
these real bands; isolated earlier poles can be bypassed in those complex
neighborhoods. No new branch unrelated to the original germ is selected.

A D-finite analytic germ satisfies a linear differential equation with
polynomial coefficients. Its finite singularities can occur only at the
finitely many zeros of the leading coefficient. The infinite pole family
contradicts that property. Subject to independent review of the proof and
certificate, W is therefore non-D-finite.

No effective first N, uniqueness, simplicity or residue estimate is needed
or asserted. Slow convergence of D_I may prevent small finite indices from
showing the limiting endpoint signs; such failures do not replace or refute
the uniform eventual argument. They must be retained as numerical evidence.
