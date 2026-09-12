# M10: derivative of the bare phase product

Status: bounded exploratory lemma for the bare product only.  It does not
differentiate the full moment \(P_N,H_N\), and it does not imply a sign for
the phase function \(F_N\).  The smooth factor, the kernel product, the
weights, and the boundary terms all still depend on \(\theta\).

Let
\[
 a=N+\theta,\qquad b=a-\beta(e),\qquad
 \beta(e)=\eta_e=\frac{s_g(e)-s_g(-e)}e,
 \qquad e=e_N(\theta),
\]
and
\[
 T_0=1,\qquad
 T_{n+1}=\frac{a-n}{b-n}T_n,\qquad
 T_n=\prod_{j=0}^{n-1}\frac{a-j}{b-j}.
\]
The real phase interval is \(\theta\in[.8,.9]\).  Whenever
\(\beta\in[.70,.72]\), put
\[
 u=\theta,\qquad v=\theta-\beta.
\]
Then
\[
 .08\le v\le.20,\qquad
 a-j,\ b-j>0\ (0\le j\le N),\qquad
 a-j,\ b-j<0\ (j\ge N+1). \tag{1}
\]
Thus every denominator product \((a-j)(b-j)\) is positive, including on
the post-crossing side.  The strip condition is valid for the scalar
phase domain in M7_COMPLEX_SCALARS.md; the exact fixed-\(\beta\) identity
below only needs (1), so it applies for every \(N\ge32\) for which the
real phase and this beta strip have been established.

## 1. Exact product derivative

For a moment, hold \(\beta\) fixed while differentiating \(a\) and \(b\).
Termwise differentiation gives
\[
 \left.\partial_\theta\log T_n\right|_{\beta}
 =\sum_{j=0}^{n-1}
 \left(\frac1{a-j}-\frac1{b-j}\right)
 =-\beta S_n, \tag{2}
\]
where
\[
 S_n=\sum_{j=0}^{n-1}\frac1{(a-j)(b-j)}>0. \tag{3}
\]
This proves strict decrease of the bare product with \(\theta\) at fixed
\(\beta\), for every \(n\ge1\).

For the physical phase family, \(\beta\) also varies through \(e_N(\theta)\).
The chain rule gives the exact correction
\[
 \boxed{\;
 \partial_\theta\log T_n
 =-\beta S_n+\beta_\theta H_n,\qquad
 H_n=\sum_{j=0}^{n-1}\frac1{b-j},\qquad
 \beta_\theta=\beta'(e)e_\theta .
 \;} \tag{4}
\]
There is no sign conclusion in (4) until the second term is bounded.
Notice that \(H_n\) is a signed sum, whereas \(S_n\) is positive.

For \(n=N+1+K\), \(K\ge0\), the two sums have the explicit forms
\[
 S_n=
 \sum_{k=0}^{N}\frac1{(k+u)(k+v)}
 +\sum_{\ell=1}^{K}\frac1{(\ell-u)(\ell-v)}, \tag{5}
\]
\[
 H_n=
 \sum_{k=0}^{N}\frac1{k+v}
 \;-\sum_{\ell=1}^{K}\frac1{\ell-v}. \tag{6}
\]
The second sum in (5) is absent when \(K=0\).  The post-crossing product
itself is
\[
 T_{N+1+K}
 =T_{N+1}\prod_{\ell=1}^{K}
 \frac{\ell-u}{\ell-u+\beta}, \tag{7}
\]
so each additional post-crossing factor lies in \((0,1)\).

## 2. Uniform fixed-beta margin after the crossing

For \(n\ge N+1\), (5) contains the \(k=0,1\) terms.  Since
\[
 uv\le .9\cdot.20=.18,\qquad
 (1+u)(1+v)\le1.9\cdot1.2=2.28,
\]
\[
 S_n\ge\frac1{uv}+\frac1{(1+u)(1+v)}
 \ge\frac{50}{9}+\frac{25}{57}
 =\frac{1025}{171}. \tag{8}
\]
Consequently
\[
 \beta S_n\ge\frac7{10}\frac{1025}{171}
 =\frac{1435}{342}>4.19. \tag{9}
\]
This is an \(N\)- and \(n\)-independent negative margin for the
fixed-beta derivative.

The signed correction sum has a logarithmic bound on the finite window
used by the M7 tail ledger.  If \(0\le K\le60N\), monotone integral
comparison in (6) gives
\[
 \sum_{k=0}^{N}\frac1{k+v}
 \le\frac1v+\log\frac{N+v}{v}
 \le12.5+\log(25N), \tag{10}
\]
and, for \(K\ge1\),
\[
 \sum_{\ell=1}^{K}\frac1{\ell-v}
 \le\frac1{1-v}+\log\frac{K-v}{1-v}
 \le1.25+\log(75N). \tag{11}
\]
For \(K=0\), the right side of (11) is still a valid positive allowance.
Therefore
\[
 |H_n|\le14+\log(2000N^2),\qquad
 N+1\le n\le60N. \tag{12}
\]
The cruder constant \(2000\) absorbs
\(13.75+\log(1875N^2)\).

The real product envelope from M7_COMPLEX_PRODUCT_DOMINATION.md also
applies on this interval:
\[
 0<T_n\le
 300\left(\frac{N+\theta+1}{1+n-N-\theta}\right)^\beta,
 \qquad n\ge N+1. \tag{13}
\]
Equation (13) is only an envelope for \(T_n\); it is not a derivative
estimate.

## 3. The beta derivative from even analyticity

The exact root symmetry in M6_EFFECTIVE_PRODUCT.md is
\[
 s_h(e)=s_g(-e),\qquad
 \beta(e)=\frac{s_g(e)-s_g(-e)}e. \tag{14}
\]
Thus \(\beta\) is even and analytic at zero:
\[
 \beta(z)=\eta+\sum_{m\ge1}c_{2m}z^{2m}. \tag{15}
\]
M7_COMPLEX_SCALARS.md bounds the analytic quotient by \(20\) on
\(|z|=r_0=10^{-5}\).  By the maximum principle and Cauchy's coefficient
estimate,
\[
 |c_{2m}|\le\frac{20}{r_0^{2m}}.
\]
For \(|e|\le r_0/2\), summing the differentiated series gives
\[
 |\beta'(e)|
 \le\frac{40|e|}{r_0^2}
 \frac1{(1-|e|^2/r_0^2)^2}
 \le\frac{640}{9}\frac{|e|}{r_0^2}
 <7.12\cdot10^{11}|e|. \tag{16}
\]
This is the gain from evenness.  The one-sided Cauchy estimate
\(|\beta'(e)|=O(1)\) would be much weaker.

The exact phase-inverse derivative from M7 is
\[
 e_\theta=\frac{e^2}{e\,s_g'(e)-s_g(e)}. \tag{17}
\]
On the accepted M7 scalar domain the denominator is bounded away from
zero, and the recorded bound \(|e_\theta|\le20|e|^2\) applies.  Combining
(16)--(17) gives
\[
 |\beta_\theta|
 \le\frac{12800}{9r_0^2}|e|^3
 <1.43\cdot10^{13}|e|^3. \tag{18}
\]
For \(e=e_N(\theta)\) and \(e<1/N\), this becomes
\[
 |\beta_\theta|<\frac{1.43\cdot10^{13}}{N^3}. \tag{19}
\]
The scalar notes are scoped at \(N\ge10^{120}\), where all these
hypotheses certainly hold.  The phase-inverse contraction calculation
itself starts at \(N\ge10^6\); extending (18)--(19) to that smaller
threshold is conditional on accepting the same scalar boxes there.

## 4. Combined finite-window sign

Substituting (9), (12), and (19) into the exact identity (4) gives, for
\(N+1\le n\le60N\),
\[
 \partial_\theta\log T_n
 \le -4.19+
 \frac{1.43\cdot10^{13}}{N^3}
 \bigl(14+\log(2000N^2)\bigr). \tag{20}
\]
The factor multiplying \(N^{-3}\) decreases for \(N\ge10^6\), because
\[
 \frac{d}{dN}\left[
 \frac{14+\log(2000N^2)}{N^3}\right]
 =\frac{2-3(14+\log(2000N^2))}{N^4}<0.
\]
Using \(\log(2000)<8\) and \(\log(10)<2.303\), its value at
\(N=10^6\) is below \(50/10^{18}\).  Hence, on the conditional
\(N\ge10^6\) extension, and therefore on the accepted \(N\ge10^{120}\)
domain,
\[
 |\beta_\theta H_n|<7.2\cdot10^{-4},\qquad
 \boxed{\ \partial_\theta\log T_n<-4.18\ } \tag{21}
\]
throughout the finite post-crossing window.

For arbitrary \(n\), (6) instead gives the explicit bound
\[
 |H_n|
 \le12.5+\log(25N)
 +1.25+\log\!\left(\frac{\max(1,n-N-1)}{.8}\right). \tag{22}
\]
This grows like \(\log n\).  Therefore (21) has deliberately been
restricted to the finite window.  Without an independent sign for
\(\beta_\theta\), (4) does not prove a uniform sign for every
post-crossing index \(n\to\infty\): asymptotically the correction contains
\(-\beta_\theta\log n\).  If \(\beta_\theta=0\), the fixed-beta sign (2)
does hold for all \(n\).

## Remaining obligations

The result supplies an exact negative derivative margin for the bare
finite product on the M7-relevant finite window, conditional on the
accepted phase-scalar domain and the even root quotient.  It does not
establish any of the following:

1. monotonicity of the full \(P_N,H_N\) or of \(F_N\);
2. a sign for \(\beta_\theta\) beyond the absolute bound (18);
3. a uniform bare-product derivative sign for the infinite tail without
   using a tail-weighted argument;
4. the finite-\(N\) derivative contributions from \(K_n,V_j,z_0\), or the
   boundary terms.

A sharper real-only estimate for item 2 could start from the exact identity
\[
 \beta'(e)
 =e\int_{-1}^{1}r^2\int_0^1
 s_g'''(u r e)\,du\,dr, \tag{23}
\]
obtained by differentiating
\(\beta(e)=\int_{-1}^{1}s_g'(re)\,dr\) and subtracting the odd
zero-order term.  No interval bound for \(s_g'''\) has been established
here, so (18), rather than (23), is the quantitative input used above.

No numerical measurements or held-out \(N\) values are used.
