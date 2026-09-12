# M6 phase protocol verification checks

This is an implementation diagnostic for the frozen M6 phase protocol. It
does not call locate_root, evaluate a finite \(N=1024\) row, or alter the
canonical protocol/calibration files.

The deterministic calibration replay
experiments.m6_phase_predictions.produce_calibration() was compared as a
full JSON object with
results/m6-phase-predictions-v1/payload.json; the comparison passed.

Four temporary protocol copies were then created below experiments/ and
deleted by a TemporaryDirectory cleanup. The wrapper's _verify_protocol
rejected each before any validation producer could run:

| mutation | rejection field |
|---|---|
| change predictions.resummed["1024"] | protocol predictions |
| change tolerances.resummed | protocol tolerances |
| replace calibration_payload_sha256 by zeros | calibration payload SHA-256 |
| add observed["1024"] | forbidden observed \(N=1024\) |

The canonical files remained unchanged, and no temporary protocol path
remained after the check. The M6 calibration output retains separate
truncated_2nd and resummed pass/fail values; the protocol verifier checks
both prediction maps and all three common/model tolerance fields for exact
equality with calibration.

## Provenance

The checks used source commit
411b55e4457b9a55b222506b5b303507ce61cc95
(Preregister N1024 phase predictions and common benchmark tolerance).

| file | SHA-256 |
|---|---|
| experiments/m6_phase_batch.py | d6abcf6e45eb4e0d997f69283b11a0b10372fed5b521c46dda0e94e9ce080f48 |
| experiments/m6_phase_predictions.py | 6b7cc87fa0496b468a3036a392d0a292197e2b3bd88e873b5ce0f58844ea9900 |
| experiments/m6_phase_protocol.json | dc1edbc44e449de32a9ee19e5a92d77d8b8c043264518358ad1ed017bcb2dae2 |
| results/m6-phase-predictions-v1/payload.json | 8dedba3e3506b4072d53b1eff6b42df898ead24cde114c1b98839cc3a1d6f84d |
| experiments/m5_phase_diagnostics.py | d4ab6762b731f7e92db85286a777279215b600d0d51a2715a3ed7b4919992d29 |
| src/provenance.py | c82faec776899d6de355731e5194a43971106f40c53cdeb89c0ab5e96ed68b34 |
| proofs/M6_SECOND_ORDER.md | 1d9641b561cf24e346ecc6996fe6f48e833d5694a97788c4d8de07f4d5c546c0 |
| proofs/M6_RESUMMED_PHASE.md | 47d7ff8a5e90b82a593e262cee5ec426a237e037c5e59cab94f02ad65197b301 |
| requirements-lock.txt | 2e57ddd45362cddee6307d6a33b84a5d291743d34ed17611e2ad7c51562c1206 |
