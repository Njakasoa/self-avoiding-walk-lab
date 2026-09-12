# W — proof and evidence dossier

Date: 12 September 2026. Status: **complete proof accepted at the internal
mathematical-draft gate**. This is AI-assisted internal review, not external
peer review. Publication priority remains **UNRESOLVED**.

The result concerns exactly the two-sided weakly prudent bridge generating
function of Bacher–Beaton (2014):

\[
 W=\frac{I}{1-I},\qquad I=4J-2D_I-t,
 \qquad J=\frac{P-H}{1+P}.
\]

**Theorem established in the reviewed draft:** this analytic germ W is not
D-finite. The argument constructs infinitely many genuine poles converging
to \(\sigma=\sqrt2-1\). It uses the cited BB2014 formulas and continuation
theorem and the previously reviewed critical-product foundations. It does
not transfer non-D-finiteness through an arbitrary rational quotient.

## Proof and completion audit

The complete argument is [W_NON_DFINITE.md](proofs/W_NON_DFINITE.md).
Its historical candidate header is superseded by this acceptance record;
the reviewed mathematical bytes have been retained unchanged.

| Requirement | Authoritative evidence and outcome |
| --- | --- |
| Identify zeros of the correct denominator | Section 1 and `w-identities-v1`: exact identity \(I-1=F/(1+P)\), where \(F=(3-t-2D_I)P-4H-(1+t+2D_I)\). |
| Control the partially directed term | Section 2, independent [directed-ramp proof](proofs/W_DIRECTED_RAMPS.md), and symbolic recurrence checks: positive summands, local complex normal convergence, harmonic critical divergence, hence \(D_I\to1\). |
| Prove phase-uniform limits | Section 3 extends the Gamma-product estimates to \([4/5,9/10]\): all small Gamma arguments and sine denominators remain separated from zero, the post-crossing amplitude changes sign, and the same integrable crossing bound and exponential tail apply. |
| Certify opposite signs | `w-critical-v1` recomputes all four critical integrals using 384-bit outward integer intervals, 2048 rectangles and 16-bit power enclosures; strict opposite F-limit signs pass. |
| Exclude cancellation and non-holomorphic I | Section 4 gives \(1+P_0<-2.26\) uniformly. Thus eventually \(1+P<-2\); P, H, D_I and I are holomorphic at the selected F zeros, where I=1. |
| Obtain infinitely many distinct poles | Section 5 uses the intermediate value theorem on every sufficiently late disjoint phase band and \(W=-1-(1+P)/F\). Continuation attaches to the original germ. Infinitely many finite poles contradict a polynomial-coefficient linear ODE. |
| Independent mathematical and arithmetic review | [Astra analytic review](proofs/W_ASTRA_REVIEW.md) accepts the full argument and independently replays the symbolic identities and exact certificate. [Final review](results/w-final-review.md) checks integration, all four receipts and retained numerical failures. |
| Preserve failures and separate numerics from proof | [Finite exploration](proofs/W_PHASE_EXPLORATION.md), `w-phase-v1` and `w-phase-fine-v1` retain all 34 tested cases. Small-index signs and the finite directed-term correction are explicitly reported below. |

The certified limit enclosures are

\[
 F_0(4/5)\in[0.99180337,1.05700564],\qquad
 F_0(9/10)\in[-0.23240630,-0.19788695].
\]

The exact upper-bound enclosure for \(1+P_0\) has upper endpoint
\(-2.26608430\). These certify limit signs and separation only; the
analytic proof supplies the uniform passage to finite, sufficiently large N.

## Frozen computations

Scientific source commit: `9a63181dc11100fa4dfccdea510650976383ffb3`.
Proof SHA-256:
`351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a`.

Each receipt includes input hashes, output hashes, exact command, parameters,
UTC, runtime and process memory. Every recorded input matches both its frozen
commit and the current source bytes. The dirty-worktree flag records notes
and new outputs; the driver rejects any unfrozen scientific input.

| Receipt | Scope | Runtime |
| --- | --- | ---: |
| [w-identities-v1](results/w-identities-v1/metadata.json) | Exact quotient identities and directed recurrence checks, plus bounded numerical controls | 0.49 s |
| [w-critical-v1](results/w-critical-v1/metadata.json) | Full exact limiting-sign certificate | 2.92 s |
| [w-phase-v1](results/w-phase-v1/metadata.json) | Independent direct formulas, 20 finite cases, N=8,16,32,64 | 36.63 s |
| [w-phase-fine-v1](results/w-phase-fine-v1/metadata.json) | 14 additional finite cases, N=32,64 and phases 0.84–0.90 | 35.93 s |

The critical payload SHA-256 is
`ab5cbc0caf0f24f5b32e877668e87cc2d4d75cd830c62123ad450711f0c7ed6c`,
identical to the separately reproduced reviewer output. All four receipts
passed input/output hash verification. Existing regression suite:
**54 tests passed in 10.06 s**. New Python modules compiled successfully;
the exact checker rejects Python `-O`, which would disable assertions in
the inherited interval engine.

To generate fresh receipts from these committed scientific sources, choose
new output IDs (existing receipts are never overwritten):

```bash
.venv/bin/python -m experiments.w_research_batch identities w-identities-replay
.venv/bin/python -m experiments.w_research_batch critical w-critical-replay
.venv/bin/python -m experiments.w_research_batch phase w-phase-replay
.venv/bin/python -m experiments.w_research_batch phase-fine w-phase-fine-replay
```

## Retained finite failures and limitations

At phase 0.80, the direct finite F evaluations are approximately
\(-0.273335,-0.108665,+0.019735,+0.122345\) for N=8,16,32,64.
At phase 0.90 they remain negative. Thus the limiting endpoint pattern fails
at N=8,16. In the finer sweep F remains negative throughout 0.84–0.90,
even though substituting D_I=1 gives a diagnostic crossing near 0.87.
The exact identity

\[
 F-F_{D_I=1}=2(1-D_I)(1+P)
\]

explains why that substitution materially changes the finite computation.
All 34 finite cases have negative 1+P. None of these floating-point checks
certifies an infinite tail or a finite pole. Truncation drift compares values
serialized to 32 significant digits; a zero drift is agreement at that
displayed precision. The numerical time budget is cooperative, not a hard
process limit. These diagnostics do not replace any analytic proof step.

No effective first index N_0, uniqueness, simplicity, residue estimate or
exact unrestricted square-lattice connective constant is asserted. External
review and a broader priority audit remain future work; see
[W priority checkpoint](references/W_PRIORITY_NOTE.md). The original M3/M4
manuscript remains at its previous J-only scope. This acceptance records the
W research freeze on branch `codex/w-bridges`; subsequent public-snapshot
status is documented in the repository README.
