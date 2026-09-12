# M6 candidate: global real moment error with polynomial constants

Status: candidate for independent review. A new threshold additionally needs
an accepted product lemma supplying B and its domain. M5 is unchanged.

Put e=e_N(theta), x_n=ne, theta in [.8,.9], lambda=1/(1-sigma),
and s*=-log(1/2+sqrt(2)/4). Suppose e<=10^-8 and the real product
lemma supplies B>=1 with

 0<R_e(s)<=1, -B<=psi(s)<=0,
 |log R_e(s)/e-psi(s)|<=B e,
 |psi(s)-psi(x)|<=B sqrt(|s-x|),
 r<=exp(-e), |(-log r)/e-lambda|<=B e,
 |z0+1/sigma²|<=B e, |z0|<=10,
 eta_e in [.70,.72], |eta_e-eta|<=B e.                  (P)

These hypotheses hold with B=10^50 and e<=10^-100 if the new sign
lemma is combined with the accepted M5 kernel lemma. Smaller constants
are a separate improvement; no such value is assumed without proof.

The accepted real phase certificate gives, on e<=.01,
.3<s_g'<.4 and s_g in [.15,.17]. Consequently

 |s_g-s*|<.4e,
 s*/e=N+theta-m_e,    .3<m_e<.4.

Thus the critical center is separated from the grid by at least .4e:
theta-m_e lies in [.4,.6]. This elementary spacing is used below.

The proposed real bound is

 |P_N-P0|+|H_N-H0|
 <=10^9 e^(1/4)+10^9 B sqrt(e)+10^14 e.                 (T)

## 1. Absolute comparison of the damped products

Set A_n=sum_(j<n)log R_e(je), A(x)=integral_0^x psi(s) ds.
Both are nonpositive. The rectangle estimate gives

 |A_n-A(x_n)|<=B x_n(e+sqrt(e)).

Let K_n=r^n exp A_n and K(x)=exp(-lambda*x+A(x)). Since
|exp u-exp v|<=|u-v| for u,v<=0, retaining the r damping yields

 |K_n-K(x_n)|<=3B x_n exp(-x_n)sqrt(e),
 |K_n|, |K(x_n)|<=exp(-x_n).                            (1)

Indeed, the r-only difference is bounded by B*x_n*e*exp(-x_n)
using |exp(-u)-exp(-v)|<=|u-v|exp(-min(u,v)). The other term is
exp(-x_n)|A_n-A(x_n)|. No growing cutoff or small relative exponential
error is required.

## 2. Elementary cusp sums

Let d_n=|x_n-s*| and set w(d)=d^(-3/4) for d<=1, w(d)=1 for d>1;
also w_e(d)=(e+d)^(-3/4) for d<=1, w_e(d)=1 for d>1.
Grouping points separately on the two sides of s*, with spacing e and
at most one point per side in each interval [k e,(k+1)e), gives

 e sum_n w_e(d_n) exp(-x_n/2) <=30,
 e sum_(d_n>=10e) w(d_n) exp(-x_n) <=30,
 e sum_(d_n>=10e) w(d_n)/d_n exp(-x_n) <=30 e^(-3/4),
 e sum_(d_n>=10e) w(d_n)(1+|log d_n|)exp(-x_n) <=200.    (2)

For details, within distance1 use the decreasing power and
integrals int_0^1 x^(-3/4) dx=4 and
int_0^1 x^(-3/4)|log x| dx=16. There are two sides. The endpoint
rectangle costs at most2 e^(1/4) for w_e. In the far-from-cell sums,
the omitted initial part begins at10e; comparison with the integral
adds at most2e(9e)^(-3/4), or2e(9e)^(-7/4) for the third sum.
For the logarithmic weight use its decreasing behavior on (0,1)
and the same integral16; the first rectangle is <1 for e<=10^-8.
Outside distance1, sum the geometric exp(-x_n/2) tail; its weighted
mass is <3. For the last sum, log d_n<=x_n+1 on this tail and the
geometric first moment has mass <4. These estimates fit (2).

The same bounds, without the endpoint rectangle and with smaller
constants, hold for the corresponding integrals.

## 3. Gamma comparison, including the closest cells

Let G_theta(x)=(s*/|x-s*|)^eta times the post-crossing multiplier
sin(pi theta)/sin(pi(theta-eta)), equal to1 before the crossing.
The multiplier is positive and at most5. The exact product is
z_n=z0*T_n*K_n; the critical product is Z=-sigma^-2*G_theta*K.

There are at most21 indices with d_n<10e. Their Gamma factors obey

 |T_n|<=2000 e^(-3/4),  |G_theta(x_n)|<=20e^(-3/4).     (3)

For the first, use the pre/post Wendel bounds
|T_n|<=20(a/|n-a|)^eta_e from M5, before its19/25 exponent
enlargement. Here |n-a|>=.1 and a/|n-a|>=2. Since eta_e<=.72<.75,
and (1+|n-a|)/|n-a|<=11, this gives
|T_n|<=200(a/(1+|n-a|))^.75
<=200(e+|x_n-s_g|)^(-3/4), using s_g<1.
This is safely below the first bound in (3), since |x_n-s_g|<11e
and s_g>.15. The second bound uses the critical grid separation .4e.
For all indices, the convenient absolute envelope is

 |T_n|<=2000 w_e(d_n),    |G_theta(x_n)|<=10 w_e(d_n).   (4)

Near the cusp, use the M5 Gamma bound and |s_g-s*|<.4e;
(e+d_n)/(e+|x_n-s_g|)<=1.4. Beyond distance1, Wendel and
the sine multiplier bound imply T_n<20 and G_theta<5, both
covered by (4). This also bounds points away from the fixed crossing
window: apply the same Gamma formulas directly, dropping the
restriction |n-a|<=a/2 and using the smaller exponent for a/|n-a|<1.

For d_n>=10e, Wendel gives logarithmic error3/a+3/|n-a| between
T_n and the exact-center/exponent bare profile. The pointwise relative
error is at most twice this number. Moving the center by <.4e changes
a power by at most a constant times e*w(d_n)*(1+1/d_n).
Moving eta_e to eta is estimated by differentiating the positive real
power, not by exponentiating B e log d_n. For the exponent parameter,
the derivative is the same power times log(s_g/|x-s_g|); the sine
multiplier's logarithmic derivative is at most13. The intermediate
powers, with exponent in [.70,.72], are bounded by10w(d_n), and
|log(s_g/|x-s_g|)|<=3+|log d_n|. Altogether the generous bound

 |T_n-G_theta(x_n)|
 <=1000e*w(d_n)*(1+1/d_n)
       +1000B e*w(d_n)*(1+|log d_n|)                   (5)

holds on these indices. The same side of the crossing is used throughout,
since d_n>=10e and center motion is <.4e.

Multiplying by a weight bounded by40 and exp(-x_n), and using (2),
the far part of e sum |T_n-G|*weight*exp(-x_n) is bounded by

 3*10^6 e^(1/4)+8*10^6 B e.

The near part (3) costs less than2*10^6 e^(1/4). Therefore

 e sum |T_n-G|*weight*exp(-x_n)
 <=5*10^6 e^(1/4)+8*10^6 B e.                         (6)

## 4. Quadrature of the critical weighted profile

The M5 real weight lemma gives |V0|<40 and Holder constant110 in s.
Since |psi|<=B is included in (P), |K'|< (B+2)exp(-s).
Thus H(s)=K(s)V0(s)
has the damped Holder bound

 |H(s)-H(r)|<=300B sqrt(|s-r|)exp(-min(s,r))
                              when |s-r|<=1.           (7)

For a cell outside d_n<10e, use |G|<=10w(d_n), (7), and the
cusp derivative bound |G'|<=20w(d_n)/d_n throughout the cell.
This gives a total quadrature error, after summing (2), of at most

 10^5 B sqrt(e)+3*10^4 e^(1/4).

The omitted cells lie within distance11e; their discrete mass is
bounded using (3), and their integral mass by
400 int_0^(11e) x^(-3/4) dx. Both fit an additional
10^5 e^(1/4). Thus, for each j=1,2,

 |e sum G(x_n)K(x_n)Vj,0(x_n)-int G K Vj,0|
 <=2*10^5 e^(1/4)+10^5 B sqrt(e).                      (8)

Applying the bound to absolute values is legitimate and introduces
no new singularity; it is also consistent with the direct mass bounds.

## 5. Exact weights, prefactors and final ledger

The M5 weight lemma gives |Vj,e-Vj,0|<=1200e along the physical ray.
Its rational checker gives boundary and Q/e errors<=10^6e,
with Q/e<1, t²<1 and |t²-sigma²|<e.

Using (1), (2), and (4), the product-comparison error in the normalized
sum, including |z0|<=10 and |Vj|<=40, is at most

 10*3B sqrt(e)*2000*40*30 = 7.2*10^7 B sqrt(e),

where x exp(-x)<=exp(-x/2). The weight perturbation costs at most
10*2000*30*1200e<10^9e. Changing z0 costs at most
B e*10*40*30<2*10^4B e. Equation (6), with |z0|<=10,
and (8), with sigma^-2<10, then supply all discrete/profile errors.
Their sum for both moments fits

 2*10^8 e^(1/4)+4*10^8 B sqrt(e)+2*10^9e.

For the prefactor errors, the absolute exact normalized moment sum is
bounded by10*2000*30*40=2.4*10^7. Multiplying by10^6e for Q/e,
adding both boundary errors, the corresponding critical bound, and the
extra t² change in H gives a total below10^14e.
Absorbing the smaller preceding e term into the generous remaining
margin yields (T).

Every numerical constant above is an analytic allowance, not fitted from
finite data. The new sign and approximation lemma, this aggregation, and
any proposed reduced threshold must all pass independent review.
