"""I384 real interval check for the third derivative of s_g.

The check uses only rational/dyadic outward interval operations.  It is
intentionally a small scalar certificate for the signed interval
e in [-1/180,1/180], not a phase-band scan.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F

from proofs.m7_finite_poles import I384


if not __debug__:
    raise RuntimeError("run without -O: I384 assertions are required")


def iv(value) -> I384:
    return value if isinstance(value, I384) else I384(value)


@dataclass(frozen=True)
class Jet3:
    """Value and first three derivatives with I384 coefficients."""

    x: I384
    d1: I384
    d2: I384
    d3: I384

    def __add__(self, other):
        y = j3(other)
        return Jet3(self.x + y.x, self.d1 + y.d1,
                    self.d2 + y.d2, self.d3 + y.d3)

    __radd__ = __add__

    def __neg__(self):
        return Jet3(-self.x, -self.d1, -self.d2, -self.d3)

    def __sub__(self, other):
        return self + -j3(other)

    def __rsub__(self, other):
        return j3(other) + -self

    def __mul__(self, other):
        y = j3(other)
        return Jet3(
            self.x * y.x,
            self.d1 * y.x + self.x * y.d1,
            self.d2 * y.x + 2 * self.d1 * y.d1 + self.x * y.d2,
            self.d3 * y.x + 3 * self.d2 * y.d1
            + 3 * self.d1 * y.d2 + self.x * y.d3,
        )

    __rmul__ = __mul__

    def inverse(self):
        x = self.x
        return Jet3(
            1 / x,
            -self.d1 / (x ** 2),
            2 * self.d1 * self.d1 / (x ** 3)
            - self.d2 / (x ** 2),
            -6 * self.d1 * self.d1 * self.d1 / (x ** 4)
            + 6 * self.d1 * self.d2 / (x ** 3)
            - self.d3 / (x ** 2),
        )

    def __truediv__(self, other):
        return self * j3(other).inverse()

    def __rtruediv__(self, other):
        return j3(other) * self.inverse()

    def __pow__(self, exponent: int):
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        result = j3(1)
        for _ in range(exponent):
            result = result * self
        return result


def j3(value) -> Jet3:
    if isinstance(value, Jet3):
        return value
    x = iv(value)
    return Jet3(x, I384(0), I384(0), I384(0))


def log_third(f: Jet3) -> I384:
    """Third derivative of log(f), using only f and its jets."""

    f.x.positive("log-third denominator")
    return (f.d3 / f.x
            - 3 * f.d2 * f.d1 / (f.x ** 2)
            + 2 * f.d1 ** 3 / (f.x ** 3))


def produce() -> dict:
    bits = 384
    e_box = I384(-F(1, 180), F(1, 180))
    sigma = I384(2).sqrt() - 1
    t_box = I384(sigma.lo - I384(F(1, 180**2 * 8)).hi,
                 sigma.hi, raw=True)
    q_box = I384(F(359, 360), F(1003, 1000))

    # Implicit equation A(t)=2 cosh(e/2), with q=e^(-e/2).
    t = j3(Jet3(t_box, I384(0), I384(0), I384(0)))
    q = Jet3(q_box, -q_box / 2, q_box / 4, -q_box / 8)
    A1 = -1 / (t.x ** 2) + 1 + 2 * t.x
    A2 = 2 / (t.x ** 3) + 2
    A3 = -6 / (t.x ** 4)
    sinh = (1 / q.x - q.x) / 2
    cosh = (q.x + 1 / q.x) / 2
    t1 = sinh / A1
    t2 = (cosh / 2 - A2 * t1 * t1) / A1
    t3 = (sinh / 4 - A3 * t1 * t1 * t1
          - 3 * A2 * t1 * t2) / A1
    t = Jet3(t_box, t1, t2, t3)

    D = 1 - t * q
    t_sq = t * t
    f_c = D - t_sq
    f_d = D
    f_one_minus_t_sq = 1 - t_sq
    for name, value in (("q", q.x), ("D-t^2", f_c.x),
                        ("D", f_d.x), ("1-t^2", f_one_minus_t_sq.x)):
        value.positive(name)

    sg3 = (-log_third(q) - log_third(f_c)
           + log_third(f_d) + log_third(f_one_minus_t_sq))
    sg3.positive("s_g'''")
    # The sharp N^{-3} coefficient below is allowed to use .414 only
    # after this exact I384 guard has established sg3 < .414 on the
    # entire signed box.
    sg3_upper_claim = F(414, 1000)
    if not sg3.hi < sg3_upper_claim * (1 << bits):
        raise ArithmeticError("s_g''' upper bound is not below 0.414")

    # beta'(e)/e = integral_{-1}^1 r^2 integral_0^1 s_g'''(u*r*e) du dr.
    beta_prime_over_e = (sg3 * F(2, 3))
    beta_prime_lower = beta_prime_over_e.lo
    beta_prime_upper = beta_prime_over_e.hi
    sg3_upper = F(sg3.hi, 1 << bits)
    phase_e_n32_upper = F(17, 100) / (32 + F(4, 5))
    beta_theta_n32 = F(2, 3) * sg3_upper * phase_e_n32_upper ** 2 / 32
    coarse_n_coefficient = F(8, 3) * F(17, 100) ** 2
    sharp_n_coefficient = (F(2, 3) * sg3_upper_claim
                           * F(17, 100) ** 2)
    eta_lower = F(7, 10)
    eta_upper = F(71, 100)
    beta_increment = F(138, 1000) * F(1, 180) ** 2
    beta_upper = eta_upper + beta_increment

    out = {
        "classification": "EXACT I384 REAL THIRD-DERIVATIVE BOX",
        "bits": bits,
        "e_box": e_box.record(),
        "t_box": t_box.record(),
        "q_box": q_box.record(),
        "boxes": {
            "A_prime": A1.record(),
            "A_second": A2.record(),
            "A_third": A3.record(),
            "t_prime": t1.record(),
            "t_second": t2.record(),
            "t_third": t3.record(),
            "s_g_third": sg3.record(),
            "beta_prime_over_e": I384(beta_prime_lower,
                                      beta_prime_upper, raw=True).record(),
            "beta_theta_N32_abs_upper": I384(0, beta_theta_n32).record(),
            "coarse_beta_theta_N_coefficient": str(coarse_n_coefficient),
            "sharp_beta_theta_N_coefficient": str(sharp_n_coefficient),
            "beta_upper_from_eta": str(beta_upper),
        },
        "claims": {
            "sg3_lower_positive": sg3.lo > 0,
            "sg3_upper_lt_0.414": sg3.hi < F(414, 1000) * (1 << bits),
            "beta_prime_over_e_lt_0.276": (
                beta_prime_upper < F(276, 1000) * (1 << bits)
            ),
            "eta_gt_0.70": F(1, 2) > eta_lower * eta_lower,
            "eta_lt_0.71": F(1, 2) < eta_upper * eta_upper,
            "phase_e_N32_lt_1/180": phase_e_n32_upper < F(1, 180),
            "beta_upper_lt_0.72": beta_upper < F(72, 100),
            "coarse_beta_theta_coefficient_lt_0.078": (
                coarse_n_coefficient < F(78, 1000)
            ),
            "sharp_beta_theta_coefficient_lt_0.008": (
                sharp_n_coefficient < F(1, 125)
            ),
        },
        "status": "pass",
    }
    if not all(out["claims"].values()):
        raise ArithmeticError(f"failed claims: {out['claims']}")
    return out


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
