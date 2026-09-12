# M8 candidate: an explicit resummed phase error and improved algebraic rate

Status: candidate for independent review. Uses the accepted M6 real
moment and directed-constant estimates. Uniqueness at10^57 is a separate
M8 candidate; the phase estimate below applies to every selected root
in the band for N>=10^46 even without that uniqueness improvement.

Use L=logN, d_hat=sigma/(L+b), b=sigma(1+c_D)-log(s*), and let
theta_hat_N be the zero of

    F_hat_N(theta)=F0(theta)+2d_hat*(1+P0(theta)).

This is the same explicit affine/trigonometric approximation as M6.
Put

    E(N)=10^9 N^-1/4+10^21 N^-1/2+10^14/N,
    R_theta(N)=(5/27)*(4E(N)+2/N²+285/(N logN)).        (1)

For every integer N>=10^46 and every W root theta_N in[.8,.9],

                  abs(theta_N-theta_hat_N)<=R_theta(N). (2)

## Directed reciprocal with a finite error

The real phase certificate gives .3<s_g'(e)<.4 on the physical domain.
Thus s_g(e)=s*+m_e e with .3<m_e<.4, by the real mean-value theorem.
The phase equation gives

    s*/e=N+theta-m_e, .4<theta-m_e<.6,
    0<log(1/e)-[logN-log(s*)]<.6/N.

Write D_hat=L/sigma+c_D-log(s*)/sigma. The accepted directed theorem
has abs(D-log(1/e)/sigma-c_D)<=100e log(1/e). Since e<1/N and
x log(1/x) increases on(0,exp(-1)),

    abs(D-D_hat)<.6/(sigma N)+100logN/N<102logN/N.

M6 gives D>L/sigma on this domain. Also D_hat>L/sigma since c_D>3/4
and s*<1. Hence both reciprocal denominators1+D and1+D_hat exceed
L/sigma. Since sigma²<.18,

    abs(delta_N-d_hat)
      =abs(D-D_hat)/[(1+D)(1+D_hat)]<19/(N logN).      (3)

No derivative of the directed remainder is used.

## Uniform denominator error and inverse stability

M6 gives abs(P_N-P0)+abs(H_N-H0)<=E(N), abs(1+P0)<7.5 and abs(P0)<8.5.
Using the exact denominator identity and0<1-t+2delta_N<1 gives

    abs(F_N-F_hat_N)<=4E(N)+2/N²+285/(N logN).         (4)

The parameter term is bounded by(abs(P0)+1)abs(t-sigma)<2e².
The final term is2abs(1+P0)*abs(delta_N-d_hat), using(3).

The certified critical margins and d_hat<sigma/logN<1/250 yield

    F_hat_N'=F0'+2d_hat P0'<-6+150/250=-27/5.

The left endpoint remains positive: F0(.8)>1, so
F_hat_N(.8)>1-15/250>0. The right remains negative because
F0(.9)<-1/5 and1+P0(.9)<0. Thus theta_hat_N exists uniquely in the
same sector. Evaluate(4) at any exact root and use the real mean-value
theorem to obtain(2). In particular the phase error is O(N^-1/4),
an improvement over the earlier non-effective O(N^-1/20) statement.

## Spatial error

For real e<=10^-8, the M7 even-kernel expansion and its Cauchy bound give

    abs(t_e)<=e/8+16*10^6 e³<e/7.

Also abs(e_theta)=e/(N+theta-s_g')<e/N. Therefore
0<t_N'(theta)<1/(7N³). For w_hat_N=t_N(theta_hat_N),

                abs(w_N-w_hat_N)<=R_theta(N)/(7N³),   (5)

which is O(N^-13/4). This concerns evaluation of the full analytic
kernel at the resummed phase, not a finite truncation of its1/N series.

At the proposed uniqueness threshold N>=10^57, the rational allowance
E(N)<5.656*10^-6 and logN>114 give the concrete consequences

    abs(theta_N-theta_hat_N)<4.19*10^-6,
    abs(w_N-w_hat_N)<6*10^-7/N³.

The decreasing function R_theta(N) retains the stronger dependence on N.
These bounds are checked exactly in m8_chebyshev_threshold.py.

## Improved derivative rate for subsequent residue analysis

Assuming M8_COMPLEX_DOMAIN, apply the joint interpolation inequality
in M8_CHEBYSHEV_THRESHOLD with m=ceil(logN), M=10^8+100 and E=E(N).
Here log(22/15)>1/4 (for example exp(1/4)<4/3<22/15), so
q^m<=N^-log(22/15). Its two tail terms are O(m²q^m), while the real
term is20m² E(N). Thus uniformly on the real phase sector,

    abs(P_N'-P0')+abs(H_N'-H0')=O(N^-1/4 log²N).        (6)

Equation(6) follows from a proved holomorphic bound. The real error in
(1) is never directly differentiated. The fixed-degree exact threshold
certificate and this variable-degree asymptotic statement have distinct
purposes; neither replaces a finite certificate at an accessible index.
