# M11: an endpoint-safe smooth-product phase bound

Status: analytic candidate for independent review.  On the real domain
\(N\ge32\), \(\theta\in[.8,.9]\), and \(n\le60N\), this note proves
\[
 \left|\partial_\theta\log K_{e,n}\right|<\frac{112.2}{N},
 \qquad
 K_{e,n}=r^n\Pi_{e,n},
 \tag{1}
\]
where the nonsingular product is
\(\Pi_{e,n}=\prod_{j<n}R_e(je)\).  The proof avoids differentiating the
square-root kernel at its critical endpoint by factoring each \(R_e\)
through the inverse kernel.  It does not assert a sign for \(F_N\).

The phase and signed scalar inputs are
\[
 0<e<\frac{.17}{N}<\frac1{180},\qquad
 |e_\theta|<\frac eN,\qquad
 .3<s_g'(e)<.4,                                           \tag{2}
\]
where the last inequality is checked on the complete signed
\(e\)-box \([-1/180,1/180]\) by
proofs/m11_smooth_phase_bounds.py.  The M5 real root bounds on
\(e\le.01\), together with the implicit equation for \(t\), give
\[
 .414<t<.4143,\quad q=e^{-e/2},\quad
 -\frac e7<t_e<0,\quad q_e=-\frac q2.                     \tag{3}
\]
Only these real bounds are used at \(N=32\); no small-\(e\) complex estimate
is extrapolated.

## 1. Inverse-kernel factorization

For \(u=U(t,v)\), direct rearrangement of the inverse kernel equation gives
\[
 v=v_t(u):=
 \frac{(u-t)(1-tu)}{t(1-t^2)u}.                           \tag{4}
\]
For any \(a,u>0\),
\[
 v_t(a)-v_t(u)
 =\frac{(a-u)(1-au)}{(1-t^2)au}.                          \tag{5}
\]
Let
\[
 D=1-tq,\quad C=q-t,\quad
 u_g=\frac tD,\quad h=u_h=\frac{tq}{C}.
\]
The two recurrence zeros satisfy \(g_e(s_g)=0\), \(g_e(s_h)+\delta=0\),
and hence
\[
 g_e(s)=D(u_g-u),\qquad
 g_e(s)+\delta=D(h-u),\qquad u=U(t,e^{-s}).                \tag{6}
\]
Define the positive exponential secant
\[
 M(s,a)=\int_0^1
 \exp\!\bigl(-[(1-v)s+va]\bigr)\,dv
 =\frac{e^{-a}-e^{-s}}{s-a},                              \tag{7}
\]
with its continuous value at \(s=a\).  Thus
\[
 e^{-a}-e^{-s}=(s-a)M(s,a).                               \tag{8}
\]
Applying (5) first with \(a=h\), then with \(a=u_g\), and using (8), gives
\[
\begin{aligned}
 R_e(s)
 &=\frac{g_e(s)/(s-s_g)}
         {(g_e(s)+\delta)/(s-s_h)}\\
 &=\frac{u_g-u}{h-u}\frac{s-s_h}{s-s_g}\\
 &=\frac{u_g}{h}\,
   \frac{1-uh}{1-u u_g}\,
   \frac{M(s,s_g)}{M(s,s_h)}.                             \tag{9}
\end{aligned}
\]
The orientation in the last ratio follows from
\[
\frac{e^{-s_h}-e^{-s}}{e^{-s_g}-e^{-s}}
 =\frac{s-s_h}{s-s_g}\frac{M(s,s_h)}{M(s,s_g)}.
\]
All factors in (9) are positive on the physical ray.  The identity extends
through \(s=s_g,s_h\) by the divided-difference limits.
For the present larger real domain, M5 gives \(s_g>.15\), while
\(s_h=s_g-\beta e>.15-.72/180>0\).  The M6 positive-series proof that
\(g_e\) is increasing and concave holds for every \(0<t<\sigma\), so this
extension uses no small-\(e\) Taylor estimate.

The signed scalar checker gives
\[
 .70<u_g<.71,\qquad .70<h<.71,\qquad
 -.26<u_{g,e}<0<h_e<.26,                                \tag{10}
\]
where the \(h\)-boxes use the exact symmetry
\[
 t(-e)=t(e),\quad q(-e)=q(e)^{-1},\quad h(e)=u_g(-e).
 \tag{11}
\]
Also, for \(e>0\),
\[
 h-u_g=\frac{t^2(1-q^2)}{CD}<.51e.                       \tag{12}
\]
The last inequality uses \(1-q^2=1-e^{-e}<e\) and the checked rational
box \(t^2/(CD)<.51\).  The same symmetry gives
\[
 s_h(e)=s_g(-e),\qquad |s_{g,e}|+|s_{h,e}|<.8.             \tag{13}
\]

## 2. Direct motion bound for the kernel mesh

This section derives the mesh motion independently of any upper bound on
\(u_{n,\theta}\).  Put
\[
 x=je,\qquad v=e^{-x},\qquad
 B=t^{-1}+t-(1-t^2)v,\qquad
 \Delta=B^2-4.
\]
Then
\[
 U(t,v)=\frac2{B+\sqrt\Delta},\quad
 U_t=\frac{U(t^{-2}-1-2tv)}{\sqrt\Delta},\quad
 U_v=\frac{U(1-t^2)}{\sqrt\Delta}.                        \tag{14}
\]
Since \(B(t,1)=2\cosh(e/2)\), \(1-t^2>3/4\), and
\(2\cosh(e/2)-2\ge e^2/4\),
\[
 B-2\ge\frac{e^2}{4}+(1-t^2)(1-v),\qquad
 \sqrt\Delta\ge\sqrt{e^2+3(1-v)}.                        \tag{15}
\]
The implicit equation for \(t\) gives
\[
 -t_e=\frac{\sinh(e/2)}{|{-t^{-2}+1+2t}|}<\frac e7.       \tag{16}
\]
At fixed integer \(j\),
\[
 u_{j,e}=U_t t_e-U_v\,jv<0.                              \tag{17}
\]
Use \(U<1\), \(t^{-2}<6\), \(xv\le1-v\), and (15):
\[
\begin{aligned}
 e|u_{j,e}|
 &\le\frac{6e^2}{7\sqrt\Delta}
       +\frac{xv}{\sqrt\Delta}\\
 &\le\frac{6e}{7}+\sqrt{\frac{1-v}{3}}
 <\frac{6}{7\cdot180}+\frac35
 =\frac{127}{210}<.61.                                  \tag{18}
\end{aligned}
\]
Here \(xv\le1-v\) is \(x\le e^x-1\), and
\(1/\sqrt3<3/5\).  This includes \(j=0\): the second term vanishes,
while \(e>0\) makes the first derivative finite.

## 3. Derivative of one nonsingular factor

Write the two non-exponential factors in (9) as
\[
 A(u,e)=\log(1-uh)-\log(1-u u_g),\qquad
 m(s,e)=\log M(s,s_g)-\log M(s,s_h).                      \tag{19}
\]
Since \(0\le u<1\) and (10) holds, both denominators in \(A\) exceed
\(.29\).  At fixed \(u\),
\[
 |A_e|
 \le\frac{|h_e|+|u_{g,e}|}{.29}
 <\frac{.52}{.29}<1.8,                                  \tag{20}
\]
while the cancellation in the \(u\)-derivative gives
\[
 A_u=\frac{u_g-h}{(1-uh)(1-u u_g)},\qquad
 |A_u u_{j,e}|
 <\frac{.51e}{.29^2}\frac{.61}{e}
 =\frac{3111}{841}<3.721.                                \tag{21}
\]
The scalar ratio in (9) has
\[
 \left|\partial_e\log\frac{u_g}{h}\right|
 <\frac{.26}{.70}+\frac{.26}{.70}
 =\frac{26}{35}<.75.                                    \tag{22}
\]

For \(M\), use the probability density proportional to the integrand in
(7) on \(0\le v\le1\).  Then
\[
 \partial_a\log M=-\mathbb E[v]\in[-1,0],\qquad
 \partial_{sa}\log M=-\operatorname{Var}(v),\qquad
 |\partial_{sa}\log M|\le\frac14.                       \tag{23}
\]
Consequently, along the mesh \(s=je\),
\[
 \left|\frac d{de}m(je,e)\right|
 \le |s_{g,e}|+|s_{h,e}|
    +\frac14j|s_g-s_h|
 <.8+.18\,je.                                            \tag{24}
\]
Since \(j<n\le60N\) and \(e<.17/N\), \(je<10.2\), so the last
two terms in (24) are bounded by
\[
 .8+1.836.                                                \tag{25}
\]
Combining (20)--(25) with (18) yields, for every
\(0\le j<n\le60N\) in the stated domain,
\[
 \left|\frac d{de}\log R_e(je)\right|
 <.75+1.8+3.721+.8+1.836
 =\frac{8907}{1000}<9.                              \tag{26}
\]
This is an endpoint-safe bound; no derivative of a raw square root at
the critical \(e=0,s=0\) point is used.

## 4. Product and post-crossing consequence

Summing (26) and applying (2),
\[
 |\partial_\theta\log\Pi_{e,n}|
 <\frac{e}{N}\,9n
 <\frac{91.8}{N}.                                       \tag{27}
\]
For the physical \(e>0\) branch, \(q\le1\) and
\(e/7\le1/(7\cdot180)<1/400\).  The scalar geometric factor has the
independent real bound
\[
 |(\log r)_e|<2,\qquad
 |\partial_\theta\log r^n|
 <\frac{20.4}{N},                                      \tag{28}
\]
from \(C>.57,D>.58,-1/400<t_e<0,q_e=-q/2\), with the exact rational
guard
\[
 \frac12+
 \frac{\frac12+\frac1{400}}{57/100}
 \frac{\frac1{400}+\frac{83}{400}}{58/100}<2.
\]
Therefore
\[
 \boxed{\ |\partial_\theta\log K_{e,n}|<
 \frac{91.8+20.4}{N}=\frac{112.2}{N}.\ }                 \tag{29}
\]

For the positive post-crossing summand, use the separately reviewed
M11 weight input
\[
 \partial_\theta\log[A_0L_W(u_n)]<\frac{11}{N},
\qquad A_0=Q(-z_0)>0,\quad L_W(u_n)>0.
 \tag{30}
\]
Together with the M10 bare-product bound and \(N+1\le n\le60N\),
\[
\begin{aligned}
 \partial_\theta\log[A_0T_nK_{e,n}L_W(u_n)]
 &<-\frac{1435}{342}+\frac{112.2+11}{N}\\
 &\le-\frac{1435}{342}+\frac{123.2}{32}\\
 &=-\frac{1183}{3420}<-.345.                            \tag{31}
\end{aligned}
\]
Equation (31) is a componentwise post-crossing result.  It does not cover
the pre-crossing sum, the boundary terms, the distant tail, or the full
phase function \(F_N\).

## Checker and provenance

Run without optimization:

    python3 -m proofs.m11_smooth_phase_bounds > /tmp/m11-smooth-phase-bounds.json

The checker returns status: pass, verifies the signed I384 boxes in
(10), and replays every remaining numerical inequality with exact
Fractions.  Its direct \(h=tq/C\) interval is retained only as a
diagnostic; the sharp \(h\)-box in (10) is transferred by the exact
symmetry (11).  No numerical phase scan or held-out index is used.

The note is conditional only on the separately reviewed weight estimate
(30) for the final margin (31).  The smooth-product bound (29) itself is
independent of that input.  The directed phase candidate is also a separate
input to the W weight estimate; it is not used in the derivation of (29).

Source snapshot and input hashes:

| input | SHA-256 |
|---|---|
| proofs/M11_WEIGHT_PHASE_BOUND.md | e6fa7bbec97ed9caeb3785850728aeef64b20af610f70d3234a5e38398f06ca6 |
| proofs/M11_DIRECTED_PHASE_BOUND.md | efe6b4c4a57e502cb4ff9b04835aaed556463c83d7cbc5e0d86cf73b687ef08e |
| proofs/M10_BETA_REAL.md | 51b59ecaea7fa22647d76471f8ecef9e8483581fdd3941a02d56b0fb22397f80 |
| proofs/M10_BARE_PHASE_DERIVATIVE.md | 04605690a985a1c65a682354eab86c08480c17c46be39f243c86a020a094a265 |
| proofs/M6_EFFECTIVE_PRODUCT.md | a3b6b878102cfbe022aada6477c78c8641edc5d25b813ea7030f032fce96c522 |

The repository snapshot was
14b460244d7282fed8c8ef2bbc1edf5b09e8b92b.  The two new files are
uncommitted by design; their release hashes are supplied in the task report.
