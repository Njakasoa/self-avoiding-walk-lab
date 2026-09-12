# M5 candidate: an algebraic moment rate and phase derivatives

Status: **new proof candidate, awaiting independent review**. Constants in
the estimates below are uniform but not numerically evaluated. Consequently
this note does not give an explicit first index N_0. It leaves the previously
accepted J/W proofs unchanged.

Use the notation and exact regularized moments of
`M3_NON_DFINITE_CANDIDATE.md`, with the W phase sector [4/5,9/10]. Put
sigma=sqrt(2)-1, eta=1/sqrt(2), s*=-log(1/2+sqrt(2)/4), and h=s*/N.
The functions P_N(theta),H_N(theta) mean P(t_N(theta)),H(t_N(theta)).

## Proposed quantitative statement

There exist C and N_1, independent of real theta in [4/5,9/10], such that

    |P_N-P_0|+|H_N-H_0| <= C N^(-1/20),
    |partial_theta P_N-P_0'|+|partial_theta H_N-H_0'|
                            <= C N^(-1/20).                 (Q)

The exponent is deliberately nonoptimal. In particular the errors are
o(1/log N), as needed to resolve the directed-term logarithmic correction.
The route to derivatives is holomorphic convergence on a fixed phase
neighborhood, not differentiation of a moving singular Riemann sum.

## 1. Complex phase family and kernel control

Work initially on Omega={theta: dist(theta,[4/5,9/10])<1/50}; take its
closure inside a slightly larger such neighborhood when obtaining uniform
bounds. Its distance from 0,eta,1 is positive. The analytic inverse equation

    s_g(e)=e(N+theta)

and s_g(0)=s*>0 give, uniformly on this neighborhood,

    e=e_N(theta)=h+O(h²),   partial_theta e=-h²/s*+O(h³),
    t(e)=sigma-e²/16+O(e⁴),   eta_e=eta+O(e).

These follow by the analytic implicit-function theorem applied to
s_g(e)-e(N+theta)=0 after setting e=h y and 1/N=h/s*. The derivative
in y at h=0,y=1 is -s*. In particular Re e>0 and |Im e|=O(h²).

For v=e^(-s), factor the kernel discriminant as

    Delta(t,v)=[(1-t)²-t(1-t²)v][(1+t)²-t(1-t²)v].

The closer branch value is v_c=(1-t)/(t(1+t)). The expansion for t gives
v_c=1+c h²+O(h³) with c>0, uniformly for complex theta in Omega; the
imaginary part is O(h³). Thus |v_c|>1. The other branch value stays farther
than 1 from the origin. The physical U branch is analytic on |v|<=1,
with the square root continued from v=0. It agrees with U(t,1)=q.

On the small initial ray s=n e, the two discriminant factors therefore
give |Delta| comparable to |s|+h². At t=sigma the discriminant has a
simple zero at s=0 with positive s derivative. The elementary identity
sqrt(z+w)-sqrt(z)=w/(sqrt(z+w)+sqrt(z)), together with the bound by a
constant times sqrt(|w|) when |z| is small, implies

    |U(t(e),e^(-s))-U(sigma,e^(-s))| <= C h.               (1)

Here s is on the ray of e or a narrow positive-real sector; the square
roots stay in the same sector. On the rest of that sector the discriminant
is bounded away from zero and ordinary analytic bounds apply. The limiting
kernel is uniformly 1/2-Hölder on the positive ray and its nearby sector.
Its derivative is O(|s|^(-1/2)) at zero, bounded on intermediate compact
sets, and exponentially decreasing at infinity. No bounded derivative at
zero is assumed.

The source denominators cannot introduce a pole in Omega for large N.
Indeed g(t,U(t,v))=0 implies v=e^(-s_g(e)); h(t,U(t,v))=0 implies
v=e^(-s_h(e)). At v=e^(-ne), either equality requires

    n=a+2*pi*i*m/e  or  n=b+2*pi*i*m/e,   m an integer,
    a=N+theta,   b=N+theta-eta_e.

For m!=0 the imaginary part has size at least c|m|/h, whereas Im a,Im b
are bounded. For m=0, a and b are separated from every integer. The other
rational denominators are separated by their positive limiting values.
This excludes finite summand poles. The uniform tail below supplies normal
convergence, proving holomorphy of P_N,H_N on Omega.

## 2. Quantify the nonsingular product globally

Let R_e(s) denote the divided-difference ratio of the accepted product
factorization (not the directed generating function). With Delta_s=s_g-s_h,
delta=t²(1-q²)/(q-t), its exact logarithm outside the removable crossing is

    log R_e(s)=log(1+Delta_s/(s-s_g))-log(1+delta/g_e(s)).

Choose the branches tending to zero as e->0. The following estimates hold
uniformly for s on the ray and for every finite cutoff S:

    sup_(0<=|s|<=S) |log R_e(s)/e-psi(s)| <= C h,
    psi(s)=-kappa/g_0(s)+eta/(s-s*),
    kappa=sigma²/(1-sigma).                              (2)

The constant in (2) is independent of S. To verify this, cover three regions.
On a fixed disk about s*, both divided differences are analytic and nonzero,
so Taylor's theorem in e, using Delta_s/e=eta+O(e), gives a uniform O(h)
remainder. Outside that disk on a fixed initial compact set, denominators
in the two-log formula are separated; (1), Delta_s/e=eta+O(e), and
delta/e=kappa+O(e) give (2), including s=0. On the remaining half-ray,
g_e tends uniformly to t²q and |s-s_g| increases; the same two-log Taylor
bound has uniform constants. These three regions also show that psi has
a bounded global 1/2-Hölder constant; its singularity at s* is removable.

Riemann sums of a 1/2-Hölder function on a ray consequently give

    |sum_(j<n) log R_e(je)-integral_0^(ne) psi(s) ds|
                              <= C(1+S) sqrt(h),   |ne|<=S.   (3)

The term from (2) is O(S h); the Hölder quadrature term is O(S sqrt(h)).
Also n log r+lambda n e=O(S h), with lambda=1/(1-sigma), and
z_0=-1/sigma²+O(h). For S=O(log(1/h)) all these errors tend to zero.

## 3. Gamma ratios away from the crossing

Keep the exact split n<=N versus n>=N+1. All small Gamma arguments have
positive real parts bounded below on Omega. Reflection multipliers are
bounded there. For large positive real part, the ratio expansion with
bounded complex shifts has relative error O(1/|z|); this follows from
Stirling's expansion with remainder in a fixed sector, as in
[DLMF 5.11(ii),(iii)](https://dlmf.nist.gov/5.11).

Let rho>Ch and compare to the real mesh x_n=n h. At points
|x_n-s*|>=rho and x_n<=S, the exact Gamma formulas, (3), and
s_g=s*+O(h), eta_e=eta+O(h) yield the relative bound

    z_n=Z_theta(x_n) [1+O(E)],
    E=h/rho+(1+S)sqrt(h)+h(|log rho|+log(2+S)),           (4)

provided E is small. The mesh shift ne-x_n=O(h x_n) is included: the
logarithmic derivative of the critical profile is O(1+1/|s-s*|), so its
contribution is O(h(1+S)+h/rho), since x_n=s*+O(rho) near the crossing.
The two branches of Z are -A M before the crossing and B(theta) M after,
with exactly the accepted normalization and complex sine multiplier.

The accepted Gamma domination also holds in Omega by the same formulas
and bounded complex shifts. Fix nu=1/20 and p=eta+nu<1. On a fixed compact
crossing neighborhood,

    |z_n| <= C(h+|x_n-s*|)^(-p).                         (5)

No positivity of z_n is used. The critical profile has exponent eta<p.
Therefore both discrete and integral crossing-window masses are bounded
by C(rho+h)^(1-p). The constant is attached to a fixed neighborhood and
does not grow with S.

## 4. Uniform tails and regularized weights

Choose S0 fixed and large. For x_n>=S0 the kernel variable has small
modulus, and g_e(ne)=t²q+O(e^(-x_n/2)) lies near a positive real number.
The quotient delta/g_e(ne) has positive real part for large N, uniformly
on Omega; hence |g_e/(g_e+delta)|<=1. Moreover |r|<=exp(-h) for large N,
since -log r/e->lambda>1. Formula (4) at the first index beyond the fixed
cutoff S0, which is separated from the crossing, bounds its starting value
uniformly. Iterating the exact recurrence from that index gives

    |z_n| <= C exp(-(x_n-S0)),    x_n>=S0.               (6)

For the critical profile, its logarithmic derivative tends to
-lambda-kappa/sigma²=-2/(1-sigma)<-1; enlarging S0 if necessary gives
the same exponential bound with another constant. Its regularized weights
are bounded. These bounds imply normal convergence on compact phase
subsets and a moment tail O(exp(-(S-S0))).

The exact divided-difference formulas for V_(j,e) have no crossing pole.
Their rational denominators stay separated. Their values are bounded and
their difference from critical weights at x_n is O(h(1+S)). Boundary terms
and Q/e differ from their limits by O(h). Since the comparison mesh is h,
use Q/h=(Q/e)(e/h)=K+O(h), where K=sigma²(1-sigma²); thus the change of
mesh adds only O(h) times a uniformly bounded absolute moment sum.
The limiting weighted profile
is 1/2-Hölder off the crossing, with a Hölder constant bounded by
C rho^(-1-eta). This follows from the kernel endpoint estimate and the
single power singularity at s*. Thus, outside the crossing window, its
Riemann-sum error is at most C(1+S)sqrt(h)rho^(-1-eta).

Integrating (4), the sum of absolute critical profile weights is uniformly
bounded when rho>=Ch: its crossing exponent is less than one and its tail
decays exponentially. Combining all terms yields

    |P_N-P_0|+|H_N-H_0| <= C [
        h/rho+(1+S)sqrt(h)+h(|log rho|+log(2+S))
        +(1+S)sqrt(h)rho^(-1-eta)
        +(rho+h)^(1-eta-1/20)+exp(-(S-S0)) ].             (7)

The estimates hold uniformly for complex theta in a fixed neighborhood
of the real interval, and C is independent of h,rho,S in the stated range.

## 5. Choose cutoffs and obtain derivatives

Set rho=h^(1/4) and S=S0+log(1/h). The slowest powers in (7) are

    h^((1-eta)/4) log(1/h),
    h^((1-eta-1/20)/4).

Both are O(h^(1/20)), because eta=1/sqrt(2)<3/4. All other terms are
smaller. This proves the first bound (Q) uniformly on a complex
neighborhood of [4/5,9/10], if the preceding estimates survive review.
Cauchy's estimate on disks of a fixed smaller radius then gives the
second bound (Q). It also gives every fixed higher theta derivative with
the same nonoptimal rate and a derivative-dependent constant.

No differentiation across a truncated lattice crossing is used. The
remaining effective task is to replace the uniform constants and
"large N" thresholds in Sections 1–4 by explicit inequalities and numbers.
This candidate rate alone does not discharge the requested explicit N_0.
