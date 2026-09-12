# M8 independent analytic review

Status: **ACCEPTED at the internal mathematical research-draft gate**, for
precisely the scopes and source bytes below. This is an independent agent
review, not external peer review, a novelty determination, or completion of
the full W theory. The frozen baseline is commit
`f925ac6142604fd15d7d9d830b9193aecb3d31ac` (M7_END). The reviewer changed
only this review; frozen scientific sources were read-only.

## Accepted scopes

The complex joint moment norm is below 10^8 on the stated rectangle for
all integer N>=10^30. The Chebyshev transfer proves joint phase derivative
error below 1.033 at N>=10^57, and thus exactly one simple noncancelled
restricted W pole in each specified phase band at that threshold. The
explicit phase bound applies to every root in the band already at
N>=10^46; its spatial bound uses the full analytic kernel. The resummed
normalized residue has the displayed explicit error at N>=10^57 and
asymptotic error O(N^-1/4 log²N). The first inverse-log residue correction
and its negative interval enclosure are accepted; the separate coarse
finite residue interval in that note is accepted at N>=10^120. Section4
of the resummed residue note extends that interval to N>=10^57; this
stronger finite statement is also accepted.

The discrete primitive and its finite summation-by-parts identity are
accepted algebra. Its infinite version requires the stated decay and
polynomial-envelope hypotheses. It supplies no improved moment rate yet.
None of these conclusions covers the finite-to-asymptotic gap, every
possible phase sector, or unrestricted square-lattice SAWs. Finite
interval derivative work is outside this review.

## Independent analytic audit

The M7 domain ledger uses smallness inequalities, not a limiting argument
specific to 10^120. At e0<=10^-30 the kernel-sector domain, exterior
separations, crossing half-tube and parameter disks all retain their
margins. The accumulated smooth logarithm allowance is at most .1<1/2.
The factor count also covers the prefix at ceil(4/epsilon). The same
scalar estimates preserve damping and the full-recurrence tail contraction.
The common cutoff 60N proves normal convergence at each fixed N. The
joint compact, tail and boundary ledger totals 84,800,100<10^8. The
critical complex norm below100 follows on the entire rectangle from its
explicit sine bounds, although the original M7 note states a smaller
neighborhood as its primary domain.

The chosen ellipse is strictly within that rectangle. Laurent coefficient
extraction on one contour bounds the vector Chebyshev coefficients by
2M q^k in the joint norm. Absolute derivative convergence follows from
the convergent sum k²q^k. Pointwise real signs reduce the vector polynomial
Markov bound to its scalar version, with the theta scale factor20. Thus
20m²(E+A_m)+B_m is a valid uniform derivative estimate including endpoints.
The transfer identity does not require E1<=1 before its final substitution;
1.033 still gives a strictly negative derivative with magnitude above1.

The phase equation and .3<s_g'<.4 give theta-m_e in(.4,.6). Its logarithm
error is bounded by .6/N. The directed remainder is bounded through the
increasing function x log(1/x), not by differentiating a remainder.
Both reciprocal denominators exceed logN/sigma; 102sigma²<19 proves the
reciprocal allowance. The denominator comparison then costs 4E, 2/N²,
and 285/(N logN). The critical derivative margin27/5 and endpoint signs
justify existence, uniqueness and inverse stability for the approximate
root. The spatial derivative bound follows from the even analytic kernel
expansion and exact inverse phase derivative.

For the residue, the exact identity is -p_N t_N'/F_N'. The Jacobian
normalization tends to j0=s*²/8, with error below1/N and upper bound.004.
The derivative comparison includes moment errors, the t parameter term,
the t derivative term, directed reciprocal error and directed derivative
error. The phase shift costs1200R_theta: the affine profile identity
F_hat''/F_hat'=B''/B' and the inherited whole-sector derivative enclosure
justify that bound. The three quotient changes use |F_N'|>1 and
|F_hat_N'|>27/5 separately, so they remain valid for any integer m>=1,
even when that m gives an unhelpfully large E1. Choosing ceil(logN)
produces the claimed rate because log(22/15)>1/4.

Expanding the exact residue quotient gives
r1/r0=c1 F0''/F0'-4sigma P0'/F0'. Substitution of B'=kappa_B Q(B)
and p=p0+post1 B gives exactly the combined numerator in equation(M8.18).
This confirms the signs and avoids spurious interval dependency loss.
The additive directed constant first enters at inverse-log order two.
The finite residue size estimates use the correctly oriented phase
Jacobian and numerator/denominator bounds. The discrete primitive also
has the correct n=0 boundary; direct recurrence subtraction proves all
subsequent indices. No rate is inferred from this algebra alone.

The final Section5 elimination is also accepted. Put K=J+2delta s
and C=C0+2delta p0. At the approximate root, p=H/K and
F_hat'=K*kappa_B*Q(-C/K), giving exactly -j0 H/(kappa_B D).
Here K is nonzero on the stated domain because F_hat' is nonzero.
At delta=0, D0=J²Q(B(theta*)) is nonzero. Multiplying the proposed
inverse-log series by 1+a1/L+a2/L² gives coefficients r0, 2b r0,
b²r0 and zero thereafter, exactly the rational numerator. This proves
the displayed recurrence, including its exceptional first two terms.
Analyticity at 1/L=0 and the separately proved algebraic error justify
every fixed-order asymptotic coefficient, with no claim of uniformity
as the number of retained terms grows.

## Arithmetic replay

The reviewer independently ran both producers with `.venv/bin/python`.
The threshold producer's normal and optimized outputs were byte-identical.
A separate rational script recomputed the geometric moments underlying
its derivative tail, checked the strict uniqueness allowance, checked both
coarse residue endpoints, the resummed quotient coefficient and Jacobian
allowances, and tested the discrete identity exactly on two rational
parameter pairs (including changing product signs). All checks passed.
The resulting derivative bound is approximately1.032293710817869; that
decimal is only a summary of the exact rational calculation. The residue
producer reproduces the outward intervals displayed in its proof note.
The symbolic identities and analytic argument above, not those finite
identity tests or decimal summaries, support the infinite statements.

The final added residue checks also pass in normal and optimized modes.
An independent replay of the M7 endpoint derivative certificate confirms
|F0'|<26 by its analytic monotonicity; hence |F_N'|<31 at10^57.
The bounds J_N>.0028 and J_N<.004 give the stated coarse residue
interval already at10^57.

The final symbolic algebra producer was read and independently replayed;
normal and optimized outputs are byte-identical. Its exact cancellations
check the eliminated residue, agreement of the first coefficient, the
recurrence through order7, and the bare primitive step and initial value;
rational weighted finite sums also agree. The general recurrence follows
from the analytic argument above, not merely those eight coefficients.

Canonical receipt creation and committed-source provenance remain root
integration obligations. Temporary replay files below identify review
evidence, not canonical archival receipts. No unresolved mathematical
blocker was found in the listed analytic scopes.

## Reviewed source and output hashes

| Source/output | SHA-256 |
|---|---|
| `proofs/M8_COMPLEX_DOMAIN.md` | `f0805eb13495486eed4a9c8809d4bebfba2dac16e4dc65345da905a17eac6283` |
| `proofs/M8_CHEBYSHEV_THRESHOLD.md` | `3a48d150a12b8ac7eaa103bb02b70a491a4f0c15f4b4a98c4c5543336a59c5da` |
| `proofs/M8_EFFECTIVE_PHASE.md` | `359c116ffa597319463fa0c439d55793d35c7e7f00a5727580bbbf3004ce3e04` |
| `proofs/M8_RESUMMED_RESIDUE.md` | `6337a164bebed858331895da68b89bf0d259f5dffae669db189d99e28a7db15b` |
| `proofs/M8_DISCRETE_PRIMITIVE.md` | `284365adf0c8ce26bc93205e110b5788080f7237659e1ce9ccd9358340341488` |
| `proofs/M8_RESIDUE_EXPANSION.md` | `1d1e864f2184900d4cae5359dc817306691d3bcd81090c5214fa8ca6cadb02da` |
| `proofs/m8_chebyshev_threshold.py` | `a8a8dbbeb8020643a00f13ad2726c8e7a31e20f74d0b5730e6a1caf882a55a3f` |
| `proofs/m8_residue_coefficients.py` | `97d17a3cb0e8a457652d8fdda046bda18b51853eafc7a19cee24b73a44a80cf2` |
| `results/m5-critical-v1/payload.json` | `f94823cf257ffd1c9cf6becea60c07cad100232b787e4253ba7d18681557fd8b` |
| `proofs/M7_EFFECTIVE_REVIEW.md` | `2ece28c0515e21d05c9ccc7fda53fc05ddb1e3f4e0ebdeb6e07fa92274d35ba9` |
| `proofs/M7_EFFECTIVE_DERIVATIVE.md` | `e79045816d8ec87313584ba8bc960ff09833e299071013c9cf84fae1903df7d1` |
| `proofs/M7_COMPLEX_SCALARS.md` | `53fa59586ba44673d5904190f4ee3fc556b826677c6053f6ddc08e5a82060c38` |
| `proofs/M7_COMPLEX_KERNEL_SECTOR.md` | `0c1b006aa6d202bc89345b9d0ba194ce8502c504497061007acdca548d59bfe3` |
| `proofs/M7_COMPLEX_PRODUCT_DOMINATION.md` | `c366bb558d128ecdeb8f43de5c1c261df1d1807f3559c6a5d50a76e1b796864c` |
| `proofs/M7_REAL_TO_DERIVATIVE.md` | `7e34ef6f8aeaf78cccce82a1aa6aae059ef09e676834de066649506ae6c685f5` |
| `proofs/M7_UNIQUENESS_TRANSFER.md` | `641806191be795952a15c2062f5e7a6e5f836f14a087768cb35f9e92bd1c24e0` |
| `/tmp/m8-review-chebyshev.json` | `3a00d9704d3dd1b196dce07bc1ee12ab028d21f55a122e4ec23ea8f5691e8740` |
| `/tmp/m8-review-residue.json` | `b00c18a7e2d7296e8045861b92230f13114c0406b6c3c93d41f4d53c2506a5fa` |
| `/tmp/m8_independent_review.py` | `d0fd627c7df2593ef483cadbb01628db536bf4cfd097b9ff99a653f775ce21ff` |
| `/tmp/m8-review-independent.json` | `1d46ece348a7c14295a0a4a10268b5dd5dc0e6f9c2b539f25346234e5b9561ea` |
| `proofs/m7_uniqueness_transfer.py` | `94701dd179348f267366d8f90efd014976d05d3aa2c45e9d6e428f12d11ab73b` |
| `/tmp/m8-review-critical-derivative.json` | `abe372241ae59cc56e5c029357545e305264d847867ab7d9e0d18f9221a0a1c0` |
| `proofs/m8_algebra.py` | `80072392adc1d6096c6f322ff752d492d97887425df0e60c6627bf835dfc3bbb` |
| `/tmp/m8-review-algebra.json` | `c36fab70d96461e7f24e9405efad1ed11379fe36517057e8afc7aab8ee1fb307` |
