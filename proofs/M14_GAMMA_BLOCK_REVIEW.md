# Independent review of the M14 Gamma primitive envelope

The core shifted Gamma sandwich, coefficient interval and zero-start offset are analytically valid. Final source approval is recorded below after the auxiliary domain clarifications.

## Exact product and primitive audit

The positive finite-product recurrence gives Q_n-Q_(n-1)=T_n, including n=0 by the explicitly defined Q_-1. Because a,b share the same noninteger strip, their recurrence factors have the same sign and no denominator vanishes. Both Gamma representations follow by telescoping and, on the post side, reflection with a positive sine ratio.

Wendel plus the displayed weighted logarithmic concavity argument proves (z-beta)^alpha<=Gamma(z+alpha)/Gamma(z)<=z^alpha for z>beta. Pre-crossing y>=theta>beta permits this substitution directly; the negative primitive sign reverses the interval endpoints. Post-crossing the substitution z=y+beta and the Gamma recurrence give endpoints y^alpha and(y+beta)^alpha. This proves the unified shifted Qbar sandwich for every n>=0, including both indices adjoining the crossing. Subtraction with opposite enclosure endpoints proves the finite block bounds; their lower endpoints remain positive because the shift beta is less than one.

For the normalization coefficient, Wendel gives the upper endpoint(a+alpha)^beta. Its lower bound(a+alpha)/(a+1)^alpha exceeds a^beta by weighted AM--GM. Multiplying by e^beta gives precisely s^beta<=A_e<=(s+alpha e)^beta.

The zero-start offset h0=eA/alpha+Qbar(0) satisfies the two displayed integral bounds: the lower integral follows from the coefficient upper bound, and the upper integral follows directly from Wendel's lower bound A/(a+1)^alpha. These bounds imply h0>0 and h0<=e(1+alpha e/s)^beta<1.001e for N>=512, since e/s=1/a<1/N. Extending Qbar to negative x by the same pre-side power also gives Qbar(-e)<=eQ_-1<=Qbar(-alpha e), exactly the n=-1 form of the shifted sandwich. Thus no fictitious negative-index T is required.

## Auxiliary bounds

The coarse Wendel bounds apply with x=y+alpha on the pre side and x=y on the post side. Their common lower argument1/10 and coefficient argument A justify the stated factors. The sine bound follows from sin(pi*v)>=2v for0<v<1/2. The coefficient and Holder allowances are consequently valid. On opposite sides of the cusp, one adds the two side allowances rather than assuming differentiability at the cusp. Floors and ceilings introduce no more than one mesh step, and the zero-start case retains its separate offset.

The away-from-cusp estimate with rho^(-18/25) requires0<rho<=1; for larger rho, beta<18/25 does not permit that power replacement. This restriction is explicit in the corrected final source. The subsequent profile-comparison section already uses that restricted rho domain. Its coefficient logarithm follows from Wendel, the scalar displacement and beta perturbation bounds. The center displacement, exponent logarithm, normalization and sine terms are separately bounded with the correct signs; the resulting same-side ratio is positive even on the negative pre branch. These auxiliary estimates assert convergence and effective primitive allowances, not any weighted moment error or endpoint sign.

## Final source approval and replay

Status: PASS after the source owner corrected the auxiliary rho domain, defined the coarse x arguments, made the h=0 Holder endpoint nonstrict, and changed the producer scope to integer N. None of these corrections changes the core sandwich or offset result.

Independently replayed the final producer: all21 arithmetic checks PASS. Complete stdout SHA256: `10b2279aaa9fb6de9f937d7667fa8a1350c9a769f51f1faf8e971ddc4c071329`.

| Path | SHA256 |
|---|---|
| proofs/M14_GAMMA_BLOCK_ENVELOPE.md | a911e14576c9217ba6cc9d8e365067d4a544d2ab1767a70f91844772f769c9fd |
| proofs/m14_gamma_block_bounds.py | 64a8f44131ca584b07821647bfdf7e014eef32975c9a5c47b8de84bd0ff2905e |

No material findings remain for this Gamma component. Weighted product/moment approximation and endpoint signs are outside this review's conclusion.
