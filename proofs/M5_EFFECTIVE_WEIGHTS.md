# M5: effective real bounds for the regularized weights

Status: supporting real-variable lemma. The estimates below are deliberately
coarse and are intended for the real moment comparison in
M5_MOMENT_RATE.md. They do not prove the product estimate, the phase
inversion, the directed term, or an effective first-index theorem. In
particular, no held-out \(N=512\) calculation is used.

Put

\[
 e=\varepsilon,\qquad \sigma=\sqrt2-1,\qquad d=1-\sigma,\qquad
 \eta=\frac1{\sqrt2},\qquad u_*=\frac{\sigma}{d}=\frac1{\sqrt2}.
\]

The real input from the kernel and phase lemmas is, for
\(0<e\le 10^{-10}\),

\[
 \frac25<t\le \sigma<\frac{21}{50},\qquad
 0\le \sigma-t\le \frac{e^2}{8},\qquad
 1-\frac e2\le q=e^{-e/2}\le1. \tag{1}
\]

The first two estimates in (1) are the real root bounds recorded in
M5_DIRECTED_LOG.md; they are used here as an input. Consequently

\[
 .57<C:=q-t<.60,\qquad .58<d<.60,\qquad
 |C-d|<.51e,\qquad |tq-\sigma|<.22e. \tag{2}
\]

For \(v\in[0,1]\), use the physical branch

\[
 U(t,v)=\frac{2t}{a(t,v)+\sqrt{\Delta(t,v)}},\qquad
 a(t,v)=1-tv+t^2+t^3v,\qquad
 \Delta(t,v)=a(t,v)^2-4t^2. \tag{3}
\]

The square root in (3) is the nonnegative real square root. Direct
monotonicity in \(v\) gives
\[
 t\le U(t,v)\le U(t,1)=q\le1. \tag{4}
\]
Indeed \(a_v=-t(1-t^2)<0\), hence the denominator in (3) decreases as
\(v\) increases. Define \(u_e(s)=U(t,e^{-s})\) and
\(u_0(s)=U(\sigma,e^{-s})\). The critical ray also satisfies
\(\sigma\le u_0(s)\le1\).

## 1. The regularized weights

Set
\[
 f_t(u)=\frac{u}{1-tu},\qquad g_j(t,u)=f_t(u)^j\quad(j=1,2),
 \qquad u_h=\frac{tq}{C}.
\]
The exact cancellation from M3 gives, including at \(u=u_h\),

\[
 V_{j,e}(u)=
 \frac{A_j(t;u,u_h)+L_j(t,u_h)}{C}, \tag{5}
\]
\[
 A_j(t;u,w)=
 \frac{g_j(t,u)-g_j(t,w)}{u-w}
 =\int_0^1\partial_u g_j(t,w+r(u-w))\,dr,
 \qquad
 L_j(t,w)=\frac{g_j(t,w)}{1-w}. \tag{6}
\]

The integral expression in (6) is the definition at \(u=w\), so no
division by \(u-u_h\) is made in an estimate. From (2),

\[
 \frac{2}{3}<u_h<\frac34,\qquad
 |u_h-u_*|<3e. \tag{7}
\]

For the lower bound, \(\sigma>.414\) and (1) give \(t>.41\) and
\(q>.99\), hence
\(tq>.4059>.4\); together with \(C<.60\) this gives \(u_h>2/3\).
The upper bound follows from \(tq<.42\), \(C>.57\). For the second part,

\[
 \left|\frac{tq}{C}-\frac{\sigma}{d}\right|
 \le \frac{d\,|tq-\sigma|+\sigma\,|C-d|}{Cd}
 < 3e. \tag{8}
\]

On the rectangle \(t\in[.4,.42]\), \(u\in[.4,1]\), one has
\(1-tu\ge.58\), and elementary differentiation gives

\[
\begin{array}{c|ccccc}
 & |f_t|& |(f_t)_u|& |(f_t)_t|&
 |(f_t)_{uu}|& |(f_t)_{tu}|\\ \hline
 \text{upper bound}&2&3&3&5&11 .
\end{array} \tag{9}
\]

Here, for instance,
\((f_t)_u=(1-tu)^{-2}\),
\((f_t)_t=u^2(1-tu)^{-2}\),
\((f_t)_{uu}=2t(1-tu)^{-3}\), and
\((f_t)_{tu}=2u(1-tu)^{-2}+2tu^2(1-tu)^{-3}\).
The chain rule for \(g_j=f_t^j\) therefore gives, for \(j=1,2\),

\[
 |g_j|\le4,\quad |(g_j)_u|, |(g_j)_t|\le16,\quad
 |(g_j)_{uu}|\le40,\quad |(g_j)_{tu}|\le70. \tag{10}
\]

Equations (6), (7), and (10) imply

\[
 |A_j|\le16,\qquad |\partial_u A_j|\le20. \tag{11}
\]

Also \(f_t(u_h)<.75/(1-.42\cdot.75)<1.1\), so
\[
 |L_j|<5,\qquad |A_j+L_j|<21. \tag{12}
\]
It follows from \(C>.57\) that

\[
 \boxed{|V_{j,e}(u)|<40\quad (j=1,2,\ .4\le u\le1).} \tag{13}
\]

The same argument at \(t=\sigma\), \(C=d\), \(u_h=u_*\), gives
\(|V_{j,0}(u)|<40\). It also gives the uniform \(u\)-Lipschitz bound

\[
 |\partial_u V_{j,e}(u)|,\ |\partial_u V_{j,0}(u)|<36. \tag{14}
\]

For the perturbation estimate, compare (6) at
\((t,u_h)\) and \((\sigma,u_*)\), holding \(u\) fixed. Along the segment
in (6), the \(u\)-argument changes by at most \(3e\). Hence (10) gives

\[
 |A_j(t;u,u_h)-A_j(\sigma;u,u_*)|
 \le 70\frac{e^2}{8}+40(3e)<121e. \tag{15}
\]

Viewing \(L_j(t,w)\) as a function of its two displayed variables,

\[
 |\partial_t L_j|\le\frac{16}{.25}<64,\qquad
 |\partial_w L_j|\le\frac{16}{.25}+\frac4{.25^2}<128,
\]
so (1), (7) imply

\[
 |L_j(t,u_h)-L_j(\sigma,u_*)|<385e. \tag{16}
\]

Finally,
\[
 \left|\frac1C-\frac1d\right|
 =\frac{|C-d|}{Cd}<1.6e.
\]
Combining (12), (15), and (16) in (5) proves the fixed-\(u\) estimate

\[
 \boxed{|V_{j,e}(u)-V_{j,0}(u)|<1000e
 \quad(j=1,2,\ .4\le u\le1).} \tag{17}
\]

The constants \(40,1000,36\) are much smaller than the ledger allowance
\(10^{20}\).

## 2. The square-root endpoint and a \(1/2\)-Hölder bound

The discriminant in (3) factors as

\[
 \Delta(t,v)=
 \bigl((1-t)^2-t(1-t^2)v\bigr)
 \bigl((1+t)^2-t(1-t^2)v\bigr). \tag{18}
\]

For \(t\in[.4,.42]\), \(v\in[0,1]\),
\[
 .8<a(t,v)<1.2,\qquad |a_t(t,v)|<2.4,\qquad
 |\Delta_t(t,v)|<10. \tag{19}
\]
On the physical subbox \(t\le\sigma\), (18) gives \(\Delta\ge0\) and
\(a\ge2t\), so the denominators \(a+\sqrt\Delta\) are at least
\(2t>.8\).
Using (1), (19), and the real inequality
\[
 |\sqrt{x}-\sqrt{y}|\le\sqrt{|x-y|}\qquad(x,y\ge0), \tag{20}
\]
gives, uniformly in \(v\in[0,1]\),

\[
 |a(t,v)-a(\sigma,v)|<.3e^2,\qquad
 |\Delta(t,v)-\Delta(\sigma,v)|<1.25e^2,
\]
\[
 |\sqrt{\Delta(t,v)}-\sqrt{\Delta(\sigma,v)}|<1.2e,\qquad
 \boxed{|U(t,v)-U(\sigma,v)|<3e.} \tag{21}
\]

The last estimate is obtained by subtracting the two quotients in (3)
and using the denominator lower bound .8. No division by
\(\sqrt{\Delta}\) occurs. Thus (21) remains valid at \(v=1\), where the
critical discriminant is zero and \(s=0\).

For \(v,w\in[0,1]\), (19) also gives
\[
 |a(t,v)-a(t,w)|<.42|v-w|,\qquad
 |\Delta(t,v)-\Delta(t,w)|<1.1|v-w|.
\]
Applying (20) once more to (3) yields

\[
 |U(t,v)-U(t,w)|<3|v-w|^{1/2}. \tag{22}
\]
Since \(|e^{-s}-e^{-r}|\le|s-r|\), (22) and (14) imply

\[
 |u_e(s)-u_e(r)|,\ |u_0(s)-u_0(r)|
 <3|s-r|^{1/2}, \tag{23}
\]
\[
 \boxed{
 |V_{j,e}(u_e(s))-V_{j,e}(u_e(r))|<110|s-r|^{1/2}
 } \tag{24}
\]
and the same bound with \(e\) replaced by \(0\). Combining (17),
(21), and (14) also gives the endpoint-safe comparison

\[
 \boxed{
 |V_{j,e}(u_e(s))-V_{j,0}(u_0(s))|<1200e
 \quad(s\ge0,\ j=1,2).
 } \tag{25}
\]

The estimates (21)--(25) are real estimates; they make no claim about a
complex square-root continuation.

## 3. The critical profile

Write

\[
 \phi(u)=\frac{(u-\sigma)(1-\sigma u)}
 {\sigma(1-\sigma^2)u},\qquad
 \phi(u_0(s))=e^{-s}, \tag{26}
\]
\[
 M_{\rm raw}(u)=
 (u-\sigma)^{2+\sqrt2}
 \left(\frac1\sigma-u\right)^{\sqrt2}
 |u-u_*|^{-\eta}u^{-1-\sqrt2},\qquad
 M(u)=\frac{M_{\rm raw}(u)}{M_{\rm raw}(1)}. \tag{27}
\]

The real critical profile from M3 is

\[
 Z_\theta(s)=
 \begin{cases}
 -A\,M(u_0(s)),&0\le s<s_*,\\
 B(\theta)\,M(u_0(s)),&s>s_*,
 \end{cases} \tag{28}
\]
where
\[
 s_*=-\log\left(\frac12+\frac{\sqrt2}{4}\right),\qquad
 A=\sigma^{-2},\qquad
 B(\theta)=A\,\frac{\sin(\pi\theta)}
                 {\sin(\pi(\eta-\theta))}. \tag{29}
\]
At \(s=s_*\) the two one-sided profiles have the integrable
\(|s-s_*|^{-\eta}\) singularity; its value at that single point is
irrelevant.

For \(\theta\in[.8,.9]\), \(0.09<\theta-\eta<.20\). The chord bound
\(\sin(\pi x)\ge2x\) for \(0\le x\le1/2\) gives
\[
 A<6.25,\qquad |B(\theta)|<\frac{6.25}{.18}<35. \tag{30}
\]
The denominator in (27) satisfies
\[
 M_{\rm raw}(1)
 =d^{2+\sqrt2}\left(\frac1\sigma-1\right)^{\sqrt2}
 (1-u_*)^{-\eta}
 >d^4>.58^4>.1. \tag{31}
\]
For \(u\in[\sigma,1]\),
\[
 u-\sigma\le1,\quad \frac1\sigma-u\le2,\quad
 u^{-1-\sqrt2}<.4^{-5/2}<16.
\]
Thus
\[
 0<M(u)<480\,|u-u_*|^{-\eta}. \tag{32}
\]

On \(u\in[.6,.8]\),
\[
 \left|\frac{d}{du}\log\phi(u)\right|
 =\left|\frac1{u-\sigma}-\frac{\sigma}{1-\sigma u}-\frac1u\right|
 <8. \tag{33}
\]
Consequently, in this neighborhood,
\(|u-u_*|\ge|s-s_*|/8\). Outside it,
\(|u-u_*|>.09\). Since \(0<s_*<1\), (32), (33), and
\(|s-s_*|\le4\) on \(0\le s\le4\) give the integrable envelope

\[
 \boxed{|Z_\theta(s)|<4\cdot10^5\,|s-s_*|^{-\eta}
 \quad(0\le s\le4,\ s\ne s_*).} \tag{34}
\]

Indeed, on \([.6,.8]\) use \(8^\eta<5\) in (32), while outside it use
\(.09^{-\eta}<6\) and \(4^\eta<3\); multiplying by the phase bound
\(35\) in (30) is below \(4\cdot10^5\). Because \(\eta<.71\),

\[
 \int_0^4 |s-s_*|^{-\eta}\,ds
 =\frac{s_*^{1-\eta}+(4-s_*)^{1-\eta}}{1-\eta}<12,
\]
and hence
\[
 \int_0^4|Z_\theta(s)|\,ds<4.8\cdot10^6. \tag{35}
\]

For the tail, (26) implies
\[
 e^{-s}=\phi(u_0(s))\ge u_0(s)-\sigma,
\]
because \(1-\sigma u\ge d\) and
\(\sigma(1-\sigma^2)u\le\sigma(1-\sigma^2)<d\) on
\([\sigma,1]\). Thus \(u_0(s)-\sigma\le e^{-s}\). For \(s\ge4\),
\(u_0(s)-\sigma<.02\) and \(u_*>.7\), so
\(|u_0(s)-u_*|>.26\). Inserting this in (27), and using
\(2+\sqrt2>3\), gives

\[
 M(u_0(s))<2000e^{-(2+\sqrt2)s}<2000e^{-3s},
 \qquad
 \boxed{|Z_\theta(s)|<10^5e^{-3s}\quad(s\ge4).} \tag{36}
\]
Therefore
\[
 \int_4^\infty |Z_\theta(s)|\,ds
 <\frac{10^5}{3}e^{-12}<1, \tag{37}
\]
where the last coarse inequality follows already from \(e^4>50\).
Equations (35)--(37) prove the explicit real mass bound

\[
 \boxed{\int_0^\infty|Z_\theta(s)|\,ds<5\cdot10^6.} \tag{38}
\]

For use with the weighted moments, (13) gives
\[
 \int_0^\infty |Z_\theta(s)V_{j,0}(u_0(s))|\,ds
 <2\cdot10^8. \tag{39}
\]

Finally, differentiating the four factors in (27) gives the crude
pointwise estimate
\[
 |M'(u)|<10^7\bigl(1+|u-u_*|^{-1-\eta}\bigr)
 \quad(\sigma<u<1,\ u\ne u_*). \tag{40}
\]
To see that (40) is uniform at \(u=\sigma\), the only potentially small
factor is \((u-\sigma)^{2+\sqrt2}\), and its differentiated power is
\((u-\sigma)^{1+\sqrt2}\le1\); the other denominators are bounded by
\(\sigma>.4\), \(1/\sigma-u\ge1/\sigma-1>1\), and (31). Near
\(u_*\), the displayed \(|u-u_*|^{-1-\eta}\) term is the only singular
one. Combining (33), (40), (14), (22), and the boundedness in (34) shows
that, for \(0<\rho\le1/10\), the weighted critical profile
\[
 Y_{j,\theta}(s)=Z_\theta(s)V_{j,0}(u_0(s))
\]
satisfies, whenever \(|s-s_*|,|r-s_*|\ge\rho\),

\[
 |Y_{j,\theta}(s)-Y_{j,\theta}(r)|
 \le 10^{15}\rho^{-1-\eta}|s-r|^{1/2}. \tag{41}
\]
For points on opposite sides of \(s_*\), use (34) and
\(|s-r|\ge2\rho\); on one side, use (40) and the
\(1/2\)-Hölder estimate (22). The same bound holds across \(s=0\)
because (22), rather than a derivative at the square-root endpoint, is
used. In particular the much larger ledger constant
\[
 A_{\rm ledger}=\exp(10^{54})
\]
dominates both the mass bound in (39) and the Hölder constant in (41).

As an independent rational-algebra audit of the weight part, the
root-owned checker proofs/m5_weight_boxes.py uses the equivalent
closed forms
\[
 V_{1,e}(u)=\frac{[(1-tu)(1-tu_h)]^{-1}+L_1}{C},
\qquad
 V_{2,e}(u)=\frac{[f_t(u)+f_t(u_h)][(1-tu)(1-tu_h)]^{-1}+L_2}{C}.
\]
Its exact-box/automatic-differentiation pass covers
\(t\in[.4,.415]\), \(q\in[.99,1]\), \(u\in[.4,1]\), and
\((1-e^{-e})/e\in[.99,1]\); it reports value upper bounds
\(10.69\) and \(18.27\) for \(V_1,V_2\), respectively, and
all recorded rational Jacobian and boundary bounds below \(10^6\).
This is a cross-check of the rational factors, not a replacement for the
real square-root estimate (21).

The same checker gives the effective boundary and scale limits needed in
the moment identities.  With
\[
 D=1-tq,\qquad g=t-Dq,\qquad S_0=-\frac{tD^2}{g},
\]
write
\[
 {\cal B}_P=\frac{C}{g}+L_1S_0,\qquad
 {\cal B}_{H/t^2}=f_t(q)\frac{C}{g}+L_2S_0,\qquad
 {\cal Q}_e=q\,t^2\,\frac{1-e^{-e}}e(1-t^2).
\]
At \((t,q)= (\sigma,1)\), direct substitution in these rational formulas
gives
\[
 {\cal B}_P=-d,\qquad {\cal B}_{H/t^2}=-3,\qquad
 {\cal Q}_e=K:=\sigma^2(1-\sigma^2). \tag{42}
\]
The auxiliary coordinate satisfies
\[
 0\le1-q\le e/2,\qquad
 0\le1-\frac{1-e^{-e}}e\le e/2,\qquad
 |t-\sigma|\le e.
\]
The checker reports an exact rational-box \(L^1\) Jacobian bound below
\(452\) and boundary values below \(5\) on
\(t\in[.4,.415]\), \(q\in[.99,1]\), and
\((1-e^{-e})/e\in[.99,1]\).  The mean-value theorem therefore gives the
explicit real estimates
\[
 |{\cal B}_P+d|,\quad
 |{\cal B}_{H/t^2}+3|,\quad
 |{\cal Q}_e-K|<10^6e. \tag{43}
\]
Thus (43) records the boundary limits and \(Q/e\to K\), rather than only
their qualitative convergence.  When the \(H/t^2\) identity is converted
back to \(H\), the prefactor obeys
\[
 |t^2-\sigma^2|=(t+\sigma)|t-\sigma|<e.
\]
Its product with the bounded moment/profile terms is absorbed by the
ledger majorant \(A_{\rm ledger}\).

The only inherited conditions in this note are the real root bounds (1)
and the exact M3 regularization/profile formulas. Everything else above
is a real inequality on the stated boxes. No complex estimate, product
convergence assertion, \(D_I\) estimate, or numerical validation at
\(N=512\) is included.
