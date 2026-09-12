# W public packet review

Date: 2026-09-12. Internal AI review; no external review or endorsement.

## Source and scope checks

Reviewed `publication/GITHUB_README.md`, `publication/REVIEW_J_W.md`,
`publication/reproduce_w.py`, and the revised final paragraph of
`W_ACCEPTANCE.md`. No scope blocker found. They identify the J manuscript
and separate W supplement accurately, retain the cited-input conditions,
and distinguish internal mathematical acceptance from priority and external
review. The reading guide poses the actual analytic obligations and does
not claim that finite computations prove convergence or finite W poles.
The historical publication-status adjustment does not alter the proof.

The portable W script imports the retained scientific modules directly;
it calls neither git nor the receipt producer and does not read a third-party
PDF. It verifies the executed scientific module hashes against the retained
receipts, checks expected payload hashes, then compares recomputed Python
payloads exactly. This is an arithmetic replay, not an independent proof
of authenticity against coordinated changes to sources and receipts; the
separate public manifest supplies exported-byte integrity checking.

Independent local execution of `publication/reproduce_w.py` passed both
identity and full exact critical-certificate replay. Execution with `-O`
failed immediately as intended. The five scientific modules in its hash
groups are all local modules it imports, and those modules have no additional
local imports outside the listed groups.

Reviewed SHA-256 values:

| File | SHA-256 |
| --- | --- |
| publication/GITHUB_README.md | `b03f743a4f9d885066d54ab8f97d0e402157934977c8e5614cf234e9d2fbc799` |
| publication/reproduce_w.py | `999a8edc3a7cf5d95bf2e4c5e37760b546777552259ed02992d1ebf0d51f03f1` |
| publication/REVIEW_J_W.md | `d62fdd3ce63400436c7e50c4e87a89656e47a0ce26557b8b8a92f167bbe746b3` |
| W_ACCEPTANCE.md | `00d7bb8fe4461d4402aaf340468b770ff1d74dcaacc61836279e941f981ca652` |

## Export verification

**PASS.** Independently verified the export at
`publication/dist/github-w-20260912`, from source revision
`980b4bf66b0f4b6043d8030637c283eb6a6fc38e`.
All 234 manifest hashes match exported bytes. Retained source files match that
source commit, mapping the public README to `publication/GITHUB_README.md`.
The two additional export transformations are the documented public-ignore
suffix in `.gitignore` and the generated `papers/README.md` directing readers
to original sources; both match `scripts/export_github.py`.
All 22 named excluded source files are absent. Local links from the public
README, review guide and W acceptance resolve within the export.

The exported W proof retains its accepted hash
`351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a`.
The guide, portable checker, acceptance record, claim, citation metadata and
roadmap also match the reviewed source bytes. Citation metadata and the
updated roadmap preserve unresolved priority and describe review preparation
without claiming contact or external endorsement.

No publication-packet blocker found. Root owns clean-export execution,
tamper tests, final Git integration and authorized remote push. This report
records source/export review and does not claim that remote publication has
already occurred. Its final update remains local to avoid changing a frozen
export merely to update the report of that same export.
