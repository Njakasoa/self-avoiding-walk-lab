# Independent review of the M10 structural wrapper

The wrapper correctly combines the three independently reviewed scalar,
weight/product and directed payloads. Its conclusion remains explicitly
componentwise: the full denominator phase sign and complete index coverage
are open. It does not combine component signs into an unproved F_N sign.

An independent call to experiments.m10_structural_batch.payload() reproduced
each earlier per-component output exactly, using sorted indented JSON with
final newline:

| Component | SHA-256 |
|---|---|
| real_beta_derivatives | 7a04339811087b634dbab95557810a3e6c933571d5af60163b8a60d0e7a32734 |
| weight_and_product | 49db78a15baa982f91cf2ada380c302fd404a743ba445788932ef89bf62c1093 |
| directed_monotonicity | f0210db9efbf79dbf5bc4ce6d871520c1b93238fad0ec7cda69993e225294c88 |

Combined payload SHA-256:
57f731f971f887b4853464ce604cbcf2da24bc0f5217162980d30d15fb43ef81.
The imported beta engine rejects -O at import; payload also has an explicit
optimization guard. Each component raises on failed checks, so top-level
status pass is reached only after all three complete.

The source list includes the three producers, their scientific notes,
the M7 interval engine, phase-domain certificate, M5 directed root and
derivative notes, M6 analytic inputs, provenance implementation and locked
dependencies. The initially reviewed 19-source wrapper omitted the frozen
M6 coefficient receipt used for c_D>3/4 in the original combined-weight
component. I requested that receipt and its metadata be added before
freezing. The newer basepoint argument does not depend on c_D, but the
wrapper still retains the earlier structural arithmetic component.

Initial wrapper SHA-256 before that dependency correction:
e9b744090e50bc68a80fce7aac06b803867eb3083a40161120b56113f97d1707.
Final source-list correction and approval are recorded below. No scientific
producer or wrapper was edited by this reviewer.

Final correction verified: the wrapper now lists 22 sources, including
results/m6-coefficient-v1/payload.json, its metadata and check_m3.py,
and calls receipt('m6-coefficient-v1') before the three producers.
An independent final wrapper replay passed and reproduced the same combined
payload hash above. This resolves the dependency finding.

Final wrapper SHA-256:
f8396447ace42f2674b35f2844fb0bd789bc557152ac8dda8fae3fc4da3bb7b8.
Verdict: PASS for source freezing and canonical structural execution,
with the stated component-only scope and unresolved full-denominator sign.
