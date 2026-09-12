# M5 candidate: explicit real nonsingular-product bounds

Status: candidate, awaiting independent review. This is one component of
an effective W threshold, not such a threshold by itself.

Use the notation of M5_MOMENT_RATE.md, and put B=10^50. For real
0<e<=10^-100 and s>=0, the proposed bounds are

    |eta_e-eta| <= B e,
    |log R_e(s)/e-psi(s)| <= B e,
    |psi(s)| <= B,
    |psi(s)-psi(x)| <= B sqrt(|s-x|)  (s,x>=0),
    |log r/e+1/(1-sigma)| <= B e,
    |z0+1/sigma²| <= B e.                         (K)

These give an explicit version of the real part of the product argument.
All powers of ten are deliberately generous; the analytic disks below,
not a numerical fit, supply the constants.

## 1. Analytic physical parameter

The equation for t is

 (t-1)(t-sigma)(t+1+sqrt(2)) = [2cosh(e/2)-2]t.

For complex |e|<=10^-3, Rouche on |t-sigma|=1/100 applies:
the left modulus is >.01*.57*2.82>.016; the right modulus is
<(.425/3)|e|². There is exactly one root in the circle. The same
identity gives |t-sigma|<|e|²/10. Also |q|<1.001 and
|q-1|<=|e|. The root is analytic in e (one zero counted with
multiplicity), real on the real axis, and even.

## 2. Analytic crossing strip

For real y in [.1,.25] and |s-y|<=.001, |v|<.91 and
|Im v|<.001. Write a=1+t²-t(1-t²)v. The preceding bounds imply
Re a>.85, |Im a|<.0011, and

 Re(a²-4t²)>.85²-.0011²-4*.415²>.03.

Thus the principal kernel is analytic on this product of disks,
|U|<=2|t|/Re a<1, and |g|<2. On the smaller disks
|e|<=.0005, |s-y|<=.0005, Cauchy bounds give

 |g_e|<=4000, |g_s|<=4000,
 |g_ss|<=16*10^6, |g_es|<=8*10^6.

At e=0 on the real interval [.1,.25], the identity

 g_s=(1-sigma)*v*sigma*(1-sigma²)*U/sqrt(a²-4sigma²)

shows g_s>1/25: use 1-sigma>.58, v>.77, sigma>.4,
1-sigma²>.82, U>1/3, sqrt(a²-4sigma²)<1.2.
The bound U>1/3 follows from U=2sigma/(a+sqrt(a²-4sigma²)),
a<1.172, sqrt(a²-4sigma²)<1.2 and 2sigma>.8.

Let r_s=10^-10 and r_e=10^-20. On |s-s*|=r_s,
Taylor's theorem gives |g_0(s)|>=sigma*r_s-8*10^6*r_s²
>.4*r_s. For |e|<=r_e, |g_e(s)-g_0(s)|<=4000*r_e.
Moreover |delta|<=|e|: |t|²<.173, |q-t|>.58 and
|1-exp(-e)|<=1.001|e|. Rouche supplies analytic roots s_g,s_h
in |s-s*|<r_s throughout |e|<=r_e.

For real y in [.1,.25], |s-y|<10^-10, the segments from s
to either root remain within 2*10^-10 of the real interval.
The derivative estimates give Re g_s>1/25-.004>1/100,
and |g_s|<4000. Consequently both divided differences

 F_e(s)=integral_0^1 g_s(s_g+u(s-s_g)) du,
 G_e(s)=integral_0^1 g_s(s_h+u(s-s_h)) du

have real part >1/100 and modulus <4000. Their logarithms
with argument in (-pi/2,pi/2) are analytic, each of modulus <10.
Therefore L(e,s)=log F_e(s)-log G_e(s) has modulus <20.
At e=0 it vanishes. Cauchy's Taylor bound, for |e|<=r_e/2,
gives

 |L(e,s)/e-L_e(0,s)| <= 40 e/r_e².

The exact derivative is L_e(0,s)=psi(s). It is bounded by
20/r_e, and its s derivative on the real interval is bounded by
40/(r_e*10^-10). These quantities are all smaller than 10^42.
The root disks similarly give

 |(s_g-s_h)/e-eta| <= 4*r_s*e/r_e² < 10^31 e.

Here the first derivative eta=kappa/g_0'(s*)=1/sqrt(2)
follows by differentiating g_e(s_h)+delta=0 and g_e(s_g)=0.

## 3. The rest of the half line

On the real axis, t is in [.4,sigma], U is in [t,q], and
0<e<=10^-100. Uniformly in s>=0 the discriminants at t and
sigma differ by at most 100|t-sigma|. For nonnegative A,B,
|sqrt A-sqrt B|<=sqrt(|A-B|). Denominators a+sqrt Delta
are >=2t>=.8. Applying this to U=2t/(a+sqrt Delta) gives

 |U(t,exp(-s))-U(sigma,exp(-s))| <=100 e,
 |g_e(s)-g_0(s)|<=200 e.

The same calculation in v, with |exp(-s)-exp(-x)|<=|s-x|,
gives the global Holder bound |g_0(s)-g_0(x)|<=100 sqrt(|s-x|).
For |s-x|>=1 use boundedness instead.

Outside [.1,.25], monotonicity and the derivative lower bound in
Section 2 imply |g_0(s)|>10^-3, since s* in [.153,.167].
The root bounds give |s-s_g|>.05 for s<=.1 and >.08 for s>=.25.
In particular both denominators in

 log R_e(s)=log(1+(s_g-s_h)/(s-s_g))-log(1+delta/g_e(s))

are separated by 10^-4. The roots obey |s_g-s*|<=4000 e/.01
on the real axis by the mean value theorem. Rational differentiation
of delta=t²(1-exp(-e))/(q-t), using |t-sigma|<=e²/10,
gives |delta/e-kappa|<=100 e.
Inserting these inequalities, |eta_e-eta|<=10^31 e, and
|log(1+x)-x|<=x² for |x|<=1/2, gives

 |log R_e(s)/e-psi(s)| <=10^40 e

throughout the two remaining intervals. The same denominator bounds
and the Holder bound for g_0 give a Holder constant <10^10
for psi within either interval. Section 2 gives constant <10^32
in the middle. Splitting an interval at .1 and .25 increases the
Holder constant by at most sqrt(3), so B bounds the global constant.
The modulus bound follows by the same two formulas.

Finally r=q(q-t)/(1-tq)=1-(1-q²)/(1-tq). The denominator is
>.58 and its difference from 1-sigma is <=2e. Expanding log(1-x)
with the preceding elementary remainder gives the stated bound for r.
Also z0=1/[t-(1-tq)q], whose denominator differs from -sigma²
by at most 4e and has modulus >.17, giving the bound for z0.
This proves (K), subject to independent checking of the explicit estimates.
