# M3 prudent-ramp formula audit

Status: independent transcription and bounded analytic audit. This file does
not claim non-D-finiteness of the irreducible series. The finite interval
certificates in `proofs/m3_prudent_intervals.py` are separate and have the
same finite-only status.

## Inputs and provenance

The primary source is the locally archived Bacher--Beaton paper,
`papers/bacher-beaton-2014.pdf`, pages 834--835 (Propositions 14 and 16) and
page 836 (Theorem 17). The audit was run from repository commit
`4a324867c950e8cd27470277cfe36dcfe238916b`.

Input SHA-256 values at audit time:

| input | SHA-256 |
|---|---|
| `papers/bacher-beaton-2014.pdf` | `04205e9fafa5330cb518e4c22a3db6f5677cddc915342fae83acbe076039b2c0` |
| `proofs/M3_PRUDENT_CANDIDATE.md` | `8adbaed3ac604dd83ccd06a2a79e1a0bfd8ffc3aaca5983877a6cbbe4ba28014` |
| `experiments/m3_prudent_singularity_probe.py` | `71722e6841ad87127847adcfdc1bca8ab815ea7b706db8734ea1c356bd30c072` |
| `proofs/m3_prudent_reference.py` | `2fbd8c664395d45a0e53cda74b840d2d2abda26e7ce4b57bda6d479fb03bd500` |
| `NORMALIZATION.md` | `37849ff3ddc245d187c1418a75f4d2a65d438c1b181a3effa25dbfe0d5741ec7` |
| `NEXT.md` | `afe5e3886826802e4420f87ef63fecd71cb5f5db923153006304a595d5e1dd8a` |

## Proposition transcription

Let

\[
a(t,v)=1-tv+t^2+t^3v,
\qquad
U(t,v)=\frac{a(t,v)-\sqrt{a(t,v)^2-4t^2}}{2t},
\qquad q=U(t,1).
\]

The script's

```text
2*t/(a + sqrt(a*a - 4*t*t))
```

is exactly the same branch by rationalisation. It is the branch with
`U(t,v)=t+O(t^2)` at the origin, hence the unique formal power-series branch
specified in Proposition 14. Choosing the other square-root sign would give a
non-power-series branch and is not what the paper uses.

I compared every factor in the two displayed propositions against a rendered
copy of the PDF:

* Proposition 14 is implemented as
  `P=q*(1-t*t)/(1-t*q) + q*sum(A(q**(2*n))*prod(B(q**(2*k))))`.
* The numerator of `A` is
  `(q-t)*(1-t*t)*(U(v)*(1-t*q) -
  (q*(q-t)+t*(1-q*q)*U(v))*U(v*q*q))`.
* The denominator of `A` is
  `(1-t*q)*(1-t*U(v))*(1-t*U(v*q*q))*
  (t*q-(q-t)*U(v))`.
* `B` has the paper's positive prefactor `q*(q-t)**2` and the numerator
  `t-(1-t*q)*U(v*q*q)`.
* Proposition 16 has the paper's first term
  `t**2*q**2*(1-t**2)/(1-t*q)**2`, the same product of `B` factors, and the
  factor `(q-t)` in the numerator of `A_tilde` (not its reciprocal).
* The hook numerator has the paper's minus sign before the second bracket and
  the factor `1-2*t*U(v*q*q)`.

Thus I found no transcription error in signs, factors, or the physical kernel
branch.

## Pole equation and numerical consistency

Writing `u_l=U(t,q^(2*l))`, the script locates zeros of

\[
h_l(t)=tq-(q-t)u_l.
\]

Theorem 17 instead writes

\[
\frac{(q-t)(u_l-t)}{t^2}=1.
\]

These are exactly equivalent because

\[
(q-t)(u_l-t)-t^2=(q-t)u_l-tq=-h_l(t).
\]

The first six computed pole locations were

```text
0.4030317167626847758719577215333983498723563446605519978918696354861974
0.4133628121140054810343813184129976898700100625346356097822719147167418
0.4139311096070432045048018468730333190236638786749639375507749872493883
0.4140743248627061071278763586785091581942039900650412669563026100383479
0.4141309168541322898069386723882069869129703489489003948551949396216105
0.414158899776721914892489468606815828559197334414145731072748852944927
```

The first five roots of the numerical equation `P(t)=-1` lie respectively
between consecutive entries above, at the centers recorded in the candidate
file. The doubled-term probe reproduces the listed hook values. These are
analytic-continuation evaluations; they are not tail-certified by that probe.

## Independent geometric count check

The direct enumerator applies the paper's NE-prudent condition (the forward ray
in the attempted step contains no visited vertex), requires positive height,
requires the endpoint to be on the north/east boundary, and then tests the
paper's ramp and hook definitions. For a hook, the shared endpoint of the
`{N,W,...,W}` prefix is retained when testing `omega \\ omega*`, so the
subsequent suffix vertices must have height greater than 1. It gives, through
length 12,

```text
P:      0, 1, 2, 4, 9, 20, 46, 108, 257, 615, 1478, 3567, 8641
P_tilde:0, 0, 0, 0, 1, 3, 8, 20, 49, 120, 294, 721, 1768
```

At `t=1/10`, these truncations are

```text
P_<=12      = 0.125160177111
Ptilde_<=12 = 0.000140648378
```

The kernel evaluation with 300 summands gives

```text
P            = 0.125160179886968604228244031429023043701030649709...
Ptilde       = 0.000140648952859901624524784982231723186758009924...
```

The positive differences are consistent with omitted positive coefficients;
they are not, by themselves, a rigorous error bound for the kernel sum.

## A bounded residue-sign observation

This gives a concrete partial result for the proposed interlacing route. For
real `t` in the Theorem 17 interval, set

```text
C=q-t, D=1-t*q, u=U(t,q^(2*j)), w=U(t,q^(2*j+2)).
```

On the physical branch, `0<w<u<1/t` and `0<q<1`. The numerator of the `A`
summand apart from the positive factors `C*(1-t^2)` is

\[
F=uD-[qC+t(1-q^2)u]w.
\]

Since `w<=u`,

\[
F\ge u[D-qC-t(1-q^2)u]
  =u(1-q^2)(1-tu)>0.
\]

At a pole `t=t_l`, `h_l=0` gives `u_l=tq/C`. Let

\[
\phi(x)=\frac{(1+t^2)x-t-tx^2}{t(1-t^2)x},
\]

so that `phi(U(t,v))=v` on the relevant branch. A direct simplification gives

\[
\phi\!\left(\frac{t}{D}\right)-q^2\phi\!\left(\frac{tq}{C}\right)
 =\frac{qt^3(1-q^2)}{C(1-t^2)D}>0.
\]

Because `phi` is increasing on the physical branch, this proves
`u_{l+1}<t/D`, and hence the numerator
`G_l=t-D*u_{l+1}` of `B_l` is positive. Also `u_j` decreases with `j`, so
`h_j=tq-C*u_j` increases with `j`; at `t_l`, `h_j<0` for `j<l` and
`h_j>0` for `j>l` once the Theorem 17 ordered roots are used.

For completeness, the signs of the preceding product factors can also be
checked at a pole. Since `u_l=tq/C`,

\[
G_{l-1}=t-Du_l
      =-\frac{t^2(1-q^2)}{C}<0.
\]

For `j<l`, `u_{j+1}>=u_l`, so `G_j<0`; together with `h_j<0`, this makes
every preceding `B_j` positive. Thus the part of the iterated sum beginning at
index `l` has a positive singular numerator: the `A_l` numerator is positive,
and the remaining tail has positive `A_j` and `B_j` numerators/denominators
for `j>l`.

If the iterated tail is analytic and convergent in a neighbourhood of `t_l`,
and if `h_l` itself has a simple zero there, the endpoint signs (`h_l>0` near
the origin and `h_l<0` near `sigma`) give `h_l'(t_l)<0`, so the resulting
residue of `P` is negative. Those local tail and simple-`h_l` conditions are
the extra analytic steps that this audit does not promote to a theorem: the
fact that Theorem 17 states a simple pole for `P` does not, by itself, prove
which individual denominator supplies its order or provide the required local
factorisation. Direct high-precision residues for `l=0,...,5` are all negative:

```text
-0.04882237442097773222
-0.00087445045560069135
-0.00016068996379856356
-0.00005463390974500738
-0.00002473274698055145
-0.00001321753370619491
```

This supports the sign/interlacing mechanism, but the quoted paper theorem and
the finite calculation do not automatically supply the local factorisation at
every index, or a uniform all-index proof.

## Exact remaining obstruction

If all listed poles have the same residue sign and no additional real
singularities occur between them, the intermediate value theorem gives a root
of `P(t)+1` in every interval `(t_l,t_{l+1})`. The interval script now certifies
the first five such roots and certifies `1+P_tilde>0.36` on each corresponding
small bracket. Neither fact proves the all-index statement.

At a zero `r_l` of `1+P`, equation (5) gives

\[
P_I=(P-\widetilde P)/(1+P).
\]

The common poles of `P` and `P_tilde` are removable in this quotient by the
known pole structure, but the new zeros of `1+P` produce a genuine pole only if
`1+P_tilde(r_l)\ne0`. The current numerical lower bounds are finite and local;
there is no proved uniform lower bound for every `l`, and no proof that a later
zero cannot be cancelled. This is the precise unresolved step needed before a
non-D-finiteness claim. The analogous weakly-prudent bridge series has another
rational combination and needs a separate cancellation argument.

No finite check, doubled precision, or doubled summand count changes this
classification.
