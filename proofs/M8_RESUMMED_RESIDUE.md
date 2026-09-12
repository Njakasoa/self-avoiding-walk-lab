# M8 candidate: a resummed residue with an explicit algebraic error

Status: candidate for independent review. Assumes the M8 uniqueness
threshold10^57 and analytic interpolation/domain lemmas. The following
bound is uniform for every integer N>=10^57.

Use p=1+P0, j0=s*²/8, and the same theta_hat_N and F_hat_N as
M8_EFFECTIVE_PHASE. Define the normalized residue approximation

    r_hat_N=-j0*p(theta_hat_N)/F_hat_N'(theta_hat_N).     (1)

For any integer m>=1, let E1(N,m)=20m²[E(N)+A_m]+B_m, with the exact
Chebyshev tail formulas and M=10^8+100 from M8_CHEBYSHEV_THRESHOLD.
Let R_theta(N) be the explicit phase bound from M8_EFFECTIVE_PHASE.
Put

    Z(N,m)=4E1(N,m)+10/N²+2850/(N logN)+480000/N
                                      +1200R_theta(N),
    R_res(N,m)=.004*[E(N)+75R_theta(N)]+7.5/N+.006Z(N,m).

Then at the unique simple pole w_N,

       abs(N³ Res_(t=w_N) W-r_hat_N)<=R_res(N,m).       (2)

## 1. Quantitative phase Jacobian

The real phase bounds give s_g=s*+m_e e with .3<m_e<.4 and
.3<s_g'<.4. For h=theta-m_e and c=theta-s_g', both in(.4,.6),

    Ne=s*/(1+h/N), abs(e_theta)=e/(N+c).

The M7 kernel remainder implies
abs(t_e+e/8)<=16*10^6 e³. Hence J_N=N³ t_N' differs by at most
16*10^6/N² from

              j0/[(1+h/N)²(1+c/N)].

For positive h,c, the latter differs from j0 by at most1.8j0/N,
using1-(1+x)^-2<=2x and1-(1+y)^-1<=y. Since j0<.0037,

    abs(J_N-j0)<1/N, 0<J_N<.004, N>=10^57.             (3)

These are derivative bounds from the analytic kernel expansion, not a
derivative of a position-error estimate.

## 2. Numerator and denominator derivative errors

The real moment and phase bounds give, at theta_N,

    abs(p_N(theta_N)-p(theta_hat_N))<=E(N)+75R_theta(N). (4)

Subtract F_hat_N' from the exact denominator derivative at the same
phase. The moment derivatives cost at most4E1(N,m); the remaining terms
are bounded by

    75e²/8+8/(7N³)+150abs(delta_N-d_hat)+480000/N
      <10/N²+2850/(N logN)+480000/N.

Here .3<s_g'<.4 implies the Jacobian estimate used in M8_EFFECTIVE_PHASE,
and the directed reciprocal difference is less than19/(N logN).

On the whole phase interval, abs(F0')<26, P0'<75, and
abs(B''/B')=abs(2pi cot(pi(eta-theta)))<45: use
.09<theta-eta<.20, sin(pi*(theta-eta))>.18 and pi<4.
Consequently abs(F_hat_N'')<(26+150/250)*45<1200. Moving the phase to
theta_hat_N adds at most1200R_theta(N). Thus

    abs(F_N'(theta_N)-F_hat_N'(theta_hat_N))<=Z(N,m).   (5)

The critical bound26 follows from the exact M7 endpoint derivative
certificate and its analytic monotonicity, not a phase mesh sample.

## 3. Exact quotient comparison

The residue identity is

                   N³ Res W=-p_N(theta_N)J_N/F_N'.

Use the decomposition that changes first p_N, then J_N, then the
denominator. M8 gives abs(F_N')>1 and M8_EFFECTIVE_PHASE gives
abs(F_hat_N')>27/5. Also abs(p(theta_hat_N))<7.5. The three differences
are therefore at most

    .004*[E+75R_theta], 7.5/N,
    [7.5*.0037/(27/5)]*Z <.006Z,

respectively. This proves(2). The independent fixed-degree threshold
proof supplies abs(F_N')>1 even if a nonoptimal choice of m makes the
separate error estimate E1(N,m) larger than that proof's1.033 allowance.

Choosing m=ceil(logN), the analytic interpolation estimate implies

         N³ Res W=r_hat_N+O(N^-1/4 log²N).              (6)

The approximation(1) retains the directed logarithmic dependence before
expansion. It consequently determines every fixed inverse-logarithmic
coefficient of the normalized residue, with an algebraically small
remainder. It does not assert a uniform expansion when the number of
retained logarithmic terms also grows with N.

## 4. Uniform sign and size at the improved threshold

Since s*>.15, equation(3) also gives J_N>.0028. The fixed-degree
derivative certificate gives abs(F_N'-F0')<4.733, hence abs(F_N')<31.
Together with3.5<abs(p_N)<8, this yields

    3.5*.0028/31 < abs(N³ Res W) < 8*.004.

Both p_N and F_N' are negative and J_N is positive. Consequently

        -1/(20N³)<Res_(t=w_N) W<-1/(6000N³), N>=10^57.

This extends the same deliberately coarse bounds in M8_RESIDUE_EXPANSION
to the improved threshold. It does not infer finite residues from an
asymptotic remainder.

## 5. A rational expression generating all logarithmic coefficients

The affine critical profiles eliminate the implicit phase from(1).
Write A=sigma^-2, c=cos(pi eta), kappa_B=pi/(A sin(pi eta)),
s=post1, p0=sigma-A pre1, and F0=C0+JB. Define

    H=p0 J-s C0,
    D(delta)=(C0+2delta p0)²
             -2Ac(C0+2delta p0)(J+2delta s)
             +A²(J+2delta s)².

Then the exact closed expression is

                   r_hat_N=-j0 H/[kappa_B D(d_hat)].   (7)

Indeed B_hat=-(C0+2delta p0)/(J+2delta s), so
p(B_hat)=H/(J+2delta s). Also
B'=kappa_B*(B²+2AcB+A²). Substitution in(1) and multiplication
of the two denominator factors by(J+2delta s) prove(7).
No new approximation is introduced.

Write D(delta)=D0+D1 delta+D2 delta², alpha=D1/D0, beta=D2/D0,
and r0=-j0 H/(kappa_B D0). The denominator D0 is nonzero because
F0'(theta*) is nonzero and J!=0. With u=logN+b, equation(7) becomes

             r_hat_N=r0*u²/(u²+alpha sigma u+beta sigma²).

In powers of1/L with L=logN, set
a1=2b+alpha sigma and a2=b²+alpha sigma b+beta sigma².
The coefficients r_k of r_hat_N=sum_(k>=0)r_k L^-k satisfy

    r_1=-alpha sigma r0,
    r_2=r0*b²-a1*r_1-a2*r0,
    r_k=-a1*r_(k-1)-a2*r_(k-2), k>=3.                 (8)

The denominator is analytic and nonzero at1/L=0; thus this series
converges for sufficiently large L. Combined with the algebraic error
(6), it determines the actual normalized residue's asymptotic expansion
to every fixed logarithmic order. The first coefficient agrees with
the independently derived expression in M8_RESIDUE_EXPANSION.
