# High-index prudent pole/root asymptotics: bounded numerical probe

Status: **EXPLORATORY NUMERIC ONLY**.  This note records a bounded
high-index calculation for the Bacher--Beaton kernel formulas.  It does not
certify the infinite pole family, the infinite iterated sum, an asymptotic
limit, or noncancellation in the irreducible quotient.

The probe 'experiments/m3_prudent_asymptotic_probe.py' reuses the existing
'kernel', 'evaluate', and 'pole' functions in
'experiments/m3_prudent_singularity_probe.py'.  For each selected index
\(\ell\), it solves the truncated equation \(P_N(t)+1=0\) between the
consecutive pole locations \(a_\ell\) and \(a_{\ell+1}\).  It repeats the
calculation at \(N=400,800,1600,3200\) terms, using 100 decimal digits for
the evaluations and 120 digits for the pole/bisection coordinates.

The scaled root phase is

\[
 \theta_\ell =
 \frac{r_\ell-a_\ell}{a_{\ell+1}-a_\ell}.
\]

This phase removes the rapidly shrinking interval width.  The second
observable is \(1+H(r_\ell)\), whose nonzero sign would prevent the
corresponding denominator zero from cancelling in
\(J=(P-H)/(1+P)\).

## Results at \(\ell=8,16,32\)

The final \(N=3200\) values are:

| \(\ell\) | \(a_{\ell+1}-a_\ell\) | \(-\log(q_{\rm mid}^2)\) | \(\theta_\ell\) | \(1+H(r_\ell)\) |
|---:|---:|---:|---:|---:|
| 8  | \(4.5442356291041072\,10^{-6}\) | \(1.7970642051853\,10^{-2}\) | 0.6580205609698710 | 0.3621165261886163 |
| 16 | \(6.5583796832326029\,10^{-7}\) | \(9.4078485795606\,10^{-3}\) | 0.6395991953740825 | 0.3589863858148749 |
| 32 | \(8.8425699086865707\,10^{-8}\) | \(4.8214579625550\,10^{-3}\) | 0.6295252546484479 | 0.3572290644519462 |

The pole gap is consistent with an \(\epsilon^3\) scale at this resolution:
\((a_{\ell+1}-a_\ell)/\epsilon^3\) is approximately 0.7830, 0.7876,
and 0.7889 for \(\ell=8,16,32\), where
\(\epsilon=-\log(q_{\rm mid}^2)\).  This is a numerical scaling check, not
an asymptotic theorem.

The phase and hook values remain positive and settle as the truncation is
doubled.  The observed truncation drifts show why the summand count must grow
with \(\ell\):

| \(\ell\) | phase drift \(400\to800\) | phase drift \(800\to1600\) | phase drift \(1600\to3200\) | hook drift \(400\to800\) |
|---:|---:|---:|---:|---:|
| 8  | \(6.13\,10^{-13}\) | \(0\) at displayed precision | \(0\) | \(6.73\,10^{-13}\) |
| 16 | \(5.56\,10^{-8}\) | \(1.58\,10^{-13}\) | \(0\) | \(5.86\,10^{-8}\) |
| 32 | \(3.27\,10^{-5}\) | \(3.85\,10^{-8}\) | \(7.53\,10^{-14}\) | \(3.22\,10^{-5}\) |

At \(\ell=32\), the final-term magnitude falls from about
\(4.22\,10^{-6}\) at 400 terms to \(3.66\,10^{-26}\) at 3200 terms.  The
last term is useful as a diagnostic but is not a tail bound for the product
series, so these figures remain numerical.

A two-point linear extrapolation in \(1/\ell\), using the \(\ell=16,32\)
values, gives

\[
 \theta_\infty^{\rm heuristic}\approx0.6194513139,\qquad
 (1+H)_{\infty}^{\rm heuristic}\approx0.3554717431.
\]

The phase is therefore compatible with a limiting interval fraction near
0.62.  The hook values are compatible with a positive limit near 0.355.
The formal critical-product/integral calculation in
'proofs/M3_CRITICAL_PRODUCT.md' gives the separate numerical prediction
\(0.35528532226781205\) for the limiting hook gap.  Agreement at three
indices is evidence for the scaling candidate only; it does not validate the
formal connection across the critical point \(u_*=1/\sqrt2\).

## What would imply noncancellation

The exact moment/product identities in
'proofs/M3_CRITICAL_PRODUCT.md' reduce the question to a regularized hook
moment.  The formal critical ODE determines the product shape on either side
of \(u_*\), but it does not determine the relative multiplicative constants
across that singular point.  Those constants encode the discrete connection
information needed at the roots \(P(r_\ell)=-1\).

A sufficient asymptotic representation would be, for some \(\alpha>0\),

\[
  H(r_\ell)+1 = h_* + O(\ell^{-\alpha})
  \quad\text{with}\quad h_*>0,
\]

or the equivalent uniform scaled form

\[
  H(r_\ell)+1
   = \mathcal H(\theta_\ell,\epsilon_\ell)
     + O(\epsilon_\ell^\alpha),
 \qquad
  \inf_{\theta\ \mathrm{near}\ \theta_*}
  \liminf_{\epsilon\downarrow0}\mathcal H(\theta,\epsilon)>0.
\]

Deriving such a formula requires uniform product estimates away from \(u_*\),
a local discrete connection formula through \(g(u)=0\), and a remainder
bound for the regularized moment.  The formal ODE by itself cannot supply
the sign.  The finite values above suggest \(h_*>0\), but they do not give a
uniform lower bound and do not prove that later zeros of \(1+P\) survive in
the quotient.

## Reproducibility and classification

The bounded default run was:

~~~text
PYTHONPATH=. .venv/bin/python experiments/m3_prudent_asymptotic_probe.py \
  --indices 8 16 32 --terms 400 800 1600 3200 \
  --dps 100 --pole-dps 120 --max-seconds 300
~~~

It completed in about 155 seconds.  Pole coordinates and root bisection were
kept at the 120-digit mpmath context; a context restoration bug found during
development was corrected before retaining the final values.  No paid
service, external publication, or infinite-index claim is involved.
