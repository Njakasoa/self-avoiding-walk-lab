# He (2025) weighted square-lattice audit

Primary source: Q. He, *Upper bounds for the connective constant of weighted
self-avoiding walks*, arXiv:2508.01993v3 (17 Aug 2025),
[PDF](../papers/he-2508.01993.pdf), [arXiv record](https://arxiv.org/abs/2508.01993).
The source's public implementation is
[qhe28/weighted_connective_constant](https://github.com/qhe28/weighted_connective_constant).

## Method and hypotheses

He defines a translation-invariant multiplicative edge weight on p.3,
(2.1)--(2.3), and takes the weights strictly positive:
\(z\in\mathbb R_{>0}^d\). For a partition \(P\) of the \(m\)-step SAWs into
weight-preserving symmetry classes, pp.4--5 define

\[
G^P_{rs}(m,n)=\frac{F^P_{rs}(m,n)}{w(\gamma_r(m))},
\qquad
G^P(m,n)=[G^P_{rs}(m,n)]_{r,s}.
\]

Theorem 2.2 (p.4, (2.8)) states, if \(G^P(m,n)\) is primitive,

\[
\mu\leq \rho(G^P(m,n))^{1/(n-m)}.
\]

The proof on p.5, (2.9)--(2.12), joins two \(n\)-step SAWs over their common
\(m\)-step overlap. The joined walk can self-intersect, so it overcounts the
SAWs. The overlap is counted twice, which explains the normalization by
\(w(\gamma_u(m))\); this gives
\(G^P(m,2n-m)\leq G^P(m,n)^2\), then the analogous bound for all powers and
Perron--Frobenius yields the upper direction.

## Reproducible \((m,n)=(1,2)\) matrix

On the square lattice, let \(x\) weight horizontal edges and \(y\) vertical
edges. He's square-lattice convention and symmetry are on p.7. For arbitrary
anisotropic weights, the weight-preserving subgroup is

\[
H=\{(u,v)\mapsto(\pm u,\pm v)\}\cong D_2.
\]

For one-step walks use the two classes
\(P_h=\{+e_x,-e_x\}\) and \(P_v=\{+e_y,-e_y\}\). With representatives
\(+e_x,+e_y\), the continuation sums are

\[
F_{hh}=x^2,\quad F_{hv}=2xy,
\qquad
F_{vh}=2xy,\quad F_{vv}=y^2.
\]

Dividing each row by its representative's initial weight gives

\[
G^P(1,2)=
\begin{pmatrix}x&2y\\2x&y\end{pmatrix}.
\]

For \(x,y>0\) this matrix is entrywise positive and hence primitive. Its
dominant eigenvalue is

\[
U_{1,2}(x,y)=\rho(G^P(1,2))
 =\frac{x+y+\sqrt{x^2+14xy+y^2}}2,
\]

so \(\mu(x,y)\leq U_{1,2}(x,y)\). This is Table 1 on p.8.

The geometrically orientation-preserving part of \(H\) is
\(H^+=\{I,-I\}\cong C_2\); for \(m=1\) it gives the same two classes. The
full \(D_4\), including coordinate swap, is weight-preserving only when
\(x=y\). He makes this distinction explicitly in Remark 2.4 (p.6). Spatial
symmetries act on ordered walks; this does not quotient path traversal reversal.

## All exact Table 1 expressions

Writing \(R=x^2+14xy+y^2\), p.8 gives

\[
U_{1,2}=\frac{x+y+\sqrt R}{2},
\]

\[
U_{1,3}=2^{-1/2}\left[x^2+8xy+y^2+(x+y)\sqrt R\right]^{1/2}
\quad\text{(SAW and SAT)},
\]

\[
U^{\mathrm{SAW}}_{1,4}=2^{-1/3}\left[
x^3+12xy(x+y)+y^3+
\sqrt{x^6+24x^5y+136x^4y^2+254x^3y^3+136x^2y^4+24xy^5+y^6}
\right]^{1/3},
\]

\[
U^{\mathrm{SAT}}_{1,4}=2^{-1/3}\left[
x^3+12xy(x+y)+y^3+(x^2+5xy+y^2)\sqrt R
\right]^{1/3}.
\]

## Nonnegative axes

The theorem assumes positive weights. At \(x=0\), every walk containing a
horizontal edge has zero weight; the two straight vertical walks give
\(Z_n(0,y)=2y^n\) for \(n\geq1\), hence \(\mu(0,y)=y\). Likewise
\(\mu(x,0)=x\), and \(\mu(0,0)=0\). Therefore the Table 1 formulas extend to
the axes with equality, but the reducible axis matrices do not satisfy the
theorem's primitivity hypothesis and must be handled by this direct argument.

## E1 prior-art guardrail

Pönitz--Tittmann, *Improved Upper Bounds for Self-Avoiding Walks in
\(\mathbb Z^d\)*, EJC 7 (2000), R21,
[article/PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r21),
pp.2--3 and 6--8, already groups finite-memory histories with identical
future behavior, retains transition multiplicities, exploits symmetry
normalization, and uses the transfer-matrix Perron eigenvalue for a true upper
bound. Thus standard finite-memory compression is known.

For an exact equitable quotient, if \(A\) is the state adjacency matrix and
\(P\) is the class-indicator matrix, every state in class \(i\) must have the
same weighted transition sum into every class \(j\). Equivalently,

\[
AP=PB.
\]

Equality of total continuation counts alone is insufficient. Any E1 novelty
would need an additional certified invariant or simplification beyond this
standard condition. Couronné's later automaton modifications and multiple
simplifications are documented in
[arXiv:2211.16146](https://arxiv.org/abs/2211.16146), culminating in the
published bound \(2.662342426\); ordinary state compression cannot be claimed
as new.

## E2 prior-art guardrail

Kesten, *On the Number of Self-Avoiding Walks*, J. Math. Phys. 4 (1963),
960--969, [DOI](https://doi.org/10.1063/1.1704022), is the foundational
irreducible-bridge result. Jensen, *Improved lower bounds on the connective
constants for two-dimensional self-avoiding walks*, J. Phys. A 37 (2004),
11521--11529, [arXiv](https://arxiv.org/abs/cond-mat/0409381), explicitly uses
Kesten's bridge dictionary, \(B(z)=1/(1-I(z))\), and finite length/span
truncations as certified lower bounds.

The repository's span-one control is the known partially directed family whose
irreducible blocks are one horizontal step followed by a monotone vertical run,
with either vertical sign. Its generating function is

\[
I_1(z)=z\left(1+\frac{2z}{1-z}\right)=\frac{z(1+z)}{1-z},
\]

so \(I_1(\sqrt2-1)=1\) and the growth rate is \(1+\sqrt2\). After rotating
axes this is the repository's strict/weak horizontal bridge convention. The
weakly directed bridge/irreducible-bridge family is treated by
Bacher--Bousquet-Mélou,
[arXiv:1010.3200](https://arxiv.org/abs/1010.3200). Span or length truncation
alone is therefore known methodology, not a novelty claim.

## \(\mu\) versus a selected certificate

The exact \(\mu\) is homogeneous, symmetric under \(x\leftrightarrow y\),
coordinatewise nondecreasing, and log-convex in logarithmic weights; its axis
values are as above. An upper certificate \(U\) is only guaranteed pointwise by
the theorem. Its monotonicity, log-convexity, symmetry, and axis extension must
be checked or proved for that particular fixed matrix/selection; they do not
follow merely from \(U\geq\mu\). A piecewise choice of certificates or an
anisotropic invalid quotient can lose these properties.
