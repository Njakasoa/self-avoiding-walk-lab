# Independent scoped M11 and M12 closure review

Verdict: the reviewed M11 phase-component package and M12 noncancellation
package pass independent checker replay and canonical provenance checks.
These are component results. Full F_N monotonicity, zero existence and
uniqueness for all missing indices, and complete W coverage remain OPEN.

The final M11 smooth note restores the explicit plus sign between the
quotient terms in its log-r upper bound. I compared it directly with the
preserved historical note: this is the only changed line. The intended
sum was already present in the independent derivation and unchanged
Fraction code. The final canonical proof hash
15e8c64e5d554a12eb40b68ef0b724d2aead52042779516fce9e78628f180f07
is now approved in an appended table in M11_SMOOTH_PHASE_REVIEW.md;
the earlier table and historical file remain intact. No producer or
canonical payload was changed to repair this documentation provenance.

I independently executed both checker functions. M11 validates its three
component replay results and reviewed source hashes; M12 validates the
noncancellation scalar replay, scientific/wrapper hashes and open scope.
I separately compared all 23 M11 inputs and all 17 M12 inputs against
both their metadata SHA-256 values and their frozen Git bytes. Every
comparison passed:

- M11 source freeze: ed131f9a743493bafae2659c1a648d62da39cf07.
- M12 source freeze: a7c6fb5f63c98a864ff42bdd51984a1d1b9f4240.

Both canonical payload hashes agree with their metadata and with the
prior independent pre-freeze replay hashes. The checker comparison also
confirms object equality with fresh wrapper replay. The code/analytic
reviews therefore correspond to the current canonical source bytes.

| Artifact | SHA-256 |
|---|---|
| results/m11-phase-v1/payload.json | 4f0db5f348ab7ef9dced62274068df04173cce2d42276b339daf8f3cf23daa30 |
| results/m11-phase-v1/metadata.json | afdfe19b84d07e896f15774c9ba17883760da44af80a4202d1bd8a98e5f5f116 |
| independent M11 checker output | 8de892d79ffae0c6f4f24f632976f1d559e2c556f4975832b983946d874c8987 |
| results/m12-noncancellation-v1/payload.json | 8eb9952fbed02e222772dd8d4942b0a75e9e1c3113a9f5b4bb5967b5f6685a8e |
| results/m12-noncancellation-v1/metadata.json | 5ebcb0eede164cc5f8afec3cfe05b8af857ba77fa210290c1df4da0acdc3be42 |
| results/m12-verification.json | d5839dcca5ebcf1a60640dd9333b7d95fc29a5fa774315f700b0059bb63bbf12 |

The root M12 verification file matches the independent sorted checker
output byte for byte. The M11 root file needed regeneration after the
proof-hash addendum; its final comparison is recorded below.

Accepted scope: M11 bounds directed, regularized-weight and smooth-factor
phase contributions and proves a negative logarithmic derivative for the
positive post-crossing summand only through n<=60N. M12 proves
F=0 implies 1+P<-2 throughout the stated N>=32 real sector. M12 supplies
no roots and no multiplicity information. Neither package resolves the
pre-crossing, boundary and distant-tail derivative obligations or the
remaining finite-to-asymptotic index gap. No novelty claim follows.

Final comparison: regenerated results/m11-verification.json has SHA-256
8de892d79ffae0c6f4f24f632976f1d559e2c556f4975832b983946d874c8987,
identical to the independent checker output. Final scoped closure: PASS
for both packages, with full W coverage explicitly OPEN.
