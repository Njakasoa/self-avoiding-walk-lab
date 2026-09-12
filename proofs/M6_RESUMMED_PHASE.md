# M6 candidate: a phase approximation containing all logarithmic orders

Status: conditional candidate. Uses the directed-constant theorem, the
accepted M5 moment rate, and the exact affine critical profile. It does
not replace the need for an effective threshold or finite validation.

Write L=logN and b as in M6_SECOND_ORDER.md, and set

 delta_hat(N)=sigma/(L+b).

The directed input D_N=L/sigma+c_D-log(s*)/sigma+O(logN/N)
gives delta_N-delta_hat=O(1/(N logN)), uniformly in theta.
Consequently the exact W denominator differs in C0 by O(N^-1/20) from

 F_hat_N(theta)=F0(theta)+2delta_hat(N)*(1+P0(theta)).     (1)

Use the affine formulas

 F0=C0+J B(theta),  1+P0=p0+post1*B(theta),
 p0=sigma-A*pre1,  J=(1-sigma)*post1-4sigma²*post2<0.

Then the zero of (1) is explicitly specified by

 B(theta_hat_N)=-(C0+2delta_hat*p0)/(J+2delta_hat*post1).  (2)

For sufficiently large N the denominator in (2) is nonzero and the
right side approaches B(theta*). Since B is strictly increasing and
F0' is strictly negative, there is a unique solution theta_hat_N in
the W phase sector. Its derivative denominator remains separated from
zero. The exact theta_N and theta_hat_N are therefore related by

                theta_N=theta_hat_N+O(N^-1/20).         (3)

To justify (3), (1) has derivative (J+2delta_hat*post1)B', bounded away
from zero on the sector for large N. Evaluate (1) at the M5 exact root
and use the uniform denominator error and the mean-value theorem.
This avoids differentiating the directed remainder.

An optional trigonometric inversion is

 cot(pi theta_hat_N)=[cos(pi eta)+A/B(theta_hat_N)]/sin(pi eta),

with the branch theta_hat_N in (eta,1). The branch is essential.
Formula (2), or bisection of the strictly monotone (1), avoids inverse
trigonometric ambiguity in a numerical implementation.

Expanding (2) in 1/logN recovers the first two coefficients of M6 and
also fixes every higher logarithmic coefficient. Equation (3) states
that the residual is ultimately smaller than every fixed inverse power
of logN. It does not give a finite-N error constant unless the relevant
effective moment and directed remainder bounds are inserted.

This approximation offers a better diagnostic than extrapolating a
straight line in 1/logN from small indices: all logarithmic terms are
retained before examining the algebraic residual. A reserved finite test
must still be preregistered before its evaluation.
