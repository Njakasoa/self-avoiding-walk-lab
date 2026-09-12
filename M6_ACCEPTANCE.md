# M6 — second logarithmic correction and reduced W threshold

Status: **ACCEPTED at the internal research-draft gate; final closure audit
passed in results/m6-final-review.md**. Internal AI review is not external peer
review. Priority remains UNRESOLVED. Work is local on codex/w-second-order;
no M6 publication or external contact occurred.

## Requirement-by-requirement evidence

| M6 requirement | Result | Evidence and scope |
| --- | --- | --- |
| Prove the directed additive constant | D=[log(1/e)+log4-digamma(2+sqrt2)]/sigma+R, with abs(R)<=100e log(1/e), e<=.01 | M6_DIRECTED_CONSTANT and independent directed review; numerical receipt is a diagnostic only |
| Second logarithmic phase term | theta_N=theta*-C1/logN+C2/log²N+O(log^-3N) | Reviewed transfer plus proved directed input; exact C2 enclosure [.844491934033,1.148455190184] |
| Substantial threshold reduction | Every integer N>=10^46 has at least one noncancelled W pole in its band | Sharp-kernel, real moment and threshold proofs/reviews; replaces2^(10^120); existence only |
| Preserve failed predictions | Second-order truncation fails the fixed finite benchmark at512 and1024 | Both failures retained; no refit; asymptotic theorem is not a finite-error claim |
| New reserved validation | N1024 measured after source and protocol freezes | Resummed phase error1.83125e-6 passes tolerance9.33917e-6; truncated error.00496921 fails |
| Reproducibility and independent review | Five canonical receipts, exact replays, reviewed source hashes, unchanged legacy sources | proofs/check_m6.py, results/m6-final-verification.json and accepted results/m6-final-review.md |

The threshold improvement comes from a different estimate: coefficient
positivity makes g concave and gives0<R_e<=1. Absolute damped-product
comparison then avoids the previous exp(B) loss. A new local analytic
box gives B=10^12, yielding the moment bound

    |P_N-P0|+|H_N-H0|
        <=10^9 e^(1/4)+10^9 B sqrt(e)+10^14 e.

Its accepted application uses0<e<=10^-10, the common domain with the
inherited weight lemma; see M6_REAL_RATE_DOMAIN. At e<10^-46 this error
is below.013162277661. The directed correction is below.003910666619.
Exact endpoint signs on[.8,.9] and a uniformly nonzero numerator imply
existence and noncancellation in each band.

This is a structural reduction from a double-exponential index to10^46,
not a computationally useful low-index theorem. The plan's ambition of
a threshold suitable for direct numerical coverage is **not achieved**
and remains further research. The completed reduction requirement is the
substantial analytic improvement itself. Effective uniqueness and
simplicity also remain open; their inherited eventual statements hold.

## Phase formula and spatial consequence

With b=sigma(1+c_D)-log(s*) and p=1+P0, define theta_hat_N by

    F0(theta_hat_N)+2sigma p(theta_hat_N)/(logN+b)=0.

The affine dependence on B(theta) solves this equation explicitly.
The reviewed estimate theta_N-theta_hat_N=O(N^-1/20) means that this
formula determines every fixed logarithmic coefficient. It does not
give an arbitrary-order uniform expansion or a small finite-N error bar.

For K=s*²/16, the pole-position expansion gains the term
-2K C2/(N³log²N), with its coefficient enclosed in
[-.003599521365,-.002646830964]. No second-order residue theorem is
included. All statements concern the same restricted W series as M5,
not unrestricted square-lattice SAWs.

## Held-out numerical result and its limits

Frozen predictions at1024 were .82665390497070380983 (resummed) and
.83162494645304304726 (truncated). The direct diagnostic returned

    theta_1024=.826655736217392822902422627418615954.

The resummed error is .00000183124668901307; the truncated error is
.00496921023565022436. Both are compared to the unchanged tolerance
.00000933917227090409, defined as twice the already observed resummed
error at512. That empirical tolerance is resummed-derived, not a neutral
model-selection criterion or a rigorous enclosure. The payload's aggregate
status remains **fail**, because one comparison fails.

The constants used in these predictions come from midpoints of the frozen
critical integral enclosures, not finite root fitting. The direct sums use
mpmath and are labelled diagnostic, not outward-rounded certificates.
The small numerical residual of F and the directed tail estimate are
recorded without promoting them to a proof of the finite root location.

## Frozen sources and canonical receipts

- 73f1603: second-order transfer/coefficient sources; m6-coefficient-v1.
- c6ed109: directed theorem and diagnostic sources; m6-directed-v1.
- 7ed5055: theoretical prediction scripts; m6-phase-predictions-v1.
- 411b55e: calibration and protocol committed before the reserved
  calculation; m6-phase-holdout-v1 records this exact source commit.
- e7c18da: sharp kernel, domain clarification and threshold arithmetic;
  m6-threshold-v1.

The integration verifier checks all five receipts against their committed
and current input bytes, reproduces the exact coefficient and threshold
outputs, reproduces the calibration, verifies eleven reviewed source
hashes, and independently recomputes held-out comparisons with Decimal.
The original J manuscript and M3/W proof files retain their frozen hashes.
The regression suite passed54tests in10.61s; Python compilation and the
new exact-engine optimization guards are checked separately.

Further research: rigorous finite-N interval evaluations to connect the
large-index theorem to accessible bands, an effective derivative estimate
for uniqueness, and a sharper algebraic remainder for theta_N-theta_hat_N.
