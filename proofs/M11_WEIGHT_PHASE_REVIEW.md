# Independent review of the regularized weight phase bound

Verdict: PASS. For N>=32 and every n>=0 the proof establishes
partial_theta log[A0 L(u_n)]<11/N. Combining with the reviewed bare-product
sign gives a margin below -3.85 for N+1<=n<=60N before the smooth factor
K_n is included. It does not establish a derivative sign for full F_N.

The physical kernel equation implies
 t(1+q^2)-q=-qt(1-t-t^2)
exactly, giving the stated cancellation in A0=Q*(-z0). Its denominator
is positive on the real t box. J(t)=t(1-t^2)/(1-t-t^2) increases because
its numerator increases and its positive denominator decreases;
its logarithmic derivative is below 7 by the endpoint allowance.
Thus partial_e log A0>-e+1/(2e)>0 and e_theta<0 makes its phase
contribution favorable. The exponential inequality used here holds
throughout e<=1/180.

Direct quotient differentiation gives the stated C_e and h_e formulas.
The lower q box and |t_e|<e/7 prove C_e<0; the t lower bound proves h_e>0.
Hence C_theta>0 and h_theta<0. For independent variables t,h,C,u,delta,
partial_C log L=-1/C. The stated partial_h log V1 is positive: its first
two terms have nonnegative sum for u<=1, and its last term is positive.
Also R_h=1/(1-th)^2-u/(1-tuh)^2>=0 because 1-tuh>=1-th and u<=1.
Since the weight gap is positive, partial_h L>0. Dropping these h,C
contributions in an upper bound is therefore legitimate.

For the kernel, B(t,1)=2cosh(e/2) and 1-t^2>3/4 yield
B-2>=e^2/4+(1-t^2)(1-v) and then
sqrt(B^2-4)>=sqrt(e^2+3(1-v)). The derivative formulas for U follow
from U+1/U=B and have the displayed positive signs. The t contribution
is bounded by 6e/(7N), while x*exp(-x)<=1-exp(-x) bounds the v
contribution by 1/(sqrt(3)N)<.6/N. At n=0 that second contribution is
zero and the positive e gap controls the first. This is uniform in all
n, with no differentiation of the critical endpoint or hidden compact
cutoff. The resulting coefficient is 127/210<.61.

The upper bounds for R, R_t and partial_t log V1 follow by positive
numerator maxima and denominator minima. The negative term
-uh/(1-tuh) in the last logarithmic derivative can safely be discarded.
The derivative of the gap with respect to t is positive, so division
by its .07 lower bound is valid. Independent exact replay gives the
partial-t upper allowance
15211672183172127027700/119638135041968778487<200.
Combining with t_theta<e^2/(7N) makes its contribution less than .001/N.
The already reviewed directed contribution is nonnegative and below
1.12/N. The full chain rule therefore gives
(.001+16*.61+1.12)/N=10.881/N<11/N after dropping only the three
established favorable terms A0,h,C.

The factorization -Q*z_n*L=A0*T_n*K_n*L has the correct signs. The beta
strip places numerator and denominator zeros in the same integer strip,
so T_n>0. The real secant positivity proof extends to this domain because
s_h=s_g-beta*e>.15-.72/180>0 and the physical g is increasing/concave;
it requires no small-e Taylor remainder. Hence the logarithms used are
well-defined. The post-crossing margin is
1435/342-11/32=21079/5472>3.85. The unestimated smooth factor,
pre-crossing sum, boundary terms and distant tail remain separate
obligations exactly as stated in the note.

All 13 Fraction checks passed in an independent replay. Separate symbolic
checks verified R_h, partial_h log V1, and the A0 kernel cancellation.
The sorted JSON output SHA-256 is
5c480862089b150f1acecb11586937740dc9a2522c0ac4cb2f2d0b03ff4d1125.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M11_WEIGHT_PHASE_BOUND.md | e6fa7bbec97ed9caeb3785850728aeef64b20af610f70d3234a5e38398f06ca6 |
| proofs/m11_weight_phase_bounds.py | 9270136d7b6f1c3f0fa1eb7f9c81548feeceed57e328087e9d766441c132b725 |

No scientific source was edited. This componentwise approval makes no
novelty or full-index-coverage claim.
