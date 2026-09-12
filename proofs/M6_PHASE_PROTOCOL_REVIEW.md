# Independent M6 prediction and preregistration review

Status: **prediction formulas, calibration provenance and held-out protocol
accepted as numerical diagnostics**. The finite N=1024 observation and
its receipt have not been audited here; no validation producer was run
by this reviewer.

The prediction implementation correctly evaluates the two reviewed
formulas: theta_star-C1/log(N)+C2/log(N)^2, and the solution of
B(theta)=-(C0+2 delta_hat p0)/(J+2 delta_hat post1), with
delta_hat=sigma/(log(N)+b). The derivative B' and simplified expression
for C2 have the correct signs. Both are computed from critical-integral
midpoints and the explicit digamma constant, without fitting coefficients
to observed finite phases. These midpoint evaluations are numerical
estimates, not interval enclosures; 68-digit arithmetic does not make
the midpoint uncertainty disappear.

The tolerance is explicitly empirical: twice the absolute resummed error
at the already observed N=512. Its common value is approximately
9.3391722709e-6 for both models. This is a legitimate frozen benchmark,
not a statistical confidence interval or a theorem error bound. Because
it is selected from the resummed model, it should not be described as a
model-neutral performance criterion. The truncated second-order model's
failure is retained, as required; it need not meet this tolerance at
these modest N for the asymptotic theorem to hold.

The calibration receipt records commit
7ed5055533f0faf10cc81e1b60d5dd5406973f41. I checked every input hash against
both the current bytes and that commit, and confirmed that commit is an
ancestor of preregistration commit
411b55e4457b9a55b222506b5b303507ce61cc95. The current protocol, scripts and
calibration payload match their bytes in the preregistration commit.
Thus the recorded dirty workspace flag does not conceal changes to the
recorded scientific inputs. Actual-run chronology remains to be checked
against the eventual validation receipt.

Independent lightweight replay of produce_calibration() equals the entire
canonical payload JSON object. The canonical protocol verifier passes.
I independently repeated all four temporary mutations described in
M6_PHASE_PROTOCOL_CHECKS.md: prediction, tolerance, calibration hash and
an observed N=1024 entry. Each is rejected before calling a validation
producer, and temporary files were removed. The implementation directly
calls locate_root(1024) only in validation, with frozen numerical settings;
it preserves separate comparisons and does not refit either model.

| Reviewed file | SHA-256 |
| --- | --- |
| experiments/m6_phase_predictions.py | `6b7cc87fa0496b468a3036a392d0a292197e2b3bd88e873b5ce0f58844ea9900` |
| experiments/m6_phase_batch.py | `d6abcf6e45eb4e0d997f69283b11a0b10372fed5b521c46dda0e94e9ce080f48` |
| experiments/m6_phase_protocol.json | `dc1edbc44e449de32a9ee19e5a92d77d8b8c043264518358ad1ed017bcb2dae2` |
| results/m6-phase-predictions-v1/payload.json | `8dedba3e3506b4072d53b1eff6b42df898ead24cde114c1b98839cc3a1d6f84d` |
| proofs/M6_PHASE_PROTOCOL_CHECKS.md | `1f1a7307ef49d966e37d213136947b293b4c45029b681abf1552f71611217579` |

Expected N=1024 predictions remain frozen at approximately .831624946453
(truncated) and .826653904971 (resummed). No finite N=1024 value is used
in this review or required for its conclusion. The forthcoming audit must
retain both outcomes, numerical uncertainties and the receipt's overall
failure if either common-tolerance comparison fails.
