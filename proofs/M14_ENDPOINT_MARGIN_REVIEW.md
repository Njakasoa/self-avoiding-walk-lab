# Independent review of M14 conditional endpoint margins

Status: PASS for the directed bound, critical affine margins, and conditional transfer. The moment-error hypothesis and uniform endpoint existence are NOT PROVED.

The reference t=414213556/10^9 lies below sqrt(2)-1 and has certified0<e<.01 and a<512.8. Thus the accepted real phase inverse order puts every target N>=512, theta in[.8,.9] above this reference in t. The producer checks0<q<1, beta_dir>0 and beta_dir+gamma_dir>0. Each exact denominator beta_dir+gamma_dir q^(2k) is a convex combination of those positive endpoints, including for every omitted index. All omitted summands are therefore positive. The outward enclosure of the first16384 terms gives a valid LOWER bound on the complete convergent D_R, without an upper remainder. Directed monotonicity transfers D_R>19 and delta_D<1/20 to all declared targets.

The critical profile reconstruction agrees with the accepted M5 formulas: its constant and slope give F0, and sigma-A*pre1+post1*phase_factor gives1+P0. Recovery preserves the original384-bit dyadic endpoints. The inherited Machin pi enclosure and sine Taylor remainder enclose both endpoint factors, with reciprocal denominators bounded away from zero. Multiplication of the negative numerator interval by the independent interval2delta in[0,.1] encloses every actual directed parameter, without requiring its dependence on theta. The resulting affine interval is above1/4 on the left and below-1/5 on the right.

Direct subtraction from F=(1-t+2delta)P_N-4H_N-3-t+2delta yields exactly the stated error identity, including the positive coefficient(sigma-t)(1+P0). Bounding its absolute value uses|1+P0|<15/2, sigma-t<=e^2/8, and the coefficient of the P error bounded by4. The joint error hypothesis<1/25 then gives transfer error<17/100, preserving strict endpoint margins2/25 and-3/100. The hypothesis is explicitly conditional; no step establishes it.

## Independent replay and provenance

Independently verified the complete frozen `m5-critical-v1` receipt against its source/live/output digests, then ran `.venv/bin/python -m proofs.m14_endpoint_margins`: all12 checks PASS. The standalone producer records the critical input digest but does not itself validate that receipt; this review supplies that validation, and any future canonical wrapper should retain the receipt check.

The reference a is approximately496.231903913, epsilon approximately.0003193266713, and the directed partial lower endpoint approximately19.832248906. These are readable summaries of the exact intervals. The affine left lower bound is682801253/2500000000 and the right upper bound is-2063866341/10000000000. The transfer allowance is1342178147/8388608000. Complete producer stdout SHA256: `8eeabaa1311d78ba2b35012fac073450bcdb20205119843bedfc8f32c77aa736`.

Observed repository HEAD: `9a8f2120cd3c04875d877b33b58f521f8d547a56`. Approved actual source/input bytes:

| Path | SHA256 |
|---|---|
| proofs/M14_ENDPOINT_MARGIN_TRANSFER.md | 34e0d58ab9549f4b7c673e0a122855583cbb7bc4b0e529e062e6fc800faf53e6 |
| proofs/m14_endpoint_margins.py | 9de64a2f755e4665e99c76cc9aa97c6155c217a401b407e95710a25f64d4d70f |
| results/m5-critical-v1/payload.json | f94823cf257ffd1c9cf6becea60c07cad100232b787e4253ba7d18681557fd8b |

No material analytic finding remains. Acceptance covers delta_D<1/20 for integer N>=512 and the stated sufficient endpoint-error target only. The joint moment approximation and the remaining finite32..511 coverage are unresolved; existing individual finite certificates are not a certificate for that entire range.
