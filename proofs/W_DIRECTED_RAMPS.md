# The Bacher--Beaton partially directed-ramp term \(D_I\)

Status: **exact analytic lemma and reproducible checks**.  This note proves
the behavior of the partially directed term needed in the two-sided weakly
prudent bridge quotient.  It does not by itself prove non-D-finiteness of
\(W\).

The source is Bacher--Beaton, *Weakly prudent self-avoiding bridges*,
Proposition 8, pp. 830--831 of the archived 2014 paper.  In the source,
\(D(t)\) counts all (possibly reducible) partially directed ramps and
\(D_I(t)\) counts irreducible partially directed ramps.  Their equations are

\[
 D(t)=\sum_{k\geq 0}\frac{t^{k+1}}{G_k(t)},\qquad
 D_I(t)=\frac{D(t)}{1+D(t)},
\]

with

\[
 G_{-1}=1,\qquad G_0=1-t,\qquad
 G_k=(1-t+t^2+t^3)G_{k-1}-t^2G_{k-2}.
\tag{1}
\]

The \(D\) in this note is the source's generating function.  It should not be
confused with the auxiliary factor \(1-tq\) used in the prudent-ramp formulas.

## Physical kernel and exact closed form

Put

\[
 A(t)=1-t+t^2+t^3,
 \qquad
 q=U(t,1)=\frac{A(t)-\sqrt{A(t)^2-4t^2}}{2t}.
\]

For \(0<t<\sigma=\sqrt2-1\),

\[
 A(t)-2t=(t-1)(t^2+2t-1)>0,
\]

and

\[
 A(t)^2-4t^2=(t-1)(t+1)(t^2+1)(t^2+2t-1)>0.
\]

Thus the displayed square-root branch is real and \(0<q<1\).  Rationalizing
the definition of \(U\) gives the exact kernel equation

\[
 t\left(q+\frac1q\right)=A(t),
 \qquad
 tq^2-A(t)q+t=0.
\tag{2}
\]

The two characteristic roots of \((1)\) are \(tq\) and \(t/q\).  Define

\[
 \beta(t)=\frac{1-t-tq}{1-q^2},
 \qquad
 \gamma(t)=\frac{q\,[t-q(1-t)]}{1-q^2}.
\]

Then, for every integer \(k\geq -1\),

\[
 G_k(t)=\left(\frac tq\right)^k
       \left(\beta(t)+\gamma(t)q^{2k}\right).
\tag{3}
\]

At \(k=-1\) and \(k=0\), \((3)\) gives \(G_{-1}=1\) and \(G_0=1-t\).  Using
\((2)\), substitution of \((3)\) into \((1)\) gives the recurrence exactly.  The useful
form for the summand is therefore

\[
 \frac{t^{k+1}}{G_k(t)}
 =\frac{tq^k}{\beta(t)+\gamma(t)q^{2k}}.
\tag{4}
\]

For real \(0<t<\sigma\), \(\beta>0\), since

\[
 1-t-tq>1-2t>0,
\]

and

\[
 \beta+\gamma=1-t>0.
\]

As \(0<q^{2k}\leq 1\), the denominator in \((4)\) lies between the positive
numbers \(\beta\) and \(\beta+\gamma=1-t\), regardless of the sign of
\(\gamma\).  In particular \(G_k(t)>0\) for every \(k\geq-1\), so no real
denominator in the defining series vanishes.  With

\[
 m(t)=\min\{\beta(t),1-t\}>0,
\]

\((4)\) also gives the convergent geometric bound

\[
 0<\frac{t^{k+1}}{G_k(t)}\leq \frac{t}{m(t)}q^k.
\tag{5}
\]

Consequently \(D(t)\) is finite and positive on \(0<t<\sigma\), and

\[
 0<D_I(t)=\frac{D(t)}{1+D(t)}<1.
\]

## Local holomorphy and denominator control

Fix \(t_0\in(0,\sigma)\).  The discriminant in the definition of \(q\) is
nonzero at \(t_0\), so the physical branch \(q(t)\) extends holomorphically to
a sufficiently small complex disk \(V\) around \(t_0\).  Shrink \(V\) so that

\[
 |q(t)|\leq r<1,
 \qquad \inf_{t\in V}|\beta(t)|\geq b>0.
\]

The finitely many polynomials \(G_k\) with \(k<K\) have positive values at
\(t_0\); shrink \(V\) once more so that none of them vanishes there.  Since
\(\gamma\) is bounded on \(V\), choose \(K\) so large that

\[
 \sup_{t\in V}|\gamma(t)|r^{2K}\leq b/2.
\]

For \(k\geq K\), \((3)\) then implies

\[
 |\beta(t)+\gamma(t)q(t)^{2k}|\geq b/2,
\]

so all remaining \(G_k\) are nonzero on \(V\).  Formula \((4)\) gives the
uniform majorant

\[
 \left|\frac{t^{k+1}}{G_k(t)}\right|
 \leq \frac{2\sup_{V}|t|}{b}\,r^k
 \qquad(k\geq K).
\]

The Weierstrass \(M\)-test proves that the series for \(D\) converges locally
uniformly and defines a holomorphic function on \(V\).  Since \(D(t_0)>0\), a
final shrink of \(V\) ensures \(1+D(t)\neq0\), so \(D_I\) is holomorphic there
as well.  This proves holomorphy in a complex neighborhood of every real
\(t_0\in(0,\sigma)\), hence also real-analyticity throughout that interval.
On a compact subinterval of \((0,\sigma)\), finitely many such disks give
uniform local convergence.  No fixed complex neighborhood reaching
\(t=\sigma\) is asserted; the geometric margin \(r<1\) necessarily degrades
as \(t_0\uparrow\sigma\).

## Critical divergence

At \(\sigma=\sqrt2-1\), one has \(A(\sigma)=2\sigma\), so the characteristic
root in \((1)\) is repeated.  Solving the recurrence with the two initial values
gives, exactly,

\[
 G_k(\sigma)=\sigma^k\bigl[(1-\sigma)+(1-2\sigma)k\bigr].
\tag{6}
\]

Both \(a=1-\sigma\) and \(b=1-2\sigma\) are positive.  Hence the critical
partial sums are

\[
 S_K=\sum_{k=0}^{K}\frac{\sigma^{k+1}}{G_k(\sigma)}
 =\sum_{k=0}^{K}\frac{\sigma}{a+bk}.
\]

For \(k\geq1\),

\[
 \frac{\sigma}{(a+b)k}
 \leq \frac{\sigma}{a+bk}
 \leq \frac{\sigma}{bk}.
\]

Thus \(S_K=\Theta(\log K)\), in particular the critical series diverges.

This also gives the one-sided divergence needed below without assuming any
rate in \(\sigma-t\).  Let \(M>0\).  Choose a finite \(K\) with
\(S_K>M+1\).  Each \(G_k(\sigma)>0\), so the finite partial sum

\[
 S_K(t)=\sum_{k=0}^{K}\frac{t^{k+1}}{G_k(t)}
\]

is continuous at \(\sigma\) and \(S_K(t)>M\) for all real \(t<\sigma\)
sufficiently close to \(\sigma\).  Positivity from \((5)\) gives

\[
 D(t)\geq S_K(t)>M,
\]

and therefore

\[
 \lim_{t\uparrow\sigma}D(t)=+\infty,
 \qquad
 \lim_{t\uparrow\sigma}D_I(t)=1.
\tag{7}
\]

The finite-partial-sum argument is the required rigorous passage; no
unproved asymptotic relation between \(D(t)\) and \(\sigma-t\) is used.

## Uniformity on the critical phase families

The phase construction used for the prudent-ramp products sets

\[
 \epsilon=-\log(q^2),\qquad
 a(\epsilon)=\frac{s_g(\epsilon)}{\epsilon},\qquad
 a(\epsilon_N(\theta))=N+\theta,\qquad
 t_N(\theta)=t(\epsilon_N(\theta)).
\]

For every fixed compact phase set \({\cal T}\) on which this inverse is
defined, the established expansion

\[
 \epsilon_N(\theta)=\frac{s_*}{N}+O(N^{-2})
\]

is uniform in \(\theta\in{\cal T}\).  Since \(t(0)=\sigma\) and \(t(\epsilon)\)
is continuous (in fact real analytic) at zero,

\[
 \sup_{\theta\in{\cal T}}|t_N(\theta)-\sigma|\longrightarrow0.
\tag{8}
\]

Combining \((7)\) with \((8)\) yields the desired uniform limit.  Explicitly, given
\(\eta>0\), choose \(M>\max\{0,\eta^{-1}-1\}\).  The finite-partial-sum
argument gives \(\delta>0\) such that \(D(t)>M\) for every
\(t\in(\sigma-\delta,\sigma)\).  For all sufficiently large \(N\), \((8)\) puts
every \(t_N(\theta)\) in that
interval, and hence

\[
 \sup_{\theta\in{\cal T}}
 \left|D_I(t_N(\theta))-1\right|
 =\sup_{\theta\in{\cal T}}\frac1{1+D(t_N(\theta))}
 <\eta.
\tag{9}
\]

For the real phase family, all \(G_k(t_N(\theta))\) are strictly positive and
\(1+D(t_N(\theta))>1\).  Therefore neither the summand denominators nor the
\(D_I\) denominator has a zero along the family.  The local complex
holomorphy argument above applies at each family point; it is intentionally a
local statement and does not claim a fixed disk radius as \(N\to\infty\).

## Consequence for the bridge quotient

The source combines this term with the prudent-ramp quotient as

\[
 W=\frac{I}{1-I},\qquad I=4P_I-2D_I-t.
\]

Equation \((9)\) rigorously permits replacing \(D_I(t_N(\theta))\) by \(1\) in a
uniform limiting calculation.  It does not by itself produce zeros of
\(1-I\), nor does it prove that a prospective zero is not cancelled; those
are separate \(W\)-specific obligations.

## Reproducibility

Run the exact and bounded checks with:

```text
.venv/bin/python experiments/w_directed_ramps_check.py
```

The run verifies the cleared kernel relation, \((3)\)--\((4)\) for
\(k=1,\ldots,7\), the critical formula \((6)\) and its recurrence for the same
indices.  Critical
partial sums at \(K=10,100,1000,10000\) were respectively approximately

```text
3.76307132569128315577622055699
8.61671165481977029430006086236
14.0923709560635608945290475441
19.6428165057148324942657798782
```

At \(t=0.1,0.3,0.4,0.414\), the physical \(q\) values from the branch formula
were approximately \(0.1111250017580\), \(0.4374718218904\),
\(0.7832207464149\), \(0.9711850349200\); the 200-term partial sums of \(D\)
were approximately \(0.1250019319314\), \(0.7604563221472\),
\(2.7196140425532\), \(7.6015759772293\).  These are checks only; the proof
of \((7)\)--\((9)\) is analytic.

The source and input provenance for this note is:

| item | value |
|---|---|
| source commit | `c698d932ede87358382d20bdde2eded39a099241` |
| `NORMALIZATION.md` SHA-256 | `37849ff3ddc245d187c1418a75f4d2a65d438c1b181a3effa25dbfe0d5741ec7` |
| `NEXT.md` SHA-256 | `164b6d53249f592965fc9e8754496f8ddef2459f0ca498ad0d041e46de443321` |
| archived source text SHA-256 | `d9dfa12998b29a5e19fe1cb021f352debe3656a4e5a9a78767e2f29d60b1d865` |
| archived source PDF SHA-256 | `04205e9fafa5330cb518e4c22a3db6f5677cddc915342fae83acbe076039b2c0` |
| checker SHA-256 | `fe22d8c9555ed75fbfe028921078b8a4f6b385652d83a31543ddb78dfdeb258a` |
| checker stdout SHA-256 | `c11555317211ea1a0e5a2256349adc8f70fa2d28237055f8db265d6c86e90eb5` |
