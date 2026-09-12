# M7: explicit complex phase inverse, scalar boxes and full-recurrence tail

Status: candidate for independent review. Fix N>=10^120 and
Omega={theta: .78<Re(theta)<.92, |Im(theta)|<.02}.
The compact smooth-product bound is a separate input below.

## 1. Quantitative phase inverse

M6 supplies analytic s_g on |e|<=r0=10^-5 with
|s_g(e)-s*|<10^-4. Cauchy gives |s_g'|<20 on |e|<=r0/2.
Already for N>=10^6, e -> s_g(e)/(N+theta) maps the disk |e|<=1/N
strictly into itself, since |s_g(e)|<.17 and .17/(N-1)<1/N.
Its contraction constant is at most20/(N-1)<1. Iteration from zero
converges uniformly in theta to an analytic solution e_N(theta).
The same strict estimates hold on a slightly larger parameter neighborhood,
so boundary limits of Omega introduce no analyticity issue.

For real u=Re(theta), the iterates and their limit e0=e_N(u) are
positive real. The identities give

 0<e0<1/N,  N*e0>.14,  |s_g(e0)-s*|<=20e0.

Indeed s_g(e0)>.15 and N/(N+u)>.99. Subtracting the two fixed-point
equations, with y=Im(theta), gives

 |e-e0| <=20|e-e0|/(N-1)+e0|y|/(N-1),
 |e-e0| <= e0|y|/(N-21) <=.04e0/N <e0².              (1)

Consequently epsilon=Re(e)>e0/2, |Im(e)|<e0²,
|e|<1/N and |e|<2epsilon. The auxiliary kernel-sector lemma now
applies, in particular |t(e)|<sigma and |U(t(e),v)|<1 for |v|<=1.
Also |s_g-e s_g'|>.1 on this disk, so |e_theta|<10|e|².
Writing A=Re(a)=N+Re(theta) in e*a=s_g(e) also gives
epsilon*(A+1)<.17+.02e0²+1/N<.2, as required by the compact
bare-product mass lemma.

The roots s_g,s_h have distance less than10^-4 from s* on |e|=r0.
Their removable quotient eta_e=(s_g-s_h)/e is analytic and bounded
by20 on that circle. Cauchy's coefficient estimate gives

 |eta_e-eta|<=20|e|/(r0-|e|)<10^7|e|,                (2)

so Re(eta_e) in[.70,.72]. The same root estimate gives
|s_g(e)-s*|<=10^-4|e|/(r0-|e|)<20|e|.

## 2. Uniform rational boxes

Write d=1-sigma, C=q-t, D=1-tq, q=exp(-e/2). The exponential series
gives |q-1|<=|e|, |1-exp(-e)|<=2|e|, and
|(1-exp(-e))/e-1|<=|e| on the small domain used here.
Using |t-sigma|<=|e|²/10, |t|<sigma<.415 and |q|<1 gives

 |C-d|<2|e|, |D-d|<|e|,
 .58<|C|<.60, |D|<.60,
 |g(q)+sigma²|<2|e|, |g(q)|>.16, |z0|<10.            (3)

Here g(q)=t-Dq, and d in(.585,.586), sigma²>.171396.
The physical identity U(t,1)=q follows by continuing from real e0:
the compact kernel-sector lemma keeps the discriminant in the right
half-plane along that continuation.

Put u_h=tq/C and u*=sigma/d=eta. Since |tq-sigma|<|e|,

 |u_h-u*| <= |e|/.58 + .415*2|e|/(.58²)<5|e|,
                         |u_h|<.75.                 (4)

For every |u|<1, the regularized weight denominators obey
|1-tu|>.58, |1-tu_h|>.68, |1-u_h|>.25.
Thus |f(u)|<2, |f(u_h)|<1.11, the first divided difference has
modulus below3, and both |L1|,|L2|<5. The closed V formulas give

 |V1|<14, |V2|<26, |V1|+|V2|<100.                   (5)

The boundary terms of both moments have joint modulus below100:
|C/g(q)|<.6/.16, |S0|<.415*.6²/.16<1, |f(q)|<2,
and |L1|,|L2|<5; the additional t² factor of H has modulus below1.
Finally Q=q*t²*(1-q²)*(1-t²) satisfies

                     |Q|<2epsilon.                  (6)

Indeed |Q|<.18*2|e|*1.18<.425|e|<.85epsilon.

For delta=t²*(1-exp(-e))/C and kappa=sigma²/d in(.28,.30),
subtracting t²/C from sigma²/d gives an error below2|e|;
the factor (1-exp(-e))/e differs from1 by at most |e| and
|t²/C|<.32. Hence

               |delta/e-kappa|<100|e|.               (7)

These are complex modulus estimates, not extensions of real interval
inequalities by an unspecified continuity radius.

## 3. Damping of r

For arbitrary complex |z|<=r0, the same parameter bounds give |D|>.58
and r=1-(1-exp(-z))/D, so |r-1|<4|z| and the logarithm continued
from r(0)=1 satisfies |log r|<5|z|. The analytic quotient log(r)/z
has value -lambda=-1/d at zero. Cauchy gives, for |e|<=r0/2,

 |log r+lambda e|<=10^6|e|².

As lambda>1.6 and |e|<2epsilon, this implies
Re log r <=-1.6epsilon+4*10^6epsilon²<-epsilon. Thus

                        |r|<exp(-epsilon).           (8)

## 4. Far-kernel disk and normal convergence

For |v|<=.02, the nonnegative-coefficient Y=U-t identity bounds Y
by its value at (|t|,|v|). The trial value Y=.01 is a strict upper
solution, because

 .02*.415*(.415+.01)/(1-.415*.01/.82)<.01.

Monotone iteration from zero therefore gives |U-t|<.01 on this disk.
Since g=t²q-D(U-t) and |t²q-sigma²|<|e|, it follows that

                     Re g>.15, |g|<.20.              (9)

From (1) and (7), Re(delta)>.27epsilon and
|Im(delta)|<402epsilon². Hence

 Re(delta*conj(g)) > .27*.15epsilon-402*.20epsilon²>0,

which proves Re(delta/g)>0. Combining with (8), the exact full
recurrence obeys, whenever |v_n|<=.02,

             |z_(n+1)|<=exp(-epsilon)|z_n|.           (10)

Let m=ceil(4/epsilon). Then |v_n|<=exp(-4)<.02 for n>=m.
Assuming the separately proved compact product bound |Pi_m|<=2,
the bare-product lemma gives |T_m|<600 (as |m-Re(a)|>Re(a)).
Equations (3), (8) imply |z_m|<12000. Thus

 sum_(n>=m)|z_n| <12000/(1-exp(-epsilon))<24000/epsilon.

By (5)--(6), the joint omitted moment contribution is below4.8*10^6.
This proves a geometric tail bound for the full z recurrence; no
separate assertion about decay of Pi_n is made.

All source denominators are excluded on Omega. For m=0 in the periodic
zero equations n=a+2pi*i*m/e or n=b+2pi*i*m/e, Re(a) stays at least.08
and Re(b) at least.06 from an integer. For m!=0,
Re(1/e)=epsilon/|e|²>1/(4epsilon)>N/4, so the imaginary part of the
periodic term cannot cancel |Im(a)|<.02 or
|Im(b)|<.02+10^7|e|. The other rational denominators are separated
by (3)--(5). The global kernel series is analytic by the positive
coefficient majorant and |t|<sigma, |v|<=1. Together with (10), this
gives local normal convergence and holomorphy of the moment series.
Explicitly epsilon>.07/N, so m<60N for every theta in Omega. Beyond
the common integer cutoff60N, (10) has the uniform geometric ratio
at most exp(-.07/N)<1 and starting modulus below12000. Thus the
moving auxiliary cutoff does not obstruct normal convergence.

The compact-product bound remains a necessary separate input for a
uniform moment norm. Once it holds, the compact mass below2*10^4,
(3), (5)--(6) and |Pi|<=2 bound the compact joint norm by8*10^7.
Adding the tail above and boundary100 is safely below10^10.
