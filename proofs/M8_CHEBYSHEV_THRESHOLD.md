# M8 candidate: effective W uniqueness from polynomial approximation

Status: candidate for independent review. The proposed threshold is
N_unique=10^57, replacing M7's sufficient10^120 for the same real phase
sector. It remains far beyond finite enumeration and does not close the
accessible-to-asymptotic coverage gap.

## 1. A joint analytic derivative estimate

Let f,g be holomorphic on the rectangle Omega from M8_COMPLEX_DOMAIN,
real on T=[.8,.9], with sup_Omega(abs(f)+abs(g))<=M and
sup_T(abs(f)+abs(g))<=E. Write theta=17/20+x/20. On the x plane choose
the Bernstein ellipse with rho=22/15 and q=1/rho=15/22. Its theta
semiaxes are (rho+rho^-1)/40 and (rho-rho^-1)/40. The latter is less
than.02; the former is less than.07. Its closed interior therefore lies
strictly inside Omega.

For the vector h=(f,g), let a_k be its vector Chebyshev coefficients,
using h(x)=a_0+sum_(k>=1)a_k T_k(x). Cauchy's integral applied to
h((w+w^-1)/2) on abs(w)=rho gives

                     norm_1(a_k)<=2M q^k, k>=1.         (1)

The same contour is used for both components before summing absolute
values, so no extra factor2 is required for a joint norm. The coefficient
bound is the usual analytic Chebyshev estimate; see Trefethen, Section3
of [Multivariate polynomial approximation in the hypercube](https://people.maths.ox.ac.uk/trefethen/hypercube_published.pdf).

For the degree-m truncation p_m and k=m+1, define the exact tail bounds

    A_m=2M q^k/(1-q),
    B_m=40M q^k*[k²/(1-q)+2kq/(1-q)²+q(1+q)/(1-q)³].

Then sup_T norm_1(h-p_m)<=A_m and
sup_T norm_1((h-p_m)')<=B_m, since abs(T_j')<=j² on[-1,1]
and differentiation in theta contributes20. Absolute uniform derivative
convergence follows from sum j² q^j<infinity and justifies the operation.

Markov's polynomial inequality gives

              sup_T norm_1(p_m')<=20m² sup_T norm_1(p_m).

For clarity about the vector norm, at any point choose the two real
signs attaining the norm of p_m' there, apply scalar Markov to their
linear combination, and bound its supremum by sup norm_1(p_m). The
polynomial is real because f,g are real on T. This uses the classical
inequality stated in Aptekarev et al., Section1 of
[arXiv:1405.0167](https://arxiv.org/abs/1405.0167).

Consequently the effective interpolation inequality is

        sup_T(abs(f')+abs(g'))<=20m²(E+A_m)+B_m.         (2)

This uses no differentiated real remainder and no sampled derivative.

## 2. Application to the moment errors

Set f=P_N-P0, g=H_N-H0. M8_COMPLEX_DOMAIN gives the joint complex norm
below10^8, and M7_REAL_TO_DERIVATIVE gives the critical norm below100.
Thus M=10^8+100 is valid whenever N>=10^30.

At N>=10^57, the accepted M6 real moment estimate and e_N<1/N give

    E_N<10^9 N^-1/4+10^21 N^-1/2+10^14/N
       <=1000^(1/4)*10^-6+sqrt(10)*10^-8+10^-43
       <5.656*10^-6=:E.

The last inequality follows from5.624^4>1000 and3.163²>10; every term
decreases with N. The inherited e<=10^-10 domain is satisfied.

Take m=92. Exact rational evaluation of(2), with this M,E,q, gives

          sup_T(abs(P_N'-P0')+abs(H_N'-H0'))<1.033.    (3)

This is intentionally a larger derivative allowance than M7's .009;
it is sufficient for the denominator's strict monotonicity.

## 3. Transfer to the W pole

The exact derivative identity and error bound in M7_UNIQUENESS_TRANSFER
equations(4)--(5) apply to any derivative-error bound E1. They do not
require E1<=1 until that note's final numerical substitution. Use(3)
instead. M6 supplies N>=10^46 endpoint signs, noncancellation,
delta_N<1/250 and e_N<1/N. The frozen critical certificate gives
F0'<-6. Hence for every N>=10^57,

    F_N'<-6+4*(1.033)+150/250+18*10^-114+480000*10^-57
         <-1.

Existence follows from M6's endpoint signs. Strict decrease proves
uniqueness, the derivative is nonzero, and the nondegenerate phase-to-t
map makes the pole simple in t. The numerator stays nonzero by M6.

Therefore every integer N>=10^57 has exactly one simple noncancelled
real W pole in its phase band theta in[.8,.9]. The exact arithmetic
certificate is m8_chebyshev_threshold.py; the analytic inputs and this
transfer require independent review before acceptance.
