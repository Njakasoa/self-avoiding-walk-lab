# Span-two irreducible bridges: exact ladder decomposition

This note analyzes the exact family selected by `max_span=2` in
`src/bridge_spans.py`.  The convention is the one in `NORMALIZATION.md`:
after the root, every visited point has positive horizontal coordinate, the
first edge is east, and the terminal horizontal coordinate is the weak maximum
visited by the walk.  A renewal point is an internal bridge prefix after which
all points are strictly to the right of the joining point.

The result below is an **EXACT INTEGER** characterization and an exact
weighted generating function for the whole span-two irreducible family.  It is
a finite-width ladder calculation; no novelty or priority claim is made.

## Geometric characterization

Write the two allowed columns as C₁ = {1} × ℤ and C₂ = {2} × ℤ, after
the mandatory root edge (0,0) → (1,0).  Let the first C₁ → C₂ rung occur
at height h₁.  A span-two bridge is irreducible exactly when it visits C₁
again after that first rung.

Indeed, if there is no later C₁ vertex, the last C₁ vertex before
the first rung is a renewal point: its prefix has maximum one and the whole
suffix has horizontal coordinate two.  Conversely, if a later C₁ vertex
exists, a potential renewal point before the first rung has a suffix containing
a C₁ vertex, while a potential point after the first rung is either at
horizontal coordinate one below the earlier maximum two or at coordinate two,
from which a strict-right suffix is impossible.

Consequently the inter-column rungs of an irreducible span-two bridge have the
form

\[
 C_1\xrightarrow{E}C_2,
 \quad(C_2\xrightarrow{W}C_1\xrightarrow{E}C_2)^r,
 \qquad r\geq1.
\]

The root edge is a separate east edge from x = 0 to C₁.  Let a >= 0 be the
initial vertical run in C₁, let b₁ >= 1 be the first vertical run in C₂
before the first return W, and let cⱼ >= 1 be the vertical run in C₁ before
the j-th return E.  After the first rung, all vertical runs move in one
common direction d ∈ {N,S}, and the successive rung heights strictly
progress in direction d.  The only constraint at the initial escape is:

* if a = 0, either direction d is allowed and b₁ >= 1;
* if a > 0, d may agree with the sign of the initial run, with b₁ >= 1,
  or oppose it, with b₁ >= a + 1.

To see the strict progression, suppose for definiteness that the first escape
is upward.  The first C₁ run occupies the interval between height zero and
h₁.  The first return to C₁ must be above this interval.  The next C₁ run
then occupies the interval from that return height to the next E rung.  A
subsequent C₂ run cannot turn back through the gap: that gap is occupied on
C₁.  Induction gives strict upward progression;
the downward case is its reflection.  This also proves the converse: any
sequence satisfying these run constraints visits disjoint vertices and is a
span-two irreducible bridge.

The weak terminal maximum matters.  After the final E rung, a vertical tail
is allowed in C₂.  If the last C₁ run has length c, the tail can move
outward in direction d for any length t >= 0, or inward through the gap for
1 <= t < c.  It cannot pass the previously visited C₂ segment or reverse
direction.

## Exact weighted generating function

Let u mark horizontal edges and v mark vertical edges.  A positive
vertical run has series

\[
 A(v)=\frac{v}{1-v}.
\]

The initial run together with the first escape run has series

\[
 \begin{aligned}
 T(v)
 &=2A(v)+2A(v)^2
   +2\sum_{a\geq1}\sum_{b\geq a+1}v^{a+b}\\
 &=\frac{2v(1+v+v^2)}{(1-v)^2(1+v)}.
 \end{aligned}
\]

For a final C₁ run of length c, the tail series is

\[
 R_c(v)=\frac1{1-v}+\sum_{t=1}^{c-1}v^t
       =\frac{1+v-v^c}{1-v}.
\]

Thus the final run plus its weak terminal tail contributes

\[
 L(v)=\sum_{c\geq1}v^cR_c(v)
     =\frac{v(1+v+v^2)}{(1-v)^2(1+v)}.
\]

The root edge and the first C₁ → C₂ rung contribute u².  For a fixed r >= 1,
the r return pairs contribute u^(2r), the ordinary
vertical runs between the first and last pair contribute
A(v)^(2(r-1)), and the two endpoint factors are T(v)L(v).  Therefore

\[
 \begin{aligned}
 I_2(u,v)
 &=u^2T(v)L(v)\sum_{r\geq1}u^{2r}A(v)^{2(r-1)}\\
 &=\frac{u^4T(v)L(v)}{1-u^2A(v)^2}\\
 &=\boxed{\frac{2u^4v^2(1+v+v^2)^2}
 {(1-v)^2(1+v)^2\bigl((1-v)^2-u^2v^2\bigr)}}.
 \end{aligned}
\]

This is the irreducible span-exact series, not a finite-length fit.  The
span-one control in the same variables is

\[
 I_1(u,v)=u\left(1+2A(v)\right)=\frac{u(1+v)}{1-v}.
\]

Since a total span-two bridge factors either as one span-two irreducible or as
two span-one irreducibles, its bivariate bridge coefficient is

\[
 B_2(u,v)=I_2(u,v)+I_1(u,v)^2.
\]

At u = v = z,

\[
 I_2(z,z)=
 \frac{2z^6(1+z+z^2)^2}
 {(1-z)^2(1+z)^2((1-z)^2-z^4)}
 =
 \frac{2z^6(1+z+z^2)^2}
 {(1-z)^2(1+z)^2(1-z-z^2)(1-z+z^2)}.
\]

The first nonzero coefficients i_(n,2), indexed from n = 0, are

\[
 0,0,0,0,0,0,2,8,24,52,102,180,312,524,878,1448,
 2380,3880,6318,10256,16644,26972,43698,70748,
 114532,185364,299994,485456,785560,1271120,2056794.
\]

## Exact replay and scope

The bounded probe `experiments/m3_span_probe.py` independently repeats the
direct renewal test while retaining horizontal/vertical degrees, then checks
those coefficients against the displayed decomposition.  The default command

```text
PYTHONPATH=. .venv/bin/python experiments/m3_span_probe.py \
  --max-n 30 --weighted-max-n 18 --max-seconds 60
```

completed in about 13 seconds in the development workspace.  It enumerated
5,384,930 capped bridge paths through length 30 and checked the direct
irreducible rows against bivariate renewal inversion.  The univariate formula
matched every n <= 30; the weighted formula matched every retained
(n_h,n_v) coefficient through total length 18.  These are exact integer
checks under the stated cap and convention.

As a separate falsification diagnostic, the probe fits a unique order-eight
scalar recurrence after the transient n = 6, using n = 14,...,21 as training
equations.  Its coefficient vector in the convention

    a_n = c_1 a_(n-1) + ... + c_8 a_(n-8)

is (2, 1, -4, 2, 2, -3, 0, 1), and all nine terms n = 22,...,30 are held out
and match exactly.  This recurrence screen is not the proof; it is consistent
with the displayed rational denominator.  There is no claim that the
unrestricted square-lattice bridge series is rational, nor a claim of
publication novelty for finite-width ladder walks.
