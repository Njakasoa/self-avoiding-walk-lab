# Independent scoped M9 integration closure review

Verdict: PASS for the reviewed M9 analytic/arithmetic package and its
canonical provenance. The full W theory goal remains OPEN. Six narrow
finite brackets and the theorem for every integer N>=10^27 do not provide
continuous integer-index coverage or full-band results at the finite indices.
No exploratory scan is used as proof evidence in this review.

I independently executed `.venv/bin/python -m proofs.check_m9`; it passed.
The returned object equals results/m9-verification.json. A separate fresh
`.venv/bin/python -m proofs.m9_linear_bounds` run reproduced the canonical
results/m9-linear-v1/payload.json byte for byte. The earlier normal/-O replay
and formula-by-formula arithmetic audit are recorded in
proofs/M9_QUANTITATIVE_REVIEW.md; those findings remain resolved.

The canonical metadata names frozen commit
196c66cd6c7c80f0a747789f57c44675e972c0d8. I compared all 29 declared
input files against their bytes in that commit, their current working-tree
bytes and their metadata SHA-256 values: every comparison agrees.
The metadata's git_dirty=true does not indicate changed producer inputs;
the explicit source comparisons establish that all recorded inputs are
identical to the frozen commit. The canonical command and recorded runtime
0.0004655899974750355 seconds describe arithmetic replay only, not the cost
or completeness of the analytic proofs.

All seven assigned scientific/code files match the current hashes explicitly
covered by their independent reviews:

| File | SHA-256 | Corresponding review |
|---|---|---|
| proofs/M9_PRODUCT_VARIATION.md | 4830bf678a5733af94a927db275dda1f9ca61ab5e52d66daac4ac13b700a1ab8 | M9_KERNEL_REVIEW.md |
| proofs/M9_COMPLEX_KERNEL_LINEAR.md | cb383687009961812dbed481071b48ad9c86a1cfc78de424fd8a927b6219ce52 | M9_KERNEL_REVIEW.md |
| proofs/M9_LINEAR_MOMENT_RATE.md | 4510f1e74fec80c9d96018918c1e17e230e7afc7942d496e706255df87dc573c | M9_MOMENT_REVIEW.md |
| proofs/M9_UNIQUENESS_THRESHOLD.md | 099a6838b1afdd73806a25b6d278ba5febc17e418b8f0d8014d5c93bf42fb98d | M9_THRESHOLD_REVIEW.md |
| proofs/M9_PHASE_RESIDUE_RATE.md | 7ff526d4b96128d9afddcae9b0bbc898f9f767a9c9813584b7419010a68ee611 | M9_QUANTITATIVE_REVIEW.md |
| proofs/m9_linear_bounds.py | 4cb493028aeae8c51a32f60693848889296a70c6547feaa44adbc97cf54f1538 | M9_QUANTITATIVE_REVIEW.md |
| experiments/m9_linear_batch.py | 12dd8c5a2ae8c715184bf68cac5b939eb7e4efca52b56a0822cda08407a5ef18 | M9_QUANTITATIVE_REVIEW.md |

Additional audited artifact hashes:

| Artifact | SHA-256 |
|---|---|
| results/m9-linear-v1/payload.json | c3bc0f813ab3dc75fe5a2c1ff48141e188560e082f04212c40e3c8bdf9d9f9cd |
| results/m9-linear-v1/metadata.json | b345e4fdd82763ced306001cffb0a81b5987861cba013229459dfa3c20f883da |
| results/m9-verification.json | 463d4d92aa20319797ae3ed38845044eff2f6bbba05e646b08452ba90c0555e9 |
| proofs/check_m9.py | 0fe9eda27d99ccd7215db09c44279dec341273e946c6dde8062f6cc8dbd6e90b |

The checker correctly guards inherited assertion-based provenance against
optimized execution, recomputes the arithmetic, and verifies each reviewed
source hash. Searching a review for a hash is a provenance check, not a
machine verification of analytic validity; the previously completed
independent reviews supply the analytic assessment. No new scientific
source change required repeating that assessment during this closure pass.

Accepted scoped consequences are the linear real moment error, the complex
norm domain, uniqueness/simplicity for N>=10^27, phase error O(1/N), full
kernel position error O(1/N^4), and normalized residue error
O(log(N)^2/N) relative to the resummed approximation. None resolves the
remaining finite-to-asymptotic index gap or establishes publication novelty.
