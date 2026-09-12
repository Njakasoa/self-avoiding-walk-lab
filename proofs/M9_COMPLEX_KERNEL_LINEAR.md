# M9 candidate: linear complex-kernel comparison on the compact ray

Status: candidate for independent review. The M7 square-root sector
already proves more than the coarse square-root modulus comparison used
there. Retaining the scale in its discriminant bound gives an O(e0)
comparison and may improve subsequent effective domains.

Assume0<e0<=10^-8 and abs(e-e0)<=e0², exactly as in the frozen
M7_COMPLEX_KERNEL_SECTOR lemma. For s=ne=x+iy,0<=x<=4, write
v=exp(-s), v0=exp(-x), Delta=Delta(t(e),v), Delta*=Delta(sigma,v0).
The accepted bounds give

    abs(t(e)-sigma)<e0²/5, abs(v-v0)<=2e0*x,
    Re Delta>.004(e0²+x), Delta*>=0.

The polynomial derivative bound160 therefore yields

    abs(Delta-Delta*)<=160(e0²/5+2e0*x)
                     <=320e0(e0+x).                   (1)

Both square roots are principal, with positive real part for Delta
and nonnegative real value for Delta*. Hence

    abs(sqrt(Delta)+sqrt(Delta*))>=abs(sqrt(Delta))
                               >.06sqrt(e0²+x).

Factor the difference of squares. Since
(e0+x)/sqrt(e0²+x)<=1+sqrt(x)<=3, equation(1) gives

    abs(sqrt(Delta)-sqrt(Delta*))<16000e0.              (2)

The compact kernel denominators remain above.8 and the corresponding
a difference is below130e0, as already shown in M7. Subtracting the two
quotients2t/(a+sqrt(Delta)) now yields

          abs(U(t(e),exp(-s))-U(sigma,exp(-x)))<25000e0. (3)

For example2(e0²/5)/.8+.83*(16130e0)/.8²<25000e0.
This includes x=0; its square-root denominator has order e0 there and
its discriminant numerator has order e0². No uniform endpoint derivative
is being assumed.

## Consequence for the smooth-product domain

For the phase inverse from M8, abs(e)<2e0, abs(D-(1-sigma))<2e0,
abs(Ucrit)<=1 and1-sigma<.6. Equation(3) gives

                   abs(g_e(s)-g0(x))<16000e0.

For N>=10^15, e0<1/N. The exterior denominator margins .049 and .0009
remain valid. The M8 exterior root fraction costs at most5*10^8 e0;
the g fraction now costs at most

    [200/.0009+.3*16000/(.0009*.001)]e0<6*10^9 e0.

For the logarithm remainder, abs(eta_e)<1 and abs(delta/e)<.301 bound
the two fractions before multiplication by e by21 and335. Since abs(e)<2e0,
the quadratic logarithm remainders divided by e cost less than
4*(21^2+335^2)e0=450664e0<5*10^6 e0. The crossing estimate
is still2*10^12 e0. Thus a common bound is

                 abs(ell_e(s)/e-psi(Re s))<10^13 e0.

The same fewer-than5/e0 prefix count and psi<=0 then give

            Re sum_(j<n) ell_e(je)<10^14 e0<.1<1/2.

This preserves abs(Pi_n)<2 for every prefix with j*Re(e)<4, already
for N>=10^15. The remaining M8 scalar/kernel/domain inequalities hold
at e0<=10^-15: the exterior g loss is below1.6*10^-11, root displacement
below4.8*10^-14, eta perturbation below2*10^-8, and4*10^6 Re(e)<4*10^-9.
All are strictly inside the previously displayed margins. The fixed-point
construction requires only N>=10^6, and the kernel-sector lemma only
e0<=10^-8.

Consequently the same compact/tail/boundary ledger and normal convergence
argument yield the candidate extension

          sup_Omega(abs(P_N)+abs(H_N))<10^8, N>=10^15.

Here Omega is the M8_COMPLEX_DOMAIN rectangle
{theta: .78<Re(theta)<.92, abs(Im(theta))<.02}.

This is a domain improvement only. A useful uniqueness threshold still
requires a sufficiently small real moment error and derivative transfer;
no low-index coverage follows from this statement by itself.
