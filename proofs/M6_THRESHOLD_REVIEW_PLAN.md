# M6: structural audit of the effective threshold

Status: **independent research plan and structural derivation; not an
accepted reduced threshold**. M6 requires both a second logarithmic
correction and a substantial threshold reduction. Completing only one
does not complete the objective. No M5 source was changed.

## Where the M5 threshold is lost

The dominant waste is the nonsingular-product bound exp(10B), with
B=10^50 inherited from a tiny complex crossing disk. This forces
A=exp(10^54), then exp(10^60) in the moment error. The auxiliary domain
log(1/e)>=10^100 is also far stronger than the actual physical restrictions.
These choices dominate N0=2^(10^120); the final sign-margin arithmetic
does not require anything comparable.

Other losses are separable:

- The actual critical weighted mass is replaced by A, although M5 already
  bounds it polynomially. Gamma constants from Wendel are small.
- A fixed exponent .05 is obtained by discarding an entire crossing window
  and applying a coarse global Hölder quadrature bound outside it.
- Two independent P,H error bounds ignore their correlation in F.
- The directed additive error80 makes its standalone reciprocal expansion
  quantitative only very late. A sharper directed remainder is a separate
  worker's task and must be inserted before claiming a useful threshold.
- The final bracket [.8695,.872] has small endpoint margins. For a first
  existence index the wider [.8,.9] band has much larger certified margins;
  a narrow localization bracket need not be imposed at the same index.

## Exact sign of the regularized product

There is a direct real-variable route that eliminates exp(10B). Put
c=t(1-t²), Y(v)=U(t,v)-t. The kernel quadratic rearranges exactly to

    Y = v*c*(t+Y)/(1-t²-tY).

For 0<t<sigma, the right-side power series in Y has nonnegative
coefficients. Iteration at v=0, or formal coefficient recursion, therefore
gives nonnegative coefficients in Y(v). The physical branch's nearest
v singularity is v_c=(1-t)/(t(1+t))>1, so this series and its derivatives
converge at v in [0,1]. Write U(t,v)=t+sum_(m>=1)c_m v^m with c_m>=0.
Then, for D=1-tq>0,

    g_e(s)=t²q-D sum_(m>=1)c_m exp(-m s),
    g_e'(s)=D sum_(m>=1)m c_m exp(-m s)>0,
    g_e''(s)=-D sum_(m>=1)m² c_m exp(-m s)<0.

Thus g_e is increasing and concave on the real half-line. For any fixed s,
the secant slope (g_e(s)-g_e(r))/(s-r), with its derivative value at r=s,
is nonincreasing in the anchor r. This also follows by integrating
g_e'(r+u(s-r)): increasing r increases the integrand's argument for u<1,
and g_e' is decreasing.

Since s_h<s_g,

    0<F_e(s)<=G_e(s),    0<R_e(s)=F_e(s)/G_e(s)<=1.

The definitions are exactly the accepted divided differences because
g_e(s_g)=0 and g_e(s_h)=-delta. The conclusion includes both removable
root values and all real s>=0. Consequently every finite smooth product
is at most one. This is a structural inequality, independent of the
size of a Cauchy remainder constant.

The existing pointwise limit also gives psi(s)<=0. This sign controls the
limiting smooth exponential, including its removable crossing value; no
independent normalization constant is introduced after the crossing.
The product worker should verify this derivation independently before it
becomes an input to a new accepted threshold.

## Much smaller absolute profile bounds

The exact factorization immediately yields

    |z_n| <= |z0| r^n |T_n|.

For the critical profile the accepted Gamma limit and psi<=0 similarly give

    |Z_theta(s)| <= A0*C_theta*exp(-lambda s)
                         (s*/|s-s*|)^eta,

where A0=1/sigma² and C_theta is1 before the crossing and
|sin(pi theta)/sin(pi(theta-eta))| afterward. On [.8,.9] the multiplier
is bounded by5, and A0<6.25. This gives a small explicit cusp envelope
without exponentiating10^50. Integrating it by splitting at the crossing
and a fixed tail cutoff gives a correspondingly modest mass bound.
The precise constants should be computed and certified in the new lemma,
not inherited from the huge M5 ledger.

In this phase sector the exact Gamma factors are positive and z0<0, so
every z_n is negative. This extra sign may help bound the combined F
moment directly. It does not by itself prove the sign of its weight:
that weight must be checked on its parameter box before any one-sided
argument is used.

## A defensible route toward a useful threshold

1. Replace the absolute smooth-product estimate by R_e<=1. Retain a
   separate explicit approximation bound for log R_e/e-psi; the sign
   alone proves domination, not convergence or a numerical error rate.
2. Obtain that approximation bound from real algebraic divided differences
   on practical parameter boxes. Near the crossing cancel the removable
   zero symbolically; at s=0 retain the discriminant comparison with
   s+e². Tiny complex disks are unnecessary for real endpoint signs.
3. For the crossing contribution, consider summing its exact Gamma factor
   against a slowly varying smooth weight. Bounding the smooth-weight
   variation around the crossing is potentially much sharper than throwing
   away the full mass O(rho^(1-eta)). This requires a real remainder bound;
   a fitted cancellation or a formal integral is not sufficient.
4. Use interval rectangle or Taylor bounds on the remaining finite compact
   region and an analytic exponential tail. Preserve actual polynomial
   mass constants and optimize cutoffs using the certified error ledger.
5. Apply the combined error first to the wide phase endpoints with their
   large certified limiting margins. Couple this with the improved
   directed-term remainder. Only afterward ask for a narrow phase location,
   effective uniqueness, or second-order residual estimates.
6. If the general estimate starts at a still moderate N_large, cover a
   finite earlier range by genuine interval-certified endpoint evaluations
   and source-pole exclusion. Numerical sign scans cannot close that gap.

A useful threshold is an output of this ledger, not a preselected number
to be justified after observing data. Root should report both the smallest
proved sufficient index and exactly which property it guarantees.

## Relation to the second logarithmic correction

The accepted algebraic moment rate is asymptotically smaller than every
fixed inverse power of logN, so the new second-order phase coefficient
will chiefly need the directed additive constant and careful implicit-root
Taylor expansion. That non-effective fact does not reduce N0 by itself.
Conversely, R_e<=1 and a better real ledger do not identify the additive
directed constant. The two workstreams must remain separate until both
have been proved, reviewed, and combined with explicit scopes.

This review plan contains no reduced N0, no numerical fit, and no claim
that the full M6 objective is already achieved.

Reviewed base HEAD: `76106cfee741e7e71fb3ad11bbf5bb998b9c6272`.
M5 threshold input SHA-256:
`5caf2b70e21ca0a4ec6ade19433e448e69f6b8aa13b2f0796e3043d7c9364c56`.
Kernel/Gamma/weight inputs retain the hashes recorded in the accepted M5
threshold review. This plan produced no numerical output.
