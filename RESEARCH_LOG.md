# Research log

2026-09-12 — M1 bootstrap. Full original specification archived. No discovery
claim. Three actual Luna research/explorer tasks launched; root implemented
independent exact bridge geometry and finite-memory orbit quotient.

Exploratory smoke test (unfrozen source, not canonical experiment): m=1..6
state counts 1,2,5,13,36,98; certified displays 3,3,2.8311772073,
2.8311772073,2.7755911424,2.7755911424. Expected parity plateau is a known
control, not new mathematics. Direct irreducibles and renewal inversion
agree through n=10; finite bridge dictionary lower display 2.4963116582.
Canonical replay requires source commit, complete metadata and independent test.

Canonical source61b85b1: Python n≤14 and C++ n≤20 match OEIS. Shared n14:
Python1.1019s, C++0.00459s; C++ n20=1.1960s. Finite-box DFS, occupation TM and
all-vertex connectivity TM agree on seven boxes through3x4. Performance numbers
are single-run measurements, not confidence intervals. Local honeycomb test
passes all exact polynomial reductions and rejects the phase mutant.

Independent reviewer reproduced bridges through12; independent tester in progress.
Only input-validation issue found so far: Python bool silently treated as int by
automaton/bridge API. Corrected, with old artifacts still tied to their original
source. Negative finding retained; no mathematical result affected.

M1 accepted after independent Luna tester and Astra reviewer. Final canonical
validation at ebfed56:10passed/3.77s,31source receipt entries and4output payloads
verified. E1–E3 proposed only after acceptance. M2–M4 and the original scientific
success criteria remain open; no novel result or publication claimed.

Completion audit: previous goal turn PROGRESS; fresh scope check exposed literal
§8.2 optimization gap. Corrected with packed bits/canonical full-state memo.
All15 immediate items independently accepted. Exact mode results archived at
source8f25c4b; memo n12 about0.0663s/16156KiB vs direct0.0024s/3584KiB. This
negative performance result justifies opt-in memo, not a novelty claim.
