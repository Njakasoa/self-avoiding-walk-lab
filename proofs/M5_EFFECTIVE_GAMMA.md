# M5: effective real Gamma bounds for \(T_n\)

This note isolates the real Gamma factor in the moment estimate.  It uses
the phase/kernel input already recorded in
M5_EFFECTIVE_KERNEL.md and does not estimate the nonsingular product, the
kernel endpoint, or the moment weights.

Let

\[
 \eta=\frac1{\sqrt2},\qquad
 a=N+\theta,\qquad b=a-\eta_e,\qquad
 \theta\in\left[\frac45,\frac9{10}\right],
\]

where \(e=\varepsilon_N(\theta)\), \(s_g=e\,a\), and
\[
 T_n(a,b)=\prod_{j=0}^{n-1}\frac{j-a}{j-b}.
\]

The only phase hypotheses used here are the explicit real bounds from the
kernel lemma:

\[
 0<e\le10^{-100},\qquad
 \frac7{10}\le\eta_e\le\frac{18}{25},\qquad
 |\eta_e-\eta|\le 10^{50}e.                              \tag{1}
\]

For the conversion from the exact center \(s_g\) to \(s_*\), the parent
ledger separately supplies \(0.15<s_g<0.17\).  No relation between \(e\)
and \(s_*/N\) is used in the Gamma estimates below.

## Wendel's inequality

For \(x>0\) and \(0\le u\le1\), put
\[
 A_u(x)=\frac{\Gamma(x+u)}{\Gamma(x)x^u}.
\]
Wendel's inequality gives
\[
 \left(\frac{x}{x+u}\right)^{1-u}\le A_u(x)\le1.           \tag{2}
\]
For completeness, Holder's inequality applied to the positive Gamma
integral gives log-convexity and hence
\(\Gamma(x+u)\le\Gamma(x)^{1-u}\Gamma(x+1)^u=x^u\Gamma(x)\).
Applying this upper bound at base \(x+u\) with shift \(1-u\), then
using \(\Gamma(x+1)=x\Gamma(x)\), gives the lower bound in (2).
Consequently, for \(x\ge1\) and \(u,v\in[0,1]\),
\[
 \left|
 \log\frac{\Gamma(x+u)}{\Gamma(x+v)}
 -(u-v)\log x\right|\le\frac2x.                           \tag{3}
\]
Each \(|\log A_u(x)|\) is at most
\(\log(1+u/x)\le1/x\).  In particular,
\[
 \frac12x^{u-v}\le
 \frac{\Gamma(x+u)}{\Gamma(x+v)}
 \le2x^{u-v}\qquad(x\ge1).                                \tag{4}
\]

For \(z\ge1/10\), the same inequality before the simplification
\(x\ge1\) gives
\[
 \frac{\Gamma(z)}{\Gamma(z+\eta_e)}
 \le z^{-\eta_e}
 \left(1+\frac{\eta_e}{z}\right)^{1-\eta_e}
 <2z^{-\eta_e},                                          \tag{5}
\]
because \((1+7.2)^{3/10}<2\).

## Exact positive Gamma forms

The fixed integer split is \(n\le N\) and \(n\ge N+1\).  Reflection gives
the positive-argument identities

\[
 T_n=
 \frac{\Gamma(a+1)\Gamma(b-n+1)}
      {\Gamma(b+1)\Gamma(a-n+1)}
 \quad(0\le n\le N),                                    \tag{6}
\]

\[
 T_n=
 \frac{\sin(\pi\theta)}{\sin(\pi(\theta-\eta_e))}
 \frac{\Gamma(a+1)\Gamma(n-a)}
      {\Gamma(b+1)\Gamma(n-b)}
 \quad(n\ge N+1).                                        \tag{7}
\]

All Gamma arguments in (6)--(7) are positive.  For (6), put
\(d=a-n\ge\theta\ge4/5\).  For (7), put
\(d=n-a\ge1-\theta\ge1/10\).  The sine multiplier obeys

\[
 0<
 \frac{\sin(\pi\theta)}{\sin(\pi(\theta-\eta_e))}
 <5,                                                     \tag{8}
\]
since \(0.08\le\theta-\eta_e\le0.20\).

## Absolute domination at the crossing

Assume \(a\ge200\), and consider indices satisfying
\[
 d=|n-a|\le\frac a2.                                     \tag{9}
\]
Using (4) in (6), with bases \(a\) and \(d\) (the harmless
\(d\ge4/5\) endpoint enlargement costs less than a factor \(3\)), gives
\[
 |T_n|\le10\left(\frac ad\right)^{\eta_e}
 \qquad(n\le N).                                         \tag{10}
\]
For \(n\ge N+1\), (5), (7), and (8) give
\[
 |T_n|\le20\left(\frac ad\right)^{\eta_e}.                \tag{11}
\]
On (9), \(a/d\ge2\).  Since \(\eta_e<19/25\), and
\(d\ge1/10\), (10)--(11) imply the uniform bound

\[
 \boxed{\quad
 |T_n|\le1000
 \left(\frac a{1+d}\right)^{19/25}.
 \quad}                                                   \tag{12}
\]

Indeed \(d^{-1}\le11(1+d)^{-1}\) for \(d\ge1/10\), and
\(11^{19/25}<7\); the constants in (10)--(11) are therefore safely
covered by \(1000\).

Since \(x_n=ne\) and \(s_g=ea\),
\[
 \frac a{1+|n-a|}
 =\frac{s_g}{e+|x_n-s_g|}.                                \tag{13}
\]
Thus, whenever a real crossing window satisfies
\(\rho+e\le s_g/2\),

\[
 \boxed{\quad
 |T_n|\le1000\,
 (e+|x_n-s_g|)^{-19/25}
 \quad (|x_n-s_g|<\rho). \quad}                           \tag{14}
\]

The factor \(s_g^{19/25}\) was dropped using \(s_g<1\).  This is the
absolute Gamma domination. Moving the center from \(s_g\) to \(s_*\)
with the parent bound \(|s_g-s_*|\le4\cdot10^5 e\) costs an additional
multiplicative factor at most \(10^6\), giving a constant at most
\(10^9\) before the smooth product is included.

The corresponding crossing mass is explicit.  With \(p=19/25\),
\[
 e\sum_{|x_n-s_g|<\rho}|T_n|
 \le 12000\,(\rho+e)^{1-p}
 =12000\,(\rho+e)^{6/25}.                                \tag{15}
\]
To see this, sum separately on both sides and use
\[
 e\sum_{k=0}^{K}(e+ke)^{-p}
 \le e^{1-p}
 \left(1+\frac{(K+1)^{1-p}}{1-p}\right),
\]
with \(K e\le\rho\), then enlarge the constant.  No sign of \(T_n\) is
used in (12)--(15).

## Relative Gamma error away from the crossing

Define the exact-\(\eta_e\) comparison profile on the mesh \(x_n=ne\):
\[
 {\cal T}_{e,\theta}(x_n)=
 \begin{cases}
 (a/(a-n))^{\eta_e},&n\le N,\\[1ex]
 \displaystyle
 \frac{\sin(\pi\theta)}{\sin(\pi(\theta-\eta_e))}
 (a/(n-a))^{\eta_e},&n\ge N+1.
 \end{cases}                                             \tag{16}
\]

If
\[
 a\ge200,\qquad |n-a|\ge10,                               \tag{17}
\]
then (3), applied to the two Gamma ratios in (6) or (7), gives

\[
 \boxed{\quad
 \left|
 \log\frac{T_n}{{\cal T}_{e,\theta}(x_n)}
 \right|
 \le\frac3a+\frac3{|n-a|}.
 \quad}                                                   \tag{18}
\]

For the pre-side, use the bases \(a\) and \(a-n\); for the post-side use
the bases \(a\) and \(n-a\).  The sine multiplier is already exact in
(16).  This is the requested Wendel bound: the error is
\(O(a^{-1}+|n-a|^{-1})\), with no unspecified Gamma constant.  Since
the right side of (18) is at most \(0.315\), exponentiation also gives

\[
 \left|
 \frac{T_n}{{\cal T}_{e,\theta}(x_n)}-1
 \right|
 \le 2\left(\frac3a+\frac3{|n-a|}\right).                 \tag{19}
\]

In physical variables, if \(|x_n-s_g|\ge\rho\), then
\(|n-a|\ge\rho/e\), so (18) becomes
\[
 \left|
 \log\frac{T_n}{{\cal T}_{e,\theta}(x_n)}
 \right|
 \le\frac3a+\frac{3e}{\rho}.                              \tag{20}
\]
The first term is \(O(e)\) after using the parent ledger's
\(s_g=ea\ge0.15\).  This is the effective \(O(e/\rho)\) Gamma error
before replacing \(\eta_e\) and \(s_g\) by their limits.

## Explicit cost of replacing \(\eta_e\) by \(\eta\)

The parent aggregation may instead compare (16) with the critical profile
having exponent \(\eta\).  The Gamma estimate itself contributes (20).
The exponent replacement contributes exactly
\[
 |\eta_e-\eta|\,
 \left|\log\frac a{|n-a|}\right|
 \le10^{50}e\,
 \left|\log\frac a{|n-a|}\right|.                         \tag{21}
\]
If \(x_n\le S\) and \(|x_n-s_g|\ge\rho\), then
\[
 \left|\log\frac a{|n-a|}\right|
 \le 2+|\log\rho|+\log(2+S),                              \tag{22}
\]
using \(0.15<s_g<0.17\).  The sine factor has the analogous bound
\[
 \left|
 \log\frac{\sin(\pi(\theta-\eta))}
          {\sin(\pi(\theta-\eta_e))}
 \right|
 \le13\,10^{50}e,                                        \tag{23}
\]
because \(\pi\cot(\pi x)<13\) for \(0.08\le x\le0.20\).
Combining (20)--(23), the Gamma-only logarithmic error after the exponent
replacement is bounded by
\[
 10^{52}e\,
 \left[
 \rho^{-1}+|\log\rho|+\log(2+S)
 \right],                                                 \tag{24}
\]
provided \(\rho\le1/10\).  The terms \(3/a\) and \(3e/\rho\) from
(20) are absorbed here using \(a=s_g/e\) and \(s_g>0.15\).
Whenever the right side is at most \(1/10\), the corresponding relative
error is at most
\[
 10^{53}e\,
 \left[
 \rho^{-1}+|\log\rho|+\log(2+S)
 \right].                                                 \tag{25}
\]
The larger \(10^{59}\) coefficient in the parent ledger safely covers
(25), the center replacement \(s_g\to s_*\), and the other non-Gamma
factors.  No such other factors are asserted here.

## Ledger conditions and status

The Gamma estimate requires exactly the following conditions:

1. \(e\le10^{-100}\) and (1), supplied by the effective kernel lemma.
2. \(a=N+\theta\ge200\).
3. For the crossing bound, \(\rho+e\le s_g/2\).
4. For the relative Wendel bound, \(|n-a|\ge10\); in a physical window
   this is implied by \(\rho\ge10e\).
5. For (24)--(25), \(x_n\le S\), \(\rho\le1/10\), and the displayed
   logarithmic error must be \(\le1/10\) before exponentiation.

The note does not claim that the kernel, product, weight, or tail lemmas
hold automatically from these five conditions.  In particular, it does not
prove a W first index, uniqueness, or simplicity.

Provenance: the Gamma identities are the BB2014 formulas reproduced in
M3_NON_DFINITE_CANDIDATE.md and W_NON_DFINITE.md.  The parameter input (1)
is from the parent-owned M5_EFFECTIVE_KERNEL.md. Its final source hash is
recorded by the effective-threshold receipt and independent review.
