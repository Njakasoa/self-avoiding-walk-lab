# M14 candidate: compare the positive denominator sum directly

Status: analytic component awaiting independent review. This provides a
more permissive alternative to the joint-moment target in
M14_ENDPOINT_MARGIN_TRANSFER. It does not prove the remaining discrete
sum approximation or endpoint existence.

Let N>=512, e=e_N(theta)<17/51200 and delta be the actual directed
reciprocal at that point. The reviewed reference comparison gives
0<delta<1/20. Hold this delta fixed when comparing with critical values.
Define

    S_e=A0 sum_(n>=0) T_n K_n L_e(u_e(ne);delta),
    S0(delta)=J0 integral_0^infinity G_theta(s)K0(s)L0(u0(s);delta)ds,
    J0=J(sigma)=2sigma,
    Stilde_e=J0 e sum_(n>=0) T_n K_n L0(u0(ne);delta).

The critical density and product G_theta,K0 are those of the accepted
M6/M9 limit theorem. All sums and integrals above are positive and finite.
The exact decompositions are F_e=B(e,delta)+S_e and
Fhat=B(0,delta)+S0(delta), with Fhat from M14_ENDPOINT_MARGIN_TRANSFER.

## Pointwise relative regularized-weight error

Use the independent variables t,h,C,u in L=V1[4t^2 R-(1-t+2delta)].
The rectangular bounds .414<=t<=.4143, .706<=h<=.71, .414<=u<=1,
C>=359/360-.4143 contain the finite and critical points and straight
segments between them. The M10 lower-gap argument uses only these
rectangular endpoints and delta<=.07, and hence L>.07V1 throughout
the segments. Its use does not require the artificial intermediate
parameters to satisfy the physical phase equation.

The reviewed logarithmic partial bounds are

    |partial_t log L|<200, |partial_h log L|<50,
    |partial_C log L|<2, |partial_u log L|<16.         (1)

The t,u estimates and positivity are from M10/M11. The absolute h
estimate is the rational quotient bound in the M13 tail proof; it used
the full u<=1 rectangle. Its constant is recomputed in the new ledger.
The C estimate follows from partial_C log L=-1/C.

The M11 scalar and new M14 kernel estimates give

    |t-sigma|<=e^2/8, |h-eta|<.26e,
    |C-(1-sigma)|<.51e, |u_e(s)-u0(s)|<e/2.          (2)

Integrating the gradient along the straight segment, (1),(2) imply

    |log[L_e(u_e(s);delta)/L0(u0(s);delta)]|
       <(22.02+25e)e.                               (3)

Since A0/e=J(t)*(1-exp(-e))/e and 0<J_t/J<7,
the inequalities1-e/2<(1-exp(-e))/e<1 and
-log(1-z)<=z/(1-z) give

    |log[(A0/e)/J0]|<e/(2-e)+7e^2/8<.51e.          (4)

Consequently, uniformly in s>=0 and delta in[0,1/20],

    |log[((A0/e)L_e)/(J0 L0)]|<23e,
    |((A0/e)L_e)/(J0 L0)-1|<1/125.                  (5)

The final rational bound uses exp(23e)-1<=23e/(1-23e)<1/125
on e<=17/51200; negative logarithmic errors are smaller. Positivity
permits summing (5) against e*T_n*K_n, giving

    |S_e-Stilde_e|<(1/125)Stilde_e.                  (6)

## Critical mass and the remaining approximation target

At both phase endpoints, the frozen critical integral enclosures give

    0<S0(delta)<3, 0<=delta<=1/20.                   (7)

Indeed B(0,delta)=B00+2delta*sigma, while
Fhat=F0+2delta*(1+P0). Thus S0(delta) is decreasing in delta, and
its upper bound is F0-B00 at delta=0. The ledger checks it is below3
for both endpoints. Positivity also follows from its integral definition.

Suppose now that the following remaining estimate can be proved at both
endpoints uniformly for N>=512:

    |Stilde_e-S0(delta)|<1/8.                         (8)

This is NOT established in this note. Equations(6)--(8) would give

    |S_e-S0(delta)| < (3+1/8)/125+1/8 =3/20.         (9)

The M13 boundary partial derivative bound at fixed delta gives
|B(e,delta)-B(0,delta)|<7e. Thus(9) implies

    |F_e-Fhat|<3/20+7*(17/51200)<4/25.              (10)

Combined with the critical margins>1/4 and<-1/5, this would prove
F_N(.8)>9/100 and F_N(.9)<-1/25 for every N>=512.
Existence then follows by continuity and M13 gives uniqueness.

The practical next target is(8), a comparison of the exact discrete
Gamma/product mass against the critical mass with the SAME critical
weight. It avoids multiplying separate moment errors by four. The
Gamma cumulative-mass sandwich and sharp smooth-product comparison
are intended inputs, but their integrated numerical allowance still
has to be proved. Finite32<=N<=511 coverage is also still required.

The rational/interval constants can be replayed with
`python -m proofs.m14_combined_weight_transfer`.
