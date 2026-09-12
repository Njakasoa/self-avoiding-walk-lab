# M6 candidate: second logarithmic displacement of W poles

Status: conditional candidate, awaiting the directed constant theorem and
independent review. The M5 theorems remain unchanged.

Use sigma=sqrt(2)-1, eta=1/sqrt(2), s*=-log(1/2+sqrt(2)/4),
L=logN, and the exact phase family e_N(theta). Write
p(theta)=1+P0(theta), f=F0'(theta*), p*=p(theta*), and

 c_D=[log4-digamma(2+sqrt2)]/sigma,
 b=sigma*(1+c_D)-log(s*).

The directed input to prove is

 D(t(e))=log(1/e)/sigma+c_D+O(e log(1/e)).                (D)

Since e_N=s*/N+O(N^-2) uniformly, (D) gives

 sigma*(1+D_N)=L+b+O(logN/N).

The shift caused by the moving phase in e_N has size O(1/N), so b has
no theta dependence. Uniform reciprocal expansion gives

 delta_N=1-D_I=sigma/L-sigma*b/L²+O(L^-3).               (1)

The accepted M5 moment error O(N^-1/20) is O(L^-k) for every fixed k.
The exact denominator identity therefore yields, in C0,

 F_N(theta)=F0(theta)+2sigma*p(theta)/L
                     -2sigma*b*p(theta)/L²+O(L^-3).     (2)

M5 already provides eventual unique simple roots theta_N and
x_N=theta_N-theta*=O(1/L). Taylor-expand F0 to second order and p to
first order in (2). The cubic and omitted terms are O(L^-3), uniformly
on the fixed phase interval. Set C1=2sigma*p*/f>0 and

 C2= -[F0''(theta*)*C1²/2 -2sigma*p'(theta*)*C1
                                    -2sigma*b*p*]/f.    (3)

Substitution gives

 theta_N=theta*-C1/L+C2/L²+O(L^-3).                     (4)

For a direct remainder argument, first recover the M5 relation
x_N=-C1/L+O(L^-2) from (2). Substitute that relation into its quadratic
terms to obtain f*(x_N+C1/L-C2/L²)=O(L^-3). Division by the fixed
nonzero f proves (4). No differentiation of the remainder in (D) is
needed for this phase statement; M5 already establishes uniqueness.

## Form using the affine critical profile

Write F0=C0+J B(theta), p=sigma-A*pre1+post1*B(theta),
where A=1/sigma², J=(1-sigma)*post1-4sigma²*post2<0, and
B=A*sin(pi*theta)/sin(pi*(eta-theta)). Then

 B'=A*pi*sin(pi*eta)/sin²(pi*(eta-theta)),
 B''/B'=2pi*cot(pi*(eta-theta)),
 p'/f=post1/J,   F0''/f=B''/B'.

Thus (3) is equivalently

 C2 = C1*[b+2sigma*post1/J]
                 -pi*cot(pi*(eta-theta*))*C1².           (5)

This form avoids dividing separately estimated large derivatives. The
critical integrals and root interval are already certified by M5; new
work must certify b and C2, retaining all interval dependency losses.
The numerical sign of C2 is not assumed here.

## Spatial consequence

M5 gives sigma-w_N=K/N²-2K(theta_N-eta/2)/N³+O(N^-4),
with K=s*²/16. Consequently (4) implies

 sigma-w_N=K/N²-2K(theta*-eta/2)/N³
           +2K*C1/(N³L)-2K*C2/(N³L²)+O(1/(N³L³)).       (6)

All statements in this file are conditional on a justified directed input
(D). A computed fit, a digamma evaluation without an enclosure, or the
old O(1) directed remainder does not establish (D) or C2.
