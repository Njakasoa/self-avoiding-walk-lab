# Code archaeology — 2026-09-12

Luna explorer returned a read-only primary-source audit. No external code was
executed, imported or relicensed. Implementations in src/ are new reproductions.

| Source | Artifact / normalization | Availability and limitation |
|---|---|---|
| [OEIS A001411](https://oeis.org/A001411), [b-file](https://oeis.org/A001411/b001411.txt) | rooted oriented infinite square SAWs, n=0…79 | plain n/count data; first 29 values cross-checked by explorer; license not presumed for snippets |
| [Conway–Enting–Guttmann](https://arxiv.org/abs/hep-lat/9211062) | finite-lattice connectivity method, n≤39 | primary algorithm description, executable not located |
| [Jensen 2004](https://arxiv.org/abs/cond-mat/0404728) | square c_n through 71 | algorithm/paper; not runnable code audit |
| [Jensen 2013](https://arxiv.org/abs/1309.6709) | improved future-connectivity TM, n≤79 | algorithm/paper; not locally reproduced frontier |
| [Jensen GitHub](https://github.com/IwanJensen/Self-avoiding-walks-and-polygons) | Fortran/OpenMP finite-domain walks/polygons | no LICENSE located; branch WCAS(H) data are NOT A001411 (starts 1,12,322) |
| [SAWdoubler](https://webspace.science.uu.nl/~bisse101/SAW/) | C length-doubling package, examples 3D | paper identifies LGPL; square adaptation needed; not run |
| [Pönitz–Tittmann](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r21) | finite memory automata; k4≈2.8312,k6≈2.7756,k8≈2.7445 | pseudocode and values; no executable located |
| [Jensen bridges](https://arxiv.org/abs/cond-mat/0409381) | strict-min/weak-max, Kesten renewal, lower 2.625622 | exact modular TM, length250/span15 reported; no source executable audited |

No data from finite squares may be substituted into infinite-lattice c_n tests.
Our memory m corresponds to maximum forbidden loop length m+1; odd loop lengths
are redundant by bipartiteness. Our 5/36/272-state m3/5/7 matrices use a simple
D4 quotient and reproduce the displayed historical k4/6/8 rates, not historical
state-minimization performance.
