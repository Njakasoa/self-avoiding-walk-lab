# M3 target audit — finite memory, anisotropic certificates, and weakly prudent poles

Audit date: 2026-09-12. This is a bounded primary-source literature audit for
the M3/M4 search. I read `NORMALIZATION.md`, `NEXT.md`,
`DISCOVERY_REPORT.md`, `STATE_OF_THE_ART.md`,
`environment/USER_RESEARCH_BRIEF.md`, and the local finite-memory and weighted
proof notes before searching. This file records literature and theorem targets;
it does not certify priority or novelty. No code, numerical matrix, or external
publication was changed, so no input/output hash is applicable.

## Verdict

The strongest narrow M3 candidate found is not another finite-memory quotient.
It is a precise unresolved analytic lemma in Bacher–Beaton's model of
2-sided weakly prudent bridges:

> Prove or disprove that the explicit quotient
> $P_I=(P-\widetilde P)/(1+P)$ has a new non-removable singularity
> accumulation (for example from zeros of $1+P$), and then transfer the
> obstruction to $W=I/(1-I)$.

The 2014 primary paper proves that $P$ and $\widetilde P$ each have an
infinite sequence of simple poles accumulating at
$\sigma=\sqrt2-1$, but explicitly says that it cannot conclude that
$P_I$ or $W$ is non-D-finite. At a common simple pole of $P$ and
$\widetilde P$, the quotient is automatically analytic after multiplying
numerator and denominator by the local parameter (provided the denominator's
residue is nonzero); that pole family is therefore not itself a viable
survival target. The viable M3 question is whether zeros of $1+P$ (or another
singularity family) create infinitely many non-removable singularities, and
whether the resulting obstruction transfers to $W$.

The finite-memory audit found useful guardrails but no comparably strong
square-lattice rate theorem. Monotonicity of the accepted languages is
elementary; high-dimensional/spread-out memory-$\tau$ convergence rates are
known; a quantitative rate for nearest-neighbor $\mathbb Z^2$, or a theorem
that every finite memory has a strict gap from the SAW connective constant, was
not found in this bounded audit. The anisotropic polynomial-certificate idea
is feasible locally, but generic positivity and weighted Perron methods are
already standard; it becomes M3 only if it yields a new uniform bound or a
nontrivial interpolation theorem.

Recommended order: **A (weakly prudent pole/cancellation lemma) > B (one
strict finite-memory gap with a reusable symbolic criterion) > C (uniform
anisotropic certificate)**.

## Primary-source guardrails

### Finite-memory upper bounds

* **Pönitz–Tittmann (2000),** *Improved Upper Bounds for Self-Avoiding Walks
  in $\mathbf Z^d$*, Electronic Journal of Combinatorics 7, R21:
  [official article page](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r21),
  [official PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r21/pdf),
  [DOI](https://doi.org/10.37236/1499).
  The abstract and §§1–3 describe automatically generated finite-memory
  automata and a square-lattice upper bound (2.679192495). The paper's
  finite-memory table gives the sequence (2.8312,2.7756,2.7445,
  2.7248,2.7113,2.7014,2.6939,2.6880,2.6832,2.6792) for loop cutoffs
  $k=4,6,8,10,12,14,16,18,20,22$ in $d=2$. It states that the finite-
  memory power-iteration limit exists, and explicitly says that its rate of
  convergence was not known there (PDF p. 8). Thus ordinary finite-memory
  construction, symmetry grouping, and a transfer-matrix bound are prior art.

* **Couronné (2022),** *New upper bound for the connective constant for
  square-lattice self-avoiding walks*,
  [arXiv record](https://arxiv.org/abs/2211.16146),
  [PDF](https://arxiv.org/pdf/2211.16146).
  The abstract says that modifying the Pönitz–Tittmann automaton and using
  loops through length 26 gives 2.662343 (the paper's detailed value is
  2.662342426). Its finite-state construction and successive bounds are
  an established benchmark. I found no monotonicity theorem for the numerical
  sequence, no square-lattice convergence rate, and no strict-gap theorem in
  this source.

* **Jensen (2004),** *Improved lower bounds on the connective constants for
  two-dimensional self-avoiding walks*,
  [arXiv record](https://arxiv.org/abs/cond-mat/0409381).
  This is a bridge/irreducible-bridge lower-bound source, not a proof of a
  finite-memory upper-bound rate. It reports empirical behavior for truncated
  bridge lower bounds (including an observed $a/n$-type error), while its
  discussion of Alm's upper method gives finite matrices but no corresponding
  $\mathbb Z^2$ convergence theorem. It should not be used to transfer a
  lower-bound rate to the upper automata.

* **Kawamoto (v3, 2026),** *Rate of convergence of the critical point of the
  memory-$\tau$ self-avoiding walk in dimensions $d>4$*,
  [arXiv record](https://arxiv.org/abs/2306.13936),
  [PDF](https://arxiv.org/pdf/2306.13936).
  The abstract and Theorem 1.1 treat spread-out walks in $d>4$. They record
  the known monotonicity and convergence of the memory-$\tau$ critical point
  and prove an asymptotic order $\tau^{-(d-2)/2}$ in the large-range regime.
  The introduction also records earlier high-dimensional bounds and says why
  Kesten's estimate cannot take $\tau\to\infty$ at fixed $d$. This is a
  positive result for the general memory question, but it does **not** supply
  a nearest-neighbor square-lattice rate. It is unsafe to state that no rate
  exists anywhere; the safe statement is that this primary source is
  dimension/range restricted and did not resolve the project's $d=2$ case.

* **Graham (2010),** *Borel type bounds for the self-avoiding walk connective
  constant*, [arXiv record](https://arxiv.org/abs/0911.5163),
  [DOI](https://doi.org/10.1088/1751-8113/43/23/235001).
  The memory-$\tau$ lace-expansion discussion gives high-dimensional
  stabilization of fixed expansion coefficients once $\tau$ is large
  enough. This is another guardrail against claiming a new general
  finite-memory convergence principle; it does not give a square-lattice
  quantitative rate.

### Strictness and entropy perturbations

* **Ramsey (2019),** *Perturbing subshifts of finite type: two words*,
  [arXiv record](https://arxiv.org/abs/1902.03352),
  [PDF](https://arxiv.org/pdf/1902.03352).
  For an irreducible SFT, forbidding one or two admissible words lowers the
  Perron/entropy value with an explicit exponentially small bound in word
  length. The higher-block construction makes a fixed finite-memory SAW
  transition deletion look similar. This is a useful theorem-level template,
  not a direct result for the square-lattice SAW automata: the SAW memory
  family changes its state graph and the forbidden loop set is not a single
  arbitrary word. Any application must prove the required primitive component,
  admissibility, and correspondence exactly.

### Weighted and anisotropic upper bounds

* **Alm (1993),** *Upper bounds for the connective constant of self-avoiding
  walks*, [Cambridge article page](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/upper-bounds-for-the-connective-constant-of-self-avoiding-walks/F203A1A0A2A35B9049DB06D31795FC3F),
  [DOI](https://doi.org/10.1017/S0963548300000547).
  The matrix/Perron construction underlying the modern finite-state upper
  method is prior art. The full article was not available through the bounded
  access path used here; claims about its details are therefore cross-checked
  against He and Pönitz–Tittmann rather than presented as a fresh reading.

* **He (2025),** *Upper bounds for the connective constant of weighted
  self-avoiding walks*, Journal of Physics A 58, 505003,
  [arXiv record](https://arxiv.org/abs/2508.01993),
  [PDF](https://arxiv.org/pdf/2508.01993),
  [published DOI](https://doi.org/10.1088/1751-8111/ae280e),
  [public implementation](https://github.com/qhe28/weighted_connective_constant).
  Theorem 2.2 proves, for a positive weighted lattice and a primitive matrix
  $G^P(m,n)$,
  \[
      \mu(z)\le \rho(G^P(m,n))^{1/(n-m)}.
  \]
  Remark 2.4 allows a finer partition that remains valid for all positive
  weights, whereas a coarser symmetry partition may require relations such as
  $x=y$. The paper provides pointwise symbolic/numerical bounds and a
  convergence domain for the multivariate generating function. It does not
  give a single rational polynomial positive-vector certificate valid over a
  parameter box, nor a theorem describing all partition changes as the weight
  ratio varies. Therefore a uniform interval certificate could be a useful
  applied target, but the underlying weighted-Perron method and parameter
  sensitivity are already known.

* **Handelman (1988),** *Representing polynomials by positive linear functions
  on compact convex polyhedra*, Pacific Journal of Mathematics 132, 35–62,
  [DOI](https://doi.org/10.2140/pjm.1988.132.35).
  Handelman's theorem says that a strictly positive polynomial on a compact
  polytope has a positive combination representation in the defining affine
  inequalities. This is a generic exact positivity certificate that could
  certify coefficientwise or residual inequalities for a fixed SAW matrix;
  it is not an SAW novelty by itself.

## Target A — weakly prudent bridge pole/cancellation lemma

### What the primary source leaves open

Bacher and Beaton, *Weakly prudent self-avoiding bridges*, FPSAC 2014,
DMTCS Proceedings AT, 827–838,
[official PDF](https://www.nicholasbeaton.com/papers/BB2014.pdf),
[DMTCS DOI](https://doi.org/10.46298/dmtcs.2445), give the exact structural
identities (paper pp. 830–835):

\[
 W=\frac{I}{1-I},\qquad I=4P_I-2D_I-t,
 \qquad P_I=\frac{P-\widetilde P}{1+P}.
\]

Here $P$ is the generating function of NE-prudent ramps,
$\widetilde P$ is the hook-ramp generating function, and $P_I$ counts
irreducible prudent ramps. Proposition 14 and Proposition 16 express $P$ and
$\widetilde P$ as explicit infinite sums of algebraic functions. Theorem 17
(paper p. 836) proves that each is meromorphic in $|t|<\sigma$, with simple
real poles $t_{2\ell}\in[\rho,\sigma)$ accumulating at
$\sigma=\sqrt2-1$, and hence each is non-D-finite.

The same paragraph then says, explicitly, that the relation (5) is not enough
for the authors to conclude that $P_I$ is non-D-finite, although they
strongly expect it. Section 4.2 likewise says that the complicated $I$ leaves
them unable to prove that $W$ is non-D-finite. Proposition 18 only brackets
the dominant singularity of $W$ numerically to 101 digits, and Corollary 19
derives the corresponding asymptotic growth estimate.

The phrase “full details will appear in a longer version” occurs in the
extended abstract (§3.4 and §5). In this bounded search I found no later
primary paper or full-length version resolving the $P_I/W$ non-D-finiteness
question. Exact-title searches, author/title searches, the DMTCS version, the
HAL record, and the author bibliography all led back to the 2014 source or
talk material. This is a search limitation, not evidence that no unpublished
or hard-to-index follow-up exists.

### A precise theorem target

Do not state the target as “the poles of $P$ automatically prove that
$P_I$ is non-D-finite.” If $P$ and $\widetilde P$ share a genuine simple
pole at $t_{2\ell}$, then the quotient is locally analytic there: after
multiplying numerator and denominator by $t-t_{2\ell}$, both become analytic
and the denominator has nonzero value. Theorem 17's common pole family is
therefore a cancellation/regularity fact, not a pole-survival proof.

A viable candidate lemma is one of the following:

1. **Zero-family form.** Prove that the analytic continuation of $P$ has an
   infinite family of simple zeros of $1+P$ in a domain where
   $P-\widetilde P$ does not vanish, with an accumulation point at or
   controlled by $\sigma$. These zeros give genuine poles of $P_I$.
2. **Alternative-accumulation form.** Locate another infinite family of
   non-removable singularities of the quotient, or prove an equivalent
   obstruction to a finite-order differential equation with polynomial
   coefficients. A finite set of numerically observed zeros is evidence for
   a search, not a theorem; an all-index existence/non-cancellation argument
   is required.
3. **Bridge-transfer form.** Prove the preceding statement for $P_I$, and
   separately show that the substitution
   $I=4P_I-2D_I-t$, followed by $W=I/(1-I)$, does not remove the
   obstruction. This last transfer is a separate lemma and should not be
   silently assumed.

The first successful lemma is enough for an M3 result. A complete proof that
$W$ is non-D-finite is a stronger follow-up, not a prerequisite for a useful
contribution.

### Feasible exact work package

The local work can stay symbolic and exact rather than relying on a floating
plot:

1. Implement or transcribe the algebraic series $U(v)$, $q=U(1)$, and the
   summands $A(q^{2n})$, $\widetilde A(q^{2n})$, $B(q^{2n})$ in BB
   Propositions 14 and 16.
2. At a candidate $t_{2\ell}$, isolate the common pole factor and compute
   exact algebraic principal and constant Laurent coefficients of $P$ and
   $\widetilde P$ to verify the automatic removability. Then search the
   continuation for exact or rigorously isolated zeros of $1+P$.
3. Prove an all-index sign, monotonicity, or algebraic nonvanishing statement
   for the numerator at such a zero family, or locate a different singularity
   family with the same effect. The first five numerical $P=-1$ roots seen in
   the local probe (with the companion denominator check reported as
   $H+1>0$) are a search lead only; no all-index existence or non-cancellation
   proof was found here.
4. Only after the local quotient is controlled, test the transfer to $I$ and
   $W$. Keep exact series truncation separate from a rigorous analytic
   continuation argument.

Useful falsifiers are equally concrete: if symbolic Laurent expansion proves
that every $t_{2\ell}$ is removable for $P_I$, the pole-survival route is
closed and the target should move to a different accumulation mechanism rather
than being overstated.

### Novelty guardrail

Bacher–Bousquet-Mélou, *Weakly directed self-avoiding walks*, JCTA 118
(2011), [arXiv](https://arxiv.org/abs/1010.3200), proves non-D-finite behavior
for a related weakly directed model. That precedent makes the general theme
well established, but it does not resolve the 2-sided weakly prudent bridge
quotient $P_I$ or $W$. The safe claim is therefore “a missing analytic lemma
in the 2014 primary source,” not “first non-D-finite prudent model.”

## Target B — one strict finite-memory gap with a reusable criterion

### What is already known

For the repository's suffix-memory languages, increasing memory removes
accepted walks, so the finite-memory growth rates are nonincreasing. The
odd/even loop parity and the line-graph explanation already audited in
`references/LINEGRAPH_PRIOR_AUDIT.md` are known consequences and should not be
used as M3. Pönitz–Tittmann's finite-memory paper gives true finite-memory
upper bounds but says it does not know the numerical power-iteration rate. The
Kawamoto result supplies monotonicity/convergence/rates in a different,
high-dimensional/spread-out regime. None of these sources, in this bounded
audit, gives a square-nearest-neighbor theorem of the form

\[
    \rho(A_m)>\rho(A_{m+2})\quad\text{for every finite }m,
    \qquad\text{or}\qquad
    \rho(A_m)-\mu\le f(m)\text{ in }d=2.
\]

This is an absence statement about the audited sources, not a priority claim.

### Theorem-level target

Choose the smallest pair of local memory matrices for which the exact data
show a non-parity transition. Build a common higher-block graph in which the
larger-memory automaton is obtained by deleting a nonempty set of admissible
loop-closing transitions from the primitive recurrent component. Prove:

\[
  \rho(A_{m+2})<\rho(A_m),
\]

and give an exact rational interval containing the gap. A reusable version
would state a graph criterion: if the deleted transition lies in the same
primitive recurrent component and every relevant state can reach and leave it,
then the Perron root strictly decreases. Ramsey's one/two-word SFT estimates
could be used only after the SAW-specific graph correspondence and primitivity
are proved.

This target is feasible with exact small matrices and can expose a genuine
obstruction to claims of “finite memory converges at rate $f(m)$.” It is
lower priority than Target A because strict PF decrease for a particular
finite graph may be a finite computation rather than a new asymptotic theorem.
To make it M3, the result should include either a symbolic criterion reusable
for all $m$ in a family, or an explicit quantitative lower gap that feeds a
new certified bound.

## Target C — uniform anisotropic positive-vector certificate

### What is already known

He gives the weighted matrix theorem and pointwise anisotropic bounds for all
positive weights. The project has already reproduced small symbolic cases and
knows that the weight-preserving symmetry group changes when $x=y$ or other
relations hold. Generic equitable refinement/partition changes and generic
polynomial positivity are not new. In particular, a certificate of the form
“choose $U$ very large and $v=\mathbf1$” would have no scientific value.

### Theorem-level target

For one fixed exact small matrix $A_m(x,y)$ and one compact rational box or
ratio interval $K\subset(0,\infty)^2$, construct rational polynomials

\[
  v_i(x,y)>0,
  \qquad A_m(x,y)v(x,y)\le U(x,y)v(x,y)\quad (x,y)\in K,
\]

where $U(x,y)$ is an explicit nontrivial majorant of the Perron bound and
the inequalities are certified exactly, for example by a Handelman
representation on $K$. The result should state a useful comparison, such as
an interval-wide bound no larger than a specified He pointwise envelope, or a
single certificate that remains valid across the $D_2$ partition strata and
improves the best endpoint-only cover.

The scientific content is the *reusable uniform theorem*, not the generic
existence of a polynomial certificate. A negative result is also useful:
prove that a prescribed low-degree $v$ or prescribed partition cannot be
uniform because a residual changes sign at one of the exceptional weight
ratios. Parent experiments suggest possible exceptional ratios
$\{1/2,1,2\}$ for simple linear edge weights; this should be treated as a
computational conjecture until a symbolic partition proof is written.

## Search limits and safe wording

The literature search was bounded to primary articles, official journal or
arXiv records/PDFs, DOI landing pages, and the authors' publication pages. It
included exact-title and author/title searches for the Bacher–Beaton model,
finite-memory SAW automata, weighted connective constants, entropy perturbation
of finite-type shifts, and polynomial positivity. Some older publisher pages
and the full Alm PDF were inaccessible or only exposed an abstract; those
claims are reported through the accessible primary sources that quote or
extend the method. ResearchGate and author pages were used only as discovery
cross-checks, not as mathematical evidence.

No search hit is evidence of novelty. The defensible statements are:

* Bacher–Beaton's 2014 source explicitly leaves the $P_I$ and $W$
  non-D-finiteness questions unresolved, and no later primary resolution was
  located in this bounded search.
* Pönitz–Tittmann/Couronné/He establish the finite-memory and weighted-Perron
  baselines; Kawamoto establishes a memory-$\tau$ rate in a restricted
  high-dimensional/spread-out setting.
* A square-lattice strict-gap or rate result, and a nontrivial uniform
  anisotropic certificate theorem, remain candidate targets only until checked
  against a broader literature search and exact local computations.
