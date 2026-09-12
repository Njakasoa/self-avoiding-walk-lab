# M10: a real third-derivative bound for the phase quotient

Status: exact scalar interval lemma supporting
M10_BARE_PHASE_DERIVATIVE.md.  It uses no phase-band scan and changes no
earlier note.  The checker
proofs/m10_beta_real.py uses the 384-bit outward interval type I384 and
must be run without -O.

Let
\[
 \sigma=\sqrt2-1,\qquad q=e^{-e/2},\qquad
 D=1-tq,
\]
where \(t=t(e)\) is the physical even root.  On
\[
 |e|\le\frac1{180},
\]
use the real boxes
\[
 \sigma-\frac{(1/180)^2}{8}\le t\le\sigma,\qquad
 \frac{359}{360}\le q\le\frac{1003}{1000}. \tag{1}
\]
The \(t\)-box is the even extension of the M5_DIRECTED_LOG.md real root
bound \(0\le\sigma-t\le e^2/8\), proved there for \(|e|\le1/10\).
The \(q\)-box follows without numerical evaluation:
\[
 e^{-1/360}>1-\frac1{360}=\frac{359}{360},\qquad
 e^{1/360}<\frac1{1-1/360}=\frac{360}{359}<\frac{1003}{1000}.
\]
The checker recomputes all derivative expressions from these boxes with
I384.

## 1. Implicit derivatives of \(t\)

The implicit equation is
\[
 A(t):=t^{-1}-1+t+t^2=2\cosh(e/2).
\]
Write
\[
 A'=-t^{-2}+1+2t,\qquad
 A''=2t^{-3}+2,\qquad
 A'''=-6t^{-4},
\]
and
\[
 \sinh(e/2)=\frac{q^{-1}-q}{2},\qquad
 \cosh(e/2)=\frac{q+q^{-1}}2.
\]
Since \(A'<0\) on (1), implicit differentiation gives
\[
 t'=\frac{\sinh(e/2)}{A'},\qquad
 t''=\frac{\cosh(e/2)/2-A''(t')^2}{A'}, \tag{2}
\]
\[
 t'''=\frac{\sinh(e/2)/4-A'''(t')^3-3A''t't''}{A'}. \tag{3}
\]
The corresponding derivatives of \(q\) are
\[
 q'=-q/2,\qquad q''=q/4,\qquad q'''=-q/8. \tag{4}
\]

## 2. Algebraic formula for \(s_g'''\)

The phase coordinate has the exact algebraic-logarithmic form
\[
 s_g(e)=-\log q-\log(D-t^2)+\log D+\log(1-t^2). \tag{5}
\]
For a positive scalar jet \(f,f',f'',f'''\), define
\[
 {\cal L}_3(f)=
 \frac{f'''}f-\frac{3f''f'}{f^2}
 +\frac{2(f')^3}{f^3}. \tag{6}
\]
This is the third derivative of \(\log f\).  Therefore
\[
 s_g'''=-{\cal L}_3(q)-{\cal L}_3(D-t^2)
          +{\cal L}_3(D)+{\cal L}_3(1-t^2). \tag{7}
\]
All four arguments in (7) are strictly positive on the I384 box.  No
logarithm is numerically evaluated; only rational interval operations,
the displayed derivatives, and the formula (6) are used.

The exact checker output is
\[
 0.2827276553397733
 <s_g'''(e)<
 0.4137860369747535
 \qquad \left(|e|\le\frac1{180}\right). \tag{8}
\]
In particular,
\[
 0<s_g'''(e)<0.414<4. \tag{9}
\]
The full dyadic endpoints are retained in the JSON output produced by
the checker; the decimals in (8) are only a readable rendering.

## 3. Consequences for \(\beta\) and the phase derivative

The exact even quotient identity from M6 is
\[
 \beta(e)=\eta_e=\frac{s_g(e)-s_g(-e)}e
          =\int_{-1}^{1}s_g'(re)\,dr. \tag{10}
\]
Differentiating and subtracting the odd zero-order term gives
\[
 \beta'(e)
 =e\int_{-1}^{1}r^2\int_0^1s_g'''(u r e)\,du\,dr. \tag{11}
\]
Thus for \(e>0\), (8) implies
\[
 0.1884851035598489\,e
 <\beta'(e)<
 0.2758573579831690\,e. \tag{12}
\]
The exact I384 check records these two endpoints as the interval
\((2/3)[\,s_g'''\,]\).
Since \(\beta(0)=\eta\), integration of the upper bound gives
\[
 \eta<\beta(e)<\eta+0.138e^2. \tag{13}
\]
The checker proves \(\eta>.70\), \(\eta<.71\), and
\(\eta+0.138/180^2<.72\).  Thus the beta strip
\[
 .70<\beta(e)<.72 \tag{14}
\]
is obtained on the full physical \(N\ge32\) range, rather than assumed.

For the real phase inverse,
\[
 s_g(e)=e(N+\theta).
\]
Using the accepted real phase box
\[
 .3<s_g'(e)<.4,\qquad .15<s_g(e)<.17,\qquad
 \theta\in[.8,.9], \tag{15}
\]
gives
\[
 e_\theta=\frac{e}{s_g'(e)-N-\theta}<0,\qquad
 |e_\theta|<\frac eN,\qquad
 0<e<\frac{.17}{N}. \tag{16}
\]
For \(N\ge32\), the last upper bound is below \(1/180\), so the signed
I384 interval covers every physical \(e_N(\theta)\) in this range.
Combining (11)--(15) gives the sign and size
\[
 \boxed{\ \beta_\theta=\beta'(e)e_\theta<0,\qquad
 |\beta_\theta|
 <\frac{2}{3}(0.414)\frac{e^2}{N}
 <\frac{0.008}{N^3}.\ } \tag{17}
\]
The final coefficient is checked exactly:
\[
 \frac23\,(0.414)\,(0.17)^2
 =\frac{19941}{2500000}<0.008. \tag{18}
\]

## 4. Bare-product consequence for \(N\ge32\)

Use the exact derivative identity from
M10_BARE_PHASE_DERIVATIVE.md:
\[
 \partial_\theta\log T_n=-\beta S_n+\beta_\theta H_n.
\]
For \(\beta\in[.70,.72]\), \(\theta\in[.8,.9]\), and
\(n=N+1+K\), \(K\ge0\), the first two pre-crossing terms give
\[
 \beta S_n>\frac{1435}{342}>4.19. \tag{19}
\]
For \(0\le K\le60N\), the harmonic comparison there gives
\[
 |H_n|\le14+\log(2000N^2). \tag{20}
\]
The function in (20) divided by \(N^3\) is decreasing for \(N\ge32\).
Using \(\log(2000)<8\) and \(\log(32)<3.5\),
\[
 \frac{0.008}{N^3}\bigl(14+\log(2000N^2)\bigr)
 <\frac{0.008\cdot29}{32^3}<10^{-5}. \tag{21}
\]
Consequently, on this finite post-crossing window,
\[
 \boxed{\ \partial_\theta\log T_n<-4.19+10^{-5}<-4.18,
 \qquad N\ge32,\quad N+1\le n\le60N.\ } \tag{22}
\]

This remains a statement about the bare product.  It does not control the
\(\theta\)-derivatives of the kernel factor, regularized weights,
prefactors, or boundary terms, and it gives no monotonicity theorem for
the full phase function \(F_N\).

## Reproduction and scope

Run the following command:

    python3 -m proofs.m10_beta_real > /tmp/m10-beta-real.json

The checker returns status pass, certifies the derivative, beta-strip,
and coarse/sharp \(\beta_\theta\) claims, and records the exact I384 dyadic
intervals.  The JSON is an ad hoc output in /tmp, not a committed
result.  No held-out measurements or full-band scan are used.
