# Finite-memory upper certificates (known construction)

State = a self-avoiding suffix with m edges, translated to its first vertex.
An extension may not revisit any vertex of that suffix, then the oldest vertex
is forgotten. All ordinary SAWs are accepted. Accepted words may self-intersect
after memory loss, so the inclusion goes in the upper-bound direction.
All length-m suffixes are included, including dead-end and transient states.

D4 acts on states and commutes with extensions. For an orbit representative,
count each directional extension into its destination orbit; keep multiplicity.
This makes an equitable quotient: continuation counts are identical within
orbits. A transition count is not merely a Boolean adjacency entry.

For a nonnegative integer adjacency A, positive integer vector v and rational
U=p/q with q>0, qAv≤pv implies A^k v≤U^k v. Comparing 1 with a positive
multiple of v bounds all extension counts by a constant times U^k. Thus μ≤U.
No irreducibility assumption or floating eigenvalue computation is required.
The full-length initialization factor is finite and disappears under nth roots.
The generator uses v=(A+I)^t 1, and the verifier checks all inequalities exactly.

Increasing memory shrinks the accepted language. Its asymptotic growth rates
are nonincreasing, though loose finite-iteration certificates need not be.
Parity makes forbidding an odd-length return redundant on the square lattice;
this is a known structural control, not a novelty claim.

This is a small reproduction of the finite-memory strategy, not reproduction
of the historical best bound or the full optimized Pönitz–Tittmann computation.
