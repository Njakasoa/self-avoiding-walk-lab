# Bridge renewal lower certificate (known construction)

Use NORMALIZATION.md: strict initial minimum and weak terminal maximum.
Concatenation translates the second bridge to the end of the first. All new
vertices have x strictly larger than that joining x-coordinate, so the result
is self-avoiding. A renewal index k is characterized by x_k=max_{j≤k}x_j and
x_j>x_k for every j>k. All renewal indices give a unique irreducible factorization.
Thus B=1+IB and b_n=Σ_{k=1}^n i_k b_{n-k}, with b_0=1.

Let I_N(z)=Σ_{k=1}^N i_k z^k. The freely concatenated finite dictionary is a
subset of bridges, hence SAWs. Its generating function is 1/(1-I_N(z)); its
positive root r of I_N(r)=1 is its radius, because coefficients are nonnegative
and the positive real pole cannot cancel. Therefore μ≥1/r. Rational lo,hi
with I_N(lo)≤1≤I_N(hi) give μ≥1/hi. These bounds concern the dictionary's root,
not an enclosure of the full unknown μ from both sides.

Direct geometric irreducibility and formal inversion must agree in tests.
A classical analytic positive control is the subset of partially directed
bridges: each block E followed by any monotone vertical run (possibly empty).
Its irreducible GF is z(1+z)/(1-z), so the concatenation growth is 1+sqrt(2).
These blocks are strict/weak bridges of span 1 and are all irreducible. This
proves the known lower bound μ≥1+sqrt(2). Finite dictionaries approach it from
below unless they include richer span families; the control is an infinite
analytic family, not inferred from a short numerical series.
