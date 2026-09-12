# Independent review of the strengthened middle mass

Verdict: PASS. The summed bare-product lower bound yields
S_sub>4059/82250>6/125 and S_mid,theta<-9/50 uniformly for N>=32,
theta in [.8,.9]. This strengthens the earlier middle contribution only;
it gives no pre-crossing, boundary or tail conclusion.

The subwindow has exactly M=floor(N/2) terms, indexed by
n=N+1+k for 0<=k<=M-1. For k>=1 the already reviewed telescoping
bound gives a power with base larger than 2N/(3k)>1. Replacing beta>.7
by p=.7 therefore lowers that power, so the stated k-dependent lower
bound has the correct direction. At k=0 the pre-crossing telescope has
base larger than 5N/6>1, giving the separate C0*N^p lower bound.
No singular k^(-p) expression is used at k=0.

Since x^(-p) decreases, its left rectangle over [k,k+1] is at least its
integral. Summing k=1 through M-1 yields the integral from 1 to M with
the exact coefficient 10/3. The resulting negative constant is safely
absorbed by the k=0 term: (5/6)^p>5/6 implies C0>15/4, while
(10/3)A=(75/41)*(2/3)^p<75/41<15/4. Dropping their strictly positive
difference is legitimate.

The remaining power term is
(75/41)*(2/3)^(.7)*N^(.7)*M^(.3).
Using M>=31N/64 gives a lower bound proportional to N. All factors
are positive, so raising both sides of the final coefficient comparison
to the tenth power preserves the inequality. The exact rational tenth-
power check proves its coefficient exceeds 11/10 without rounded powers.

Every subwindow term shares the already reviewed lower bounds
A0>.82e, K_n>1/4 and L_W>3/2. Multiplication into the sum of T_n is
therefore valid and gives
S_sub>(41/50)*(1/4)*(3/2)*(11/10)*(48/329)=4059/82250>6/125.
The same fixed finite index sets retain the earlier logarithmic derivative
bound below -15/4, while the other middle terms have negative derivatives.
Consequently S_mid,theta<-(15/4)S_sub<-9/50. No derivative of a lower
mass inequality is taken; it is combined with the separately established
per-term derivative inequality.

The independent Fraction producer replay passed all four checks and
returned sorted JSON SHA-256
d8feac07160dcb91e74983e0fab45daf5ae8e593e62474f43396afa358bc0656.
Its checks agree with the proof; the analytic power-sum argument remains
a separately reviewed input as the output explicitly states.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M13_MIDDLE_STRENGTHENED.md | 5f2391e0e39a52ea73486fafb628997955670896dcbf849fadb81424b454c101 |
| proofs/m13_middle_strengthened.py | 02977a1ae9654efd9c161c3a8144af53190a70f65cbff89957202eccc62bf9d8 |

No earlier proof or scientific producer was modified. Full F derivative
and complete W index coverage remain outside this component approval.
