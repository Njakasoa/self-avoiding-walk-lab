# Independent review of the M13 distant-tail derivative bound

Status: PASS for |S_tail,theta|<1/1000, where the tail is over integer n>60N, integer N>=32 and theta in[.8,.9]. This is an absolute component bound, not a full F derivative sign.

## Analytic audit

The phase inequalities give eN>29/200, eN<.17 and8.7<(60N+1)e<11. The inherited real secant positivity and r<=exp(-e) bound K_n by exp(-ne) on this entire ray.

The reflected Gamma formula has positive sine factors. Its arguments b+1 and n-a exceed1 even at N=32. Wendel's inequalities therefore apply directly, without the old a>=200 restriction. The upper bounds (b+1)/(n-a)<1/56 and beta/(n-a)<1/2000 are strongest at N=32. Because the base is below1, beta>.7 gives the correct upper power. The sine multiplier bound uses positive lower and upper trigonometric estimates. These yield T_n<.151 uniformly throughout the tail.

The inverse-kernel relation gives u-t<v*t*(1+t)<v, so u<.4145. Each tail V1 and R upper enclosure in the ledger follows by separately increasing its positive factors and decreasing its denominators. The positive combined gap allows multiplication by these upper bounds; dropping positive2delta from the subtracted coefficient increases L. The resulting L<2 is valid on the whole tail.

The bare logarithmic derivative identity has S_n positive on both sides of the crossing. In the theta<=.85 case, the first pre/post terms are at most125/8 and400/51; the post k>=2 factors are bounded below by(.575k)(.925k). In the theta>=.85 case the first terms are at most2000/221 and25/2, and the remaining post factors exceed(.55k)(.9k). Adding the pre reciprocal-square bound5/3 and the post bound from sum_(k>=2)k^-2<2/3 verifies both displayed ledgers and S_n<27.

For H_n, absolute values give at most12.5+1+log N from the pre side, and1.25+(10/9)log n from the post side. Thus59/4+(9/4)log n is a valid upper bound. The substitution log n=log x_n+log(1/e)<=x_n+1/e, followed by1/e<7N, gives the stated beta-harmonic average. Its coefficients decrease with N, so N=32 controls the uniform ledger.

The all-mesh factor estimate7.071+.18je is justified by M11's factorization and variance argument before its finite-window cutoff; only the later replacement of .18je by1.836 required j<60N. The new tail argument retains the linear term. The absolute weight ledger additionally controls the previously favorable h,C,A0 terms. In particular, the displayed h quotient bound is below50, the t partial is positive and below200, and 0<(log A0)_e<1/e implies the allowed2/N absolute bound. These justify the new14/N estimate rather than incorrectly taking absolute values of the old one-sided11/N conclusion.

The normalized geometric moments are bounded by12 and146 using ep/(1-p)<1 and e^2p(1+p)/(1-p)^2<3. The averaged logarithmic derivative is663317/28000<119/5. The exact factor A0=J(1-p) cancels the geometric normalization. The positive degree18 exponential partial sum then proves the final strict1/1000 bound.

For each fixed N, e is bounded away from zero uniformly over the closed theta interval. The positive summands and their theta derivatives admit a constant times a polynomial in n times exp(-c_N n) majorant, with c_N>0. The harmonic logarithm is included in that polynomial bound. The Weierstrass test therefore supplies uniform convergence of the differentiated series and justifies differentiating its sum. No convergence uniform in unbounded N is needed for this step; the final numerical allowance itself is uniform in N.

## Arithmetic replay

Independently ran `.venv/bin/python -m proofs.m13_tail_bounds`: all34 exact checks PASS. Stdout SHA256: `a9bcfa20cf89e327a543e6316ef69aac3b4ebf61726697641ae6eb7daced511b`. The final rational upper bound is1348812365824000000000000000000/1349525612617437793687516180938219<1/1000. No point scan or old large-a Gamma bound enters this conclusion.

## Final source approval

Observed repository HEAD: `8f8176b8039c518455ea5a1ec284564f4f1ea108`; actual reviewed bytes are pinned below. The released note repairs markup and now states explicitly the uniform-convergence justification audited above. Its inequalities and the producer are unchanged. No material findings remain.

| Path | SHA256 |
|---|---|
| proofs/M13_TAIL_PHASE_BOUND.md | 6601ca6f1e6e1bcb8c30fcb3b3a3539b7555b4945a23a33ca3253df66b77cbde |
| proofs/m13_tail_bounds.py | 12039e0314c7fb7b86ba92e18501cc6dcd3730b0218bc7fd732262472660b07f |
