# M7: effective phase derivatives from a complex moment bound

Status: **candidate for independent review**. This note proves the
holomorphic boundedness input needed by the finite-difference derivative
transfer in proofs/M7_REAL_TO_DERIVATIVE.md. The real \(C^0\) remainder is
never differentiated.

The real inequality \(0<R_e\leq1\) is used only on the real reference ray.
It does not by itself control a complex product. The new work below adds a
small complex phase tube, an elementary complex Gamma domination, a
square-root endpoint continuation, and a geometric tail bound. With those
inputs the uniform bound
\[
 \sup_{\operatorname {dist}(\theta,[.8,.9])<.02}
       \bigl(|P_N(\theta)|+|H_N(\theta)|\bigr)\leq10^{10}
\tag{M7.0}
\]
holds for \(N\geq10^{120}\). The finite-difference argument then gives
\[
 \sup_{.8\leq\theta\leq.9}
 \bigl(|P_N'(\theta)-P_0'(\theta)|
      +|H_N'(\theta)-H_0'(\theta)|\bigr)<.009<1.
\tag{M7.1}
\]
Together with the accepted M6 endpoint signs and the exact transfer
identity, this yields one simple noncancelled W pole in every band for
\(N\geq10^{120}\).

The complex estimates in Sections 3--5 are a candidate analytic lemma and
must pass the independent Astra review before (M7.0)--(M7.1) can be
advertised as a theorem.

## 1. Phase tube and inverse bounds

Put
\[
 \sigma=\sqrt2-1,\qquad \eta=2^{-1/2},\qquad
 I=[4/5,9/10],\qquad s_*=-\log(1/2+\sqrt2/4).
\]
Use the rectangular tube
\[
 \Omega=\{\theta=u+iv: .78\leq u\leq.92,\ |v|\leq.02\}.
\tag{M7.2}
\]
Every disk of radius \(1/100\) centered on \(I\) is contained in \(\Omega\).

For \(e=e_N(\theta)\), write
\[
a=\frac{s_g(e)}e=N+\theta,\qquad b=a-\eta_e(e),\qquad
 x_n=ne.
\]
Write \(\varepsilon=\operatorname {Re}e\).
The M5 phase boxes give, on the real ray,
\[
 .15<s_g<.17,\qquad s_g-e s_g'>1/20,\qquad |s_g'|<2.
\tag{M7.3}
\]
On \(|e|=10^{-5}\), the Rouché box in M6 gives
\(|s_g(e)-s_*|<10^{-4}\). Cauchy's estimate therefore gives
\(|s_g'(e)|<20\) on \(|e|\leq5\cdot10^{-6}\). For \(N\geq10^6\),
the map \(e\mapsto s_g(e)/(N+\theta)\) is a contraction of
\(|e|\leq1/N\), uniformly on \(\Omega\), since its derivative is at most
\(20/(N-.92)\). Thus \(e_N(\theta)\) is holomorphic on the whole tube.
For the real solution \(e_0=e_N(u)\), the box \(s_g(e_0)>.15\) gives
\(N e_0>.14\). Subtracting the two fixed-point equations and using
\(|s_g'|<20\) gives
\[
 |e-e_0|
 \leq\frac{20}{N-1}|e-e_0|
       +\frac{e_0|v|}{N-1}.
\]
Since \(N e_0>.14\) and \(|v|\leq.02\), this implies
\[
 |e-e_0|\leq\frac{e_0|v|}{N-21}<e_0^2.
\]
Consequently, for \(N\geq10^{120}\),
\[
 |e|<2/N,\qquad |\operatorname {Im}e|<4|e|^2,\qquad
 |e_\theta|\leq20|e|^2.
\tag{M7.4}
\]
The last inequality is the exact formula
\[
 e_\theta=\frac{e^2}{e s_g'(e)-s_g(e)}.
\]
The scalar phase lemma proofs/M7_COMPLEX_SCALARS.md supplies the only
kernel facts needed below:
\[
 |t|<\sigma,\qquad |q|<1,\qquad |e|<2\operatorname {Re}e.
\tag{M7.5}
\]

For completeness, the removable quotient
\(\eta_e=(s_g(e)-s_h(e))/e\) is analytic at zero because
\(s_h(e)=s_g(-e)\). On \(|e|=10^{-5}\), the M6 Rouché boxes put both roots
within \(10^{-4}\) of \(s_*\), so \(|\eta_e|<20\). Cauchy's estimate gives
\[
 |\eta_e'|<3\cdot10^6,\qquad
 |\eta_e-\eta|<10^7|e|,\qquad
 |\operatorname {Re}\eta_e|\in[.70,.72]
\tag{M7.6}
\]
throughout the \(e\)-domain in (M7.4). The last interval is the only
information about \(\eta_e\) needed for complex Gamma domination.

## 2. Holomorphy and source-pole exclusion

The source denominators can vanish only when
\[
 n=a+\frac{2\pi i m}{e}\quad\hbox{or}\quad
 n=b+\frac{2\pi i m}{e},\qquad m\in\mathbb Z.
\tag{M7.7}
\]
For \(m\neq0\), (M7.4) makes
\(\operatorname {Im}(2\pi i m/e)=2\pi m\operatorname {Re}(1/e)\)
have size at least \(\pi/|e|\), while \(|\operatorname {Im}a|\leq.02\)
and \(|\operatorname {Im}b|\leq.02+10^7|e|\). It cannot be an integer. For
\(m=0\), \(\operatorname {Re}a\) is at least .08 from an integer and
\(\operatorname {Re}b\) is at least .06 from an integer. The other rational
kernel denominators are separated by the explicit boxes in
proofs/M7_COMPLEX_SCALARS.md. Thus the finite summands have no source
poles in \(\Omega\).

The scalar tail ledger in proofs/M7_COMPLEX_SCALARS.md gives
\(\varepsilon>.07/N\), a cutoff \(m<60N\), and a uniform geometric ratio
\(\leq e^{-.07/N}\) after that cutoff. Together with Section 5 this gives
normal convergence uniformly on compact subsets of \(\Omega\). Consequently
\(P_N\) and \(H_N\) are holomorphic there. This is a required prerequisite
for the finite-difference argument;
real analyticity alone would not permit differentiating a \(C^0\) error
bound.

## 3. Complex smooth-product modulus

Use the exact factorization
\[
 z_n=z_0\,r^n\,T_n(a,b)\,\Pi_{e,n},\qquad
 \Pi_{e,n}=\prod_{j<n}R_e(je).
\tag{M7.8}
\]
The real signed-product lemma gives \(0<R_e\leq1\) only for real \(e,s\).
For the complex tube we prove the compact bound
\[
 |\Pi_{e,n}|\leq2,\qquad
 j\varepsilon<4\quad\text{for every integer }0\leq j<n.
\tag{M7.9}
\]
In particular this controls every prefix \(\Pi_{e,n}\) whose factors have
\(j\varepsilon<4\), including the index \(m=\lceil4/\varepsilon\rceil\)
whether or not \(m\varepsilon=4\).
It is valid for \(N\geq10^{120}\), when \(|e|<2\cdot10^{-120}\). The tail
will be bounded directly for the full \(z_n\) recurrence, rather than by
asserting a separate complex bound for \(\Pi_{e,n}\).

Here is the constant ledger for (M7.9). Let
\(\ell_e(s)=\log R_e(s)\), with the branch \(\ell_0=0\). The exact two-log
formula is
\[
 \ell_e(s)=
 \log\!\left(1+\frac{\eta_e e}{s-s_g}\right)
 -\log\!\left(1+\frac{\delta}{g_e(s)}\right).
\tag{M7.10}
\]
This display is used only away from the removable crossing. On the
crossing interval, \(\ell_e=\log F_e-\log G_e\) with the divided
differences \(F_e,G_e\) from the M6 sharp-kernel lemma; their real parts
are \(>.02\), so this is the analytic continuation of the same logarithm.
Let \(u=\operatorname {Re}\theta\) and let \(e_0=e_N(u)>0\) be the real
phase inverse. The fixed-point estimate in Section 1 gives
\[
 |e-e_0|\leq e_0^2.
\tag{M7.11}
\]
The real reference in the compact logarithm estimate is
\(x=\operatorname {Re}(ne)\); \(e_0\) is used only to control the phase
displacement and the square-root sector. Thus the sign input below is the
real critical inequality \(\psi(x)\leq0\), rather than a presumed sign for
a complex product.

The endpoint comparison is supplied by the auxiliary square-root sector
lemma in proofs/M7_COMPLEX_KERNEL_SECTOR.md. It applies here because
(M7.11) gives its reference hypotheses. In its notation, if
\(s=ne=x+iy\) and \(0\leq x\leq4\), then
\[
 |U(t,e^{-s})-U(\sigma,e^{-x})|<500\sqrt {e_0},\qquad
 |y|\leq8e_0 .
\tag{M7.12}
\]
The second estimate uses \(|e-e_0|\leq e_0^2\) and
\(\operatorname {Re}e>.99e_0\), hence \(n<5/e_0\), on this compact range.
The lemma also
proves \(|t|<\sigma\) and \(|U(t,v)|<1\) for \(|v|\leq1\), so the branch
used here is the physical branch and no continuation-sector assertion is
being made.

Write \(\kappa=\sigma^2/(1-\sigma)\) and
\(\psi(x)=\eta/(x-s_*)-\kappa/g_0(x)\) on the real ray. The accepted
real signed-product lemma gives \(\psi(x)\leq0\). We now compare one
complex logarithm directly with this real first-order function; this
avoids importing the sign of a complex product.

For \(0\leq x\leq4\), (M7.12), \(|D|<1.5\), and \(|U|<1\) give
\[
 |g_e(s)-g_0(x)|<1000\sqrt {e_0},\qquad
 \left|\frac{\delta}{e}-\kappa\right|<200e_0.
\tag{M7.13}
\]
For the second inequality, use
\[
 \frac{\delta}{e}
 =\frac{t^2}{q-t}\frac{1-e^{-e}}e,\qquad
 \left|\frac{1-e^{-e}}e-1\right|\leq2|e|,
\]
\(|q-t|>.57\), and \(|t-\sigma|\leq |e|^2/10\); the elementary
reciprocal difference bound is \(<100|e|\). The root bounds in (M7.6)
and Cauchy's estimate \(|s_g'|<20\) give
\[
 |s_g-s_*|<20|e|,\qquad |s_h-s_*|<50|e|,\qquad
 |\eta_e-\eta|<10^7|e|.
\tag{M7.14}
\]

On \(x\in[0,.1]\cup[.25,4]\), the M6 separations remain
\(|s-s_g|>.049\) and \(|g_e(s)|>.0009\) at
\(e_0\leq10^{-120}\). Substituting (M7.13)--(M7.14) in the two fractions
of (M7.10) gives
\[
 \left|\frac{\eta_e}{s-s_g}-\frac{\eta}{x-s_*}\right|
 <5\cdot10^8 e_0,\qquad
 \left|\frac{(\delta/e)}{g_e(s)}-\frac{\kappa}{g_0(x)}\right|
 <4\cdot10^9\sqrt {e_0}.
\tag{M7.15}
\]
For example, the first bound uses denominator \(.049\), root displacement
less than \(50e_0+8e_0\), and \(|\eta_e|<20\); the second uses
\(|g_0|>.001\), (M7.13), and \(\kappa<.3\). All four fraction moduli are
below \(2\cdot10^3\), so
\(|\log(1+w)-w|\leq2|w|^2\) contributes \(<4\cdot10^7e_0\) after division by
\(e\). Hence
\[
 \left|\frac{\ell_e(s)}e-\psi(x)\right|
 <10^{10}\sqrt {e_0}
\tag{M7.16}
\]
on the exterior ranges. This calculation uses the square-root comparison
from the auxiliary lemma only through (M7.13), and uses no endpoint
\(s\)-derivative.

On \(x\in[.1,.25]\), the M6 complex crossing tube gives
\[
 \left|\frac{\ell_e(s)}e-\psi(s)\right|<4\cdot10^{11}|e|,
\qquad |\psi'(s)|<4\cdot10^{10}.
\]
Since \(|s-x|\leq8e_0\) and \(|e|<2e_0\), this implies
\[
 \left|\frac{\ell_e(s)}e-\psi(x)\right|
 <2\cdot10^{12}e_0\leq2\cdot10^{12}\sqrt {e_0}.
\tag{M7.17}
\]
Thus (M7.16)--(M7.17) yield, on all compact mesh points,
\[
 \operatorname {Re}\ell_e(ne)
 \leq\operatorname {Re}e\,\psi(x)
       +2\cdot10^{13}e_0\sqrt {e_0}.
\tag{M7.18}
\]
There are fewer than \(5/e_0\) points with
\(\operatorname {Re}(ne)\leq4\). Since \(\operatorname {Re}e>0\) and
\(\psi(x)\leq0\), summing (M7.18) gives
\[
 \operatorname {Re}\sum_{j<n}\ell_e(je)
 <10^{14}\sqrt {e_0}<\frac12
\tag{M7.19}
\]
for \(N\geq10^{120}\). Exponentiation proves the compact product bound in
(M7.9).

For the tail, do not bound \(\Pi_{e,n}\) separately. At the first point
with \(\operatorname {Re}(ne)\geq4\), the compact Gamma and product bounds
give \(|z_n|<12000\). Since \(|e^{-ne}|<e^{-4}<.02\), the positive
coefficient kernel majorant (the \(Y=.01\) supersolution in
proofs/M7_COMPLEX_SCALARS.md) gives
\[
 |t|<.415,\quad |U(t,e^{-ne})-t|<.01,\quad
 \operatorname {Re}g_e(ne)>.15.
\]
Set \(m=\lceil4/\varepsilon\rceil\). The scalar calculation also gives
\(\operatorname {Re}\delta>.27\operatorname {Re}e\),
\(|\operatorname {Im}\delta|<402(\operatorname {Re}e)^2\), and
\(|g_e|<.20\). Thus
\(\operatorname {Re}(\delta/g_e)>0\). Its analytic logarithm gives
\(|r|\leq\exp(-\operatorname {Re}e)\). Hence the full recurrence ratio
has modulus at most \(\exp(-\operatorname {Re}e)\), and
\[
 |z_n|\leq12000\exp[-\varepsilon(n-m)],
 \qquad \operatorname {Re}(ne)\geq4.
\tag{M7.20}
\]
This is the only tail estimate used below; no unsupported separate
complex bound for \(\Pi_{e,n}\) is claimed.

## 4. Complex Gamma domination

The bare finite product is
\[
T_n(a,b)=\prod_{j=0}^{n-1}\frac{a-j}{b-j}.
\tag{M7.21}
\]
Set \(A=\operatorname {Re}a\), \(\beta=\operatorname {Re}\eta_e\), and
\(y=\operatorname {Im}\theta\). Since
\(\operatorname {Re}b=A-\beta\),
\[
 |b-j|\geq|A-\beta-j|,\qquad
 |a-j|=|A-j|\sqrt{1+\frac{y^2}{(A-j)^2}}.
\]
The elementary sum
\[
 \sum_{j\geq0}(A-j)^{-2}
 \leq 1/.78^2+1/.78+1/.08^2+1/.08<172
\tag{M7.22}
\]
therefore gives
\[
 |T_n(a,b)|<2\,T_n(A,A-\beta).
\tag{M7.23}
\]
This is the candidate lemma proofs/M7_COMPLEX_PRODUCT_DOMINATION.md.
Its real envelope, proved by elementary harmonic sums rather than Gamma
asymptotics, is
\[
 T_n(A,A-\beta)\leq
300\left(\frac{A+1}{1+|n-A|}\right)^\beta,\qquad
 \beta\in[.70,.72].
\tag{M7.24}
\]
For \(0<\varepsilon\leq1\), \(\varepsilon(A+1)<1/5\), and
\(0\leq n\varepsilon\leq4\), the same lemma proves the explicit mesh mass
\[
 \varepsilon\sum_{n\varepsilon\leq4}T_n(A,A-\beta)<10^4.
\tag{M7.25}
\]
The proof splits the pre and post sides at \(N\), handles the \(N+1\)
factor \(u/(u-\beta)<16\), and sums
\((1+|n-A|)^{-3/4}\); the constant 300 contributes at most 1500 and the
cusp envelope at most 600. Combining (M7.23) with (M7.25), and
including the factor \(2\) from \(|T_n(a,b)|\), gives
\[
 \varepsilon\sum_{\operatorname {Re}(ne)\leq4}|T_n(a,b)|<2\cdot10^4.
\tag{M7.26}
\]
This is the only Gamma mass estimate used below. It is uniform on the
wider real-phase range \(.78\leq\operatorname {Re}\theta\leq.92\) and
does not use an unsupported complex Stirling remainder.

## 5. Complex weight and moment mass

The exact regularization formulas for \(V_{j,e}\) are rational divided
differences in \(t,q,u_h,u_n\). The positive-coefficient kernel identity
\[
 U(t,v)-t=v\,\frac{t(t+U(t,v)-t)}
                       {1-\frac{t}{1-t^2}(U(t,v)-t)}
\]
is a positive-coefficient majorant for real \(0\leq t<\sigma\) and
\(|v|\leq1\). The even expansion and (M7.5) prove the required strict
\(|t|<\sigma\) in the complex tube; consequently its coefficient
majorant gives \(|U(t,v)|<1\) for \(|v|\leq1\). The remaining elementary
boxes are
\[
 |t|<.415,\quad |q|<1,\quad |C|>.58,\quad .55<|D|<.60,\quad
 |g_e(q)|>.16,\quad |u_h|<.75 .
\tag{M7.27}
\]
These are the explicit boxes (3)--(6) in
proofs/M7_COMPLEX_SCALARS.md, not a continuity assertion. To make the
weight arithmetic visible, put \(f(u)=u/(1-tu)\). Then
\[
 |1-tu|>.58,\quad |1-tu_h|>.68,\quad |1-u_h|>.25,\quad
 |f(u)|<2,\quad |f(u_h)|<1.11.
\]
The first divided difference is
\(A_1=[f(u)-f(u_h)]/(u-u_h)
=[(1-tu)(1-tu_h)]^{-1}\), so \(|A_1|<3\); the second is
\(A_2=(f(u)+f(u_h))A_1\), so \(|A_2|<10\). Since
\(|L_1|,|L_2|<5\) and \(|C|>.58\), direct substitution in the closed
forms gives
\[
 |V_{1,e}(u_n)|+|V_{2,e}(u_n)|<100.
\tag{M7.28}
\]
The same boxes give
\[
 |z_0|<10,\qquad |Q|/\varepsilon<2,
\tag{M7.29}
\]
and the joint modulus of all boundary terms in \(P\) and \(H\) is \(<100\):
\(|S_0|<.415(.60)^2/.16<1\), \(|C/g(q)|<4\),
\(|f(q)|<2\), and \(|L_1|,|L_2|<5\). The scalar estimate
\(|Q|<2\operatorname {Re}e\) is exactly the displayed
\(|Q|/\varepsilon<2\) bound used in the mass ledger.

We now bound the normalized absolute mass. The compact Gamma mass in
(M7.26), the compact product factor in (M7.9), and \(|z_0|<10\) give
\[
 \varepsilon\sum_{\operatorname {Re}(ne)\leq4}|z_n|
 <2\cdot(2\cdot10^4)\cdot10=4\cdot10^5 .
\tag{M7.30}
\]
Here the first tail index \(m=\lceil4/\operatorname {Re}e\rceil\) has
\(m\operatorname {Re}e\geq4\), while every prefix factor in \(\Pi_{e,m}\)
has \(j\operatorname {Re}e<4\); hence (M7.9) applies at the start of
the tail. The full recurrence estimate (M7.20), with
\(1-e^{-x}\geq x/2\) for \(x=\varepsilon\), gives
\[
 \varepsilon\sum_{\operatorname {Re}(ne)\geq4}|z_n|<10^5 .
\tag{M7.31}
\]
Indeed the left side is at most
\(12000\varepsilon/(1-e^{-\varepsilon})<24000\), using (M7.20).
Multiplying (M7.30)--(M7.31) by (M7.28)--(M7.29), and adding the
boundary terms, gives a compact contribution below \(8\cdot10^7\), a
tail contribution below \(2\cdot10^7\), and hence
\[
 |P_N(\theta)|<10^9,\qquad |H_N(\theta)|<10^9
 \quad(\theta\in\Omega,\ N\geq10^{120}).
\tag{M7.32}
\]
We retain the larger joint ledger
\[
 \boxed{\sup_{\theta\in\Omega}
       (|P_N(\theta)|+|H_N(\theta)|)<10^{10}.}
\tag{M7.33}
\]
The critical functions are affine in
\(B(\theta)=\sigma^{-2}\sin(\pi\theta)/
\sin(\pi(\eta-\theta))\). On \(\Omega\),
\[
 |\sin(\pi(\eta-\theta))|>.14,\qquad |B(\theta)|<86,
\]
The critical integral boxes from proofs/M7_REAL_TO_DERIVATIVE.md are
\(\mathrm{pre}_1<.5,\ \mathrm{pre}_2<.7,\ \mathrm{post}_1<.5,\)
\(\mathrm{post}_2<.6,\ \sigma^{-2}<6,\ \sigma^2<.18\). Inserting these
in the affine critical formulas gives
\[
 |P_0|<.6+6(.5)+86(.5)=46.6,\qquad
 |H_0|<.18(3+6(.7)+86(.6))<10.6.
\]
Thus the exact critical integral enclosures give
\[
 \sup_{\theta\in\Omega}(|P_0(\theta)|+|H_0(\theta)|)<100.
\tag{M7.34}
\]
Equations (M7.33)--(M7.34) are the promised holomorphic boundedness input.

## 6. Real derivative transfer and effective uniqueness

Let
\[
 f_N=P_N-P_0,\qquad g_N=H_N-H_0.
\]
From (M7.33)--(M7.34), Cauchy's formula on radius
\(\rho=.01\) gives
\[
 |f_N''(\theta)|+|g_N''(\theta)|
 \leq2(10^{10}+100)/\rho^2<10^{16}
\quad(\theta\in I).
\tag{M7.35}
\]
For \(N\geq10^{120}\), the accepted real M6 estimate with \(B=10^{12}\)
and \(e_N<1/N\) gives
\[
 |f_N|+|g_N|
 \leq10^9e_N^{1/4}+10^{21}\sqrt {e_N}+10^{14}e_N
 <10^{-21}+10^{-39}+10^{-106}<2\cdot10^{-21}.
\tag{M7.36}
\]
At each endpoint of \(I\), use the inward one-sided increment; in the
interior choose a sign whose full increment stays in \(I\). With \(h=10^{-18}\), Taylor's theorem and
(M7.35) give
\[
 |f_N'|+|g_N'|
 \leq\frac{2(2\cdot10^{-21})}{h}
      +\frac{10^{16}h}{2}
 =.004+.005=.009<1.
\tag{M7.37}
\]
This is a finite-difference estimate with a separately justified second
derivative bound. It does not differentiate the real \(C^0\) remainder.

For completeness, the exact W denominator is
\[
 F_N=(1-t_N)P_N-4H_N-(3+t_N)+2\delta_N(1+P_N),
 \qquad \delta_N=1-D_I(t_N).
\]
The frozen critical certificate gives \(0<P_0'<75\) and \(F_0'<-6\) on
\(I\). Combining (M7.37) with the accepted
\(\delta_N<1/250\), \(|\delta_N'|\leq30000/N\),
\(|t_N'|<e_N^2\), and \(|1+P_N|<8\), yields
\[
 |F_N'-F_0'|
 \leq4(.009)+150/250+18e_N^2+480000/N<1,
\]
for \(N\geq10^{120}\). Hence \(F_N'<-1\) throughout \(I\). The M6 endpoint
signs give one zero, and strict decrease gives exactly one. The phase-to-\(t\)
map has nonzero derivative, so the zero is simple in \(t\). The numerator is
separated from zero by M6, so the pole is noncancelled.

Thus the candidate effective uniqueness statement is
\[
\boxed{\text{Every integer }N\geq10^{120}\text{ has exactly one simple,
 noncancelled W pole in its phase band.}}
\tag{M7.38}
\]

## 7. Review obligations and provenance

The independent review must verify:

1. the analytic inverse phase and source-pole exclusion on \(\Omega\);
2. the explicit scalar boxes and endpoint square-root continuation in
   proofs/M7_COMPLEX_SCALARS.md and
   proofs/M7_COMPLEX_KERNEL_SECTOR.md, and the one-step product ledger
   (M7.9)--(M7.19);
3. the complex Gamma domination and mesh mass in (M7.21)--(M7.26);
4. the complex regularized-weight box and absolute mass arithmetic in
   (M7.27)--(M7.34).

No finite numerical scan is used as a proof input. The real sign
\(R_e\leq1\) is not silently promoted to a complex sign.

Frozen source commit inspected: a7fa96f.

Input SHA-256 values at authoring time:

M6_ACCEPTANCE.md                         6ee93e1e27984dfda45d6932b943ea953e2953e7bfb10da31dcf65abdc8914a6
proofs/M5_MOMENT_RATE.md                 9d8bdc4d72b8decbf696778ed061c635f8a216ed4440eb73a89c3de56d8fa811
proofs/M6_REAL_MOMENT_RATE.md            901ca9d78df982140078ec079462d31fb5b9b6527592e08cd062d99ce5040af8
proofs/M6_REAL_RATE_DOMAIN.md            fb08308744e8e273c7725da4d1f2fb862e7653ea8daf31ec425f56df6dea0588
proofs/M6_SHARP_KERNEL.md                8717a3a191eb9f958f4b6a68d4066ae41bb8c13bc051985f3fe0791499158487
proofs/M5_DIRECTED_REFINED.md            08668a0ddbba107c2f56cc88e0d5f1b549c9ddec92490f4d35ba5f4e4005e38a
proofs/M5_W_QUANTITATIVE.md              2dc1dee4dae9a0fb58604f7c6d0b630f0410d7074732e1b1c9c202463608763f
proofs/M7_COMPLEX_SCALARS.md             53fa59586ba44673d5904190f4ee3fc556b826677c6053f6ddc08e5a82060c38
proofs/M7_COMPLEX_KERNEL_SECTOR.md      0c1b006aa6d202bc89345b9d0ba194ce8502c504497061007acdca548d59bfe3
proofs/M7_COMPLEX_PRODUCT_DOMINATION.md  c366bb558d128ecdeb8f43de5c1c261df1d1807f3559c6a5d50a76e1b796864c
proofs/M7_UNIQUENESS_TRANSFER.md        641806191be795952a15c2062f5e7a6e5f836f14a087768cb35f9e92bd1c24e0

The output is a candidate analytic lemma and threshold, not an external
publication or an independent review result.
