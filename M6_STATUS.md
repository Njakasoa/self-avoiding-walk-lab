# M6 — second logarithmic correction and effective W threshold

Status: COMPLETE at the internal research-draft gate; final independent audit passed.
Work is local on codex/w-second-order. M5 and the public snapshot are unchanged.

The directed additive constant has been proved and independently reviewed:

    D(t(e)) = [log(1/e)+log4-digamma(2+sqrt2)]/sigma
                + O(e log(1/e)),

with explicit remainder at most100e log(1/e) for0<e<=.01. This discharges
the input of the accepted second-order transfer. With L=logN,

    theta_N=theta*-C1/L+C2/L²+O(L^-3),
    C2 in [.844491934033,1.148455190184].

The coefficient enclosure is exact and outward rounded. Its width includes
the inherited uncertainty of the frozen M5 critical integrals. It is not
inferred from a finite fit. The asymptotic theta_N denotes M5's eventual
unique simple pole; no new effective uniqueness index is claimed.

The affine critical denominator also supplies a phase approximation
theta_hat_N containing every inverse-logarithmic order, with
theta_N-theta_hat_N=O(N^-1/20). Its finite numerical implementation uses
midpoints of the certified critical integrals and remains diagnostic.

The regularized product satisfies0<R_e<=1 on the near-critical physical
domain. This removes the exponential loss in the earlier majorant. The
reviewed conditional moment bound is

    |P_N-P0|+|H_N-H0|
       <=10^9 e^(1/4)+10^9 B sqrt(e)+10^14 e.

A new sharp-kernel lemma supplies B=10^12 and, after endpoint sign
aggregation, N0=10^46 for existence and noncancellation. The analytic
components and exact arithmetic have passed independent internal review.
The accepted moment application uses the common domain e<=10^-10,
as clarified in proofs/M6_REAL_RATE_DOMAIN.md. The index remains
conservative and does not cover the numerically accessible low-index
range by a proof.

N512 is previously observed. N1024 was measured only after the prediction
protocol was frozen. The formula retaining all logarithmic orders passed
the declared9.33917e-6 tolerance with error1.83125e-6. The truncated
second-order prediction failed with error.00496921; this failure is
preserved. Neither numerical comparison constitutes an interval proof.

Reviewed components and proof sources are in proofs/M6_*.md. Canonical
Five canonical receipts are complete and verified: m6-coefficient-v1,
m6-directed-v1, m6-phase-predictions-v1, m6-threshold-v1, and
m6-phase-holdout-v1. The final independent audit passed in
results/m6-final-review.md.
The existing regression suite passed54tests; Python compilation and
exact-engine optimization guards also passed. M6_ACCEPTANCE.md records
the full result and the computationally useful threshold still not achieved.
