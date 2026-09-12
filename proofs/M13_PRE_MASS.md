# M13 candidate: absolute upper bounds on the pre-crossing mass

Status: analytic component for independent review. On N>=32,
theta in[.8,.9], let S_pre=sum_(n=0)^N A0 T_n K_n L_W(u_n).
This note proves S_pre<31/10 throughout the sector, and S_pre<2
when32<=N<=64. It does not estimate its phase derivative.

## Uniform upper envelope for the weight

The M10/M11 exact weight ratio and V1 formula simplify at u=1:

    R(1)=1/(1-t),
    V1(1)=1/[(1-t)(q(1-t)-t)],
    L_W(1)=[4t^2/(1-t)-(1-t+2delta)]
              /[(1-t)(q(1-t)-t)].                      (1)

L_W increases in u, so L_W(u_n)<=L_W(1). The numerator in (1)
increases in t and decreases in delta; it is positive by M10. Its
denominator is positive, decreases in t and increases in q. Thus with
t_h=.4143 and q_l=359/360,

    L_W(u_n)<Lmax(delta_lower),
    Lmax(d)=[4t_h^2/(1-t_h)-(1-t_h+2d)]
              /[(1-t_h)(q_l(1-t_h)-t_h)].               (2)

The rational checker gives Lmax(0)<5.899 and Lmax(1/17)<4.716.
Also A0/e<J_h:=t_h(1-t_h^2)/(1-t_h-t_h^2), by the increasing J(t)
proved in M11 and (1-exp(-e))/e<1. Finally K_n<=1 by the positive
secant product bound and r<1.

## Exact sum of the bare factors

The finite product recurrence yields the exact primitive

    sum_(n=0)^N T_n=[b+1-theta*T_N]/(1-beta).           (3)

For completeness, put Q_n=(n-a)T_n/(1-beta) and
Q_-1=-(b+1)/(1-beta). Then Q_n-Q_(n-1)=T_n, also at n=0;
telescoping gives (3) because N-a=-theta.
All terms are positive. Since b+1<N+6/5 and1-beta>.28,

    sum_(n=0)^N T_n<(N+6/5)/.28.

Using Ne<.17 and N>=32, equations(2),(3) give the entirely rational
uniform upper allowance

    S_pre<J_h*.17*Lmax(0)*(1+(6/5)/32)/.28<31/10.      (4)

## A directed lower reciprocal bound for32<=N<=64

Set t_ref=4142133/10000000. Exact I384 phase and directed-sum calculations
prove

    0<e(t_ref)<.01, a(t_ref)>64.9, D_R(t_ref)<16.       (5)

The complete positive directed tail is included. The M5 real phase
inverse is increasing in t on the domain containing the reference point
and every target point. Thus N+theta<=64.9 implies t_N<t_ref.
M10 directed monotonicity then yields D_R(t_N)<16, hence

    delta_D>1/17,   32<=N<=64.                          (6)

This is an order comparison proved for an interval of indices, not an
interpolation of sampled values.

## Keeping the negative endpoint term in the primitive

For n=N the pre-crossing telescope from M13_MIDDLE_MASS gives

    T_N>[(N+1+v)/(1+v)]^beta>[(5/6)N]^(7/10).

When N<=64, it follows that T_N/N>1/4. The exact positive tenth-power
comparison is (5/6)^7>64^3/4^10. Therefore

    b+1-theta*T_N
       <N+1-beta+theta*(1-N/4)
       <(4/5)N+11/10,

where1-N/4<0 makes theta>=.8 the correct endpoint for an upper bound,
and beta>.7. Equations(2),(3),(6) now give

    S_pre<J_h*.17*Lmax(1/17)*(.8+(11/10)/32)/.28<2.    (7)

The exact allowance is approximately1.97993. The proof uses no
pre-crossing derivative sign. The script m13_mass_bounds.py retains
all basepoint dyadic intervals, the directed tail and rational allowances.
