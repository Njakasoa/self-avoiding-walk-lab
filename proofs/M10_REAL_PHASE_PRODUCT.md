# M10 candidate: bare-product phase decrease on the full working prefix

Status: conditional on the real scalar certificate M10_BETA_REAL. This
is a componentwise derivative result, not a derivative theorem for F_N.

For N>=32, theta in[.8,.9], put a=N+theta, beta=eta_e and b=a-beta.
The new real third-derivative certificate gives

    .70<beta<.72, beta_theta<0.

Let T_n=product_(j<n)(a-j)/(b-j). All factors are positive because a
and b lie in the same integer strip. The exact derivative is

    partial_theta logT_n=-beta S_n+beta_theta H_n,
    S_n=sum_(j<n)1/[(a-j)(b-j)]>0,
    H_n=sum_(j<n)1/(b-j).                             (1)

These identities are derived in M10_BARE_PHASE_DERIVATIVE. Here we
control the sign of the correction, rather than just its absolute value.

## A positive harmonic difference up to n=60N

For n<=N+1 every term of H_n is positive. For N+1<=n<=60N, set
v=theta-beta in(.08,.20), M=n-N-1<=59N-1. Then

    H_n=1/v+sum_(k=1)^N 1/(k+v)-sum_(k=1)^M 1/(k-v).

If M<=N, pair the first M terms and drop the remaining positive terms.
If M>N, pair the first N terms. In either case the paired loss is bounded by

    sum_(k>=1) 2v/(k^2-v^2)
       < (5/12) sum_(k>=1)1/k^2 <25/36.             (2)

The first inequality uses v<1/5 and k^2-v^2>(24/25)k^2. For the second,
the elementary bound

    sum_(k>=1)1/k^2 < sum_(k=1)^5 1/k^2 + integral_5^infinity x^-2 dx
                    <5/3

avoids any evaluation of the zeta function.

When M>N, the remaining decreasing harmonic tail satisfies

    sum_(k=N+1)^M1/(k-v)
       <=integral_N^M dx/(x-v)
       =log[(M-v)/(N-v)]<log60<21/5.                 (3)

Indeed M<=59N-1 and N+1>59v for N>=32 imply the ratio is below60.
Also log60<log64=6log2<21/5: the first five terms of exp(7/10)
already exceed2. If M<=N the tail is absent, so the same positive
allowance remains safe. Equations(2)--(3) yield

    H_n>5-25/36-21/5=19/180>1/10,
                         N+1<=n<=60N.              (4)

## Uniform negative margin after the crossing

Since beta_theta<0, the correction in(1) is negative throughout
1<=n<=60N. For n>=N+1, the j=N and j=N-1 terms alone give

    S_n>=1/(.9*.20)+1/(1.9*1.2)=1025/171.

Consequently

    partial_theta logT_n < -1435/342 < -419/100,
                         N+1<=n<=60N, N>=32.        (5)

Before the crossing, equation(1) also proves strict decrease for n>=1,
without asserting the same fixed negative margin.

For fixed N and n tending to infinity, H_n eventually becomes negative
and behaves like -log n. Therefore this proof is intentionally restricted
to the working prefix n<=60N. Beyond it, the correction must be bounded
inside the exponentially damped tail. The other factors in the exact W
moments and their boundary terms also vary with theta; neither(4) nor(5)
proves monotonicity of the complete denominator.
