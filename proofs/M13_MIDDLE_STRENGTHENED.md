# M13: summing the bare-product lower bound strengthens the middle margin

Status: additional analytic lemma for independent review. It uses the
subwindow and all prefactor, kernel, weight and derivative bounds from
M13_MIDDLE_MASS, without changing that earlier proof.

Let M=floor(N/2), so the subwindow is n=N+1+k, 0<=k<=M-1.
Put p=7/10. The telescoping inequalities already proved there imply,
for every k>=1 in this range,

    T_(N+1+k)>(45/82)[2N/(3k)]^p.

Indeed (N+1+v)/(k-v)>N/k, (1-v)/(1+v)>2/3, and
2N/(3k)>1. Since beta>p, replacing beta by p gives a lower bound.
For k=0 the pre-crossing telescope instead gives

    T_(N+1)>(9/2)[5N/6]^p.

Define A=(45/82)(2/3)^p and C0=(9/2)(5/6)^p. Since x^(-p)
decreases, integration over each interval[k,k+1] yields

    sum_(k=1)^(M-1) k^(-p)
       >= integral_1^M x^(-p) dx=(10/3)(M^(3/10)-1).

The empty-range issue never arises because N>=32 implies M>=16.
Moreover C0>15/4, while (10/3)A<75/41<15/4. Therefore

    sum_(n=N+1)^floor(3N/2) T_n
      >N^p[C0+(10/3)A(M^(3/10)-1)]
      >(75/41)(2/3)^(7/10) N^(7/10) M^(3/10)
      >=(75/41)(2/3)^(7/10)(31/64)^(3/10) N
      >(11/10)N.                                      (1)

The last inequality is proved without rounded fractional powers: all
quantities are positive, and the exact tenth-power comparison is

    (75/41)^10 (2/3)^7 (31/64)^3 > (11/10)^10.

The prefactor and weight bounds from M13_MIDDLE_MASS hold for every
term of this entire subwindow, so they can be multiplied into (1):

    S_sub>(41/50)e*(1/4)*(3/2)*(11/10)N
          >(41/50)*(1/4)*(3/2)*(11/10)*(48/329)
          =4059/82250>6/125.                           (2)

The reviewed subwindow logarithmic derivative is less than-15/4;
every other term of S_mid has negative derivative. Consequently

    S_mid,theta<-(15/4)S_sub<-9/50.                    (3)

This strictly strengthens the earlier-3/56 allowance and preserves its
domain N>=32, theta in[.8,.9]. It says nothing about the sign of the
pre-crossing or tail derivatives. Its exact arithmetic is reproduced by
`python -m proofs.m13_middle_strengthened`.
