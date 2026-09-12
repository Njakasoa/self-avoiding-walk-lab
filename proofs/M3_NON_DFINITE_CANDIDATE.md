# Candidate proof: irreducible NE-prudent ramps are non-D-finite

Status: **CANDIDATE PROOF UNDER INDEPENDENT REVIEW**, not yet M3 acceptance.
This extends the earlier interlacing lemma using a matched product limit and
certified integral signs. Any defect in the convergence proof invalidates the
conclusion; finite checks alone cannot replace it. Novelty remains unresolved.
The claim concerns J=(P-H)/(1+P), not the additional weakly prudent bridge
quotient W. The starting formulas and meromorphic continuation are BB2014
Propositions14/16, equation(5), and Theorem17.

## 1. Parameter and exact product

Use the definitions and exact identities in M3_CRITICAL_PRODUCT.md. Put

    epsilon=-log(q²), q=exp(-epsilon/2), sigma=sqrt(2)-1,
    C=q-t, D=1-tq, E=1-q²,
    g_e(s)=t-D*U(t,exp(-s)), delta=t²*E/C, r=q*C/D.

The quadratic kernel relation is equivalent to

    q+1/q=1/t-1+t+t².

At t=sigma the right side is2 and its derivative is nonzero. The implicit
function theorem gives a real analytic t(epsilon)=sigma+O(epsilon²), with
t(epsilon)<sigma for positive small epsilon. Throughout this proof epsilon
is positive and tends to zero.

The function g_e(s) increases strictly with s. Let s_g(e) be its zero and
s_h(e) the zero of g_e(s)+delta. The kernel is analytic in (e,s) near the
positive limiting zero, and

    s_g -> s*=-log(1/2+sqrt(2)/4)>0,
    U(sigma,exp(-s*))=u*=1/sqrt(2),
    partial_s g_0(s*)=sigma.

The implicit function theorem, delta/epsilon ->kappa=sigma²/(1-sigma),
and Taylor expansion at s_g give

    eta_e=(s_g-s_h)/epsilon = eta+O(epsilon),
    eta=1/sqrt(2) in (0,1).

Also -log(r)/epsilon ->lambda=1/(1-sigma). All these limits follow by
ordinary differentiation of algebraic expressions at positive s*, where
there is no square-root branch singularity.

Let a=s_g/epsilon and b=s_h/epsilon=a-eta_e. Since
s_g(e)=s*+O(e), its analytic expansion gives a'(e)=-s*/e²+O(1).
Thus for each sufficiently large integer N and each theta in the compact
interval T=[3/10,7/20], there is a unique small e=e_N(theta) with

    a=N+theta,       e_N(theta)=s*/N+O(N^-2),

uniformly in theta; this choice is continuous in theta. For all such N,
a and b stay a fixed positive distance from every integer, because
T is separated from0,1,eta. In particular no g_n or h_n vanishes there.
The source's real pole classification ensures P and H are analytic on each
of these parameter intervals.

With z_n=p_n/g_n the exact recurrence is

    z_0=1/g_e(0),
    z_(n+1)/z_n = r*g_e(n*e)/(g_e(n*e)+delta).

## 2. Gamma factorization and uniform product limits

For fixed finite S>s*, define positive divided differences on 0<=s<=S:

    F_e(s)=g_e(s)/(s-s_g),
    G_e(s)=(g_e(s)+delta)/(s-s_h),
    R_e(s)=F_e(s)/G_e(s).

The values at their removable zeros are the positive derivatives. Exactly,

    z_n = z_0*r^n * T_n(a,b) * product_(j<n) R_e(j*e),
    T_n(a,b)=product_(j<n) (j-a)/(j-b)
            =Gamma(n-a)*Gamma(-b)/(Gamma(-a)*Gamma(n-b)).

Here products at n=0 equal1. No approximation has entered this factorization.

We first justify the nonsingular factor. Uniformly on each fixed [0,S],

    log R_e(s)/e -> psi(s)
       = -kappa/g_0(s)+eta/(s-s*),

where the apparent pole at s* is removable. Near s*, this follows from
Taylor expansion of the two positive divided differences with respect to
their root locations, using g_e smooth there and eta_e=eta+O(e). Off a
fixed neighborhood of s*, use directly

    log R_e(s)=log(1+(s_g-s_h)/(s-s_g))
                -log(1+delta/g_e(s)).

Both perturbations are uniformly O(e) with denominators bounded away from
zero. The kernel g_e converges uniformly to g_0 on [0,S], including s=0,
by its explicit square-root expression. Thus this argument needs no bounded
s-derivative at0. The square-root endpoint cannot invalidate the uniform
log-ratio expansion. The limiting psi is continuous at0 and at s*.
Uniform convergence and the usual Riemann-sum criterion for a continuous
function consequently give

    sum_(j<n) log R_e(j*e) -> integral_0^s psi(x) dx,
    n*e -> s,

uniformly for n*e in [0,S] and theta in T. Likewise n log r ->-lambda*s.

For T_n apply the Gamma reflection formula and the positive-real ratio
asymptotic Gamma(x+c)/Gamma(x+d)~x^(c-d), uniformly for c,d in compact
sets. These standard formulas are [DLMF5.5.3](https://dlmf.nist.gov/5.5.E3)
and [DLMF5.11.12](https://dlmf.nist.gov/5.11.E12); compact-parameter uniformity
also follows directly by inserting bounded shifts in Stirling's remainder.
For s separated from s*, this gives

    T_n -> (s*/|s-s*|)^eta                    if s<s*,
    T_n -> [sin(pi*theta)/sin(pi*(theta-eta))]
             *(s*/|s-s*|)^eta               if s>s*.

Before the crossing the two reflection factors cancel; after the crossing
one remains. eta_e=eta+O(e) in particular implies
(eta_e-eta)*log(e)->0, so no unaccounted power of epsilon survives.
The convergence is uniform on closed s-subintervals excluding s*, and
uniform in theta in T.

For later integration a bound is needed at the crossing, not just pointwise
asymptotics. The same reflection identities and the Gamma ratio bound give

    |T_n| <= C*a^eta_e*(1+|n-a|)^(-eta_e).

More explicitly, for n<=N the exact positive-argument expression is

    T_n=Gamma(a+1)*Gamma(b-n+1)/(Gamma(b+1)*Gamma(a-n+1)).

For n>=N+1 it is

    T_n=[sin(pi*a)/sin(pi*b)]
         *Gamma(a+1)*Gamma(n-a)/(Gamma(b+1)*Gamma(n-b)).

All four arguments in each expression are positive and stay a fixed distance
from zero where they can be small. To see that the constant is uniform,
apply the positive-argument ratio bound to these expressions. All sine denominators are bounded away from zero by the phase
separations. The remaining positive Gamma arguments either lie in a fixed
compact interval avoiding their poles, or tend to infinity where the ratio
asymptotic supplies the bound. This covers n on both sides and within a fixed
number of steps of a. The nonsingular product and r^n are bounded on [0,S].
Choose any fixed nu>0 with eta+nu<1. For sufficiently small e, the result is

    |z_n| <= C_S*(e+|n*e-s_g|)^(-eta-nu),       n*e<=S.       (A)

For s beyond a fixed S>s*+1, g_e(s) is uniformly positive, delta>0, and
0<r<=exp(-c*e) for a fixed c>0. The exact recurrence then yields

    |z_n| <= C*exp(-c*(n*e-S)),                n*e>=S.       (B)

The constant at the first index beyond S is bounded by(A), far from the
crossing. These are bounds uniform in theta and N; their explicit numerical
constants are unnecessary for the existence theorem below.

## 3. The limiting product profile

The product limit just obtained solves, on each side of s*,

    d log |Z|/ds=-lambda-kappa/g_0(s).

Writing u=U(sigma,exp(-s)), d=1-sigma, direct partial fractions give the
profile

    M(u)=M_raw(u)/M_raw(1),
    M_raw(u)=(u-sigma)^(2+sqrt(2))*(1/sigma-u)^sqrt(2)
             *|u-u*|^(-eta)*u^(-1-sqrt(2)).

All powers here are positive real powers. The exact rational derivative is
checked in experiments/m3_moment_identities.py. Since g_0(0)=-sigma²,
put A=1/sigma². The limiting product is

    Z=-A*M(u),                              u>u*,
    Z= B(theta)*M(u),                       u<u*,
    B(theta)=A*sin(pi*theta)/sin(pi*(eta-theta))>0.

The relative constants are fixed by the Gamma reflection factor, not chosen
independently across the singular point.

## 4. Exact regularization and convergence of the moments

Let u_h=tq/C, so h(u_h)=0, and for j=1,2 put

    L_j=f(u_h)^j/(1-u_h),
    R_j(u)=f(u)^j-L_j*(1-u),
    V_(j,e)(u)=-R_j(u)/h(u).

The divided difference identity shows that the apparent singularity cancels:

    V_(j,e)(u)=[(f(u)^j-f(u_h)^j)/(u-u_h)+L_j]/C.

It is positive and uniformly bounded on the physical real interval t<=u<=q
for small e, and converges uniformly to its critical counterpart. All other
denominators remain separated from zero. From the exact moment identities,
with Q=q*t²*E*(1-t²) and S0=-t*D²/g(q),

    P = C/g(q)+L_1*S0 + Q*sum z_n*V_(1,e)(u_n),
    H/t² = f(q)*C/g(q)+L_2*S0 + Q*sum z_n*V_(2,e)(u_n).

Also Q/e ->K=sigma²*(1-sigma²). No asymptotic cancellation of two divergent
moments is being assumed: the singular factor was cancelled exactly first.

Bounds(A),(B) now justify these Riemann-sum limits. In particular, for a
crossing window |n*e-s_g|<rho, (A) bounds its absolute contribution by

    C*e*sum_(|n*e-s_g|<rho) (e+|n*e-s_g|)^(-eta-nu)
       <= C'*(rho+e)^(1-eta-nu).

The estimate follows by comparison with the integral of x^(-eta-nu); it tends
to zero uniformly as rho then e tend to zero. Thus there is no hidden point
mass at the crossing. Off this window the uniform product convergence gives
ordinary Riemann-sum convergence. Bound(B) controls the infinite tail, and
the initial endpoint has no singular denominator and is covered by(A).
This proves convergence of both moments uniformly in theta in T.

At criticality f(u*)=1, L_1=L_2=L=2+sqrt(2), and the two boundary terms are
respectively -d and -3. Set

    phi(u)=(u-sigma)*(1-sigma*u)/(sigma*(1-sigma²)*u),

The formulas used below are

    V_1(u)=[L+1/(u_star*(1-sigma*u))]/d,
    V_2(u)=[L+(f(u)+1)/(u_star*(1-sigma*u))]/d.

Define four positive convergent integrals

    J_(j,pre)=K*integral_(u*)^1 M(u)*V_j(u)*phi'(u)/phi(u) du,
    J_(j,post)=K*integral_sigma^(u*) M(u)*V_j(u)*phi'(u)/phi(u) du.

Their only interior endpoint singularity is |u-u*|^-eta with eta<1.
The uniform limits are

    P_0(theta)=-d-A*J_(1,pre)+B(theta)*J_(1,post),
    H_0(theta)=sigma²*[-3-A*J_(2,pre)+B(theta)*J_(2,post)].

## 5. Certified signs of the limiting functions

The checker proofs/m3_critical_integrals.py uses exact outward dyadic
interval arithmetic. The substitution u=u*+Delta*x^8 on the pre interval,
and u=u*-Delta*x^8 on the post interval removes the integrable singularity.
After combining powers, the integrand contains x^[8*(1-eta)-1], with strictly
positive exponent. The other powers have nonnegative bases and positive
exponents, apart from a reciprocal of a base bounded away from zero.

Each real power is enclosed between neighboring dyadic exponents with
16 fractional bits, evaluated by16 exact outward square roots followed by
integer powers. Monotonicity in the exponent on either side of base1 proves
the enclosure; the hull covers bases straddling1. Interval rectangle sums over
2048 subdivisions enclose the integral without any assumed quadrature error.
The positive endpoint factors are evaluated after algebraic cancellation.
Machin's identity with alternating arctangent remainders encloses pi; a sine
Taylor polynomial with its Lagrange remainder encloses B(theta).

The initial exact run gives the following conservative decimal consequences
of the rational enclosures:

    -0.193 < 1+P_0(3/10) < -0.166,
     0.163 < 1+P_0(7/20) <  0.192,
     0.310 < 1+H_0(3/10) <  0.318.

These signs require independent checker review and source-frozen reproduction
before acceptance. Moreover B'(theta)=A*pi*sin(pi*eta)/sin²(pi*(eta-theta))>0
on T, and J_(2,post)>0. Hence 1+H_0(theta)>0.310 for every theta in T,
not only the checked endpoints.

## 6. Consequence if the preceding proof and certificate survive review

Uniform convergence provides, for every sufficiently large N,

    P(t_N(3/10))<-1<P(t_N(7/20)),
    1+H(t_N(theta))>0                       for all theta in T.

Continuity gives at least one r_N in that parameter interval with P(r_N)=-1.
The intervals for different N are disjoint because a=N+theta, so the r_N are
distinct and tend to sigma. Both P,H are analytic at these points. Since
P-H=-1-H is nonzero, each r_N is a non-removable pole of J.
A D-finite analytic germ satisfies a linear differential equation with
polynomial coefficients and can have finite-plane singularities only at the
finitely many zeros of its leading coefficient. Infinitely many poles of J
therefore contradict D-finiteness.

The proof intentionally claims neither an effective first N nor uniqueness
or simplicity of the zeros r_N. Neither is needed for infinitely many poles.
It also does not transfer the conclusion automatically to W or establish
publication priority. All gates remain pending independent review of this
candidate argument and the integral certificate.
