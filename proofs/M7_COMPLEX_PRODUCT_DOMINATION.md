# M7: an elementary bound for the complex bare product

Status: candidate for independent review. This lemma addresses the bare
finite product only; the smooth factor and physical phase inverse still
need their own complex estimates.

Let N be a nonnegative integer, a=N+theta, b=a-eta_e, and assume

 Re(theta) in[.78,.92], |Im(theta)|<=.02,
 Re(eta_e) in[.70,.72].

For n>=0 set T_n(a,b)=product_(j=0)^(n-1) (a-j)/(b-j), with T_0=1.
Put A=Re(a), beta=Re(eta_e). Then

               |T_n(a,b)| < 2 T_n(A,A-beta).           (1)

The right side is a positive real product. In particular any available
real Wendel bound for its exponent beta gives complex domination with
only the fixed factor2. No complex Gamma asymptotic remainder is needed
for this domination statement.

Indeed Re(b)=N+Re(theta)-beta lies strictly between N and N+1,
as does A. Thus every corresponding real numerator and denominator
have the same sign and none vanishes. Since |b-j|>=|Re(b)-j|,

 |T_n(a,b)|/T_n(A,A-beta)
 <=product_(j<n) sqrt(1+y²/(A-j)²), y=Im(theta).

For u=Re(theta), comparison of a decreasing positive function with
its integral gives

 sum_(j>=0)1/(A-j)²
 <=sum_(k>=0)1/(u+k)²+sum_(k>=0)1/(1-u+k)²
 <=1/.78²+1/.78+1/.08²+1/.08 <172<200.

This bound even includes extra negative j terms and is therefore valid
for every N. Using log(1+x)<=x for x>=0, the logarithm of the product
multiplier is at most y²*200/2<=1/25. Finally exp(1/25)<2, for example
by exp(x)<=1/(1-x) on0<=x<1 and25/24<2. This proves (1), including
n=0 by the empty-product convention.

Only the real part of eta_e is restricted: its imaginary part can only
increase |b-j| relative to the lower bound used above. Holomorphy of the
physical eta_e and its domain still need proof before applying the lemma
to phase derivatives. The result is a bound, not an asymptotic comparison
to the critical profile.

## Real product envelope without Gamma remainder estimates

For the real product in (1), write A=N+u, beta in[.70,.72],
v=u-beta in[.06,.22], and N>=1. For every n>=0, put d_n=|n-A|.
Then

 T_n(A,A-beta)<=300*((A+1)/(1+d_n))^beta.              (2)

For1<=n<=N, all factors are1+beta/(A-beta-j). Let
c=A-beta-n+1>=1.06. The decreasing harmonic sum estimate yields

 log T_n <= beta*(1/c+log((A-beta)/c)).

Here exp(beta/c)<3, c=(1+d_n)-beta>=.28*(1+d_n),
and A-beta<A+1. Since beta<1, this gives

 T_n<12*((A+1)/(1+d_n))^beta.

The same bound holds for n=0, where the product and the ratio are both1.
At n=N+1 the extra factor is u/v<16, so
T_(N+1)<192*(A+1)^beta. For n=N+1+k, k>=0, the remaining product is

 product_(l=1)^k (1-beta/(l-v)).

Its logarithm is at most -beta*sum_(l=1)^k1/(l-v), and the decreasing
integral lower estimate gives

 sum_(l=1)^k1/(l-v)>=log((k+1-v)/(1-v)).

As k+1-v=d_n+beta>=.7*(1+d_n) and1-v<1, the remaining factor is
at most[1/(.7*(1+d_n))]^beta. Since192/.7<300, this proves (2)
on the post-crossing side also. The empty k=0 product is included.

Consequently, for d_n<=A, (2) is at most
300*((A+1)/(1+d_n))^(3/4); for d_n>A it is at most300.

## An explicit compact mesh mass

Let epsilon>0 satisfy epsilon<=1 and epsilon*(A+1)<1/5.
For the indices n with0<=n*epsilon<=4,

           epsilon*sum_n T_n(A,A-beta)<10^4.          (3)

Indeed, the constant300 part contributes at most
300*epsilon*(4/epsilon+1)<=1500. For the remaining cusp envelope,
there is at most one mesh point per side in each distance interval
[k,k+1). Therefore

 sum_(d_n<=A)(1+d_n)^(-3/4)
 <=2*sum_(k=0)^floor(A)(1+k)^(-3/4)
 <=2+8*(A+1)^(1/4)<=10*(A+1)^(1/4).

Its contribution is at most3000*epsilon*(A+1)<600. The sum is thus
below2100, leaving a generous margin in (3). Combining with (1) gives
the complex compact mass bound below2*10^4. These are elementary
finite-product and power-sum estimates; they do not need Stirling's
formula or an asymptotic Gamma-ratio error.
