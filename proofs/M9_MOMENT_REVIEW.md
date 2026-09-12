# Independent review of the M9 linear moment rate

Verdict: the proposed bound
|P_N-P0|+|H_N-H0|<10^21 e_N(theta)
is valid on theta in [.8,.9], 0<e_N(theta)<=10^-10, conditional on the
inherited accepted real M5/M6 estimates and the separately reviewed
M9_PRODUCT_VARIATION lemma. No mathematical blocker was found. This result
is a real value-error estimate; phase derivative transfer and any new
uniqueness threshold require their own argument. It does not bridge the
unlisted finite indices or imply novelty.

## Weight measure

The critical kernel decreases in x. The positive first and second
u derivatives of f and f^2 imply that each regularized divided difference,
and therefore Vj,0, increases in u. Hence Vj,0 decreases in x. Combined
with K'=(-lambda+psi)K<0 this makes w=K*Vj,0 positive and decreasing.
The explicit square-root endpoint gives an integrable x^(-1/2) derivative
at zero, so w is absolutely continuous there; merely having a Holder
bound would not suffice, but that is not the argument used here.

The measure nu=-w' is nonnegative with mass w(0)<40. Integrating
(1+x)^2 against it gives w(0)+2*integral(1+x)w(x)dx<200, since
w<40 exp(-x). Boundary terms at infinity vanish. The removable formula
psi=kappa*J/(gamma*F) is correct: Taylor's integral identity has the
factor (1-u) exactly as displayed. With |J|<50, gamma>.4, F>.04 and
kappa<.3 it bounds |psi| by 937.5<1000 on I. The exterior two-term
bound is also below 1000. The M6 kernel derivative and M5 weight
Jacobian therefore give the local density nu<41000 on I. No bounded
density is required at zero or infinity.

## Exact cumulative identity

The primitive identity gives
 e*sum_(k=0)^n T_k=e*(n-a)T_n/(1-beta)+e*(b+1)/(1-beta).
Since b=a-beta, the last term is exactly s_g/(1-beta)+e. Thus the
boundary constant C_e contains the correct extra e, including the n=0
case. The continuous primitive Q=(x-c)G/(1-eta) has derivative G on
both sides, extends continuously through c, and Q(0)=-c/(1-eta).
It consequently gives A(x)=Q(x)+C_0 as stated.

For almost every x, A_e(x) is the cumulative mass of the discrete positive
measure e*sum T_n delta_(ne). Since w(t)=integral_t^infinity nu(x)dx,
Tonelli proves the displayed identity exactly, with the floor convention
at grid boundaries irrelevant to the Lebesgue integral. The same argument
applies to positive G. Exponential weight decay and the accepted product
envelopes prove finiteness. Subtracting the two identities and integrating
absolute cumulative error is therefore legitimate; no divergent signed
integration by parts or discarded crossing mass is hidden here.

## Primitive comparison and full domain

The replacement of B by K_eta=300000 is justified specifically in the
second term of M6_REAL_MOMENT_RATE equation (5): that term comes only
from varying the exponent and its sine multiplier. The center displacement,
Gamma ratio errors, and all smooth-product errors retain their independent
bounds. Thus this is not an unjustified global reduction of B.

For d_n>=10e the coefficient (d_n+.4e)/.28 is below 4d_n. Combining
that coefficient with the inherited product comparison and G<=10h gives
the stated 10^4*K_eta*e*h*[1+d_n(1+|log d_n|)] primitive bound.
There are at most 21 grid points with d_n<10e, and their grid cells have
total measure at most 21e. The primitive difference is at most
76000 e^(1/4) there. Against the bounded local density its contribution
is O(e^(5/4)), rather than the O(e^(1/4)) lost when comparing bare masses.
The critical grid spacing from M6 keeps the discrete G(x_n) values finite.

On H the far cusp sum is bounded by 40, by multiplying the inherited
damped bound 30 by exp(.25)<4/3. The interpolation Q(x)-Q(x_n) costs
one cell integral of G; summing and exchanging integrals costs at most
e*integral_I G, even for cells that cross c. Its bound 80 follows directly
from the two integrals of |x-c|^(-3/4).

Outside H, the entire relevant cell stays farther than .039 from c
on the stated e-domain. For d<=1, h<12 and the other bracket is <=2;
for d>1, log(d)<=d and d<=1+x give the claimed polynomial envelope.
Consequently the full infinite exterior contribution is controlled by
the weighted variation integral <=200. Every x>=0 is covered; the argument
has no implicit finite cutoff or omitted tail.

## Prefactors and exact arithmetic

The order of replacements is valid: first replace K_n by K with the exact
bounded weight, then replace the weight, then z0, then the cumulative
bare-profile integral. Each step uses the bound appropriate to that stage.
The factor Q/e<1 and the t^2 factor do not amplify these errors.
The separate inherited 10^14 e allowance controls boundary, Q/e and t^2
changes using the unchanged absolute mass estimate 2.4*10^7.

An independent integer/Fraction replay gave:

- Far local coefficient: 32800000000*K_eta*e.
- Closest-cell coefficient: 65436000000*e^(5/4).
- Total primitive coefficient after e^(1/4)<=1:
  9864065488000000 < 6*10^10*K_eta = 18000000000000000.
- Final two-moment coefficient:
  288360100001536000000 < 10^21.

These arithmetic checks support the analytic argument rather than replace
it. The result has ample final ledger slack.

## Provenance

Observed source commit during the preceding M9 review:
0a62a455d75d1880ab73ef7bae91cc3492d9d82e. Reviewed file hashes:

| File | SHA-256 |
|---|---|
| proofs/M9_LINEAR_MOMENT_RATE.md | 4510f1e74fec80c9d96018918c1e17e230e7afc7942d496e706255df87dc573c |
| proofs/M9_PRODUCT_VARIATION.md | 4830bf678a5733af94a927db275dda1f9ca61ab5e52d66daac4ac13b700a1ab8 |
| proofs/M6_REAL_MOMENT_RATE.md | 901ca9d78df982140078ec079462d31fb5b9b6527592e08cd062d99ce5040af8 |
| proofs/M5_EFFECTIVE_WEIGHTS.md | 3e941af8ac231dfb1833645459dd44dbdd697fb3502ba064c5d0d6d283c4e716 |
| proofs/M8_DISCRETE_PRIMITIVE.md | 284365adf0c8ce26bc93205e110b5788080f7237659e1ce9ccd9358340341488 |

The M6 sharp-kernel and product input hashes are recorded in
M9_KERNEL_REVIEW.md. No scientific proof file was edited by this reviewer.
