# CLAIM-0009 — Second logarithmic phase correction for W poles

Status: proved in the internally reviewed M6 draft; final acceptance
audit passed. Mathematical priority UNRESOLVED.

Use the same weakly prudent bridge series W and phase family as
CLAIM-0008. Put sigma=sqrt(2)-1, eta=1/sqrt(2),
s*=-log(1/2+sqrt(2)/4), L=logN, and K=s*²/16.
For the eventual unique simple pole w_N=t_N(theta_N),

    theta_N=theta*-C1/L+C2/L²+O(L^-3),

where C1 is the positive M5 coefficient and

    c_D=[log4-digamma(2+sqrt2)]/sigma,
    b=sigma(1+c_D)-log(s*),
    C2=C1[b+2sigma post1/J]-pi cot(pi(eta-theta*)) C1².

The critical integrals and J are exactly those in the M5 critical
certificate. The outward exact enclosure gives

    C2 in [.844491934033,1.148455190184],
    b in [2.569062496883,2.569062496884].

Consequently the spatial expansion gains the term

    sigma-w_N=K/N²-2K(theta*-eta/2)/N³
        +2K C1/(N³L)-2K C2/(N³L²)+O(N^-3L^-3).

The analytic input identifying c_D has explicit remainder
|D-log(1/e)/sigma-c_D|<=100e log(1/e) on0<e<=.01.
Finite phase fitting plays no role in identifying this constant.

There is also a phase approximation theta_hat_N defined by the zero of

    F0(theta)+[2sigma/(logN+b)](1+P0(theta))=0.

For sufficiently large N it is unique on the phase sector and obeys
theta_N-theta_hat_N=O(N^-1/20). This formula retains every logarithmic
order, with the remaining error controlled by algebraic convergence.

The separately proved sufficient threshold10^46 concerns existence and
noncancellation only. It follows from0<R_e<=1, a sharp kernel remainder,
a polynomial-constant real moment estimate, and certified endpoint signs.
It replaces the earlier2^(10^120) threshold but is still far beyond
feasible numerical enumeration.
No effective uniqueness threshold, second-order residue theorem, priority
claim, or result for unrestricted square-lattice SAWs is asserted.

Evidence: proofs/M6_DIRECTED_CONSTANT.md, proofs/M6_SECOND_ORDER.md,
proofs/M6_RESUMMED_PHASE.md, the corresponding independent reviews,
and results/m6-coefficient-v1. See M6_ACCEPTANCE.md and
results/m6-final-review.md for the complete acceptance audit.
