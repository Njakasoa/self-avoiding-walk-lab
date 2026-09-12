# Exact product form and an unproved critical scaling route

Status: exact algebraic identities plus a **formal asymptotic candidate**.
The scaling limit and connection across its singular point are not proved.
This note does not establish noncancellation or complete M3.

Use C=q-t, D=1-tq, E=1-q², h(u)=tq-Cu, g(u)=t-Du,
f(u)=u/(1-tu), u_n=U(t,q^(2n)), p_0=1 and p_(n+1)=p_n B(u_n).
The kernel relation implies CD=tq(1-t²).

## Exact moment and product identities

The two inhomogeneous summands simplify to

    A_n = C(1-t²)/(D*h_n) * [D*f_n-q*C*f_(n+1)],
    Ah_n = t²*C(1-t²)/(D*h_n) * [D*f_n²-q*C*f_(n+1)²].

For Y_j(u)=D(1-t²)f(u)^j/g(u), direct subtraction gives

    A_(j,n)=Y_j(u_n)-B_n*Y_j(u_(n+1))
             -t²*E*(1-t²)*f_n^j/(h_n*g_n),

where A_(1,n)=A_n and A_(2,n)=Ah_n/t². Summing telescopes. For fixed
0<t<sigma away from the known poles and any intermediate zero denominators,
the products decay geometrically as n tends to infinity. The resulting exact
identities are

    P = C/g(q) + sum W_n*f_n,
    H = t²*f(q)*C/g(q) + t²*sum W_n*f_n²,
    W_n = -q*t²*E*(1-t²)*p_n/(h_n*g_n).

An additional telescoping identity is

    sum W_n*(1-u_n) = -t*D²/g(q).

Indeed, with k=q*C²/D² one has h(u)-k*g(u)=C*E*(1-u)/D.
Writing z_n=p_n/g_n gives z_n-z_(n+1)=p_n*(h_n-k*g_n)/(h_n*g_n).
The endpoint at infinity is zero and z_0=1/g(q).
Intermediate g_n zeros can be handled by analytic continuation: for n>=1,
z_n=k*p_(n-1)/h_(n-1), which has no g_n denominator. The displayed
moment expressions thus have removable g_n singularities away from h poles.

More explicitly, let r=q*C/D and delta=t²*E/C. Then

    z_0=1/g(q),
    z_(n+1)/z_n = r / (1+delta/g_n),
    z_n = z_0*r^n * product_(j<n) (1+delta/g_j)^(-1).

The ratio notation assumes nonzero z_n,g_n; the equivalent rational recurrence
z_(n+1)=k*p_n/h_n supplies the removable cases. This is an exact reformulation
of the original product, not an approximation.

`experiments/m3_moment_identities.py` checks these rational identities exactly,
reducing by the quadratic kernel relation when needed. Identities involving an
infinite sum additionally use the fixed-t local convergence argument already
proved in the interlacing note; symbolic checking alone is not that argument.

## Formal critical differential equation

Set epsilon=-log(q²), and consider t tending to sigma=sqrt(2)-1 from below,
so q tends to1. Write v=exp(-s), u=U(sigma,v), d=1-sigma. Away from g(u)=0,
the exact logarithmic product increments formally give

    d log Z / ds = -1/d - sigma²/[d*(sigma-d*u)].

This uses -log(r)/epsilon ->1/d and delta/epsilon ->sigma²/d.
At the critical point, the inverse kernel is

    phi(u)=(u-sigma)*(1-sigma*u)/(sigma*(1-sigma²)*u),
    s=-log(phi(u)).

Consequently the proposed limiting equation is

    d log Z / du = (1-u)/(sigma-d*u) * phi'(u)/phi(u).

Its exact partial fractions are

    (2+sqrt(2))/(u-sigma)
    +sqrt(2)/(u-1/sigma)
    -(1/sqrt(2))/(u-1/sqrt(2))
    -(1+sqrt(2))/u.

Thus on either side of u*=1/sqrt(2) any solution of this formal equation is
proportional to

    (u-sigma)^(2+sqrt(2)) * (1/sigma-u)^sqrt(2)
    * |u-1/sqrt(2)|^(-1/sqrt(2)) * u^(-1-sqrt(2)).

The corresponding critical v* is 1/2+sqrt(2)/4. The local exponent1/sqrt(2)
is derived from the exact rational differential equation, rather than fitted
to data. This establishes what the formal limit would be, not that the actual
discrete products have this limit uniformly near the singular point.

## What this route still needs

The equation cannot determine the relative multiplicative constants on the
two sides of u*. Discrete factors crossing the zero of g carry precisely this
missing connection information. Near an interlacing root the cancellation of
large contributions to P fixes a connection condition. The behavior of H
then requires a controlled limit of a regularized moment, for example
H-t²*f(u*)*P. Merely integrating the formal equation separately on each side
would discard the decisive information and cannot prove noncancellation.

A viable theorem needs uniform product estimates away from u*, a rigorous
local discrete connection formula near u*, and remainder estimates for the
regularized moment at a sequence of actual P=-1 zeros. No such convergence or
connection theorem is asserted here. The finite asymptotic probe is intended
to falsify proposed scalings before attempting those estimates.
