# M13: uniform strict phase decrease of the W denominator

Status: integration theorem awaiting independent review and frozen receipt.
All indices N in this note are integers. The domain is N>=32 and
theta in[4/5,9/10], with the physical phase inverse e=e_N(theta).

## Statement

On every such complete real phase band,

    dF_N/dtheta < -3141/64000 < -1/25.                  (1)

Consequently F_N has at most one zero in its band. Any zero is simple,
and the corresponding W=-1-(1+P)/F has a simple noncancelled pole.
Existence for every index N>=32 is NOT asserted by this theorem.

## Exact decomposition and domains

The M12 identity and M10/M11 real regularization give

    F_N = B + S_pre + S_mid + S_tail,
    J_n = A0 T_n K_n L_W(u_n) > 0,
    S_pre = sum_(n=0)^N J_n,
    S_mid = sum_(n=N+1)^(60N) J_n,
    S_tail = sum_(n=60N+1)^infinity J_n.                (2)

Here N is fixed during differentiation. The two finite index sets and
the tail form an exact partition including n=0. The phase strip gives
a=N+theta and b=a-beta in(N,N+1), so neither source crossing hits an
integer. The accepted real/complex local regularization applies.
The M13 tail proof establishes locally uniform convergence of the sum
and its derivative over the complete real band, justifying (2) after
differentiation. No finite truncation replaces the infinite sum.

## Reviewed component inequalities

The new component proofs give the following bounds on precisely this
same domain:

| Component | Bound | Source |
|---|---|---|
| Boundary | B_theta < 6/(5N^2) | M13_BOUNDARY_PHASE.md |
| Initial mass | S_pre < 31/10 | M13_PRE_MASS.md |
| Initial mass for32<=N<=64 | S_pre < 2 | M13_PRE_MASS.md |
| Initial derivative | S_pre,theta < (103/(50N)) S_pre | M13_PRE_CROSSING_RESEARCH.md |
| Middle derivative | S_mid,theta < -9/50 | M13_MIDDLE_STRENGTHENED.md, using M13_MIDDLE_MASS.md |
| Tail derivative | abs(S_tail,theta) < 1/1000 | M13_TAIL_PHASE_BOUND.md |

All inequalities are analytic statements with exact constant ledgers.
The ledger checks arithmetic implications, while the independent
component reviews check the analytical hypotheses and estimates.

For32<=N<=64,

    S_pre,theta < 103/(25N) <= 103/800.                (3)

For integer N>=65, the other mass allowance gives

    S_pre,theta < 3193/(500N)
                <=3193/32500 <103/800.               (4)

These two cases cover every integer N>=32, including both endpoints
64 and65, without any sampled-index interpolation. The boundary is
at most6/(5*32^2)=3/2560. Summing (3) or (4) with the other bounds,

    F_N,theta < 103/800 + 3/2560 - 9/50 + 1/1000
              = -3141/64000 < -1/25.                 (5)

This proves (1). The negative middle mass controls the possible positive
initial, boundary and tail contributions; no unproved monotonicity of
S_pre is needed.

## Simplicity, noncancellation, and actual coverage

Strict decrease gives at most one zero by the mean value theorem. The
real phase map is differentiable and has nonzero derivative in t on
each band (M5 phase inverse); hence a nonzero theta derivative at a zero
also means a nonzero t derivative. Local meromorphy of the regularized
formula then makes that denominator zero simple. M12 proves 1+P<-2
at every such zero, so the W numerator cannot cancel it.

The frozen M7/M8 certificates establish a zero inside the band for each
N in{32,64,128,256,512,1024}. Equation(1) now upgrades uniqueness from
each narrow certified bracket to its ENTIRE phase band. The finite
residue enclosures remain unchanged. The M9 theorem separately supplies
existence for every N>=10^27, and hence the full-band conclusion there.

For other indices32<=N<10^27, this theorem supplies at most one simple
noncancelled pole if a zero exists. It supplies neither endpoint signs
nor existence. In particular strict decrease alone cannot show that a
zero lies inside the chosen interval. The full W goal remains active
until the missing existence coverage and final integration obligations
are discharged.

## Reproduction

Run `python -m proofs.m13_combination_bounds` for the exact rational
case split and arithmetic margin. The complete M13 receipt must also
replay the component producers, check their independently reviewed
source hashes and retain the accepted M10--M12 dependencies. This note
does not claim a new pole-position or residue error estimate, an
external peer review, or a public release.
