# Final N=32 full-band proof snapshot review

The final proof note adds the frozen engine/input hash ledger to the
previously reviewed argument. I reread it and verified those four listed
hashes. Its phase geometry, e<.01 domain, cell guards and M7 zero transfer
are unchanged and remain approved. Producer and canonical wrapper bytes
are identical to the previously reviewed versions.

A new independent first-cell replay is retained separately in
results/m10-full-band-review-first-cell-final.json. The original review
artifact remains unchanged as historical evidence. The new replay output
is identical to the earlier result; only the input snapshot/provenance
changed. Its exact result hash is
72e73fcce174b5979afecd73bad594402a110539f0466377893667a8a960a246.
This is a bounded replay, not an independent full 128-cell execution.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M10_FULL_BAND.md | 9cf6e1e014a66595765acda379db3752988af18e7e660eb2b9d893f2861fd923 |
| proofs/m10_full_band.py | 8372d4cf50e291edc0700a49a9ad08ddbe4bf9e3a71d6efd77a9e4b10f140079 |
| experiments/m10_full_band_batch.py | e3cd1a4b4a486358fcf61889e026d9f2de9f62463c6e8431c07ae300e7b47041 |

The full W theory goal remains OPEN. Any accepted full-band conclusion is
limited to N=32; the structural component results for N>=32 do not prove
full-band uniqueness at unlisted finite indices.
