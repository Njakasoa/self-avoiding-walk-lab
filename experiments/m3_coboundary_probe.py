"""Exact local algebra for the BB2014 prudent-ramp summands.

This probe checks identities only.  It does not evaluate the infinite series
or certify the noncancellation inequality.
"""
import sympy as sp


def exact_checks():
    t, q, u, w = sp.symbols("t q u w")
    C, D, E = q - t, 1 - t * q, 1 - q**2
    h, g = t * q - C * u, t - D * u
    k = q * C**2 / D**2
    f = lambda x: x / (1 - t * x)
    K = C * (1 - t**2) / D

    F = u * D - (q * C + t * E * u) * w
    Kh = D * u**2 * (1 - 2 * t * w) - (
        q * C - t * u * (2 * q * C + t * E * u)
    ) * w**2
    assert sp.factor(
        D * f(u) - q * C * f(w) - F / ((1 - t * u) * (1 - t * w))
    ) == 0
    assert sp.factor(
        D * f(u)**2
        - q * C * f(w)**2
        - Kh / ((1 - t * u)**2 * (1 - t * w)**2)
    ) == 0
    assert sp.factor(
        Kh - (u * (1 - t * w) * F + q * C * w * (u - w) * (1 - t * u))
    ) == 0

    for power in range(5):
        Ap = K / h * (D * f(u)**power - q * C * f(w)**power)
        ydiff = D * (1 - t**2) * (f(u)**power / g - k * f(w)**power / h)
        remainder = t**2 * E * (1 - t**2) * f(u)**power / (h * g)
        assert sp.factor(Ap - (ydiff - remainder)) == 0

    q_relation = t - (1 - t + t**2 + t**3) * q + t * q**2
    moment_numerator = sp.together(
        h - k * g - C * E / D * (1 - u)
    ).as_numer_denom()[0]
    assert sp.simplify(
        moment_numerator + q_relation * (q - 1) * (q + 1)
    ) == 0
    return {
        "A_equals_A1": True,
        "hook_equals_t2_A2": True,
        "positive_hook_decomposition": True,
        "telescoping_powers_checked": list(range(5)),
        "moment_identity_mod_q_relation": True,
    }


if __name__ == "__main__":
    print(exact_checks())
