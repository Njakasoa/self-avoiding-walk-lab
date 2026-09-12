# Independent M4 reproduction receipt

Reviewed 2026-09-12.  This receipt covers the standalone `publication/`
directory after the source manifest was released.  The PDF stage was omitted
as permitted by the task; the replay regenerated the figures.

## Source-copy audit

`publication/proof-checkers/PROVENANCE.json` identifies source commit `dbf8e65`.
The five repository-to-publication copies match as follows:

| repository source | bundled checker | source SHA-256 | bundled SHA-256 | adaptation |
|---|---|---|---|---|
| `proofs/m3_prudent_intervals.py` | `proof-checkers/intervals.py` | `a2230bdeedbefcd5550cc64f304dcdd4b887a5c60f77e4f7cac974ad71451ff1` | same | byte-identical |
| `proofs/m3_critical_integrals.py` | `proof-checkers/critical_integrals.py` | `da519b98367b64d29b18f50f13ecf42a2dae54550c6b3771fabbd92f8964cf16` | `9e5c593b76a41435315be6d0f1e163fcd082a2c88b4cff0f0aaad67a23f0f2c5` | local import only |
| `experiments/m3_moment_identities.py` | `proof-checkers/moment_identities.py` | `da79d60772e70d2db3301ac305909e7b1df290bbf4e4ff086687dc52d9c3d98c` | same | byte-identical |
| `experiments/m3_coboundary_probe.py` | `proof-checkers/independent_identities.py` | `4b6ea78b9016139de7da00ebaa50f1e3eb354111f5c78668d2e7ddc228313dd1` | same | byte-identical |
| `proofs/m3_prudent_reference.py` | `proof-checkers/reference_counts.py` | `2fbd8c664395d45a0e53cda74b840d2d2abda26e7ce4b57bda6d479fb03bd500` | same | byte-identical |

The only source adaptation is the critical-integrals import from the
repository package path to the bundled local `intervals` module.  The official
manifest contains 20 static inputs and has SHA-256
`e4ed9774c991ad3c5e81ed1f79d0ce23165f6b174c5f6911f8751bd3c5f50bde`.

## Isolated positive replay

I copied `publication/` to `/tmp/m4-independent-reproduction-PFipKD`, removed
any `build/` and `__pycache__/` directories, and ran:

```text
/home/njakasoa/.openclaw/workspace/projects/github/self-avoiding-walk-lab/.venv/bin/python \
  /tmp/m4-independent-reproduction-PFipKD/reproduce.py
```

The command exited 0 and wrote `VALIDATION.json`.  The replay JSON hash and
the generated validation hash are both
`f1b94796e962c2a041c3ad239a3f781d53097ac126076f274feecd764c7c720b`.
The result was `status: PASS`, with these checks:

- `integral_certificate_exact_match: true`; the frozen
  `proof-checkers/expected-integrals.json` hash is
  `060d525c2dcbe4051ae29e9d9d5dd90a6bfba862b5274e6703084823970c0c23`.
- All 11 primary symbolic checks are true, including both power identities,
  both coboundaries, both boundary identities, the kernel relation, recurrence,
  and formal critical ODE partial fractions.
- The independent implementation reports `A_equals_A1`,
  `hook_equals_t2_A2`, `moment_identity_mod_q_relation`, and
  `positive_hook_decomposition` as true, and checks telescoping powers
  `[0, 1, 2, 3, 4]`.
- `finite_poles_checked: 5` and `geometric_length: 12`.
- `publication_priority: UNRESOLVED` and `pdf_compiled: false`.

The regenerated figure hashes exactly match the publication inputs:

| output | SHA-256 |
|---|---|
| `figures/critical_phase.pdf` | `57546bb7f9613ef93fe305ad15d4a78a53dd89ca24a379e612b5ea9da7f972ce` |
| `figures/critical_phase.png` | `475210488101d4a4144d62e209b239234ca1a76840f267445456f0388df538e1` |
| `figures/critical_phase.svg` | `7d0f1729fe24af17c322b30d57b99b3b34dbf19385986b861a75b085abd8ae0a` |

The isolated source-manifest hash reported by the replay matches the official
manifest hash above.

## Required negative tests

For the tamper test, I copied the positive replay to
`/tmp/m4-tamper-0TrKpv`, appended a comment to the manifest-covered
`proof-checkers/README.md`, and reran `reproduce.py`.  It exited 1 with:

```text
RuntimeError: Source hash mismatch: proof-checkers/README.md
```

For the optimization test, I copied the positive replay to
`/tmp/m4-opt-wZpHIN` and ran the same entry point with `python -O`.  It exited
1 before any checker ran with:

```text
RuntimeError: Run without -O: the proof checkers require assertions
```

These checks were performed only in isolated temporary copies; the publication
directory was not edited.  The receipt verifies computational reproduction and
source integrity, not formal proof-assistant coverage or publication priority.
