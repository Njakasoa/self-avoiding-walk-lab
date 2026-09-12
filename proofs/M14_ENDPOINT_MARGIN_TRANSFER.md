# M14 candidate: useful directed and critical endpoint margins from N=512

Status: component for independent review. This gives a concrete sufficient
moment-approximation target, not an existence theorem or a new threshold.
All N are integers and theta lies in[.8,.9].

## Uniform directed reciprocal bound

Set t_ref=414213556/10^9. The exact phase enclosure in the accompanying
producer gives0<e_ref<.01 and a(t_ref)<512.8. The directed-ramp series has
positive terms

    d_k=t q^k/(beta_dir+gamma_dir q^(2k)),
    beta_dir=(1-t-tq)/(1-q^2),
    gamma_dir=q[t-q(1-t)]/(1-q^2).

The checker verifies0<q<1, beta_dir>0, beta_dir+gamma_dir>0. Every
denominator is a convex combination of these two positive endpoints.
It sums exactly16384 terms using outward dyadic intervals and proves

    sum_(k=0)^16383 d_k >19.                           (1)

The omitted terms are positive; no upper-tail estimate is needed for
this LOWER bound on D_R. For any N>=512 and theta in[.8,.9], the accepted
M5 phase order gives t_N(theta)>t_ref. M10 directed monotonicity and(1)
therefore imply

    D_R(t_N)>19,  0<delta_D=1/(1+D_R)<1/20.            (2)

The reference point is an order comparison, not interpolation of a scan.

## Critical profile with the actual directed parameter

Let sigma=sqrt(2)-1 and let P0(theta),H0(theta) be the accepted critical
moment profiles from the frozen M5 integral certificate. Define

    Fhat(theta,delta)=(1-sigma+2delta)P0(theta)
                       -4H0(theta)-3-sigma+2delta
                    =F0(theta)+2delta[1+P0(theta)].   (3)

The source-frozen integral enclosures, exact Machin pi interval and sine
Taylor remainders give, for every0<=delta<=1/20,

    Fhat(.8,delta)>1/4,
    Fhat(.9,delta)<-1/5,
    -15/2<1+P0(theta)<0 at both endpoints.             (4)

The interval for delta is independent of theta, and it includes the
actual directed parameter by(2). No asymptotic approximation to D_R is
used. Broadening the old bound delta<.07 would lose the left margin;
the explicit reference is needed.

## Conditional transfer to the exact denominator

Suppose, at the two phase endpoints and for every N>=512, that

    |P_N-P0|+|H_N-H0|<1/25.                           (5)

This is the UNPROVED remaining hypothesis. Set delta to its exact value
at each physical point. Direct subtraction of(3) from the exact F gives

    F_N-Fhat=(1-t+2delta)(P_N-P0)-4(H_N-H0)
                 +(sigma-t)(1+P0).                  (6)

Here0<1-t+2delta<4, sigma-t<=e^2/8, and e<.17/N.
Using(4),(5) and N>=512, the exact rational ledger gives

    |F_N-Fhat|<4/25+(15/2)(17/51200)^2/8<17/100.      (7)

Consequently(5) would imply F_N(.8)>2/25 and F_N(.9)<-3/100.
The intermediate value theorem would then supply one zero in every
N>=512 band; M13 and M12 would give uniqueness, simplicity and absence
of cancellation. A complete certified finite treatment of32<=N<=511
would still be required for full coverage from32.

Neither that finite coverage nor(5) is proved here. The purpose of this
component is to replace the vague demand for a useful effective error by
the concrete joint error target1/25 on e<17/51200, keeping the actual
directed correction. The exact producer is
`python -m proofs.m14_endpoint_margins`; its arithmetic PASS must not be
interpreted as proof of hypothesis(5).
