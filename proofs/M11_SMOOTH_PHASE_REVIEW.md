# Independent review of the smooth phase factor

The inverse-kernel argument proves the proposed smooth-product bound on
N>=32, theta in [.8,.9], n<=60N, subject to the final scope/ledger
clarifications recorded below. Combining it with the reviewed weight and
bare-product results gives a negative derivative for the positive
post-crossing summand on N+1<=n<=60N. This is not a sign theorem for F_N.

## Factorization and signed scalar boxes

Expanding the inverse kernel gives
v_t(u)=[1+t^2-t(u+1/u)]/[t(1-t^2)], from which the difference identity
in equation (5) follows with the stated sign. Applying it at h and u_g,
then using the exponential secants, yields exactly
R=(u_g/h)*(1-uh)/(1-u*u_g)*M(s,s_g)/M(s,s_h).
In particular the orientation of the two M factors is correct. All
non-secant denominators remain positive, and the positive integral
representation of M removes both crossing singularities.

The scalar code rebuilds the previously reviewed signed t/q interval
and implicit derivatives. Its expression for s_g' is the derivative of
the exact four-log formula. The checks apply to the complete signed box,
not only positive e. The identity h(e)=u_g(-e) therefore transfers the
u_g value interval to h and reverses the derivative sign. This use of
symmetry is exact; the broader direct h diagnostic is not silently used
as a sharper bound. The rational identity
h-u_g=t^2*(1-q^2)/(CD) gives the .51e allowance on positive e.
Likewise s_h(e)=s_g(-e) supplies the required derivative bound on both
anchors.

## Kernel motion and logarithmic secants

The kernel motion proof derives e*|u_j,e| directly at fixed integer j;
it does not reverse an upper bound involving the potentially small
phase derivative. The discriminant gap e^2+3(1-v) covers j=0, and
x*v<=1-v controls every larger j. The resulting 127/210<.61 allowance
is valid without a finite ray cutoff.

In log(1-uh)-log(1-u*u_g), differentiating in u produces the cancellation
(u_g-h)/[(1-uh)(1-u*u_g)]. This cancels the potentially 1/e scale in
u_j,e. The separate anchor contribution is below .52/.29, while the
mesh contribution is below .51*.61/.29^2. The u_g/h logarithmic scalar
ratio costs less than .52/.70. All are whole-domain bounds.

Writing log M=-s+log integral exp(v(s-a))dv gives
partial_a log M=-E[v] and partial_sa log M=-Var(v), with absolute mixed
derivative at most 1/4 for a variable supported on [0,1]. Thus the total
e derivative along s=je of the logM ratio is bounded by .8+.18je.
The .18 coefficient uses |s_g-s_h|=beta*e<.72e. For factors j<n<=60N,
je<10.2, giving the stated .8+1.836 bound. Summing the five contributions
is 8.907<9. This constant bound is restricted to that working prefix;
the more general .8+.18je expression remains valid beyond it.

Multiplying the factor bound by n*|e_theta| gives 91.8/N. The real
geometric ratio r=qC/D has
(log r)_e=-1/2+(-q/2-t_e)/C+(q*t_e+t*q_e)/D.
The stated scalar boxes and |t_e|<1/400 bound its absolute value by
1/2+(.5+.0025)/.57+(.0025+.4143/2)/.58<2.
Consequently r^n contributes at most 20.4/N, and the complete smooth
factor contributes at most 112.2/N.

Adding the independent weight allowance 11/N to the bare-product
negative margin gives
1435/342-123.2/32=1183/3420>.345. This controls the positive
post-crossing summand through n=60N only. Pre-crossing terms, boundaries
and the distant tail remain unestimated, so no full denominator sign or
complete index coverage follows.

## Findings and final replay

The first draft incorrectly described the constant per-factor bound as
holding for every j>=0; it requires 0<=j<n<=60N. I requested that scope
correction and an explicit scalar log-r arithmetic guard. The total
mesh-derivative notation for the M ratio also needs to include the s=je
chain rule. These are resolved and final hashes recorded below only after
the implementation worker releases the corrected files.

Final corrections verified: equation (26) now restricts the factor bound to
0<=j<n<=60N; equation (24) uses the total mesh derivative notation; and
the geometric bound includes an explicit rational log-r allowance and
physical e/7<1/400 guard. The guard uses .415/2 rather than .4143/2,
a safe enlargement. These resolve the findings without changing scope.

Independent final replay passed all 29 guarded claims. I also checked the
inverse-kernel difference and rational factorization identities independently
with symbolic algebra. Smooth producer sorted JSON SHA-256:
5cb292bc44e04c659297358f427859259ad94b0d6bf409468906b29fce329987.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M11_SMOOTH_PHASE_BOUND.md | 7a99778ac8135da260681f6d36495af412788c97349764c73d3012976b7ebf0c |
| proofs/m11_smooth_phase_bounds.py | 720e4d0f4d61cee04ea51db61f9130dc4791c294cd35f519f1fa0ba58c20fe44 |

Final verdict: PASS for the smooth-product and stated finite-window
post-crossing component result. No scientific proof or producer was edited
by this reviewer, and no full F_N sign is inferred.

## Final canonical proof typography correction

The canonical M11 freeze captured the intended explicit plus sign between
the two quotient terms in the equation (28) log-r allowance. A later attempt
to preserve the earlier approved byte hash restored the version without
that sign. The integrating root restored the canonical version. I compared
the two files directly: the only difference is the added `+` between those
terms. This is the sum already used in my derivation and in the unchanged
Fraction checker, so the canonical version correctly expresses the reviewed
inequality. The earlier byte version is preserved at
results/m11-review-history/smooth-note-before-plus.md; its historical review
table above is retained rather than rewritten.

The final current/canonical proof is approved at the following hash. No
producer arithmetic, canonical payload or scientific claim changed.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M11_SMOOTH_PHASE_BOUND.md | 15e8c64e5d554a12eb40b68ef0b724d2aead52042779516fce9e78628f180f07 |
