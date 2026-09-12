# M6: reducing the sufficient W existence index to 10^46

Status: candidate, conditional on acceptance of M6_SHARP_KERNEL.md and
the aggregation below. Existence and noncancellation only; the eventual
uniqueness and simplicity theorem remains non-effective.

Use the accepted real moment estimate (T) in M6_REAL_MOMENT_RATE.md,
with the sharp kernel constant B=10^12. On theta in T=[.8,.9], the
phase certificate gives 0<e=e_N(theta)<1/N. For

                         N >= N0 = 10^46,

all component domains hold, including e<10^-10 for the M5 weight lemma.
Every term on the right side of (T) increases with e, so

 E := |P_N-P0|+|H_N-H0|
 < 1/(100 sqrt(10)) + 1/100 + 10^-32 < 1/50.          (1)

This uses e^(1/4) at 10^-46 exactly, not a rounded floating power.

## Directed correction

The new directed theorem gives

 D = log(1/e)/sigma+c_D+R,
 c_D>3/4, |R|<=100e log(1/e).

Since e log(1/e) increases for e<exp(-1), the last error at our
domain endpoint is at most 4600 log(10) 10^-46 < 10^-41.
Thus D>log(1/e)/sigma>log(N)/sigma and

 0<delta_N=1/(1+D)<sigma/log(N)
 <=sigma/(46log(10))<1/250.                           (2)

The exact coefficient certificate supplies c_D>3/4. The accompanying
threshold checker replays the remaining logarithmic inequalities.

## Uniform noncancellation and endpoint signs

Use the frozen M5 critical integrals, A=1/sigma², d=1-sigma,

 B(theta)=A sin(pi theta)/sin(pi(eta-theta)),
 p(theta)=1+P0(theta)=sigma-A pre1+post1 B(theta),
 J=d post1-4sigma² post2,
 C0=-d²-d A pre1+12sigma²+4pre2-3-sigma,
 F0(theta)=C0+J B(theta).

The exact outward checker below verifies

 F0(.8)>1, F0(.9)<-1/5,
 -15/2<p(.8)<p(.9)<-18/5, post1>0, J<0.              (3)

Here monotonicity follows from
B'=A*pi*sin(pi eta)/sin²(pi(eta-theta))>0. Endpoint hulls, rather
than direct interval substitution over the entire T, therefore imply
-7.5<p(theta)<-3.6 everywhere on T. By (1),

             -8<1+P_N(theta)<-3.5.                   (4)

In particular the W numerator never vanishes on the band.
As |P0|<8.5, |P_N-P0|<=E, |t-sigma|<=e²/8 and 0<1-t<1,
the exact denominator

 F_N=(1-t)P_N-4H_N-(3+t)+2delta_N(1+P_N)

satisfies

 |F_N-F0| <=4E+2e²+16delta_N
 <4/50+2*10^-92+16/250 <3/20.                        (5)

For the parameter term, (|P0|+1)e²/8<2e² suffices.
Equations (3)--(5) give F_N(.8)>17/20 and F_N(.9)<-1/20.
Continuity therefore gives at least one zero in each band.

The same source-pole exclusion as M5 applies: a=N+theta and
b=N+theta-eta_e stay at least .08 from integers because
eta_e lies in [.70,.72]. The remaining physical kernel denominators
are nonzero, and the geometrically convergent tail supplies local
analyticity. By (4), every zero of F_N is a noncancelled meromorphic
pole of W=-1-(1+P_N)/F_N. The phase map is strictly monotone and the
bands are disjoint. Thus every integer N>=10^46 has at least one
real W pole in its band, accumulating at sigma.

This replaces the sufficient M5 index 2^(10^120) by 10^46 through
a new polynomial-constant error bound. It remains conservative and
far beyond numerical enumeration; it does not assert optimality or
an effective uniqueness threshold.
