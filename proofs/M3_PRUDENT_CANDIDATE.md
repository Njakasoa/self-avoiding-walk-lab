# Research candidate: non-D-finiteness of irreducible prudent ramps

Status: OPEN PROOF ATTEMPT. This is not an accepted M3 theorem, and it does not
authorize a M4 publication claim. Primary source: Bacher–Beaton2014,
https://www.nicholasbeaton.com/papers/BB2014.pdf, archived locally. Sections4.1–4.2
explicitly leave non-D-finiteness of the irreducible-ramp series and weakly prudent
bridge series unresolved in that article. The bounded later-literature audit is in references/M3_TARGET_AUDIT.md; no later resolution was located, which does not establish novelty.

## Exact reduction

Use the source's notation: P counts NE-prudent ramps, H counts its hook-ramps,
and J counts irreducible NE-prudent ramps. Equation(5) gives

    J(t) = (P(t) - H(t)) / (1 + P(t)).

Theorem17 supplies infinitely many real simple poles a_l of P and H accumulating
at sigma=sqrt(2)-1, with a_l defined using the algebraic kernel U and q=U(1).
All these common simple poles of P are removable in the quotient J: multiplying numerator and denominator by t-a leaves a nonzero denominator equal to the residue of P at a. Merely quoting
Theorem17 does not prove J non-D-finite. The potential new poles lie where
P(t)=-1 and H(t) differs from -1.

Sufficient new lemma to seek:

1. For every l there is r_l in(a_l,a_(l+1)) with P(r_l)=-1.
2. At such a selected root, 1+H(r_l) is nonzero.

Then J has a singularity at every r_l, giving infinitely many singularities at
distinct finite points. A D-finite germ over characteristic zero satisfies a
linear ODE with polynomial coefficients, hence has only finitely many possible
finite singularities. Thus the lemma would prove J non-D-finite. This does not
automatically prove the corresponding weakly prudent bridge series non-D-finite:
its additional rational combination with the partially directed series can
cause further cancellations and needs its own argument.

One possible route to(1) is to prove that the residues of P at consecutive a_l
have the same sign, so P has opposite infinite limits at the interval endpoints.
The all-index residue sign and hence existence of the zeros are now proved in proofs/M3_PRUDENT_INTERLACING.md, using a local holomorphic-tail argument and the source's simple-pole classification. A possible strengthened target
for(2), suggested only by computation, is 1+H(r_l)>1/3 for all l. It remains a
conjecture, not a measured universal inequality.

## Initial falsifiable evidence

The root transcribed Propositions14/16 into
experiments/m3_prudent_singularity_probe.py using mpmath. These are numerical
analytic-continuation evaluations, not rigorous interval enclosures. Increasing
the series from700 to1400 terms and precision70 to100 digits gives consistent
values at the first five numerically located roots:

| l | r_l, approximate | 1+H(r_l), approximate |
|---:|---:|---:|
| 0 | 0.41257508666590646 | 0.410934837870692 |
| 1 | 0.41381169333386277 | 0.383968683619009 |
| 2 | 0.41403636149110697 | 0.374788292591698 |
| 3 | 0.41411430354223307 | 0.370116572712377 |
| 4 | 0.41415020038700697 | 0.367274514589828 |

Largest observed hook-value difference in this doubled-term check is about10^-35.
This is an observed stability check, not a tail error bound. The finite checks
neither establish infinitely many poles nor eliminate an eventual cancellation.

An independent geometric enumerator proofs/m3_prudent_reference.py gives ramp
coefficients through length12:

    0,1,2,4,9,20,46,108,257,615,1478,3567,8641,

and hook coefficients:

    0,0,0,0,1,3,8,20,49,120,294,721,1768.

At t=1/100, the numerical kernel values exceed these truncated sums by positive
amounts below the elementary nonbacktracking tail bound
(4/3)(3t)^13/(1-3t). This checks transcription and convention at small t; the
kernel's own numerical truncation is still not certified by this comparison.

## Needed before a theorem or publication

- Verify the primary formulas independently, including physical branches of U.
- Derive a rigorous tail bound away from the known poles to certify a finite
  initial set of root/noncancellation checks.
- Prove an all-index noncancellation statement (the interlacing part is now supplied), or find
  a counterexample and retain it.
- Check later literature for a solution of the2014 question.
- Obtain independent proof scrutiny and Astra review. M4 waits for these gates.

The weighted quotient and ladder results remain supporting explorations. Their
known-method character is not used to manufacture a contribution while this
main proof remains open.

## Exact finite singularity certificate

`proofs/m3_prudent_intervals.py` replaces the initial floating probes by exact
outward dyadic intervals (384 fractional bits). Every arithmetic operation
rounds endpoints outward using integer division. Square roots use integer square
roots with an upward correction for the upper endpoint. Division rejects any
interval containing zero.

For each of the five displayed centers c, the closed rational interval
[c-10^-20,c+10^-20] has P(left)+1<0 and P(right)+1>0. The enclosure of H+1
on the entire interval is strictly positive (lower bounds exceed 0.36).
The intervals are disjoint. These checks imply at least five distinct
singularities of J, conditional on the audited BB2014 formulas and meromorphic
continuation theorem. They do not imply non-D-finiteness.

For clarity, the tail is bounded, not guessed from the last term. At iteration
N, all later v=q^(2n) lie in [0, upper(q^(2N))] because 0<q<1. Interval
substitution in A(v), H-summand(v), B(v) gives uniform absolute upper bounds
M_A, M_H, beta. The checker accepts only beta<1 and bounds the two remaining
sums by |product_(j<N) B(q^(2j))| times M_A/(1-beta) and M_H/(1-beta).
It adds symmetric outward tail intervals before testing signs. This holds
uniformly on each root bracket, establishes continuity there, and checks all
possible denominator zeros by interval rejection. The existing meromorphic
continuation theorem then ensures that a zero of 1+P has finite order; the
nonzero numerator -1-H makes that zero a non-removable singularity of J.

This finite certificate is a research checkpoint. The all-index noncancellation statement
remains open, and the certificate has passed independent arithmetic/formula
review in results/m3-astra-review.md. Canonical frozen-source replay records its inputs. No M4 manuscript has been started.
