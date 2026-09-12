# M14 endpoint research: exact reductions and the remaining sign gap

Status: **bounded research reduction; no uniform endpoint-sign certificate**.
The target is

\[
 F_N(4/5)>0,\qquad F_N(9/10)<0\qquad(N\ge32).
\]

All inequalities below are analytic consequences of the reviewed real
M10--M13 boxes.  No phase samples, interpolation in \(N\), or finite
floating-point sign is used as evidence.  The exact rational checks are in
`proofs/m14_endpoint_bounds.py`.

## 1. The endpoint inequalities reduce to positive-mass bounds

Write the M10 regularized decomposition as

\[
 F_N(\theta)=B_N(\theta)+\sum_{n\ge0}J_n(\theta),
 \qquad
 J_n=A_0T_nK_nL_W(u_n)>0.
\tag{1}
\]

The reviewed M13 boundary box is

\[
 -2<B_N(\theta)<-\frac75.
\tag{2}
\]

Let \(S_{\le60N}=\sum_{n=0}^{60N}J_n\) and let
\(S_{>60N}\) be the remaining positive tail.  Therefore sufficient
conditions, with the currently available boundary box, are

\[
 S_{\le60N}(4/5)+S_{>60N}(4/5)>2,
\tag{3L}
\]
and

\[
 S_{\le60N}(9/10)+S_{>60N}(9/10)<\frac75 .
\tag{3R}
\]

The M13 tail ingredients give a useful value bound, independent of any
endpoint sampling.  Use the exact identity
\(A_0=J(t)(1-e^{-e})\) with \(J(t)<5/6\), so the factor
\(1-e^{-e}\) cancels the geometric sum denominator.  Together with
\(T_n<151/1000\) after \(60N\), \(L_W<2\), \(r^n\le e^{-ne}\), and
\(x_{60N+1}>87/10\),

\[
 0<S_{>60N}<\frac56\frac{151}{1000}\,2e^{-87/10}
 <\frac{151}{3\,000\,000}.                         \tag{4}
\]

Thus the right endpoint would follow from the finite-mass target

\[
 S_{\le60N}(9/10)<\frac75-\frac{151}{3\,000\,000}
 =\frac{4\,199\,849}{3\,000\,000}.                 \tag{5}
\]

## 2. Exact block primitive

The bare product is

\[
 T_n=\prod_{j=0}^{n-1}\frac{a-j}{b-j},
 \qquad a=N+\theta,\quad b=a-\beta,
\]

with \(7/10<\beta<18/25\).  Define

\[
 Q_n=\frac{(n-a)T_n}{1-\beta},
 \qquad Q_{-1}=-\frac{b+1}{1-\beta}.
\]

Direct substitution, including the \(n=0\) step, gives

\[
 Q_n-Q_{n-1}=T_n>0.
\tag{6}
\]

Consequently every finite block has the exact mass

\[
 M(\ell,r):=\sum_{n=\ell}^{r}T_n=Q_r-Q_{\ell-1}>0.  \tag{7}
\]

The reviewed real product estimate gives
\(K_{n+1}/K_n=r_{\rm geom}R_e(ne)<1\), hence \(0<K_n\le1\).  M10 gives
that \(L_W(u_n)>0\) while it increases with \(u_n\).  Since \(u_n\)
decreases in \(n\), the product \(D_n\) below is decreasing:

\[
 D_n:=K_nL_W(u_n)>0
 \quad\text{decreases in }n.
\]

Hence (7) gives the exact block enclosure

\[
 A_0D_rM(\ell,r)
 \le \sum_{n=\ell}^{r}J_n
 \le A_0D_\ell M(\ell,r).                         \tag{8}
\]

This is the useful uniform reduction: it avoids estimating the singular
bare factors one at a time.  It does not by itself give numerical bounds,
because a uniform lower/upper enclosure for the endpoint values \(D_\ell\)
and \(D_r\), with blocks whose integer endpoints vary with \(N\), is still
needed.

## 3. A strict endpoint-left improvement

At \(\theta=4/5\), put \(v=\theta-\beta\).  The accepted beta strip gives

\[
 \frac2{25}<v<\frac1{10},\qquad
 \frac{\theta}{v}>8,\qquad
 \frac{1-\theta}{1-\theta+\beta}>\frac5{23}.          \tag{9}
\]

Repeating the M13 positive-side and post-crossing telescopes with these
endpoint constants gives, for \(M=\lfloor N/2\rfloor\),

\[
\begin{aligned}
 T_{N+1}&>8\left(\frac{5N}{6}\right)^{7/10},\\
 T_{N+1+k}&>\frac{40}{23}\left(\frac{2N}{3k}\right)^{7/10}
 \quad(1\le k<M).                                    \tag{10}
\end{aligned}
\]

Using \(\sum_{k=1}^{M-1}k^{-7/10}\ge
\int_1^M x^{-7/10}\,dx\), \(M\ge31N/64\), and exact tenth-power
comparisons, this yields

\[
 \sum_{n=N+1}^{\lfloor3N/2\rfloor}T_n>\frac72N.       \tag{11}
\]

This is a strict improvement over the reviewed uniform lower constant
used in M13.  Multiplying (11) by the reviewed subwindow bounds

\[
 \frac{A_0}{e}>\frac{41}{50},\qquad K_n>\frac14,\qquad
 L_W(u_n)>\frac32,\qquad eN>\frac{48}{329},
\]

gives the endpoint-left positive contribution

\[
 S_{N+1:\lfloor3N/2\rfloor}(4/5)
 >\frac{41}{50}\frac14\frac32\frac72\frac{48}{329}
 =\frac{369}{2350}\approx0.15702.                    \tag{12}
\]

This is useful but far below the mass \(2\) required by (3L).  Positivity
of the omitted blocks cannot be turned into a quantitative lower bound by
itself.

At the right endpoint, the pre-crossing product has a different safe
specialization.  With \(v=9/10-\beta<1/5\), the product at \(n=N\) has
no \(\theta/(\theta-\beta)\) factor, and the M13 telescope gives

\[
 T_N>\left(\frac{5N+6}{6}\right)^{7/10}.              \tag{13}
\]

Inserting (13) into the exact primitive (7) gives

\[
 \sum_{n=0}^{N}T_n
 <\frac{25}{7}\left[
 N+\frac65-\frac9{10}\left(\frac{5N+6}{6}\right)^{7/10}
 \right].                                             \tag{14}
\]

This is an endpoint-safe refinement of the bare pre-mass only.  Combining
it with the currently uniform bounds \(A_0<5e/6\), \(K_n\le1\), and
\(L_W<5899/1000\) still has limiting certified allowance

\[
 \frac56\frac{17}{100}\frac{5899}{1000}\frac{25}{7}
 =\frac{100283}{33600}>2.98,                         \tag{15}
\]

which is above the full right target (5), even before the post-crossing
blocks are added.  A phase-endpoint block enclosure for \(D_n\) is needed.

## 4. What is and is not covered

The endpoint-left refinement (12), exact block identity (8), and tail value
bound (4) are rigorous reductions.  They do not prove either sign.  The
remaining obligations are concrete:

* sharpen the boundary value at \(\theta=4/5\), or lower-bound enough
  additional block masses to reach (3L);
* upper-bound every finite block at \(\theta=9/10\) so that their total
  meets (5); and
* make those \(D_n\) bounds uniform in all integer \(N\ge32\), including
  the floor changes in the block endpoints.

The M7 six-index artifact certifies signs at the two ends of a narrow
*root bracket* for six selected indices; those are not the phase endpoints
\(.8,.9\).  The N=32 full-band artifact is finite.  The reviewed M9/M6
eventual comparisons begin at large thresholds and leave the intervening
indices open.  None of these facts supplies a monotonicity-in-\(N\) bridge,
so replacing (8) by a sampled interpolation would be invalid.

## 5. Reproduction and provenance

Run the exact rational ledger with:

```text
python3 -m proofs.m14_endpoint_bounds
```

It returns `status=pass` and the classification `EXACT RATIONAL ENDPOINT
REDUCTIONS; NO SIGN CLAIM`.  It uses no external files and writes no output.
The source revision at drafting was
`8f8176b8039c518455ea5a1ec284564f4f1ea108`; the final hashes of this note
and the checker are reported to the parent for source freezing.
