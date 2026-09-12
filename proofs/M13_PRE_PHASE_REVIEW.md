# Independent review of the M13 pre-crossing phase bound

Status: PASS for S_pre,theta<(2.06/N)S_pre, for integer N>=32 and theta in[.8,.9]. No pre-crossing nonincrease or complete F derivative sign follows from this component alone.

## Analytic audit

The logarithmic derivative of the finite bare recurrence is exactly -beta sum1/[(a-j)(b-j)]+beta_theta sum1/(b-j). Both denominators are positive for j<n<=N. It is strictly negative for n>=1 and zero for the empty product n=0. The rest of the argument retains strict bounds at n=0, where the kernel mesh-motion contribution is zero.

The inherited endpoint-safe kernel estimate gives the new .244/N allowance from ne<.17. Since ne<s_g, monotonicity of U in its second argument gives u_n>u_g>.70. The strengthened gap uses the correct lower endpoints: R increases in t,u,h, with R_h=1/(1-th)^2-u/(1-tuh)^2>=0. The numerator gap exceeds1/5, and the independent upper bound for R_u yields partial_u log L<6. The delta contribution uses the negative delta partial and negative delta_theta, giving a positive allowance below.4/N. The favorable h,C contributions can be discarded; the remaining t partial is bounded by the inherited .001/N.

For A0=J(t)(1-exp(-e)), J_t/J<7 and -t_e<e/7 imply (log A0)_e>1/e-1-e>0. The signed scalar input s_g'>.3 gives |e_theta|>e/(N+.6). The resulting N/(N+.6)(1-e-e^2) is bounded below at N=32 and e=17/3200, and exceeds.97. Multiplication by negative e_theta gives the claimed favorable contribution with the correct inequality direction.

The smooth-factor improvement replaces only the anchor-motion constant in the inherited exact factorization. Its variance bound remains valid for every mesh point. Summing the linear mesh term uses sum_(j<n)j=n(n-1)/2, giving the stated .002601/N allowance. Together with the geometric-r term, this yields the exact relative coefficient1731319941/841000000<2.06. Positivity of the finite summands permits multiplication and summation without a convergence issue.

## Arithmetic replay

Independently ran the final `.venv/bin/python -m proofs.m13_pre_phase_bounds`: all12 arithmetic checks PASS. Final stdout SHA256: `f88d00e91ee19e0dc1933430eafe28e193e90a2e3bee048c63a11014a0afbae0`. The preliminary producer had a tautological kernel-lower flag; the released producer removes it and explicitly identifies that inequality as an inherited analytic input. All rational allowances are unchanged. The physical lower bound is supplied by the reviewed M11 signed scalar enclosure and the analytic order argument above.

## Final source approval

Observed repository HEAD: `8f8176b8039c518455ea5a1ec284564f4f1ea108`; actual reviewed bytes are pinned below. The final note fixes mathematical markup; its inequalities are unchanged. No material findings remain.

| Path | SHA256 |
|---|---|
| proofs/M13_PRE_CROSSING_RESEARCH.md | e9aabeb8534e5b8c7a35319ec177fecc2d00e92a32ba7b73e39e8f2139776e5e |
| proofs/m13_pre_phase_bounds.py | 99e856af48d5f7fe78f17a0d246ab745aad1a24f3770aea179d844d2c16e164e |
