# M7: effective derivative control from real error and complex boundedness

Status: conditional candidate for independent review. The missing input
is the explicit holomorphic moment bound (H), not a presumed derivative
of the real remainder.

Let Omega={theta:dist(theta,[.8,.9])<.02}. Suppose for every integer
N>=10^120 that P_N,H_N are holomorphic there and

                sup_Omega(|P_N|+|H_N|)<=10^10.         (H)

Then on the real T=[.8,.9],

       |P_N'-P0'|+|H_N'-H0'| <9/1000<1.              (1)

Together with M7_UNIQUENESS_TRANSFER, this would give the explicit
uniqueness/simplicity threshold10^120. Until (H) is proved with its
domain and reviewed, this is not an accepted finite uniqueness theorem.

## 1. A bound for the critical functions on Omega

On this complex neighborhood, Re(theta) in(.78,.92) and
|Im(theta)|<.02. The exact critical integral enclosures imply

 pre1<.5, pre2<.7, post1<.5, post2<.6,
 A=sigma^-2<6, d=1-sigma<.6, sigma²<.18.

All four integrals are positive. Since .70<eta<.71, we have
.07<Re(theta)-eta<.22<1/2. For complex z=x+iy,
|sin z|²=sin²x+sinh²y, whereas |sin z|<=cosh|y|.
Consequently the denominator of B(theta) satisfies

 |sin(pi*(eta-theta))|>.14

by sin(pi*x)>=2x on[0,1/2]. Its numerator has modulus less than2,
using pi<4 and cosh(.08)<2 (the exponential series suffices).
Therefore |B|<600/7<86, and the exact affine formulas give

 |P0|<.6+6*.5+86*.5=46.6,
 |H0|<.18*(3+6*.7+86*.6)=10.584.

In particular |P0|+|H0|<100 on Omega. The functions are holomorphic
there since the sine denominator is separated from zero.

## 2. Second derivatives from a genuine analytic bound

Set f=P_N-P0 and g=H_N-H0. Assumption (H) and the preceding estimate
give |f|+|g|<10^10+100 throughout Omega. Every disk of radius rho=.01
centered on a point of T is contained in Omega. Cauchy's integral formula,
applied on the same circle to both components and then summed, gives

 |f''(theta)|+|g''(theta)|
 <=2(10^10+100)/rho²<10^16=:M, theta in T.             (2)

Using the same circle is why a bound on the sum of component moduli
suffices. No complex convergence rate is used.

## 3. The real error and an inward finite difference

For N>=10^120, e_N<1/N and the accepted M6 real error bound with B=10^12
give uniformly on T

 |f|+|g|
 <=10^9 e^(1/4)+10^21 sqrt(e)+10^14 e
 <10^-21+10^-39+10^-106<2*10^-21=:E.                 (3)

The common domain e<=10^-10 is satisfied. Take h=10^-18. At each
theta in T, at least one of theta+h and theta-h lies in T. Choose
that direction. Taylor's theorem with integral remainder on the real
segment, and (2), gives

 |f'(theta)|+|g'(theta)| <=2E/h+Mh/2
                         =.004+.005=.009.             (4)

This includes both endpoints of T by using the inward direction. It is
a quantitative interpolation argument with a separately justified second
derivative bound; it does not differentiate an O-symbol or a C0 inequality.

The powers and constants are deliberately conservative. The intended
remaining proof obligation is precisely (H), including normal convergence
and absence of source singularities on the fixed complex neighborhood.
