# M10 portable (N=32) full-band certificate

Status: **candidate exact certificate, pending independent review**.  This
note and `proofs/m10_full_band.py` cover one finite index, `N=32`, and the
phase band

\[
        \theta\in[4/5,9/10],\qquad a(t)=32+\theta.
\]

They make no statement for an unlisted `N`, for another phase band, or for
the asymptotic residue theory.  The producer uses the frozen M7 phase/moment
engine and the frozen M8 first-derivative engine; it introduces no new
enumerated data and does not modify those sources.

## Exact inputs and outer phase bracket

All endpoints are `Fraction` values and all interval arithmetic is the
384-bit outward dyadic arithmetic (`I384`) already used by M7 and M8.  The
producer starts from the frozen M7 seed

```text
0.41421207394799683735264571222663623
```

and the exact seed half-width `10^-7`.  It performs 80 exact phase
bisections for each target.  The selected lower and upper endpoints are

\[
\begin{aligned}
t_L&=
\frac{93272267066240905538577423361389732622106268130379}
{225179981368524800000000000000000000000000000000000},\\
t_R&=
\frac{46636134561417541055585897243227261435488558869877}
{112589990684262400000000000000000000000000000000000}.
\end{aligned}
\]

The stored endpoint interval fields certify, with strict outward endpoint
inequalities,

\[
             a(t_L)<\frac{164}{5}=32.8,
       \qquad a(t_R)>\frac{329}{10}=32.9.
\]

The endpoint phase intervals, the initial seed bracket, every bisection
count, and the exact `I384(t_L)`/`I384(t_R)` records are retained in the
`endpoint_phase_intervals` part of the JSON result.  This is an endpoint
certificate rather than a floating-point phase inversion.

The phase-coverage transfer uses the real inverse domain already certified by
`proofs/m5_phase_domain.py` and the directed derivative bounds in
`proofs/M5_DIRECTED_REFINED.md`.  For `0<e<=1/100`, those bounds give

\[
 a_e(e)=\frac{e s_g'(e)-s_g(e)}{e^2}<0,
 \qquad t_e<0,
 \qquad \frac{d a}{d t}=\frac{a_e}{t_e}>0.
\]

Thus `a(t)` is strictly increasing on this physical branch.  The exact
endpoint inequalities therefore enclose every target level `32.8<=a<=32.9`
in the single connected outer interval; they do not introduce a second
inverse component.  Each cell also checks the returned M8 phase-inverse
interval with the exact integer test `100*epsilon.hi < SCALE`, so the
inherited `e<=1/100` domain is explicit on every derivative cell.

The rational outer interval is partitioned into 128 adjacent cells,

\[
 t_k=t_L+\frac{k}{128}(t_R-t_L),
 \qquad [t_k,t_{k+1}],\quad 0\leq k<128.
\]

Full mode checks that the first cell starts at `t_L`, the last ends at
`t_R`, and every neighboring pair has exactly equal rational endpoints.
`produce(cell_subset=...)` is an explicit bounded review mode.  Its result
is labelled `PARTIAL ... DOES NOT CLAIM FULL COVERAGE`; it never changes that
label to a full-band conclusion.

## Cell certificate

For each requested cell the producer evaluates

```text
evaluate_derivative(I384(t_k, t_{k+1}))
```

from `proofs/m8_finite_derivatives.py`.  The cell record retains the complete
phase record and the complete returned engine record, recursively serializing
every `I384` and `Jet384` value and derivative.  In particular, the JSON
contains `q`, `epsilon`, `P`, `H`, `D_I`, `F`, the finite-prefix fields, the
directed-tail fields, and the prudent value/derivative tail fields.  It is
therefore possible to audit the tail closure without reconstructing a hidden
last-term estimate.

The explicit checks on every cell are:

* `phase_data(I384(...))` encloses both `a` and `b` strictly inside
  `(32,33)`, excluding the integer source-pole locations for both source
  factors;
* the M8 physical kernel, square-root, denominator, recurrence-sign, and
  contraction guards complete successfully;
* the directed geometric value and derivative tails and the prudent value
  and derivative tails are each nonnegative and at most `10^-18`;
* the upper endpoint of the complete interval for `F_t` is strictly
  negative.

The last item is a derivative certificate on the whole cell, not a finite
difference of a `C^0` enclosure.  Adjacent cells and the source-pole
checks supply the connected source-free interval needed to use strict
monotonicity of `F`.

## Transfer of the frozen M7 zero

The producer loads `results/m7-finite-v1/payload.json` and verifies its exact
SHA-256 before using it:

```text
75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f
```

The frozen M7 (`N=32`) narrow bracket is

```text
41421207394799683734264571222663623/100000000000000000000000000000000000
to
41421207394799683736264571222663623/100000000000000000000000000000000000
```

The loader rechecks the opposite endpoint signs of `F`, the whole-bracket
strict upper bound `1+P<0`, the phase/source-pole check, and containment of
this narrow bracket in `[t_L,t_R]`.  Thus the M7 intermediate-value zero is
inside the M10 outer interval and lies in the target phase band.  The full
128-cell derivative certificate makes `F` strictly decreasing on the
connected outer interval, so that zero is the only one there and is simple.
The M7 inequality (1+P<0) at that zero then excludes cancellation in

\[
                    W(t)=-1-\frac{1+P(t)}{F(t)}.
\]

The resulting full-mode conclusion is therefore: **exactly one simple
noncancelled W pole in the `N=32` phase band
\(\theta\in[0.8,0.9]\)**.  This conclusion is deliberately finite and does
not extend to other `N` values.

## Bounded replay and provenance

The bounded producer replay used the project environment and reviewed cell 0:

```text
.venv/bin/python -m proofs.m10_full_band --first-cell
```

The replay passed with the explicit partial classification.  Its JSON output
was `/tmp/m10-n32-first-cell.json`, with SHA-256
`72e73fcce174b5979afecd73bad594402a110539f0466377893667a8a960a246`.
The replayed producer source hash was
`8372d4cf50e291edc0700a49a9ad08ddbe4bf9e3a71d6efd77a9e4b10f140079`.
The frozen engine/input source hashes used by this producer were:

```text
proofs/m7_finite_poles.py       3712829fbf510e558e9215c7219731b40678ca9525e36387bb1f9d528f912c26
proofs/m8_finite_derivatives.py f721495320cd7439cc7079c24205c818e5bc02834322e2b8f142d0ccf8e887c4
proofs/m5_phase_domain.py       76b0b18fcb282e9d303754293258a1dedc7069514032814d9a833eba55310c97
proofs/M5_DIRECTED_REFINED.md   08668a0ddbba107c2f56cc88e0d5f1b549c9ddec92490f4d35ba5f4e4005e38a
```

The existing exploratory 128-cell scan supplied by the root task is
`/tmp/w-fullband-N32-full-128.json`; its hash at review time was
`87b60d0289fd0ad0f31f83d40e5852aa9aca88c153330a97479906c2948250d3`.
The producer separately reproduced the exact rational partition formula and
matched all 128 stored diagnostic cell bounds without rerunning the expensive
128-cell derivative scan.  A canonical full-mode run remains the root
reviewer's release check.

The optimized interpreter is intentionally rejected:

```text
.venv/bin/python -O -m proofs.m10_full_band --first-cell
```

because the inherited interval and receipt checks must remain enabled.  The
producer raises before claiming any result under `-O`.
