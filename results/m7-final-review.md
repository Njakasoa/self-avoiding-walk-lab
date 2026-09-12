# M7 final independent closure review

Status: **ACCEPTED at the internal research-draft gate.** No remaining
scientific or integration blocker was found. Internal AI review does not
establish novelty or replace external peer review.

The reviewer independently ran `.venv/bin/python -m proofs.check_m7` after
both canonical receipts completed. It passed, and the output was byte-for-byte
identical to `results/m7-final-verification.json`, SHA-256
`6e98d196627fb8d2a2e051341ee49760a6f329845337439924a230a6ae8ac194`.
This verifies frozen/current input bytes and receipt payload hashes, the exact
six-index sign/phase/tail conclusions, effective arithmetic replay, source
hashes covered by the analytic reviews, unchanged selected legacy sources,
full exploratory/canonical equality, the independent reviewer N32 row, and
the original-versus-regularized full moment overlap. The full six-index
producer was not run a third time by the reviewer; the verifier accurately
records `full_finite_producer_replayed: false`.

The canonical finite receipt was generated from
`fc445b368abd297d35b927ca348d2ceb8af72fcc`. Its payload exactly matches the
successful exploratory full-six run. The effective receipt was generated
from `81dcaba1a23d2caf0786a4d0e0af4497bdb561b5`, the HEAD observed during
this closure audit. Both source commitments and their current-file equality
were checked by the independently replayed verifier.

The analytic and finite arguments were separately reviewed in
`proofs/M7_EFFECTIVE_REVIEW.md` and `proofs/M7_FINITE_REVIEW.md`.
The reviewer also read `M7_ACCEPTANCE.md` and `claims/CLAIM-0010.md`.
Their scope is accurate:

- The six exact rational brackets at N=32,64,128,256,512,1024 each contain
  at least one noncancelled pole; these certificates do not prove finite
  uniqueness or simplicity.
- Every integer N>=10^120 has exactly one simple noncancelled W pole in
  its phase band [.8,.9]. The joint phase-derivative error is below .009.
- M6's separate existence-only threshold 10^46 remains in force. The
  accessible-to-asymptotic gap is not claimed to be closed.
- The theorem concerns the restricted weakly prudent bridge series W;
  there is no unrestricted SAW connective-constant or novelty claim.

The acceptance and claim documents still carried “pending final closure”
status during this reading. This report discharges that condition and
permits status-only closure edits and references to this review. Other
changes to scientific statements or reviewed source bytes need fresh audit.

## Audited content hashes

| Artifact | SHA-256 |
|---|---|
| `results/m7-final-verification.json` | `6e98d196627fb8d2a2e051341ee49760a6f329845337439924a230a6ae8ac194` |
| `results/m7-finite-v1/payload.json` | `75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f` |
| `results/m7-finite-v1/metadata.json` | `acd3d51f2b8f3e247ad555afd4b05d4be8e4aa1b63b6c917293e8f02c44dbd9c` |
| `results/m7-effective-v1/payload.json` | `1de734badeb7cd514d3618b8684064e5bdc5cbf7d626091153fed2dae1ae05e8` |
| `results/m7-effective-v1/metadata.json` | `dc7b7407d502522942f33532cba895b643d0a6f980d64399867f9123c0714021` |
| `proofs/M7_FINITE_REVIEW.md` | `ada26cd6d6287839852cb38c3613bb6301e0eaa925ea30c6014d546cd3526f17` |
| `proofs/M7_EFFECTIVE_REVIEW.md` | `2ece28c0515e21d05c9ccc7fda53fc05ddb1e3f4e0ebdeb6e07fa92274d35ba9` |
| `proofs/check_m7.py` | `d0a0056db1e79afd8e415d243bdaef999266adb3d9ed31165062698cb14c5c74` |
