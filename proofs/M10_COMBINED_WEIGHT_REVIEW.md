# Independent review of the positive combined W weight

Verdict: PASS for the structural lemma in M10_POSITIVE_COMBINED_WEIGHT.md.
For every N>=32 and theta in [.8,.9], the combined weight satisfies
L_W(u)>V1(u)/100>0 along the complete physical kernel ray and decreases
with the ray coordinate x at fixed e and delta_D. This does not establish
the sign of a phase derivative or close any missing-index coverage gap.

## Input domains and directed bound

The M5 phase inverse applies for N>=20 with e<=.01 and s_g<.17.
Hence e=s_g/(N+theta)<.17/32<1/180 for N>=32. The M5 physical root
bound sigma-t<=e^2/8 is valid on the larger domain e<=.1, and the M6
directed remainder holds for e<=.01. Neither is being used beyond its
proved domain. The directed additive constant margin c_D>3/4 is the
frozen coefficient certificate, independent of an eventual pole theorem.

Since 1/sigma>12/5 and 100e<5/9, the remainder yields
D_R>(12/5-5/9)log(1/e)+3/4. The proposed exponential majorant is
correct: the tail starting at 1/24 has successive ratios at most 1/5,
so exp(1)<87/32<11/4, and (11/4)^5<180. Thus log(1/e)>5 and
D_R>359/36, giving delta_D<36/395<.1. No directed-summand monotonicity
is needed.

The bounds .4142<sigma<.4143 imply t>.414 using e<1/180 and the
physical root bound. Also q>359/360. The function tq/(q-t) increases
in t and decreases in q on the positive denominator domain, which
justifies the two independent endpoint substitutions yielding
.706<u_h<.71. All denominators remain positive throughout the ray.

## Algebra and sign

Write h=u_h. Directly from the displayed formulas,
V2=f(h)*V1+f(u)*dd/C. Moreover
L1/dd=h*(1-tu)/(1-h), so
dd/(dd+L1)=(1-h)/(1-tuh).
These identities give exactly the claimed ratio
V2/V1=f(h)+f(u)*(1-h)/(1-tuh).
For fixed t,h its second term is strictly increasing in u, since f
increases and the positive denominator decreases. The lower bound R_min
uses u>=t>.414, h>.706 and h<.71 correctly, with positive numerator
lower bounds and denominator upper bounds in each factor.

An independent Fraction replay gives
R_min=4681056404117904500/4027005197519687537
and
4*(.414)^2*R_min-(1-.414+.2)
=22015644255147517323/2013502598759843768500
>1/100 (approximately .010934003397218056).
The strict ratio margin therefore gives L_W>V1/100.

The first divided-difference term dd is strictly increasing in u, and
L1 is constant at fixed t,h, so V1 increases in u. Both factors in
V1*[4t^2*(V2/V1)-c_W] are positive and increasing; their product is
therefore increasing in u. The physical kernel U(t,exp(-x)) decreases
with x. This proves the claimed monotonicity only with the other
parameters held fixed.

Substitution of P=B1+Q sum z_n V1 and
H=t^2*(B2+Q sum z_n V2) into the exact denominator identity gives
F=c_W*B1-4t^2*B2-(3+t)+2delta_D-Q sum z_n L_W,
including the sign of the combined sum. If the separately proved
z_n<0 condition holds, Q>0 makes that sum contribution positive.
The note correctly treats that condition separately and makes no
claim about the total phase derivative, whose factors all vary.

## Provenance

Observed source commit: 05eb99a804ee2df99f05c0f1106a19db2532c794.
All rational inequalities above were independently replayed with Python
Fraction arithmetic. This arithmetic corroborates the analytic derivation;
it does not replace its domain or monotonicity arguments.

| Source | SHA-256 |
|---|---|
| proofs/M10_POSITIVE_COMBINED_WEIGHT.md | 9801fb62426a4d88730c31a19febfdbb5c10f9e2edb7f904eaea54bdd2d66b2a |
| proofs/M5_DIRECTED_LOG.md | fcf18e907607e185cb8dba7e4c25c58c8df3aa5088027429fc33d86677c9cf1f |
| proofs/M5_DIRECTED_REFINED.md | 08668a0ddbba107c2f56cc88e0d5f1b549c9ddec92490f4d35ba5f4e4005e38a |
| proofs/M6_DIRECTED_CONSTANT.md | b45599ada46df5d992f81b142b5285ce062f02d04ae02234e76a21afab4caab3 |
| results/m6-coefficient-v1/payload.json | 8b17975deacb8d46f6a4ef7a1a17bcbac5a6e9e973574b52ebf4056ba56d14a1 |

No scientific source file was modified by this review. No finite scan,
phase-derivative conclusion, full-coverage claim or novelty claim is part
of this approval.
