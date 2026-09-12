# Independent directed monotonicity and structural arithmetic review

Verdict: PASS. Directed monotonicity on 0<t<sigma and the exact basepoint
bound imply delta_D<.07 for every N>=32 in the stated phase sector.
The stronger combined-weight gap and fixed-parameter logarithmic u slope
follow. This supplies no full F_N phase-derivative sign or index coverage.

The shifted Chebyshev formula is correct. The solution of the normalized
recurrence is (1-t)U_k-t U_(k-1); subtracting consecutive U polynomials
and using Pascal's identity gives exactly the two nonnegative binomial
sums displayed in the note. Their constant terms already imply g_k>=1-t.
On 0<t<sigma, y>0, y'<0, 1-t>0 and 1-2t>0. Each g_k decreases strictly,
so t/g_k increases strictly. Positive partial sums preserve monotonicity
in the limit, and the strict increase of the first summand preserves
strictness for the infinite sum. No interchange of derivative and sum is
required. Independently expanding the recurrence and proposed formula
with SymPy gave identical polynomials for k=0 through 12; the general
recurrence/binomial argument, rather than these examples, proves the claim.

The I384 basepoint replay passed independently. It verifies e in (0,.01),
a(t0)<32.8, and D_R(t0)>93/7 with a complete directed tail. For readability
only, the lower directed endpoint is approximately 13.544393193535354 and
the upper a endpoint approximately 32.02415488419348. The directed sum
used 30720 terms. The basepoint and every physical N>=32 phase point lie
on the inherited monotone real inverse branch, so their phase ordering
implies t_N>t0. Applying the proved directed monotonicity then establishes
the bound uniformly over all those indices, without extrapolating data.

The strengthened gap is the earlier exact gap plus .06, approximately
.07093400339721806>.07. The displayed V1 logarithmic derivative follows
from its factored rational formula; its positivity reduces to 1-h>0.
Differentiating the exact ratio R gives the displayed two positive terms.
Independent denominator bounds use 1-tu>=1-.4143 and
1-tuh>=1-.4143*.71, while 1-h<=.294. Inserting these in the quotient
derivative bounds yields an upper allowance approximately
15.523242448290235<16. These derivatives hold t,q,delta_D fixed.

I also audited every Fraction/SymPy check in m10_structural_bounds.py
against the combined-weight and harmonic proofs. The scalar estimates,
weight-ratio identity, paired harmonic loss, logarithm bounds and negative
prefix margin agree with those proofs. The script properly distinguishes
arithmetic/algebra from the phase inverse and beta sign inputs.

Independent sorted JSON output hashes:

- m10_directed_monotone: f0210db9efbf79dbf5bc4ce6d871520c1b93238fad0ec7cda69993e225294c88.
- m10_structural_bounds: 49db78a15baa982f91cf2ada380c302fd404a743ba445788932ef89bf62c1093.

Reviewed source hashes:

| File | SHA-256 |
|---|---|
| proofs/M10_DIRECTED_MONOTONICITY.md | 2f7a47aa316b10fc119d3bb7d6b11b4005b7b2234a2321696eecf01f37c4cc61 |
| proofs/m10_directed_monotone.py | 61419e5bdcd208c901166fb738f60aea9020e7b358c80aa65f3d3b1bee7bbb00 |
| proofs/m10_structural_bounds.py | 5985b3f78179d50674c5497c7e425d44a42df1cfadc8470c6bb7308bf73df8e7 |

No producer or scientific proof was changed by this reviewer.
