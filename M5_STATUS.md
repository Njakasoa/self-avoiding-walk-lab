# M5 — quantitative W poles

**Completed at the internal research-draft gate.** External peer review and
publication priority remain open. The new M5 work is local; the public
GitHub snapshot has not been changed. Full evidence: [M5_ACCEPTANCE.md](M5_ACCEPTANCE.md).

- Uniform directed law: 1-D_I=sigma/logN+O(log^-2N), with explicit
  error31/log²N for N>=2^108.
- Uniform moment and phase-derivative errors: O(N^-1/20).
- Logarithmic phase displacement: theta_N=theta*-C_shift/logN+O(log^-2N),
  theta* in [.8695,.8720], C_shift in [.38696091,.44166261].
- Eventual unique simple pole in each phase band; residue
  C_res/N³+O(N^-3/logN), C_res in [-.00167097,-.00146400].
- Explicit sufficient existence/noncancellation index N0=2^(10^120).
  This enormous bound is not an effective uniqueness/simplicity threshold.
- Calibration32/64/128/256 and preregistered holdout512 completed. Both
  fixed-tolerance holdout comparisons pass. The failed finite extrapolation
  of the asymptotic coefficient is preserved.
- Six source-frozen receipts and independent review reports verified;
 54 regression tests pass. Existing J/W proof sources remain unchanged.

Next research: sharpen the directed additive constant and the second
logarithmic phase term; reduce the existence threshold to a useful range;
make uniqueness and residue error bounds effective.
