# Independent review of the M13 wrapper and checker

Status: PASS for the released integration mechanism and exploratory replay. Canonical receipt creation and final closure verification remain outstanding; no canonical M13 receipt was created by this review.

The wrapper validates the frozen M7 finite, M10 structural, M11 phase and M12 noncancellation receipts before running all seven M13 producers: boundary, original middle, strengthened middle, pre mass, pre phase, tail, and combination. The pre-phase adapter captures and parses its printed JSON and rejects a non-dictionary or failed status. The other producers fail internally on unsuccessful arithmetic or interval guards. No component is replaced by a literal result or cached exploratory payload.

The52 distinct source paths cover all seven new code/note pairs, the wrapper, imported interval engines, inherited analytic hypotheses, M11 scalar producers, receipt payloads and metadata, receipt verification, provenance and dependency lock. The wrapper delegates to run_record, which compares every declared source with its HEAD bytes before execution, records input/output hashes and source commit, and refuses an existing output directory. The inherited receipt helper compares recorded hashes with both source-commit bytes and current files, and validates output hashes. The explicit optimization guard prevents its assertion checks from being disabled.

The checker validates the M13 receipt, reruns the complete wrapper, and requires exact parsed-payload equality before its component checks. It independently recalculates the low/high integer-index allowances and exact-3141/64000 margin. It checks the component, domain, nonexistence and no-scan markers and requires current source hashes in all seven independent scientific review tables plus the wrapper/checker review. Its helper field checks are used together with complete replay equality, not as a standalone validator for arbitrary partial payloads. The wrapper/checker pair is pinned by this separate review table; the checker itself is not claimed to be part of its producer receipt input list.

All reported conclusions retain integer N>=32, theta in[4/5,9/10], at most one zero per full band, and a simple noncancelled pole whenever a zero exists. The explicit all-index existence marker is NOT PROVED. No new index scan or complete existence coverage is asserted.

## Independent replay

Called payload() without writing a receipt, then ran _check_components and _check_combination: PASS. All seven nested component objects exactly matched separate standalone producer JSON, including the retained interval/tail records. Their stdout hashes match the individual scientific reviews. The complete wrapper JSON, serialized with sorted keys, indentation2 and a final newline, has SHA256 `bd5f7921ef126884c41736323ecb5ba8a8b18e3c1e39f474ab0628994711b25c`.

Independent temporary-directory negative tests confirmed rejection of a missing review, missing source hash entry, and stale source hash. Both checker and wrapper reject execution under -O. Before this review was written, _check_reviews successfully checked all scientific reviews and then rejected the absent wrapper review. Final review-table replay succeeds after this table is installed.

## Released source hashes

| Path | SHA256 |
|---|---|
| experiments/m13_phase_batch.py | 7cf4d6f69d96fe1666d162f7b2fec51cf55190c4f827068d48996f17dd25ed9c |
| proofs/check_m13.py | 9e0c3f02680b9302dbac28141ff5b71fe68e6f8e1d13af95fe74e1c67d672907 |

No material findings remain. This review does not substitute for verifying the subsequently frozen canonical receipt.
