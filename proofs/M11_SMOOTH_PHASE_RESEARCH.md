# M11: smooth-factor phase derivative research

Status: **partial real lemma plus a derivative obstruction**.  This note
controls the scalar part of the smooth factor on the complete real domain
\(N\ge32\), \(\theta\in[.8,.9]\), and records the exact derivative identity
needed for the nonsingular product.  It does not claim a bound for that
product, a sign for the full phase \(F_N\), or a sign for the complete W
denominator derivative.

The inputs are the accepted real phase box and the M10 scalar certificate.
Write
\[
 e=e_N(\theta),\qquad
 s_g(e)=e(N+\theta),\qquad
 e_\theta=\frac{e}{s_g'(e)-N-\theta}.
\]
M10_BETA_REAL gives
\[
 0<e<\frac{.17}{N}\le\frac{.17}{32}<\frac1{180},\qquad
 |e_\theta|<\frac eN.                                      \tag{1}
\]
The M5 real formulas are used only on their stated \(e\le .01\) domain:
\[
 \frac25<t<\sigma<\frac{83}{200},\quad
 1-\frac e2\le q=e^{-e/2}\le1,\quad
 -\frac1{400}\le t_e\le0,\quad q_e=-\frac q2.              \tag{2}
\]
Thus the following argument does not extend a small-\(e\) complex estimate
to \(N=32\).

## 1. Exact smooth-factor decomposition

Use the exact M6 factorization
\[
 z_n=z_0\,r^n\,T_n(a,b)\,\Pi_{e,n},\qquad
 r=\frac{q(q-t)}{1-tq},\qquad
 \Pi_{e,n}=\prod_{j=0}^{n-1}R_e(je),                       \tag{3}
\]
where
\[
 a=N+\theta,\qquad b=a-\beta(e),\qquad
 \beta(e)=\frac{s_g(e)-s_g(-e)}e.
\]
The smooth product is \(K_{e,n}=r^n\Pi_{e,n}\).  For the moment formulas,
the same smooth part occurs in
\[
 \frac{Qz_n}{T_n}=Qz_0\,K_{e,n},\qquad
 Q=q\,t^2(1-q^2)(1-t^2)>0.                                \tag{4}
\]
Consequently, wherever the logarithmic derivatives are defined,
\[
 \partial_\theta\log\left|\frac{Qz_n}{T_n}\right|
 =\partial_\theta\log Q+\partial_\theta\log|z_0|
  +\partial_\theta\log r^n+\partial_\theta\log\Pi_{e,n}.    \tag{5}
\]
The first three terms can be bounded on the full \(N\ge32\) domain without
any derivative assertion about \(\Pi_{e,n}\).

The integer grid stays away from both Gamma roots.  Indeed
\(s_g=ea\), \(s_h=eb\), and M10 gives
\(\beta\in(.70,.72)\), so
\[
 |j-a|\ge .1,\qquad |j-b|\ge .08,\qquad
 |je-s_g|\ge .1e,\qquad |je-s_h|\ge .08e                 \tag{6}
\]
for every integer \(j\ge0\).  This is useful for divided differences, but
by itself it is not a derivative bound.

## 2. A proved \(0.71\) allowance for \(Qz_0r^n\)

Put \(C=q-t\) and \(D=1-tq\).  From (2), \(q>.99\),
\[
 C>.57,\qquad D>.58.                                      \tag{7}
\]
Since
\[
 (\log r)_e=-\frac12+\frac{q_e-t_e}{C}-\frac{D_e}{D},
\qquad D_e=-t_eq-tq_e,
\]
we have \((\log r)_e<0\).  The same boxes give the exact rational
allowance
\[
 0<-(\log r)_e
 <\frac12+
 \frac{\frac12+\frac1{400}}{57/100}
 +\frac{\frac1{400}+\frac{83}{400}}{58/100}
 <2.                                                       \tag{8}
\]
Therefore, for \(n\le60N\), (1) gives
\[
 0<\partial_\theta\log r^n
 <\frac{2ne}{N}
 <\frac{20.4}{N}\le\frac{51}{80}.                         \tag{9}
\]

For the moment prefactor in (4),
\[
 (\log Q)_e
 =-\frac12+\frac{2t_e}{t}
   +\frac{q^2}{1-q^2}
   -\frac{2tt_e}{1-t^2}.                                  \tag{10}
\]
For \(0<e<.01\), \(1-q^2=1-e^{-e}\ge e/2\).  With (2),
\[
 |(\log Q)_e|<
 \frac2e+\frac12+\frac1{80}+\frac1{300}
 <\frac2e+1.
\]
It follows that
\[
 |\partial_\theta\log Q|
 <\frac eN\left(\frac2e+1\right)
 <\frac{2.01}{N}<.063.                                   \tag{11}
\]

The initial factor has a similarly direct bound.  Since
\[
 g_e(0)=t-q+tq^2,\qquad
 \frac{d}{de}g_e(0)
 =t_e(1+q^2)-q_e(1-2tq),
\]
the boxes (2) imply
\[
 g_e(0)<2\frac{83}{200}-.99<-.16,\qquad
 \left|\frac{d}{de}g_e(0)\right|
 <\frac{2}{400}+\frac12=\frac{101}{200}.                 \tag{12}
\]
As \(z_0=1/g_e(0)\), (1) gives
\[
 |\partial_\theta\log|z_0||
 <\frac{16}{5}\frac eN
 <\frac{.544}{N^2}.                                      \tag{13}
\]
Combining (9), (11), and (13), and using \(N\ge32\), proves the uniform
scalar allowance
\[
 \boxed{\ 
 \left|\partial_\theta\log|Qz_0r^n|\right|
 <\frac{51}{80}+\frac{.063}{1}
   +\frac{.544}{32^2}
 <.71,\qquad n\le60N.
 \ }                                                       \tag{14}
\]
The sign in (9) is also known: the geometric factor \(r^n\) contributes
positively when \(\theta\) increases, because \(r_e<0\) and \(e_\theta<0\).
No sign is asserted for the \(Q\) or \(z_0\) contributions.

## 3. Exact derivative identity for the remaining product

Let
\[
 g_e(s)=t(e)-D(e)U(t(e),e^{-s}),\qquad
 \ell_e(s)=\log R_e(s).
\]
With \(s_g=s_g(e)\), \(s_h=s_h(e)\), define the removable divided
differences
\[
 {\cal F}_e(s)=\int_0^1
  g_{e,s}\bigl(s_g+u(s-s_g)\bigr)\,du,
\quad
 {\cal G}_e(s)=\int_0^1
  g_{e,s}\bigl(s_h+u(s-s_h)\bigr)\,du.                    \tag{15}
\]
These equal \(g_e(s)/(s-s_g)\) and
\((g_e(s)+\delta)/(s-s_h)\), respectively, because
\(g_e(s_g)=0\) and \(g_e(s_h)=-\delta\).  The M6 concavity lemma gives
\({\cal F}_e,{\cal G}_e>0\) and \(R_e={\cal F}_e/{\cal G}_e\).

Use a dot for the partial \(e\)-derivative at fixed \(s\).  Implicit
differentiation of the two root equations gives
\[
 \dot s_g=-\frac{\dot g_e(s_g)}{g_{e,s}(s_g)},\qquad
 \dot s_h=-\frac{\dot g_e(s_h)+\dot\delta}{g_{e,s}(s_h)}.  \tag{16}
\]
For \(y_g(u)=s_g+u(s-s_g)\) and
\(y_h(u)=s_h+u(s-s_h)\), differentiation of (15) gives
\[
 \begin{aligned}
 \dot{\cal F}_e(s)
 &=\int_0^1\left[
   \dot g_{e,s}(y_g(u))
   +(1-u)\dot s_g\,g_{e,ss}(y_g(u))\right]du,\\
 \dot{\cal G}_e(s)
 &=\int_0^1\left[
   \dot g_{e,s}(y_h(u))
   +(1-u)\dot s_h\,g_{e,ss}(y_h(u))\right]du,\\
 {\cal F}_{e,s}(s)
 &=\int_0^1u\,g_{e,ss}(y_g(u))\,du,\qquad
 {\cal G}_{e,s}(s)
 =\int_0^1u\,g_{e,ss}(y_h(u))\,du.
 \end{aligned}                                             \tag{17}
\]
Thus, at the mesh point \(s_j=je\),
\[
 \frac d{de}\ell_e(je)
 =\left(\frac{\dot{\cal F}_e}{{\cal F}_e}
        -\frac{\dot{\cal G}_e}{{\cal G}_e}\right)(s_j)
 +j\left(\frac{{\cal F}_{e,s}}{{\cal F}_e}
          -\frac{{\cal G}_{e,s}}{{\cal G}_e}\right)(s_j),   \tag{18}
\]
and exactly
\[
 \partial_\theta\log\Pi_{e,n}
 =e_\theta\,{\cal D}_{e,n},\qquad
 {\cal D}_{e,n}:=\sum_{j=0}^{n-1}\frac d{de}\ell_e(je).     \tag{19}
\]
The grid separation (6) prevents a Gamma-root denominator from vanishing.
For each fixed \(e>0\), the \(j=0\) endpoint is also an ordinary real
kernel point: the implicit equation gives
\[
 \Delta(t,1)=t^2(q^{-1}-q)^2>0.
\]
The issue below is uniformity as \(e\downarrow0\), not existence at any
fixed \(N\).

## 4. The remaining uniform estimate is not supplied by the frozen inputs

Equations (15)--(19) reduce the missing estimate to real bounds for
\(\dot g_{e,s}\), \(g_{e,ss}\), the two root derivatives, and the positive
divided differences over the segments joining \(s_g,s_h\) to \(s_j\).
The existing inputs do not supply those bounds on the domain needed here:

* M5's real product estimate is a \(C^0\) estimate for
  \(\ell_e(s)/e-\psi(s)\), and its analytic derivative boxes are restricted
  to the tiny \(e\)-disks used in that note.
* M6 and M9 give \(0<R_e\le1\), finite variation, and \(C^0\) mesh error,
  but no \(e\)- or \(s\)-derivative estimate for \(\ell_e\).
* M7's complex derivative argument is scoped to its large-\(N\) complex
  domain; it cannot be substituted for a real \(N=32\) estimate.
* M10_BETA_REAL bounds \(s_g'''\), hence \(\beta_\theta\), but does not
  bound the mixed derivatives in (17).

There is a genuine endpoint scale issue.  At \(s=0\),
\(\sqrt{\Delta(t,1)}=t(q^{-1}-q)\asymp e\), so direct differentiation of
the square-root kernel produces \(g_{e,s}(0)\) and \(g_{e,ss}(0)\) with
negative powers of \(e\).  A uniform constant box for those derivatives
cannot be valid.  A valid proof would have to isolate the first few mesh
cells in the scaled coordinate \(s/e\), then use ordinary real boxes away
from \(s=0\), and sum the resulting weighted bounds.  No such checker or
lemma is present in the frozen inputs.

For reference, the following would be sufficient and would be quantitatively
useful, but is **conditional**:
\[
 |{\cal D}_{e,n}|\le100N
 \quad(N\ge32,\ \theta\in[.8,.9],\ n\le60N).               \tag{20}
\]
By (1), (19), and \(e<.17/N\), this would imply
\[
 |\partial_\theta\log\Pi_{e,n}|
 <\frac{e}{N}(100N)
 <\frac{17}{N}\le\frac{17}{32}<.532.                    \tag{21}
\]
Together with the proved scalar allowance (14), it would give
\[
 \left|\partial_\theta\log\left|\frac{Qz_n}{T_n}\right|\right|
 <.71+.532<1.25.                                       \tag{22}
\]
Combining (22) with the M10 bare-product bound
\(\partial_\theta\log T_n<-4.18\) on \(N+1\le n\le60N\) would leave
a negative margin below \(-2.93\) for the scalar term \(Qz_n\), before
regularized weights, boundary terms, and the directed parameter are
included.  This is not a theorem until (20) is proved.

The directed phase derivative of \(\delta_D\), the regularized weights,
and the boundary terms are separate contributions.  In particular,
(22) cannot be promoted to a derivative sign for \(P_N\), \(H_N\), or
the full \(F_N\).

## Provenance and scope

No numerical scan or held-out index was used.  The input snapshot was
ce376e85793887f770b35fc80e180e35f4b2ff18; relevant input hashes were:

| input | SHA-256 |
|---|---|
| proofs/M10_BETA_REAL.md | 51b59ecaea7fa22647d76471f8ecef9e8483581fdd3941a02d56b0fb22397f80 |
| proofs/M10_BARE_PHASE_DERIVATIVE.md | 04605690a985a1c65a682354eab86c08480c17c46be39f243c86a020a094a265 |
| proofs/M6_EFFECTIVE_PRODUCT.md | a3b6b878102cfbe022aada6477c78c8641edc5d25b813ea7030f032fce96c522 |
| proofs/M5_PHASE_DOMAIN.md | e28526758615f3d3d2279dda542b381c9a5d69313f770c5c4a6e5c57863065bf |
| proofs/M5_DIRECTED_LOG.md | fcf18e907607e185cb8dba7e4c25c58c8df3aa5088027429fc33d86677c9cf1f |

This research note is new and unreviewed.  It preserves the distinction
between the proved scalar allowance, the exact product identity, and the
unproved derivative envelope (20).
