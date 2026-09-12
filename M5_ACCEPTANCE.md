# M5 — quantitative W poles: acceptance dossier

Status: **ACCEPTED at the internal research-draft gate**. The effective
threshold review passed, all six canonical receipts were verified, and their
source hashes match the reviewed files.
Internal AI review is not external peer review. Mathematical priority remains
UNRESOLVED. This work is local on `codex/w-quantitative`; it has not been
added to the public GitHub snapshot.

## Results and evidence

| Requested result | Evidence | Scope |
| --- | --- | --- |
| Directed logarithmic law | `proofs/M5_DIRECTED_LOG.md`, `M5_PHASE_DOMAIN.md`, directed/phase receipts | Uniform error <31/log²N for 1-D_I-sigma/logN when N>=2^108 |
| Moment error and phase derivatives | `proofs/M5_MOMENT_RATE.md`, `M5_MOMENT_RATE_REVIEW.md` | Uniform C0/C1 O(N^-1/20); constants initially non-effective |
| Limiting phase and coefficients | `results/m5-critical-v1` and `M5_DIRECTED_CRITICAL_REVIEW.md` | Exact outward intervals, 4096 rectangles and 384-bit arithmetic |
| Directed phase derivative | `M5_DIRECTED_REFINED.md`, `M5_TRANSFER_REVIEW.md` | Absolute bound30000/N for N>=20 |
| Logarithmic displacement | `M5_W_QUANTITATIVE.md`, transfer review | theta_N=theta*-C_shift/logN+O(log^-2N) |
| Unique simple poles and residues | Same transfer and review | Eventual unique simple pole in each phase band; residue=C_res/N³+O(N^-3/logN) |
| Explicit first W existence index | `M5_EFFECTIVE_THRESHOLD.md`, component lemmas, `M5_EFFECTIVE_THRESHOLD_REVIEW.md`, `m5-effective-v1` | Proven sufficient index2^(10^120); existence/noncancellation only |
| Independent numerical validation | Frozen protocol and `m5-phase-holdout-v1`, `M5_HOLDOUT_REVIEW.md` | N512 excluded from calibration, both predeclared tolerance checks pass |
| Preserve negative evidence | `M5_PHASE_DIAGNOSTICS.md` | Calibration extrapolation of C_shift fails its exact limiting enclosure |

The accepted critical intervals are theta* in [.8695,.8720],
C_shift in [.38696091,.44166261], and C_res in
[-.00167097,-.00146400]. They enclose constants of the limit function;
the analytic transfer, not finite data fitting, supplies the pole theorem.

The accepted explicit threshold establishes existence and
noncancellation. It is not advertised as an effective uniqueness threshold
or as the smallest possible N0. The uniqueness and simplicity result has
its separately proved eventual scope.

## Canonical provenance

- `106db6d44466ef82d57ecbc44e83a8c224b655f7`: sources of critical,
  phase-domain and directed-log receipts.
- `8232d82e372860319b5562fef33a5982293ddbca`: repaired calibration sources.
- `24b3839`: protocol and calibration committed before N512 validation.
- `36de162`: effective-threshold source freeze, recorded by `m5-effective-v1`.
- `results/m5-final-verification.json`: root integration audit, including
  exact equality to the reviewer's independent arithmetic outputs.
- `results/m5-final-review.md`: independent closure audit passed, including
  six receipts, ten reviewed-source hashes and the exact output comparisons.

All run receipts record source hashes, source revision, output hash, runtime,
CPU and RAM. Exploratory mpmath evaluations remain labelled diagnostic.
The final arithmetic checker relies on separately reviewed analytic bounds;
it does not by itself turn a candidate estimate into a theorem.

## Validation and remaining research

The regression suite passed54tests (10.20s). All newly added Python modules
compiled. The six canonical numerical/certificate receipts were verified
against their frozen source and current bytes. The independent reports
record exactly which statements and file hashes they accept.

Further work after M5 is to reduce the conservative existence threshold,
make a uniqueness threshold effective, prove or refute the unused digamma
constant conjecture in the directed refinement, and sharpen the moment
error enough to control a second logarithmic correction. External review
of both the older J/W proofs and the new M5 estimates remains desirable.
Neither novelty nor a solution for unrestricted square-lattice SAWs is
claimed by this restricted prudent-bridge result.
