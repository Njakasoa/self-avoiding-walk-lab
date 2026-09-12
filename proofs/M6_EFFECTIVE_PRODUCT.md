# M6: signed real bounds for the nonsingular product

Status: real-product reduction for the M5 aggregation.  The main conclusion is
an exact sign bound, not a numerical fit:

\[
 0<R_e(s)\le1,\qquad
 0<\prod_{j<n}R_e(je)\le1.
\]

This removes the factor \(\exp(10B)\) from the absolute domination of the
product, where the M5 kernel note used \(B=10^{50}\).  The remaining
\(B\)-dependent Taylor error is additive and is never put in an exponential.
This note does not prove the Gamma transfer, the phase inverse, the directed
term, or the final W threshold.  No \(N=1024\) calculation is used.

The statements involving \(R_e\) assume \(0<s_h<s_g\), so that both
secant anchors belong to the real half-line of concavity. This holds in
the near-critical domain used here, \(0<e\le10^{-100}\), by the M5
phase and separation bounds. The concavity statement itself holds for
every \(0<t<\sigma\); no global small-\(t\) sign claim for \(R_e\) is made.

Use the M3 notation
\[
 C=q-t,\qquad D=1-tq,\qquad E=1-q^2,\qquad
 \delta=\frac{t^2E}{C},\qquad r=\frac{qC}{D},
\]
\[
 g_e(s)=t-D\,U(t,e^{-s}),\qquad
 s_g:\ g_e(s_g)=0,\qquad s_h:\ g_e(s_h)+\delta=0.
\]
For the real physical branch \(0<t<\sigma=\sqrt2-1\), the accepted
M5 bounds give \(C,D,\delta>0\), and hence \(s_h<s_g\).

## 1. A positive-coefficient proof of monotonicity and concavity

Put \(Y=U(t,v)-t\).  The inverse kernel equation is exactly
\[
 v=\frac{Y(1-t^2-tY)}{t(1-t^2)(t+Y)},
\]
or, equivalently,
\[
 Y=v\,\Phi_t(Y),\qquad
 \Phi_t(Y)=\frac{t(t+Y)}{1-\alpha_tY},\qquad
 \alpha_t=\frac{t}{1-t^2}. \tag{1}
\]
For \(0<t<\sigma\), the physical solution at \(0\le v\le1\) has
\(0\le Y\le q-t\), and
\(1-\alpha_tY>0\).  Therefore \(\Phi_t(Y)\) has a power series with
nonnegative coefficients:
\[
 \Phi_t(Y)=t(t+Y)\sum_{k\ge0}(\alpha_tY)^k. \tag{2}
\]
Lagrange inversion applied to \(Y=v\Phi_t(Y)\) gives
\[
 Y(t,v)=\sum_{m\ge1}c_m(t)v^m,\qquad c_m(t)\ge0. \tag{3}
\]
For \(t<\sigma\) this series converges at \(v=1\); the critical statements
below follow by taking the monotone real limit \(t\uparrow\sigma\).

Since \(v=e^{-s}\),
\[
 g_e(s)=t-Dt-D\sum_{m\ge1}c_m(t)e^{-ms}. \tag{4}
\]
For \(s>0\), termwise differentiation gives
\[
 g_e'(s)=D\sum_{m\ge1}m c_m(t)e^{-ms}>0,\qquad
 g_e''(s)=-D\sum_{m\ge1}m^2c_m(t)e^{-ms}<0. \tag{5}
\]
Thus \(g_e\) is increasing and concave on \([0,\infty)\); at a possible
square-root endpoint the assertion is understood by continuous extension
of the secant inequalities.  This proof uses only positivity of the
physical real series.

## 2. Secant slopes force \(R_e\le1\)

For an increasing concave function \(g\), define the continuous secant slope
\[
 {\cal S}_g(s,a)=
 \begin{cases}
  \dfrac{g(s)-g(a)}{s-a},&s\ne a,\\[1ex]
  g'(a),&s=a.
 \end{cases}
\]
For fixed \(s\), the map \(a\mapsto{\cal S}_g(s,a)\) is nonincreasing.
This follows by writing each secant as an average of the decreasing
derivative \(g'\): moving the right endpoint to the right adds smaller
derivatives, while moving the left endpoint to the right removes larger
derivatives.  The case where \(s\) lies between the two endpoints follows
from the same ordering of the two derivative averages.

Define the removable divided differences
\[
 F_e(s)=\frac{g_e(s)}{s-s_g}
       ={\cal S}_{g_e}(s,s_g),\qquad
 G_e(s)=\frac{g_e(s)+\delta}{s-s_h}
       ={\cal S}_{g_e}(s,s_h). \tag{6}
\]
The second equality for \(G_e\) uses \(g_e(s_h)=-\delta\).  Since
\(s_h<s_g\), (6) and the secant monotonicity give
\[
 0<F_e(s)\le G_e(s)\qquad(s\ge0). \tag{7}
\]
Strict positivity follows from strict increase of \(g_e\), with the values
at the two removable points obtained by continuity.  Therefore the
nonsingular product factor
\[
 R_e(s)=\frac{F_e(s)}{G_e(s)}
\]
satisfies the exact real bound
\[
 \boxed{0<R_e(s)\le1,\qquad \ell_e(s):=\log R_e(s)\le0.} \tag{8}
\]
This includes intervals containing \(s_h\) or \(s_g\); no lower bound on a
raw sampled denominator is used.

The pointwise critical limit already identified in M5 is
\[
 \psi(s)=\lim_{e\downarrow0}\frac{\ell_e(s)}e
       =-\frac{\kappa}{g_0(s)}+\frac{\eta}{s-s_*},
 \qquad
 \kappa=\frac{\sigma^2}{1-\sigma},\quad \eta=\frac1{\sqrt2},
\]
with its removable value at \(s=s_*\).  Taking the limit in (8) gives
\[
 \boxed{\psi(s)\le0\quad(s\ge0).} \tag{9}
\]

There is also an exact parity improvement for the root separation. Inverting
the kernel at the two zero locations gives
\[
 v_g(e)=\frac{q(D-t^2)}{D(1-t^2)},\qquad
 v_h(e)=\frac{C-t^2q}{qC(1-t^2)}. \tag{10a}
\]
The defining equation for \(t\) is even in \(e\), so \(t(-e)=t(e)\) and
\(q(-e)=q(e)^{-1}\). Hence
\[
 C(-e)=\frac{D(e)}{q(e)},\qquad D(-e)=\frac{C(e)}{q(e)},\qquad
 v_g(-e)=v_h(e).
\]
With \(s_g(e)=-\log v_g(e)\), this gives
\[
 s_h(e)=s_g(-e),\qquad
 \eta_e=\frac{s_g(e)-s_h(e)}e
       =\frac{s_g(e)-s_g(-e)}e. \tag{10b}
\]
Thus \(\eta_e\) is an even analytic function and
\(\eta_e=\eta+O(e^2)\). This identity is exact and is a possible route to
a much smaller real Taylor constant. The numerical ledger below does not
use an unproved bound for the third derivative of \(s_g\).


## 3. Product domination without \(\exp(10B)\)

The exact M3 factorization is
\[
 z_n=z_0\,r^n\,T_n(a,b)\,\Pi_{e,n},\qquad
 \Pi_{e,n}=\prod_{j=0}^{n-1}R_e(je), \tag{10}
\]
where \(a=s_g/e\), \(b=s_h/e\), and \(T_n\) is the Gamma factor.  By (8),
\[
 \boxed{0<\Pi_{e,n}\le1.} \tag{11}
\]
The old absolute product bound
\(\Pi_{e,n}\le\exp(10B)\) is replaced by (11).

The accepted real Gamma bound gives, for \(p=19/25\), \(a\ge200\), and
\(|x_n-s_g|<\rho\) with \(\rho+e\le s_g/2\),
\[
 |T_n|\le1000\,(e+|x_n-s_g|)^{-p},
 \qquad x_n=ne. \tag{12}
\]
The M5 kernel bound \(|z_0|<10\) and (11) therefore give
\[
 |z_n|\le10^4\,(e+|x_n-s_g|)^{-p}. \tag{13}
\]
Summing the two sides of the crossing, as in the accepted Gamma estimate,
yields
\[
 e\sum_{|x_n-s_g|<\rho}|z_n|
 \le1.2\cdot10^5\,(\rho+e)^{6/25}. \tag{14}
\]
There is no exponential product constant in (13) or (14).

The same sign bound also improves the tail.  For \(x_n\ge4\), the post-side
Gamma formula gives
\[
 |T_n|\le20\left(\frac{a}{n-a}\right)^{\eta_e}<20,
\]
because \(s_g<.17\) and \(n-a=(x_n-s_g)/e>(4-.17)/e\).  Since the accepted
real kernel estimate gives \(0<r\le e^{-e}\),
\[
 |z_n|\le200e^{-x_n},\qquad x_n\ge4. \tag{15}
\]
Consequently, for \(S\ge4\),
\[
 e\sum_{x_n\ge S}|z_n|
 \le\frac{200e\,e^{-S}}{1-e^{-e}}
 \le400e^{-S}, \tag{16}
\]
using \(1-e^{-e}\ge e/2\).  This replaces the \(A^2e^{-(S-4)}\) tail
in the M5 ledger by a fixed numerical constant.

## 4. The Taylor error is additive, not exponential

The accepted M5 kernel proof actually supplies the smaller common real
constant
\[
 B_{\rm real}=10^{42}. \tag{17}
\]
Indeed, on the crossing strip its Taylor remainder is
\(40e/r_e^2=4\cdot10^{41}e\) with \(r_e=10^{-20}\); the exterior
log-ratio remainder is \(10^{40}e\).  The corresponding Hölder bounds for
\(\psi\) are below \(10^{32}\) in the strip and \(10^{10}\) outside it.
The two cut points only multiply this by \(\sqrt3<2\).  Thus the M5
convenience envelope \(10^{50}\) can be replaced by \(B_{\rm real}\) in
the real estimates below, without changing any M5 source.

Retain the accepted real M5 estimates
\[
 \left|\frac{\ell_e(s)}e-\psi(s)\right|\le B_{\rm real} e,\qquad
 |\psi(s)-\psi(r)|\le B_{\rm real}|s-r|^{1/2}. \tag{18}
\]
They are used here only to quantify the residual approximation, not to
dominate the product.

Let
\[
 \Psi_0(x)=\int_0^x\psi(y)\,dy.
\]
For \(x_n=ne\le S\), summing the first estimate in (18) and comparing the
second by one-cell integration gives
\[
 \left|\log\Pi_{e,n}-\Psi_0(x_n)\right|
 \le B_{\rm real} S(e+\sqrt e). \tag{19}
\]
Both logarithms in (19) are nonpositive by (8) and (9).  Hence the elementary
one-sided exponential Lipschitz inequality
\[
 |e^A-e^B|\le|A-B|\qquad(A\le0,\ B\le0) \tag{20}
\]
gives the direct product error
\[
 \boxed{
 |\Pi_{e,n}-e^{\Psi_0(x_n)}|
 \le B_{\rm real} S(e+\sqrt e),\qquad x_n\le S.
 } \tag{21}
\]
The right side of (21) is not exponentiated.

For the scale \(S=L+4\), \(L=\log(1/e)\), and \(L\ge1000\),
\[
 \log(L+4)\le L/100,\qquad 42\log10<97,
\]
 so
\[
 B_{\rm real} S\sqrt e
 \le\exp\!\left(97+\frac L{100}-\frac L2\right)
 \le e^{-393}, \tag{22}
\]
 and \(B_{\rm real}Se\le e^{-903}\).  Thus the retained \(10^{42}\) constant is already
harmless at \(L=1000\) once (8) is used.  In particular, a smaller
real Taylor constant is useful for optimization but is not needed to remove
the astronomical product domination.

## 5. Quantified route to the moment bound

The effective weight note gives \(|V_{j,e}|,|V_{j,0}|<40\) and
\(Q/e<1\).  Combining these with (14), the regularized crossing contribution
to either moment is at most
\[
 40\cdot1.2\cdot10^5\,(\rho+e)^{6/25}
 <5\cdot10^6(\rho+e)^{6/25}. \tag{23}
\]
The tail contribution after \(S\) is at most \(10^5e^{-S}\), by (16) and
the weight bound, after enlarging the constant.

Let
\[
 A_{\rm real}=10^{14}.
\]
This single ledger constant dominates the fixed real factors \(10^4\) in
(13), \(10^6\) in the boundary/scale-box check, \(2\cdot10^8\) for the
critical weighted mass, and the \(10^9\) center-moving factor in the
accepted Gamma note.  It is therefore enough for the absolute real
domination steps that previously used \(A=\exp(10^{54})\).

For comparison with the existing M5 error decomposition, set
\(\rho=e^{1/4}\), \(S=4+L\).  Substituting the additive product estimate
(21), the accepted Gamma/weight errors, and (23) gives the conservative
conditional ledger
\[
\begin{aligned}
 |P_N-P_0|+|H_N-H_0|
 \le 10^{120}\bigl[&
 B_{\rm real} S(e+\sqrt e)
 +e/\rho
 +(1+S)\sqrt e\,\rho^{-1-\eta}\\
 &+e\bigl(|\log\rho|+\log(2+S)\bigr)
 +(\rho+e)^{6/25}
 +e^{-(S-4)}\bigr]. \tag{24}
\end{aligned}
\]
The coefficient \(10^{120}\) is deliberately larger than
\(A_{\rm real}^4=10^{56}\) and the existing \(10^{60}\) relative-error
coefficient; it is a transparent replacement for the former
\(\exp(10^{60})\)-scale ledger.  Equation (24) is an aggregation route
conditional on the parent-owned Gamma transfer and phase estimates; it is
not a new claim about the final W theorem.

Since \(\eta<.71\), the powers in (24) satisfy
\[
 (\rho+e)^{6/25}\le2^{6/25}e^{3/50},\qquad
 (1+S)\sqrt e\,\rho^{-1-\eta}
 \le(L+5)e^{-0.0725L}. \tag{25}
\]
The other terms decay at rates at least \(e^{-0.75L}\), apart from the
signed-product term, which is bounded by (22).  At \(L\ge10^4\),
\[
 10^{120}\,2^{6/25}e^{-0.06L}<e^{-320},
\]
and the remaining terms are smaller.  Thus the moment part of the M5
ledger is already below \(e^{-300}\) at \(L=10^4\), subject to the
parent-owned transfer and endpoint inputs.  Since \(e_N<1/N\), the
illustrative moment threshold \(N\ge2^{15000}\) forces
\(\log(1/e_N)>10^4\).  This is a route-level bound, not the final N0:
the directed transfer and the endpoint sign margin remain owned by the
root.

The key reduction is structural.  The former \(\exp(10B)\) factor is
replaced by \(1\) in every absolute product and tail estimate; the \(B\)
term remains only in (21), where it is multiplied by \(S\sqrt e\) and
never exponentiated.

## Scope and checks

The argument is entirely real and uses the physical branch.  It handles the
removable \(g\)- and \(h\)-zeros through divided differences and does not
assume a lower bound on a raw denominator.  It uses no \(N=1024\) value and
does not modify any M5 source.  A future sharper threshold can reduce the
\(10^{120}\) aggregation coefficient by replacing \(B_{\rm real}\) in
(18) with a direct real Taylor box; that optimization is separate from the
sign reduction proved here.
