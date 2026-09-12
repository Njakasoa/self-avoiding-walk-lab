# M5 held-out numerical protocol review

Status: **PASS for the recorded exploratory protocol and its two numerical
comparisons**. This is not interval validation of a finite W pole or proof
of an asymptotic law. No numerical root run was repeated during this review.

## Chronology and source integrity

The calibration receipt records source commit
`8232d82e372860319b5562fef33a5982293ddbca`, committed at
2026-09-12 12:17:52 UTC; its producer started at12:17:57.183556 UTC.
Its calibration indices are exactly32,64,128,256, with512 absent.
The protocol commit `24b383916083ad18ca9b57594571bdbd37a1f588`
is a direct child, committed at12:21:08 UTC. It contains the calibration
payload and the fixed protocol. The held-out receipt uses that commit and
starts at12:21:08.952358 UTC. The recorded chronology therefore supports
calibration followed by committed preregistration followed by validation.
Git and receipts establish this recorded sequence, not the absence of
arbitrary unrecorded executions elsewhere.

Every recorded input hash in both receipts was independently compared with
the named commit's bytes and current workspace bytes. All matched. Both
payload hashes were independently verified:

| Item | SHA-256 |
| --- | --- |
| Calibration payload | `23c4c0ac3fecb8ac8eed5dadaa921b77f27615cb293324023a82390c7ef15946` |
| Preregistered protocol | `11a2b0e291cf4d1ccd0073fcb180e6b15e9279854b37f5c082dc3cb35949d023` |
| Held-out payload | `bb72073186c9d53520f1ed97292e2f140db744b1afebc0d6e3f059940357a5fa` |
| Batch driver | `9b5c06d4adeb7f938795995b866a0d9433a0b5821a78fadcad2b247d52a35fa8` |
| Numerical producer | `d4ab6762b731f7e92db85286a777279215b600d0d51a2715a3ed7b4919992d29` |

## Protocol and arithmetic

The wrapper verifies the calibration hash, run parameters, indices,
reference midpoint, predictions and held-out index. The validation path
calls the root locator directly at512; it never calls the fitting function.
The two predictions come unchanged from the calibration payload. The
reference theta midpoint is deliberately frozen from that calibration
reference, not replaced afterward by a sharper limiting-root certificate.

Each tolerance is exactly five times the corresponding recorded maximum
absolute calibration residual. This equality was checked independently
with high-precision Decimal arithmetic. The multiplier is a fixed heuristic
tolerance policy, not a statistical confidence interval or rigorous error
bound. The wrapper checks positivity of tolerances but does not enforce
the five-times rule itself; the committed protocol and this audit verify
that rule for these actual receipts.

The held-out theta is0.82316287432966148645722838345844077.
The distance observable's absolute prediction error is approximately
3.2900989148768e-7, below tolerance1.1797893296170e-6.
The logarithmic phase observable's error is approximately .00272463664035,
below tolerance .00509436118049. These use respectively .279 and .535
of their fixed tolerances. Recorded errors and pass labels agree with
independent subtraction and comparison of the serialized numbers.

## Preserved failures and limits

The earlier log-offset fit intercept .362289565863457 lies below the
certified asymptotic shift interval [.38696091,.44166261]. That mismatch
is retained in the calibration payload and explicitly noted in the
protocol; neither held-out success nor later limiting certificates repair
it retroactively. The validation code retains tolerance failures as false
comparison flags and a failed status rather than discarding them.

The finite root finder, tail computations and centered derivatives remain
floating-point diagnostics. Two passed held-out observables establish
neither interval-certified root existence nor uniform large-N error
bounds, root uniqueness, residues, or an effective W N0. The files and
receipts keep that scope distinction explicit. No refit on the held-out
observation was found in the reviewed validation path.
