# M8 candidate: a larger effective domain for the complex moment bound

Status: candidate for independent review. This is a new domain audit of
the frozen M7 arguments, not a change to those arguments or their receipts.

For every integer N>=10^30, on the open rectangle

    Omega={theta: .78<Re(theta)<.92, |Im(theta)|<.02},

the moments P_N,H_N are holomorphic and satisfy

                sup_Omega(|P_N|+|H_N|)<10^8.             (H8)

## Domain audit

Write e=e_N(theta), e0=e_N(Re(theta)), epsilon=Re(e). The fixed-point
construction in M7_COMPLEX_SCALARS Section1 already applies for N>=10^6.
It gives e0<1/N, |e|<1/N, |e-e0|<e0², epsilon>.99e0 and |e|<2epsilon.
All following estimates use the endpoint e0<=10^-30 and decrease with it.

| Required step | Explicit allowance on the enlarged domain |
|---|---|
| Analytic phase and root boxes | 1/N<=10^-30<5*10^-6; the M6 Cauchy disks are unchanged |
| Kernel-sector lemma | e0<=10^-30<10^-8, its independently proved domain |
| Real part of eta_e | abs(eta_e-eta)<2*10^7 e0<=2*10^-23, inside[.70,.72] |
| Exterior root separation | abs(s-s_g)>=.05-48e0>.049 |
| Exterior kernel separation | abs(g_e(s))>=.001-1000sqrt(e0)>.0009 |
| Crossing half-tube | abs(Im(s))<=8e0<5*10^-5 |
| Parameter Taylor disk | abs(e)<10^-30<10^-5/2 |
| Smooth product | Re sum log R <10^14 sqrt(e0)<=.1<1/2 |
| Scalar damping | Re log r<=-1.6epsilon+4*10^6 epsilon²<-epsilon |
| Tail delta real part | Re delta>.28epsilon-400epsilon²>.27epsilon |
| Tail contraction | Re(delta conjugate(g))>.0405epsilon-80.4epsilon²>0 |

Here s=ne with0<=Re(s)<=4. The exterior separations follow by subtracting
the M7 kernel comparison and root displacement from the real M6 bounds;
they are not continuity assumptions. The crossing estimate uses the same
M6 analytic divided differences and half-tube Cauchy derivative4*10^10.
Consequently the full M7 logarithm comparison and its fewer-than5/e0
prefix count apply, including m=ceil(4/epsilon). In particular |Pi_m|<2.

All rational scalar boxes in M7_COMPLEX_SCALARS follow from abs(e)<10^-30
and abs(t-sigma)<=abs(e)^2/10; their denominator margins exceed .16.
For the far tail, abs(Im(delta))<402epsilon² is unchanged. The explicit
majorant gives Re(g)>.15 and abs(g)<.20, so the last line of the table
establishes the same full-recurrence geometric ratio exp(-epsilon).

The bare-product lemma requires only the stated phase rectangle,
Re(eta_e) in[.70,.72] and epsilon(Re(a)+1)<.2. The last inequality follows
from the phase equation exactly as in M7_COMPLEX_SCALARS Section1; no10^120
restriction occurs in that argument.

The source-zero exclusion uses the distance .08 for a and .06 for b at
the zero periodic copy. All other copies have imaginary part of size
at least pi*N/2, whereas the phase imaginary parts are below.03. The
kernel series is analytic by abs(t)<sigma and its positive coefficient
majorant. A common integer cutoff60N and ratio exp(-.07/N) prove normal
convergence for each fixed N throughout Omega. Thus the moment functions
are holomorphic, not merely bounded along the real interval.

## Norm audit

Use the sharper joint ledger at the end of M7_COMPLEX_SCALARS:

    compact: (2epsilon)*10*2*100*(2*10^4/epsilon)=8*10^7,
    tail:    (2epsilon)*100*(24000/epsilon)=4.8*10^6,
    boundaries: <100.

The t² factor of H has modulus below1 and is already absorbed. The
sum is84,800,100<10^8. The looser10^10 bound chosen in M7 was an allowance,
not the result of a larger required mass. This proves(H8), subject to
independent review of the domain audit and inherited dependencies.
