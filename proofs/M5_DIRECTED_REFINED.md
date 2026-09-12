# M5: a uniform \(C^1\) bound for the directed term

This note supplies the parameter derivative needed after the logarithmic
estimate in `M5_DIRECTED_LOG.md`. The only phase input used here is the
certified interval statement in `proofs/m5_phase_domain.py`; that file is
owned by the parent task and is read-only for this subtask.

Put

\[
 \sigma=\sqrt2-1,
 \qquad F(t)=\frac{1-t+t^2+t^3}{t},
 \qquad F(t(\varepsilon))=2\cosh(\varepsilon/2),
 \qquad q=e^{-\varepsilon/2},\quad Q=q^2=e^{-\varepsilon}.
\]

For \(0<\varepsilon\le 1/10\), the relevant branch has

\[
 0.4\le t\le\sigma,
 \qquad
 \alpha=1-t-tq\ge\frac16,
 \qquad
 r=\frac t\alpha\le3,
 \qquad
 c=\frac{1-t}{\alpha}\le4.
\]

The exact recurrence solution gives

\[
 D(\varepsilon)=\sum_{k\ge0}d_k(\varepsilon),
 \qquad
 d_k=\frac{t(1-Q)q^k}
 {\alpha(1-Q^k)+(1-t)(1-Q)Q^k}.
 \tag{1}
\]

The \(k=0\) term is \(d_0=t/(1-t)\). For \(k\ge1\), set

\[
 x=\varepsilon k,
 \quad
 b(x)=\frac{x}{2\sinh(x/2)},
 \quad
 a(\varepsilon)=\frac{1-e^{-\varepsilon}}{\varepsilon},
 \quad
 w(x)=\frac1{e^x-1},
 \quad
 u_k=c(1-e^{-\varepsilon})w(x).
\]

Then (1) becomes

\[
 d_k=\frac{r\,a(\varepsilon)b(x)}{k(1+u_k)}.
 \tag{2}
\]

All quantities in (1)--(2) are positive on the real interval under
consideration. The tail estimate (13) supplies a summable derivative
majorant on every compact interval \([\varepsilon_0,1/10]\), with
\(\varepsilon_0>0\), and justifies termwise differentiation there.
The resulting bound (16) holds for every positive \(\varepsilon\) in the
stated range; no summable majorant uniform down to zero is asserted.

## Effective derivative estimate

Differentiation of \(F(t(\varepsilon))=2\cosh(\varepsilon/2)\) gives

\[
 t_\varepsilon=\frac{\sinh(\varepsilon/2)}{F'(t)},
 \qquad |t_\varepsilon|<\frac1{20}.
 \tag{3}
\]

Here \(F'(t)=1+2t-1/t^2\le -4\) on \(0.4\le t\le\sigma\). Since

\[
 q_\varepsilon=-q/2,
 \qquad
 \alpha_\varepsilon=-(1+q)t_\varepsilon-tq_\varepsilon,
\]

we have \(|\alpha_\varepsilon|<7/20\), and hence the deliberately coarse
bounds

\[
 |r_\varepsilon|<7,
 \qquad |c_\varepsilon|<13,
 \qquad |a_\varepsilon|<1.
 \tag{4}
\]

The elementary hyperbolic estimates used below are

\[
 0<b(x)\le1,
 \quad |b'(x)|\le1\quad(0\le x\le1),
 \tag{5}
\]

and, for \(x\ge1\),

\[
 b(x)\le2xe^{-x/2},
 \qquad |b'(x)|\le6(1+x)e^{-x/2}.
 \tag{6}
\]

For completeness, (5) follows by writing \(x=2y\), using

\[
 |b'(2y)|=
 \frac{2(y\cosh y-\sinh y)}{4\sinh^2y}
 \le\frac{y\cosh y}{4}\le1\quad(0\le y\le1/2),
\]

and (6) follows from
\(b(x)=xe^{-x/2}/(1-e^{-x})\), with \(1-e^{-x}\ge1/2\).
Also,

\[
 w(x)\le x^{-1},\quad |w'(x)|\le3x^{-2}\quad(0<x\le1),
 \tag{7}
\]

while

\[
 w(x)\le2e^{-x},\quad |w'(x)|\le4e^{-x}\quad(x\ge1).
 \tag{8}
\]

Let \(K=\lfloor1/\varepsilon\rfloor\). For \(1\le k\le K\), (7) and
(4) imply

\[
 u_k\le\frac4k,
 \qquad
 |(u_k)_\varepsilon|
 \le \frac{29}{\varepsilon k}.
 \tag{9}
\]

Differentiating (2), then using (4), (5), and (9), gives

\[
 |(d_k)_\varepsilon|
 \le \frac{10}{k}+3+\frac{90}{\varepsilon k^2}
 \qquad(1\le k\le K).                         
 \tag{10}
\]

Since \(\sum_{k\le K}k^{-2}<2\), \(K\le1/\varepsilon\), and
\(1+\log(1/\varepsilon)\le1/\varepsilon\) for \(\varepsilon\le1/10\),

\[
 \sum_{k=1}^K |(d_k)_\varepsilon|\le \frac{200}{\varepsilon}.
 \tag{11}
\]

For the tail \(k>K\), (8) gives

\[
 |(u_k)_\varepsilon|
 \le16(1+x)e^{-x},
 \qquad x=\varepsilon k,
 \tag{12}
\]

and differentiating (2) now gives

\[
 |(d_k)_\varepsilon|
 \le20\varepsilon e^{-x/2}
       +28(1+x)e^{-x/2}.                        
 \tag{13}
\]

The geometric estimates

\[
 \sum_{k>K}e^{-\varepsilon k/2}\le\frac4\varepsilon,
 \qquad
 \sum_{k>K}(1+\varepsilon k)e^{-\varepsilon k/2}
 \le\frac{36}{\varepsilon}
 \tag{14}
\]

follow from \(K\varepsilon>1-\varepsilon\),
\(1-e^{-y}\ge y/2\) for \(0<y\le1/2\), and
\(xe^{-x/2}\le4e^{-x/4}\). Consequently

\[
 \sum_{k>K}|(d_k)_\varepsilon|
 \le\frac{1020}{\varepsilon}.                
 \tag{15}
\]

The \(k=0\) derivative is bounded by \(1\), which is absorbed into the
same constant. Combining (11) and (15) proves the explicit estimate

\[
 \boxed{\quad |D_\varepsilon(\varepsilon)|\le
 \frac{1500}{\varepsilon},\qquad 0<\varepsilon\le\frac1{10}.\quad}
 \tag{16}
\]

The constant is intentionally generous. The proof only uses positive real
denominators and elementary geometric bounds, so (16) is an effective real
estimate rather than a formal asymptotic differentiation.

## Composition with the phase coordinate

Write \(s_g(\varepsilon)=-\log v_g(\varepsilon)\) for the phase coordinate
of the prudent kernel zero \(g=0\), and

\[
 a_g(\varepsilon)=\frac{s_g(\varepsilon)}{\varepsilon}.
\]

The exact interval certificate in `proofs/m5_phase_domain.py` gives, for
\(0<\varepsilon\le1/100\) and \(\theta\in[4/5,9/10]\), the recorded
enclosures are

\[
 s_g\in\left[\frac{15330489}{10^8},\frac{16692269}{10^8}\right],
 \qquad
 s_g'\in\left[\frac{4212409}{12500000},
                    \frac{36785089}{10^8}\right],
 \qquad
 s_g-\varepsilon s_g'\ge\frac{7481319}{5\cdot10^7}.
\]

In particular,

\[
 \frac{s_*}{2}\le s_g\le2s_*,
 \qquad |s_g'|<2,
 \qquad s_g-\varepsilon s_g'>\frac1{20},
 \tag{17}
\]

where \(s_*=s_g(0)=0.158\ldots\). Since

\[
 a_g'(\varepsilon)=
 \frac{\varepsilon s_g'(\varepsilon)-s_g(\varepsilon)}{\varepsilon^2},
\]

the inverse phase branch satisfies

\[
 \left|\frac{d\varepsilon_N}{d\theta}\right|
 =\frac{\varepsilon_N^2}{s_g-\varepsilon_Ns_g'}
 \le20\varepsilon_N^2.                         
 \tag{18}
\]

For \(N\ge20\), the same certificate places
\(\varepsilon_N\le1/100\) and \(N\varepsilon_N/s_*<2\). As \(2s_*<1\),

\[
 \varepsilon_N<\frac1N.                         
 \tag{19}
\]

Combining (16), (18), and (19),

\[
 |\partial_\theta D(\varepsilon_N(\theta))|
 \le30000\varepsilon_N\le\frac{30000}{N}.      
 \tag{20}
\]

Finally \(D_I=D/(1+D)\), so positivity of \(D\) gives

\[
 \boxed{\quad
 |\partial_\theta D_I(t_N(\theta))|
 =\frac{|\partial_\theta D|}{(1+D)^2}
 \le\frac{30000}{N}\xrightarrow[N\to\infty]{}0,
 \quad \theta\in[4/5,9/10].\quad}              
 \tag{21}
\]

If the logarithmic lower bound from `M5_DIRECTED_LOG.md` is also inserted,
then for the certified large-\(N\) range one may multiply the right side of
(20) by \(4\sigma^2/(\log N)^2\). The weaker bound (21) already gives the
uniform \(C^1\) convergence required for the phase-family residue argument.

## Hyperbolic rewrite: status of the additive constant

There is an exact useful rewrite, but the sharper additive constant is not
needed for (21). With

\[
 z=-\frac\beta\alpha,
 \qquad a_\varepsilon=-\frac{\log z}{\varepsilon},
 \qquad
 \beta=q\,[t-q(1-t)],
\]

whenever \(0<z<1\), (1) is exactly

\[
 D=\frac t\alpha e^{\varepsilon a_\varepsilon/2}(1-e^{-\varepsilon})
 \sum_{k\ge0}\frac1{2\sinh(\varepsilon(k+a_\varepsilon)/2)}. 
 \tag{22}
\]

The formal regularized-sum calculation suggested by (22) is

\[
 D\stackrel{?}=\frac1\sigma
 \left[\log\frac1\varepsilon+\log4
       -\psi(2+\sqrt2)\right]+O(\varepsilon\log(1/\varepsilon)),
 \tag{23}
\]

where \(\psi\) is the digamma function. Equation (23) is recorded as a
conjectural refinement only: this file does not use it, and no claim of an
effective remainder or of the constant in (23) is made here.

## Provenance

The recurrence and \(D_I=D/(1+D)\) are the BB2014 directed-bridge formulas
recorded in `proofs/W_DIRECTED_RAMPS.md`. The exact phase margins in (17)
come from the parent-owned `proofs/m5_phase_domain.py`. The working tree
source revision inspected for this note was
`106db6d44466ef82d57ecbc44e83a8c224b655f7`.
