# M7: an effective derivative criterion for one simple W pole per band

Status: candidate for independent review. A finite derivative threshold
is still an input to be proved, not supplied by this criterion.

On T=[4/5,9/10], suppose N>=10^46 and

 E1(N):=sup_T (|P_N'-P0'|+|H_N'-H0'|)<=1.             (U)

Then the entire Nth band has exactly one W pole and it is simple.
Primes here are derivatives in the real phase theta.

## Exact critical margins

With the frozen M5 critical integrals and notation,

 B'=A*pi*sin(pi*eta)/sin²(pi*(theta-eta)),
 P0'=post1*B',  F0'=J*B',
 J=(1-sigma)*post1-4sigma²*post2<0.

Since0<theta-eta<1/2 on T, sine is positive and increasing in theta,
so B' is positive and decreasing. The endpoint interval computations
in m7_uniqueness_transfer.py imply throughout T

                     0<P0'<75,  F0'<-6.               (1)

No derivative is estimated by differentiating a numerical enclosure.
The analytic monotonicity supplies the full-sector inference.

## Exact finite derivative identity

Put delta=1-D_I, e=e_N(theta), and p_N=1+P_N. The accepted M6 theorem
gives, uniformly on T for N>=10^46,

 |P_N-P0|+|H_N-H0|<1/50,
 -8<p_N<-3.5,  0<delta<1/250, e<1/N.                 (2)

The accepted M5 directed derivative bound is |delta'|<=30000/N.
Moreover |t_e|<1/20 and |e_N'|<=20e² give

                   |t_N'|<e².                        (3)

The physical branch has t>.4 and |t-sigma|<=e²/8. Differentiate only
the exact analytic denominator identity

 F_N=(1-t)P_N-4H_N-(3+t)+2delta(1+P_N).

Subtracting F0' yields

 F_N'-F0'=(1-t+2delta)(P_N'-P0')-4(H_N'-H0')
          +(sigma-t+2delta)P0'-t_N'p_N+2delta'p_N.    (4)

Since0<1-t+2delta<1, (1)--(3) imply

 |F_N'-F0'|
 <=4E1+150delta+18e²+480000/N.                       (5)

Indeed the parameter difference costs75e²/8, the t derivative costs
8e², and their sum is less than18e². The directed derivative costs
16*30000/N. Thus (U), N>=10^46 and (2) give

 F_N'<-6+4+150/250+18*10^-92+480000*10^-46<-1.        (6)

M6 provides opposite endpoint signs and a nonzero numerator throughout
the band. Equation (6) makes F_N strictly decreasing, hence its zero
unique. Its phase derivative is nonzero. The phase-to-t map has strictly
positive nonzero derivative on this physical domain (both t_e and e_N'
are negative), so the zero is simple in t as well. The numerator does
not vanish there, proving a unique simple meromorphic pole of W.

If an independently proved bound (U) holds for all N>=N_der, this
criterion supplies the effective uniqueness threshold

                    N_unique=max(10^46,N_der).

Without that derivative bound, the statement remains conditional.
Real C0 moment convergence alone is not differentiated or treated as
evidence for (U).
