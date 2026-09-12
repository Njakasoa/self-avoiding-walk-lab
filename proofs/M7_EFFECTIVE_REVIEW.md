# M7 effective uniqueness review

Status: **ACCEPTED at the internal mathematical research-draft gate** for
the analytic statement specified below, at the source hashes in this report.
This is an independent agent review, not external peer review or a priority
finding. Canonical receipt provenance and final integration replay are
separate closure obligations owned by the root.

The accepted statement is: for every integer N>=10^120, the restricted W
series has exactly one simple noncancelled real pole in its phase band
[.8,.9]. The reviewed proof supplies a holomorphic joint moment norm below
10^10 on a fixed complex neighborhood, and hence joint phase-derivative
error below .009. It does not lower the accepted M6 existence threshold
10^46, establish finite uniqueness at N=32,...,1024, or cover all intermediate
indices. No assertion concerns the unrestricted square-lattice SAW constant.

## Independent analytic audit

The inverse construction is a contraction on |e|<=1/N, using the accepted
M6 root disk and Cauchy bound |s_g'|<20. It is uniform in the fixed phase
rectangle, hence holomorphic. Comparison with the real inverse e0 gives
|e-e0|<e0² and epsilon=Re(e)>.07/N. This is enough to keep |t|<sigma:
the even expansion has a real deficit of order e0² and a complex
perturbation only of order e0³. The explicit polynomial discriminant
bounds preserve a positive real part along the compact ray, including
the initial critical square-root endpoint. The quotient comparison gives
the stated 500 sqrt(e0) bound without a nonexistent uniform derivative
of the square root at that endpoint.

The positive-coefficient Y identity supplies the global |U|<1 majorant.
All weight denominators are therefore separated by explicit complex
modulus inequalities. The phase coordinates exclude the m=0 source
zeros; nonzero periodic copies have an imaginary component of order N
that cannot be canceled by either phase coordinate. The scalar logarithm
of r gives |r|<exp(-epsilon).

The bare product domination is valid term by term: imaginary parts of the
denominator increase its modulus, while the numerator's correction has
logarithm bounded by half |Im(theta)|² times a convergent reciprocal-square
sum. The real comparison product is positive on both sides of its crossing.
Its harmonic-sum proof handles the extra N+1 factor explicitly, and the
resulting cusp envelope has exponent at most 3/4<1. The compact mass bound
uses epsilon consistently; it does not lose a factor |e|/epsilon.

For the smooth product, exterior denominators stay above .049 and .0009.
The kernel comparison, root displacement and delta/e estimate bound the
two first-order logarithm fractions and their remainders. In the crossing
region, the divided differences from M6 have positive real part, so their
analytic logarithms remove the apparent source crossing. Cauchy's derivative
bound on the half-width crossing tube is 4*10^10; it applies to the tiny
imaginary mesh displacement. The two regional estimates give

    Re ell_e(ne) <= epsilon psi(Re(ne)) + 2*10^13 e0 sqrt(e0).

Here psi<=0 is only a real critical statement. There are fewer than 5/e0
prefix factors, so the accumulated positive allowance is below 1/2 at
N>=10^120. This proves |Pi|<2 rather than assuming a complex extension
of the real sign R<=1. The same factor-count argument applies to Pi_m
for m=ceil(4/epsilon), since all of its factors have j epsilon<4 even
when m epsilon>4.

At m, |z_m|<12000 follows from the bare-product envelope and this prefix
bound. In the far kernel disk, Re g>.15 and |g|<.20, while Re delta is
positive to first order and Im delta is quadratic. Thus Re(delta/g)>0,
and the complete recurrence contracts by exp(-epsilon). The correct tail
is indexed by n-m. It gives the joint moment tail below 4.8*10^6 using
the scalar ledger, or below 2*10^7 using the looser bridge ledger. A common
cutoff 60N and uniform ratio exp(-.07/N) prove normal convergence without
assuming that a moving auxiliary cutoff suffices. The compact and boundary
masses then fit comfortably within the joint norm 10^10.

Cauchy's formula on radius .01 bounds the sum of second derivatives of
the two errors by 10^16. The accepted M6 real estimate, with B=10^12 on
its common e<=10^-10 domain, gives a joint real error below 2*10^-21.
An increment h=10^-18 chosen to stay in [.8,.9] gives derivative error
strictly below .004+.005=.009, including both endpoints. No real C0
remainder is differentiated.

The critical derivative margins are obtained from exact interval integrals
and the analytic monotonicity of the sine expression, not from finite
sampling of the phase band. The exact derivative identity in the transfer
note has all four correction terms and signs correct. Even the weaker
hypothesis joint derivative error<=1 gives F_N'<-1 using the directed
bound 30000/N and M6 numerator bounds. Opposite endpoint signs give a
zero, strict decrease makes it unique, and the nonzero phase-to-t derivative
makes it simple in t. The M6 uniform numerator separation rules out
cancellation.

## Arithmetic and integration checks

The reviewer ran the auxiliary arithmetic with `.venv/bin/python` and with
`-O`; outputs were byte-identical. The exact uniqueness transfer also
passed. In particular P0'(.8)<74.945 and F0'(.9)<-6.325, which support
the displayed whole-band margins 75 and -6. These decimals summarize
outward rational certificates and are not separate proof inputs.

The integration verifier and effective receipt wrapper were read. The
wrapper freezes the analytic notes, inherited inputs, arithmetic code and
provenance implementation. The verifier checks committed/current source
hashes, payload hashes, exact six-index phase/sign/tail conclusions,
regenerated effective arithmetic, reviewed source hashes, frozen legacy
sources, full exploratory/canonical equality, and the independent N32
row and original-versus-regularized moment overlap. Its optional full replay
flag accurately distinguishes a fresh producer replay from receipt checks.
Its inherited assertion checks are guarded against optimized execution.
The final canonical finite run is not being duplicated by this reviewer.

## Corrections resolved during review

The bridge was corrected to use epsilon consistently in its compact mass,
to start exponential decay at m rather than the noninteger cutoff 4/epsilon,
to use 200e0 for the delta/e allowance, and to use the half-tube Cauchy
constant 4*10^10. These changes preserve the stated threshold with ample
margin. The inward increment and a strict-versus-equal arithmetic display
were also clarified. No scientific blocker remains at the reviewed hashes.

## Provenance

Frozen scientific baseline: M6 `a7fa96f`. The source commit observed during
this audit was `fc445b368abd297d35b927ca348d2ceb8af72fcc`; several M7 proof
files were additions or revisions after that commit. The exact hashes below
identify the reviewed bytes; the final canonical receipt records the commit
that freezes them. Frozen M3–M6 producer/proof sources were not edited by
the reviewer.

| Reviewed source or output | SHA-256 |
|---|---|
| `proofs/M7_EFFECTIVE_DERIVATIVE.md` | `e79045816d8ec87313584ba8bc960ff09833e299071013c9cf84fae1903df7d1` |
| `proofs/M7_COMPLEX_SCALARS.md` | `53fa59586ba44673d5904190f4ee3fc556b826677c6053f6ddc08e5a82060c38` |
| `proofs/M7_COMPLEX_KERNEL_SECTOR.md` | `0c1b006aa6d202bc89345b9d0ba194ce8502c504497061007acdca548d59bfe3` |
| `proofs/M7_COMPLEX_PRODUCT_DOMINATION.md` | `c366bb558d128ecdeb8f43de5c1c261df1d1807f3559c6a5d50a76e1b796864c` |
| `proofs/M7_REAL_TO_DERIVATIVE.md` | `7e34ef6f8aeaf78cccce82a1aa6aae059ef09e676834de066649506ae6c685f5` |
| `proofs/M7_UNIQUENESS_TRANSFER.md` | `641806191be795952a15c2062f5e7a6e5f836f14a087768cb35f9e92bd1c24e0` |
| `proofs/m7_complex_boxes.py` | `aba67065b2b63a741d032f6a71cabbafdcee52f38aefc7a3e69929da93ea2cfb` |
| `proofs/m7_uniqueness_transfer.py` | `94701dd179348f267366d8f90efd014976d05d3aa2c45e9d6e428f12d11ab73b` |
| `proofs/check_m7.py` | `d0a0056db1e79afd8e415d243bdaef999266adb3d9ed31165062698cb14c5c74` |
| `experiments/m7_effective_batch.py` | `f958d7fce41c589ed9fc2c2f6c8a047e89f10f64461398d3fa1bb6454ee6214c` |
| `/tmp/m7-review-complex-boxes-final.json` | `f4561717052450e10f283c18b37b6e6f410c1b1b8b21f2f6754edf9bf3eb203d` |
| `/tmp/m7-review-uniqueness.json` | `abe372241ae59cc56e5c029357545e305264d847867ab7d9e0d18f9221a0a1c0` |

The final auxiliary output above was replayed after the metadata-only rename
from “missing input” to “required analytic input”; both normal and optimized
execution again matched exactly. Its analytic dependency is supplied by the
reviewed bridge. Temporary output copies are evidence, not substitutes for
the final canonical receipt and its provenance.
