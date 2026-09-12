# M5 phase diagnostics: large-index finite exploration

Status: **EXPLORATORY NUMERICAL AND CALIBRATION EXTRAPOLATION ONLY**. This
note records a direct finite evaluation of the Bacher--Beaton formulas. It
does not certify an infinite sum, a root, root uniqueness, a sign for later
indices, a convergence rate, or the non-D-finiteness argument.

The accepted non-effective moment-rate candidate is recorded separately in
`proofs/M5_MOMENT_RATE.md` and its internal review in
`proofs/M5_MOMENT_RATE_REVIEW.md`. That result does not provide an explicit
first index for finite W roots. The calculations below are therefore
diagnostics for the accepted W argument, not a proof or a quantitative
replacement for that analysis.

## Direct evaluator and cost

The owned driver is `experiments/m5_phase_diagnostics.py`. It uses the
physical kernel branch

$$
q=U(t,1),\qquad
t\left(q+q^{-1}\right)=1-t+t^2+t^3,
$$

and inverts the existing phase coordinate by bisection:

$$
a(t)=\frac{\log v(t)}{\log(q(t)^2)}=N+\theta.
$$

For the partially directed term it uses the exact closed form of the
Proposition 8 recurrence,

$$
G_k=\left(\frac{t}{q}\right)^k
       \left(\beta+\gamma q^{2k}\right),
\quad
\beta=\frac{1-t-tq}{1-q^2},
\quad
\gamma=\frac{q\,[t-q(1-t)]}{1-q^2},
$$

so that

$$
D=\sum_{k\geq0}\frac{tq^k}{\beta+\gamma q^{2k}}.
$$

The summation stops after a geometric tail estimate is below the requested
working tolerance. This is a numerical stopping rule, not an outward
interval bound. The prudent terms for $P$ and $H$ are evaluated directly from
the BB summands, with

$$
M_N=\max\left(2000,\left\lceil\frac{c}{\epsilon}\right\rceil\right),
\qquad \epsilon=-\log(q^2),
$$

using $c=9$ during root location and $c=12$ for the final reported values.
The finite denominator diagnostic is

$$
F_N(\theta)=(3-t-2D_I)P-4H-(1+t+2D_I),
\qquad D_I=\frac{D}{1+D}.
$$

The default scan phases are $0.75,0.80,0.85,0.90$. The first sign-changing
bracket is refined by safeguarded secant steps, followed by one high-precision
Newton correction. The displayed $F_\theta$ is a central finite difference
with step $10^{-4}$; it is not a derivative estimate with a proved error.

The historical ad hoc calibration command was:

```text
.venv/bin/python experiments/m5_phase_diagnostics.py \
  --output /tmp/m5_phase_calibration.json
```

It used locator precision 52 digits, final precision 68 digits, eight
refinement steps, and a cooperative 120-second budget. The completed run took
81.64 seconds. The direct sums used 2,459, 4,885, 9,736 and 19,436 terms at
the reported roots for $N=32,64,128,256$, respectively. The closed-form $D$
sum used 15,536, 31,418, 63,736 and 129,484 terms; its final numerical tail
bound was about $10^{-14}$ in each case. The run predates the final
precision-context repair in the driver; root will rerun the canonical sweep
from the repaired source before freezing any receipt.

## Fixed phase-limit reference

The reference $\theta_{\mathrm{lim}}$ was reconstructed once from the
existing `results/w-critical-v1/payload.json` interval integrals. The payload
hash is

```text
ab5cbc0caf0f24f5b32e877668e87cc2d4d75cd830c62123ad450711f0c7ed6c
```

The certificate parameters are 2,048 rectangles and 16 fractional power
bits. Taking the midpoint of each stored integral interval and solving the
resulting fixed critical-limit formula gives

$$
\theta_{\mathrm{lim}}^{\mathrm{mid}}
 =0.8707742524874707084657127864\ldots.
$$

As a diagnostic for the uncertainty of this reference, solving with all 16
corners of the four stored integral intervals gives the box

$$
[0.8684421585455307,\;0.8731091557846466].
$$

The existing certificate proves the endpoint signs at $4/5$ and $9/10$;
it does not certify this interior root. The midpoint value is fixed before
any finite-$N$ fit and is not adjusted to the data.

The newer root-owned checker `proofs/m5_critical_pole.py` uses 4,096
rectangles and gives the authoritative internal interval

$$
\theta_*\in[1739/2000,109/125]=[0.8695,0.872].
$$

It also encloses the positive logarithmic phase-shift coefficient as

$$
C_{\mathrm{shift}}\in[0.38696091,0.44166261].
$$

Its independent location coefficient is

$$
N^2(\sigma-w_N)\longrightarrow
[0.00156711,0.00156712]
$$

at the level of the certified limiting expansion. The finite rows below are
close to, but do not certify, this limit.

Those certified limit bounds are separate from the scalar midpoint reference
used in the table below. For orientation, the certified theta interval gives
the following ranges for the last column:

| $N$ | lower value using $0.8695$ | upper value using $0.872$ |
|---:|---:|---:|
| 32  | 0.23617374 | 0.24483808 |
| 64  | 0.25397277 | 0.26436998 |
| 128 | 0.26812310 | 0.28025318 |
| 256 | 0.27960161 | 0.29346455 |

The finite fits below do not alter either the certified $\theta_*$ interval or
$C_{\mathrm{shift}}$ enclosure.

## Calibration results

Every listed root used the first direct sign change, which was the bracket
$[0.80,0.85]$ for all four indices. The columns $N^2(\sigma-w_N)$ and
$(\theta_{\mathrm{lim}}^{\mathrm{mid}}-\theta_N)\log N$ are numerical
diagnostics only.

| $N$ | $\theta_N$ | $D_I(t_N(\theta_N))$ | $F_\theta$ | $N^2(\sigma-w_N)$ | $(\theta_{\mathrm{lim}}-\theta_N)\log N$ |
|---:|---:|---:|---:|---:|---:|
| 32  | 0.801354663486230 | 0.931520542455054 | -14.3651207548 | 0.00152414730057 | 0.240589961959 |
| 64  | 0.808432456898186 | 0.938498694091880 | -13.3390485475 | 0.00154507031423 | 0.259272239063 |
| 128 | 0.814240018751241 | 0.944211316373391 | -12.6140929768 | 0.00155589384302 | 0.274305813036 |
| 256 | 0.819077518788584 | 0.948963697338885 | -12.0767943706 | 0.00156143028838 | 0.286667561660 |

The reported residuals $|F_N(\theta_N)|$ were below $4\times10^{-15}$ at
the final working precision. The corresponding $P+1$ values were
$-7.27665$, $-6.77538$, $-6.41733$, and $-6.14920$; these are finite
floating-point observations and not certified noncancellation bounds.

The slow movement of $D_I$ is visible even at $N=256$. It is the reason the
finite $D_I$ calculation is retained rather than replacing it by its limiting
value $1$ in this diagnostic.

## Calibration-only predictions

Only the four rows above were used in the following two affine fits:

1. $N^2(\sigma-w_N)$ versus $1/N$;
2. $(\theta_{\mathrm{lim}}^{\mathrm{mid}}-\theta_N)\log N$ versus $1/\log N$.

The fitted intercept and slope, with the maximum absolute calibration
residual, are:

| fit | intercept | slope | max residual |
|---|---:|---:|---:|
| $N^2(\sigma-w_N)$ vs. $1/N$ | 0.001566572903378 | -0.00136106440220 | $2.36\times10^{-7}$ |
| log-scaled phase offset vs. $1/\log N$ | 0.362289565863 | -0.424199647218 | 0.00101887 |

The second fitted intercept, $0.362289565863$, lies below the independently
certified interval $C_{\mathrm{shift}}\in[0.38696091,0.44166261]$. It is
therefore a **failed finite extrapolation of the asymptotic constant**, retained
as an adversarial diagnostic rather than evidence against the certificate.

The resulting **pre-registered N=512 prediction** is

$$
N^2(\sigma-w_N)\approx0.001563914574468,
$$

$$
(\theta_{\mathrm{lim}}^{\mathrm{mid}}-\theta_N)\log N
 \approx0.294290596154,
\qquad
\theta_N\approx0.823599632082.
$$

N=512 was not run in this calibration. The driver rejects indices above 256
unless the explicit `--include-heldout-512` flag is supplied. Any later N=512
run must be compared with these stored predictions and must not be included
in their refit.

## Limits and provenance

This experiment does not add an effective finite-$N$ root conclusion beyond
the separate accepted non-effective rate. In particular, the finite root
residual and negative numerical $F_\theta$ do not prove existence, uniqueness,
simplicity, or persistence of a root for all later bands. The phase-limit
midpoint is a fixed numerical reference derived from an endpoint-sign
certificate, not a certified interior root. The direct tail bounds are
stopping diagnostics, not interval certificates.

The historical pre-repair source script SHA-256 for this run is

```text
a458c929f2c67e9f84a5200ac267f37e5501ec3096e035ffc0f50f89c9b6e092
```

The repaired source is the file currently present in the worktree; root must
record its canonical output after the rerun. Its current repaired-source hash
is

```text
d4ab6762b731f7e92db85286a777279215b600d0d51a2715a3ed7b4919992d29
```

The ad hoc JSON output was retained at `/tmp/m5_phase_calibration.json` with
SHA-256

```text
ec7efb274a6cc011522da97bc0046156fbe3f1b9d80ebc27a7a44b255dd679c0
```

No result receipt was added under `results/`; root should freeze or discard
the ad hoc output independently after reviewing the code and numbers.

## Canonical rerun and reserved validation (root integration)

The repaired source was frozen at `8232d82e372860319b5562fef33a5982293ddbca`.
Its canonical calibration is `results/m5-phase-v1`, with payload SHA-256
`23c4c0ac3fecb8ac8eed5dadaa921b77f27615cb293324023a82390c7ef15946`.
The new decimal values agree with the displayed historical calibration at
its stated precision. No N=512 data was used in those fits.

The protocol `experiments/m5_holdout_protocol.json` and that calibration
were committed at `24b3839` before the reserved run. The two tolerances were
fixed to five times the maximum calibration residual; they are heuristic
prediction tolerances, not confidence intervals or theorem error bounds.
The receipt `results/m5-phase-holdout-v1` records:

| Observable at N=512 | Prediction | Observed | Absolute error | Fixed tolerance |
| --- | ---: | ---: | ---: | ---: |
| N²(sigma-w_N) | .001563914574468 | .001564243584359 | 3.2901e-7 | 1.1798e-6 |
| (theta_mid-theta_N) logN | .294290596154 | .297015232794 | .00272464 | .00509436 |

Both comparisons passed, without refitting. The observed phase is
`.823162874329661486457228383458440770`. This out-of-sample success does
not repair the failed extrapolation of the asymptotic constant: its
calibration intercept remains outside the independently certified interval.
