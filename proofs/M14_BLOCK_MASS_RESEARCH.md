# M14 research: exact block masses for endpoint enclosures

Status: research reduction, not an endpoint-sign certificate. Independent
review and effective uniform block enclosures remain outstanding.
Use the M13 real sector, integer N>=32 and theta in[.8,.9].

The bare recurrence admits an exact primitive for every integer n>=0:

    Q_n=(n-a)T_n/(1-beta), Q_-1=-(b+1)/(1-beta),
    Q_n-Q_(n-1)=T_n>0.

Indeed T_(n-1)/T_n=(b-n+1)/(a-n+1), and substitution gives
[(n-a)+(b-n+1)]/(1-beta)=1. The n=0 case uses the explicit Q_-1.
The noninteger strip ensures that the recurrence denominators are nonzero.
Thus for any finite integer block0<=l<=r,

    M(l,r):=sum_(n=l)^r T_n=Q_r-Q_(l-1)>0.            (1)

Let D_n=K_n L_W(u_n). The accepted M6/M11 secant inequality gives
K_(n+1)/K_n=r_geom R_e(ne)<1. Here r_geom denotes the geometric
ratio, to distinguish it from the block's upper index. Since e>0,
u_n=U(t,exp(-ne)) decreases with n. The positive L_W increases in u
by M10, hence D_n is positive and strictly decreases with n. It follows
without differentiating in theta that

    A0 D_r M(l,r) <= sum_(n=l)^r J_n
                  <= A0 D_l M(l,r).                  (2)

This gives exact block enclosures of each finite mass, including blocks
across the Gamma crossing. A block touching n=N orN+1 must retain the
actual primitive endpoints rather than replacing the singular shape by
a maximum of individual T_n. The identity already includes its mass.

With a finite partition of0..60N, summing (2), adding an enclosure of B,
and adding a separately certified positive tail could enclose F_N(.8)
and F_N(.9). For an upper tail VALUE bound, M13_TAIL_PHASE_BOUND gives

    S_tail < (5/6)(151/1000)*2*exp(-8.7)
           <151/3000000,

using A0=J(1-exp(-e)), r_geom<=exp(-e), Pi<=1 and exp(8.7)>5000.
This bound controls value rather than derivative and preserves positivity.

The reduction does not yet give a usable uniform enclosure for D_l,D_r
or Q_r-Q_(l-1) at index-dependent block boundaries. In particular:

- Bounds must hold for every integer N in their declared domain.
- Intervals for floors/ceilings must cover changes of block indices.
- Interval subtraction of Q endpoints may lose accuracy even though
  the true block mass is positive; positivity is not a numerical enclosure.
- A point scan or one successful finite partition at N=32 cannot certify
  every larger index.

The two desired endpoint signs are still unproved uniformly. This note
records an exact reduction for the next endpoint research step and does
not contribute to the accepted M13 derivative certificate.
