# M6 signed product and resummed phase review

Status: **ACCEPTED at the internal mathematical-draft gate for product
Sections1--4 and the resummed phase transfer**, using the separately
accepted directed constant theorem.
Internal AI review only. No numerical prediction or threshold is certified
by this report.

## Signed real product, Sections1--4

The Y=v Phi_t(Y) rewrite is exact, and Phi_t has nonnegative coefficients.
Lagrange inversion therefore proves nonnegative v coefficients of U-t.
For t<sigma, the nearest positive kernel branch point is beyond1, so the
power series and its derivatives converge on the physical v interval.
Termwise differentiation shows g_e is increasing and concave. Its secant
slope decreases with the anchor, yielding F_e<=G_e because s_h<s_g.
Thus R_e<=1, including removable root values, and every finite smooth
product lies in(0,1]. The critical limit gives psi<=0 without a separate
normalization assumption.

The sign argument as written is on s>=0, so both secant anchors must lie
there. The intended near-critical e range satisfies this, whereas the
introductory unrestricted0<t<sigma formulation does not guarantee positive
s_h. Restrict the claim to the certified near-critical range, or extend
the concavity argument to the negative-s anchor. The former suffices for
all intended applications and is the requested clarification. The revised
introduction now explicitly assumes0<s_h<s_g for R_e and restricts its
application to the certified near-critical range. This correction has
been checked and closes the domain issue.

The exact inverse-kernel formulas for v_g,v_h are correct. Under
t(-e)=t(e), q(-e)=1/q(e), substitution gives v_g(-e)=v_h(e).
The logarithm branches coincide at the positive critical value, so
s_h(e)=s_g(-e) locally and eta_e is even analytic with
eta_e=eta+O(e²). This provides no numerical third-derivative bound by
itself; the note appropriately does not invent one.

The crossing and tail estimates in Section3 follow from the accepted
Gamma formulas and the exact product bound. In particular the tail starts
directly with T_n<20 and r^n<=exp(-ne); no previously huge prefactor is
needed. Section4's extraction B_real=10^42 fits the explicit M5 crossing
remainder4*10^41 e, exterior remainder10^40 e and Hölder constants.
The required modulus |psi| also fits that constant. The one-sided
exponential Lipschitz inequality converts logarithmic error to additive
product error without exponentiation. Its illustrative L>=1000 arithmetic
is consistent.

Section5's illustrative aggregation is deliberately **not reviewed or
accepted here**; root uses M6_REAL_MOMENT_RATE.md instead. No conclusion
about a final threshold follows from merely reading that section.

## Resummed phase transfer

The directed input gives sigma(1+D_N)=L+b+O(L/N), hence
delta_N-sigma/(L+b)=O(1/(N L)) uniformly. Combining this with the
accepted M5 moment error yields a uniform denominator errorO(N^-1/20)
relative to F_hat=F0+2delta_hat*(1+P0).

Because F0 and1+P0 are affine in B(theta), equation(2) correctly solves
for the B value at the approximate root. For large N its denominator
approaches J<0, and its target approaches the interior critical root.
The inverse function is therefore well defined in the W sector and its
derivative denominator is separated from zero. Applying the mean-value
theorem to F_hat at the actual M5 root proves the stated algebraic phase
error. No derivative of the directed remainder is required.

The optional inversion sign is correct:
A/B=sin(pi eta)*cot(pi theta)-cos(pi eta). Restricting the inverse to
(eta,1) selects the required branch. The approximation is analytic in
1/logN near zero, so its expansion determines every fixed logarithmic
coefficient. This is an asymptotic statement, not a uniform assertion
about arbitrarily high expansion order or a finite-N error constant.

The numerical value at512 is not part of this proof review. A reserved
1024 comparison still needs preregistration and separate validation.
The directed constant theorem has now passed the separate review in
M6_DIRECTED_REVIEW.md. Its effective remainder supplies the input used
above, lifting that condition for the non-effective resummed transfer.

Final accepted source SHA-256 values:

- Product note, Sections1--4 only:
  `a3b6b878102cfbe022aada6477c78c8641edc5d25b813ea7030f032fce96c522`.
- Resummed phase note:
  `47d7ff8a5e90b82a593e262cee5ec426a237e037c5e59cab94f02ad65197b301`.

No finite-N residual constant, improved threshold or validation result is
accepted by this report. Section5 of the product note remains outside its
review scope. Later changes to the accepted portions require reviewing
those changes.
