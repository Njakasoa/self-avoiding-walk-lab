# M8 candidate: the first logarithmic correction to the W residue

Status: **candidate for independent review**.  This note derives the next
residue coefficient from the accepted M5 \(C^1\) moment convergence and the
accepted directed phase derivative estimate.  It does not differentiate a
real \(C^0\) remainder.  The asymptotic \(O\)-constant is non-effective
because the accepted M5 moment rate has a non-effective constant.  An
effective sign and size bound at \(N\ge 10^{120}\), using the accepted M7
complex derivative transfer, is recorded separately in Section 7.

All statements concern the same restricted weakly prudent bridge series and
the normalization

\[
 W(t)=-1-\frac{1+P(t)}{F(t)},
 \qquad
 F=(1-t)P-4H-(3+t)+2(1-D_I)(1+P).
\tag{M8.1}
\]

No statement concerns unrestricted square-lattice self-avoiding walks, and
no priority or novelty claim is made.

## 1. Accepted inputs and notation

Put
\[
 \sigma=\sqrt2-1,\quad \eta=2^{-1/2},\quad L=\log N,
 \quad p(\theta)=1+P_0(\theta),\quad f(\theta)=F_0'(\theta).
\]
Let \(\theta_*\) be the accepted unique critical root in
\([.8,.9]\), and abbreviate
\[
 p_*=p(\theta_*),\qquad f_*=f(\theta_*),\qquad
 p_*'=P_0'(\theta_*),\qquad f_*''=F_0''(\theta_*).
\]
The accepted critical certificate gives (p_*<0), (f_*<0), and
\[
 c_1:=\frac{2\sigma p_*}{f_*}>0,
 \qquad
 r_0:=-\frac{p_*s_*^2}{8f_*}<0.
\tag{M8.2}
\]

The M5 moment theorem, including its holomorphic route to the first phase
derivatives, supplies on the real phase interval
\[
 P_N-P_0=O(N^{-1/20}),\quad H_N-H_0=O(N^{-1/20}),
\]
\[
 P_N'-P_0'=O(N^{-1/20}),\quad H_N'-H_0'=O(N^{-1/20}).
\tag{M8.3}
\]
The constants are uniform in the phase interval.  Since
\(N^{-1/20}=o(L^{-2})\), these errors are \(o(L^{-2})\) in the
calculation below.  The accepted directed logarithmic theorem and its
phase derivative estimate give
\[
 \delta_N:=1-D_I(t_N)=\frac{\sigma}{L}+O(L^{-2}),
 \qquad \delta_N'=O(N^{-1}).
\tag{M8.4}
\]
The second estimate is the reviewed (30000/N) bound after composition
with the phase inverse; it is not obtained by differentiating the first
estimate.

The accepted phase transfer gives
\[
 \theta_N=\theta_*-\frac{c_1}{L}+O(L^{-2}),
 \tag{M8.5}
\]
and the phase Jacobian estimate gives
\[
 t_N'(\theta_N)=\frac{s_*^2}{8N^3}+O(N^{-4}).
\tag{M8.6}
\]
The pole is (w_N=t_N(\theta_N)), with the eventual uniqueness and
simplicity scope inherited from M5/M7.

## 2. The exact residue transfer

At a simple zero of \(F_N(\theta)=F(t_N(\theta))\), the exact quotient
identity (M8.1) gives
\[
 \operatorname {Res}_{t=w_N}W
 =-\frac{p_N(\theta_N)t_N'(\theta_N)}{F_N'(\theta_N)},
 \qquad p_N=1+P_N.
\tag{M8.7}
\]
This fixes the sign and the Jacobian: \(W=-1-p_N/F_N\), and
\(F_N(t_N(\theta))=F_N(\theta)\), so the denominator derivative in
the \(t\)-coordinate is \(F_N'/t_N'\).

Differentiate only the exact identity (M8.1).  It yields
\[
 F_N'=(1-t_N+2\delta_N)P_N'-4H_N'-t_N'p_N+2\delta_N'p_N.
\tag{M8.8}
\]
Using (M8.3)--(M8.4), \(t_N-\sigma=O(N^{-2})\), and
\(t_N'=O(N^{-3})\), this becomes uniformly
\[
 F_N'(\theta)=F_0'(\theta)+\frac{2\sigma}{L}P_0'(\theta)
                  +O(L^{-2}).
\tag{M8.9}
\]
The \(2\delta_N'p_N\) term is \(O(N^{-1})=o(L^{-2})\).  This is the
point where the directed derivative estimate is needed; no derivative of a
directed \(O(L^{-2})\) remainder is used.

Similarly, (M8.3) gives
\[
 p_N(\theta)=p(\theta)+O(L^{-2})
\tag{M8.10}
\]
at the precision relevant here.  Expanding (M8.10) and (M8.9) at the root
using (M8.5) gives
\[
 p_N(\theta_N)=p_*-\frac{c_1p_*'}{L}+O(L^{-2}),
\tag{M8.11}
\]
\[
 F_N'(\theta_N)=f_*+
 \frac{-c_1f_*''+2\sigma p_*'}{L}+O(L^{-2}).
\tag{M8.12}
\]
The Jacobian error in (M8.6) is \(O(N^{-1})\) relative to its leading
term, hence is absorbed into \(O(L^{-2})\) after multiplication by
\(N^3\).  Substitution in (M8.7) proves the expansion
\[
 \boxed{
 N^3\operatorname {Res}_{t=w_N}W
 =r_0+\frac{r_1}{L}+O(L^{-2})
 }
\tag{M8.13}
\]
with the exact coefficient
\[
 r_1=r_0\left[
 c_1\left(\frac{f_*''}{f_*}-\frac{p_*'}{p_*}\right)
 -2\sigma\frac{p_*'}{f_*}\right].
\tag{M8.14}
\]
Because (c_1=2\sigma p_*/f_*), this has the shorter equivalent form
\[
 \boxed{
 r_1=r_0\left(c_1\frac{f_*''}{f_*}
                   -4\sigma\frac{p_*'}{f_*}\right).
 }
\tag{M8.15}
\]

The directed additive constant (b) and the M6 second phase coefficient
enter only at order (L^{-2}).  Thus (M8.14) is determined by the first
phase displacement and the first derivative correction alone.

## 3. Affine critical profile form and signs

The accepted critical profile is affine in
\[
 B(\theta)=\frac{A\sin(\pi\theta)}{\sin(\pi(\eta-\theta))},
 \qquad
 F_0=C_0+JB,\qquad p=p_0+\mathrm{post}_1B,
\]
where
\[
 J=(1-\sigma)\mathrm{post}_1-4\sigma^2\mathrm{post}_2<0.
\]
Therefore
\[
 \frac{p_*'}{f_*}=\frac{\mathrm{post}_1}{J},
 \qquad
 \frac{f_*''}{f_*}=\frac{B''(\theta_*)}{B'(\theta_*)}
 =2\pi\cot\!\bigl(\pi(\eta-\theta_*)\bigr).
\tag{M8.16}
\]
The exact arithmetic form used by the new checker is consequently
\[
 \boxed{
 r_1=r_0\left[
 2\pi c_1\cot\!\bigl(\pi(\eta-\theta_*)\bigr)
 -4\sigma\frac{\mathrm{post}_1}{J}
 \right].
 }
\tag{M8.17}
\]
For the interval evaluation, subtracting the two large terms in (M8.17)
loses useful correlation.  Set
\[
 \alpha=\pi\eta,\qquad
 Q(B)=B^2+2A\cos(\alpha)B+A^2,\qquad
 \kappa_B=\frac{\pi}{A\sin(\alpha)},\qquad
 p_0=\sigma-A\,\mathrm{pre}_1.
\]
Then \(B'=\kappa_BQ(B)\), and the exact combined form is
\[
 \frac{r_1}{r_0}
 =\frac{4\sigma}{J}\,
 \frac{(p_0-\mathrm{post}_1A\cos\alpha)B
       +p_0A\cos\alpha-\mathrm{post}_1A^2}
      {Q(B)}.
\tag{M8.18}
\]
The new checker evaluates (M8.18) directly.  This retains the certified
sign \(r_1<0\) at the current interval resolution; it is an arithmetic
correlation improvement, not a finite-\(N\) fit.

## 4. Exact arithmetic receipt for the coefficients

`proofs/m8_residue_coefficients.py` reads only the frozen
`results/m5-critical-v1/payload.json`, uses the existing 384-bit dyadic
interval engine, and records source precision and output intervals.  The
replay command is

```text
.venv/bin/python -m proofs.m8_residue_coefficients
```

The current outward enclosures are
\[
\begin{array}{c|c}
\text{coefficient}&\text{outward interval}\\ \hline
c_1&[0.38696091937,\;0.441662608427]\\
r_0&[-0.001670963732,\;-0.001464008157]\\
r_1&[-0.000754845272,\;-0.000431005922].
\end{array}
\tag{M8.19}
\]
These are exact limit-coefficient enclosures, not finite-\(N\) fits.  The
interval for \(r_1\) uses the combined exact form (M8.18).

## 5. Remainder ledger and scientific scope

The \(O(L^{-2})\) remainder in (M8.13) has the following sources:

1. the \(O(L^{-2})\) phase displacement from (M8.5), including the Taylor
   remainders of \(p\) and \(F_0'\);
2. the \(O(L^{-2})\) difference between \(\delta_N\) and \(\sigma/L\);
3. the \(O(N^{-1/20})=o(L^{-2})\) \(C^1\) moment errors;
4. the \(O(N^{-1})\) directed phase derivative error and the
   \(O(N^{-3})\) Jacobian terms.

All four estimates are uniform on the fixed phase band once the eventual
root is in that band.  The first two are the accepted M5 transfer inputs;
the third is the accepted holomorphic M5 moment theorem; the fourth uses
the reviewed directed derivative bound and the exact inverse phase map.
No finite-index conclusion follows from this non-effective asymptotic
remainder.  In particular, (M8.13) does not turn the interval for \(r_1\)
into a finite-(N) numerical error bar.

## 6. Sign and scaling audit

The signs in the residue formula are fixed as follows:

\[
 p_*<0,\qquad f_*<0,\qquad t_N'>0,
\]
so (M8.7) gives \(r_0<0\).  The phase displacement is
\(\theta_N-\theta_*=-c_1/L+O(L^{-2})\), hence its numerator contribution
is \(-c_1p_*'/L\).  The explicit \(2\delta_N P_N'\) term contributes
\(+2\sigma p_*'/L\) to the denominator derivative.  These two terms are
the reason the simplified bracket in (M8.15) contains
\(-4\sigma p_*'/f_*\), rather than a sign-free fitted constant.

The factor (s_*^2/8) is the phase-to-(t) Jacobian coefficient:
\[
 e_\theta=\frac{e^2}{e s_g'(e)-s_g(e)},\qquad
 t_e=-\frac e8+O(e^3),\qquad e=\frac{s_*}{N}+O(N^{-2}).
\]
Thus \(t_N'=s_*^2/(8N^3)+O(N^{-4})\), and the residue scale is \(N^{-3}\).

## 7. Effective nonzero residue bounds for \(N\ge10^{120}\)

The accepted M7 effective derivative transfer gives, on the unique pole's
phase band for \(N\ge10^{120}\),
\[
 -8<p_N<-\frac72,\qquad F_N'<-1,\qquad
 |P_N'-P_0'|+|H_N'-H_0'|<0.009.
\tag{M8.20}
\]
The exact M5 phase box gives, for the real phase inverse,
\[
 0.1533<s_g<0.167,\qquad 0.33<s_g'<0.37,
\]
and \(e=s_g(e)/(N+\theta)\).  Hence, for this threshold,
\[
 \frac{0.149}{N}<e<\frac{0.17}{N},\qquad
 0.14<s_g(e)-e s_g'(e)<0.17.
\tag{M8.21}
\]
For the kernel equation
\[
 \left(\frac1t-1+t+t^2\right)_t t_e=\sinh(e/2),
\]
the physical branch has \(0.4<t<\sigma\), so
\(4<|F'(t)|<4.5\).  The elementary series bounds
\(e/2<\sinh(e/2)<0.51e\) then give
\[
 \frac e{10}<|t_e|<\frac e7,\qquad
 \frac{e^3}{1.7}<t_N'=|t_e|\frac{e^2}{s_g-e s_g'}<1.1\,e^3.
\tag{M8.22}
\]
The accepted derivative identity and the M7 bound in (M8.20) give
\[
 |F_N'-F_0'|
 \le 4(0.009)+150/250+18(0.17)^2\,10^{-240}
       +480000\,10^{-120}<0.64.
\]
The exact M5 critical enclosure has \(|F_0'|<33\) throughout the band,
so \(|F_N'|<34\).  Combining these inequalities with (M8.7) yields the
fully explicit, noncancelled residue bound
\[
 \boxed{
 -\frac1{20N^3}<\operatorname {Res}_{t=w_N}W
                    <-\frac1{6000N^3},\qquad N\ge10^{120}.
 }
 \tag{M8.23}
\]
The constants are intentionally coarse.  This is an effective sign/size
statement based on the already accepted M7 threshold; it does not claim
that \(10^{120}\) is minimal and it does not make the asymptotic \(r_1\)
interval effective at finite \(N\).

## 8. Required review and provenance

An independent review should check (M8.8)--(M8.18), the \(N^{-3}\) Jacobian
scaling, and the elementary arithmetic in (M8.21)--(M8.23).  The new
arithmetic source is
`proofs/m8_residue_coefficients.py`; its only scientific input is the
accepted frozen M5 critical payload.  Frozen M3--M7 files were not edited.
Any later improvement of the \(r_1\) enclosure must preserve the current
interval classification and record its source and output hashes.
