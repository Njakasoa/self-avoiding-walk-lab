# M3 non-D-finiteness priority audit — irreducible prudent ramps

Audit date: 2026-09-12. Scope: a bounded primary-source priority audit for
the under-review candidate in `proofs/M3_NON_DFINITE_CANDIDATE.md`. The target
is

\[
J(t)=\frac{P(t)-H(t)}{1+P(t)},
\]

where \(P\) is the NE-prudent-ramp generating function and \(H\) is the
hook-ramp function denoted \(\widetilde P\) in Bacher–Beaton. The candidate
claims infinitely many poles of \(J\) accumulating at
\(\sigma=\sqrt2-1\), using matched Gamma products, a critical phase, and
certified limiting integral signs. It concerns \(J=P_I\), the irreducible
NE-prudent-ramp series. It does **not** prove the additional weakly prudent
bridge quotient \(W=I/(1-I)\).

This file records evidence and limits. It does not certify the candidate proof,
priority, or publication readiness.

## Priority verdict

**Status: UNRESOLVED, conditional M3.** The only primary source located that
directly defines this exact \(J\) is Bacher–Beaton (2014), and that source says
explicitly that it cannot conclude that \(P_I\) is non-D-finite. It likewise
leaves non-D-finiteness of \(W\) unproved. No later primary article, full
version, or theorem citation resolving \(J\) was located in this bounded audit.

That result is evidence that the candidate addresses a documented gap. It is
not a novelty certificate: author lists and indexed searches can miss an
unpublished, differently titled, or inaccessible follow-up. If independent
review validates every analytic and interval step in the candidate proof, the
safe provisional wording is:

> “We prove non-D-finiteness of the irreducible NE-prudent-ramp generating
> function \(J=(P-H)/(1+P)\), a question left open in Bacher–Beaton (2014).”

The words “first” and “resolved” should remain conditional until a broader
citation and author check is completed. The result should not be described as
a proof for \(W\), for the full weakly prudent bridge generating function, or
for general prudent walks.

## What Bacher–Beaton actually establishes

Primary source: Axel Bacher and Nicholas R. Beaton, *Weakly prudent
self-avoiding bridges*, FPSAC 2014, DMTCS Proceedings AT, 827–838:
[DMTCS record](https://dmtcs.episciences.org/2445),
[official PDF](https://dmtcs.episciences.org/2445/pdf),
[author-hosted PDF](https://www.nicholasbeaton.com/papers/BB2014.pdf),
[DOI](https://doi.org/10.46298/dmtcs.2445).

The paper gives, in §2.2 and equation (5),

\[
W=\frac{I}{1-I},\qquad I=4P_I-2D_I-t,qquad
P_I=\frac{P-\widetilde P}{1+P}.
\]

Propositions 14 and 16 express \(P\) and \(\widetilde P\) through infinite
sums of algebraic functions. Theorem 17 (p. 836) proves that both \(P\) and
\(\widetilde P\) have infinitely many simple real poles \(t_{2\ell}\) in
\([\rho,\sigma)), accumulating at \(\sigma=\sqrt2-1\), and therefore both
are non-D-finite. Immediately afterward, the authors state that equation (5)
does not let them conclude that \(P_I\) is non-D-finite, although they expect
that it is. Section 4.2 says similarly that they cannot prove that \(W\) is
non-D-finite.

This distinction is essential. The common simple poles of \(P\) and
\(\widetilde P\) do not themselves prove a pole sequence for \(J\): when both
have a genuine simple pole and the denominator residue is nonzero, multiplying
numerator and denominator by the local parameter makes the quotient analytic.
The candidate therefore needs its separate zero-family argument for
\(1+P=0\), its non-vanishing check for \(P-H=-1-H\), and its uniform
all-\(N\) continuation/integral estimates.

The same source calls itself an extended abstract and says in §3.4 and §5 that
full details would appear in a longer version. The DMTCS record identifies it
as the 2014 conference paper and links the HAL version; it does not by itself
document a later full version. Thus the extended-abstract remark is evidence
of an intended historical follow-up, not evidence that such a follow-up was
later published.

## Candidate-proof scope and review gates

The under-review local proof has a substantially sharper claim than the old
pole-cancellation target:

1. It sets \(t=t(\varepsilon)\to\sigma^-\), chooses phases
   \(a=N+\theta\) in a fixed interval, and factors the exact recurrence for the
   coefficient ratios into a Gamma term and a nonsingular product.
2. It derives a limiting product profile on the two sides of the critical
   crossing, with a singular exponent \(\eta=1/\sqrt2<1\). The exponent is
   intended to make the critical crossing integrable rather than produce a
   hidden point mass.
3. It regularizes the two moments defining \(P\) and \(H\) before taking the
   limit, then uses outward dyadic interval integration to obtain endpoint
   signs for \(1+P_0(3/10)\), \(1+P_0(7/20)\), and a positive lower bound for
   \(1+H_0(\theta)\) on the whole phase interval.
4. If those uniform limits and signs survive review, continuity gives one root
   \(r_N\) of \(P(r_N)=-1\) in each disjoint phase interval. Since
   \(P-H=-1-H\ne0\), each root is a non-removable pole of \(J\). Infinitely
   many finite-plane poles contradict D-finiteness.

The proof file itself labels these steps **CANDIDATE PROOF UNDER INDEPENDENT
REVIEW**. Priority must remain conditional until the following gates pass:

* source formulas and notation \(H=\widetilde P\) are transcribed exactly;
* the \(t(\varepsilon)\), root-phase, and uniform Gamma-product limits are
  proved with all parameter dependencies controlled;
* the crossing estimate is strong enough for the stated Riemann-sum limits;
* the outward interval integral implementation and algebraic endpoint
  cancellations are independently reproduced from source-frozen inputs;
* the signs imply an all-(N) sequence, rather than only the finite numerical
  probes; and
* the final D-finite obstruction uses the analytic germ and its continuation
  correctly. No conclusion for \(W\) follows automatically.

## Later primary-source audit

### Exact-title and full-version checks

Queries used on 2026-09-12 included:

* `"Weakly prudent self-avoiding bridges" Bacher Beaton full version`
* `"Weakly prudent bridges" "P_I"`
* `"Weakly prudent self-avoiding bridges" citing`
* `"weakly prudent" bridge Bacher Beaton prudent walks`
* `"weakly prudent bridge" -ResearchGate`
* `"P_I" prudent ramps generating function`
* `"irreducible prudent ramps"`
* `site:arxiv.org "Weakly prudent self-avoiding bridges"`

The exact-title locations checked were the
[DMTCS proceedings record](https://dmtcs.episciences.org/2445), its
[PDF](https://dmtcs.episciences.org/2445/pdf), the
[HAL record](https://hal.inria.fr/hal-01207571), the
[arXiv exact-title search](https://arxiv.org/search/?query=Weakly+prudent+self-avoiding+bridges&searchtype=all),
and the authors' publication lists:
[Nicholas Beaton](https://www.nicholasbeaton.com/papers.html) and
[Axel Bacher's 2017 CV](https://lipn.fr/~bacher/cv-fr.pdf).

The DMTCS record and author pages return the 2014 item. Beaton's page lists it
as the 2014 FPSAC publication and does not show a later full paper under that
title. Bacher's dated 30 April 2017 CV lists the 2014 proceedings item among
his publications and no corresponding arXiv preprint in the displayed list.
These are useful dated checks, but absence from a bibliography is not a
nonexistence proof.

### Subsequent primary prudent/weakly-prudent work

The DMTCS record's machine-generated citing-document panel points to
Banderier and Wallner, *The Kernel Method for Lattice Paths Below a Line of
Rational Slope*, [arXiv version](https://arxiv.org/abs/1606.08412),
[published chapter](https://doi.org/10.1007/978-3-030-11102-1_7). Inspection
of that primary paper found a general rational-slope lattice-path kernel
method, not a theorem about \(P\), \(H\), \(J\), or \(W\). This single indexed citing
entry is not an exhaustive citation search and does not affect the unresolved
priority verdict.

Heydenreich, Taggi, and Torri, *Prudent walk in dimension six and higher*,
[arXiv record](https://arxiv.org/abs/2210.03174),
[PDF](https://arxiv.org/pdf/2210.03174), is a genuine later primary source
(submitted 2022, revised 2023). It studies a high-dimensional probabilistic
prudent walk and a penalized weakly-prudent walk. Its main theorem is a
Brownian scaling limit for sufficiently high dimension; it does not use or
resolve the square-lattice bridge generating functions \(P\), \(H\), \(J\), or
\(W\). It is therefore related terminology, not a priority collision.

Bacher and Bousquet-Mélou, *Weakly directed self-avoiding walks*,
[arXiv record](https://arxiv.org/abs/1010.3200), is the relevant earlier
primary precedent: its weakly directed generating function is proved
non-D-finite. The model is distinct from 2-sided weakly prudent bridges and
does not settle \(J\). Bousquet-Mélou, *Families of prudent self-avoiding
walks*, [arXiv record](https://arxiv.org/abs/0804.4843), proves non-D-finiteness
for the third prudent subclass while stating that the general fourth class
remains unresolved. Neither source contains the desired \(J\) theorem.

No primary source located in this bounded pass states “\(J\) is non-D-finite,”
proves the candidate's matched-product phase argument, or supplies a later
full version of BB2014. The absence is reported only as an unresolved search
outcome.

## Known versus desired claims

| Claim | Audit status | Primary evidence |
|---|---|---|
| \(P\) and \(H=\widetilde P\) are non-D-finite | **KNOWN** | BB2014, Theorem 17, p. 836 |
| Weakly directed bridge/walk model has a non-D-finite generating function | **KNOWN, different model** | Bacher–Bousquet-Mélou 2011 |
| A prudent-walk subclass has a non-D-finite generating function | **KNOWN, different subclass** | Bousquet-Mélou 2010 |
| \(J=(P-H)/(1+P)\) is non-D-finite | **Candidate theorem; priority unresolved** | Candidate proof; BB2014 explicitly leaves it open |
| \(W=I/(1-I)\) is non-D-finite | **UNRESOLVED here and in BB2014** | BB2014 §4.2 |
| Candidate is first in the literature | **UNRESOLVED** | No negative search can certify this |

## Conditional M4 wording

If independent review accepts the candidate proof, a cautious M4 draft can
state that it supplies a rigorous non-D-finiteness theorem for the irreducible
NE-prudent-ramp series \(J\), and that the proof resolves an explicit question
left open by BB2014. It should cite BB2014 for the formulas and known
non-D-finiteness of \(P,H\), cite the distinct weakly directed/prudent results
as context only, and label literature priority as pending.

It should not claim a solution for \(W\), the full 2-sided weakly prudent bridge
series, or general prudent walks. It should also avoid saying that the BB pole
sequence survives the quotient: the candidate's new root sequence comes from
zeros of \(1+P\), while the shared poles are locally removable.

## Search limits

This was a bounded first-pass web audit, not an exhaustive MathSciNet,
zbMATH, Google Scholar, Crossref-citation, library, or author-email check.
Search indexing returned the BB proceedings item, author pages, related
weakly-directed/prudent papers, and high-dimensional probabilistic work. A
different title, unpublished longer version, non-indexed proceedings paper,
or inaccessible manuscript could change the priority outcome. The only safe
conclusion is therefore **conditional M3, M4/priority unresolved** pending
proof review and a broader source audit.
