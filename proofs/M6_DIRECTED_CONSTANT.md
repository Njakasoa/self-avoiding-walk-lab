# M6: the additive constant of the directed logarithm

This note proves the additive constant in the directed term and gives an
effective remainder.  It changes no earlier source file.  Write
\[
 \sigma=\sqrt2-1,\qquad c=2+\sqrt2,\qquad
 \varepsilon=-\log(q^2),\qquad q=e^{-\varepsilon/2}.
\]
The result below is uniform for \(0<\varepsilon\le10^{-2}\):
\[
 \boxed{\displaystyle
 D(t(\varepsilon))
 =\frac1\sigma\left[
 \log\frac1\varepsilon+\log4-\psi(c)\right]
 +R(\varepsilon),\qquad
 |R(\varepsilon)|\le100\,\varepsilon\log\frac1\varepsilon .}
 \tag{1}
\]
Here \(\psi=\Gamma'/\Gamma\).  In particular, the conjectural constant in
the preceding directed note is correct.

## Exact hyperbolic form

Use
\[
 \alpha=1-t-tq,\qquad
 \beta=q[t-q(1-t)],\qquad r=\frac t\alpha,\qquad
 s=1-e^{-\varepsilon}.
\]
The exact directed summand is
\[
 D=\sum_{k\ge0}\frac{t\,s\,q^k}{\alpha+\beta q^{2k}}.
 \tag{2}
\]
For \(0<\varepsilon\le10^{-2}\), \(\alpha>0\), \(\beta<0\), and
\(\alpha+\beta=(1-t)s>0\).  Hence \(z=-\beta/\alpha\in(0,1)\).  Define
\[
a_\varepsilon=-\frac{\log z}{\varepsilon}.
\]
For completeness, the sign assertion follows from \(q>e^{-0.005}>0.99\),
\(t<\sigma<0.42\), and
\(q(1-t)-t>0.99(1-0.42)-0.42>0\), while
\(\alpha>1-0.42(1+e^{0.005})>1/7\).  The identity
\(\alpha+\beta=(1-t)(1-q^2)\) then gives \(z<1\).
Since
\[
 z=q^2\frac{\alpha(-\varepsilon)}{\alpha(\varepsilon)},
 \tag{3}
\]
where \(t(-\varepsilon)=t(\varepsilon)\) and
\(q(-\varepsilon)=q(\varepsilon)^{-1}\), one has
\[
 a_\varepsilon
 =1+\frac{\log\alpha(\varepsilon)-\log\alpha(-\varepsilon)}
          {\varepsilon}.
 \tag{4}
\]
The denominator in (2) is
\(\alpha[1-\exp(-\varepsilon(k+a_\varepsilon))]\).  With
\[
 f(x)=\frac1{2\sinh(x/2)},
 \]
equation (2) is therefore exactly
\[
 D=P(\varepsilon)\,S(\varepsilon,a_\varepsilon),\qquad
 P(\varepsilon)=r\,e^{\varepsilon a_\varepsilon/2}
                    \frac{1-e^{-\varepsilon}}{\varepsilon},
 \tag{5}
\]
\[
 S(\varepsilon,a)=
 \varepsilon\sum_{k\ge0} f(\varepsilon(k+a)).
 \tag{6}
\]

## Effective parameter bounds

The kernel equation is
\[
 F(t):=\frac1t-1+t+t^2=2\cosh(\varepsilon/2).
 \tag{7}
\]
For \(0<|\varepsilon|\le10^{-2}\), the physical even branch satisfies
\(2/5<t<\sigma\); at \(\varepsilon=0\), \(t=\sigma\), and the weak
versions of all bounds below still hold.  On this interval
\[
 |F'(t)|\ge4,\qquad F''(t)<34,\qquad |F'''(t)|<235.
\]
Implicit differentiation of (7), using
\(|\sinh(\varepsilon/2)|<0.006\), gives the deliberately coarse bounds
\[
 |t'|<\frac1{100},\qquad |t''|<\frac15,\qquad |t'''|<\frac1{10}.
 \tag{8}
\]
More explicitly, with \(R(\varepsilon)=2\cosh(\varepsilon/2)\),
\[
t'=\frac{R'}{F'},\quad
t''=\frac{R''-F''(t')^2}{F'},\quad
t'''=\frac{R'''-F'''(t')^3-3F''t't''}{F'}.
\]
Here \(|R'|<0.006,\ |R''|<0.501,\ |R'''|<0.0013\); therefore the
displayed bounds follow respectively from
\[
\frac{0.006}{4}<0.01,\qquad
\frac{0.501+34(0.01)^2}{4}<0.13<0.2,\qquad
\frac{0.0013+235(0.01)^3+3(34)(0.01)(0.2)}{4}<0.052<0.1.
\]
Also \(e^{-0.005}<q<e^{0.005}\), so
\[
 \alpha(\varepsilon)> \frac17,\quad
 |\alpha'|<\frac{11}{20},\quad
 |\alpha''|<\frac34,\quad
 |\alpha'''|<\frac32.
 \tag{9}
\]
These follow by differentiating
\(\alpha=1-t(1+q)\), with
\(|q'|<1,|q''|<1,|q'''|<1\), and inserting (8).
For example, using \(q<1.01\), \(|q'|<0.51\), \(|q''|<0.26\),
and \(|q'''|<0.13\), the three right-hand sides are bounded by
\[
2.01(0.01)+0.42(0.51)<0.24,\quad
2.01(0.2)+2(0.01)(0.51)+0.42(0.26)<0.53,
\]
\[
2.01(0.1)+3(0.2)(0.51)+3(0.01)(0.26)+0.42(0.13)<0.57,
\]
which are below the constants in (9).

For \(L(\varepsilon)=\log\alpha(\varepsilon)\), (9) gives
\[
 |L'''|
 \le\frac{3/2}{1/7}
 +\frac{3(11/20)(3/4)}{(1/7)^2}
 +\frac{2(11/20)^3}{(1/7)^3}
 <200.                                                     \tag{10}
\]
At zero, \(\alpha(0)=\sigma^2\), \(\alpha'(0)=\sigma/2\), hence
\[
 L'(0)=\frac1{2\sigma}.
 \]
Taylor's formula applied to (4), with the two third-order remainders,
therefore yields
\[
 |a_\varepsilon-c|\le\frac{200}{3}\varepsilon^2
 <67\varepsilon^2,\qquad
 3<a_\varepsilon<4.                                      \tag{11}
\]

The earlier elementary directed bound gives
\[
 \left|r-\frac1\sigma\right|\le5\varepsilon.              \tag{12}
\]
Since \(3<a_\varepsilon<4\), \(\varepsilon\le10^{-2}\), and
\[
 \left|\frac{1-e^{-\varepsilon}}{\varepsilon}-1\right|
 \le\frac{\varepsilon}{2},\qquad
 \left|e^{\varepsilon a_\varepsilon/2}-1\right|
 \le3\varepsilon,
\]
we have
\[
 \left|P(\varepsilon)-\frac1\sigma\right|\le25\varepsilon.
 \tag{13}
\]
Indeed, if \(A=e^{\varepsilon a_\varepsilon/2}(1-e^{-\varepsilon})/\varepsilon\),
then \(A<2\) and \(|A-1|<4\varepsilon\), so (12) gives
\(|P-1/\sigma|\le10\varepsilon+3\cdot4\varepsilon<25\varepsilon\).

## The regularized hyperbolic sum

Set
\[
 g(x)=f(x)-\frac{e^{-x}}x,\qquad g(0)=1.
 \tag{14}
\]
The function \(g\) is positive and decreasing on \([0,\infty)\).  To prove
the monotonicity, for \(x>0\),
\[
 -f'(x)=\frac{\cosh(x/2)}{4\sinh^2(x/2)}
 \ge\frac1{x^2\cosh(x/2)}.
 \]
The power-series coefficients of
\[
 e^x-(1+x)\cosh(x/2)
\]
are nonnegative: for even powers this is immediate, while the coefficient
of \(x^{2m+1}\), \(m\ge1\), is positive because \(4^m>2m+1\).
Thus \(e^x\ge(1+x)\cosh(x/2)\), and
\[
 g'(x)=f'(x)+e^{-x}\left(\frac1x+\frac1{x^2}\right)\le0.
 \tag{15}
 \]
The limits \(g(0)=1\) and \(g(\infty)=0\) follow from the elementary
Taylor expansions of \(\sinh\) and \(e^{-x}\).

The integral of \(g\) is exact.  For \(\delta>0\),
\[
 \int_\delta^\infty f(x)\,dx=-\log\tanh(\delta/4),
\]
while \(\int_\delta^\infty e^{-x}dx/x=E_1(\delta)\).  The standard
Euler-limit identity
\[
 E_1(\delta)+\gamma+\log\delta\longrightarrow0
 \quad(\delta\downarrow0)
\]
and \(-\log\tanh(\delta/4)+\log\delta\to\log4\) give
\[
 \int_0^\infty g(x)\,dx=\log4+\gamma.                    \tag{16}
\]

For \(3\le a\le4\), monotonicity gives a shifted rectangle estimate:
\[
 0\le
 \varepsilon\sum_{k\ge0}g(\varepsilon(k+a))
 -\int_{\varepsilon a}^\infty g(x)\,dx
 \le\varepsilon.
\]
The omitted interval \([0,\varepsilon a]\) has integral at most
\(4\varepsilon\).  Consequently
\[
 \left|
 \varepsilon\sum_{k\ge0}g(\varepsilon(k+a))
 -(\log4+\gamma)\right|\le5\varepsilon.                  \tag{17}
\]

## The exponential harmonic part

Define
\[
 A(\varepsilon,a)=
 \sum_{k\ge0}\frac{e^{-\varepsilon(k+a)}}{k+a}
 =\int_\varepsilon^\infty
 \frac{e^{-au}}{1-e^{-u}}\,du.                            \tag{18}
\]
The Euler-product integral for the digamma function is
\[
 \psi(a)+\gamma
 =\int_0^\infty\frac{e^{-u}-e^{-au}}{1-e^{-u}}\,du.
 \tag{19}
\]
Subtracting the \(a=1\) case in (18), the omitted interval
\([0,\varepsilon]\) has absolute integrand at most \(6\): indeed
\[
 \frac{|e^{-au}-e^{-u}|}{1-e^{-u}}
 \le\frac{3u}{u/2}\le6
 \qquad(0<u\le10^{-2},\ 3\le a\le4).
\]
Also
\[
 \left|-\log(1-e^{-\varepsilon})-\log\frac1\varepsilon\right|
 \le\varepsilon.
\]
Indeed, \(1-\varepsilon/2\le(1-e^{-\varepsilon})/\varepsilon\le1\),
and \(-\log(1-\varepsilon/2)\le\varepsilon\) on
\(0<\varepsilon\le10^{-2}\).
Thus
\[
 \left|
 A(\varepsilon,a)
 -\left(\log\frac1\varepsilon-\psi(a)-\gamma\right)
 \right|\le7\varepsilon.                                \tag{20}
\]

Since \(f=e^{-x}/x+g\), (17) and (20) give
\[
 \left|
 S(\varepsilon,a)
 -\left(\log\frac1\varepsilon+\log4-\psi(a)\right)
 \right|\le12\varepsilon.                               \tag{21}
\]

The trigamma series implies, for \(x\ge3\),
\[
 0<\psi'(x)=\sum_{j\ge0}\frac1{(x+j)^2}
 \le\frac1{x^2}+\frac1x<\frac49.
\]
Combining this with (11),
\[
 |\psi(a_\varepsilon)-\psi(c)|<30\varepsilon^2\le0.3\varepsilon,
\]
so the \(12\varepsilon\) error in (21) is at most \(12.3\varepsilon<13\varepsilon\),
and (21) becomes
\[
 \left|
 S(\varepsilon,a_\varepsilon)
 -\left(\log\frac1\varepsilon+\log4-\psi(c)\right)
 \right|\le13\varepsilon.                               \tag{22}
\]

## Assemble the constant and the effective remainder

Let \(L=\log(1/\varepsilon)\) and
\(C_0=\log4-\psi(c)\).  Since \(3<c<4\),
\(|\psi(c)|<2\), hence \(|C_0|<4\).  For \(L\ge4\), (22) gives
\[
 \left|S(\varepsilon,a_\varepsilon)\right|\le3L.
\]
Using (13), (22), and \(1/\sigma<3\),
\[
\begin{aligned}
 \left|D-
 \frac1\sigma(L+C_0)\right|
 &\le25\varepsilon\,|S|
 +\frac1\sigma\,13\varepsilon\\
 &\le75\varepsilon L+39\varepsilon
 \le100\varepsilon L.
\end{aligned}
\]
This proves (1), with no unquantified limit exchange.

## Independent check

The companion script
experiments/m6_directed_constant_check.py evaluates the exact
hyperbolic partial sum, an explicit positive tail bound, the digamma
constant, and the resulting upper enclosure for the normalized residual
\[
 \frac{\max_{x\in[D_-,D_+]}
 \left|x-(\log(1/\varepsilon)+\log4-\psi(c))/\sigma\right|}
      {\varepsilon\log(1/\varepsilon)}.
\]
It also checks the exact identity (5) against the original summand formula
on the partial sums.  Here \([D_-,D_+]\) is the interval formed by the
partial sum and its positive tail bound.
The script is diagnostic; the inequalities above are the proof.

## Provenance

The exact recurrence and reparametrization are the BB2014 formulas recorded
in M5_DIRECTED_LOG.md.  The source revision inspected for this note is
106db6d44466ef82d57ecbc44e83a8c224b655f7.

| input or output | SHA-256 |
|---|---|
| NORMALIZATION.md | 37849ff3ddc245d187c1418a75f4d2a65d438c1b181a3effa25dbfe0d5741ec7 |
| NEXT.md | 164b6d53249f592965fc9e8754496f8ddef2459f0ca498ad0d041e46de443321 |
| references/bacher-beaton-2014.txt | d9dfa12998b29a5e19fe1cb021f352debe3656a4e5a9a78767e2f29d60b1d865 |
| papers/bacher-beaton-2014.pdf | 04205e9fafa5330cb518e4c22a3db6f5677cddc915342fae83acbe076039b2c0 |
| experiments/m6_directed_constant_check.py | 09fea1a4590b029da58a7c38766e1a1bb78de6cb4087fd317e58e39b36302b5c |
