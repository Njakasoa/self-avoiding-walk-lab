# Performance policy

First compare identical counts on overlapping n, then runtime. Compile C++20
locally; no GPU or multi-day scale run. Actual benchmark JSON must record compiler,
source commit and input/output hashes via src/provenance.py before being treated
as a canonical experiment. Small filesystem probe in environment/audit.json is
not a physical SSD throughput characterization.
