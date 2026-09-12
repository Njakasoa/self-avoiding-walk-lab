# M8 research lemma: an exact primitive of the bare product

Status: algebraic candidate; its use in a sharper uniform moment error
remains a research obligation. This note does not assert a new rate.

Let beta=a-b with beta!=1, and

    T_0=1, T_(n+1)=(a-n)/(b-n)*T_n,

with no denominator b-n equal to zero. Define

    Q_n=(n-a)T_n/(1-beta), n>=0,
    Q_-1=-(b+1)/(1-beta).

Then for every integer n>=0,

                         T_n=Q_n-Q_(n-1).             (1)

For n=0 this is(-a+b+1)/(1-beta)=1. For n>=0,

    (n+1-a)T_(n+1)-(n-a)T_n
       =(n-a)T_n*[(n+1-a)/(n-b)-1]
       =(1-beta)T_(n+1),

which proves the remaining cases. Thus for any finite scalar weights w_n,

    sum_(n=0)^M T_n w_n
      =Q_M w_M+(b+1)w_0/(1-beta)
         +sum_(n=0)^(M-1) Q_n(w_n-w_(n+1)).           (2)

When the weights decay exponentially and the product grows at most
polynomially, the boundary Q_M w_M tends to zero and(2) passes to the
infinite sum by absolute convergence. Those conditions hold for the
accepted real W weights r^n Pi_n V_e(ne), since0<Pi_n<=1, r<1, V_e is
bounded and the bare product has the M7 polynomial envelope.

## Why this identity matters for the coverage gap

The current real moment comparison bounds the absolute singular profile
cell by cell, leading to a conservative e^(1/4) error. At the critical
limit, the corresponding continuous primitive is

    Q(x)=(x-s*)G_theta(x)/(1-eta),

where G_theta is the pre/post critical bare profile. Its derivative is
G_theta on either side and Q is continuous with value0 at the crossing,
because eta<1. Consequently integration by parts gives

    integral_0^infinity G_theta(x) w(x) dx
      =s* w(0)/(1-eta)-integral_0^infinity Q(x) w'(x) dx,

whenever w is absolutely continuous with the stated integrability and
decay. The singularity has become a vanishing cusp in the primitive.

For the exact W sum, take w_n=r^n Pi_n V_e(ne) and multiply(2) by e.
The new comparison object is e Q_n, not T_n directly. This suggests a
route to bounds based on discrete weight differences and the integrable
cusp, rather than the crude mass of the closest cells.

Still to prove before claiming an improved moment rate: explicit uniform
bounds for eQ_n-Q(ne), discrete differences of the exact weights, the
parameter-dependent boundary, and the full tail. The algebraic identity
alone neither yields O(e) nor closes the finite-to-asymptotic gap.
