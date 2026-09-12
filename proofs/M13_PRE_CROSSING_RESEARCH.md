# M13: a uniform pre-crossing phase bound

Status: independent bounded lemma, not a monotonicity theorem.  On the real
domain \(N\ge32\), \(\theta\in[.8,.9]\), write

\[
 S_{\rm pre}(\theta)=\sum_{n=0}^{N}W_n(\theta),
 \qquad
 W_n=A_0T_nK_{e,n}L_W(u_n).
\]

The reviewed M10/M11 inputs give \(W_n>0\).  This note proves the useful
relative upper bound

\[
 \boxed{\quad
 \partial_\theta S_{\rm pre}
 <\frac{2.06}{N}S_{\rm pre}.\quad}                 \tag{1}
\]

The bound uses \(ne<.17\), the pre-crossing lower box \(u_n\ge u_g>.70\),
and the favorable derivative of \(A_0\).  Its sign is still positive; it
does not prove that \(S_{\rm pre}\) is nonincreasing.

## 1. The Gamma factor is decreasing before the crossing

Use the M10 notation
\[
 a=N+\theta,\qquad b=a-\beta(e),\qquad
 T_n=\prod_{j=0}^{n-1}\frac{a-j}{b-j},
 \qquad \beta_\theta<0,
\]
where the accepted real beta strip is
\(.70<\beta<.72\).  If \(0\le n\le N\), then \(a-j>0\) and
\(b-j>0\) for every \(j<n\).  The exact chain rule is

\[
 \partial_\theta\log T_n
 =-\beta\sum_{j=0}^{n-1}\frac1{(a-j)(b-j)}
  +\beta_\theta\sum_{j=0}^{n-1}\frac1{b-j}<0                 \tag{2}
\]

for \(n\ge1\), and is zero for \(n=0\).  Both terms in (2) are
nonpositive, with the first one strictly negative.  This is a genuine
pre-crossing sign and does not use a finite point measurement.

## 2. The kernel motion improves on the pre mesh

For \(x=ne\), \(v=e^{-x}\), the endpoint-safe M11 kernel estimate gives
\[
 e\,|u_{n,e}|
 <\frac{6e}{7}+\sqrt{\frac{1-v}{3}}.                 \tag{3}
\]
The real phase box gives \(0<e<.17/N\).  For \(0\le n\le N\),

\[
 x=ne<.17,\qquad 1-e^{-x}<x<.17,
\]
and the exact checker proves
\[
 \sqrt{\frac{17}{300}}<\frac{239}{1000},\qquad
 \frac6{7\cdot180}=\frac1{210}.
\]
Since \(|e_\theta|<e/N\), (3) therefore yields

\[
 0<u_{n,\theta}<\frac{\bar u}{N},\qquad
 \bar u:=\frac1{210}+\frac{239}{1000}
 =\frac{5119}{21000}<.244.                             \tag{4}
\]

The \(n=0\) endpoint is included: the mesh term in (3) vanishes there.
This uses the positive real \(e\) gap in the reviewed M11 derivation and
does not differentiate the critical square root at \(e=0\).

## 3. Weight contribution

For \(n\le N<a=N+\theta\), the kernel point satisfies
\[
 u_n=U(t,e^{-ne})\ge U(t,e^{-s_g})=u_g>.70.             \tag{5}
\]
Here \(U_v>0\), \(ne<s_g\), and the last box is the reviewed M11 scalar
box.  Use
\[
 R(t,u,h)=\frac{V_2(u)}{V_1(u)}
 =\frac{h}{1-th}
  +\frac{u(1-h)}{(1-tu)(1-tuh)}.
\]
The displayed expression is increasing in \(t,u,h\) on the physical box:
the \(t,u\) derivatives are positive, and
\[
 R_h=\frac1{(1-th)^2}-\frac{u}{(1-tuh)^2}\ge0
\]
as in the reviewed M11 weight calculation.  With
\[
 t_\ell=\frac{207}{500},\quad u_\ell=\frac7{10},\quad
 h_\ell=\frac{353}{500},\quad
 \delta_D<\frac7{100},
\]
the exact rational checker gives
\[
 \begin{aligned}
 R&\ge R_\ell:=
 \frac{h_\ell}{1-t_\ell h_\ell}
 +\frac{u_\ell(1-h_\ell)}
 {(1-t_\ell u_\ell)(1-t_\ell u_\ell h_\ell)},\\
 G&:=4t^2R-(1-t+2\delta_D)
 >4t_\ell^2R_\ell-\frac{363}{500}
 >\frac15.                                             \tag{6}
 \end{aligned}
\]
Thus the positive combined weight is \(L_W=V_1G\), with a pre-mesh gap
larger than the global \(7/100\) gap used in M11.

At fixed \(t,h,C,\delta_D\), the exact derivatives are
\[
 \frac{V_{1,u}}{V_1}
 =\frac{t}{1-tu}-\frac{th}{1-tuh}
 <\frac{t_h}{1-t_h}<\frac{71}{100},
\]
\[
 R_u=(1-h)\left[
 \frac1{(1-tu)^2(1-tuh)}
 +\frac{t h u}{(1-tu)(1-tuh)^2}\right].
\]
Using \(t_h=.4143\), \(h\in[.706,.71]\), \(u\le1\), the checker gives
\[
 R_u<R_{u,\max}<\frac{1511}{1000},\qquad
 0<\partial_u\log L_W
 =\frac{V_{1,u}}{V_1}+\frac{4t^2R_u}{G}<6.             \tag{7}
\]

The reviewed M11 weight decomposition has favorable \(A_0,h,C\) terms.
The fixed-\(t\) contribution is \(<1/(1000N)\), and the directed
\(\delta_D\) contribution is, by (6) and
\(-49/(1250N)<\delta_{D,\theta}\le0\),
\[
 0\le(\partial_{\delta_D}\log L_W)\delta_{D,\theta}
 <\frac{2}{1/5}\frac{49}{1250N}
 <\frac{2}{5N}.                                         \tag{8}
\]
The \(A_0\) term can also be kept quantitatively.  From the reviewed
\(J_t/J<7\), \(-t_e<e/7\), and
\[
 \frac1{e^e-1}>\frac1e-1,
\]
the exact formula for \(A_0\) gives
\[
 (\log A_0)_e>\frac1e-1-e.
\]
Since \(|e_\theta|=e/(N+\theta-s_g'(e))>e/(N+.6)\), the elementary
endpoint check at \(N=32\), \(e=17/3200\), and monotonicity in \(N\), gives
\[
 \partial_\theta\log A_0<-\frac{.97}{N}.                \tag{9}
\]
Combining (4), (7)--(9), uniformly for \(0\le n\le N\), yields
\[
 \partial_\theta\log[A_0L_W(u_n)]
 <\frac1N\left[
 6\frac{61}{250}+\frac1{1000}+\frac25-\frac{97}{100}
 \right]
 =\frac{179}{200N}.                                     \tag{10}
\]

The strict \(A_0\) inequality in (9) uses only the real scalar boxes; it
does not assert a sign for the full phase derivative.

## 4. Smooth factor on \(0\le n\le N\)

For each \(j<n\le N\), the M11 inverse-kernel factorization and exact
secant estimate give
\[
 \left|\frac d{de}\log R_e(je)\right|
 <\frac34+\frac95+
 \frac{.51}{.29^2}\frac{61}{250}
 +\frac45+\frac{18}{100}\,je.                            \tag{11}
\]
The \(3.721\) anchor-motion term from the global M11 bound is reduced here
by (4): \(e|u_{j,e}|<61/250\).  Since \(je<.17\), summing the mesh term
directly gives
\[
 c_R=\frac34+\frac95+
       \frac{.51}{.29^2}\frac{61}{250}+\frac45
     =\frac{16247}{3364}.                              \tag{12}
\]

Using \(n\le N\), \(e<.17/N\), and \(|e_\theta|<e/N\),
\[
 \left|\partial_\theta\log\Pi_{e,n}\right|
 <\frac{17c_R}{100N}
   +\frac{9}{100}\frac{17^2}{100^2N}
 =\frac{692684941}{841000000N}.                       \tag{13}
\]
The reviewed real scalar bound \(|(\log r)_e|<2\) similarly gives
\[
 \left|\partial_\theta\log r^n\right|<\frac{17}{50N}. \tag{14}
\]
Hence
\[
 \left|\partial_\theta\log K_{e,n}\right|
 <\frac{978624941}{841000000N}<\frac{1.164}{N}.       \tag{15}
\]

## 5. Summing the positive pre terms

Combining (2), (10), and (15),
\[
 \partial_\theta\log W_n
 =\partial_\theta\log[A_0L_W(u_n)]
  +\partial_\theta\log T_n
  +\partial_\theta\log K_{e,n}
 <\frac{1731319941}{841000000N}
 <\frac{2.06}{N}.                                    \tag{16}
\]
Because \(W_n>0\), summing (16) proves (1).  The exact rational replay is

    python3 -m proofs.m13_pre_phase_bounds \
      > /tmp/m13-pre-phase-bounds.json

and returns status pass with all twelve arithmetic claims true.  It is an
exact constant check, not a numerical phase scan.

There is a sharper identity that isolates what is still missing.  With
\[
 S_n^{(\Gamma)}:=\sum_{j=0}^{n-1}\frac1{(a-j)(b-j)},
\]
the favorable beta correction in (2) can be retained, giving
\[
 \partial_\theta S_{\rm pre}
 \le \frac{2.06}{N}S_{\rm pre}
 -\sum_{n=0}^{N}W_n\,\beta S_n^{(\Gamma)}.             \tag{17}
\]
Thus a proof of nonincrease would need a lower bound for the
\(W_n\)-weighted Gamma mass in (17), or a signed estimate for the smooth
and weight derivatives.  The reviewed inputs provide only the absolute
smooth bound (15) and the one-sided weight bound (10); they do not provide
that weighted lower bound.  In particular, positivity and decrease of
\(K_nL_W(u_n)\) as a function of \(n\) do not by themselves control its
\(\theta\)-derivative or the weighted average in (17).

The existing \(N=32,\theta=.85\) decomposition output reports a finite,
non-certified pre derivative near \(-.07389\).  It is retained only as
motivation and is not used in (1), (10), or (17).

## Scope and provenance

This note uses the real M10 beta sign/strip, the endpoint-safe M11 smooth
factor bound, the reviewed M11 weight estimate, and positivity of
\(T_n,K_n,L_W\).  M11/M12 sources are read-only inputs; no source there was
modified.  The note does not assert a sign for the full \(F_N\), the boundary
term, the post-crossing sum, or the distant tail.

The new checker has no external inputs, performs no phase scan, and writes no
repository output.  Hashes of the frozen inputs are
reported below; final new-file hashes belong to the independent review.

| input | SHA-256 |
|---|---|
| proofs/M11_SMOOTH_PHASE_BOUND.md | 15e8c64e5d554a12eb40b68ef0b724d2aead52042779516fce9e78628f180f07 |
| proofs/M11_WEIGHT_PHASE_BOUND.md | e6fa7bbec97ed9caeb3785850728aeef64b20af610f70d3234a5e38398f06ca6 |
| proofs/M11_DIRECTED_PHASE_BOUND.md | efe6b4c4a57e502cb4ff9b04835aaed556463c83d7cbc5e0d86cf73b687ef08e |
| proofs/M10_BETA_REAL.md | 51b59ecaea7fa22647d76471f8ecef9e8483581fdd3941a02d56b0fb22397f80 |
| proofs/M10_BARE_PHASE_DERIVATIVE.md | 04605690a985a1c65a682354eab86c08480c17c46be39f243c86a020a094a265 |
| proofs/M10_POSITIVE_COMBINED_WEIGHT.md | 9801fb62426a4d88730c31a19febfdbb5c10f9e2edb7f904eaea54bdd2d66b2a |
| proofs/M10_DIRECTED_MONOTONICITY.md | 2f7a47aa316b10fc119d3bb7d6b11b4005b7b2234a2321696eecf01f37c4cc61 |

The repository HEAD during this replay was
8f8176b8039c518455ea5a1ec284564f4f1ea108; the two M13 files are new and
uncommitted by design.
