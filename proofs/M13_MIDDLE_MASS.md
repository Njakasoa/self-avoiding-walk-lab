# M13 candidate: a uniform negative contribution from the middle sum

Status: analytic component for independent review. Let N>=32 be an integer,
theta in[.8,.9], and J_n=A0 T_n K_n L_W(u_n)>0. Define

    S_mid=sum_(n=N+1)^(60N) J_n,
    S_sub=sum_(n=N+1)^floor(3N/2) J_n.

We prove S_sub>1/70 and S_mid,theta<-3/56. Other parts of F are excluded.
All inputs are the reviewed M10--M12 real lemmas, not a finite scan.

## A lower bound on the smooth product

The M11 inverse-kernel identity is

    R_e(s)=(ug/h)*(1-uh)/(1-u*ug)*M(s,sg)/M(s,sh),
    .70<ug,h<.71, 0<h-ug<.51e, 0<u<1.

The elementary log inequalities log(1+x)<=x and
log(1-x)>=-x/(1-x), and -1<=partial_a log M(s,a)<=0, give

    log R_e(s)>-[.51/.70+.51/.29+.72]e>-(13/4)e.

This holds on the entire physical kernel ray. The real scalar bound
|(log r)_e|<2, together with r(0)=1, gives r>exp(-2e). Hence

    K_n=r^n product_(j<n)R_e(je)>exp(-(21/4)ne).

In the subwindow n<=3N/2, ne<51/200. The rational exponential Taylor
majorant recorded by the checker proves exp(1071/800)<4, so

    K_n>1/4.                                             (1)

## An elementary lower bound on the bare product

Write beta in(.70,.72), v=theta-beta in(.08,.20), and
n=N+1+k, with 0<=k<=N/2. The exact product is

    T_n=[theta/v] product_(l=1)^N (l+theta)/(l+v)
          * product_(l=1)^k (l-theta)/(l-v).

For 0<beta<1, concavity gives (1+x)^beta<=1+beta*x and
(1-x)^beta<=1-beta*x, for x>0 and 0<x<1 respectively. Thus

    product_(l=1)^N (l+theta)/(l+v)
       >=[(N+1+v)/(1+v)]^beta.

When k>=1, separate the first post-crossing factor and telescope the rest:

    product_(l=2)^k (l-theta)/(l-v)
       >=[(1-v)/(k-v)]^beta.

Both formulas include their empty products correctly. Also

    theta/(theta-beta)>9/2,
    (1-theta)/(1-theta+beta)>5/41,
    (N+1+v)/(k-v)>2, (1-v)/(1+v)>2/3.

The first two bounds follow by monotonicity in theta and beta, using
the same physical parameters in each ratio. Therefore for k>=1,

    T_n>(45/82)(4/3)^beta>(45/82)(6/5)=27/41.             (2)

The last inequality follows from beta>.7 and the exact rational check
(4/3)^7>(6/5)^10. For k=0, T_n>theta/v>9/2, so (2) also holds.

## Uniform prefactor and regularized weight

From the exact identity A0=J(t)(1-exp(-e)),
J(t)=t(1-t^2)/(1-t-t^2), and the M11 proof J_t>0,

    A0/e>J(.414)(1-1/360)>41/50.                        (3)

For n in the subwindow, exp(-ne)>1-ne>149/200. The physical kernel
increases in both t and its second argument. An exact I384 square-root
evaluation gives U(.414,149/200)>.63, hence u_n>.63.

Use the independent variables t,h,u,C in the rational formulas for V1,R.
Both R and V1 increase in t,h,u, while V1 decreases in C. The h,u
derivatives were proved in M11. Positivity of the remaining t derivative
follows directly from the positive terms of R, and

    partial_t log V1
       =u/(1-tu)-uh/(1-tuh)+h/(1-th)>0.

Since C=q-t<1-.414, set t_l=.414,h_l=.706,u_l=.63,C_u=1-t_l.
The following lower allowances are rational:

    R_l=h_l/(1-t_l h_l)
          +u_l(1-h_l)/[(1-t_l u_l)(1-t_l u_l h_l)],
    V_l=(1-t_l u_l h_l)
          /[C_u(1-t_l u_l)(1-t_l h_l)(1-h_l)],
    L_W>V_l[4t_l^2 R_l-(1-t_l+.14)]>3/2.               (4)

All denominators and the bracket are positive; the checker verifies the
last inequality exactly, approximately1.52518>1.5.

There are floor(N/2)>=31N/64 subwindow terms. The real phase box gives
Ne>.15N/(N+.9)>=48/329. Combining (1)--(4) yields

    S_sub>(31/64)(41/50)(27/41)(1/4)(3/2)(48/329)
         =7533/526400>1/70.                            (5)

## A stronger derivative margin in this subwindow

Before M11 replaces je by10.2, its factor estimate is

    |d_e log R_e(je)|<7.071+.18je.

In the present subwindow je<51/200, so this is below7.12. Therefore

    |partial_theta log Pi_n|<(7.12)(.255)/N,
    |partial_theta log r^n|<.51/N,
    partial_theta log(A0 L_W)<11/N.

Their sum is below13.4/N. The bare-product bound now gives

    partial_theta log J_n<-1435/342+13.4/N
                         <-15/4.                       (6)

Every other term of S_mid still has negative derivative by M11. The
finite index sets are fixed when theta is differentiated. Dropping those
other negative terms and using (5),(6),

    S_mid,theta<-(15/4)S_sub<-3/56.                    (7)

This is a bound on one part of F_theta. Pre-crossing, boundary and
distant-tail contributions must still be controlled before a complete
denominator derivative claim. Run the rational/I384 allowance checker
`python -m proofs.m13_middle_bounds` without optimization.
