# Independent review of uniform real-sector noncancellation

Verdict: PASS. For every N>=32 and theta in [.8,.9], any zero of F
satisfies 1+P<-2. The same inequality holds wherever F>=0. This proves
noncancellation at such zeros; it proves no zero exists and gives no
count or multiplicity. Full W index coverage remains OPEN.

The M10 beta strip places a and b in the same integer strip, so every
bare factor is positive. The reviewed real secant argument gives K_n>0
on this domain, while the exact scalar denominator gives z0<0. Hence
z_n<0. For fixed positive e the full recurrence approaches a ratio r^2<1,
and the rational weights are bounded along the physical ray. The two
positive weighted series therefore converge absolutely. In particular
the V1 sum is finite and strictly positive, so it is valid to normalize
its terms into probability weights. This makes Rbar a weighted average
of V2/V1 and proves the strict Rmin/Rmax bounds, rather than assuming
that a ratio of sums has the same bounds without checking signs.

The M10 lower combined-weight gap gives ell>.07. Its upper bound follows
from cW>1-t>=1-t_h, the ratio maximum and t<t_h. Independently replayed
exact arithmetic gives ell_upper approximately .5931778611992468<.6.

The scalar I384 box contains every physical parameter pair, including
all correlations as an overbound. C,D,-gq,1-h and 1-th are positive
before division; other denominators are those same guarded quantities.
The formulas for B1 and t^2B2 match the exact regularized moment
identities. The independent replay produced the outward intervals
approximately B1 in [-.66733649,-.45552312], t^2B2 in
[-.53456294,-.47956422], and Zmin in [.30503608,.42243610].
The actual certificate consists of the exact dyadic endpoints, not these
readable decimal enlargements. It proves 1+B1>0 and Zmin>.3.

The direction of the Rbar substitution is essential and correct:
1+B1>0 and t^2>0 make -t^2*Rbar*(1+B1) decrease with Rbar.
Thus replacing Rbar by the larger Rmax yields a lower bound for Z.
Consequently Z>=Zmin>.3. No sign is inferred for 1+P before this step.

Substituting S=B1-P in the moment formulas gives
F=-ell*(1+P)-4Z exactly. I also verified this identity independently by
symbolic expansion with t,delta,Rbar,B1,B2,P as independent variables.
At F=0 it implies 1+P=-4Z/ell<-4*.3/.6=-2; for F>=0 the same
conclusion follows with a non-strict intermediate inequality. Source-pole
exclusion and local analytic continuation are inherited from the real
phase strip and convergent tail. The resulting numerator separation
prevents cancellation in the meromorphic W quotient at any zero.

Independent command: `.venv/bin/python -m proofs.m12_noncancellation_bounds`.
It passed with sorted JSON SHA-256
8eb9952fbed02e222772dd8d4942b0a75e9e1c3113a9f5b4bb5967b5f6685a8e.
The checker correctly states scalar-only scope; the averaging and analytic
convergence are supplied by the proof and this review.

| Reviewed source | SHA-256 |
|---|---|
| proofs/M12_UNIFORM_NONCANCELLATION.md | b615a6e4a11273526bb6f89779fe1e1a7c7f32bef7f6a341d73decd851ef2fb4 |
| proofs/m12_noncancellation_bounds.py | a97217a7c154c45ca5f49e26106c2f7535be37be67a7158be0460891da40b994 |

No scientific proof or producer was changed by this review. The result is
separate from the M11 receipt and asserts neither full F monotonicity nor
existence/uniqueness at unlisted indices.

## Wrapper and checker mechanism

The canonical wrapper validates the M10 structural receipt and pins 17
inputs, including the interval engine, exact moment formulas, M10 scalar
and ratio lemmas, the reviewed M11 real secant argument, earlier root and
product notes, receipt/provenance code and locked dependencies. Its payload
replay independently matches the producer output hash above. It retains
explicit existence-and-uniqueness-open scope and rejects optimized execution.

The checker compares the canonical payload to a fresh wrapper replay,
validates current scientific/producer/wrapper hashes against this review,
and requires both the -2 numerator allowance and the NOT PROVED
existence/uniqueness marker. This mechanism is approved for source freezing
and later canonical verification. No canonical receipt was created or
checker release run attempted during this pre-freeze review.

| Reviewed source | SHA-256 |
|---|---|
| experiments/m12_noncancellation_batch.py | c7b30834af5fb6f5657bc332d9da6f118263614c4d769c6f48dceb30ff75dd26 |
| proofs/check_m12.py | d0658886fb1f0a6667ffb4a2f6ce0d57914334e987ebdc51af0acb5489ca03f1 |
