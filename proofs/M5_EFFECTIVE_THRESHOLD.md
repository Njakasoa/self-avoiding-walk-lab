# M5 candidate: an explicit first index for existence of W poles

Status: candidate; independent review required for the aggregation below.
The threshold here guarantees existence and noncancellation. The separately
accepted eventual uniqueness, simplicity and residue theorem remains
non-effective. No practical sharpness is claimed for this first threshold.

Put B=10^50, A=exp(10^54), and let e=e_N(theta), theta in [.8,.9].
The component inputs are M5_EFFECTIVE_KERNEL.md, M5_EFFECTIVE_GAMMA.md
and M5_EFFECTIVE_WEIGHTS.md. This note is not accepted until each input
and the aggregation have been independently checked.

## 1. Real quantitative moment bound

The proposed explicit statement is

 |P_N(theta)-P0(theta)|+|H_N(theta)-H0(theta)|
       <= exp(10^60) e^(1/20),     log(1/e)>=10^100.       (E)

Only real variables are used here. Set rho=e^(1/4) and S=4+log(1/e),
and compare the exact sums to the critical profile on the mesh x_n=n e.
Using this mesh avoids any change-of-mesh constant. The phase relation
s_g=e(N+theta) is exact. The phase-domain certificate already gives
e<1/N, and the kernel lemma gives |s_g-s*|<=4*10^5 e.
The domain log(1/e)>=10^100 implies e<=10^-100, a=s_g/e>=200,
rho<1/20, rho>2*(4*10^5 e)+20e, and
1/20+4*10^5 e+e<s_g/2. Thus both the fixed crossing window
and the moving cutoff satisfy the Gamma lemma's domain conditions.

Here is the constant ledger for the sum-to-integral comparison.

1. On x_n<=5, the kernel lemma gives
   |sum_(j<n) log R_e(je)|<=2B*x_n<=10B.
   Also 0<r<=1 and |z0|<10. The effective Gamma domination, with
   eta_e in [.70,.72], implies

       |z_n|<=A (e+|x_n-s*|)^(-19/25)   if |x_n-s*|<=1/20.

   Indeed the Gamma factor is bounded by a fixed constant times
   (s_g/(e+|x_n-s_g|))^eta_e; moving its center by at most
   4*10^5 e loses at most 10^6. All these factors, multiplied by
   exp(10B), are less than A. Enlarging the power from eta_e<.72
   to19/25=.76 only enlarges the bound on this window.

2. Away from |x_n-s*|<rho, the effective Gamma ratio estimate and
   the kernel lemma imply the relative approximation

       z_n=Z_theta(x_n)(1+u_n),
       |u_n|<=10^60 E0,
       E0=e/rho+(1+S)sqrt(e)
                     +e(|log rho|+log(2+S)), x_n<=S.     (R)

   For detail, the Gamma ratio logarithmic error is bounded by a
   constant times e/rho; replacing s_g by s* costs at most
   10^7 e/rho, and replacing eta_e by eta costs at most
   10^52 e(|log rho|+log(2+S)). The sine multiplier logarithm has
   derivative bounded by100 on theta-eta_e in [.08,.20]; its
   error is at most100B e. Kernel quadrature costs at most
   B S sqrt(e)+B S e, the expansion of r at most B S e,
   and z0 at most100B e. Their sum is at most10^59 E0.
   It is <1/10 on the stated e domain. The inequality
   |exp(u)-1|<=2|u| for |u|<=1/10 gives (R).

3. The discrete crossing mass is at most
   100A(rho+e)^(6/25), by comparison of the decreasing function
   x^(-19/25) with its integral. The critical crossing mass has
   the same upper bound. This counts both sides and the closest
   lattice points; the exponent6/25 equals1-19/25.

4. At the first mesh point beyond4, (R) and the critical-profile
   bound give |z_n|<=A. For x_n>=4, g_e(x_n)>0 and delta>0,
   while r=1-(1-exp(-e))/(1-tq)<=exp(-e).
   Thus the exact recurrence gives |z_n|<=2A exp(-(x_n-4)).
   The critical ODE has logarithmic derivative
   -lambda-kappa/g0<-1 on s>=4, giving the same tail bound.
   Including the bounded weights, each tail after S is bounded by
   A² exp(-(S-4)).

5. The effective weight lemma bounds the weights, their perturbations,
   and the changes in the exact boundary terms and Q/e by10^20
   times the appropriate factor (one, e, or sqrt(distance)).
   Critical weighted profiles have an integrable absolute majorant
   of total mass <=A. Their Holder constant off the crossing is
   at most A rho^(-1-eta). Hence their Riemann-sum error is at most
   10A(1+S)sqrt(e)rho^(-1-eta), including the two boundary cells.
   Applying this same bound to the absolute weighted profile shows
   that its discrete mass off the crossing is <=2A: its integral
   mass is <=A and the displayed error is <A on the stated domain.
   This is the discrete mass multiplying the relative error in (R).
   The exact regularization removes the apparent weight pole, so
   no uncancelled denominator is being estimated here.

Multiplying and adding these five estimates, the absolute moment error is
bounded by

 A^4 [ E0+(1+S)sqrt(e)rho^(-1-eta)
          +(rho+e)^(6/25)+exp(-(S-4)) ].                 (M)

The four powers of A cover the fixed weight/boundary constants, the
critical mass and the sum of all terms above; the coefficients10^60,
100,10^20 and their products are smaller than A. None grows with S.
All relative exponential errors in (R) are small before this step; a
bound exp(B*S) at a growing S is not used.

Write L=log(1/e)>=10^100. Since eta<.71, the nontrivial powers after
substituting rho=e^(1/4) are at least .0725 and .06. The factors
5+L, L/4+log(6+L), and2^(6/25) are each <=exp(L/1000)
on this range (differentiate their logarithms and check the left
endpoint). Each term in the bracket in (M) is consequently at most
exp(-.059 L), except terms with still larger powers. Their sum is
<=exp(-L/20). Thus (M) is <=A^4 e^(1/20), which is smaller than
the right side of (E).

## 2. An explicit W existence threshold

A sufficient first index is

                  N0 = 2^(10^120).                     (N0)

This is an integer specified without constructing its decimal expansion.
For N>=N0, the certified e_N<1/N gives

 L=log(1/e_N)>log N> (69/100)*10^120 >10^100.

By (E), log of the moment error is at most
10^60-(69/2000)*10^120<-1000. The error is therefore <10^-100.
The directed certificate gives, since N>=2^108,

 0<1-D_I <=sigma/logN+31/(logN)^2 <1/logN <10^-100.

On the smaller bracket T*=[1739/2000,109/125], the exact critical
certificate gives

 F0(left)>7*10^-4,    F0(right)<-3*10^-4,
 -5<1+P0(theta)<-4,  |P0(theta)|<6.

The P0 enclosure on the whole bracket is included in the coefficient
certificate: B is increasing and the integral coefficients are positive.
Using |t-sigma|<=e²/10 and the exact formula

 F_N=(1-t)P_N-4H_N-(3+t)+2(1-D_I)(1+P_N),

we obtain |F_N-F0|<10^-90 on this bracket, and 1+P_N<-3.
Thus F_N has opposite endpoint signs and every zero there is a
noncancelled pole of W=-1-(1+P_N)/F_N.

There are no source poles on the whole [.8,.9] band: a=N+theta,
b=N+theta-eta_e are separated from integers by at least .08, since
eta_e in [.70,.72]. Other kernel denominators are positive and
separated on the physical branch, and the geometric tail gives local
analyticity. The phase map is strictly increasing in t by the exact
phase-domain certificate. Consequently each N>=N0 gives at least one
real W pole in the corresponding band. The bands for different N are
disjoint and accumulate at sigma.

This explicit existence result complements, but does not make effective,
the accepted eventual uniqueness and simplicity theorem. A smaller useful
N0, or an explicit uniqueness threshold, is a further optimization problem.
