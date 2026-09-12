# M12 candidate: uniform noncancellation throughout the real W sector

Status: new lemma awaiting independent review. It concerns every real
N>=32, theta in[.8,.9]. It neither supplies zeros nor proves uniqueness.
The claim is: at every zero of F in this sector, 1+P<-2.

Use the exact regularized moments from M7/M8 and the M10 scalar/weight
lemmas. Write C=q-t, D=1-tq, h=tq/C, f(u)=u/(1-tu), and

    gq=t-Dq<0, z0=1/gq,
    L1=f(h)/(1-h), S0=-t D^2/gq,
    B1=C/gq+L1 S0,
    B2=f(q)C/gq+f(h)L1 S0,
    Q=q t^2(1-q^2)(1-t^2)>0.

On the complete real phase band, a,b lie in the same integer strip.
The M10 beta bounds and M11 real secant argument imply T_n>0 and K_n>0,
hence z_n=z0 T_n K_n<0 for every n>=0. The regularized series converge:
for each fixed positive e, their recurrence tends to a ratio of modulus
less than1 and their rational weights stay bounded. This also gives local
analytic convergence on source-free compact neighborhoods, as in the
accepted M7 tail argument. No critical-endpoint convergence is asserted.

Put

    S=Q sum_(n>=0)(-z_n)V1(u_n)>0,
    Rbar=[sum(-z_n)V2(u_n)]/[sum(-z_n)V1(u_n)].

The exact weight ratio R=V2/V1 and M10 scalar boxes give

    Rmin<Rbar<Rmax,
    Rmax=h_h/(1-t_h h_h)
          +(1-h_l)/[(1-t_h)(1-t_h h_h)],
    t_h=.4143, h_l=.706, h_h=.71.

These inequalities follow by averaging against positive weights.
In particular the moments are exactly

    P=B1-S, H=t^2(B2-Rbar S).

Let cW=1-t+2delta_D and ell=4t^2 Rbar-cW. By M10,

    ell>.07,
    ell<4t_h^2 Rmax-(1-t_h)<.6.                       (1)

The following scalar interval certificate holds on a box enclosing
every physical e in(0,1/180]:

    sigma-(1/180)^2/8 <=t<=sigma,
    359/360<=q<=1,
    1+B1>0,
    Zmin:=1+t^2 B2-t^2 Rmax(1+B1)>.3.                 (2)

The companion I384 checker recomputes all the displayed rational
expressions and checks the denominators before division. Its retained
intervals are approximately B1 in[-.66734,-.45552], t^2B2 in
[-.53457,-.47956], and Zmin in[.30503,.42244]; the exact dyadic
endpoints, rather than these readable outward decimals, prove (2).
Since 1+B1>0, replacing Rbar by Rmax gives

    Z:=1+t^2 B2-t^2 Rbar(1+B1)>=Zmin>.3.              (3)

The W denominator has the exact rearrangement

    F=cW P-4H-(3+t)+2delta_D
     =-ell(1+P)-4Z.                                 (4)

Indeed S=B1-P and cW+(3+t)-2delta_D=4. If F=0, (1)--(4) give

    1+P=-4Z/ell < -4*.3/.6=-2.                       (5)

Thus cancellation with the W numerator is impossible at any such zero.
The same inequality holds wherever F>=0. This is a uniform real-sector
statement, rather than extrapolation of finite pole data or the large-N
asymptotic moment bounds. At a zero it ensures W has a pole, but says
nothing about the zero's existence, number or multiplicity.

Reproduce the interval and rational allowances with
`python -m proofs.m12_noncancellation_bounds` without optimization.
The averaging and algebraic argument above require separate review.
