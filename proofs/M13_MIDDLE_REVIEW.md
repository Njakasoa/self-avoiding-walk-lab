# Independent review of the middle mass and phase decrease

Verdict: PASS for the middle component. Uniformly for N>=32 and theta in
[.8,.9], the proof establishes S_sub>1/70 and S_mid,theta<-3/56.
It does not control the rest of F_theta or prove zero existence/uniqueness.

The smooth-factor lower bound follows from the reviewed positive inverse
kernel factorization. For log(ug/h), the log inequality yields the loss
(h-ug)/ug<.51e/.70. For the second rational ratio it gives
u(h-ug)/(1-uh)<.51e/.29. The log M anchor derivative lies in [-1,0],
so its loss is at most sg-sh=beta e<.72e. Their sum is below 13e/4
on the entire ray. Integrating |(log r)_e|<2 from r(0)=1 gives r>exp(-2e).
Thus K_n>exp(-21ne/4). In the subwindow ne<.255, the exact Taylor
upper bound on exp(1071/800) is below 4, proving K_n>1/4.

The bare-product telescoping directions are correct. Concavity gives
1+beta*x>=(1+x)^beta, which lower-bounds each positive-side factor.
For post-crossing l>=2 it gives
1-beta/(l-v)>=(1-1/(l-v))^beta, with 1/(l-v)<1.
The latter product telescopes to ((1-v)/(k-v))^beta. The l=1 factor
must be separated and is handled correctly. The bounds theta/v>9/2 and
(1-theta)/(1-theta+beta)>5/41 follow from the stated monotonicity and
endpoints, with strictness supplied by the beta strip. For k>=1,
(N+1+v)/(k-v)>2 and (1-v)/(1+v)>2/3; for k=0 the post product is
empty and theta/v alone suffices. The rational power check therefore
gives T_n>27/41 throughout the subwindow.

The positive increasing J(t) gives A0/e>J(.414)*(359/360)>.82.
Since exp(-ne)>1-ne>.745 and the physical kernel increases in t and v,
the exact U(.414,.745) interval yields u_n>.63. V1 and R increase in
t,h,u on the stated positive domain; V1 decreases in C. For V1's
partial t derivative, the difference u/(1-tu)-uh/(1-tuh) is positive
because h<1, and h/(1-th)>0. Thus the independent endpoint substitutions
used for R_l and V_l are valid. Their resulting gap is positive, and
L_W>V_l*gap>1.5, independently replayed as approximately 1.52518494687.

There are exactly floor(3N/2)-N=floor(N/2) terms. Since
floor(N/2)>=N/2-1/2>=31N/64 for N>=32, the count allowance is valid
for odd and even N. Also Ne>.15N/(N+.9)>=48/329. Multiplying the
per-term bounds gives exactly 7533/526400>1/70; the factor N from
the term count and e from A0 combine as Ne, with no missing scaling.

The refined M11 per-factor derivative 7.071+.18je is available before
its larger working-prefix bound is substituted. On this subwindow it
is below 7.12. The product, geometric ratio and weight phase allowances
therefore sum to less than 13.4/N. Combined with the bare logarithmic
margin, this is below -15/4 for N>=32. Every remaining term in the
finite middle sum has a negative derivative by the accepted M11 result.
The index boundaries are fixed with respect to theta. Dropping those
other negative terms yields S_mid,theta<-(15/4)S_sub<-3/56 exactly.

The independent producer replay passed all 13 checks. Its exponential
majorant uses terms through degree 12 and bounds the remaining positive
tail by its first term divided by 1-x/14, a valid decreasing-ratio bound.
It is approximately 3.81427268338<4. The kernel I384 evaluation and all
other rational expressions agree with the analytic argument.

Sorted JSON output SHA-256:
daa791dc638870acb58b5dcf5336809dd53af1c9fa821b9736d21094fc9cdf6c.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M13_MIDDLE_MASS.md | 9865db56835727781f833744741307f8687ae9e2bcf64c70879bd3360799de2f |
| proofs/m13_middle_bounds.py | 2cb9be5f9bceaa74e86768a0f180a6e93581c9970abafcbb97332edf5e69b6b3 |

No accepted source was edited. The pre-crossing, boundary and distant-tail
contributions must still be combined before any full F phase claim.
