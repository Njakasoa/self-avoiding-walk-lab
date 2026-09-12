# Independent review of the N=32 full-band producer

Verdict: the certificate mechanism is valid. Independent execution covered
cell 0 only and passed, with the explicit partial classification. Acceptance
of the full N=32 band requires the source-frozen canonical 128-cell run and
receipt verification. No independent full scan was performed in this review.
Neither this mechanism nor that eventual finite result covers unlisted N.

## Outer phase coverage

The two phase targets are 164/5 and 329/10. Each endpoint is chosen by
exact rational bisection with outward I384 phase boxes: the selected left
endpoint has its whole phase interval below the lower target; the right
endpoint has its whole interval above the upper target. Thus no rounded
point estimate is substituted for a phase-inverse enclosure.

Every derivative cell explicitly requires 0<epsilon and
100*epsilon.hi<SCALE, proving the M5 real inverse domain e<.01 there.
The inherited real derivative signs a_e<0 and t_e<0 make a(t) strictly
increasing on the physical branch. Consequently the connected outer
interval contains the full target phase band with a single inverse branch.
This argument uses the cell domain guards, not an unproved extrapolation
of the phase inverse beyond its accepted interval.

The rational partition t_k=t_L+k(t_R-t_L)/128 has no gaps. Full mode
checks every index, its first/last endpoints and exact neighboring endpoint
equality. Cells are evaluated on outward rounded intervals containing their
closed rational cells, so rounding cannot leave a gap between cells.
The final cell necessarily certifies the right boundary as well.

## Source poles, derivative tails and transferred zero

Each complete cell has a and b strictly in (32,33), excluding real integer
source zeros. The inherited physical kernel, discriminant, denominator,
recurrence sign and contraction guards are exercised by the M8 engine.
The new wrapper also rechecks all prudent and directed value/derivative
tails as nonnegative and at most 10^-18, using exact fractions rather than
rounded tolerances. The strict upper endpoint of F_t is checked on each
whole cell. The analytic differentiated-tail review from M8 therefore
applies to these domains; it was not intrinsically restricted to the narrow
seed widths, provided its guards and tail closures succeed.

The M7 payload is pinned by SHA-256 before use. The N32 row supplies
opposite endpoint signs, a source-free narrow bracket, and a whole-bracket
negative 1+P. Its frozen a interval lies strictly inside (32.8,32.9), so
the supplied zero belongs to the requested phase band. Checking containment
of that bracket in the new outer interval then transfers this same zero.
Strict F_t negativity across all adjacent cells makes F strictly decreasing
on the connected outer interval, hence the zero is unique there. The M7
local holomorphy argument and nonzero derivative give simplicity, and its
negative numerator at the zero excludes cancellation in W. No assertion
that the numerator stays negative across every outer cell is necessary.

## Serialization and partial scope

The recursive serializer handles I384, Jet384, rational values, nested
mappings and sequences. The retained engine record contains both the
prudent and directed derivative-tail data; the Jet384 contraction factor
is serialized as a full value/derivative record. This avoids the earlier
M8 serialization defect.

Full coverage is claimed only when cell_subset is None and all 128 checks
complete. Every explicit subset remains classified PARTIAL, even if it
lists all cell indices. The independently replayed cell-0 result has
full_coverage=false, partial_mode=true, cells_requested=[0], and no
full-band conclusion. The optimized interpreter was independently tested
and correctly rejects execution before interval work.

The canonical wrapper validates the inherited M7 receipt and records the
producer, proof note, M7/M8 engines and phase-domain dependencies. It runs
full mode, which is appropriate for its one-band conclusion. Canonical
source/output hash checks remain the integrating root's release step.
The earlier diagnostic scan is not substituted for that canonical run.

## Independent replay and provenance

The bounded replay used produce_first_cell() in the project Python
interpreter and finished in 6.262630133001949 seconds. The exact output and
input/source hashes are retained in
results/m10-full-band-review-first-cell.json. The JSON result's SHA-256
(using the producer's sorted, indented formatting with final newline) is
72e73fcce174b5979afecd73bad594402a110539f0466377893667a8a960a246,
identical to the implementation worker's separately retained first-cell
output. This agreement is a reproducibility check, not a second full scan.

| Reviewed source | SHA-256 |
|---|---|
| proofs/m10_full_band.py | 8372d4cf50e291edc0700a49a9ad08ddbe4bf9e3a71d6efd77a9e4b10f140079 |
| proofs/M10_FULL_BAND.md | d6b65eae53eba85fda47a30eaefda5a0cde31c98d3a515f0c70b9e859ce7e0b5 |
| experiments/m10_full_band_batch.py | e3cd1a4b4a486358fcf61889e026d9f2de9f62463c6e8431c07ae300e7b47041 |

The replay snapshot also records all inherited inputs and the observed
source commit. No scientific producer was edited by this reviewer. The
full W theory goal remains OPEN regardless of this one-index improvement.
