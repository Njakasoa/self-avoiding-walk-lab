# Bounded public snapshot review

Reviewed scripts/export_github.py, scripts/check_public_snapshot.py, public README, rights/attribution metadata, publication/reproduce.py, NORMALIZATION.md, NEXT.md, M3/M4 acceptance, and the non-D-finiteness proof scope. Also inspected tracked filenames and the earlier privacy audit; did not read personal memory.

## Verdict

No blocking defect found in the publication exporter or public scientific claims, subject to the root's fresh exported-tree validation and the planned roadmap corrections.

- git archive HEAD produces a new tree without original Git metadata/history. Exclusions cover operational settings, instructions, personal memory, user briefs, machine audit, and downloaded paper/full-text copies present in the tracked inventory.
- Nonregular archive members and paths escaping the destination are rejected. Export refuses a nonempty destination. Scientific receipt bytes are retained, with README disclosure that old commit IDs/machine paths are historical and some historical gates cannot run in the public snapshot.
- README confines the theorem to J, explicitly excludes W and a square-lattice connective-constant result, and distinguishes internally reviewed analysis from computational certificates and external priority.
- The portable publication gate uses bundled frozen source hashes and does not require original Git history. Public root manifest excludes its mutable VALIDATION.json deliberately.
- MIT code/documentation scope, distinct manuscript/figure rights, and the OEIS fixture's separately attributed license are stated clearly. This review relies on the root's already completed primary-source OEIS license verification.

## Operational notes, not blockers

1. Export only includes committed HEAD. Commit the new README/license/metadata/scripts/roadmap before export; the inspected tracked-file listing did not yet contain these additions.
2. check_public_snapshot verifies every manifest-listed file but permits extra files and does not authenticate the manifest. Its printed claim correctly says that the listed snapshot files match SHA-256. Do not describe it as a privacy scanner, complete file-set validator, or third-party authenticity guarantee.
3. README's historical 54-test result is properly labeled historical. Root should record fresh snapshot test/reproduction results separately.
4. Initial roadmap text imposed an effective first index and simple roots for W, and blanket axis-swap symmetry for oriented ramps. Root has already assigned corrections: infinite noncancelled poles need neither effective N0 nor simplicity; oriented ramp exchange must be mapped geometrically before assumed invariant.

No external write or repository edit performed by this reviewer.

## Final roadmap review

Accepted final P1/P2/P3 corrections. P1 now makes effective N0, simplicity, and derivative lower bounds optional: infinitely many distinct zeros of 1-I at holomorphic points with I=1 supply nonremovable poles. P2 correctly obtains phase convergence from uniform convergence to the strictly increasing limiting profile, and F'(sqrt(2)-1)=-4 yields t(epsilon)=sigma-epsilon^2/16+O(epsilon^4), hence sigma-r_N~s_*^2/(16N^2). It no longer assumes a 1/N convergence rate across the integrable singularity. P3 distinguishes the axis-transported oriented class and starts at ratios 9/10,1,11/10. No remaining blocking scientific finding in the requested roadmap scope.
