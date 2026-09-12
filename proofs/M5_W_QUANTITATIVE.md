# M5 candidate: logarithmic pole displacement and residues of W

Status: **candidate for independent review**. The phase displacement below
uses the directed logarithmic theorem and the quantitative moment theorem.
Uniqueness, simplicity and residues additionally require the directed phase
derivative estimate explicitly stated in Section 3. No explicit W-pole N_0
is obtained by the non-effective moment constants in this note.

## 1. Critical root and certified constants

Put sigma=sqrt(2)-1, eta=1/sqrt(2), d=1-sigma, A=1/sigma², and
s*=-log(1/2+sqrt(2)/4). The W limit is

    F0(theta)=C0+L B(theta),
    C0=-d²-d A J_1,pre+12 sigma²+4 J_2,pre-3-sigma,
    L=d J_1,post-4 sigma² J_2,post,
    B(theta)=A sin(pi theta)/sin(pi(eta-theta)).

The exact interval checker `m5_critical_pole.py` certifies L<0 and

    B'(theta)=A pi sin(pi eta)/sin²(pi(eta-theta))>0

on [4/5,9/10]. The opposite endpoint signs therefore give a unique
critical phase theta*; the new exact enclosure is

    0.8695 <= theta* <= 0.8720.

Write p*=1+P0(theta*)<0 and f*=F0'(theta*)<0. Define

    C_shift=2 sigma p*/f*>0,
    K=s*²/16>0,
    C_res=-p* s*²/(8 f*)<0.

The 4096-rectangle, 384-bit certificate encloses these coefficients:

    0.38696091 <= C_shift <= 0.44166261,
    0.00156711 <= K <= 0.00156712,
   -0.00167097 <= C_res <= -0.00146400.

These are exact limit-function enclosures, not estimates fitted to finite
phase data. Their use in a finite-pole theorem needs the analysis below.

## 2. First displacement law without assuming simple roots

Set L_N=log N and delta_N(theta)=1-D_I(t_N(theta)). The directed theorem
gives, uniformly on the real phase interval,

    delta_N=sigma/L_N+O(L_N^-2).

The moment-rate theorem gives P_N=P0+O(N^-1/20), H_N=H0+O(N^-1/20),
and t_N=sigma+O(N^-2). The exact decomposition is

    F_N=(1-t_N)P_N-4H_N-(3+t_N)+2 delta_N(1+P_N).

Consequently

    F_N(theta)=F0(theta)+2 sigma(1+P0(theta))/L_N
                                            +O(L_N^-2).       (1)

Here every inverse power of N is eventually smaller than L_N^-2; the
constants and threshold in that comparison are not yet numerical.

The previously proved eventual endpoint signs give at least one root
theta_N in each sufficiently late phase band. Since -F0' has a positive
minimum, (1) at any such root first implies
|theta_N-theta*|=O(1/L_N), by the real mean-value theorem. Taylor expansion
at theta*, with uniformly bounded second derivative on the phase interval,
then gives

    theta_N=theta* - C_shift/log N + O((log N)^-2).        (2)

This holds for every selected root in the band, even before uniqueness is
established. The sign is fixed: finite roots approach their limiting phase
from below eventually. Small-index behavior need not obey this asymptotic.

## 3. Additional derivative input and simple poles

The separate directed estimate in `M5_DIRECTED_REFINED.md` supplies

    |partial_theta D_I(t_N(theta))| <= 30000/N = o(1)

uniformly on the real phase interval. An O(N^-1/(log N)^2) estimate is more
than sufficient. The moment theorem already gives uniform convergence of
P_N',H_N' to P0',H0'. Since t_N'=O(N^-3), differentiating the exact
decomposition yields F_N'->F0' uniformly. Thus F_N'<0 on the whole interval
for sufficiently large N. There is exactly one root theta_N in each such
band, and it is simple. The phase map has t_N'>0, so w_N=t_N(theta_N)
is also a simple zero in the t coordinate.

At this zero, 1+P_N is separated from zero, and the exact quotient gives

    Res_(t=w_N) W=-(1+P_N(theta_N)) t_N'(theta_N)/F_N'(theta_N).

Implicit differentiation of s_g(e)=e(N+theta), together with
t_e=-e/8+O(e³), gives uniformly

    e_theta=-s*/N²+O(N^-3),
    t_N'=s*²/(8N³)+O(N^-4).

It follows that

    N³ Res_(t=w_N) W -> C_res < 0.                       (3)

Since 30000/N=o(L_N^-2), (1) also
holds after one phase derivative with remainder O(L_N^-2). Equations
(2) and (3) then sharpen to

    Res_(t=w_N) W = C_res/N³ + O(1/(N³ log N)).           (4)

Neither this derivative condition nor its verification can be replaced by
numeric finite differences alone.

## 4. Translate the phase correction into the t plane

The explicit inverse-kernel expression is

    v_g=q(1-tq-t²)/[(1-tq)(1-t²)],  s_g=-log v_g.

At e=0, t_e=0 and q_e=-1/2. Direct logarithmic differentiation gives

    s_g'(0)=sigma/[2(1-sigma)]=eta/2=:s1.

Solving the analytic phase equation to the next order gives

    e_N(theta)=s*/N-s*(theta-s1)/N²+O(N^-3).

Therefore, already for any bounded selected phase,

    sigma-w_N=K/N²-2K(theta_N-s1)/N³+O(N^-4).

Substituting (2) yields the quantitative candidate expansion

    sigma-w_N = K/N² - 2K(theta*-eta/2)/N³
                 + 2K C_shift/(N³ log N)
                 + O(1/(N³(log N)²)).                   (5)

The leading 1/N² accumulation was already an accessible corollary of the
older phase construction. The new information is the controlled logarithmic
phase displacement and its corresponding term in (5).

## Remaining effective obligation

The directed subproblem has an explicit sufficient index 2^108 for its
31/(log N)^2 error bound. That index is **not** an N_0 for W poles.
An actual W threshold requires explicit constants and validity domains for
the moment error and derivative error. Those have not been supplied by the
non-effective O(N^-1/20) theorem. The overall M5 goal remains open until
this separate requirement is discharged, even if (2)–(5) pass review.
