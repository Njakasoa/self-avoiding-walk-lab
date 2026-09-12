# M9 candidate: one simple W pole in each band for N>=10^27

Status: conditional on independent acceptance of M9_LINEAR_MOMENT_RATE,
M9_COMPLEX_KERNEL_LINEAR and this transfer. This is still an inaccessible
threshold, and does not close the finite-to-asymptotic coverage gap.

Let theta range over T=[.8,.9]. The new linear moment estimate gives

    E_N=|P_N-P0|+|H_N-H0|<10^21/N<=10^-6, N>=10^27.   (1)

The common domains e<1/N<=10^-27<=10^-10 are satisfied. The new complex
domain supplies holomorphy and the joint norm below10^8 on Omega for
N>=10^15; the critical norm is below100. Therefore the M8 Chebyshev
interpolation inequality applies to the moment errors with M=10^8+100,
q=15/22, and E=10^-6. Choose m=97, k=m+1, and set

    A_m=2M q^k/(1-q),
    B_m=40M q^k[k^2/(1-q)+2kq/(1-q)^2+q(1+q)/(1-q)^3].

Exact rational arithmetic gives

    E1_N:=sup_T(|P_N'-P0'|+|H_N'-H0'|)
       <=20m^2(E+A_m)+B_m <201/1000.                 (2)

Primes in this note denote phase derivatives.

## Directed term and existence at the new threshold

The M6 directed theorem gives D=log(1/e)/sigma+c_D+R, c_D>3/4 and
|R|<=100e log(1/e). Since e log(1/e) increases up to exp(-1), its
maximum here is at most2700log(10)/10^27<8100/10^27<3/4.
Thus D>log(1/e)/sigma and, using log(10)>2 and sigma<.42,

    0<delta=1/(1+D)<sigma/log(N)<.42/54<1/125.        (3)

The simple logarithm bounds follow from exp(2)<10<exp(3).
For exp(2), sum through n=3 and bound the tail starting at n=4 by
(2^4/4!)/(1-2/5); for exp(3), the first four terms already exceed10.

The frozen M5/M6 critical certificates give on T

    -7.5<1+P0<-3.6,
    F0(.8)>1, F0(.9)<-1/5,
    0<P0'<75, F0'<-6.

Equation(1) implies -8<1+P_N<-3.5. The exact M6 denominator comparison,
with its constants re-evaluated here instead of importing its10^46 domain,
is

    |F_N-F0| <=4E_N+2e^2+16delta
       <4*10^-6+2*10^-54+16/125 <3/20.               (4)

Hence F_N(.8)>17/20 and F_N(.9)<-1/20. There is a zero in each band.
The M6 source-pole exclusion uses a=N+theta, b=a-eta_e and
eta_e in[.70,.72], which also hold on this smaller e domain. The physical
kernel denominators and normally convergent tail give local holomorphy.
The numerator never vanishes by the displayed uniform bound.

## Uniqueness and simplicity

Use the exact differentiated identity of M7_UNIQUENESS_TRANSFER, rather
than that theorem's old threshold. The bounds |delta'|<=30000/N,
|t_N'|<e^2 and |t-sigma|<=e^2/8 hold on this domain. Since
0<1-t+2delta<.6+2/125<1, the same algebra gives

    F_N' <-6+4E1_N+150delta+18e^2+480000/N
          <-6+4*(201/1000)+150/125
                     +18*10^-54+480000*10^-27
          <-39/10.                                  (5)

Thus the zero in every Nth band, N>=10^27, is unique and simple in phase.
The phase-to-t derivative is positive and nonzero, so it is simple in t.
Together with the uniform negative numerator it is a noncancelled W pole.
This statement covers every integer beyond the stated threshold; it does
not cover any unlisted indices below it or exclude poles outside T.
