# Independent scoped M10 integration closure review

The full-band producer and structural lemmas have passed their separate
analytic reviews. The full-band claim is limited to exactly one simple
noncancelled W pole in the N=32 phase band theta in [.8,.9]. The structural
results apply componentwise for N>=32; they prove no complete denominator
sign and no full-band theorem for unlisted finite N. The full W theory
goal remains OPEN.

## Canonical sources and bounded replay

I independently compared every declared input against both its canonical
metadata SHA-256 and its frozen Git commit bytes. All 15 full-band inputs
match commit 12eeca15f54f77eabf7ac2c7c5d84e9e8c41de94; all 22 structural
inputs match commit ce376e85793887f770b35fc80e180e35f4b2ff18. The recorded
runtimes are respectively 504.5359766820038 and 0.7814437130000442 seconds.
The producer output hashes match their canonical metadata.

The first integration attempt correctly rejected stale documentation
provenance in the original first-cell review artifact. The final proof note
added a frozen input-hash ledger after that first snapshot; its mathematical
argument and producer were unchanged. I reread the final note and performed
a new bounded first-cell replay, recorded separately in
results/m10-full-band-review-first-cell-final.json. The old artifact remains
untouched. The new run finished in 6.352350663000834 seconds and returned
exactly the original result with hash
72e73fcce174b5979afecd73bad594402a110539f0466377893667a8a960a246.
The final note and source hashes are approved in
proofs/M10_FULL_BAND_FINAL_REVIEW.md. No full 128-cell computation was
repeated by this reviewer.

## Certificate mechanism and checker audit

I read check_m10.py and verified its exact reconstruction of all 128
rational cells, outward I384 rounding, neighboring endpoint equality,
outer endpoint phase inequalities and equality of the displayed fractions
to the encoded phase intervals. Per-cell checks cover the real e<.01
inverse domain, a/b source-pole intervals, complete directed/prudent tails,
strict F_t negativity, engine consistency and producer guard records.
It compares every derivative with the separately retained diagnostic scan,
and cell zero with the independent review. These comparisons supplement
the canonical certificate; the diagnostic is explicitly not the certificate.

The M7 transfer checks the frozen hash, exact narrow bracket, opposite
endpoint signs, source-pole flag, negative whole-bracket numerator, and
strict containment in the outer interval. Its accepted phase box lies in
the target band. Thus the retained M7 zero is the unique simple zero in
the certified outer interval, and its nonzero numerator makes it a W pole.
The checker replays only inexpensive structural producers, compares their
three component hashes with independent reviews and verifies current
source/review hashes. Scope checks preserve the single-index conclusion
and the open full-denominator/index-coverage obligations.

## Artifact hashes

| Artifact | SHA-256 |
|---|---|
| results/m10-full-band-v1/payload.json | c682f989fac39045ce3232b3097c657d30797585672bdb82ef43e4cd4d34f30f |
| results/m10-full-band-v1/metadata.json | ff67333b04d9396618ef827c136101f8c0e1b13c961dbd70407edb55d161369a |
| results/m10-structural-v1/payload.json | 57f731f971f887b4853464ce604cbcf2da24bc0f5217162980d30d15fb43ef81 |
| results/m10-structural-v1/metadata.json | 04bbfae7768bdd61b5e3145e836244909fab79dc8ee9808bcda7dd532c768728 |

Final checker replay and comparison to the root verification artifact are
recorded below after the documentation-snapshot path is updated.

The updated checker was independently replayed and PASSed after selecting
the final first-cell artifact and final proof review. It verified all 128
canonical derivative records, their diagnostic matches and the exact
first-cell match, without rerunning the full producer.
Reviewed checker SHA-256:
bc7d3ce79affbca1c1b52e8f16cf0b68d8a142a93227b21669a7e164baf189fa.
Independent sorted checker JSON SHA-256:
2de751e7a0020edb9afa8ba7a3a5f1899b131a74ecb7048fd9b18da6fe7655e9.

The root results/m10-verification.json is now present and has the same
SHA-256 as the independent checker output above. Final scoped verdict:
PASS. N=32 has full-band uniqueness/simplicity and noncancellation; no
new N>32 full-band conclusion is asserted, and the full goal remains OPEN.
