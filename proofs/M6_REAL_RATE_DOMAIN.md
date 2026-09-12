# Domain clarification for the M6 real moment rate

The frozen M6_REAL_MOMENT_RATE.md states e<=10^-8 in its header and
uses the M5 effective weight estimates in Sections4--5. Those inherited
estimates were stated on e<=10^-10. To avoid extending their domain
implicitly, the accepted application of the moment bound (T) in this
research step is restricted to

                         0<e<=10^-10,

with every hypothesis (P) also required. All the proof's elementary
estimates remain valid on this smaller domain. The new sharp product
lemma may have the larger domain e<=10^-8, but the common domain used
for aggregation is the smaller one above.

The candidate N0=10^46 has e_N<10^-46 and thus satisfies this restriction.
The threshold arithmetic and claimed existence scope are unchanged.
No claim about the moment bound on (10^-10,10^-8] is needed or accepted
by this domain clarification. The frozen source and its earlier review
are retained for auditability.
