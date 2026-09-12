# Independent review of the M13 uniform phase derivative integration

Status: PASS for the analytic integration and exact arithmetic. A frozen receipt and its independent verification remain separate integration obligations.

## Common domain and decomposition

Every component used here holds for integer N>=32 and theta in[4/5,9/10], with the same physical inverse e_N(theta), the same directed reciprocal delta_D, and the same regularized moments. Substituting P=B1-S and H=t^2(B2-Rbar S) into the exact denominator gives B plus the positive series with summand A0 T_n K_n L_W(u_n), with the signs displayed in the integration note. Thus the three index sets0,...,N; N+1,...,60N; and60N+1,... are disjoint and exhaustive. In particular n=0 is included once, and N is fixed while differentiating.

The reviewed tail proof supplies uniform convergence of the original and differentiated series for each fixed N on its compact phase interval. The finite pre and middle sums need no limiting argument. Consequently the component derivative bounds can be added to obtain the derivative of F itself. No limit uniform in unbounded N is needed, and no finite scan substitutes for a component theorem.

## Case split and exact margin

For32<=N<=64, the reviewed mass bound S_pre<2 and relative derivative bound103/(50N) give S_pre,theta<103/(25N)<=103/800. For integer N>=65, the other mass bound31/10 gives S_pre,theta<3193/(500N)<=3193/32500<103/800. There is no gap between64 and65 and neither argument assumes a sign for the pre derivative.

The boundary allowance is at most3/2560; the middle derivative is strictly below-9/50; and the tail absolute derivative is below1/1000. Their sum with103/800 is exactly-3141/64000=-.049078125<-1/25. The strict upper bound persists at all phase endpoints and throughout both index cases.

## Consequences and limits

The mean value theorem gives at most one zero on each complete phase band. Both a=N+theta and b=N+theta-beta remain strictly between N and N+1, so the source poles do not obstruct the inherited local analytic regularization. The phase map has a finite nonzero derivative in t at each physical point. Hence nonzero F_theta at a zero gives nonzero F_t there; local analyticity makes the zero simple. The reviewed M12 inequality1+P<-2 at every zero prevents cancellation in W=-1-(1+P)/F, giving a simple pole.

The accepted M7/M8 existence receipts for N in{32,64,128,256,512,1024} now imply uniqueness on each entire band, extending the previous narrow-bracket conclusion. Existing finite residue enclosures still concern the same unique poles. The separately accepted M9 endpoint theorem supplies existence for every integer N>=10^27. Neither the present negative derivative nor noncancellation establishes existence for any remaining index32<=N<10^27. The note states this limitation explicitly and does not exclude poles outside its phase sector. The full goal remains open pending missing existence coverage and receipt integration.

## Independent replay and approved sources

Ran `.venv/bin/python -m proofs.m13_combination_bounds`: all6 checks PASS. Stdout SHA256: `828440b7a8e67ac13403b6eee12f56120f1938db9771bd2e1405f94f64a4c1e2`.

Observed repository HEAD: `8f8176b8039c518455ea5a1ec284564f4f1ea108`. The actual approved source bytes are:

| Path | SHA256 |
|---|---|
| proofs/M13_UNIFORM_PHASE_DERIVATIVE.md | 36e69716d43dba04c18fd2855e2b2acd6df2bca1833023372c50f66339f4486b |
| proofs/m13_combination_bounds.py | 57234d89f0520708587b9619531c991d50e6ed43ffaefdd7f33fab66a70d8f8d |

No material findings remain. This review relies on the separately recorded analytic component reviews, rather than interpreting the arithmetic ledger as an independent proof of its input hypotheses.
