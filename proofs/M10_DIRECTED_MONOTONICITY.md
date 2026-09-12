# M10 candidate: directed monotonicity and a stronger uniform W weight

Status: candidate for independent review. The conclusions below apply to
every N>=32, but do not prove a phase derivative sign for F_N.

## Positive polynomial form of the directed denominators

Use the directed recurrence from W_NON_DFINITE:

    G_-1=1, G_0=1-t,
    G_(k+1)=(1-t+t^2+t^3)G_k-t^2 G_(k-1),
    D_R(t)=sum_(k>=0) t^(k+1)/G_k(t), 0<t<sigma.

Let A=t^-1-1+t+t^2, y=A-2 and g_k=G_k/t^k. Then
g_-1=t, g_0=1-t and g_(k+1)=(2+y)g_k-g_(k-1).
The shifted Chebyshev polynomials

    U_k(1+y/2)=sum_(j=0)^k binom(k+j+1,2j+1)y^j

satisfy U_-1=0,U_0=1 and the same recurrence. Therefore

    g_k=(1-t) sum_(j=0)^k binom(k+j,2j)y^j
          +(1-2t) sum_(j=0)^(k-1) binom(k+j,2j+1)y^j. (1)

The second sum is empty when k=0. Formula(1) also follows by subtracting
U_(k-1) from U_k and applying Pascal's identity. Every coefficient is
nonnegative, and its constant terms give g_k>=1-t>0.

On0<t<sigma, y>0 and y'=A'=-t^-2+1+2t<0. The factors1-t and1-2t are
strictly positive and decreasing. Thus g_k is strictly decreasing in t,
and each summand t/g_k is strictly increasing. Taking limits of the
positive partial sums proves that D_R is strictly increasing on this
interval. No termwise differentiation of the infinite sum is needed.

## One exact lower bound controls all N>=32

Set the rational reference point t0=207106/500000=.414212. The outward
I384 checker m10_directed_monotone.py proves

    0<e(t0)<.01, a(t0)<32.8, D_R(t0)>93/7.            (2)

The directed series is enclosed with its full positive geometric tail.
The M5 real phase inverse gives a(t) strictly increasing on this physical
domain. Since a(t_N(theta))=N+theta>=32.8, equation(2) implies
t_N(theta)>t0 for every N>=32. Directed monotonicity therefore yields

    D_R(t_N)>93/7, 0<delta_D=1/(1+D_R)<7/100.         (3)

This is a bound on all those indices, not an extrapolation from a finite fit.

## Stronger combined-weight gap and its logarithmic slope

Retain R_min and t_l=.414 from M10_POSITIVE_COMBINED_WEIGHT. Replacing
delta_D<.1 by(3), exact rational arithmetic gives

    4t_l^2 R_min-(1-t_l+.14)>.07.

Consequently L_W=4t^2V2-(1-t+2delta_D)V1 satisfies

    L_W>(7/100)V1>0                                  (4)

on the full physical kernel ray for every N>=32.

There is also a useful uniform logarithmic derivative bound in u, with
t,q,delta_D held fixed. Put h=u_h, R=V2/V1 and f=u/(1-tu). The exact formulas

    V1=(1-tuh)/[C(1-tu)(1-th)(1-h)],
    R=f(h)+f(u)(1-h)/(1-tuh)

give

    0<V1_u/V1=t/(1-tu)-th/(1-tuh)<t/(1-tu),
    R_u=(1-h)[1/((1-tu)^2(1-tuh))+f(u)th/(1-tuh)^2].

Use t<=t_h=.4143, h in[.706,.71], u<=1, d=1-t_h and d_h=1-.71t_h.
Then

    R_u <=R_u,max=.294[1/(d^2 d_h)+.71t_h/(d d_h^2)],
    L_W,u/L_W <=t_h/d+4t_h^2 R_u,max/.07<16.          (5)

The final inequality is checked exactly. Thus

    0<partial_u log L_W<16.

This bound concerns the kernel variable only. Changes in t,q,delta_D,
the smooth product and the boundary terms still have to be included in
any estimate of the complete theta derivative.
