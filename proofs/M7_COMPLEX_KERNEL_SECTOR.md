# M7: an explicit compact-ray square-root sector

Status: candidate for independent review. This auxiliary lemma assumes
the phase inverse has supplied a positive real reference e0<=10^-8 with
|e-e0|<=e0². It does not prove that inverse statement itself.

The inherited analytic t branch on |z|<=R=5*10^-4 obeys
|t(z)-sigma|<=|z|²/10, is even, and has coefficient -1/16 at z².
For |z|<=R/2, Cauchy's estimate for the even analytic quotient
(t(z)-sigma)/z² yields

 |t(z)-sigma+z²/16|<=10^6 |z|^4.                      (1)

Indeed the omitted even coefficients are bounded by .1/R^(2k), so
their sum is at most .1|z|^4/[R²(1-|z/R|²)]<10^6|z|^4.
For z on the segment between e0 and e, a Cauchy circle of radius |z|
applied to the remainder in (1) gives

 |t'(z)|<=|z|/8+16*10^6|z|³<e0,

because |z|<=2e0 and e0<=10^-8. These circles lie inside |z|<=R/2.
Consequently, with t0=t(e0),

 |t(e)-t0|<=e0³,  t0<=sigma-e0²/17,
 |t(e)|<sigma-e0²/20<sigma.                           (2)

Here (1) implies1/16-10^6e0²>1/17, and1/17-e0>1/20.
Also t0>.4 from the inherited real branch bounds.

Put epsilon=Re(e), s=ne=x+iy with n>=0 and0<=x<=4. Then
epsilon>=e0/2 and |Im(e)|<=e0², whence |y|<=2e0*x.
Set v=exp(-s), v0=exp(-x). The elementary exponential/trigonometric
identities give

 |v-v0|<=|y|<=2e0*x,
 |Re(v-v0)|<=y²/2<=2e0²*x².                           (3)

## Positive real part of the discriminant

Write a(t,v)=1+t²-tv+t³v and Delta=a²-4t². The sum of absolute
coefficients of Delta is at most20 and its total degree is at most8.
On |t|,|v|<=1 its first coordinate derivatives are bounded by160,
and all second coordinate derivatives by1280. Straight segments between
(t0,v0) and (t(e),v) remain in this polydisk by (2) and |v|=v0<=1.
As the polynomial coefficients and (t0,v0) are real, Taylor's formula
and (2)--(3) give

 |Re(Delta(t(e),v))-Delta(t0,v0)|
 <=160(e0³+2e0²*x²)+640(e0³+2e0*x)²
 <=24000e0*(e0²+x).                                  (4)

For the last inequality use (u+v)²<=2u²+2v², x<=4 and e0<=1.
The right side before the last bound is at most
160e0³+1280e0^6+5440e0²*x², which fits the displayed allowance.

On the real reference ray,
Delta(t0,1)=t0²*(exp(e0/2)-exp(-e0/2))²>=.16e0².
Furthermore a>=2t0>.8 and
a_x=t0*(1-t0²)*exp(-x)>.4*.8/100=.0032 on0<=x<=4;
exp(4)<100 follows already from exp(1)<3. Thus

 Delta_x(t0,exp(-x))=2a*a_x>.005,
 Delta(t0,v0)>=.005*(e0²+x).

Since24000e0<=.00024, (4) proves

             Re Delta(t(e),v)>.004*(e0²+x)>0.          (5)

The principal square root therefore stays in the right half-plane and
agrees with continuation from the positive real physical root. No
unquantified branch-continuity assertion is needed on this compact ray.

## Comparison with the critical real kernel

Let a*=a(sigma,v0), Delta*=Delta(sigma,v0)>=0. The polynomial degree
bounds for a (coefficient sum4, total degree4) give
|a(t(e),v)-a*|<=16(|t(e)-sigma|+|v-v0|)<130e0.
The corresponding Delta bound is <1300e0. Here
|t(e)-sigma|<e0²/5 follows from (1)--(2), and x<=4 in (3).

For a principal square root w of any z off the negative real cut and
real d>=0, Re(w)>=0 implies |w+sqrt(d)|>=|w-sqrt(d)|. Factoring
z-d then shows

                  |sqrt(z)-sqrt(d)|<=sqrt(|z-d|).

Using (5), the square-root difference here is therefore <40sqrt(e0).
As a*>=2sigma>.828 and130e0<.001, both kernel denominators
a+sqrt(Delta) and a*+sqrt(Delta*) have modulus greater than .8.
Subtracting the quotients U=2t/(a+sqrt(Delta)) gives the generous bound

 |U(t(e),exp(-ne))-U(sigma,exp(-Re(ne)))|<500sqrt(e0).  (6)

This includes n=0, where the critical square root vanishes.

Finally the formal identity
Y=v*t*(t+Y)/(1-t*Y/(1-t²)), Y=U-t,
has nonnegative coefficients in t,v by formal iteration. For real
0<t<sigma and0<=v<=1, iteration from0 is increasing and bounded by
the physical solution Y=U-t<1-t. The denominator remains positive
because t*Y/(1-t²)<t/(1+t)<1. Thus the nonnegative series converges
there and equals the branch analytic at v=0. Equation (2) therefore
also implies the useful global bound

               |U(t(e),v)|<=U(|t(e)|,|v|)<1,
                         |v|<=1.                    (7)

This last positivity argument bounds weights and the far v-disk; the
compact comparison (6) separately controls the change from the critical
profile. Neither assertion by itself bounds the entire smooth product.
