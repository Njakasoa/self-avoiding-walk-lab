# Independent review of M13 pre-crossing mass bounds

Status: PASS for the stated mass bounds, for integer N>=32 and theta in[.8,.9]. This does not establish a pre-crossing derivative sign or a complete F phase derivative theorem.

## Analytic audit

Substituting h=tq/(q-t) in the inherited regularized weights gives exactly R(1)=1/(1-t) and V1(1)=1/[(1-t)(q(1-t)-t)]. The inherited positive, increasing kernel-ray weight therefore permits the endpoint u=1. The numerator increases in t and decreases in delta; the positive denominator decreases in t and increases in q on the stated box. Replacing t by .4143, q by359/360 and delta by a lower bound consequently gives an upper bound, with the correct quotient direction. The inherited increasing J(t), A0/e<J(t), and 0<K_n<=1 justify the remaining weight envelope.

For n>=1, T_n/T_(n-1)=(a-n+1)/(b-n+1). Direct substitution in Q_n=(n-a)T_n/(1-beta) gives Q_n-Q_(n-1)=T_n because a-b=beta. The explicitly assigned Q_-1 makes the same identity true at n=0. Thus the finite primitive includes both endpoints n=0 and n=N without an index shift. Positivity permits dropping -theta*T_N for the general bound; b+1=N+theta-beta+1<N+6/5 and 1-beta>.28 have the required directions.

The reference point is below sqrt(2)-1 and its certified epsilon lies in the inherited real inverse domain. Its a>64.9 places every target with32<=N<=64 below it in t. Strict directed monotonicity transfers the complete upper enclosure D_R<16 to those targets and proves delta_D>1/17. This is an analytic order argument for all those bands. The directed routine includes its geometric remainder after74752 positive terms; the displayed tail is a bound on the omitted sum, and its upper endpoint is added to the returned D_R upper endpoint.

The pre-crossing product T_N is exactly the product over l=1,...,N of(l+theta)/(l+v). Concavity gives the telescoping lower bound in the note. Its base exceeds(5/6)N>1, so lowering beta to.7 preserves a lower bound. Taking the positive tenth power reduces T_N/N>1/4 on N<=64 to the stated rational comparison. In the primitive numerator, 1-N/4<0 makes theta=.8 the correct upper endpoint; beta>.7 then yields .8N+1.1. Combining this with Ne<.17 and N>=32 gives the claimed restricted mass bound.

## Independent replay and provenance

Ran `.venv/bin/python -m proofs.m13_mass_bounds` independently: all10 checks PASS. Exact allowances are3651716165278632471/1185755220092887048 (approximately3.079654303) and65736008313894493353/33201146162600837344 (approximately1.979931897). Weight allowances are approximately5.898612177 and4.715469595. These decimals are summaries of exact rational results.

Observed source commit: `8f8176b8039c518455ea5a1ec284564f4f1ea108`. Assigned sources are identified by their actual bytes below, independently of commit inclusion. Complete stdout SHA256: `9ad698482964c4790e33369553c40b68e20818a6d9fb309ca4c988ec569f2a68`.

| Path | SHA256 |
|---|---|
| proofs/M13_PRE_MASS.md | b8a50734cbe6d36c9cc6f7b75ca0caa3022efa1a6a390d9251f7a4337509e513 |
| proofs/m13_mass_bounds.py | d4b4253487cdf6cd619a8d0bf116ed874fd1f8feacf9890c97ab66093a9161db |
| proofs/m7_finite_poles.py | 3712829fbf510e558e9215c7219731b40678ca9525e36387bb1f9d528f912c26 |

No material findings remain. The approved conclusions are S_pre<31/10 for all N>=32 and S_pre<2 for32<=N<=64, on the stated phase sector.
