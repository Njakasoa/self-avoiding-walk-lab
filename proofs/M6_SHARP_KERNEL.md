# M6: a sharp real kernel box for the product Taylor bound

Status: supporting real estimate for M6.  This note does not replace the
signed-product lemma in M6_EFFECTIVE_PRODUCT.md and does not alter any M5
source.  It supplies a smaller real constant on
\[
 0<e\le10^{-8},\qquad B_{\rm sharp}=10^{12},
\]
for the product Taylor and Hölder estimates.  No \(N=1024\) value is used.

Put
\[
 \sigma=\sqrt2-1,\quad q=e^{-e/2},\quad
 C=q-t,\quad D=1-tq,\quad
 g_e(s)=t-DU(t,e^{-s}).
\]
Use \(I=[1/10,1/4]\).  The real parameter bounds from the accepted kernel
note imply
\[
 .4<t<\sigma<.415,\qquad .58<D<.60,\qquad
 |t-\sigma|\le e^2/8,\qquad 1-e/2\le q\le1. \tag{1}
\]
For the auxiliary complex estimates, take
\[
 |e|\le r_e=10^{-5},\qquad
 \mathcal T:=\{s:\operatorname {dist}(s,I)\le r_s=10^{-4}\}.
 \tag{2}
\]
Thus every point of \(\mathcal T\) has
\(0.0999\le\operatorname {Re}s\le0.2501\) and
\(|\operatorname {Im}s|\le10^{-4}\).  The larger M5 strip
\(\operatorname {dist}(s,I)\le10^{-3}\) is used only for its already
recorded discriminant margin.
The root equation and its real enclosure give
\[
 |t-\sigma|<|e|^2/10,\qquad |q|<1.001,\qquad |q-1|\le|e|. \tag{3}
\]
On \(\mathcal T\), the elementary boxes used below are
\[
 \operatorname {Re}a>.85,\quad |a|<1.6,\quad
 |a_t|<2.3,\quad \operatorname {Re}\Delta>.03,\quad
 |D|<1.42,\quad |a_s|<.315, \tag{4}
\]
where
\[
 a=1+t^2-t(1-t^2)e^{-s},\qquad
 \Delta=a^2-4t^2.
\]
For completeness, (4) follows by inserting
\(|t-\sigma|<2.5\cdot10^{-8}\),
\(e^{-0.2501}<|e^{-s}|<e^{-0.0999}\),
\(|\operatorname {Im}s|\le10^{-4}\), and
\(\sigma\in(.414,.415)\) into the displayed polynomial expressions.
More explicitly, \(|1+t^2|<1.18\),
\(|\partial_ta|<1.35<2.3\), and
\(|a_s|=|t(1-t^2)e^{-s}|<.312<.315\).
The imaginary part of \(a\) is below \(1.2\cdot10^{-3}\), so
\(\operatorname {Re}(a^2-4t^2)>.03\) follows from
\(\operatorname {Re}a>.85\) and \(|t|<.415001\).
The same discriminant margin on the larger M5 strip is the one used in
the accepted disk calculation.

Let \(w=\sqrt\Delta\) be the branch with positive real part.  From (4),
\[
 |w|>\sqrt{.03}>.17,\qquad
 \operatorname {Re}(a+w)>.85,\qquad
 |U|=\left|\frac{2t}{a+w}\right|<1. \tag{5}
\]

## 1. Algebraic derivative bounds

The identities
\[
 U_s=-\frac{a_sU}{w},\qquad
 g_s=\frac{D a_sU}{w}, \tag{6}
\]
follow by differentiating \(U=2t/(a+w)\), using
\(w_s=aa_s/w\).  Therefore (4)--(5) give
\[
 |g_s|<
 1.42\,\frac{.315}{.17}<3. \tag{7}
\]
Differentiating (6) once more gives
\[
 g_{ss}=DU\left(
 -\frac{a_s}{w}-\frac{a_s^2}{w^2}
 -\frac{a\,a_s^2}{w^3}\right),
\]
and hence
\[
 |g_{ss}|
 <1.42\left(\frac{.315}{.17}
       +\frac{.315^2}{.17^2}
       +\frac{1.6\,.315^2}{.17^3}\right)
 <100. \tag{8}
\]

To control the parameter derivatives, Cauchy's estimate applied to (3) on
\(|e|=5\cdot10^{-4}\) gives, for \(|e|\le r_e\),
\[
 |t_e|<
 \frac{(5\cdot10^{-4})^2/10}{5\cdot10^{-4}-10^{-5}}
 <2\cdot10^{-4},\qquad
 |q_e|<.501. \tag{9}
\]
Thus
\[
 |D_e|=|-t_eq-tq_e|<.21. \tag{10}
\]
Also
\[
 |a_t|<2.3,\qquad |\Delta_t|<11,\qquad
 |w_t|=\frac{|\Delta_t|}{2|w|}<33,
\]
so
\[
 |U_t|
 \le\frac2{.85}
 +\frac{2\,.415(2.3+33)}{.85^2}<45. \tag{11}
\]
It follows from \(g=t-DU\) that
\[
 |g_e|=|t_e-D_eU-DU_tt_e|<.23<1. \tag{12}
\]

For the mixed derivative, use
\[
 |a_{se}|<.0002,\qquad |U_e|<.009,\qquad |w_e|<.0066.
\]
Differentiating (6) in \(e\) gives
\[
 g_{es}
 =D_e\frac{a_sU}{w}
 +D\left(\frac{a_{se}U}{w}
 +\frac{a_sU_e}{w}
 -\frac{a_sUw_e}{w^2}\right),
\]
and therefore
\[
 |g_{es}|
 <.21\frac{.315}{.17}
 +1.42\left(
 \frac{.0002}{.17}
 +\frac{.315\,.009}{.17}
 +\frac{.315\,.0066}{.17^2}\right)
 <1. \tag{13}
\]
The arithmetic in (7)--(13) is recorded independently in
proofs/m6_sharp_kernel_boxes.py.

## 2. Root disks and the crossing logarithm

The exact critical derivative is \(g_0'(s_*)=\sigma>.4\).  From (8), with
\(r_s=10^{-4}\),
\[
 |g_0(s)|\ge .4r_s-\frac{100}{2}r_s^2
 =3.95\cdot10^{-5}
 \quad\text{when }|s-s_*|=r_s. \tag{14}
\]
The parameter estimate (12) gives
\[
 |g_e(s)-g_0(s)|<|e|. \tag{15}
\]
Moreover
\[
 \delta=\frac{t^2(1-q^2)}{q-t},\qquad |\delta|<.3|e|, \tag{16}
\]
because \(|1-q^2|\le e^{|e|}|e|\), \(|t|^2<.173\), and
\(|q-t|>.58\).
On \(|e|=r_e\), both perturbations in (15)--(16) are below the lower
bound in (14).  Rouché's theorem therefore puts the zeros \(s_g(e)\) and
\(s_h(e)\) of \(g_e\) and \(g_e+\delta\), respectively, in
\[
 |s-s_*|<r_s. \tag{17}
\]

For real \(s\in I\), join \(s\) to either root by a straight segment.
Its imaginary part is at most \(r_s\), and its real part remains in \(I\)
because \(s_*\in(.15,.17)\).  The real lower bound
\(g_0'(y)>.04\) on \(I\), (8), and (13) give on each such segment
\[
 \operatorname {Re}g_{e,s}>.04-100r_s-r_e>.02. \tag{18}
\]
Consequently the divided differences
\[
 F_e(s)=\int_0^1g_{e,s}\bigl(s_g+u(s-s_g)\bigr)\,du,\qquad
 G_e(s)=\int_0^1g_{e,s}\bigl(s_h+u(s-s_h)\bigr)\,du
\]
satisfy
\[
 \operatorname {Re}F_e(s),\operatorname {Re}G_e(s)>.02,\qquad
 |F_e(s)|,|G_e(s)|<3. \tag{19}
\]
Their principal logarithms are analytic in the parameter disk.  Set
\[
 {\cal L}(e,s)=\log F_e(s)-\log G_e(s).
\]
Then \({\cal L}(0,s)=0\), \(|{\cal L}(e,s)|<20\), and the exact first
parameter derivative is the M5 function
\[
 \partial_e{\cal L}(0,s)=\psi(s). \tag{20}
\]
Cauchy's Taylor remainder at radius \(r_e=10^{-5}\), for real
\(0<e\le10^{-8}\), yields
\[
 \left|\frac{\log R_e(s)}e-\psi(s)\right|
 \le\frac{40e}{r_e^2}
 =4\cdot10^{11}e,\qquad s\in I. \tag{21}
\]

The same construction holds on the whole tube \(\mathcal T\), including
the two endpoints.  Indeed \(\mathcal T\) is convex, and the straight
segment from \(s\in\mathcal T\) to either root in
\(|s-s_*|<r_s\) stays in \(\mathcal T\); the boxes (4), hence (18)--(19),
hold on that segment.  Applying the two-variable Cauchy estimate to
\({\cal L}\) on the \(e\)-disk and this fixed \(s\)-tube gives
\[
 |\psi(s)|<\frac{20}{r_e}=2\cdot10^6,\qquad
 |\psi'(s)|<\frac{20}{r_er_s}=2\cdot10^{10}. \tag{22}
\]
There is no endpoint loss: integrating the second bound along \(I\)
gives, for \(s,x\in I\),
\[
 |\psi(s)-\psi(x)|<2\cdot10^{10}|s-x|
 \le2\cdot10^{10}|s-x|^{1/2}. \tag{23}
\]

## 3. Exterior real estimate

The local derivative estimate (12) is not used to obtain a uniform
half-line estimate.  That estimate is instead obtained directly from
the two square-root formulas.  For \(v=e^{-s}\in[0,1]\), write
\[
 a_t(v)=1+t^2-t(1-t^2)v,\qquad
 \Delta_t(v)=a_t(v)^2-4t^2,\qquad
 U_t(v)=\frac{2t}{a_t(v)+\sqrt{\Delta_t(v)}}.
\]
For \(t\in[.4,\sigma]\), the physical branch has
\(t\le U_t(v)\le1\), so its denominator is at least \(2t>.8\).
Moreover
\[
 |\partial_ta_t(v)|=|2t-(1-3t^2)v|<1.35,\qquad
 |a_t(v)|<1.18,
\]
and hence, with \(d_t=|t-\sigma|\),
\[
 |a_t-a_\sigma|<2.4d_t,\qquad
 |\Delta_t-\Delta_\sigma|<10d_t. \tag{24}
\]
Here the second inequality uses
\((1.18+1.18)\,2.4+4(.415+.415)<10\).
Both discriminants are nonnegative on this physical real box, and
therefore
\[
 |\sqrt{\Delta_t}-\sqrt{\Delta_\sigma}|
 \le\sqrt{|\Delta_t-\Delta_\sigma|}
 <\sqrt{10d_t}<1.12e. \tag{25}
\]
Here \(d_t\le e^2/8\), and the last inequality is valid for
\(e\le10^{-8}\).  Comparing the two fractions for \(U_t\), using the
two denominator lower bounds, gives
\[
 |U_t(v)-U_\sigma(v)|<3e. \tag{26}
\]
The same calculation is valid at \(v=1\), where the critical
discriminant can vanish, because it uses the square-root difference
inequality rather than a derivative of the square root.  Also
\[
 |D-(1-\sigma)|
 =|\sigma-tq|
 \le|\sigma-t|+t|1-q|<.22e.
\]
Consequently, uniformly for every \(s\ge0\),
\[
 |g_e(s)-g_0(s)|<3e. \tag{27}
\]
This is an independent real estimate for \(0<e\le10^{-8}\); the
\(10^{-10}\) restriction in the older M5 weight note is not used here.

The accepted real kernel bounds outside \(I\) are
\[
 |g_0(s)|>.001,\qquad
 s_*\in(.15,.17). \tag{28}
\]
Together with the real crossing estimate below,
\(|s_g-s_*|<12e\), these imply
\[
 |s-s_g|>.049\quad(s\le.1),\qquad
 |s-s_g|>.079\quad(s\ge.25),\qquad
 |g_e(s)|>.00099. \tag{29}
\]
The elementary rational estimate
\[
 \left|\frac{\delta}{e}-\frac{\sigma^2}{1-\sigma}\right|<e \tag{30}
\]
follows by writing
\[
 \frac{\delta}{e}=\frac{t^2}{q-t}\frac{1-e^{-e}}e,
\]
using \(0\le1-(1-e^{-e})/e\le e/2\),
\(|t-\sigma|\le e^2/8\), and
\(|(q-t)-(1-\sigma)|\le.51e\).

On the real crossing, (18) and (16) give
\[
 |s_g-s_*|<12e,\qquad
 |s_g-s_h|<16e.
\]
For the first bound, integrate the sharper \(|\partial_e g|<.23\)
from (12) at \(s=s_*\), then divide by the real slope \(>.02\);
the second uses \(|\delta|<.3e\) and the same slope.
At a point between \(s_h\) and \(s_g\), (8), (13), and
\(g_0'(s_*)=\sigma\) give
\[
 |\eta_e-\eta|<3\cdot10^5e,\qquad \eta=\frac1{\sqrt2}. \tag{31}
\]
Indeed \(|g_{e,s}-\sigma|<6501e\), and
\[
 \left|\frac{\delta/e}{g_{e,s}}-\frac{\kappa}{\sigma}\right|
 \le\frac e{.02}
 +\frac{.3(6501e)}{.02\,.4}<3\cdot10^5e.
\]

For \(s\notin I\), use the exact two-log identity
\[
 \log R_e(s)=
 \log\left(1+\frac{\eta_e e}{s-s_g}\right)
 -\log\left(1+\frac{\delta}{g_e(s)}\right). \tag{32}
\]
The first-order function obtained by differentiating this identity is
\[
 \psi(s)=\frac{\eta}{s-s_*}-\frac{\kappa}{g_0(s)},\qquad
 \kappa=\frac{\sigma^2}{1-\sigma}. \tag{33}
\]
The two arguments have modulus below \(1/2\) for \(e\le10^{-8}\).
For \(s\le.1\) and \(s\ge.25\), respectively, (28)--(31) give
\[
 \left|\frac{\eta_e}{s-s_g}-\frac{\eta}{s-s_*}\right|<7\cdot10^6e,
\qquad
 \left|\frac{\delta/e}{g_e(s)}-\frac{\kappa}{g_0(s)}\right|
 <2\cdot10^6e.
\]
The remainders from \(|\log(1+x)-x|\le2x^2\) are below
\(3\cdot10^5e\).  Combining these estimates with (27) gives
\[
 \left|\frac{\log R_e(s)}e-\psi(s)\right|<10^8e,
 \qquad s\notin I. \tag{34}
\]
The exterior Hölder estimate from the accepted real calculation is
\[
 |\psi(s)-\psi(x)|<10^{10}|s-x|^{1/2}
\]
on each exterior component.  Splitting at the two endpoints costs less
than \(\sqrt3\).

For completeness, the remaining scalar inputs in (P) are also effective
on \(0<e\le10^{-8}\).  With
\[
 r=\frac{q(q-t)}{1-tq}
   =1-\frac{1-q^2}{1-tq},\qquad
 \lambda=\frac1{1-\sigma},
\]
put \(x=(1-e^{-e})/(1-tq)\).  Then \(0<x<2e\), \(r=1-x\), and
\(r<e^{-e}\).  Since
\[
 \left|\frac{1-e^{-e}}e-1\right|\le\frac e2,\qquad
 |(1-tq)-(1-\sigma)|<.22e,
\]
the identity \(-\log(1-x)=x+O(x^2)\), with
\(0\le-\log(1-x)-x\le x^2/(2(1-x))\), gives
\[
 \left|\frac{-\log r}{e}-\lambda\right|<10e. \tag{35}
\]
Likewise, for \(z_0=[t-(1-tq)q]^{-1}\), the denominator differs from
\(-\sigma^2\) by less than \(.52e\), while its modulus is \(>.17\).
Indeed
\[
 |D-(1-\sigma)|\le e^2/8+.415(e/2)<.208e,
\]
so \(|(1-tq)q-(1-\sigma)|<.208e+.30e\); the residual
\(|t-\sigma|\le e^2/8\) is absorbed in the displayed \(.52e\) margin.
Thus
\[
 |z_0+1/\sigma^2|<20e,\qquad |z_0|<10. \tag{36}
\]
Equation (31) gives \(\eta_e\in[.70,.72]\) because
\(3\cdot10^5e\le.003\) on the stated domain.
The sign and positivity inputs \(0<R_e\le1\) are the real
positive-series/concavity lemma in
M6_EFFECTIVE_PRODUCT.md.  Its algebraic proof applies here because the
root boxes give \(0<s_h<s_g\) throughout \(0<e\le10^{-8}\); this is the
near-critical scope needed below.  Hence \(\psi\le0\), while (22), (34),
and (33) give \(|\psi|\le10^{12}\).

Combining (21), (23), and (34), a common real bound valid for all \(s,x\ge0\)
is
\[
 \boxed{
 \left|\frac{\log R_e(s)}e-\psi(s)\right|\le10^{12}e,\qquad
 |\psi(s)-\psi(x)|\le10^{12}|s-x|^{1/2}.
 } \tag{37}
\]
The bound \(|\psi|\le10^{12}\) follows from (22), (28), and (29).

## Scope

The only inherited inputs are the real kernel bounds in M5 and the
elementary exterior separation in (28)--(29), together with the critical
formula for \(\psi\) already recorded in M6_EFFECTIVE_PRODUCT.md.  The
remaining scalar inputs required by (P), namely \(r,z_0\), and the
\(\eta_e\) range, are supplied directly in (31) and (35)--(36) on the
same \(0<e\le10^{-8}\) domain.  The crossing constants
\(3,100,1,45\), the root radii, the Cauchy remainder, and the resulting
\(10^{12}\) common constant are derived above and can be replayed by
proofs/m6_sharp_kernel_boxes.py using exact rational arithmetic.  The
result is real; it does not assert a complex phase theorem or a final W
threshold.
