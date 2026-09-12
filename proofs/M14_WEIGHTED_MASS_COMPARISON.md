# M14 candidate: a practical integrated Gamma/product error

Status: full analytic candidate awaiting independent review of this proof
and the new Gamma and smooth-envelope inputs. Arithmetic alone does not
establish the theorem. This note covers N>=512 only;32..511 remains a
separate finite obligation.

Let theta be either4/5 or9/10, N>=512 an integer, e=e_N(theta),
E=17/51200, c=s_g(0), eta=1/sqrt(2), beta=beta(e), alpha=1-beta,
and s_g=c+d_c. Let delta be any fixed number in[0,1/20]. The accepted
and new scalar inputs give

    0<e<E, .15<c<.17, 0<d_c<.4e,
    .7<eta<beta<.72, 0<beta-eta<.14e^2.              (1)

Define the critical positive weight and its decreasing density by

    w(x)=J0 K0(x)L0(u0(x);delta), nu(x)=-w'(x),
    J0=2sigma, sigma=sqrt(2)-1.

We prove

    |J0 e sum T_n K_n L0(u0(ne);delta)-S0(delta)|
       <56/625<1/8,                                 (2)

where S0 is the critical integral in M14_COMBINED_WEIGHT_TRANSFER.

## 1. Critical weight bounds without an endpoint derivative assumption

The M14 critical-factor identity gives TV(psi)<17/8 and
-25/8<psi<-1. Since lambda=1/(1-sigma)=1+eta,

    K0(x)<=exp(-(2+eta)x)<exp(-2.7x).

The combined weight is decreasing in x and decreasing in delta, and
the exact endpoint check gives J0 L0(1;0)<5. Thus

    0<w(x)<5 exp(-2.7x), integral_0^infinity nu(x)dx=w(0)<5. (3)

For the critical combined weight, the rational formula is

    partial_u log L0 = sigma/(1-sigma*u)
       -sigma*eta/(1-sigma*eta*u) +4sigma^2 R_u/G,
    G=4sigma^2 R-(1-sigma+2delta).

It increases with delta because R_u>0 and only G depends on delta.
Evaluate delta=1/20. Eight exact adjacent dyadic interval computations
over rational u cells covering[2/5,1] prove

    0<partial_u log L0<4.                            (4)

All denominators and gaps are checked positive. This is a continuous
interval cover of u, not a phase-point scan. It includes the physical
u range[sigma,1].

For x>=3/40, exp(-x)<=40/43 and the exact kernel evaluation gives
u0(x)<4/5. The critical discriminant satisfies Delta>=3(1-exp(-x)),
and1-sigma^2<5/6. Consequently

    |u0'(x)| <= (4/5)(5/6)/sqrt(3*(1-40/43))<3/2.

Equations(3),(4), lambda+25/8<5 imply

    0<nu(x)<11w(x),  |(log w)'(x)|<11, x>=3/40.     (5)

At x=0 the derivative may be unbounded. We use only(3) and absolute
continuity there; the explicit square-root kernel has an integrable
derivative. All subsequent uses of(5) stay strictly beyond3/40.

## 2. The normalized Gamma density and its exponent perturbation

For gamma in[eta,beta], set

    C_gamma=sin(pi*theta)/sin(pi*(theta-gamma)),
    G_gamma(x)=c^gamma * |x-c|^(-gamma)
                   *[1 if x<c, C_gamma if x>c],
    M_gamma=integral_0^infinity G_gamma(x)w(x)dx.

The removable single point x=c is irrelevant to these integrals.
M_eta=S0(delta)<3 by the reviewed critical integral certificate.
The M13 sine bounds give0<C_gamma<12/5 and the Gamma-envelope lemma
gives |partial_gamma log C_gamma|<20. Also |log c|<2.
For r=|x-c|<=1, (3) bounds the exponent derivative integrand by

    |partial_gamma G_gamma(x)| w(x)
       <12 r^(-18/25)(22+|log r|).

Integrating over both sides of c costs at most
24*[22/(7/25)+1/(7/25)^2]. On r>1, x>c+1 and the bound
12*(22+x)*exp(-x) costs at most276. Their sum is below2500.
Differentiation under the integral is justified by these integrable
uniform bounds. Therefore

    |M_beta-M_eta|<2500*(beta-eta)<350e^2,
    0<M_beta<31/10.                                 (6)

## 3. Moving the centre and amplitude

Use the exact Gamma amplitude

    A_e=e^beta*Gamma(a+1)/Gamma(b+1),
    Gbar(x)=A_e*|x-s_g|^(-beta)
                    *[1 if x<s_g, C_beta if x>s_g].

The shifted Wendel inequality gives
s_g^beta<=A_e<=(s_g+alpha*e)^beta. Since beta<.72 and c>.15,
concavity yields

    1<=r_A:=A_e/c^beta<=1+(84/25)e.                  (7)

The density Gbar is defined also for negative x by its pre branch.
Write Mbar=integral_0^infinity Gbar(x)w(x)dx. Translating y=x-d_c,

    Mbar=r_A*[integral_-d_c^0 G_beta(y)w(y+d_c)dy
                    +integral_0^infinity G_beta(y)w(y+d_c)dy].

For negative y, G_beta(y)<1, so the new negative-origin piece is at
most5d_c<2e. The remaining weight decreases under this translation.
Thus Mbar<=(1+(84/25)e)*(M_beta+2e)<16/5, and

    Mbar-M_beta <[(84/25)*(31/10)+2*(1+(84/25)E)]e<19e. (8)

For the opposite direction, drop the positive new piece and r_A>=1.
The possible loss is at most

    integral_0^infinity G_beta(y)*integral_y^(y+d_c) nu(x)dx dy.

Split the x integration at2/25=.08. Below that point, y lies in[0,.08]
and G_beta(y)<5/2 because c/(c-.08)<=15/7<5/2. This costs at most
(5/2)*d_c*integral nu<5e. Above that point, y>=.08-d_c>3/40;
(5) and decreasing w give nu(x)<11w(x)<=11w(y). The cost is then
at most11d_c*M_beta<11*.4e*(31/10). Hence

    |Mbar-M_beta|<19e.                              (9)

## 4. Exact cumulative-mass quadrature error

Let Qbar' =Gbar with Qbar(s_g)=0. The Gamma-envelope lemma supplies

    Qbar(ne)<=eQ_n<=Qbar(ne+beta*e),
    Q_n=(n-a)T_n/alpha.

It also handles n=-1 and proves, with C_e=s_g/alpha+e,

    0<h0:=C_e+Qbar(0)<1.001e.                       (10)

For x>=0 and n=floor(x/e), the exact primitive gives

    A_disc(x)=e sum_(k=0)^n T_k=eQ_n+C_e,
    A_bar(x)=integral_0^x Gbar(s)ds=Qbar(x)-Qbar(0).

Monotonicity of Qbar and the floor shift imply

    |A_disc(x)-A_bar(x)|
       <=h0+integral_(x-e)^(x+beta*e) Gbar(s)ds.      (11)

Tonelli, including the atom at n=0, expresses the discrete mass and
Mbar as the integrals of these cumulative masses against nu.
The h0 term costs less than(1001/200)e.

For0<=x<=2/25, the inner integration remains below s_g; (7) and
the phase bounds give

    Gbar(s)<[(.15+.3E)/(.15-.08-.72E)]^beta<5/2.

Thus this part costs at most(43/25)*(5/2)*5e. For x>=2/25, every
s in that integration interval satisfies s>=.08-e>3/40. Equation(5)
along the segment between s and x gives

    nu(x)<11w(x)<=11exp(11e)w(s)<11*(101/100)w(s).

Swapping the integrations, the x length at fixed s is at most
(1+beta)e<(43/25)e. The far cost is therefore at most
(43/25)*11*(101/100)*(16/5)e. All integrations are finite by positivity,
the exponential weight bound and integrability of the Gamma cusp.
Together with(6),(9), the exact rational ledger proves

    |M_disc-M_eta|<107e+350e^2<1/25,
    M_disc:=e sum_(n>=0) T_n w(ne).                 (12)

In particular M_disc<3+1/25. No cusp cell was discarded; (11) includes
every floor and the n=0 contribution.

## 5. Replace the critical product by the exact product

The new M14 smooth-envelope input states, for all integer n>=0,

    |log K_n-log K0(ne)|<e*(17/8+20ne).              (13)

On ne<=2, exp(z)-1<=z/(1-z) at z=E*(17/8+40) gives
|K_n/K0(ne)-1|<3/200. The product-replacement error on this head is
therefore below(3/200)*(3+1/25), using(12).

For the infinite tail ne>2, (13) and the critical exponential bound give

    K_n<(1001/1000)exp(-(27/10)ne),

because2+eta-20E>27/10 and exp((17/8)E)<1001/1000.
The same bound holds for K0. The direct post-crossing Wendel estimate
gives T_n<1/2 on ne>2: the ratio of its Gamma arguments satisfies

    (b+1)/(n-a)<(.17+.3E)/(2-.17)<1/10,
    beta/(n-a)<.72E/(2-.17)<1/1000.

Combine the sine multiplier<12/5, correction<1001/1000 and
(1/10)^(7/10)<1/5. This uses n>N+1, which follows from ne>2 and
eN<.17. No large-a assumption is imported.

Also u0(ne)<1/2 since exp(2)>7 and U(sigma,1/7)<1/2.
The exact critical endpoint weight satisfies L0(1/2;0)<9/4, so
L0(u0(ne);delta)<9/4. Each of the two discrete tails, with K_n or K0,
is bounded by

    (5/6)*(1/2)*(9/4)*(1001/1000)
          *[e/(1-exp(-(27/10)e))]*exp(-27/5)<1/500.  (14)

Here the geometric normalization is below3/8, by
1-exp(-z)>=z-z^2/2. A positive degree12 Taylor sum proves exp(27/5)>200
and the stated final allowance. Both tails include all integers ne>2;
the first such index has ne>2, regardless of floors.

Combining(12)--(14),

    |Stilde_e-S0(delta)|
      <1/25+(3/200)*(3+1/25)+2/500
      =56/625<1/8.                                  (15)

This proves(2), subject to the named analytic inputs and independent
review. M14_COMBINED_WEIGHT_TRANSFER then supplies opposite signs of
F at the two endpoints for every N>=512, using the actual directed
delta<1/20. Continuity, M13 uniqueness and M12 noncancellation give one
simple W pole in every such band. The finite indices32..511 remain
outside this argument and must still be certified before full coverage.

## Reproduction and evidence scope

Run `python -m proofs.m14_weighted_mass_bounds`. It checks the eight
continuous u cells and all rational implications with384-bit outward
intervals and Fractions. These checks are not a substitute for the
Gamma identities, Tonelli arguments, convergence and inequalities
proved above. No finite phase scan or measured error enters this proof.
