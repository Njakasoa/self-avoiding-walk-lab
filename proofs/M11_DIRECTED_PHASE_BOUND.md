# M11 candidate: a small uniform directed phase derivative

Status: new analytic lemma for independent review. All statements concern
real N>=32, theta in[.8,.9], e=e_N(theta). This does not establish the
sign of the complete W denominator derivative.

## Exact summand and favorable derivative

Use the exact M5_DIRECTED_REFINED representation, for k>=1,

    d_k = r a(e) b(ke) / [k(1+u_k)],
    r=t/alpha, c=(1-t)/alpha, alpha=1-t-tq,
    q=exp(-e/2), a(e)=(1-exp(-e))/e,
    b(x)=x/[2sinh(x/2)],
    u_k=c(1-exp(-e))/(exp(ke)-1).

The k=0 term is d_0=t/(1-t). The previously proved derivative majorant
in M5_DIRECTED_REFINED justifies termwise differentiation on every
compact positive e interval. No differentiation at e=0 is used.
M10_BETA_REAL supplies 0<e<1/180 and |e_theta|<e/N.

On this real interval, .414<t<.4143, alpha>1-2*.4143>.17.
The implicit equation A(t)=2cosh(e/2) and A'(t)<=-4 give

    t_e<0, |t_e|<=sinh(e/2)/4<e/7.

For the latter inequality, sinh(x)<exp(x)-1<=x/(1-x) for
0<x<=1/360, hence |t_e|<e/[8(1-e/2)]<e/7.
Direct cancellation in the quotient derivatives gives

    r_e=(t_e+t^2 q_e)/alpha^2<0,
    c_e=[q t_e+t(1-t)q_e]/alpha^2<0.

Consequently r<5/2 and

    |r_e| < [(1/180)/7+.4143^2/2]/.17^2 <3.

Also a(e)=integral_0^1 exp(-ve)dv, so 0<a<=1 and -1/2<a_e<0.
Thus (ra)_e<0 and |(ra)_e|<17/4.

To determine the sign of (u_k)_e without cancellation bounds, put z=exp(-e).
For an integer k>=1,

    (1-exp(-e))/(exp(ke)-1)
       = z^k / (1+z+...+z^(k-1)).

Its logarithmic e derivative is -k plus a weighted average of
0,...,k-1, hence is at most -1. Since c_e<0, (u_k)_e<0.
The derivative of 1/(1+u_k) is therefore positive. Dropping this
favorable contribution yields the one-sided bound

    -(d_k)_e <= (17/4)b(ke)/k + (5/2)[-b'(ke)].       (1)

This step does not take the absolute value of each denominator derivative.

## Two sums with small constants

For x>0, elementary exponential inequalities give

    0<-b'(x)<b(x)/2,
    b(x)<(1+x)exp(-x/2).                             (2)

Indeed -b'/b=coth(x/2)/2-1/x is positive because
y cosh(y)>sinh(y). Its upper bound1/2 follows from exp(x)>1+x.
The second bound follows from x/(1-exp(-x))<1+x.

Using q=exp(-e/2), the geometric sums imply

    e sum_(k>=1) b(ke)
      < e q/(1-q)+e^2 q/(1-q)^2 <=2+4=6.

Here exp(e/2)-1>=e/2 and 2sinh(e/4)>=e/2 prove the
two respective allowances. Thus

    e sum_(k>=1) [-b'(ke)] <3.                       (3)

The logarithmic series and (2) also give

    sum_(k>=1) b(ke)/k
       < -log(1-q)+e q/(1-q)
       < log(3/e)+2.

For the last bound, 1-exp(-e/2)>=e/2-e^2/8>e/3.
The function e[log(3/e)+2] increases on0<e<=1/180.
Moreover log540<7 because exp(1)>5/2 and (5/2)^7>540.
Therefore

    e sum_(k>=1) b(ke)/k <9/180=1/20.               (4)

For the omitted k=0 term,

    e |(d_0)_e| < e^2/[7(1-.4143)^2].

Combining (1),(3),(4), exact rational arithmetic gives

    -e D_R,e < 17/80+15/2
                  +(1/180)^2/[7(1-.4143)^2] <8.     (5)

M10_DIRECTED_MONOTONICITY proves D_R increases with t; analyticity and
t_e<0 imply D_R,e<=0. Thus (5) proves the absolute derivative bound

    |D_R,e|<8/e,       0<e<=1/180.                  (6)

This improves the older1500/e allowance on the narrower stated domain.

## Phase transfer and the combined weight

Since e_theta<0, D_R,theta>=0. The M10 bound delta_D<7/100,
delta_D=(1+D_R)^(-1), and |e_theta|<e/N imply

    -49/(1250N)<delta_D,theta<=0.                   (7)

For the positive weight L_W=V1[4t^2 R-(1-t+2delta_D)], the partial
derivative with only delta_D varying is exactly

    partial_delta_D log L_W=-2/[4t^2 R-(1-t+2delta_D)].

The M10 uniform gap exceeds7/100. Hence the contribution of the
directed parameter to the phase logarithmic derivative satisfies

    0 <= (partial_delta_D log L_W)delta_D,theta
        < (200/7)(49/1250)/N =28/(25N).              (8)

This isolates one previously uncontrolled positive contribution. Changes
in t,q,u, the smooth product, the boundary terms and the distant tail
still require their own estimates before a full F_N derivative claim.

The exact arithmetic allowances are replayed by
`python -m proofs.m11_directed_phase_bounds`. Its output does not replace
the analytic proof of (1)--(8).
