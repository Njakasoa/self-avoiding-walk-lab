"""Independent numerical check of the M6 directed additive constant.

The proof uses elementary estimates.  This script evaluates the exact
hyperbolic representation independently, keeps a positive tail bound, and
checks the original summand formula against the transformed one.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 60
SIGMA = mp.sqrt(2) - 1
C = 2 + mp.sqrt(2)
C0 = mp.log(4) - mp.digamma(C)


def t_from_epsilon(eps: mp.mpf) -> mp.mpf:
    """Physical solution of F(t)=2 cosh(eps/2), by bisection."""
    target = 2 * mp.cosh(eps / 2)

    def F(t: mp.mpf) -> mp.mpf:
        return (1 - t + t * t + t**3) / t

    lo, hi = mp.mpf("0.4"), SIGMA
    for _ in range(220):
        mid = (lo + hi) / 2
        if F(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def parameters(eps: mp.mpf) -> tuple[mp.mpf, ...]:
    t = t_from_epsilon(eps)
    q = mp.exp(-eps / 2)
    alpha = 1 - t - t * q
    beta = q * (t - q * (1 - t))
    z = -beta / alpha
    a = -mp.log(z) / eps
    return t, q, alpha, beta, z, a


def direct_sum(eps: mp.mpf, tail_x: mp.mpf = mp.mpf(50)) -> tuple[mp.mpf, mp.mpf]:
    """Exact hyperbolic partial sum and a positive omitted-tail bound."""
    t, q, alpha, beta, z, a = parameters(eps)
    s = 1 - q * q
    pref = (t / alpha) * mp.exp(eps * a / 2) * s
    cutoff = int(mp.ceil(tail_x / eps))
    total = mp.mpf("0")
    for k in range(cutoff + 1):
        total += 1 / (2 * mp.sinh(eps * (k + a) / 2))

    # f(x)=exp(-x/2)/(1-exp(-x)); bound every omitted term by its
    # first exponential factor and sum the resulting geometric series.
    x0 = eps * (cutoff + 1 + a)
    tail = pref * mp.exp(-x0 / 2) / (
        (1 - mp.exp(-x0)) * (1 - mp.exp(-eps / 2))
    )
    return pref * total, tail


def original_sum(
    eps: mp.mpf, tail_x: mp.mpf = mp.mpf(50)
) -> tuple[mp.mpf, mp.mpf]:
    """Untransformed partial sum and a positive omitted-tail bound."""
    t, q, alpha, beta, z, a = parameters(eps)
    s = 1 - q * q
    cutoff = int(mp.ceil(tail_x / eps))
    total = mp.mpf("0")
    Q = q * q
    for k in range(cutoff + 1):
        total += t * s * q**k / (alpha + beta * Q**k)
    # A safe positive tail bound using alpha+beta Q^k >= alpha(1-Q^k).
    k0 = cutoff + 1
    tail = (
        t * s * q**k0
        / (alpha * (1 - Q**k0) * (1 - q))
    )
    return total, tail


def regularizer_integral() -> mp.mpf:
    """Evaluate the cutoff form of integral(g), with tiny cutoff."""
    delta = mp.mpf("1e-30")
    return -mp.log(mp.tanh(delta / 4)) - mp.e1(delta)


def main() -> None:
    print("sigma =", mp.nstr(SIGMA, 20))
    print("c =", mp.nstr(C, 20))
    print("C0 = log(4)-psi(c) =", mp.nstr(C0, 20))
    print("integral(g) - (log(4)+EulerGamma) =",
          mp.nstr(regularizer_integral() - (mp.log(4) + mp.euler), 12))
    print("epsilon       a_e                 tail       identity err       err/(e log(1/e))")

    for text_eps in ("0.01", "0.005", "0.002", "0.001", "0.0005"):
        eps = mp.mpf(text_eps)
        partial, tail = direct_sum(eps)
        original_partial, original_tail = original_sum(eps)
        target = (mp.log(1 / eps) + C0) / SIGMA
        a = parameters(eps)[-1]
        # The transformed sum lies in [partial, partial+tail].  Taking
        # the larger endpoint distance is a numerical residual upper estimate
        # using the analytic tail formula; mpmath is not outward rounded.
        residual_upper = max(abs(partial - target),
                             abs(partial + tail - target))
        ratio_upper = residual_upper / (eps * mp.log(1 / eps))
        identity_error = abs(partial - original_partial)
        print(
            text_eps,
            mp.nstr(a, 16),
            mp.nstr(tail, 8),
            mp.nstr(identity_error, 8),
            mp.nstr(ratio_upper, 12),
        )
        if not tail < mp.mpf("1e-10"):
            raise AssertionError("hyperbolic tail bound is too large")
        if not original_tail > 0:
            raise AssertionError("original tail bound is not positive")
        if not identity_error < mp.mpf("1e-8"):
            raise AssertionError("transformed and original sums disagree")
        if not ratio_upper < 100:
            raise AssertionError("numerical residual estimate exceeded the proved bound")

    print("diagnostic checks: hyperbolic identity, analytic positive-tail formula, and numerical residual <= 100 e log(1/e)")


if __name__ == "__main__":
    main()
