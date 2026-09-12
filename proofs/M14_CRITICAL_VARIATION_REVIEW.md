# Independent review of M14 critical variation and kernel displacement

Status: PASS for the stated analytic components. No finite-e moment-error estimate or endpoint existence follows from them alone.

At the critical parameter, the exact scalar formulas give ug=h=eta, ug'=-1/4, h'=1/4. Symmetry and beta(0)=eta give sg'=eta/2 and sh'=-eta/2. The derivative of log(ug/h) is therefore-eta. For the difference log(1-u_e h)-log(1-u_e ug), dividing the difference by e and using a mean-value identity in its scalar anchor gives-u_0/[2(1-eta u_0)]. Only continuity of u_e is needed, because the scalar anchors coincide at e=0 and the limiting denominator is positive. This remains true at s=0; no critical U_t derivative is taken. The two exponential secants similarly give eta*m_a(s,c), including s=c through their integral definition.

The probability formula m_a=-E[v] lies strictly between-1 and0 for each finite s, and m_sa=-Var(v)<=0. It has variation at most1 over the half-line. Independently verified the identities A(1)=1+eta and A(sigma)=1-eta. Since u_0 decreases, A(u_0) has variation2eta. The triangle inequality thus gives TV(psi)<=3eta, despite the two nonconstant pieces having opposite monotonicity. The square comparison9/2<(17/8)^2 proves the claimed rational variation allowance; direct extrema give-(1+3eta)<psi<-1 and hence-25/8<psi<-1. The usual cellwise bounded-variation rectangle estimate sums to at most e*TV and includes the empty n=0 sum.

Direct differentiation of U_t=U*A_t/sqrt(Delta) confirms the exact displayed U_tv formula; an independent symbolic simplification also returned zero for the difference. On .414<=t<sigma, v in[0,1], B>=2 and Delta>0. B is largest at v=0,t=.414, while A_t and1-t^2 admit the independent lower endpoints used in the ledger. These choices validate the positive bracket allowance2837/1000. The use of.4143 in the rational bounds only widens the endpoints; it does not assume Delta positive above sigma.

Consequently U_t is positive and increases in v below the critical parameter. Integrating to T<sigma gives0<=U(T,v)-U(t,v)<=U(T,1)-U(t,1). Continuity as T increases to sigma yields the desired uniform comparison, without requiring an integrable derivative estimate to be asserted at the critical corner in advance. On the physical branch U(t,1)=q=exp(-e/2), so1-q<e/2. This covers v=0 and v=1 as well as every s>=0.

## Independent replay and source approval

Ran `.venv/bin/python -m proofs.m14_critical_variation`: all7 exact ledger checks PASS. Independently verified both endpoint A identities and the mixed derivative algebra with SymPy. Complete producer stdout SHA256: `c392f2357e52a321ec00e82bac566eaa452a14bde8f9cd0f5a4fa260cf84a3ba`.

Observed repository HEAD: `9a8f2120cd3c04875d877b33b58f521f8d547a56`. Approved actual source bytes:

| Path | SHA256 |
|---|---|
| proofs/M14_CRITICAL_VARIATION.md | 937af31f8da496cd7888e4bd95e9254418ff9d1d071505d935ad14c2534ed691 |
| proofs/m14_critical_variation.py | 156c6f85ed6a0bad6cc6fba3c6353a26ca213f274ba3ec5fd3a5e120a284466d |

No material findings remain. The finite-e factor remainder, Gamma mass control and weight perturbations are still needed for the intended moment approximation.
