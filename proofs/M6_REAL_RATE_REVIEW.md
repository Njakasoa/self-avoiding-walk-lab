# Review of the polynomial-constant real moment estimate

Status: **ACCEPTED at the internal mathematical-draft gate, conditional
on the product hypotheses (P)**. The requested Gamma-envelope derivation
has been added and verified. This review does not certify a
particular improved product constant or reduced threshold by itself.

## Damping and discrete masses

Both logarithmic smooth factors are nonpositive. Splitting the K difference
into an r contribution and a smooth-product contribution preserves
exp(-x_n) damping. The resulting3B*x_n*exp(-x_n)*sqrt(e) bound is valid
without a small relative exponential error. Also x*exp(-x)<=exp(-x/2)
for x>=0, since the maximum of x*exp(-x/2) is2/exp(1)<1.

The effective phase derivative interval implies s_g-s*=m_e e with
.3<m_e<.4. Thus s*/e=N+theta-m_e has fractional part in [.4,.6],
and the critical center is at least .4e from every grid point. This
spacing justifies discrete critical cusp estimates; omitting it would
leave arbitrarily large sampled singular values.

The power sums in (2) have ample constants. Within distance1, the two
integrals of d^(-3/4) and d^(-3/4)|log d| are8 and32 after both sides
are counted. The derivative-power integral starts beyond9e and is of
order e^(-3/4). Endpoint rectangles fit the stated bounds on e<=10^-8.
Beyond distance1 the exponential tail and its first moment control the
constant and logarithmic weights. These estimates apply to integrals and
to the actual shifted grid, not only an integer-centered singularity.

## Gamma comparison and requested clarification

The nearest-cell and global envelopes with exponent3/4 must be derived
from the M5 Gamma formulas with the actual eta_e<=.72, not from its
coarser exponent19/25=.76: the latter cannot imply a smaller exponent.
The needed derivation is available from M5's direct bounds
|T_n|<=20(a/|n-a|)^eta_e, the nearest distance |n-a|>=.1,
and (1+|n-a|)/|n-a|<=11. With s_g<.17 and center displacement<.4e,
the resulting constant is far below2000. This connection should be
written explicitly before accepting equations(3)--(4). It is now present:
20*11^(3/4)<200, the exact eta_e is enlarged only where a/|n-a|>=2,
and the remaining region is handled by a bounded ratio. The center shift
costs at most1.4^(3/4), well inside the2000 envelope. The revised proof
therefore closes this gap without invoking the incompatible .76 bound.

Away from10e, center motion preserves the side of the crossing and leaves
|n-a|>=9.6. The underlying Wendel3/a+3/|n-a| estimate still applies
there (its derivation only needs bases>=1), even though the convenient
M5 corollary was stated with distance>=10. Its logarithmic error remains
below .33, for which |exp(u)-1|<=2|u| is valid. Intermediate powers and
sine multipliers are bounded uniformly on eta_e in [.70,.72]. Applying
the mean-value theorem to the exponent avoids the invalid assumption
that B e |log d| is small on an infinite tail. The pointwise allowance1000
in (5) safely covers these changes.

The far Gamma-error sum is bounded by3*10^6 e^(1/4)+8*10^6 B e.
At most21 near indices contribute less than2*10^6 e^(1/4), using the
stated envelopes and weight40. Thus equation(6)'s arithmetic is correct.

## Critical quadrature and final ledger

With |V0|<40, Hölder constant110 and lambda<2, the damped Hölder
constant300B in (7) follows by splitting the K and V differences.
On a far cell, distance from the crossing decreases by at most e;
the d_n>=10e separation leaves a factor at worst .9 in the distance.
The actual power exponent eta<.72 and multiplier bound leave enough
margin for the20w(d_n)/d_n derivative estimate throughout the cell.
Summing cell errors gives the stated10^5 B sqrt(e)+3*10^4 e^(1/4)
allowance. Omitted near cells lie within11e; direct cusp integration and
the grid spacing fit the extra10^5 e^(1/4). There is no undifferentiated
endpoint assumption at s=0 and no crossing cell is integrated as if it
had a bounded derivative.

The product-comparison arithmetic is72,000,000 B sqrt(e). Weight
perturbation contributes720,000,000 e per normalized sum, and the z0
change contributes below20,000 B e. Combining both moments with
(6)--(8) fits the displayed2*10^8 e^(1/4)+4*10^8 B sqrt(e)+2*10^9 e.
The exact absolute normalized sum bound is24,000,000. Its multiplication
by the Q/e perturbation bound contributes24*10^12 e per moment; the
two such terms, boundary errors and t² change remain below10^14 e
with room for the preceding lower-order e allowance. Therefore (T)'s
three coefficients follow once the envelope justification is explicit.

That justification is now explicit and verified. No remaining substantive
blocker was found for the stated real moment error (T).

## Scope

The proof supplies a parametric real C0 moment bound under all hypotheses
(P), including |psi|<=B, which is necessary for the critical-factor
quadrature. R_e<=1 alone does not supply the approximation or Hölder
constants. The bound uses no growing cutoff and no exp(BS) factor.
It does not give an effective phase-derivative error or an effective
uniqueness threshold. A particular N0 still requires separately checking
the product lemma's B/domain and the final sign/numerator arithmetic.

Accepted revised `proofs/M6_REAL_MOMENT_RATE.md` SHA-256:
`901ca9d78df982140078ec079462d31fb5b9b6527592e08cd062d99ce5040af8`.
The reviewed M5 component sources retain their previously accepted hashes.
No numerical phase or moment run was performed for this analytic review.

## Domain erratum from threshold integration

The source header allows e<=10^-8, while the inherited M5 weight lemma
is stated for e<=10^-10. The accepted application scope of this review
is the intersection e<=10^-10 unless those inherited estimates are
separately extended. This clarification does not modify the frozen source
or affect the proposed threshold application at e<10^-46.
