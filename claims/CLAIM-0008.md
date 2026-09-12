# CLAIM-0008 — Quantitative accumulation of weakly prudent W poles

Status: **proved in the internally reviewed M5 draft**. Publication priority:
**UNRESOLVED**. Internal AI review is not external peer review.

Use exactly the BB2014 W series and the real phase family a=N+theta from
CLAIM-0007. Put sigma=sqrt(2)-1, s*=-log(1/2+sqrt(2)/4), eta=1/sqrt(2).
For sufficiently large N there is exactly one W pole w_N=t_N(theta_N)
in the phase sector[.8,.9], and it is simple. Its phase satisfies

    theta_N=theta*-C_shift/logN+O((logN)^-2),

where theta* is the unique zero of the critical denominator F0,
p*=1+P0(theta*), f*=F0'(theta*), and C_shift=2sigma p*/f*>0.
The certified limit enclosures are

    theta* in [.8695,.8720],
    C_shift in [.38696091,.44166261].

The residues satisfy

    Res_(t=w_N) W=C_res/N³+O(1/(N³logN)),
    C_res=-p*s*²/(8f*) in [-.00167097,-.00146400].

With K=s*²/16, the spatial expansion is

    sigma-w_N=K/N²-2K(theta*-eta/2)/N³
                 +2K C_shift/(N³logN)+O(1/(N³log²N)).

An explicit sufficient index N0=2^(10^120) guarantees at least one
noncancelled pole in each corresponding phase band for every N>=N0.
This effective bound concerns existence and noncancellation only; the
uniqueness, simplicity and residue thresholds above remain non-effective.
The bound is not presented as sharp or computationally useful.

The proof combines the directed logarithmic estimate, quantitative C0/C1
moment convergence, a directed phase-derivative bound, exact critical
integrals, and separately reviewed explicit real majorants. Finite numeric
root fits do not establish the theorem. The failed small-index estimate
of C_shift and the independent held-out check at N512 are both retained.

Evidence: [M5_ACCEPTANCE.md](../M5_ACCEPTANCE.md). Main transfer:
`proofs/M5_W_QUANTITATIVE.md`; effective bound:
`proofs/M5_EFFECTIVE_THRESHOLD.md`. Their independent reports record
accepted hashes. Effective source freeze: `36de162`; final verification:
`results/m5-final-verification.json`. Six canonical receipts are linked
from the acceptance dossier. No M5 publication or external review occurred.
