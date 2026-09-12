# Quantitative logarithmic growth of the partially directed term

Status: **effective logarithmic bound; uniform phase corollary conditional on
the existing phase inversion**.  This note concerns only the Bacher--Beaton
partially directed-ramp series \(D\) and \(D_I=D/(1+D)\).  It does not address
the prudent moments \(P,H\).

In the notation of the new goal, \(R(t)=D(t)\).

The exact source formulas are Bacher--Beaton (2014), Proposition 8:

\[
 D(t)=\sum_{k\geq0}\frac{t^{k+1}}{G_k(t)},\qquad
 D_I(t)=\frac{D(t)}{1+D(t)},
\]

\[
 G_{-1}=1,\qquad G_0=1-t,\qquad
 G_k=(1-t+t^2+t^3)G_{k-1}-t^2G_{k-2}.
\tag{1}
\]

The preceding exact closed form gives, with \(q=U(t,1)\),

\[
 \frac{t^{k+1}}{G_k(t)}
 =\frac{tq^k}{\beta_{\rm n}+\gamma_{\rm n}q^{2k}},
\quad
 \beta_{\rm n}=\frac{1-t-tq}{1-q^2},
\quad
 \gamma_{\rm n}=\frac{q[t-q(1-t)]}{1-q^2}.
\tag{2}
\]

The subscript \({\rm n}\) distinguishes these normalized coefficients from
the unnormalized coefficients below.

## Exact reparametrization

Set

\[
 \varepsilon=-\log(q^2),\qquad
 Q=q^2=e^{-\varepsilon},\qquad
 s=1-Q,
\]

and write

\[
 \alpha=1-t-tq,\qquad
 \beta=q[t-q(1-t)].
\]

The identity

\[
 \alpha+\beta=(1-t)(1-Q)
\tag{3}
\]

turns (2) into

\[
 D(t)=\sum_{k\geq0}
 \frac{t\,s\,q^k}{\alpha(1-Q^k)+(1-t)sQ^k}.
\tag{4}
\]

Define

\[
 r=\frac{t}{\alpha},\qquad c=\frac{1-t}{\alpha}.
\]

Then the \(k\)-th summand in (4) is

\[
 d_k=r\,\frac{s q^k}{1-Q^k+c\,sQ^k}.
\tag{5}
\]

For \(k=0\), \(d_0=r/c=t/(1-t)\).

## Explicit parameter bounds

The kernel equation implies

\[
 F(t):=\frac1t-1+t+t^2=q+\frac1q=2\cosh(\varepsilon/2).
\tag{6}
\]

For \(0<\varepsilon\leq1/10\), the physical solution satisfies

\[
 \frac25<t<\sigma=\sqrt2-1,\qquad
 0<\sigma-t\leq\frac{\varepsilon^2}{8}.
\tag{7}
\]

Here is an elementary verification.  On \([2/5,\sigma]\),
\[
 F'(t)=-\frac1{t^2}+1+2t\leq F'(\sigma)=-4,
\]
because \(F''(t)=2/t^3+2>0\).  Also \(F(2/5)=103/50\), while
\[
 2(\cosh(\varepsilon/2)-1)
 \leq \frac{\varepsilon^2}{4}\cosh(\varepsilon/2)
 <\frac1{200}
 <\frac3{50}=F(2/5)-2.
\]
Thus (6) has its physical root in \((2/5,\sigma)\).  The mean-value theorem
and \(\cosh(\varepsilon/2)<2\) then give
\[
 4(\sigma-t)\leq F(t)-F(\sigma)
 \leq\frac{\varepsilon^2}{2}.
\]

Since \(q<1\), \(t<\sigma<1/2\), and
\(1-2\sigma=\sigma^2>1/6\), (7) gives

\[
 \alpha\geq1-2\sigma=\sigma^2>\frac16,\qquad
 0<c<4,\qquad 0<r<3,\qquad 0<d_0<1.
\tag{8}
\]

Moreover,
\[
 r-\frac1\sigma=\frac{\sigma t-\alpha}{\sigma\alpha},
\qquad
 \sigma t-\alpha=t(1+\sigma+q)-1.
\]
Using \(1-q\leq\varepsilon/2\), \(\sigma>2/5\), and (7),
\[
 |\sigma t-\alpha|
 \leq 3(\sigma-t)+t(1-q)
 \leq \frac{3\varepsilon^2}{8}+\frac{\varepsilon}{4}
 \leq\frac{23}{80}\varepsilon.
\]
Since \(\sigma\alpha>1/15\), this yields the effective estimate

\[
 \left|r-\frac1\sigma\right|\leq5\varepsilon.
\tag{9}
\]

## Harmonic comparison

Introduce the unregularized sum

\[
 H(\varepsilon)=\sum_{k\geq1}h_k,\qquad
 h_k=\frac{s q^k}{1-Q^k}.
\tag{10}
\]

Let \(K=\lfloor1/\varepsilon\rfloor\), so
\(1/(2\varepsilon)\leq K\leq1/\varepsilon\).  For \(1\leq k\leq K\),
put \(x=\varepsilon k\leq1\).  Then

\[
 h_k=\frac{a_\varepsilon b(x)}{k},\qquad
 a_\varepsilon=\frac{1-e^{-\varepsilon}}{\varepsilon},\qquad
 b(x)=\frac{x e^{-x/2}}{1-e^{-x}}
     =\frac{x}{2\sinh(x/2)}.
\tag{11}
\]

The elementary inequalities

\[
 0\leq1-a_\varepsilon\leq\frac{\varepsilon}{2},
 \qquad
 0\leq1-b(x)\leq\frac{x^2}{4}\quad(0\leq x\leq1)
\tag{12}
\]

are sufficient.  The first follows from
\(1-e^{-\varepsilon}\geq\varepsilon-\varepsilon^2/2\).  For the second,
\(\sinh(x/2)\leq(x/2)\cosh(x/2)\), and
\(\cosh(x/2)-1\leq x^2\cosh(x/2)/8\leq x^2/4\).

Therefore

\[
 0\leq\frac1k-h_k
 \leq\frac{\varepsilon}{2k}+\frac{\varepsilon^2 k}{4}.
\]

Using \(\sum_{k\leq K}1/k\leq1+\log K\),
\(\varepsilon(1+\log(1/\varepsilon))\leq1\), and
\(\varepsilon^2K(K+1)\leq1+\varepsilon\), we obtain

\[
 0\leq\sum_{k=1}^{K}\left(\frac1k-h_k\right)<1.
\tag{13}
\]

For the tail, \(k>K\) implies \(\varepsilon k>1\), so
\[
 \sum_{k>K}h_k
 \leq\frac{\varepsilon}{1-e^{-1}}
       \frac{q^{K+1}}{1-q}
 \leq 8.
\tag{14}
\]
The last inequality uses \(1-q=1-e^{-\varepsilon/2}\geq\varepsilon/4\)
and \(1-e^{-1}\geq1/2\).

The harmonic estimates
\(\log K\leq\sum_{k\leq K}1/k\leq1+\log K\) and
\(\log(1/(2\varepsilon))\leq\log K\leq\log(1/\varepsilon)\), together with
(13)--(14), give the explicit bound

\[
 \left|H(\varepsilon)-\log\frac1\varepsilon\right|\leq9
 \qquad(0<\varepsilon\leq1/10).
\tag{15}
\]

## The regularization error

From (5) and (10), write exactly

\[
 D(t)=d_0+r\,[H(\varepsilon)-E(\varepsilon)],
\]

where

\[
 E(\varepsilon)=
 \sum_{k\geq1}h_k
 \frac{c\,sQ^k}{1-Q^k+c\,sQ^k}.
\tag{16}
\]

Every term of \(E\) is nonnegative.  For \(1\leq k\leq K\),
\[
 1-Q^k=s\sum_{j=0}^{k-1}Q^j\geq skQ^{k-1},
\]
so \(c\,sQ^k/(1-Q^k)\leq4/k\).  Since \(h_k\leq1/k\),
\[
 \sum_{k=1}^{K}h_k
 \frac{c\,sQ^k}{1-Q^k+c\,sQ^k}
 \leq4\sum_{k=1}^{K}\frac1{k^2}
 <\frac{20}{3}.
\]
The tail is bounded by (14), because the fraction in (16) is at most one.
Consequently

\[
 0\leq E(\varepsilon)<15.
\tag{17}
\]

Combining (8), (9), (15), (17), and
\(\varepsilon\log(1/\varepsilon)\leq1\), we obtain

\[
\begin{aligned}
\left|D(t(\varepsilon))
 -\frac1\sigma\log\frac1\varepsilon\right|
 &\leq d_0
 +\left|r-\frac1\sigma\right|\log\frac1\varepsilon
 +r\left|H-\log\frac1\varepsilon\right|
 +rE\\
 &<1+5+3\cdot9+3\cdot15<80.
\end{aligned}
\tag{18}
\]

Thus, with a completely explicit domain and constant,

\[
 \boxed{\displaystyle
 \left|D(t(\varepsilon))
 -\frac1\sigma\log\frac1\varepsilon\right|\leq80
 \quad(0<\varepsilon\leq1/10).}
\tag{19}
\]

This proves \(D(t(\varepsilon))=(1/\sigma)\log(1/\varepsilon)+O(1)\).
The additive limit constant is not identified here; (19) is an effective
uniform enclosure.

## Uniform phase consequence

Let \({\cal T}=[4/5,9/10]\) and let \(t_N(\theta)\) be the existing phase
family.  Its previously established inversion gives, uniformly on
\({\cal T}\),

\[
 \varepsilon_N(\theta)=\frac{s_*}{N}+O(N^{-2}),
\qquad
 s_*=-\log\left(\frac12+\frac{\sqrt2}{4}\right)>0.
\tag{20}
\]

Therefore, for some phase threshold \(N_{\rm ph}\),
\[
 \frac12\leq\frac{N\varepsilon_N(\theta)}{s_*}\leq2
 \qquad(N\geq N_{\rm ph},\ \theta\in{\cal T}),
\]
and hence

\[
 \left|\log\frac1{\varepsilon_N(\theta)}-\log N\right|\leq3.
\tag{21}
\]

The value \(3\) is explicit; the threshold \(N_{\rm ph}\) is inherited from
the prior phase-inversion proof and is not made effective in this subtask.
Combining (19) and (21), for \(N\geq N_{\rm ph}\),

\[
 \left|D(t_N(\theta))-\frac1\sigma\log N\right|
 \leq C_*:=80+\frac3\sigma<88.
\tag{22}
\]

Since \(1-D_I=1/(1+D)\), put \(L_N=\log N\).  Whenever
\(L_N\geq2\sigma(1+C_*)\), (22) gives
\(1+D\geq L_N/(2\sigma)\), and therefore

\[
 \left|
 1-D_I(t_N(\theta))-\frac{\sigma}{L_N}
 \right|
 \leq\frac{2\sigma^2(1+C_*)}{L_N^2}
 <\frac{31}{L_N^2}.
\tag{23}
\]

Thus, uniformly for \(\theta\in[4/5,9/10]\),

\[
 \boxed{\displaystyle
 1-D_I(t_N(\theta))
 =\frac{\sigma}{\log N}+O\!\left(\frac1{\log^2N}\right),}
\]

with the displayed constant \(31\) and an explicit logarithmic threshold,
apart from the inherited non-effective value of \(N_{\rm ph}\).

## Independent numerical check

The checker experiments/m5_directed_log_check.py solves (6) by bisection and
evaluates (4) through a cutoff \(K_{40}=\lceil40/\varepsilon\rceil\).  For
the omitted tail it uses

\[
 \sum_{k>K_{40}}d_k
 \leq
 \frac{t\,s\,q^{K_{40}+1}}
 {\alpha(1-Q^{K_{40}+1})(1-q)}.
\tag{24}
\]

This is a high-precision numerical check rather than directed interval
arithmetic.  For \(\varepsilon=0.1,0.05,0.02,0.01,0.005,0.002\), the computed
enclosures for
\(D-(1/\sigma)\log(1/\varepsilon)\) were respectively

\[
 [0.7703303390,0.7703303473],\
 [0.7581039969,0.7581040061],\
 [0.7539481707,0.7539481803],\
 [0.7532345509,0.7532345607],\
 [0.7530319780,0.7530319879],\
 [0.7529679391,0.7529679491].
\]

All lie far inside the effective \([-80,80]\) enclosure and display the
predicted logarithmic coefficient \(1/\sigma\).

Provenance:

| item | value |
|---|---|
| source commit | 2893bbe27f2e65449bfc345c9f7a874faa185129 |
| NORMALIZATION.md SHA-256 | 37849ff3ddc245d187c1418a75f4d2a65d438c1b181a3effa25dbfe0d5741ec7 |
| NEXT.md SHA-256 | 164b6d53249f592965fc9e8754496f8ddef2459f0ca498ad0d041e46de443321 |
| archived source text SHA-256 | d9dfa12998b29a5e19fe1cb021f352debe3656a4e5a9a78767e2f29d60b1d865 |
| archived source PDF SHA-256 | 04205e9fafa5330cb518e4c22a3db6f5677cddc915342fae83acbe076039b2c0 |
| checker SHA-256 | 8f691353245f84dd4c89fb188f521c7228ed1dca4faceb645e2c906fbebb1375 |
| checker stdout SHA-256 | 312124d4f8ab994c1ee1e557470273440f902b2f2498563c33c8f609796f68eb |
