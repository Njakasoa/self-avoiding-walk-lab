# M14: a sharp real smooth-product envelope

Status: new analytic component for independent review. On the practical
domain

    0 < e <= E := 17/51200 = 0.17/512,
    n >= 0 integer,    x := n e,

this note gives a computable two-sided enclosure for the smooth product

    K_(e,n) = r^n Pi_(e,n),
    Pi_(e,n) = product_(j=0)^(n-1) R_e(j e).

The comparison profile is

    K_0(x) = exp(-lambda x + integral_0^x psi(s) ds),
    lambda = 1/(1-sigma),    sigma = sqrt(2)-1.

The result is

    |log K_(e,n) - log K_0(n e)|
        < e (17/8 + 20 n e),                                      (M14.0)

or, equivalently,

    K_0(n e) exp(-e(17/8+20 n e))
      < K_(e,n)
      < K_0(n e) exp( e(17/8+20 n e)).

The endpoint n=0 is included: both products and both integrals are empty,
and K_(e,0)=K_0(0)=1. The proof is a real fixed-s estimate followed by a
bounded-variation rectangle estimate. It uses the M11 inverse-kernel
factorization and the M14 critical-variation lemma. It does not scan
indices, evaluate a phase endpoint, or assert a sign for a full denominator
or a W residue.

## 1. Definitions and the nonsingular factorization

Use the M11 notation

    q = exp(-e/2),       C = q-t,       D = 1-t q,
    u_g = t/D,           h = t q/C,
    delta = t^2 (1-q^2)/C,
    u(s) = U(t, exp(-s)).

The physical root t is the even solution of the M5 implicit equation and
satisfies t<sigma. The two anchors are defined by

    g_e(s_g) = 0,       g_e(s_h) + delta = 0,
    beta = (s_g-s_h)/e.

The inverse kernel has the exact form

    v_t(u) = (u-t)(1-t u) / (t(1-t^2)u),

and

    v_t(a)-v_t(u)
      = (a-u)(1-a u) / ((1-t^2) a u).                         (M14.1)

Writing g_e(s)=t-D U(t,exp(-s)), equation (M14.1) gives

    g_e(s)       = D (u_g-u(s)),
    g_e(s)+delta = D (h-u(s)).

For the positive exponential secant, define

    M(s,a) = integral_0^1 exp(-((1-v)s+v a)) dv.

This definition is continuous at s=a and is strictly positive. Since

    exp(-a)-exp(-s) = (s-a) M(s,a),

the M11 factorization is

    R_e(s)
      = (u_g/h) (1-u(s)h)/(1-u(s)u_g)
        M(s,s_g)/M(s,s_h).                                  (M14.2)

All divided differences in this equation are understood by their positive
integral limits at s=s_g and s=s_h. M6 concavity gives

    0 < R_e(s) <= 1,       ell_e(s) := log R_e(s) <= 0.       (M14.3)

This sign and the factorization are used on the whole real ray s>=0.

The two rational factors involving the anchors must be combined before
taking a logarithm. With d=h-u_g and p_e=u_g(1-u h),

    (h/u_g) (1-u u_g)/(1-u h)
       = 1 + d/p_e,

so their contribution to ell_e is

    A_e(s) = -log(1+d/p_e).                                  (M14.4)

The cancellation in (M14.4) is the reason the normalized estimate below
stays small as e tends to zero.

## 2. Scalar boxes and exact arithmetic input

The physical branch on the present domain inherits the M5 and M10 real
boxes

    207/500 < t < 83/200,       359/360 < q < 1,
    7/10 < u_g,h < 71/100.                                  (M14.5)

The second value box for h is transferred from u_g by the exact symmetry

    t(-e)=t(e),       q(-e)=q(e)^(-1),       h(e)=u_g(-e).

At e=0, u_g=h=eta, where eta=1/sqrt(2). The scalar derivatives are

    u_g'(0)=-1/4,       h'(0)=1/4,
    s_g'(0)=eta/2,      s_h'(0)=-eta/2.

The signed M10 scalar jet, rebuilt with the frozen 384-bit interval type,
checks on |e|<=1/180

    |s_g''| < 1/20,       |s_g'''| < 414/1000,
    |u_g'''| < 3/10,      -26/100 < u_g' < 0.              (M14.6)

Taylor's theorem and the two exact parity identities then give, for
0<e<=E,

    |(h-u_g)/e - 1/2| <= e^2/10,                            (M14.7)
    |beta-eta| <= 7 e^2/50,
    |(s_g+s_h)/2 - c| <= e^2/40,

where c=s_g(0). The M14 ledger also checks

    d < (51/100)e,       p_e > 203/1000,
    p_0 := eta(1-eta u_0(s)) > 203/1000,                   (M14.8)

with u_0(s)=U(sigma,exp(-s)). The critical denominator follows from
eta>7/10 and eta<17/24; the latter radical inequality is checked by
2(17^2)>24^2. On this tiny domain the sharper beta estimate and
eta<99/140 give beta<17/24 as well.

The exact replay is intentionally split. The entries named
input_compatibility in the JSON only check that the rational constants
contain the inherited analytic boxes; they do not certify those boxes.
The I384 scalar intervals and all remaining Fraction inequalities are
actual producer checks.

## 3. Endpoint-safe displacement of the inverse kernel

The critical comparison must include s=0, where direct formulas involving
the square-root discriminant have a vanishing denominator. The needed
comparison uses monotonicity in the parameter t instead.

For v in [0,1], put

    B = t^(-1)+t-(1-t^2)v,
    Delta = B^2-4,
    A_t = t^(-2)-1-2t v,
    c_t = 1-t^2.

Differentiation of the explicit inverse kernel gives

    U_t  = U A_t / sqrt(Delta),

    U_tv = U [ A_t c_t (B+sqrt(Delta)) - 2t Delta ]
              / Delta^(3/2).                                (M14.9)

On the rational enlargement 207/500<=t<=83/200, the exact ledger checks

    A_t > 39/10,       c_t > 4/5,       B >= 2,
    Delta < 41/10,     2t <= 83/100.

The last four bounds follow by the monotonic endpoint substitutions in
t and v; positivity of Delta on the physical t<sigma branch follows from
the M5 inverse-kernel domain. Thus the numerator bracket in U_tv is
bounded below by

    (39/10)(4/5)(2) - (83/100)(41/10)
       = 2837/1000 > 0.                                    (M14.10)

Therefore U_t is positive and increasing in v. Integrate first from t to
T<sigma, use this increase, and then let T increase to sigma. Continuity
of U supplies the endpoint limit:

    0 <= U(sigma,v)-U(t,v)
       <= U(sigma,1)-U(t,1)
       = 1-q
       < e/2.                                               (M14.11)

Here U(sigma,1)=1 and U(t,1)=q on the physical branch. Since
v=exp(-s), (M14.11) proves

    0 <= u_0(s)-u(s) < e/2       for every s>=0,             (M14.12)

including s=0. This argument takes no derivative of the critical kernel
at the endpoint.

For reference, the rational level check used by the ledger is

    v_t(1/2)
      = (1/2-t)(1-t/2)/(t(1-t^2)(1/2))
      > 3/8,

while exp(-1)<3/8 because the Euler number is greater than
1+1+1/2+1/6=8/3. Hence u(s)<1/2 for s>=1.

## 4. Direct fixed-s enclosure for log R_e

The probability measure

    d mu_(s,a)(v)
      = exp(-((1-v)s+v a)) dv / M(s,a)

has

    partial_a log M(s,a) = -E_mu[v],
    partial_sa log M(s,a) = -Var_mu(v),
    0 <= Var_mu(v) <= 1/4.                                  (M14.13)

For the two anchor values, the mean-value formula and (M14.4) yield

    0 <= -ell_e(s)/e
       <= (d/e)/(u_g(1-u h)) + beta E_mu[v].                (M14.14)

For 0<=s<=1, the exponential tilt parameter s-s_g is at most 1. Its
mean is therefore at most the tilt-one mean

    E_mu[v] <= 1/(exp(1)-1) < 3/5.

The final inequality follows from the positive exponential series
exp(1)>8/3. Using (M14.5) and d/e<51/100 gives

    -ell_e(s)/e
      < (51/100)/[(7/10)(29/100)]
        + (18/25)(3/5)
      = 74712/25375
      < 3,                 0<=s<=1.                        (M14.15)

For s>=1, the level check after (M14.12) gives u(s)<1/2. Therefore

    -ell_e(s)/e
      < (51/100)/[(7/10)(1-(71/100)/2)]
        + 18/25
      = 13918/7525
      < 37/20,             s>=1.                            (M14.16)

Equations (M14.15)--(M14.16) are explicit fixed-s enclosures. They
replace an absolute exponential product allowance by constants below 3
and 1.85 for the normalized logarithm.

## 5. Critical normalized factor and its finite-e remainder

Let

    m(s,a)=log M(s,a),       c=s_g(0),       u_0(s)=U(sigma,exp(-s)).

The exact first-order limit of (M14.2) is

    psi(s)
      = -eta - u_0(s)/(2(1-eta u_0(s)))
        + eta partial_a m(s,c).                               (M14.17)

To see the first two terms without differentiating U at the critical
corner, use (M14.4). At e=0, d'(0)=1/2 and

    -1/[2 eta(1-eta u_0)]
      = -eta - u_0/[2(1-eta u_0)],

because eta^2=1/2. The M-factor gives the final term in (M14.17).

For the finite-e comparison, put

    c_e=(s_g+s_h)/2,       f(a)=m(s,a).

The central secant estimate from (M14.13) is

    | [f(c_e+beta e/2)-f(c_e-beta e/2)]/e
         - beta f_a(c_e) |
      <= beta^2 e/16.                                      (M14.18)

Indeed, integrate f_a(c_e+t)-f_a(c_e) over the symmetric interval
[-beta e/2,beta e/2] and use |f_aa|<=1/4. Also,

    |f_a(c_e)-f_a(c)| <= |c_e-c|/4 <= e^2/160.               (M14.19)

Since beta<17/24<18/25, the central remainder satisfies

    beta^2/16 < (17/24)(9/200).

Combining (M14.7), (M14.18), and (M14.19), and using |f_a|<=1, gives

    | [m(s,s_g)-m(s,s_h)]/e - eta m_a(s,c) |
      <= e [ (7/50)E + (17/24)(9/200+E/160) ]
      < e/5.                                               (M14.20)

It remains to bound the combined scalar/anchor term. Let

    p_e=u_g(1-u h),       p_0=eta(1-u_0 eta),
    y=d/p_e.

From (M14.12), the scalar derivative box, and the product rule,

    |p_e-p_0| < (4/5)e.                                    (M14.21)

For example, the two scalar motions cost at most 26e/100 each and the
kernel motion costs e/2; the displayed 4/5 allowance is a rational
enlargement. From (M14.4),

    | A_e(s)/e + 1/(2p_0) |
      <= |d/e-1/2|/p_e
         + (1/2)|1/p_e-1/p_0|
         + |log(1+y)-y|/e.                                 (M14.22)

The first two terms in (M14.22) are less than 11e by

    (E^2/10)/(203/1000) / E < 1/2,
    (1/2)(4/5)/(203/1000)^2 < 10.

Also y<(510/203)e, so

    0 <= y-log(1+y) <= y^2/2

makes the last term less than

    (1/2)(510/203)^2 e < 4e.

Thus

    | A_e(s)/e + 1/(2p_0) | < 15e.                          (M14.23)

Using the identity following (M14.17), equations (M14.20) and (M14.23)
give the pointwise finite-e estimate

    |ell_e(s)/e - psi(s)| < 16e,       s>=0.                 (M14.24)

This estimate uses only positive secants and the displacement bound
(M14.12). It includes s=0 and s=c by continuity.

## 6. Critical variation and the rectangle error

The critical identity (M14.17) has finite variation on the entire
half-line. In the first nonconstant term, u_0 decreases from 1 to sigma.
For

    A(u)=u/[2(1-eta u)],

A is increasing and

    A(1)=1+eta,       A(sigma)=1-eta.

Hence the variation of A(u_0(s)) is 2eta. The probability formula in
(M14.13) gives

    m_sa(s,c)=-Var_mu(v)<=0,

so m_a(s,c) is nonincreasing and has variation at most 1. The constant
term -eta has zero variation. The triangle inequality gives

    TV_[0,infinity)(psi) <= 2eta+eta
                          = 3eta
                          < 17/8.                          (M14.25)

The strict final inequality follows from eta<17/24; the exact ledger
checks the rational endpoint 3(17/24)=17/8. The two varying terms in
(M14.17) can have opposite monotonicity, so this is a total-variation
bound rather than an assertion that psi is monotone.

For a bounded-variation function, the left rectangle rule on the mesh e
satisfies

    | e sum_(j=0)^(n-1) psi(j e)
       - integral_0^(n e) psi(s) ds |
      <= e TV_[0,n e](psi)
      < (17/8)e.                                           (M14.26)

The empty sum case n=0 is exact.

## 7. Scalar geometric factor and the final product envelope

The scalar factor can be written

    r = q(q-t)/(1-tq)
      = 1 - (1-exp(-e))/D.                                 (M14.27)

Put d_*=1-sigma and z=(1-exp(-e))/D. The inherited t/q boxes and
sigma-t<=e^2/8 imply

    D>29/50,       |D-d_*| < (21/100)e.                    (M14.28)

For the second inequality, use

    |D-d_*| = |sigma-tq|
      <= |sigma-t| + t|1-q|
      <= e^2/8 + (83/200)(e/2)
      < (21/100)e.

The elementary bounds

    |(1-exp(-e))/e - 1| <= e/2,
    0 <= -log(1-z)-z <= z^2/[2(1-z)]

give

    | (1-exp(-e))/(eD) - 1/d_* |
      < e [1/(2(29/50))
           +(21/100)/(29/50)^2]
      < (3/2)e,                                            (M14.29)

and

    [-log(1-z)-z]/e
      <= e/[2D(D-e)]
      < 2e.                                                 (M14.30)

The exact Fraction ledger checks the two displayed constants. Since
lambda=1/d_*, equations (M14.27)--(M14.30) imply

    | log r/e + lambda | < 4e.                              (M14.31)

Finally,

    log K_(e,n)
      = x(log r/e) + sum_(j=0)^(n-1) ell_e(j e).

Use (M14.24) to compare the sum with e sum psi:

    | sum ell_e(j e) - e sum psi(j e) |
      < 16 n e^2 = 16 x e.                                 (M14.32)

Equation (M14.26) contributes 17e/8 and (M14.31) contributes 4xe.
Adding the three allowances proves (M14.0):

    |log K_(e,n)-log K_0(x)| < e(17/8+(16+4)x).

The constants are exact rational allowances; no numerical logarithm is
used in the producer.

## Reproduction, provenance, and scope

Run the exact producer without optimization:

    .venv/bin/python -m proofs.m14_smooth_envelope \
      > /tmp/m14-smooth-envelope.json

The script has an explicit __debug__ guard and imports the frozen M10
I384 guard. Its current replay returns status pass with all scalar I384
and Fraction checks true. Optimized mode exits before producing a
certificate. The producer rebuilds the scalar jets from the frozen M10
formulas and imports the frozen M7 I384 interval implementation; it edits
neither source. It performs no index scan, phase scan, numerical
quadrature, or held-out-data read.

Analytic inputs are separated from arithmetic checks:

* M11 supplies the inverse-kernel factorization, positive secants, and
  the real scalar boxes.
* M6 supplies the concavity sign 0<R_e<=1 and the physical scalar
  product definition.
* M10 supplies the signed scalar third-derivative boxes and parity
  consequences used in (M14.7).
* M14_CRITICAL_VARIATION.md supplies the critical first-order identity,
  endpoint-safe kernel displacement, and bounded-variation lemma. Its
  independent review is M14_CRITICAL_VARIATION_REVIEW.md.

The producer's exact source snapshot is HEAD
9a8f2120cd3c04875d877b33b58f521f8d547a56 before these two new files.
The relevant input hashes at that snapshot are:

| input | SHA-256 |
|---|---|
| proofs/M14_CRITICAL_VARIATION.md | 937af31f8da496cd7888e4bd95e9254418ff9d1d071505d935ad14c2534ed691 |
| proofs/M14_CRITICAL_VARIATION_REVIEW.md | 1d52b68c6dbbc9ea92d1377a19c78f56619e1163d71f3af12949c4ff2f8dad77 |
| proofs/M11_SMOOTH_PHASE_BOUND.md | 15e8c64e5d554a12eb40b68ef0b724d2aead52042779516fce9e78628f180f07 |
| proofs/M11_SMOOTH_PHASE_REVIEW.md | 1533c093f7ce31632759e3492fca5e01ddc79b96ea6c8bc3538efd41aed41b46 |
| proofs/M10_BETA_REAL.md | 51b59ecaea7fa22647d76471f8ecef9e8483581fdd3941a02d56b0fb22397f80 |
| proofs/m10_beta_real.py | 8387dd9af2896cdeef4871f008a495d0507aca96c27b21399fac0960458d3231 |
| proofs/M6_EFFECTIVE_PRODUCT.md | a3b6b878102cfbe022aada6477c78c8641edc5d25b813ea7030f032fce96c522 |
| proofs/m7_finite_poles.py | 3712829fbf510e558e9215c7219731b40678ca9525e36387bb1f9d528f912c26 |

This is a smooth-product envelope for the stated small-e domain. It
supplies a useful quantitative input to moment comparisons. It carries no
claim for the larger interval e<=0.17/32, for finite-N phase existence, for
the full F_N derivative, or for residue noncancellation.
