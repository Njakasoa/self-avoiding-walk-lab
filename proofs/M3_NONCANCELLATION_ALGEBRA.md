# Algebra audit for prudent-ramp noncancellation

Status: exact identities and failed sign ansatz. This note does not prove

\[
1+\widetilde P(r_l)\ne0
\]

for all roots \(P(r_l)=-1\).

The calculation uses the explicit Bacher--Beaton Propositions 14 and 16 as
implemented in experiments/m3_prudent_singularity_probe.py. The repository
commit visible during the calculation was
9087d31ddcf6c69ef6e62a7186755a3088724d6b.

## Common notation

For one summand, write

    C = q-t,       D = 1-t*q,       E = 1-q^2,
    h(u) = t*q-C*u,               g(u) = t-D*u,
    f(u) = u/(1-t*u),              k = q*C^2/D^2,
    u = U(t,v),                    w = U(t,v*q^2).

The kernel equation at \(v=1\) gives the exact identity

    C*D = t*q*(1-t^2).

The product factor in Proposition 14 is

    B(u,w) = k*g(w)/h(u).

## Exact common A_p family

Let

\[
 K=\frac{C(1-t^2)}{D},
 \qquad
 A_p(u,w)=\frac{K}{h(u)}\left(Df(u)^p-qC f(w)^p\right).
\]

Direct expansion of the displayed formulas in Propositions 14 and 16 gives

\[
 A=A_1,
 \qquad
 \widetilde A=t^2A_2.
\]

For A, this follows from

\[
\begin{aligned}
Df(u)-qCf(w)
&=\frac{uD-[qC+t(1-q^2)u]w}{(1-tu)(1-tw)}.
\end{aligned}
\]

For the hook numerator, the corresponding exact identity is

\[
\begin{aligned}
Df(u)^2-qCf(w)^2
={}&\frac{Du^2(1-2tw)}{(1-tu)^2(1-tw)^2}\\
&-\frac{[qC-tu(2qC+tEu)]w^2}{(1-tu)^2(1-tw)^2}.
\end{aligned}
\]

Equivalently, if F is the numerator of A after its positive prefactors
are removed and K_h is the corresponding hook numerator, symbolic expansion
gives the useful positive decomposition

\[
 K_h=u(1-tw)F+qCw(u-w)(1-tu).
\]

On the physical real branch, \(0<w<u<1/t\), so this proves that
K_h>0 whenever F>0; it also gives

\[
\frac{\widetilde A}{A}
=t^2\frac{u}{1-tu}
+\frac{t^2qCw(u-w)}{(1-tw)F}.
\]

This ratio identity alone does not control the sign of the full iterated sum,
because the product factors change sign under continuation between poles.

## Exact telescoping identity

Let p_0=1, p_(n+1)=p_n B(u_n,u_(n+1)), where
u_n=U(t,q^(2n)). For every integer p>=0, direct algebra gives

\[
\begin{aligned}
 p_nA_p(u_n,u_{n+1})
={}&Y_{p,n}-Y_{p,n+1}\\
&-t^2E(1-t^2)\frac{p_nf(u_n)^p}{h(u_n)g(u_n)},
\end{aligned}
\]

where

\[
Y_{p,n}=p_n\,\frac{D(1-t^2)f(u_n)^p}{g(u_n)}.
\]

The only cancellation needed here is

\[
D h(u)-t^2E=Cg(u),
\]

and Dk=qC^2/D.

After summing and using the locally geometric tail at fixed t, define

\[
W_n=-q t^2E(1-t^2)\frac{p_n}{h(u_n)g(u_n)}.
\]

Then the two full functions have the exact representations

\[
 P=\frac{C}{g(q)}+\sum_{n\ge0}W_nf(u_n),
\]

\[
 \widetilde P=t^2f(q)\frac{C}{g(q)}
   +t^2\sum_{n\ge0}W_nf(u_n)^2.
\]

The boundary simplification uses f(q)=q/D and CD=tq(1-t^2).

## Exact moment constraint

The kernel relation also yields

\[
 h(u)-kg(u)=\frac{CE}{D}(1-u).
\]

With z_n=p_n/g(u_n),

\[
 z_n-z_{n+1}
 =\frac{p_n[h(u_n)-kg(u_n)]}{h(u_n)g(u_n)}.
\]

Consequently,

\[
\sum_{n\ge0}W_n(1-u_n)
 =-\frac{tD^2}{g(q)},
\]

provided the locally geometric boundary term tends to zero. This is an exact
signed moment relation. It is not a positivity statement: g(q) is negative
at the numerically relevant roots, and the W_n themselves have mixed signs.

## Failed sign ansatzes

At a root P(r_l)=-1, set u_l=U(r_l,q(r_l)^(2l)),
f_l=f(u_l). Eliminating sum W_nf(u_n) with P=-1 and using

\[
 Q_l(u)=t^2f(u)\bigl(f(u)-f_l\bigr)
\]

gives the exact identity

\[
 1+\widetilde P(r_l)
 =B_l+\sum_{n\ge0}W_nQ_l(u_n),
\]

where

\[
 B_l=1+t^2f(q)\frac{C}{g(q)}
      -t^2f_l\left(1+\frac{C}{g(q)}\right).
\]

Q_l has the sign of u-u_l, but the continued W_n have more than one
sign block because both h(u_n) and g(u_n) change sign. Thus the remainder
has no fixed sign. Numerically, for the first five certified root brackets,
the boundary values B_l are approximately

    0.7466974781, 0.5468328593, 0.5002194746, 0.4780044160, 0.4649399144

while the actual values of 1+widetilde P are approximately

    0.4109348379, 0.3839686836, 0.3747882926, 0.3701165727, 0.3672745146.

So this ansatz supplies only an upper-bound orientation, not the needed lower
bound. A direct global sign guess for widetilde P-P also fails: in the first
pole interval its numerical value is positive near the left side and negative
near the right side (+5.31 at the midpoint versus about -5.95 near the right
endpoint).

The exact A_p and moment identities are useful reductions, but a lower bound
on the signed remainder, or a different all-index invariant, is still needed
to establish noncancellation.

The same calculation records why the simplest pure coboundary ansatz does not
close: choosing

\[
T_p(u)=D(1-t^2)f(u)^p/g(u)
\]

gives exactly the displayed difference \(T_p(u)-B(u,w)T_p(w)\), but leaves
the nonzero residual

\[
-t^2E(1-t^2)\frac{f(u)^p}{h(u)g(u)}.
\]

This residual vanishes only in the limiting algebraic case \(E=0\), not at the
finite roots under study.

A more targeted ansatz sets
\[
Q(u)=t^2f(u)^2-\alpha f(u)-\beta(1-u)
\]
to zero at the two sign thresholds \(u_h=tq/C\) and \(u_g=t/D\). The unique
\(\alpha,\beta\) then factor symbolically as

\[
Q(u)=
\frac{t^2h(u)g(u)L(u)}
{(1-tu)^2R(t,q)},
\]

where
\[
L(u)=q^2t+qt^4u-qt^2-q+t
\]
and
\[
R(t,q)=(qt+t^2-1)(qt^2-q+t)
       (q^2t+qt^3-qt^2-q+t).
\]

This removes the \(h(u)g(u)\) denominator from \(W_nQ(u_n)\), but its
orientation in the first five numerical root checks again gives only an upper
bound for \(1+\widetilde P\). It is therefore a useful exact reduction and an
explicit failed lower-bound ansatz, not a noncancellation proof.

The reproducible symbolic check is
experiments/m3_coboundary_probe.py; it passed the identities for powers
p=0,...,4 and reported A_equals_A1=True,
hook_equals_t2_A2=True, positive_hook_decomposition=True, and
moment_identity_mod_q_relation=True. Its SHA-256 at this checkpoint is
4b6ea78b9016139de7da00ebaa50f1e3eb354111f5c78668d2e7ddc228313dd1.
