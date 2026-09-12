# Audit of the critical-integral quadrature

Reviewed 2026-09-12.  Scope is the integral certificate in
`proofs/m3_critical_integrals.py`; this audit does not certify the discrete
critical scaling limit or the resulting M3 argument.

## Verdict

I found no mismatch in the branch substitutions, density, phase signs, or
outward interval arithmetic.  The 2048-bin run is a valid enclosure of the
four proposed limit integrals, conditional on the formal integral formulas in
`proofs/M3_CRITICAL_PRODUCT.md` and `proofs/M3_NON_DFINITE_CANDIDATE.md`.
The result certifies only the signs of those formal limit integrals.  It does
not prove that the discrete products or moment sums converge to them, nor the
existence of infinitely many actual zeros of (1+P).

## Algebra and endpoint orientation

Write \(t=\sqrt2-1\), \(d=1-t\), \(u_*=1/\sqrt2\), and
\(\eta=u_*\).  From the candidate's

\[
 \phi(u)=\frac{(u-t)(1-tu)}{t(1-t^2)u}
\]

one obtains directly

\[
 \frac{\phi'(u)}{\phi(u)}
 =\frac{1-u^2}{u(u-t)(1/t-u)}.
\]

Multiplying this by the formal profile

\[
 M(u)=\frac{(u-t)^{2+\sqrt2}(1/t-u)^{\sqrt2}
 |u-u_*|^{-\eta}u^{-1-\sqrt2}}
 {(1-t)^{2+\sqrt2}(1/t-1)^{\sqrt2}(1-u_*)^{-\eta}}
\]

gives the script's non-moment shape:

\[
 \frac{(u-t)^{1+\sqrt2}(1/t-u)^{\sqrt2-1}
 |u-u_*|^{-\eta}(1-u)(1+u)}
 {\operatorname{norm}\,u^{2+\sqrt2}}.
\]

The exponent \(\sqrt2-1\) in the code is therefore correct: the extra
factor \((1/t-u)^{-1}\) comes from \(\phi'/\phi\).

For the pre branch, `side == 0` uses

\[
 u=u_*+(1-u_*)x^8,
 \qquad 0\leq x\leq1,
\]

which runs from \(u_*\) to \(1\).  For the post branch, the side-1 branch uses

\[
 u=t+(u_*-t)(1-x^8),
 \qquad 0\leq x\leq1,
\]

which runs from \(u_*\) down to \(t\).  Since the desired post integral is
oriented from \(t\) to \(u_*\), reversing the limits supplies the positive
absolute Jacobian used by the code.  In both cases

\[
 |du|=8\Delta x^7\,dx,\qquad
 |u-u_*|^{-\eta}=\Delta^{-\eta}x^{-8\eta},
\]

so the resulting power is \(x^{8(1-\eta)-1}\), exactly the exponent variable in the
script.  The remaining factors `ut`, `one_u`, and `1+u` have the correct
endpoint values on each branch.  The code's `divided` is
\(1/[u_*(1-tu)]\), matching the two (V_j) factors:

\[
 V_1=\frac{L+1/[u_*(1-tu)]}{d},\qquad
 V_2=\frac{L+(f(u)+1)/[u_*(1-tu)]}{d}.
\]

The phase formulas also match the candidate:
\(1+P_0=1-d-AJ_{1,\mathrm{pre}}+BJ_{1,\mathrm{post}}\) and
\(1+H_0=1+t^2[-3-AJ_{2,\mathrm{pre}}+BJ_{2,\mathrm{post}}]\), with
\(A=t^{-2}\) and \(B=A\sin(\pi\theta)/\sin(\pi(\eta-\theta))\).

## Independent arithmetic checks

The dyadic interval operations are outward rounded.  Repeated square roots
give an enclosure of the base raised to \(2^{-16}\); the floor/ceiling integer
exponents enclose the exponent interval, and taking the hull of the two
endpoint powers is sound on both sides of base \(1\) (including a base interval
that straddles \(1\).  The nonnegative endpoint clipping is sound because the
exact `ut` and `one_u` factors are nonnegative.

The Machin arctangent bounds use the alternating-series next-term remainder
for \(1/5\) and \(1/239\).  The sine routine retains terms through degree 79
and uses the degree-80 Taylor theorem (the even sine coefficient vanishes),
so the next-term bound \(x^{81}/81!\) is valid.  At the phase values used,
the sine denominators are positive and separated from zero.

I ran the certificate with

```text
PYTHONPATH=. .venv/bin/python proofs/m3_critical_integrals.py \
  --bins 2048 --power-bits 16
```

The output hash was
`dd851e6bb29bd0b75d97703dffcd0abe3488149e8dcdeab5b2408330324f3b12`,
identical to the supplied `/tmp/m3-critical-integrals.json`.  It reports

| branch | \(J_1\) enclosure (decimal display) | \(J_2\) enclosure (decimal display) |
|---|---:|---:|
| pre | [0.45986641, 0.46232754] | [0.650478, 0.65423355] |
| post | [0.42401814, 0.4263724] | [0.56790451, 0.5710073] |

and the asserted signs

| \(\theta\) | \(1+P_0(\theta)\) | \(1+H_0(\theta)\) |
|---:|---:|---:|
| 0.30 | [-0.19278831, -0.16685274] | [0.31077599, 0.31715257] |
| 0.35 | [0.16373676, 0.19165184] | [0.39270347, 0.39952767] |

As an independent numerical cross-check (not part of the certificate), I
integrated the unsubstituted \(u\)-densities at 80 decimal digits.  The
values were

```text
J1 pre  = 0.4610946231230832139109737971
J2 pre  = 0.6523516938500238569133033029
J1 post = 0.4251916668780859639174490505
J2 post = 0.5694512778690069945919697558
```

They lie inside the corresponding dyadic intervals.  Independent endpoint
tests of `real_power` over 107 nonnegative base/exponent rectangles, plus
Machin-π and sine checks, passed; the repository's two focused tests in
`tests/test_m3_critical.py` also pass.

## Boundary of the conclusion

The certificate establishes strict signs for the *formal limiting integrals*
only.  The separate transfer from those signs to infinitely many finite-N
roots is reviewed in `results/m3-non-dfinite-review.md`; that theorem remains
conditional on this arithmetic certificate and on the cited BB2014 formulas
and meromorphy result.  This file alone does not prove non-D-finiteness of
\(J\).

Provenance at this audit: base HEAD
`9087d31ddcf6c69ef6e62a7186755a3088724d6b`; SHA-256 of the audited source
`proofs/m3_critical_integrals.py` is
`da519b98367b64d29b18f50f13ecf42a2dae54550c6b3771fabbd92f8964cf16`.
