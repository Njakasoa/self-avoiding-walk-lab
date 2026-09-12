# Independent M6 closure audit

Decision: **accept closure of M6 at the internal research-draft gate**,
under the stated scope of a second logarithmic correction and substantial
structural reduction of the sufficient existence threshold. No analytic
blocker remains in the reviewed inputs. External peer review, priority,
and a computationally useful low-index threshold are not achieved.

## Requirement coverage

1. The independently accepted directed constant theorem supplies the
   required uniform O(e log(1/e)) remainder. It discharges the conditional
   input in the earlier second-order transfer review.
2. The phase correction C2 and spatial term have the reviewed signs and
   formulas. The exact enclosure [.844491934033,1.148455190184] comes
   from interval arithmetic, not a finite fit. The resummed phase theorem
   determines each fixed logarithmic coefficient; it does not claim a
   uniform expansion to arbitrary order or a second-order residue theorem.
3. The accepted sign argument removes the exponential product loss; the
   absolute moment comparison and B=10^12 analytic box give N0=10^46.
   This is a structural reduction of the M5 proof, rather than a mere
   replacement of one exponent in its old bound. The common moment
   domain e<=10^-10 is explicit. The threshold establishes existence and
   numerator noncancellation only; eventual uniqueness and simplicity
   remain without a new effective index. Computationally useful small-N
   coverage is explicitly not achieved and remains further research.
4. Predictions and protocol were frozen before the N=1024 run. Independent
   provenance and Decimal checks reproduce the resummed PASS and truncated
   FAIL with no refit. The overall diagnostic status remains fail. N=512
   is correctly treated as previously observed; midpoint predictions and
   tiny finite residuals are not promoted to interval proofs.
5. All new analytic components and final aggregation have independent
   internal reports. Five receipts and eleven reviewed source hashes
   pass integration verification, along with unchanged legacy hashes.

M6_ACCEPTANCE.md, M6_STATUS.md and CLAIM-0009 express these scopes
consistently. The plan's useful-threshold ambition is acknowledged as
unfulfilled, not disguised as a practical consequence of 10^46. The
stated completed requirement is substantial analytic reduction together
with the second-order theorem, matching the scope clarified during review.

## Independent final replay

I ran `.venv/bin/python -m proofs.check_m6`. It passed and its complete
JSON output equals results/m6-final-verification.json, with identical
SHA-256. This replays exact coefficient/threshold arithmetic and
calibration, not the expensive actual N=1024 run. The held-out provenance,
chronology, preserved errors and residual scope were independently audited
in M6_HOLDOUT_REVIEW.md. The code-verification receipt records 54 passing
regression tests, compilation of ten M6 modules and three optimization
guard rejections; these are the integrator's recorded checks, not a new
regression run by this reviewer.

| Reviewed file or output | SHA-256 |
| --- | --- |
| M6_ACCEPTANCE.md | `4bb0decc203756891e3ad6944b32e9fd7e6600b9e12239aad8806d4074189de5` |
| M6_STATUS.md | `4f8f34745371890a2c89834328d0c0f1162671873789a9e4f8757c8e6531575f` |
| M6_PLAN.md | `b23deaa88ff14ed8fe3b256bbe0b03ddf830b9987a50e9316afa5a973e45d701` |
| claims/CLAIM-0009.md | `71bed157fefc2e168d2af506d050dde7954a6b18a1c7b5107c6c1b0d84550361` |
| proofs/check_m6.py | `c96bd1ed20600df24069160ff81ba6ff852d64f9c91df77480a080b3ad171f73` |
| results/m6-final-verification.json and independent replay | `b56efd9e7f66ddf65610ba43d91465610f83d31b114bf788b1859137b02fddca` |
| results/m6-code-verification.json | `ff9b5b7dd827d7a7669386bcb1b44555924cf20f767f934ddf31ca3eca23e5e6` |

Independent replay path: /tmp/m6-final-review-replay.json.
Document hashes above identify the pre-closure wording containing pending
and ACTIVE statuses. The integrator may replace those administrative
statuses by accepted/completed and append memory/log entries after this
gate. This permission does not cover changes to mathematical source bytes
or enlargement of the reviewed claims. The remaining research directions
are low-index interval coverage, effective derivative/uniqueness bounds,
and stronger algebraic error control for the resummed approximation.
