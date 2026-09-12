# M10 candidate: a positive combined W weight for every N>=32

Status: candidate structural lemma for independent review. This is not
a monotonicity theorem for F_N and does not close the index gap.

Use theta in[.8,.9] and e=e_N(theta). The accepted M5 real phase inverse
exists for N>=20 with e<=.01 and s_g<.17. Thus for every N>=32,

    e=s_g/(N+theta)<.17/32<1/180.                     (1)

Write sigma=sqrt(2)-1, q=exp(-e/2), t=t(e), C=q-t,
u_h=tq/C, f(u)=u/(1-tu), and let delta_D=1/(1+D_R).
The kernel ray satisfies t<=u<=q<=1.

## A directed bound on the complete N>=32 domain

M6_DIRECTED_CONSTANT applies on0<e<=.01, with

    D_R=log(1/e)/sigma+c_D+R,
    c_D>3/4, |R|<=100e log(1/e).

The lower bound on c_D comes from the frozen M6 coefficient certificate.
Since 1/sigma>12/5 and(1) holds,

    D_R>(12/5-5/9)log(1/e)+3/4.

We have log180>5. One rational proof is
exp(1)<1+1+1/2+1/6+(1/24)/(1-1/5)=87/32<11/4,
and(11/4)^5<180. Hence log(1/e)>5, and

    D_R>359/36>9,
    0<delta_D<36/395<1/10.                           (2)

No monotonicity of the individual directed summands in t is assumed.

## Uniform scalar boxes

The physical kernel bounds give sigma-t<=e^2/8 and q>=1-e/2. Since
.4142<sigma<.4143, equation(1) yields

    .414<t<.4143, 359/360<q<=1,
    .706<u_h<.71.                                    (3)

For the last bounds, tq/(q-t) increases in t and decreases in q:

    u_h>.414/(1-.414)>.706,
    u_h<.4143*(359/360)/[(359/360)-.4143]<.71.

Every denominator here is positive. These simple boxes hold uniformly
up to the critical endpoint; no finite-N sampling is used.

## Exact weight ratio and its sign

Use the exact M8 regularized weights

    dd=1/[(1-tu)(1-tu_h)], L1=f(u_h)/(1-u_h),
    V1=(dd+L1)/C,
    V2=[(f(u)+f(u_h))*dd+f(u_h)*L1]/C.

Algebra gives the useful exact ratio

    V2/V1=f(u_h)+f(u)*(1-u_h)/(1-t*u*u_h).             (4)

For fixed t,u_h this ratio increases in u: all displayed factors are
positive, f increases, and the last denominator decreases. Consequently,
with t_l=207/500=.414, h_l=353/500=.706, h_u=71/100=.71,

    V2/V1 > R_min,
    R_min=h_l/(1-t_l*h_l)
           +t_l*(1-h_u)/[(1-t_l^2)(1-t_l^2*h_l)].    (5)

Indeed u>=t>=t_l, u_h>=h_l and u_h<=h_u allow independent positive
numerator lower bounds and denominator upper bounds in the second term.
Let c_W=1-t+2delta_D. From(2)--(3), c_W<1-t_l+1/5. Exact rational
evaluation of(5) gives

    4*t_l^2*R_min-(1-t_l+1/5) >1/100.               (6)

Therefore the combined W weight satisfies, for every N>=32 and every
point of its complete physical kernel ray,

    L_W(u):=4t^2 V2(u)-c_W V1(u) > V1(u)/100 >0.     (7)

Moreover L_W increases in u. To see this, V1 increases in u and
L_W=V1[4t^2(V2/V1)-c_W]; both factors are positive and increasing by
(4) and(7). Along u=U(t,exp(-x)), the function L_W is thus decreasing
in x, at each fixed e and delta_D.

## What this does and does not establish

If P=B1+Q sum z_n V1 and H=t^2[B2+Q sum z_n V2], then exactly

    F=c_W B1-4t^2 B2-(3+t)+2delta_D
                       -Q sum z_n L_W(u_n).           (8)

Equation(7) identifies one positive combined weight instead of estimating
the two moment contributions independently. Whenever z_n<0 has been
established on a source-pole-free phase strip, the sum contribution in(8)
is positive. The weight sign(7) itself does not require that additional
product-sign hypothesis.

This lemma says nothing about the sign of the total phase derivative:
the boundary term, Q, z_n, t, q and delta_D all vary with theta. A uniform
comparison of those derivatives remains necessary. Positivity or monotonicity
in the integration variable x cannot be substituted for monotonicity in theta.
