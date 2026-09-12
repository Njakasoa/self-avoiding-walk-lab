# M9 candidate: a linear real moment error via the discrete primitive

Status: candidate for independent analytic review. This proof uses the new
M9_PRODUCT_VARIATION input and the accepted M8_DISCRETE_PRIMITIVE identity.
It preserves all frozen M3--M8 sources. No finite-to-asymptotic coverage
claim follows from this error estimate alone.

On theta in[.8,.9], with e=e_N(theta)<=10^-10, the proposed bound is

    |P_N-P0|+|H_N-H0| < 10^21 e.                         (1)

All constants below are uniform in theta. Write sigma=sqrt(2)-1,
eta=1/sqrt(2), c=s*, beta=eta_e, a=s_g/e, b=a-beta, x_n=ne,
G=G_theta and T_n as in M6_REAL_MOMENT_RATE. Set

    B=10^12, K_eta=3*10^5, I=[.1,.25], H=[.11,.24].

The common domain includes the M5 real weight lemma. M6 supplies
|s_g-c|<.4e, |beta-eta|<K_eta e, beta in[.70,.72],
.15<c<.17, |z0+sigma^-2|<20e and |z0|<10.

## 1. Decreasing critical weights and their local density

For j=1,2 let w(x)=K(x)Vj,0(x). The critical physical kernel u0(x)
is decreasing. In M5_EFFECTIVE_WEIGHTS, f(u)=u/(1-sigma*u) has
positive derivatives, as does f(u)^2; hence the divided difference A_j
and Vj,0 are increasing in u. Thus Vj,0(x)>0 is decreasing in x.
Also K'=(-lambda+psi)K<0, since psi<=0 and lambda=1/(1-sigma)<2.
It follows that w is positive, decreasing and absolutely continuous,

    0<w(x)<40 exp(-x),  nu(x):=-w'(x)>=0,
    integral nu <=40,
    integral (1+x)^2 nu(x) dx <=200.                   (2)

The last inequality is integration by parts, bounded by
40+80 integral (1+x)exp(-x)dx=200. Absolute continuity at zero follows
from the integrable square-root derivative of the explicit kernel;
psi is continuous there. There is no singular derivative assumption at zero.

We also need a density bound only on I. Put gamma=g0'(c)=sigma>.4.
For x in I, Taylor's integral identities give

    g0(x)=(x-c)F(x), F(x)=integral_0^1 g0'(c+u(x-c))du>.04,
    F(x)-gamma=(x-c)J(x),
    J(x)=integral_0^1 (1-u)g0''(c+u(x-c))du, |J|<50.

The M6 bounds g0'>.04 and |g0''|<100 apply on the entire segment.
Since eta=kappa/gamma and kappa=sigma^2/(1-sigma)<.3,

    psi(x)=kappa J(x)/(gamma F(x)), |psi(x)|<1000.       (3)

This includes the removable value at c. Outside I, the original two-term
formula and |g0|>.001, |x-c|>.05 also give |psi|<315, so (3) holds globally.
On I, M6 gives |u0'|<.315/.17<2, and M5 gives |Vj,0,u|<36.
Consequently

    nu(x)<40*(1000+2)+100<41000 on I.                 (4)

## 2. Exact cumulative mass and its boundary constant

For x>=0, n=floor(x/e), define

    A_e(x)=e sum_(k=0)^n T_k,
    A(x)=integral_0^x G(s)ds.

The exact M8 primitive yields

    A_e(x)=Qe_n+C_e,
    Qe_n=(x_n-s_g)T_n/(1-beta), C_e=s_g/(1-beta)+e.

The continuous primitive is

    Q(x)=(x-c)G(x)/(1-eta),
    A(x)=Q(x)+C_0, C_0=c/(1-eta).

It is continuous at c, with Q(c)=0 and Q'=G away from c; G is integrable.
Since 1-beta>=.28 and 1-eta>.29,

    |C_e-C_0| <=.4e/.28 + .17*K_eta*e/(.28*.29)+e
               <4*K_eta*e.                            (5)

Tonelli's theorem, using positive T_n and nu, gives

    e sum T_n w(x_n)=integral A_e(x)nu(x)dx.

The same formula with A follows for integral G w. Exponential damping
and the M6 polynomial envelope make all quantities finite. Therefore

    |e sum T_n w(x_n)-integral G w|
       <=integral |A_e(x)-A(x)|nu(x)dx.                (6)

This identity is why the mass of the closest cells need not be discarded.

## 3. Bounds for the primitive, including the closest cells

Put d_n=|x_n-c| and h(d)=d^(-3/4) for d<=1, h(d)=1 otherwise.
For d_n>=10e, equation(5) of M6_REAL_MOMENT_RATE and its derivation give

    |T_n-G(x_n)| <=1000e h(d_n)(1+1/d_n)
           +1000 K_eta e h(d_n)(1+|log d_n|).          (7)

Only the exponent-motion bound enters the second term in that derivation;
thus K_eta replaces B there. No smooth-product bound has been reduced.
The gamma-ratio and center-motion terms are still the first term of (7).
The accepted envelope gives G(x_n)<=10h(d_n). Subtract Qe_n and Q(x_n):
the coefficient of |T_n-G| is at most(d_n+.4e)/.28<4d_n,
and the remaining coefficient is at most .4e/.28+d_n*K_eta*e/(.28*.29).
As K_eta>=1, these imply the convenient bound

    |Qe_n-Q(x_n)|
      <10^4 K_eta e h(d_n)[1+d_n(1+|log d_n|)].        (8)

There are at most21 indices with d_n<10e. The accepted M6 closest-cell
envelopes T_n<=2000e^(-3/4), G(x_n)<=20e^(-3/4) give

    |Qe_n| < (10.4/.28)*2000 e^(1/4)<75000e^(1/4),
    |Q(x_n)| < (10/.29)*20 e^(1/4)<700e^(1/4).

Thus their primitive difference is below76000e^(1/4). These cells have
total length at most21e, not an interval of fixed positive length.

## 4. Integrating the primitive error

On x in H, both x and its left grid point lie in I. For far indices
d_n>=10e, d_n<1 and d_n(1+|log d_n|)<=1. The accepted cusp sum from M6
gives e sum_(x_n in I,d_n>=10e) h(d_n)<40: insert exp(-x_n), use its
bound30, and then exp(.25)<4/3. Equations(4) and(8) therefore bound the
far-index contribution on H by

    41000 * 2*10^4 * 40 * K_eta e < 4*10^10 K_eta e.

The near-index contribution is at most

    41000 * 76000 * 21 e^(5/4) < 7*10^10 e^(5/4).

To replace Q(x_n) by Q(x), use |Q(x)-Q(x_n)|<=integral_cell G.
Integrating over H and summing the cells costs at most
41000 e integral_I G <41000*80e<4*10^6e. The integral bound80 follows
from G<=10|x-c|^(-3/4) on I and the two elementary power integrals.

Outside H, d_n>.039, so only far indices occur. If d_n<=1,
h(d_n)<12 and 1+d_n(1+|log d_n|)<=2. If d_n>1, log d_n<=d_n and
d_n<=1+x give the bound3(1+x)^2 for the bracket in(8).
These bounds fit36(1+x)^2 in both cases. Every intervening point of
the grid cell is also at distance>.039 from c, so G<200 there. Hence

    |Qe_n-Q(x)| <4*10^5 K_eta e(1+x)^2 outside H.

Its integral against nu is at most8*10^7 K_eta e by(2).
Finally (5) costs at most160 K_eta e. Adding all terms, using e^(1/4)<=1
and K_eta=300000, proves, for each j,

    |e sum T_n K(x_n)Vj,0(x_n)-integral G K Vj,0|
                      <6*10^10 K_eta e.              (9)

Every region is included, including the infinite tail via(2).

## 5. Exact-product, weight and prefactor ledger

M9_PRODUCT_VARIATION gives

    |K_n-K(x_n)|<=3B e(1+x_n)exp(-x_n).

Using (1+x)exp(-x)<=2exp(-x/2), the M6 mass envelope
T_n<=2000(e+|x_n-c|)^(-3/4) near the cusp (and2000 otherwise), and
e sum envelope_without_2000 exp(-x_n/2)<=30, its contribution including
|z0|<10 and |Vj|<40 is at most

    10*2000*40*6*30 B e =1.44*10^8 B e per moment.

The exact weight perturbation |Vj,e-Vj,0|<=1200e costs at most
10*2000*30*1200e=7.2*10^8e per moment. After replacement by the critical
product, changing z0 costs at most20e*2000*40*30=4.8*10^7e per moment.
Equation(9), multiplied by sigma^-2<10, costs at most6*10^11 K_eta e
per moment. These replacements can be made in that order, so no uncontrolled
cross-term is omitted.

The boundary and Q/e estimates and the extra t^2 factor for H are exactly
those in section5 of M6_REAL_MOMENT_RATE. Their combined allowance is
10^14e, obtained from the unchanged normalized mass bound2.4*10^7.
Thus the full error is below

    [2*(1.44*10^8 B +7.2*10^8+4.8*10^7+6*10^11 K_eta)
         +10^14]e <10^21e,

with B=10^12 and K_eta=300000. This proves the proposed bound(1),
conditional on independent review of this argument and the new product
variation lemma. It does not by itself establish a useful low-index
uniqueness threshold or bridge the remaining integer-index gap.
