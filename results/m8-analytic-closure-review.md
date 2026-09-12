# M8 analytic closure review

Status: **ACCEPTED for the analytic milestone integration only**. The full
W theory goal remains OPEN: accessible-to-asymptotic coverage is not
established. The discrete primitive remains an algebraic identity without
a proved sharper moment rate. Ongoing finite derivative work is outside
this closure review.

The reviewed canonical source commit is
`508798858de2a30e8231bcbbe06cecd78c4b2706`. The reviewer read the integration
checker, batch wrapper, canonical metadata, and inherited receipt verifier.
The wrapper freezes the scientific inputs and interval/algebra producers.
The receipt verifier compares every recorded input hash with both the
recorded Git commit and current bytes, and checks each output hash. The
metadata's dirty-working-tree flag therefore does not replace or weaken
the explicit source checks.

Independent execution of `.venv/bin/python -m proofs.check_m8_analytic`
passed. Its output is byte-identical to the canonical
`results/m8-analytic-verification.json`. This execution regenerated the
entire M8 analytic payload and compared it structurally to its canonical
receipt, checked all nine reviewed M8 source hashes against the analytic
review, checked the derivative threshold scope and negative residue
coefficient enclosures, and verified both accepted M7 receipts. These are
provenance and arithmetic checks, not a substitute for the mathematical
review. Both review and checker accurately keep the full scientific goal
open. Optimized execution was separately confirmed to fail immediately
with the required explicit guard, protecting inherited assertion checks.

No mathematical source was edited. The checker does not rerun the M7
finite producers; it verifies their frozen receipts. The complete canonical
M8 input-hash map is in the metadata below, itself hashed here. No
integration blocker was found for this analytic milestone.

## Canonical inputs, outputs and verifier hashes

| Path | SHA-256 |
|---|---|
| `results/m8-analytic-v1/metadata.json` | `b3891689455f68cfaa3fcc17166305f5ef354d341b8c7d02bc7d5877f582ab74` |
| `results/m8-analytic-v1/payload.json` | `2d1bfd90df4247521e0e47d90f427cf950be10b22ebfe9cdb91cf2635eb27441` |
| `results/m8-analytic-verification.json` | `4dc0dcd78cab9d307d35ab56c911e6efc40f41fb10ff72673db0772993655c8f` |
| `proofs/check_m8_analytic.py` | `2314f0a3cddd7752cc61614199826d8834ab1ce7ca880317e28e574437fd7b31` |
| `proofs/check_m3.py` | `fecc450372744eb07ef117a9c044bda0b716f73c27663163f02763117a38ad13` |
| `experiments/m8_analytic_batch.py` | `28ee44cefeb1586621efaec18cbd40ffdc59680921544197fe11f76c01e2a898` |
| `proofs/M8_ANALYTIC_REVIEW.md` | `b96300ff649a887187d7d15de7b76cba9ba75057ad9b49005a106779d03ddc8f` |
| `results/m7-effective-v1/metadata.json` | `dc7b7407d502522942f33532cba895b643d0a6f980d64399867f9123c0714021` |
| `results/m7-effective-v1/payload.json` | `1de734badeb7cd514d3618b8684064e5bdc5cbf7d626091153fed2dae1ae05e8` |
| `results/m7-finite-v1/metadata.json` | `acd3d51f2b8f3e247ad555afd4b05d4be8e4aa1b63b6c917293e8f02c44dbd9c` |
| `results/m7-finite-v1/payload.json` | `75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f` |
