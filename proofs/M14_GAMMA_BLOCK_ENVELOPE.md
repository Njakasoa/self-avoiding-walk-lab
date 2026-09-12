# M14 normalized Gamma-primitive envelope

Status: **uniform analytic block-envelope lemma; no endpoint-sign claim**.
This note gives exact interval endpoints for the normalized primitive at
every integer \(N\ge32\) and every \(\theta\in[4/5,9/10]\).  It is meant
to supply the Gamma part of a future block-mass enclosure.  It uses no
index scan, interpolation in \(N\), or numerical endpoint sign.

The rational domain ledger is
proofs/m14_gamma_block_bounds.py.  It checks the constants used below.

## 1. Exact products and the normalized primitive

Put

\[
 e=e_N(\theta)>0,\qquad
 a=N+\theta,\qquad b=a-\beta,\qquad
 \alpha=1-\beta,\qquad A=b+1=a+\alpha,
\]

\[
 s=ae=s_g(e),\qquad x_n=ne,\qquad
 T_n=\prod_{j=0}^{n-1}\frac{a-j}{b-j}.
\tag{1}
\]

The reviewed real phase boxes give

\[
 \frac7{10}<\beta<\frac{18}{25},\qquad
 \frac7{25}<\alpha<\frac3{10},\qquad
 \frac3{20}<s<\frac{17}{100},\qquad
 0<e<\frac{17}{100N}.
\tag{2}
\]

For the exact primitive define

\[
 Q_n=\frac{(n-a)T_n}{\alpha},\qquad
 Q_{-1}=-\frac{b+1}{\alpha}.
\tag{3}
\]

Direct substitution, including the \(n=0\) step, gives

\[
 Q_n-Q_{n-1}=T_n>0,\qquad n\ge0.
\tag{4}
\]

Consequently the normalized block mass is exactly

\[
 e\sum_{n=\ell}^{r}T_n=eQ_r-eQ_{\ell-1}.
\tag{5}
\]

The special left endpoint when \(\ell=0\) is retained as
\(eQ_{-1}=-eA/\alpha\); it is not replaced by a fictitious \(T_{-1}\).

## 2. Gamma forms and a shifted Wendel inequality

For \(0\le n\le N\), let \(y=a-n\).  Then
\(y\ge\theta>\beta\), and

\[
 T_n=\frac{\Gamma(A+\beta)}{\Gamma(A)}
      \frac{\Gamma(y+\alpha)}{\Gamma(y+1)}.
\tag{6}
\]

For \(n\ge N+1\), let \(y=n-a>0\), and set

\[
 C_\theta=\frac{\sin(\pi\theta)}
                 {\sin(\pi(\theta-\beta))}>0.
\]

Reflection gives

\[
 T_n=C_\theta\frac{\Gamma(A+\beta)}{\Gamma(A)}
      \frac{\Gamma(y)}{\Gamma(y+\beta)}.
\tag{7}
\]

The ordinary Wendel inequality, for \(0<\gamma<1\), is

\[
 x^\gamma\left(\frac{x}{x+\gamma}\right)^{1-\gamma}
 \le \frac{\Gamma(x+\gamma)}{\Gamma(x)}
 \le x^\gamma.
\tag{8}
\]

We need the following shifted form with \(\gamma=\alpha=1-\beta\):

\[
 (z-\beta)^\alpha
 \le\frac{\Gamma(z+\alpha)}{\Gamma(z)}
 \le z^\alpha,\qquad z>\beta.
\tag{9}
\]

The upper inequality is (8).  For the lower one, (8) gives

\[
 \frac{\Gamma(z+\alpha)}{\Gamma(z)}
 \ge z^\alpha\left(\frac{z}{z+\alpha}\right)^\beta.
\]

Concavity of \(\log\), applied with weights \(\alpha,\beta\), gives

\[
 \alpha\log\left(1-\frac{\beta}{z}\right)
 +\beta\log\left(1+\frac{\alpha}{z}\right)
 \le
 \log\left(\alpha\left(1-\frac{\beta}{z}\right)
 +\beta\left(1+\frac{\alpha}{z}\right)\right)=0.
\]

This is exactly the lower inequality in (9).  Its hypotheses hold for
both sides of the crossing: use \(z=y>\beta\) in (6), and
\(z=y+\beta>\beta\) in (7).

## 3. A single shifted CDF envelope for every index

Define

\[
 {\cal A}_e
   =e^\beta\frac{\Gamma(A+\beta)}{\Gamma(A)}
\tag{10}
\]

and the increasing, piecewise power function

\[
 \overline Q_e(x)=\frac{{\cal A}_e}{\alpha}
 \begin{cases}
 -(s-x)^\alpha,&0\le x<s,\\[2mm]
 C_\theta(x-s)^\alpha,&x>s,\\
 0,&x=s.
 \end{cases}
\tag{11}
\]

Multiplying (9) by the signs in (6)--(7) gives the key enclosure

\[
 \boxed{\quad
 \overline Q_e(ne)\ \le\ eQ_n\ \le\
 \overline Q_e((n+\beta)e),\qquad n\ge0.
 \quad}
\tag{12}
\]

For example, before the crossing,

\[
 eQ_n=-\frac{e}{\alpha}
 \frac{\Gamma(A+\beta)}{\Gamma(A)}
 \frac{\Gamma(y+\alpha)}{\Gamma(y)},
\]

while the two endpoints in (12) are obtained by replacing \(y^\alpha\)
with \(y^\alpha\) and \((y-\beta)^\alpha\), respectively.  After the
crossing, (7) and \(z=y+\beta\) give the two endpoints \(y^\alpha\) and
\((y+\beta)^\alpha\).  This verifies that the same formula passes through
the pre/crossing/post split without discarding the singular cell.

The function in (11) is increasing.  Hence for every block
\(1\le\ell\le r\),

\[
 \boxed{\quad
 \overline Q_e(re)-\overline Q_e((\ell-1+\beta)e)
 \le e\sum_{n=\ell}^{r}T_n
 \le
 \overline Q_e((r+\beta)e)-\overline Q_e((\ell-1)e).
 \quad}
\tag{13}
\]

For a block starting at zero, define the small endpoint offset

\[
 h_{0,e}=\frac{eA}{\alpha}+\overline Q_e(0).
\tag{14a}
\]

The same Wendel bound, now applied with \(x=a+\alpha\), gives the
sharper coefficient interval

\[
 a^\beta\le
 \frac{\Gamma(a+1)}{\Gamma(a+\alpha)}
 \le(a+\alpha)^\beta.
\tag{14b}
\]

Indeed, the upper endpoint is Wendel, and its lower endpoint is
Wendel's lower bound followed by weighted AM--GM:
\[
 (a+\alpha)^\beta
 \left(\frac{a+\alpha}{a+1}\right)^\alpha
 =\frac{a+\alpha}{(a+1)^\alpha}
 \le\frac{\Gamma(a+1)}{\Gamma(a+\alpha)}
 \le(a+\alpha)^\beta
\]
with the first displayed \(a^\beta\) lower bound obtained from
\(a+\alpha=\alpha(a+1)+\beta a\).  In particular,

\[
 s^\beta\le{\cal A}_e\le(s+\alpha e)^\beta.
\tag{14c}
\]

Extend the pre-side derivative of (11) to \(x\le0\) by
\(\overline G_e(x)={\cal A}_e(s-x)^{-\beta}\).  Direct integration and
(14b) give

\[
 \int_{-\alpha e}^{0}\overline G_e(x)\,dx
 \le h_{0,e}\le
 \int_{-e}^{0}\overline G_e(x)\,dx.
\tag{14d}
\]

Thus \(h_{0,e}>0\).  A mean-value bound in the right integral, together
with (14c), gives for \(N\ge512\)

\[
 0<h_{0,e}
 \le e\left(1+\frac{\alpha e}{s}\right)^\beta
 <\frac{1001}{1000}e.
\tag{14e}
\]

The exact zero-start block interval is therefore

\[
 h_{0,e}+\overline Q_e(re)-\overline Q_e(0)
 \le e\sum_{n=0}^{r}T_n
 \le
 h_{0,e}+\overline Q_e((r+\beta)e)-\overline Q_e(0),
\tag{14f}
\]

where \(h_{0,e}\) itself is enclosed by (14d).  This is the normalized
CDF constant needed by an integral comparison; it is an \(O(e)\) endpoint
offset and is kept rather than silently absorbed into a floor error.

These are interval enclosures, not asymptotic equalities.  In particular,
they preserve positivity of every block mass even when a block contains
the crossing.

## 4. Uniform constants and floor control

The domain ledger gives

\[
 a\ge\frac{164}{5},\qquad
 A\ge\frac{827}{25},\qquad
 y_{\rm pre}\ge\frac45,\qquad
 y_{\rm post}\ge\frac1{10}.
\tag{15}
\]

For comparison with a coarser implementation, put
\[
 W_-(x,\beta)=x^\beta\left(\frac{x}{x+\beta}\right)^{1-\beta},
 \qquad W_+(x,\beta)=x^\beta.
\]
The rational checks

\[
 \frac{x}{x+\beta}\ge\frac5{41},\qquad
 \left(\frac5{41}\right)^3>\left(\frac12\right)^{10},
\]

imply \(W_-(x,\beta)>\frac12x^\beta\) for every post-crossing
argument, while \(W_-(A,\beta)>\frac9{10}A^\beta\).  Thus

\[
 \frac9{10}\left(\frac{A}{x}\right)^\beta<T_n
 <2\left(\frac{A}{x}\right)^\beta
\tag{16}
\]

with \(x=y+\alpha\) before the crossing and \(x=y\) after it.
Use the same bounds with the extra factor
\(C_\theta\) after it.  Indeed, on the phase band
\(v=\theta-\beta\ge2/25\) and \(v<1/5\), so
\(\sin(\pi v)\ge2v\) and \(C_\theta\le1/(2v)<25/4\).  Here
\[
 C_\theta<\frac{25}{4},\qquad eA=s+\alpha e<\frac9{50}.
\tag{17}
\]

The shifted envelope is substantially sharper near the crossing.  From
(10), (17), and \(\alpha\ge7/25\),

\[
 0<{\cal A}_e<1,\qquad
 \frac{{\cal A}_e}{\alpha}\le\frac{25}{7},\qquad
 \frac{{\cal A}_eC_\theta}{\alpha}\le\frac{625}{28}.
\tag{18}
\]

For \(0<\gamma<1\), the map \(u\mapsto u^\gamma\) is
\(\gamma\)-Holder on the nonnegative line:
\[
 |u^\gamma-v^\gamma|\le|u-v|^\gamma.
\]
Using (18) on the two sides of the cusp and
\(\alpha\ge7/25\), \(0\le h\le1\), gives the global translation bound

\[
 \left|\overline Q_e(x+h)-\overline Q_e(x)\right|
 \le\frac{725}{28}|h|^{7/25}
 \le26|h|^{7/25}.
\tag{19}
\]

Consequently the pointwise floor interval (12) has width at most
\(26e^{7/25}\).  If the interval \([x,x+\beta e]\) stays on one side of
\(s\), and its distance from \(s\) is at least \(\rho/2\), with \(0<\rho\le1\), then
differentiating (11) gives the sharper

\[
 \left|\overline Q_e(x+\beta e)-\overline Q_e(x)\right|
 <9e\,\rho^{-18/25}.
\tag{20}
\]

The hypothesis for (20) is explicit: the starting distance must be at
least \(\rho\), and the center/shift margins must leave distance
\(\rho/2\) along the segment.  When a segment meets the cusp, use (19)
instead.  This is the required finite-\(N\) handling of floors; no
assumption that a floor is stable as \(N\) varies is made.

For a real block \([u,v]\), take
\(\ell=\lceil u/e\rceil\) and \(r=\lfloor v/e\rfloor\), assuming the
block is nonempty and \(\ell\ge1\).  The four arguments in (13) differ
from \(u\) or \(v\) by at most one mesh step:
\[
 (\ell-1)e\in(u-e,u],\quad
 (\ell-1+\beta)e\in(u-e,u+\beta e],
\]
\[
 re\in(v-e,v],\quad
 (r+\beta)e\in(v-e,v+\beta e].
\tag{21}
\]
Equations (13), (19), and (20) therefore enclose every floor-dependent
block with exact endpoint formulas and an explicit cusp allowance.  If
\(\ell=0\), use the separate exact endpoint formula (14).

## 5. Convergence to the critical CDF

Let

\[
 \eta=\frac1{\sqrt2},\qquad
 s_\star=s_g(0)
   =-\log\left(\frac12+\frac{\sqrt2}{4}\right),\qquad
 \alpha_\star=1-\eta,
\]

\[
 C_{\theta,\star}
 =\frac{\sin(\pi\theta)}{\sin(\pi(\theta-\eta))},
\]

and define the critical primitive

\[
 \overline Q_\star(x)=\frac{s_\star^\eta}{\alpha_\star}
 \begin{cases}
 -(s_\star-x)^{\alpha_\star},&x<s_\star,\\[2mm]
 C_{\theta,\star}(x-s_\star)^{\alpha_\star},&x>s_\star,\\
 0,&x=s_\star.
 \end{cases}
\tag{22}
\]

The reviewed real phase bounds supply
\[
 |s-s_\star|<\frac25e,\qquad
 0<\beta-\eta<\frac{69}{500}e^2,
\tag{23}
\]
throughout the present physical range.  The second inequality is the
sharp M10 beta estimate, while the first follows from the reviewed
\(.3<s_g'<.4\) phase box and the real mean-value theorem.  The older
linear \(300000e\) allowance is not used here.

For completeness, the coefficient in (10) has a direct finite-\(N\)
logarithmic bound.  Wendel gives

\[
 \log{\cal A}_e
 =\beta\log(eA)+\delta_A,\qquad
 -\frac{\beta}{A}\le\delta_A\le0.
\]

Since \(eA=s+\alpha e\), (2), (23), and
\(3/20<s_\star<17/100\) imply
\[
 |eA-s_\star|<\frac7{10}e,\qquad
 \left|\log\frac{eA}{s_\star}\right|<\frac{28}{3}e,
 \qquad |\delta_A|<\frac{24}{5}e.
\]
Using \(|\log s_\star|<2\) (the elementary bound
\(e^{-2}<3/20<s_\star<1\)) and \(e\le1/180\), this yields

\[
 \boxed{\quad
 \left|\log\frac{{\cal A}_e}{s_\star^\eta}\right|<12e.
 \quad}
\tag{24}
\]

For the normalization, \(|\log(\alpha_\star/\alpha)|
\le(25/7)|\beta-\eta|\).  On the phase band both
\(\theta-\beta\) and \(\theta-\eta\) lie in \([2/25,1/5]\), and

\[
 \left|\frac{d}{dv}\log\sin(\pi v)\right|
 =\pi|\cot(\pi v)|
 \le\frac{\pi}{2v}<20.
\]

Thus the sine-factor logarithmic error is at most
\(20|\beta-\eta|\) on the post-crossing side.

Fix \(S>0\), \(0<\rho\le1\), and a point \(x\in[0,S]\) with
\(|x-s_\star|\ge\rho\) and \(|s-s_\star|\le\rho/2\).  If \(x\) is on
the pre side, or on the post side respectively, the same-side profile
comparison gives

\[
 \left|\log\frac{\overline Q_e(x)}
                  {\overline Q_\star(x)}\right|
 \le E_{\rm par}(S,\rho),
\tag{25}
\]

where

\[
 E_{\rm par}(S,\rho)
 =12e+
 \left(\frac{25}{7}+2+\log(2+S)+|\log\rho|
       +20\,{\bf1}_{\{x>s_\star\}}\right)|\beta-\eta|
 +\frac{3}{5\rho}|s-s_\star|.
\tag{26}
\]

The \(2+\log(2+S)+|\log\rho|\) term bounds the exponent's logarithm;
the last term is the distance-center perturbation.  If
\(E_{\rm par}\le1/4\), the corresponding relative error is at most
\(4E_{\rm par}/3\).  Combining (19), (20), and (25) gives an explicit
enclosure of \(eQ_n\) around the critical CDF at every mesh point:
use (20) away from the cusp and (19) in the cusp cell.  In particular,
for any fixed \(\rho>0\), the away-cell error is \(O(e)\), while a block
whose two primitive endpoints lie within \(\rho+e\) of the cusp has
mass at most \(26(\rho+e)^{7/25}\) by (18).  Letting first \(e\to0\) and
then \(\rho\to0\) gives convergence of the block primitive to (22), with
all floor shifts retained.

## 6. Scope and remaining work

The exact shifted Wendel sandwich (12)--(14) is valid for every integer
\(N\ge32\), every \(\theta\in[4/5,9/10]\), and every finite block.  It is
the usable input for a finite partition or an integral comparison of the
positive weighted masses.  It does not bound the \(K_n\), \(L_W(u_n)\),
or boundary factors, and it does not establish either endpoint sign.
Any endpoint conclusion requires independent enclosures for those factors
and for the boundary term.  This note supplies only the Gamma primitive
and its exact pre/crossing/post and floor control.

Reproduction:

    python3 -m proofs.m14_gamma_block_bounds

The checker returns status=pass and the classification
EXACT RATIONAL WENDEL DOMAIN AND NORMALIZED-PRIMITIVE BOUNDS; NO ENDPOINT
SIGN CLAIM.  It writes no repository output.
