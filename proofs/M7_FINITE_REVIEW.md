# M7 finite pole certificate review

Status: **ACCEPTED finite six-index existence and noncancellation certificate
at the internal research-draft gate.**
The reviewer independently replayed N=32, including both endpoints and the
whole bracket. No uniqueness, simplicity, intervening-index coverage,
effective threshold, novelty, or publication claim is accepted here.

Review context: baseline M6 `a7fa96f`, root source commit
`88f78185e86ab4b2870264d16eea8ad96d981674`. The two reviewed files were
uncommitted additions at that source commit; their hashes below identify the
actual reviewed content. Frozen M3–M6 files were read only.

## Mathematical checks

The divided differences defining V1 and V2 agree with the exact regularized
identities in `M3_NON_DFINITE_CANDIDATE.md`, Section 4, including the signs
of the boundary terms, Q, S0, and the extra t² in H. The finite weight box
covers every u between t and q, and its enforced positivity and upper
bounds do not depend on an asymptotic N threshold.

The g and h phase inequalities exclude integer source poles throughout
the whole bracket. Physical kernel discriminants and every evaluated
recurrence denominator are checked. The finite prefix verifies positive
recurrence ratios, preserving z<0. At the tail start, checked g>0 and
monotonicity of U(t,v) in real v give 0<g<=t²q thereafter. The identity
q(q-t)+(1-q²)=1-tq proves the limiting ratio r² exactly. Thus the geometric
remainder using final |z_M|, the whole weight boxes, and 1/(1-r²) covers
the complete omitted sums. The final bound is checked directly, independently
of the exponent search. The bound 3 tail_P+4 tail_H is valid since on these
positive t<1 brackets and 0<D_I<1, |3-t-2D_I|<3.

The directed summand denominator is affine in q^(2k), so its minimum over
[0,1] is bounded below by the smaller positive endpoint lower bound. Its
positive geometric remainder is appended with outward rounding. D_I includes
that remainder before forming F; the additional prudent tail is then included
in F_certificate and P_plus_one_certificate. The whole-bracket negative
numerator certificate is stronger than endpoint noncancellation.

Local holomorphy follows from source-pole exclusion for a finite prefix and
uniform convergence of q(t)^(2n) to zero on a sufficiently small complex
neighborhood. The recurrence ratios consequently converge uniformly there
to r(t)², whose modulus is strictly below one at the real center. Shrinking
the neighborhood gives a strict geometric majorant, and the rational weights
remain bounded. The directed tail has the analogous local majorant; 1+D_R
is nonzero locally because it is positive at the real center. This justifies
the pole inference from a zero of F and nonzero 1+P; it does not certify the
order of that zero.

## Independent checks and evidence

An independent Fraction oracle exercised 500 reproducible random rational
interval pairs (seed 72026), checking addition, subtraction, multiplication,
reciprocal and division against exact corner extrema, and square-root
endpoints by exact squaring. All passed. Six negative inputs were rejected:
zero-containing reciprocal, negative square root, nonpositive logarithm,
negative integer exponent, an unsupported index, and reversed indices.
Three logarithm enclosures also satisfy the independent elementary bounds
x-x²/2 <= log(1+x) <= x for x=10^-6,10^-3,1/10.

Independent reviewer execution of `produce([32])` passed in approximately
four seconds. Its deterministic JSON receipt covers endpoint F signs,
whole-bracket P+1, phase exclusion, and both complete tails. The root's
separate original-versus-regularized N32 moment receipt was inspected; it
records overlapping full P and H enclosures. That original-formula replay
is root evidence, not a second reviewer implementation.

| Artifact | SHA-256 |
|---|---|
| `proofs/m7_finite_poles.py` | `3712829fbf510e558e9215c7219731b40678ca9525e36387bb1f9d528f912c26` |
| `proofs/M7_FINITE_TAIL.md` | `89869ff06633e9a9daa17ca63f848d47fcf3ba5b5c18aee1ee48b151347e48d7` |
| `/tmp/m7_review_arithmetic.py` | `7bcfe12e9524da1230cb8852b88900e3754a87659c89a0890c02b8b7732d0d92` |
| `/tmp/m7-review-N32.json` | `37c8bb91d60df19fd128e4e6f8d9343aca60a89bc694b8081f9f755a07074125` |
| `/tmp/m7-independent-N32.json` (root evidence) | `e7aecafc0fc020fd09c5147779b50cd1deef1861072f38ffe9d8aa7e4cf95cd7` |

Temporary receipts should be copied into the final evidence bundle if they
are to be retained. Complete six-row output hashes belong in the root's
acceptance record after that replay finishes.

One nonblocking API observation: `produce` accepts repeated sorted indices,
although its error text calls the input an increasing subset. This cannot
invalidate any row or the default six distinct indices. Rejecting duplicates
would make that interface wording exact. No producer changes were made by
the reviewer.

## Six-row execution addendum

The root completed the full six-index exploratory replay successfully. The
reviewer independently inspected `/tmp/m7-finite-six.json` and checked its
exact index list, all positive left F endpoints, all negative right F
endpoints, and all negative whole-bracket P+1 upper endpoints. Its SHA-256
is `75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f`.
This discharges the six-row execution condition above. The canonical frozen
receipt is being generated separately by the root; final receipt provenance
and equality remain integration checks, not additional mathematical claims.
