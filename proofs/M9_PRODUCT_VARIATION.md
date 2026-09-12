# M9: finite variation of the critical residue factor

Status: **candidate proof for review**.  This note is a new M9 input only;
it does not modify the accepted M3--M7 sources and it does not claim a new
moment rate.  Its purpose is to replace the square-root mesh loss in the
smooth product by a bounded-variation estimate.

The inputs are the accepted real estimates in
M6_SHARP_KERNEL.md, M6_SHARP_KERNEL_REVIEW.md,
M6_EFFECTIVE_PRODUCT.md, and M6_ACCEPTANCE.md.  In particular, on the
accepted common real domain for \(e\),

\[
 |g_0(s)|>10^{-3}\quad(s\notin I),
 \qquad I=[1/10,1/4],\qquad s_*\in(3/20,17/100),                 \tag{1}
\]

and the real critical function is

\[
 \psi(s)=\frac{\eta}{s-s_*}-\frac{\kappa}{g_0(s)},
 \qquad
 \eta=\frac1{\sqrt2},\qquad
 \kappa=\frac{\sigma^2}{1-\sigma},\qquad \sigma=\sqrt2-1.   \tag{2}
\]

The value at \(s=s_*\) is the accepted removable value.  The accepted
positive-series/concavity argument also gives \(g_0'(s)>0\) for \(s>0\),
and the accepted sign statement gives

\[
 \psi(s)\le 0\qquad(s\ge0).                                  \tag{3}
\]

## 1. Explicit total variation of \(\psi\)

The endpoint \(s=0\) is allowed to have an unbounded derivative in the
square-root parametrization.  We therefore use monotonicity and an
improper integral at that endpoint, rather than assuming a derivative bound
there.

At the critical parameter, the kernel identities give

\[
 g_0(0)=\sigma-(1-\sigma)U(\sigma,1)=-\sigma^2,
 \qquad
 \lim_{s\to\infty}g_0(s)=\sigma-(1-\sigma)U(\sigma,0)=\sigma^2. \tag{4}
\]

Here \(U(\sigma,1)=1\) and \(U(\sigma,0)=\sigma\) are the two endpoint
values of the physical branch.  Since \(g_0\) is increasing and its unique
zero lies in \(I\), it is negative on \([0,1/10]\) and positive on
\([1/4,\infty)\).  For \(s>0\) away from the zero, differentiating (2)
gives

\[
 \psi'(s)=-\frac{\eta}{(s-s_*)^2}
              +\frac{\kappa g_0'(s)}{g_0(s)^2}.                 \tag{5}
\]

On the exterior \(E=[0,1/10]\cup[1/4,\infty)\), the first term in (5)
has the exact integral

\[
 \begin{aligned}
 V_\eta
 &:=\eta\int_E\frac{ds}{(s-s_*)^2}\\
 &=\eta\left(
       \frac1{s_*-1/10}-\frac1{s_*}+\frac1{1/4-s_*}
      \right)<14+13=27.                                  \tag{6}
 \end{aligned}
\]

Indeed,
\[
 \frac1{s_*-1/10}-\frac1{s_*}
 =\frac{1/10}{s_*(s_*-1/10)}<\frac{40}{3}<14,
 \qquad
 \frac1{1/4-s_*}<\frac{25}{2}<13,
\]
using (1) and \(\eta<1\).

For the \(g_0\)-term, use
\[
 \frac{d}{ds}\left(-\frac1{g_0(s)}\right)
 =\frac{g_0'(s)}{g_0(s)^2}.                                  \tag{7}
\]
Integrate first from \([\varepsilon,1/10]\) and then let
\(\varepsilon\downarrow0\); on the right component let the upper
endpoint tend to infinity.  Equations (1), (4), and \(g_0'(s)>0\) give

\[
 \begin{aligned}
 V_g
 &:=\kappa\int_E\frac{g_0'(s)}{g_0(s)^2}\,ds\\
 &\le \kappa\left(
       \frac1{|g_0(1/10)|}+\frac1{|g_0(0)|}
      +\frac1{g_0(1/4)}+\frac1{\lim_{s\to\infty}g_0(s)}
      \right)\\
 &< \kappa\,2\left(1000+\frac{25}{4}\right).                \tag{8}
 \end{aligned}
\]

The elementary rational bounds
\[
 \sigma>\frac25,\qquad \sigma<\frac{83}{200},\qquad
 \sigma^2>\frac4{25},\qquad \sigma^2<\frac9{50},\qquad
 1-\sigma>\frac{29}{50}
\]
imply
\[
 \kappa<\frac{9/50}{29/50}=\frac9{29},
 \qquad
 \frac1{\sigma^2}<\frac{25}{4}.                              \tag{9}
\]
Therefore
\[
 V_g<\frac9{29}\,2\left(1000+\frac{25}{4}\right)
      =\frac{36225}{58}<625.                                 \tag{10}
\]
The use of (7) is the reason no endpoint derivative estimate is needed.
It also proves convergence of the exterior variation at infinity.

On the middle interval \(I\), the accepted Cauchy estimate is

\[
 |\psi'(s)|<2\cdot10^{10}.                                    \tag{11}
\]

The removable value at \(s_*\) makes \(\psi\) continuous there, so the
interval variation is bounded by
\[
 V_I\le |I|\sup_I|\psi'|
      =\left(\frac14-\frac1{10}\right)2\cdot10^{10}
      =3\cdot10^9.                                            \tag{12}
\]

Combining (6), (10), and (12), with the exterior and middle pieces glued by
continuity,
\[
 \operatorname{TV}_{[0,\infty)}(\psi)
 < 3\cdot10^9+27+625
 < 3\cdot10^9+700
 < 4\cdot10^9.                                                 \tag{13}
\]

Thus \(\psi\) is of finite total variation on the complete half-line.  The
bound is explicit and uses only the accepted \(g_0\) separation, monotonicity,
endpoint values, and the accepted middle derivative estimate.

## 2. \(O(e)\) rectangle error for the smooth product

Use the M6 notation
\[
 \ell_e(s)=\log R_e(s),\qquad
 \Pi_{e,n}=\prod_{j=0}^{n-1}R_e(je),\qquad x_n=ne,
\]
and let
\[
 \Psi_0(x)=\int_0^x\psi(s)\,ds.                              \tag{14}
\]
Let \(B\ge10^{12}\) be the accepted M6 real envelope.  The accepted sharp
kernel estimate and the scalar \(r\)-estimate imply, uniformly for the
accepted real \(e\)-domain,
\[
 \left|\frac{\ell_e(s)}e-\psi(s)\right|\le Be,
 \qquad
 |\log r+\lambda e|\le Be^2,
 \qquad \lambda=\frac1{1-\sigma}.                            \tag{15}
\]
The second inequality is a harmless enlargement of the accepted sharper
bound \(|(-\log r)/e-\lambda|<10e\).

For every integer \(n\ge0\) and each \(j<n\), the first estimate in (15)
contributes at most \(Be^2\).
For the rectangle term, bounded variation gives the one-cell inequality
\[
 \left|e\psi(je)-\int_{je}^{(j+1)e}\psi(s)\,ds\right|
 \le e\,\operatorname{TV}_{[je,(j+1)e]}(\psi).                \tag{16}
\]
Summing (16) and the Taylor errors over \(0\le j<n\) yields the exact
logarithmic bound
\[
 \begin{aligned}
 \left|\log\Pi_{e,n}-\Psi_0(x_n)\right|
 &\le e\,\operatorname{TV}_{[0,\infty)}(\psi)+Be^2n\\
 &\le e\left(4\cdot10^9+Bx_n\right).                         \tag{17}
 \end{aligned}
\]

Define the smooth product including the scalar geometric factor by
\[
 K_{e,n}:=r^n\Pi_{e,n},
 \qquad
 K(x):=\exp\{-\lambda x+\Psi_0(x)\}.                         \tag{18}
\]
Both exponents are nonpositive: M6 gives \(0<R_e\le1\), \(r\le e^{-e}\),
and (3) gives \(\Psi_0\le0\).  More precisely, with
\[
 A_n=n\log r+\log\Pi_{e,n},\qquad
 A(x_n)=-\lambda x_n+\Psi_0(x_n),
\]
we have
\[
 A_n\le-x_n,\qquad A(x_n)\le-\lambda x_n\le-x_n.              \tag{19}
\]
The two logarithmic contributions in (15) and (17) therefore give
\[
 |A_n-A(x_n)|
 \le Be^2n+e(4\cdot10^9+Bx_n)
 \le e\left(4\cdot10^9+2Bx_n\right).                         \tag{20}
\]
Along the line segment between \(A_n\) and \(A(x_n)\), the exponential
derivative is at most \(e^{-x_n}\).  Hence
\[
 \boxed{
 |K_{e,n}-K(x_n)|
 \le e\left(4\cdot10^9+2Bx_n\right)e^{-x_n}.
 }                                                               \tag{21}
\]
Since \(B\ge10^{12}>4\cdot10^9\), this has the convenient envelope
\[
 \boxed{
 |K_{e,n}-K(x_n)|
 \le 3Be(1+x_n)e^{-x_n}.
 }                                                               \tag{22}
\]

This is the desired \(O(Be)\) mesh error with the damping factor retained.
It uses no derivative of a \(C^0\) moment remainder: only the explicit
critical function \(\psi\), its finite variation, and the already accepted
pointwise logarithmic estimate.  It is a product estimate only; no improved
rate for \(P_N\), \(H_N\), or the final residue is asserted here.

## 3. Arithmetic and provenance ledger

The numerical steps in the proof reduce to the following exact rational
checks:

\[
 \begin{gathered}
 \frac{1/10}{(3/20)(1/20)}=\frac{40}{3}<14,
 \qquad \frac1{1/4-17/100}=\frac{25}{2}<13,\\
 \frac9{29}\,2\left(1000+\frac{25}{4}\right)=\frac{36225}{58}<625,\\
 3\cdot10^9+27+625<3\cdot10^9+700<4\cdot10^9,\\
 4\cdot10^9<10^{12}=B.
 \end{gathered}                                                     \tag{23}
\]

The analytic inputs are exactly (1), (3), (4), (5), and (11), all cited to
the accepted M6 notes above.  The input snapshot is the accepted M6
revision a7fa96f668d44031928f820d9f31bd82d9db7efd; the relevant current
input hashes are:

| input | SHA-256 |
|---|---|
| proofs/M6_SHARP_KERNEL.md | 8717a3a191eb9f958f4b6a68d4066ae41bb8c13bc051985f3fe0791499158487 |
| proofs/M6_SHARP_KERNEL_REVIEW.md | 06cb7019929de6aa1739ea081ce1d314c1e50f6468c4461b9f07d2e442d1c568 |
| proofs/M6_EFFECTIVE_PRODUCT.md | a3b6b878102cfbe022aada6477c78c8641edc5d25b813ea7030f032fce96c522 |
| M6_ACCEPTANCE.md | 6ee93e1e27984dfda45d6932b943ea953e2953e7bfb10da31dcf65abdc8914a6 |

The proof is conditional on those accepted inputs and makes no novelty or
unrestricted-SAW claim.  The frozen M3--M7 scientific files remain untouched.
