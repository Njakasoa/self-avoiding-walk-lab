"""Independent numerical checks for the M5 directed C1 estimate.

This script repeats the kernel inversion and the exact directed sum locally;
it does not import the proof or any earlier experiment.  The reported
theta derivatives use a high-precision centered difference, so they are a
diagnostic rather than part of the rigorous bound in the proof note.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 70
SIGMA = mp.sqrt(2) - 1


def kernel(t: mp.mpf, v: mp.mpf) -> mp.mpf:
    """U(t,v), the small root of the quadratic kernel equation."""
    a = 1 - t * v + t * t + t**3 * v
    disc = a * a - 4 * t * t
    return 2 * t / (a + mp.sqrt(disc))


def phase_coordinate(t: mp.mpf) -> mp.mpf:
    """Return the phase coordinate s_g(epsilon)/epsilon."""
    q = kernel(t, mp.mpf(1))
    u = t / (1 - t * q)
    v = (u - t) * (1 - t * u) / (t * (1 - t * t) * u)
    return mp.log(v) / mp.log(q * q)


def t_from_phase(N: int, theta: mp.mpf) -> mp.mpf:
    """Solve phase_coordinate(t) = N + theta below sigma."""
    target = mp.mpf(N) + theta
    lo = mp.mpf("0.4")
    hi = SIGMA - mp.mpf("1e-60")
    for _ in range(230):
        mid = (lo + hi) / 2
        if phase_coordinate(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def directed_sum(
    t: mp.mpf, tail_x: mp.mpf = mp.mpf(70)
) -> tuple[mp.mpf, mp.mpf]:
    """Return a partial sum and an explicit positive tail bound."""
    q = kernel(t, mp.mpf(1))
    eps = -2 * mp.log(q)
    Q = q * q
    s = 1 - Q
    alpha = 1 - t - t * q
    cutoff = int(mp.ceil(tail_x / eps))
    total = mp.mpf("0")
    for k in range(cutoff + 1):
        Qk = Q**k
        den = alpha * (1 - Qk) + (1 - t) * s * Qk
        total += t * s * q**k / den
    # For k >= cutoff+1, 1-Q^k >= 1-Q^(cutoff+1), giving this exact
    # geometric upper bound for the omitted positive summands.
    tail = (
        t
        * s
        * q ** (cutoff + 1)
        / (alpha * (1 - Q ** (cutoff + 1)) * (1 - q))
    )
    return total, tail


def directed_I(N: int, theta: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    t = t_from_phase(N, theta)
    eps = -2 * mp.log(kernel(t, mp.mpf(1)))
    D_partial, tail = directed_sum(t)
    return eps, D_partial / (1 + D_partial), tail


def centered_theta_derivative(N: int, theta: mp.mpf) -> mp.mpf:
    h = mp.mpf("1e-5")
    return (
        directed_I(N, theta + h)[1] - directed_I(N, theta - h)[1]
    ) / (2 * h)


def main() -> None:
    print("sigma =", mp.nstr(SIGMA, 18))
    print("theta    N       epsilon                 D_I                 tail bound       dtheta(D_I)       30000/N")
    for N in (20, 64, 256):
        for theta in (mp.mpf("0.8"), mp.mpf("0.85"), mp.mpf("0.9")):
            eps, value, tail = directed_I(N, theta)
            deriv = centered_theta_derivative(N, theta)
            bound = mp.mpf(30000) / N
            print(
                mp.nstr(theta, 3),
                f"{N:4d}",
                mp.nstr(eps, 12),
                mp.nstr(value, 12),
                mp.nstr(tail, 8),
                mp.nstr(deriv, 12),
                mp.nstr(bound, 8),
            )
            if not tail < mp.mpf("1e-9"):
                raise AssertionError("tail bound is too large for the diagnostic")
            if not abs(deriv) < bound:
                raise AssertionError("diagnostic derivative exceeded the proof bound")

    # Independent checks of the two scale inequalities used in the proof.
    for N in (20, 64, 256):
        for theta in (mp.mpf("0.8"), mp.mpf("0.9")):
            eps, _, _ = directed_I(N, theta)
            if not eps < mp.mpf(1) / N:
                raise AssertionError("phase inversion did not satisfy eps < 1/N")
    print("checks: phase epsilon < 1/N and all displayed derivatives < 30000/N")


if __name__ == "__main__":
    main()
