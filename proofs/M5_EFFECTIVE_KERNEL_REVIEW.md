# Review of explicit nonsingular-kernel constants

Status: **ACCEPTED for the internal mathematical-draft gate for (K) only**.
This review does not accept an aggregate effective W threshold. The domain
is real 0<e<=10^-100, s>=0 and the common bound is B=10^50.

## Disk and constant audit

1. On the t circle of radius .01 the three polynomial factors have
   lower moduli .01,.57,2.82. Their product exceeds .016. The cosh-series
   remainder bound gives the displayed right-side estimate for complex
   |e|<=.001. There is exactly one root counted with multiplicity, hence
   a simple analytic root. Dividing the same equation gives
   |t-sigma|<e²/10 since (.425/3)/(.57*2.82)<.1. Evenness and the real
   branch follow from uniqueness.
2. On the crossing s disks, the real-part discriminant margin really is
   positive: .85²-.0011²-4*.415²>.03. The principal square root and the
   rationalized physical kernel therefore stay analytic. The bound |g|<2
   and the .0005 Cauchy margins give the listed derivatives, including
   16*10^6 for g_ss and8*10^6 for g_es.
3. The tightest lower-bound multiplication is
   .58*.77*.4*.82/(3*1.2)>1/25. Also .8/(1.172+1.2)>1/3, so the U
   lower bound used there is valid. At s*, the linear term has modulus
   sigma*r_s and the second-order remainder is at most8*10^6*r_s².
   Its difference exceeds .4*r_s. The perturbations4000*r_e and delta
   are far smaller, so Rouché supplies a unique analytic root for each
   of g and g+delta in the stated tiny disk.
4. A point on the segment to either root lies within2*10^-10 of the real
   interval. The complex derivative perturbation is at most
   16*10^6*(2*10^-10)+8*10^6*10^-20<.004. Thus Re g_s>1/100 along
   both segments and |g_s|<4000. This proves the corresponding bounds for
   the divided differences throughout the required product domain.
5. Re F,Re G>.01 and |F|,|G|<4000 imply principal logarithms of modulus
   less than10: their real parts lie between log(.01) and log4000 and
   their imaginary parts have modulus below pi/2. They therefore give
   |L|<20, with L(0,s)=0. Cauchy's Taylor remainder is
   40|e|/r_e²=4*10^41|e|, below B|e|. Differentiating L at zero gives
   the stated psi. The s disk produces a derivative bound below10^32.
6. For the root difference, each root remains in its radius r_s disk and
   their difference vanishes at zero. The same Cauchy remainder gives
   4r_s|e|/r_e²=4*10^30|e|<10^31|e| after division by e. The leading
   derivative is kappa/g_0'(s*)=eta, with the stated sign.

The strict rational disk and derivative margins in items1--4 were also
checked independently with exact Fraction arithmetic. This was a short
arithmetic check, not numerical fitting of analytic constants.

## Real half-line completion

The uniform discriminant perturbation bound100|t-sigma| is conservative
for t in [.4,sigma], v in [0,1]. The nonnegative square-root inequality
and rationalized denominators>=.8 give ample room for the stated100e
kernel and200e g errors. The same algebra supplies the global critical
1/2-Hölder bound; distances>=1 are handled by boundedness.

The crossing-to-endpoint distance is at least .053 on the left and .083
on the right. Multiplying by the proved derivative lower bound1/25 gives
more than .001 at both boundaries. Monotonicity extends these bounds
over the exterior half intervals. Root displacements give the stated
.05 and .08 separations. The real mean-value theorem yields the explicit
400000e root displacement. The quotient expansion for delta/e has
denominator q-t>.58 and parameter increments O(e), making its bound100e
conservative.

In the two-log expansion outside the crossing interval, the root-coefficient
error10^31 e is divided by at most the reciprocal of .05. Other errors
involve only the100e and200e perturbations and denominator lower bounds
.001 or .0001. All are well below the proposed10^40 e budget. The
quadratic logarithm remainder is applicable because both log arguments
have perturbations bounded by a fixed multiple of e, with e<=10^-100.

The exterior Hölder bound for psi follows from the reciprocal difference
identity and |g_0|>.001, with constant below10^10. In the middle interval
the Cauchy derivative bound is below10^32 and implies the required
Hölder estimate. Splitting at two boundaries costs at most sqrt(3), still
far below B. The modulus bounds have the same margin.

Finally, r=1-(1-q²)/(1-tq) is exact. Its denominator stays above .58,
and its perturbation from1-sigma is at most2e, so the logarithmic
remainder is safely bounded by B e. The z0 denominator differs from
-sigma² by at most4e and remains above .17 in modulus, proving the
last estimate. No explicit-disk or constant blocker was found.

## Scope and provenance

This establishes the listed real nonsingular-product, root-offset and
critical-modulus component estimates. It does not supply effective
Gamma-ratio, moment-weight, complex-phase or final pole-threshold bounds;
those require their own aggregation and checks. In particular this real
estimate alone cannot be fed into Cauchy's formula for theta derivatives.

The source hash below fixes exactly the text reviewed. Later changes to
disks, constants or domains require reviewing those changes.

Observed source HEAD: `24b383916083ad18ca9b57594571bdbd37a1f588`.
Accepted `proofs/M5_EFFECTIVE_KERNEL.md` SHA-256:
`8eed3eefc97ee2fbefc09aa51f3de161c30de23d6c520303503ef7f1f8faa090`.
