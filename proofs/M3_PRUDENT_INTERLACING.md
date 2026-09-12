# All-index interlacing lemma for the prudent ramp series P

Status: conditional mathematical deduction from the explicit formulas and
Theorem 17 of Bacher–Beaton (2014), independently scrutinized by Astra during
this research batch. This proves infinitely many zeros of 1+P, **not**
infinitely many singularities of J=(P-H)/(1+P). Novelty is unresolved.

Use the physical kernel U(t,v), q=U(t,1), C=q-t, D=1-tq and
u_j=U(t,q^(2j)). Let a_l denote the pole called t_(2l) in the primary source.
It is the unique zero in the specified real interval of

    h_l(t)=tq-C*u_l.

The source establishes 0<a_0<a_1<...<sigma=sqrt(2)-1, simple poles of P at
these points, and meromorphy with no other poles between these real poles.
All algebra below is evaluated for 0<t<sigma; at each fixed a_l,
0<t<q<1, C,D>0, and u_j strictly decreases from q toward t.

## Signs of the summands at a pole

Write the numerator of A_j apart from C*(1-t²) as

    F_j=u_j*D-[q*C+t*(1-q²)*u_j]*u_(j+1).

Since u_(j+1)<=u_j and the bracket is positive,

    F_j >= u_j*[D-q*C-t*(1-q²)*u_j]
         = u_j*(1-q²)*(1-t*u_j) > 0.

Thus A_j has the sign of h_j. At t=a_l, monotonicity of u_j gives
h_j<0 for j<l and h_j>0 for j>l.

Write G_j=t-D*u_(j+1), the variable part of the numerator of B_j.
At a_l, u_l=tq/C, so for every j<l,

    G_j <= t-D*u_l
         = t*(C-q*D)/C
         = -t²*(1-q²)/C < 0.

Consequently all prefix factors B_j for j<l are strictly positive and finite.
For l=0 the prefix product is 1.

To determine G_l, invert the kernel on its physical real branch:

    phi(x)=((1+t²)*x-t-t*x²)/(t*(1-t²)*x),
    phi(U(t,v))=v.

Its derivative is (1/x²-1)/(1-t²)>0 for 0<x<1. The comparison point t/D
lies in (0,1), because t*(1+q)<2*sigma<1. Direct algebra gives

    phi(t/D)-q²*phi(tq/C)
      = q*t³*(1-q²)/(C*(1-t²)*D) > 0.

Because phi(u_(l+1))=q²*phi(u_l), strict monotonicity implies
u_(l+1)<t/D, hence G_l>0. All later G_j are positive as u_j decreases.
Therefore A_j,B_j are positive for every j>l, and the numerator h_l*B_l
is positive at a_l. All factors 1-t*u_j are positive.

## Local analytic justification for the infinite tail

Only a neighborhood of each **fixed** a_l is needed; no neighborhood uniform
in l is asserted. At v=0, U(t,0)=t on the physical branch, h=t², and

    B(t,0)=q²*C²/D² < 1,

because q*C<D is equivalent to q²<1. The algebraic kernel and rational
summands are analytic near (a_l,0), with nonzero denominators. Continuity
therefore gives a complex neighborhood in t and |v|<epsilon on which A and
the hook summand are bounded and |B|<beta<1. Shrink the neighborhood so that
|q|<r<1. Then q^(2j) enters that v disk uniformly for sufficiently large j.
Every earlier factor with index j>l has nonzero denominator at a_l and remains
analytic after one further finite shrinking of the neighborhood. The geometric
majorant proves locally uniform convergence of the remaining tail and thus its
holomorphy. The square-root branches are analytic there because a_l<sigma;
for real 0<=v<=1 the discriminant is positive, and finitely many such branch
choices are continued locally.

## Negative residues and interlacing

Let K_l=product_(j<l) B_j, and let

    S_(l+1)=A_(l+1)+B_(l+1)*A_(l+2)+...

be the locally holomorphic tail. Near a_l the series for P separates as
an analytic finite prefix plus

    q*K_l*[h_l*A_l+(h_l*B_l)*S_(l+1)] / h_l.

The displayed numerator is strictly positive at a_l: q,K_l,h_l*A_l,h_l*B_l
are positive, and the convergent tail has positive terms. Hence its numerator
does not vanish. The source's simple pole of P forces h_l to have a simple
zero. The unique-zero statement together with h_l>0 near t=0 and h_l<0 near
sigma implies h_l'(a_l)<0. Therefore the residue of P at a_l is negative.

It follows that on each interval (a_l,a_(l+1)),

    P(t) -> -infinity as t -> a_l from the right,
    P(t) -> +infinity as t -> a_(l+1) from the left.

P is continuous on that interval by the source's pole classification.
The intermediate value theorem gives at least one r_l with P(r_l)=-1.
The disjoint intervals give infinitely many distinct zeros of 1+P.
No uniqueness or simplicity of these zeros is claimed.

## The remaining obstruction

At such a zero r_l, J has a pole only if 1+H(r_l) is nonzero (or, more
generally, if numerator cancellation has insufficient order). The five local
certificates prove noncancellation in five intervals only. This interlacing
lemma neither extends those signs to all l nor excludes eventual cancellation.
In particular, infinitely many zeros of a denominator do not by themselves
prove that its quotient is non-D-finite. M3's selected theorem remains OPEN.
