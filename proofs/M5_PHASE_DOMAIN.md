# M5: an explicit real phase threshold

Status: **exact interval certificate and analytic argument awaiting review**.
This quantifies only the real phase inverse and the directed-log error. It
does not supply the first index for W poles or the constants in the moment
rate theorem.

The elementary physical-kernel estimates in M5_DIRECTED_LOG.md give, for
0<=e<=1/100,

    sigma-e²/8 <= t(e) <= sigma,
    1-e/2 <= q(e)=exp(-e/2) <= 1,
    -1/400 <= t_e <= 0,     q_e=-q/2.

The derivative bound uses t_e=sinh(e/2)/F'(t), F'(t)<=-4 and
sinh(e/2)<=e. The closed inverse-kernel expression is

    d=1-tq,
    v_g=q(d-t²)/(d(1-t²)),      s_g=-log v_g.

Differentiating this rational expression logarithmically gives

    s_g'=-[q_e/q+(d_e-2t t_e)/(d-t²)-d_e/d
                                      +2t t_e/(1-t²)],
    d_e=-t_e q-t q_e.

The checker `proofs/m5_phase_domain.py` substitutes the full parameter
intervals, without sampling e. Outward 384-bit arithmetic gives conservative
decimal consequences

    0.1533 < s_g < 0.1670,
    0.3369 < s_g' < 0.3679,
    s_g-e s_g' > 0.1496,
    0.9264 < N e_N/s* < 1.0542    for N>=20, theta in [.8,.9].

Since a(e)=s_g/e has derivative -(s_g-e s_g')/e²<0 and tends to infinity
at zero, and a(1/100)<20, every N>=20 and theta in [.8,.9] has exactly one
solution e_N in (0,1/100). The last ratio bound follows from

    N e_N/s*=(s_g(e_N)/s*) N/(N+theta),
    200/209 <= N/(N+theta) <= 1.

In particular the coarser ratio interval [1/2,2] holds, and the checker
certifies -log s*+log2<3. Thus |log(1/e_N)-logN|<3 with explicit phase
threshold N_ph=20.

Combining this with the directed bound
|D(t(e))-(1/sigma)log(1/e)|<=80 gives

    |D(t_N)-(1/sigma)logN| <= C*=80+3/sigma.

The checker also verifies

    108 log2 > 2 sigma(1+C*),
    2 sigma²(1+C*) < 31.

Therefore the reciprocal error estimate is fully effective:

    |1-D_I(t_N(theta))-sigma/logN| < 31/(logN)²
    for every N>=2^108 and every real theta in [.8,.9].

The large index is an intentionally coarse sufficient bound for the directed
term alone. Finite W poles at much smaller N are compatible with it. It is
not an estimate of when the complete W argument first becomes valid.

All logarithms are enclosed by
log x=2 sum_(k>=0) y^(2k+1)/(2k+1), y=(x-1)/(x+1), with absolute geometric
remainder 2|y|^(2m+1)/[(2m+1)(1-|y|²)]. The helper resides in
`proofs/m5_critical_pole.py`; its use here requires no critical quadrature.
