# Weighted baselines for later experiments (known facts)

Let nonnegative x,y be horizontal/vertical step weights, as in NORMALIZATION.
Every split at n is an injection into pairs of n- and m-step SAWs, with product
weights. Hence Z_(n+m)≤Z_n Z_m; Fekete gives μ(x,y)=inf Z_n^(1/n).
For positive weights, write x=e^a,y=e^b. Hölder's inequality makes
log Z_n(e^a,e^b) convex. The pointwise limit (1/n)log Z_n is therefore convex.
This proves log-convexity in logarithmic weights, not ordinary convexity in x,y.
Rotation gives symmetry; degree-n monomials give homogeneity. On an axis only
the two straight one-dimensional SAWs survive, so μ(x,0)=x.

D4 symmetry reduction is valid only for transformations preserving the weights.
For x≠y retain axis reflections/180-degree rotation (D2), or keep oriented states.
Using D4 on a weighted matrix without carrying orientation loses information.

Physical meaning: the exponential partition rate gives entropy/free-energy
contribution log μ per step in dimensionless units; the unweighted conformational
entropy is k_B log μ per monomer up to subextensive corrections. Fugacity z
converges for z<1/μ. No statement about unproved critical exponents follows.

These are proof sketches of standard facts, to be checked independently before
claim-level elevation. They propose controls for an anisotropic engine, not a
new identity and not a claim of ordinary convexity.
