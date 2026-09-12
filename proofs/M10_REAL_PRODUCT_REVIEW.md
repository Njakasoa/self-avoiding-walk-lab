# Independent review of the real bare-product phase sign

Verdict: PASS as a conditional analytic implication. Assuming the forthcoming
real scalar certificate supplies .70<beta<.72 and beta_theta<0 for every
N>=32, theta in [.8,.9], M10_REAL_PHASE_PRODUCT.md proves strict decrease
of T_n for 1<=n<=60N, with
partial_theta log T_n<-1435/342<-419/100 for N+1<=n<=60N.
The scalar certificate itself was not present at this review and is not
approved by this conditional verdict. No full F_N derivative sign follows.

The new proof needs only the exact finite-product derivative identity from
M10_BARE_PHASE_DERIVATIVE.md, not that note's large-N scalar or Cauchy
bounds. The identity can also be checked directly: a_theta=1 and
b_theta=1-beta_theta give
1/(a-j)-(1-beta_theta)/(b-j)
=-beta/[(a-j)(b-j)]+beta_theta/(b-j).
All paired denominators have positive product because a,b lie in the same
integer strip. Thus S_n>0 for n>=1, while the sign of H_n requires the
new argument. The empty product n=0 has derivative zero and is correctly
excluded from strict decrease.

Put v=theta-beta in (.08,.20) and M=n-N-1. For n>=N+1, splitting terms
about j=N yields exactly
H_n=1/v+sum_(k=1)^N 1/(k+v)-sum_(k=1)^M 1/(k-v).
Pairing common indices produces a loss 2v/(k^2-v^2). Since v<1/5,
this is less than (5/12)/k^2. The decreasing-integral tail gives
sum_(k>=1)1/k^2<5989/3600<5/3, hence total paired loss <25/36.
This remains a valid bound when M<N; the unpaired positive terms can
be discarded.

For M>N, decreasing-integral comparison gives the negative tail at most
log((M-v)/(N-v)). The restriction n<=60N yields M<=59N-1, and
N+1>59v proves the ratio is below 60. The five-term exponential lower
sum at .7 is 482921/240000>2, implying log 2<.7 and
log 60<log 64=6 log 2<21/5. If M<=N the tail is absent and the same
positive allowance is safe. Combining 1/v>5 with these bounds gives
H_n>5-25/36-21/5=19/180>1/10. Before n=N+1 all H_n terms are positive.

Consequently beta_theta*H_n is negative throughout 1<=n<=60N under
the explicit scalar sign hypothesis. For n>=N+1, the j=N and j=N-1
terms give S_n>=1/(.9*.20)+1/(1.9*1.2)=1025/171. Multiplication by
beta>.7 yields beta*S_n>1435/342. The stated negative logarithmic
phase-derivative margin follows. All constants were independently replayed
with exact Fraction arithmetic.

The restriction n<=60N is material. For fixed N, H_n eventually tends
to negative infinity logarithmically, so the sign of the correction reverses
when beta_theta<0. The note correctly reserves the distant tail for a
separate damped argument. The other moment factors and boundary terms
also vary with phase; neither this result nor the combined-weight sign
proves monotonicity of the complete W denominator.

Reviewed SHA-256 values:

| Source | SHA-256 |
|---|---|
| proofs/M10_REAL_PHASE_PRODUCT.md | 9cb89838da02d8cb4f03d40b8571716cc237cf121881f772555d68d5a161cfa8 |
| proofs/M10_BARE_PHASE_DERIVATIVE.md | 04605690a985a1c65a682354eab86c08480c17c46be39f243c86a020a094a265 |

The exact-identity source's separate large-N theorem is not an input to
this new conditional sign proof. No scientific file was edited and no
finite scan or novelty claim was used.
