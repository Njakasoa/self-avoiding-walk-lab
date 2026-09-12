# Independent review of the W boundary phase bound

Verdict: PASS for the boundary component. On N>=32, theta in [.8,.9],
the certificate gives -2<B<-7/5, -7<B_e<0 with delta held fixed,
and B_theta<6/(5N^2). This does not establish full F_theta negativity,
zero existence or missing-index coverage.

The physical boxes follow from the reviewed M10/M11 root and derivative
bounds: t is within 1/(8*180^2) of sigma, 359/360<=q<=1,
-1/(7*180)<=t_e<=0 and q_e=-q/2. Delta lies in [0,.07], enclosing
the strictly positive physical directed reciprocal. The independent
interval box safely enlarges correlations and contains every physical
pair and its derivatives. The endpoint e=0 is used only as a box limit;
the phase inverse transfer still assumes positive e.

Jet384 propagates whichever derivative is supplied; its name or earlier
use for t differentiation does not restrict it. Here the t and q jets
contain e derivatives, while the delta jet has derivative exactly zero.
The result is therefore B_e at fixed delta, as required. The C,D,-gq,
1-h and 1-th guards cover all rational denominators. B1 and t^2B2 match
the exact M12 formulas, including the sign of S0 and the extra t^2.
Substitution in B=(1-t+2delta)B1-4t^2B2-(3+t)+2delta is exact.

An independent producer replay passed all six guards. The B interval is
approximately [-1.98030300274,-1.40279725029] and its e derivative
approximately [-6.62156885121,-3.78401853926]. Exact dyadic endpoints
establish both strict margins; the displayed decimals are readability
allowances only. The same replay verifies 1+B1>0 and that both derivative
endpoints of delta_fixed are zero.

The chain rule gives B_theta=B_e*e_theta+2(1+B1)*delta_theta.
The directed contribution is nonpositive because 1+B1>0 and the
independently established delta_theta<=0. The product B_e*e_theta is
positive but bounded above by 7*|e_theta|<7e/N. Using e<.17/N yields
1.19/N^2<1.2/N^2. The note correctly drops the signed directed term
rather than estimating its absolute magnitude. No derivative of an
asymptotic enclosure is taken.

Independent command: `.venv/bin/python -m proofs.m13_boundary_bounds`.
Sorted JSON output SHA-256:
e47562ed9e579fdf195df3bc49c2b9ce43603991a14fef28a6edf6eb60cbe33a.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M13_BOUNDARY_PHASE.md | 742296c6c8a2892503f2054461c5220e158935e6062494651e7e08174e7b2d93 |
| proofs/m13_boundary_bounds.py | 909b95e419da54a6c35ea7c5e4a6af67db537da4914f8f6ed0f484f159972b8f |

All accepted M3--M12 sources remain untouched. This review edits only its
own report and approves no conclusion about the uncombined pre-crossing,
post-crossing or distant-tail contributions.
