# M8 finite derivative certificates for the six frozen M7 brackets

Status: **finite candidate certificate, pending independent review**. This note
specifies the derivative mechanism and the scope of
proofs/m8_finite_derivatives.py. It is a finite result for the six M7
brackets only. It does not fill intervening indices or prove a whole phase
band statement.

The M7 receipt already supplies, on each bracket, opposite endpoint signs for
the denominator numerator F, a complete real tail, and the strict whole
bracket sign 1+P<0. M8 supplies the missing strict monotonicity:

    F_t(t) < 0 on each of the six M7 brackets.

Together with the M7 endpoint signs, this gives exactly one real zero in each
bracket. The local holomorphy argument in M7_FINITE_TAIL.md applies to these
source-pole-free brackets, so the strict derivative gives a simple zero in t.
The M7 sign 1+P<0 then makes the zero a noncancelled W pole.

## Frozen inputs and exact domains

All arithmetic uses the M7 I384 type: a closed dyadic interval [L,U] with
L,U in 2^-384 Z. Operations round down at the lower endpoint and up at the
upper endpoint. Square roots use integer square-root bounds and logarithms
use the 192-term atanh series with its positive analytic remainder. The only
finite inputs are the six rational seeds and widths already frozen in
proofs/m7_finite_poles.py:

    N       half-width in t
    32      1e-20
    64      1e-21
    128     1e-22
    256     1e-23
    512     1e-23
    1024    1e-24

For a bracket T=[t_-,t_+], the jet variable is (T,1). Every positivity,
negativity, and nonzero-denominator assertion is made on the complete
interval, rather than at its seed center. The frozen M7 source hashes are:

    proofs/m7_finite_poles.py  3712829fbf510e558e9215c7219731b40678ca9525e36387bb1f9d528f912c26
    proofs/M7_FINITE_TAIL.md   89869ff06633e9a9daa17ca63f848d47fcf3ba5b5c18aee1ee48b151347e48d7
    results/m7-finite-v1/payload.json
                                75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f

The payload is the endpoint-sign and numerator-sign receipt; M8 does not
replace it with a numerical residual.

## First-order interval jets

For a jet X=(x,x'), the exact first-order rules are:

    (X+Y)'       = x' + y'
    (X*Y)'       = x'*y + x*y'
    (1/X)'       = -x'/x^2
    (sqrt(x))'   = x'/(2*sqrt(x))
    (log(x))'    = x'/x

The value part of each rule is evaluated by I384, so no machine floating point
enters the derivative. Square-root and reciprocal guards prove that their
value intervals exclude zero before these rules are used. The kernel and
regularized weights are propagated from

    U(t,v) = 2*t / (a + sqrt(a*a - 4*t*t))
    a       = 1 - t*v + t*t + t*t*t*v

    C       = q - t
    u_h     = t*q/C
    f(u)    = u/(1-t*u)
    D_d     = 1/((1-t*u)*(1-t*u_h))
    L1      = f(u_h)/(1-u_h)
    L2      = f(u_h)^2/(1-u_h)
    V1      = (D_d + L1)/C
    V2      = ((f(u)+f(u_h))*D_d + L2)/C

Thus the finite prefix of the exact recurrence is differentiated directly:

    z_0       = 1/g(q)
    z_(n+1)   = z_n*r*g(u_n)/(g(u_n)+delta)
    u_n       = U(t,q^(2n))
    g(u)      = t-D*u
    E         = 1-q^2
    delta     = t^2*E/C
    r         = q*C/D

The cutoff is the same exact mesh used by M7:

    m = ceil(4*2^384 / epsilon_-) + 1,     epsilon = -log(q^2)

Here epsilon_- is the lower endpoint on the full t bracket. The M7 real
checks give g(u_m)>0, 0 <= g(u_n) <= g_inf=t^2*q, and
0 < z_(n+1)/z_n <= R=r^2 < 1 for n >= m.

## Directed tail derivative

The directed term is

    D_R = sum_{k>=0} t*q^k/(beta + gamma*q^(2k))
    beta  = (1-t-t*q)/(1-q^2)
    gamma = q*(t-q*(1-t))/(1-q^2)

Both beta and beta+gamma are positive on every frozen bracket. Let m_D be
the smaller of their lower endpoints. For a tail beginning at K>=1 and
0<q_+<1, set

    S0(x,K) = x^K/(1-x)
    S1(x,K) = x^(K-1)*(K-(K-1)*x)/(1-x)^2

The value remainder is bounded by

    0 <= D_R - D_R,K <= t_+/m_D * S0(q_+,K).

Put q'_+=sup|q'|, beta'_+=sup|beta'|, gamma'_+=sup|gamma'|, and
gamma_+=sup|gamma|. Differentiating each summand and taking absolute values
gives the complete derivative tail bound:

    E_D(K) = (S0(q_+,K) + t_+*q'_+*S1(q_+,K))/m_D
           + t_+/m_D^2 * (
               beta'_+*S0(q_+,K)
             + gamma'_+*S0(q_+^2,K)
             + 2*gamma_+*q'_+*q_+*S1(q_+^2,K)
           ).

The factor q_+ in the last term converts q^(2k-1) to (q^2)^(k-1).
The producer appends [0,E_D(value)] to the directed value and the symmetric
derivative box [-E_D(K), E_D(K)]. It chooses K by exact integer iteration
until both directed tails are at most 1e-18.

## Prudent tail derivative

For the post-cutoff ratio

    rho_n = r*g(u_n)/(g(u_n)+delta)

the derivative is bounded without differentiating a tail inequality. Over
0 <= v <= v_m=q^(2m), the code encloses the two kernel partials U_t and U_v.
Since

    |v_n'| = 2*n*q^(2n-1)*|q'|,

the exact integer guard

    (m+1)*q_+^2 <= m

makes n*q_+^(2n-1) decrease for n>=m. Therefore

    U'_+ = sup|U_t| + sup|U_v|*2*m*q_+^(2m-1)*q'_+
    G_+  = 1 + |D'|_+ + |D|_+*U'_+.

Using 0 <= g(u_n) <= g_inf and g(u_n)+delta >= delta_-,

    Lambda = |r'|_+ + |r|_+*(delta_+*G_+ + g_inf,+*|delta'|_+)/delta_-^2

is a valid bound for |rho_n'|. The differentiated recurrence gives, with
Z=|z_m| and Z'=|z_m'|,

    |z_(m+k)|   <= Z*R^k
    |z'_(m+k)|  <= R^k*(Z' + k*Z*Lambda/R).

The post-cutoff weight and derivative boxes use

    t in T, q in q(T), u in [t_-,u_m_upper], u' in [-U'_+,U'_+].

For V=sup|V_j|, V'=sup|V_j'|, Z_tilde=Z*R^K, and
Z'_tilde=R^K*(Z'+K*Z*Lambda/R), the absolute tail bounds are

    T_j(K)  = Q_+*V*Z_tilde/(1-R_+)

    T'_j(K) = ( Z_tilde*(Q'_+*V + Q_+*V') + Q_+*V*Z'_tilde )/(1-R_+)
             + (Q_+*V*Z_tilde*Lambda/R_+) * R_+/(1-R_+)^2.

For H the code additionally applies

    T_H  = t_+^2*T_2
    T'_H = t_+^2*T'_2 + |(t^2)'|_+*T_2.

The extra cutoff K is selected by exact binary search until all four prudent
value and derivative bounds are below 1e-18. The omitted moment values are
negative (z_n<0, V_j>0); their derivative boxes are symmetric, so the
resulting P and H jets enclose the complete sums.

## Certified finite result

An exploratory six-row evaluation reported these exact term counts. Its
JSON output was not retained: independent review found a Jet384 tail field
that the initial serializer did not handle. The serializer has been corrected;
a source-frozen canonical run is required before these claims are accepted.
The counts
are deterministic consequences of the 1e-18 targets and are included as an
audit aid; the recorded dyadic intervals are the certificate.

    N       m       prudent extra terms    directed terms
    32      821     3202                   26624
    64      1630    6679                   54784
    128     3247    13959                  113152
    256     6480    29169                  234496
    512     12947   60899                  485888
    1024    25881   126983                 1006592

For each row m8_finite_derivatives.produce() records complete dyadic
intervals for F, F_t, P, H, D_I, all weight and derivative boxes, the directed
value/derivative tail, and the prudent value/derivative tails. It asserts the
strict upper-endpoint condition sup_T F_t'<0.

The run used .venv/bin/python without optimization:

    .venv/bin/python -m proofs.m8_finite_derivatives

The targeted jet and directed-tail oracle checks are diagnostic checks only;
they do not replace the displayed tail derivations. No N=2048 measurement or
new finite source was used, and the frozen M7 producer and receipt remain
unchanged.

## Finite residue enclosure

The companion wrapper experiments/m8_finite_batch.py verifies the frozen M7
receipt and exact equality of each rational t bracket. It checks the opposite
endpoint signs, source-pole exclusion, and the two independent whole-bracket
negative numerator boxes. At the unique zero w_N in that bracket,

    Res_(t=w_N) W(t) = -(1+P(w_N))/F_t(w_N).

Both quantities are enclosed by the jets on the entire bracket, and the
denominator excludes zero. Outward interval division therefore supplies a
rigorous negative residue interval; multiplication by the exact integer N^3
also gives its normalized enclosure. This formula uses the derivative in t,
so no phase-coordinate Jacobian is required.
