# W final integration review

Date: 2026-09-12. Internal AI mathematical and reproducibility review only.
Novelty and publication priority remain **UNRESOLVED**.

## Source review

No new analytic blocker was found. The main proof is unchanged from the
accepted SHA-256 recorded in `proofs/W_ASTRA_REVIEW.md`. The separate
`proofs/W_DIRECTED_RAMPS.md` supplies the same valid recurrence solution,
positive real summands, normal convergence in local complex neighborhoods,
critical harmonic divergence, and uniform phase-family limit used there.
The beta/gamma notation in that note differs from alpha/beta in the main
proof, but the formulas coincide.

The independent implementation in `experiments/w_phase_probe.py` reproduces
the explicit BB2014 P and H sums and product indexing in the reviewed
manuscript. Rationalization chooses the same physical kernel branch. The
inverse-kernel phase formula, direct G recurrence and construction of F
are consistent with the proof. The diagnostic setting D_I=1 is kept
separate from actual finite D_I values.

The `experiments/w_research_batch.py` driver includes its executed local
dependencies, proof inputs, dependency lock and archived source PDF in
the source manifest. The shared receipt writer rejects source files that
differ from the recorded commit before running the producer. Computational
assertion success is explicitly separate from independent verification.
The optimization guard prevents a critical run with disabled assertions.

The exploratory sweeps do not prove finite poles. In particular, a numerical
sign change between endpoints does not certify continuity free of intervening
source poles. The analytic proof supplies the eventual band argument
independently. Observed negative F(0.8) for N=8,16 are retained rather than
discarded; positive values for N=32,64 do not establish an effective first N.

Two numerical-reporting limits are relevant: `doubling_drift` compares
32-digit serialized values, so zero means agreement at displayed precision,
not equality to all 90 working digits. The time limit is checked between
large calculations rather than interrupting their inner loops. Neither
limitation affects the analytic theorem or changes these runs from
exploratory evidence into certificates.

## Frozen receipt verification

**PASS.** Independently checked all four completed receipts against source
commit `9a63181dc11100fa4dfccdea510650976383ffb3`. Every recorded input hash
matches both the committed bytes and the current workspace file; every
recorded output hash matches its payload. The main proof remains at its
accepted SHA-256 `351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a`.
Dirty output/documentation files do not invalidate this explicit source-byte
verification.

| Receipt | Verified payload SHA-256 |
| --- | --- |
| w-identities-v1 | `4f10effbe0d6dd04ed41228d50bcfa1640e450e2ea3e7a12c6d6f4f09fd554fa` |
| w-critical-v1 | `ab5cbc0caf0f24f5b32e877668e87cc2d4d75cd830c62123ad450711f0c7ed6c` |
| w-phase-v1 | `fd304ce9c064561c3de61779d68e415079f01906923ec3490af01a78e5894ef6` |
| w-phase-fine-v1 | `5ff35381d8d1014e1169eaff3ef26772acd9dcf6239a1b98cb8ac8fa0dbfa73d` |

All exact identity booleans passed. The critical payload is byte-identical
to this reviewer's independently rerun full 2048/16 certificate, including
both strict F0 signs and the negative uniform numerator bound.

The coarse numerical receipt contains exactly the requested 20 cases and
the fine receipt exactly 14, with no duplicate or missing phase/index pair.
Their reported phase coordinates agree with N+theta to displayed precision,
and sign labels agree with serialized F and 1+P values. In the coarse run,
F(0.8) is negative at N=8,16 and positive at N=32,64; F(0.9) is negative
at all four indices. Every fine-run F value is negative. All 34 reported
1+P values are negative. The payloads retain the explicit
`FINITE NUMERICAL FALSIFICATION ONLY` classification and uncertified-tail
warning. No full phase sweep was rerun during this bounded source review.

Final integration verdict: the internal mathematical-draft acceptance
stands, and the four computational receipts have independently verified
provenance and appropriately limited evidence scope.

## Acceptance-record scope check

Reviewed `W_ACCEPTANCE.md` and `claims/CLAIM-0007.md` after integration.
Their theorem and evidence descriptions match the accepted argument: W is
the BB2014 two-sided weakly prudent bridge germ; the exact certificate
establishes limiting signs, and the analytic proof establishes eventual
genuine poles. Both documents preserve the finite failures and distinguish
internal acceptance from external peer review and unresolved priority.
Neither asserts a connective constant for unrestricted SAWs, an effective
first index, simple zeros, or automatic inheritance from J. No scope blocker
was found. The regression-test receipt mentioned by root is root-owned;
this review independently verified the four scientific receipts above.
