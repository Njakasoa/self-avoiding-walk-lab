# Independent review of the M9 quantitative phase and residue transfer

Verdict: the phase, position and normalized residue estimates in
M9_PHASE_RESIDUE_RATE.md follow on N>=10^27 from the independently reviewed
M9 uniqueness, linear moment and complex domain results. No mathematical
blocker was found. The bounds are restricted to the stated W phase bands;
they do not cover the intervening finite indices or establish novelty.

## Directed approximation and inverse stability

The M8 directed reciprocal proof uses the real phase equation, the
M6 directed remainder, and D>log(N)/sigma. All hold at the new threshold,
as established in M9_UNIQUENESS_THRESHOLD. Its estimate
|delta-d_hat|<19/(N log N) therefore transfers without importing the
old M8 threshold. The approximate denominator has derivative below
-6+150/125=-24/5 and opposite endpoint signs. Its unique zero lies
in the same band. The inverse mean-value constant is consequently 5/24.
The stated bound on |F-F_hat| then yields exactly R_theta.

The real phase/kernel derivative bound 0<t_N'<1/(7N^3) holds on the
new domain and transfers phase displacement to the full analytic t map.
It proves the position rate O(N^-4); a finite truncation of that map
would require its own remainder. At N=10^27, using log N>54, the phase
bound is less than 8.34*10^-7 and the position allowance less than
1.2*10^-7/N^3. Each component decreases with N.

## Normalized residue

The unchanged kernel expansion gives |J_N-j0|<1/N for J_N=N^3*t_N'.
The margin 1.8*.0037+16*10^6/N<1 holds already at the new threshold.
Since .15<s*<.17, j0 lies above .0028125 and below .0037;
thus .0028<J_N<.004 follows with strict slack.

The same-phase derivative error is the exact differentiated denominator
identity, with costs 4E1, 10/N^2, 2850/(N log N), and 480000/N.
The approximate derivative is an affine multiple of the same critical
B' function, so the inherited |B''/B'|<45 gives
|F_hat''|<(26+150/125)*45=1224<1300. Moving to the approximate phase
therefore adds exactly the displayed 1300*R_theta allowance.

Changing the numerator, then J_N, then the denominator in the exact
residue quotient yields the coefficients .004, 7.5, and
7.5*.0037/(24/5)=.00578125<.006. The independent fixed-degree uniqueness
proof supplies |F_N'|>3.9>1 regardless of the degree chosen in E1(N,m).
Thus the explicit residue error bound is valid for every integer m>=1,
even when that particular interpolation bound would not prove uniqueness.

For the asymptotic rate, the choice m=ceil(4 log N) is essential to the
stated conclusion. Since log(22/15)>1/4, q^m<=N^(-4 log(22/15))=O(N^-1).
Both tails are O(m^2 q^m), and the real interpolation term is O(m^2/N).
It follows that E1 and the normalized residue error are O(log^2(N)/N).
This argument does not reuse the older ceil(log N) choice, whose slower
tail would not support this rate. Algebraic decay dominates every fixed
inverse-logarithmic order, so the inherited exact resummed rational
expression still determines every fixed coefficient. No uniformity in
a growing logarithmic truncation order is asserted.

Finally the fixed-degree derivative difference is below 2.005, so
|F_N'|<26+2.005<29. The numerator and Jacobian margins give a lower
normalized residue magnitude greater than 3.5*.0028/29>1/6000,
while the upper bound is below 8*.004<1/20 using |F_N'|>1.
The signs of numerator and derivative are both negative, so the
residue is negative. The final signed interval is therefore valid.

## Provenance

This review read M9_PHASE_RESIDUE_RATE.md, M8_EFFECTIVE_PHASE.md,
M8_RESUMMED_RESIDUE.md, and the M9 threshold/moment/kernel results already
reviewed in M9_THRESHOLD_REVIEW.md, M9_MOMENT_REVIEW.md and
M9_KERNEL_REVIEW.md. Source hashes and arithmetic-script audit are
recorded below when the final integration inputs are available.

| Source | SHA-256 |
|---|---|
| proofs/M9_PHASE_RESIDUE_RATE.md | 7ff526d4b96128d9afddcae9b0bbc898f9f767a9c9813584b7419010a68ee611 |
| proofs/M8_EFFECTIVE_PHASE.md | 359c116ffa597319463fa0c439d55793d35c7e7f00a5727580bbbf3004ce3e04 |
| proofs/M8_RESUMMED_RESIDUE.md | 6337a164bebed858331895da68b89bf0d259f5dffae669db189d99e28a7db15b |

## Arithmetic producer and wrapper audit

The Fraction producer is an arithmetic ledger, not an analytic verifier.
I compared its check formulas to the proof notes individually, including
variation, the complex kernel and ellipse constants, primitive summation,
final moment coefficient, degree-97 Chebyshev expression, directed and
endpoint allowances, derivative slope, phase error, curvature and quotient
constants. Those formulas agree with the proof. The script uses explicit
conditional raises and has no assertion-dependent success path.

Root caught erroneous coarse-residue arithmetic in a pre-final draft:
the draft divided by the Jacobian instead of multiplying, and used
inappropriate comparison bounds. The required checks are
3.5*.0028/29>1/6000 and 8*.004/3.9<1/20. A pre-correction PASS must not be
used as evidence for the residue bounds. Final corrected hashes and replay
results follow below.

The wrapper calls this producer through run_record, lists the M9 proofs
and their relevant M5--M8 scientific sources and receipts, and records the
moment coefficient and uniqueness threshold with explicit finite-coverage
limitations. Its source list now includes M9_PHASE_RESIDUE_RATE.md and
its M8 quantitative dependencies. Canonical receipt provenance is root's
integration responsibility; reviewing this wrapper does not replace that
source/output hash verification.

Final corrected arithmetic replay: all 82 exact checks passed independently
under both normal Python and Python -O, with byte-identical JSON output.
The coarse residue formulas now multiply by J with the correct lower/upper
values and comparison directions. I also checked the newly explicit
Jacobian .0028/.004 margins and |F_N'|<29 check against the proof.
The hypothesis text now distinguishes frozen critical endpoint margins
from the new M9 endpoint transfer. These changes resolve the draft findings.

- Final producer SHA-256 (proofs/m9_linear_bounds.py):
  4cb493028aeae8c51a32f60693848889296a70c6547feaa44adbc97cf54f1538.
- Final wrapper SHA-256 (experiments/m9_linear_batch.py):
  12dd8c5a2ae8c715184bf68cac5b939eb7e4efca52b56a0822cda08407a5ef18.
- Independent normal and -O JSON output SHA-256:
  c3bc0f813ab3dc75fe5a2c1ff48141e188560e082f04212c40e3c8bdf9d9f9cd.

Commands: `.venv/bin/python -m proofs.m9_linear_bounds` and
`.venv/bin/python -O -m proofs.m9_linear_bounds`.
The final arithmetic and wrapper are approved for source freezing and a
canonical run; mathematical acceptance rests on the associated analytic
reviews rather than the arithmetic PASS alone.
