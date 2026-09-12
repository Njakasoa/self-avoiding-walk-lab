# M13: an explicit absolute phase derivative bound for the distant tail

Status: bounded analytic candidate for independent review.  This note controls
only the differentiated real tail

\[
 S_{\rm tail}(N,\theta)=
 \sum_{n>60N} A_0(e)\,T_n(a,b)\,K_n(e)\,L_W(u_n),
 \qquad
 K_n=r^n\Pi_{e,n},
\]

where \(N\ge32\), \(\theta\in[4/5,9/10]\), \(e=e_N(\theta)>0\), and
\(a=N+\theta\), \(b=a-\beta\) with \(7/10<\beta<18/25\).  It proves

\[
 \boxed{\ |\partial_\theta S_{\rm tail}|<10^{-3}.\ }
 \tag{M13.1}
\]

The result is an absolute tail estimate for the real positive summands.  It
does not prove a sign for the complete \(F_N\), and it does not import the
older Gamma estimate whose hypothesis \(a\ge200\) would exclude \(N=32\).
The exact rational ledger is `proofs/m13_tail_bounds.py`; it must be run
without optimization.

## Inputs and the phase scale

Use the reviewed real phase bounds
\[
 .15<s_g<.17,
 \qquad |e_\theta|<e/N,
 \qquad e=\frac{s_g}{N+\theta}.
\tag{M13.2}
\]
They imply, for \(N\ge32\),
\[
 eN>.15\frac{N}{N+.9}>\frac{29}{200},
 \qquad eN<.17,
 \qquad e<\frac1{180}.
\tag{M13.3}
\]
Set \(m=60N+1\) and \(x_n=ne\).  Then
\[
 \frac{87}{10}<x_m<11.                                  \tag{M13.4}
\]
The lower bound is the only place where the numerical tail location enters.

The real M6 secant argument, with the M11 separation \(s_h>0\), gives
\[
 0<R_e(je),\qquad 0<\Pi_{e,n}:=\prod_{j<n}R_e(je)\le1,
 \qquad 0<r\le e^{-e}.                                  \tag{M13.5}
\]
These are real product inputs, not a finite-index scan.

## Post-crossing Gamma bound without \(a\ge200\)

For \(n\ge N+1\), reflection gives the positive form
\[
 T_n=
 \frac{\sin(\pi\theta)}{\sin(\pi(\theta-\beta))}
 \frac{\Gamma(a+1)}{\Gamma(b+1)}
 \frac{\Gamma(n-a)}{\Gamma(n-b)}.                       \tag{M13.6}
\]
For the present tail, put \(x=b+1\) and \(y=n-a\).  Even at \(N=32\),
\[
 x>1,\qquad y>1,
\]
and the elementary endpoint inequalities give
\[
 \frac{x}{y}<\frac1{56},\qquad
 \frac{\beta}{y}<\frac1{2000}.                           \tag{M13.7}
\]
Indeed \(x\le N+6/5\), \(y\ge59N+1/10\), and both inequalities are
strongest at \(N=32\).

Wendel's inequality, in the form
\[
 \frac{\Gamma(x+\beta)}{\Gamma(x)}\le x^\beta,
 \qquad
 \frac{\Gamma(y)}{\Gamma(y+\beta)}
 \le y^{-\beta}(1+\beta/y)^{1-\beta},                  \tag{M13.8}
\]
therefore gives
\[
 \frac{\Gamma(a+1)}{\Gamma(b+1)}
 \frac{\Gamma(n-a)}{\Gamma(n-b)}
 <\frac{2001}{2000}\left(\frac1{56}\right)^{7/10}
 <\frac{2001}{32000}.                                   \tag{M13.9}
\]
The last inequality is the exact check \(16^{10}<56^7\).  On the phase
interval, the sine multiplier is less than \(12/5\).  One elementary proof
uses \(\sin(\pi/5)<59/100\), the exact identity
\(\sin^2(\pi/5)=(5-\sqrt5)/8\), and
\[
 \sin(2\pi/25)>2\pi/25-(2\pi/25)^3/6>31/125.
\]
The last comparison uses \(157/50<\pi<22/7\).  Hence
\[
 \boxed{0<T_n<\frac{151}{1000}\qquad\(n>60N\).}           \tag{M13.10}
\]

This is a direct far-post Gamma estimate.  It does not use the M6
near-crossing hypothesis \(a\ge200\).

## A uniform \(L_W\) bound after \(x>8.7\)

The inverse-kernel equation gives, with \(v=e^{-x_n}\),
\[
 u_n-t=\frac{v\,t(1-t^2)u_n}{1-tu_n}<v\,t(1+t)<v.   \tag{M13.11}
\]
By (M13.4), \(v<1/5000\), so \(u_n<829/2000\).  Use the reviewed boxes
\[
 t<\frac{4143}{10000},\quad q>\frac{359}{360},\quad
 \frac{353}{500}<h<\frac{71}{100},\quad u_n<\frac{829}{2000}. 
\tag{M13.12}
\]
For
\[
 V_1=\frac{dd+L_1}{C},\quad
 dd=\frac1{(1-tu)(1-th)},\quad
 L_1=\frac{h}{(1-th)(1-h)},
\]
and
\[
 R=\frac{V_2}{V_1}
 =\frac{h}{1-th}+\frac{u(1-h)}{(1-tu)(1-tuh)},              \tag{M13.13}
\]
the endpoint maxima in the ledger give \(V_1<9\) and \(R<6/5\).  Since
\(L_W=V_1[4t^2R-(1-t+2\delta_D)]\), \(\delta_D>0\) gives
\[
 0<L_W(u_n)<V_1[4t^2R-(1-t)]<2.                         \tag{M13.14}
\]
The lower sign is the reviewed M10 combined-weight lemma; the upper bound is
the new tail-only rational calculation.

## Bare-product and harmonic derivative bounds

For \(n>60N\), write \(m_n=n-N-1\) and \(\delta=\theta-\beta\).  Then
\(2/25<\delta<1/5\), and the exact derivative identity is
\[
 \partial_\theta\log T_n=-\beta S_n+\beta_\theta H_n,
\]
where
\[
 S_n=\sum_{j<n}\frac1{(a-j)(b-j)},\qquad
 H_n=\sum_{j<n}\frac1{b-j}.                             \tag{M13.15}
\]
Splitting at \(j=N\) gives
\[
 S_n=\sum_{k=0}^{N}\frac1{(k+\theta)(k+\delta)}
 +\sum_{k=1}^{m_n}\frac1{(k-\theta)(k-\theta+\beta)}. 
\tag{M13.16}
\]
A two-case endpoint split at \(\theta=17/20\), with the remaining sums
bounded by \(\sum_{k\ge1}k^{-2}<5/3\) and
\(\sum_{k\ge2}k^{-2}<2/3\), gives
\[
 S_n<27.                                               \tag{M13.17}
\]
For example, the two exact ledgers are
\[
\begin{aligned}
 S_n&<\frac{125}{8}+\frac{400}{51}+\frac53+\frac{3200}{2553}<27,
 &&\theta\le17/20,\\
 S_n&<\frac{2000}{221}+\frac{25}{2}+\frac53+\frac{400}{297}<27,
 &&\theta\ge17/20.
\end{aligned}
\]
Thus \(\beta S_n<(18/25)27=486/25\).

The same split gives the logarithmic harmonic bound
\[
 |H_n|<\frac{59}{4}+\frac94\log n.                      \tag{M13.18}
\]
The M10 beta derivative estimate \(|\beta_\theta|<1/(125N^3)\) is used
only after this point.  Since \(\log n=\log(x_n/e)\le x_n+1/e\) and
\(1/e<7N\), its contribution is summable in the geometric tail.

## Absolute theta derivative of one tail summand

The reviewed M11 inverse-kernel argument gives, without imposing the old
\(je<10.2\) cutoff,
\[
 \left|\partial_e\log R_e(je)\right|
 <\frac{7071}{1000}+\frac9{50}je.                      \tag{M13.19}
\]
Together with \(|(\log r)_e|<2\) and \(|e_\theta|<e/N\), summing over
\(j<n\) yields
\[
 |\partial_\theta\log K_n|
 <\frac{(2+7071/1000)x_n+(9/100)x_n^2}{N}.                \tag{M13.20}
\]
The M11 weight formulas also give an absolute (rather than one-sided)
bound
\[
 |\partial_\theta\log[A_0L_W(u_n)]|<\frac{14}{N}.       \tag{M13.21}
\]
For clarity, this uses the same independent-variable allowances as the
reviewed proof: \(200\) for the positive \(t\)-derivative, \(50\) for the
absolute \(h\)-derivative, \(2\) for \(C\), \(16\) for \(u\), \(200/7\)
for \(\delta_D\), and \(2\) for \(A_0\), after the phase derivative boxes
\(|t_\theta|<e^2/(7N)\), \(|h_\theta|<.26e/N\),
\(|C_\theta|<.51e/N\), \(|u_{n,\theta}|<.61/N\), and
\(|\delta_{D,\theta}|<49/(1250N)\).  This is an absolute ledger for the
tail; the earlier \(11/N\) estimate was only an upper-sided favorable bound.

Combining (M13.17)--(M13.21) gives a pointwise polynomial majorant.  In the
normalized geometric tail, put \(p=e^{-e}\).  The exact geometric moments
\[
 (1-p)\sum_{k\ge0}p^k(x_m+ke)<12,
\qquad
 (1-p)\sum_{k\ge0}p^k(x_m+ke)^2<146                 \tag{M13.22}
\]
follow from \(x_m<11\), \(ep/(1-p)<1\), and
\(e^2p(1+p)/(1-p)^2<3\).  The beta-harmonic term contributes less than
\(1/7000\) in the same normalized average.  The exact ledger therefore
gives the averaged logarithmic derivative bound
\[
 \mathbb E\left|\partial_\theta\log(A_0T_nK_nL_W)\right|
 <\frac{119}{5}.                                      \tag{M13.23}
\]

## Summing the tail

The exact scalar cancellation is
\[
 A_0=J\(t\)(1-e^{-e}),\qquad
 J\(t\)=\frac{t(1-t^2)}{1-t-t^2}<\frac56.                 \tag{M13.24}
\]
Using (M13.5), (M13.10), (M13.14), and the normalized geometric moments,
\[
\begin{aligned}
 |\partial_\theta S_{\rm tail}|
 &\le \frac56\frac{151}{1000}\,2\,\frac{119}{5}
       e^{-x_m}\\
 &< \frac{17969}{3000}e^{-87/10}<\frac1{1000}.          \tag{M13.25}
\end{aligned}
\]
The final inequality is checked by the positive degree-18 exponential sum
\(\sum_{k=0}^{18}(87/10)^k/k!>17969/3\).

For each fixed integer N, e_N(theta) is positive and continuous on the
compact phase interval, hence has a positive minimum. The bounds above
majorize each summand and its phase derivative by a constant times
(1+n^2+log n) exp(-n e_min), uniformly in theta. Both series converge
uniformly. Termwise differentiation and the triangle inequality in
(M13.25) are therefore justified, including one-sided endpoint limits.

This closes the absolute differentiated tail only.  The pre-crossing sum,
boundary contribution, and the sign of the complete \(F_N\) remain separate
arguments owned by the root.

## Reproduction and scope

Run:

```text
.venv/bin/python -m proofs.m13_tail_bounds
```

The script returns deterministic JSON with exact Fraction strings and fails
closed under `-O`.  No finite index scan, held-out data, or full \(F_N\) sign
claim is used.

