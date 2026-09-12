# M5 final closure review

Status: **PASS at the internal research-draft gate**. Internal AI review is
not external peer review, and priority remains unresolved.

Reviewed M5_ACCEPTANCE.md, M5_STATUS.md, CLAIM-0008, the final verification
JSON and the canonical effective receipt. Their statements match the
accepted proofs: uniform directed and moment estimates, limiting critical
coefficients, negative logarithmic phase displacement, eventual unique
simple poles, residues and spatial correction, an explicit existence-only
threshold, and preregistered held-out numerical validation with its failed
calibration extrapolation retained. No goal-scope omission or unsupported
strengthening was found in this closure dossier.

The threshold N0=2^(10^120) consistently guarantees existence and
noncancellation only. The uniqueness, simplicity and residue thresholds
remain non-effective. Neither the fit nor the two held-out comparisons
are treated as proof of the analytic theorem. The unused directed
additive-constant conjecture remains unproved; external review and priority
are future work, not concealed completion requirements. No unrestricted
SAW claim or M5 external publication is asserted.

## Independent final checks

- Reverified all six canonical receipts: m5-critical-v1,
  m5-phase-domain-v1, m5-directed-log-v1, m5-phase-v1,
  m5-phase-holdout-v1 and m5-effective-v1. Every input hash matches both
  its recorded Git commit and current bytes; every output hash matches
  its retained payload.
- Reverified all ten current-source hashes in the integration audit and
  confirmed each appears in the named independent review report.
- Reverified the three legacy J/W proof/manuscript hashes are unchanged.
- The two effective subpayloads equal this reviewer's independently
  generated arithmetic and weight-box JSON objects exactly. Their original
  stdout hashes match those recorded in the root audit.
- Replayed both small effective checkers in normal and optimized Python:
  stdout is identical. These Fraction-based checkers do not rely on
  assertions disabled by `-O`; this differs deliberately from the older
  assertion-dependent dyadic interval entry points, which reject `-O`.

The canonical effective source commit is
`36de16204859c54e8326b6e109dfb4ed14e028e7`; its combined payload SHA-256 is
`c105bdc561220e9bbad1f68c8029d37f066ab4c8de61108ebd103ae2011cf86f`.
Independent component stdout hashes:

| Component | SHA-256 |
| --- | --- |
| Final threshold arithmetic | `14fa94108a43eae95db544f19f4d9b1a2be6ce5fce31751f7f684fb60f1af481` |
| Rational weight boxes | `e50ff0af82b2751b94593d6255df5df62d399a7e13202d07c7ce9d686e2b7d0c` |

The 54-test regression run and compilation receipt are root-owned; this
bounded final review did not repeat that suite or the long numerical runs.
It independently checked the scientific provenance and exact small outputs
instead. No remaining blocker was found for closing M5 at its stated
internal research-draft scope.

Reviewed closure-document SHA-256 values:

| Document | SHA-256 |
| --- | --- |
| M5_ACCEPTANCE.md | `f4db066cad6916ca8facd5a43a3ba64c1266f4722653c0aee0881a9dfe54b724` |
| M5_STATUS.md | `e63c9d5e1b6bc503a366e435846a78bc42bda4f96422b3861d1c11c27ce496b5` |
| claims/CLAIM-0008.md | `91b2a0aa699c1e944a0d96efb24a30595cd187f61619ef2f1a868386c26b6231` |
| results/m5-final-verification.json | `79b7d6fc9fc244cc8d0b39f15c734dd826fca2602d7e103c31a69ade78f76a87` |
