# M7 finite W pole certificates

Status: **candidate finite exact interval certificate, pending independent
replay/review** for the six already observed
indices \(N=32,64,128,256,512,1024\). The decimal values in the older M5/M6
diagnostic receipts are used only to choose small rational seed brackets. The
signs, phase coordinates, moments, directed term, and tails are recomputed by
`proofs/m7_finite_poles.py` with 384-bit outward dyadic intervals. This file
does not assert a unique zero in any bracket and does not cover intervening
indices.

## Exact finite construction

For a rational `t` below \(\sigma=\sqrt2-1\), set

\[
 q=U(t,1),\quad C=q-t,\quad D=1-tq,\quad E=1-q^2,
 \quad \delta={t^2E\over C},\quad r={qC\over D},
\]

where

\[
 U(t,v)={2t\over a(t,v)+\sqrt{a(t,v)^2-4t^2}},\qquad
 a(t,v)=1-tv+t^2+t^3v.
\]

The checker uses the physical positive square-root branch. Put

\[
 v_n=q^{2n},\qquad u_n=U(t,v_n),\qquad g(u)=t-Du,
 \qquad z_0={1\over g(q)},
\]

and iterate the exact recurrence

\[
 z_{n+1}=r z_n {g(u_n)\over g(u_n)+\delta}.                 \tag{1}
\]

The regularized weights are evaluated without dividing by the removable
\(h\)-zero. With `u_h=tq/C`, `f(u)=u/(1-tu)`,

\[
 \begin{aligned}
 V_1(u)&={[(1-tu)(1-tu_h)]^{-1}+L_1\over C},\\
 V_2(u)&={(f(u)+f(u_h))[(1-tu)(1-tu_h)]^{-1}+L_2\over C},\\
 L_1&={f(u_h)\over1-u_h},\\quad L_2={f(u_h)^2\over1-u_h}.
 \end{aligned}                                                   \tag{2}
\]

The exact regularized identities used by the checker are

\[
 \begin{aligned}
 P&={C\over g(q)}+L_1S_0+Q\sum_{n\ge0}z_nV_1(u_n),\\
 {H\over t^2}&=f(q){C\over g(q)}+L_2S_0+Q\sum_{n\ge0}z_nV_2(u_n),\\
 S_0&=-{tD^2\over g(q)},\\quad Q=q\,t^2(1-q^2)(1-t^2).
 \end{aligned}                                                   \tag{3}
\]

The W denominator numerator is formed as

\[
 F=(3-t-2D_I)P-4H-(1+t+2D_I),\qquad D_I={D_R\over1+D_R},          \tag{4}
\]

where `D_R` is the positive directed-ramp sum below. The exact algebraic
identity `I-1=F/(1+P)` gives `W=-1-(1+P)/F`.

## Rigorous tails

The directed term is evaluated from the positive closed-form summands

\[
 D_R=\sum_{k\ge0}{tq^k\over\beta+\gamma q^{2k}},\quad
 \beta={1-t-tq\over1-q^2},\quad
 \gamma={q[t-q(1-t)]\over1-q^2}.
\]

Both \(\beta\) and \(\beta+\gamma=1-t\) are positive on every certified
bracket. If `m_D` is the smaller of these two positive lower bounds, then
the omitted part after `K` terms is enclosed by

\[
 0\le D_R-D_{R,K}
 \le {t\over m_D}{q^K\over1-q}.                              \tag{5}
\]

The implementation sums until the outward interval in (5) is below
\(10^{-30}\).

For the prudent sum, choose `m` with `m\varepsilon\ge4`, where
\(\varepsilon=-\log(q^2)\). The interval engine proves `g(u_m)>0`, and
the monotonicity of \(U(t,v)\) in \(v\) gives `g(u_n)>0` for all \(n\ge m\).
Also `u_n\ge t`, so

\[
 0<g(u_n)\le g_\infty:=t^2q.
\]

For n\ge m, equation (1) therefore has a positive ratio and

\[
 0<{z_{n+1}\over z_n}\le
 R:=r{g_\infty\over g_\infty+\delta}=r^2<r\le e^{-\varepsilon}<1. \tag{6}
\]

The equality `R=r^2` is exact: `qC+(1-q^2)=D`. The checker also verifies
\(R<r<q^2=e^{-\varepsilon}\), which implies the requested
\(r\le e^{-\varepsilon}\) bound. Since \(z_0<0\), and the checker verifies
every finite-prefix recurrence ratio is positive, all `z_n<0`. A direct
rational box on the actual finite \(t\)-bracket gives positive `V_j` and
`V_j<40` for `j=1,2`. The two
weight boxes are recorded in the output, so this finite bound does not invoke
the asymptotic M5 domain. Thus, for `j=1,2`,

\[
 \left|\sum_{n\ge M}z_nV_j(u_n)\right|
 \le { |z_M|\,V_{j,\max}\over1-R},
 \qquad M\ge m.                                                 \tag{7}
\]

Multiplication by `Q`, and by `t^2Q` for `H`, gives the interval tail
for (3). The checker chooses `M` by exact repeated squaring of the upper
endpoint of `R` until the induced F-error is below 10^{-27}, then
checks the final bound directly. No floating-point tail estimate or last
summand is used.

## Brackets, source poles, and noncancellation

The rational seed centers are the recorded diagnostic `t_N` values. The
half-widths used by the checker are

\[
10^{-20},10^{-21},10^{-22},10^{-23},10^{-23},10^{-24}
\]

for N=32,64,128,256,512,1024, respectively. The final endpoints are
therefore exact rational numbers. The checker independently encloses

\[
 v_g={q(D-t^2)\over D(1-t^2)},\qquad
 v_h={C-t^2q\over qC(1-t^2)},
\]

and computes

\[
 a={-\log v_g\over-\log(q^2)},\qquad
 b={-\log v_h\over-\log(q^2)}.
\]

For every whole `t`-bracket it verifies

\[
 N+{4\over5}<a<N+{9\over10},\qquad N<b<N+1.                  \tag{8}
\]

Thus the `g`- and `h`-source denominators are separated from integer
indices, and the physical kernel denominators are positive. These checks are
the finite source-pole exclusion needed before applying the intermediate
value theorem.

At the left endpoint the certified `F`-interval is strictly positive; at
the right endpoint it is strictly negative. The exact `t`-bracket is
connected, so a real zero of `F` exists in every listed bracket. To cover
the cancellation possibility, the checker evaluates (3), with its complete
tail, over the *whole* bracket and verifies

\[
 1+P<0.                                                        \tag{9}
\]

Consequently every zero supplied by the endpoint signs is a genuine W pole.
The argument deliberately does not select or claim a unique zero.

The pole statement also uses the standard local analytic continuation supplied
by the same source-pole check. For each fixed point of a certified `t`-bracket,
the finite prefix of the `P,H` sums is analytic because its `g`- and
`h`-denominators are nonzero. After the checked tail start, `v_n` is small,
`r^2<1`, and the positive limiting denominators remain separated from zero
in a sufficiently small complex neighborhood. The geometric majorant in
(7), with that neighborhood shrunk if necessary, gives normal convergence of
the tail. Hence `P`, `H`, `D_I`, and `F` are holomorphic locally at each real
zero selected by the intermediate value theorem.

## Reproduction and scope

Run without optimization (the interval assertions and branch guards are part
of the certificate):

```text
python3 proofs/m7_finite_poles.py
```

The output records the exact integer-over-\(2^{384}\) endpoint intervals,
the directed-term tail, the prudent (F)-tail, the source-pole phase boxes,
and the full-bracket numerator box for each N. This is classified as
`EXACT FINITE W POLE BRACKETS; 384-BIT OUTWARD INTERVALS`. It is finite
evidence and does not imply a global effective threshold, uniqueness,
simplicity, or coverage of unlisted (N).
