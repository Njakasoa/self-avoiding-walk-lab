# Independent M6 held-out result audit

Status: **accepted as a preregistered numerical diagnostic**, with the
resummed comparison passing and the truncated second-order comparison
failing. The canonical overall status correctly remains `fail`.
No finite N=1024 calculation was repeated by this reviewer.

## Provenance and chronology

Every input hash in m6-phase-holdout-v1 matches both the current file and
its bytes in source commit 411b55e4457b9a55b222506b5b303507ce61cc95.
The payload hash also matches. Preregistration commit time was
2026-09-12 13:22:11 UTC; the receipt's start time was
13:22:20.183120 UTC. The provenance implementation records the start,
not completion, in its utc field. Runtime was 243.732061409 seconds.
Together with the prior calibration audit at 7ed5055, this establishes
the recorded prediction/protocol freeze before the observed run.
The dirty workspace flag does not affect the verified source bytes.

The frozen predictions, tolerances, diagnostic settings and calibration
constants are preserved. The validation implementation directly invokes
the finite locator and does not refit coefficients or regenerate the
prediction calibration. Independent audit also verified all input/output
hashes and source chronology for m6-threshold-v1 at commit
e7c18daed5f75b41c97a5ffc72505051d6d31761.

## Numerical comparisons and limits

The reported phase is .826655736217392822902422627418615954.
Independent 80-digit Decimal subtraction against the full frozen
prediction strings gives:

| Model | Absolute error | Common tolerance | Result |
| --- | --- | --- | --- |
| Resummed | 1.8312466890130708277e-6 | 9.3391722709040922412e-6 | PASS |
| Truncated second order | .004969210235650224357 | same | FAIL |

Both stored errors agree to better than 1e-34; the separate flags and
overall failure are correct. The resummed-derived benchmark is empirical,
as discussed in M6_PHASE_PROTOCOL_REVIEW.md. This one comparison neither
proves the asymptotic rate nor refutes the second-order theorem.

The row retains F approximately -2.05e-21, numerical phase derivative
approximately -11.3357, numerator approximately -5.77437, directed tail
quantity approximately 9.9995e-15 and the last prudent term approximately
1.76e-22. These are useful consistency diagnostics. The prudent last
term is not a certified full-tail bound; finite differences do not
certify a derivative sign. The tiny residual is not a rigorous root
enclosure or proof of a pole at N=1024. The separate existence threshold
is 10^46 and does not cover this index. No such stronger conclusion is
accepted here.

## Recorded hashes

| File | SHA-256 |
| --- | --- |
| results/m6-phase-holdout-v1/payload.json | `48c8be37147e9f0e3291d3b2fe336fae56bb615a66bb180be630b257832e4840` |
| results/m6-phase-holdout-v1/metadata.json | `99b7b870972e590e4ddff873ae0e7e0366592b88e2221cc0de9857ac530d2a2b` |
| proofs/check_m6.py | `c96bd1ed20600df24069160ff81ba6ff852d64f9c91df77480a080b3ad171f73` |

I read the integration verifier: it checks five receipts, replays exact
coefficient/threshold arithmetic and calibration, checks eleven source
hashes against review records, preserves legacy hashes, and independently
recomputes the held-out comparisons. Its hash-presence test does not by
itself establish a review verdict; the analytic conclusions remain in
the separately read reports. The final acceptance/status documents are
reserved for the next scope audit.
