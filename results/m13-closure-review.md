# Independent M13 canonical closure review

Status: PASS for the scoped M13 derivative certificate. The full W existence goal remains OPEN.

Independently ran `.venv/bin/python -m proofs.check_m13`. The checker passed all receipt, complete component replay, exact combination, scope and independent review-table checks. Its stdout is byte-identical to `results/m13-verification.json`, SHA256 `bc4d5dd65aaa13c842f1aeaa4ac5c63aa72a91e07110ce8dfc621170ac7806fe`.

## Frozen receipt and preservation

| Item | Value |
|---|---|
| Canonical receipt | results/m13-phase-v1 |
| Source freeze | f68a84c2ae9eb927b262c139583fc50f473ba195 |
| Declared inputs | 52 |
| Payload SHA256 | bd5f7921ef126884c41736323ecb5ba8a8b18e3c1e39f474ab0628994711b25c |
| Metadata SHA256 | 0d6add144d60178d35791ca62789c2ff80d77764606442f999f034ae8b6f1a80 |
| Recorded producer runtime | 1.6804652959981468 seconds |
| Wrapper SHA256 | 7cf4d6f69d96fe1666d162f7b2fec51cf55190c4f827068d48996f17dd25ed9c |
| Checker SHA256 | 9e0c3f02680b9302dbac28141ff5b71fe68e6f8e1d13af95fe74e1c67d672907 |

Separately compared all52 recorded input digests with both their live bytes and `git show` bytes at the source freeze: exact match. The canonical payload matches the independently reviewed exploratory wrapper payload hash, and the complete replay matches its parsed content. The metadata's dirty-worktree flag does not indicate an unfrozen declared input: every declared input was verified against the freeze.

All eight scientific/integration review tables pass against current source hashes. These include all seven M13 scientific note/producer pairs and the wrapper/checker pair. The prior review documents contain the independent analytic arguments; arithmetic replay alone is not being treated as proof of their hypotheses.

Also independently verified all29 existing canonical M3--M12 receipts using their source-commit, live-input and output digests: all pass. This includes M7 finite, M8 finite/analytic, M9 linear, M10 full-band/structural, M11 phase and M12 noncancellation, together with all earlier recorded M3--M6 receipts. No prior canonical source or output alteration was detected. No scientific source or canonical payload was changed during this closure review.

## Accepted scope

For every integer N>=32 and theta in[4/5,9/10], the accepted result is

    F_N,theta < -3141/64000 < -1/25.

Thus each complete band has at most one zero; any zero is simple and gives a noncancelled simple W pole by the local analytic phase transfer and M12 numerator inequality. The preliminary middle allowance shown in the checker's compact component summary is-3/56; the canonical strengthened-middle component and the independently recalculated combination correctly use-9/50.

The six accepted finite zeros at N=32,64,128,256,512,1024 consequently have full-band uniqueness, and M9 separately supplies existence for every N>=10^27. No endpoint-sign or existence theorem for the remaining indices32<=N<10^27 follows from this derivative certificate. The receipt and checker explicitly retain NOT PROVED for all-index existence and OPEN for full coverage.

No material integration findings remain for this scoped checkpoint.
