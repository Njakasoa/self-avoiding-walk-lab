"""Outward interval first derivatives for the six frozen M7 W brackets.

This module is deliberately a finite companion to ``m7_finite_poles``.  The
M7 producer supplies the endpoint signs and the whole-bracket noncancellation
box.  Here every displayed derivative is obtained by propagating a first
order interval jet through the exact rational/algebraic formulae.  The two
infinite tails are handled analytically:

* the directed tail uses the exact sums of ``q**k`` and ``k*q**(k-1)``;
* the prudent tail uses ``|z_(M+k)| <= Z R**k`` and
  ``|z'_(M+k)| <= R**k (Z' + k Z L/R)``.

No finite difference of a C0 enclosure is used.  The output is only a
derivative certificate on the six already frozen brackets; it does not make
any statement about unlisted indices or complete phase bands.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from typing import Iterable

from .m7_finite_poles import (
    BITS,
    SCALE,
    BRACKET_HALF_WIDTHS,
    I384,
    SEEDS,
    ceildiv,
    interval_log,
)


TARGET_VALUE = F(1, 10**18)
TARGET_DERIVATIVE = F(1, 10**18)


def _abs_box(x: I384) -> I384:
    a = max(abs(x.lo), abs(x.hi))
    return I384(a, a, raw=True)


class Jet384:
    """A value and its exact first derivative, both as I384 intervals."""

    __slots__ = ("x", "d")

    def __init__(self, x, d=0):
        self.x = I384.cast(x)
        self.d = I384.cast(d)

    @staticmethod
    def cast(x) -> "Jet384":
        return x if isinstance(x, Jet384) else Jet384(x)

    def __add__(self, other):
        other = Jet384.cast(other)
        return Jet384(self.x + other.x, self.d + other.d)

    __radd__ = __add__

    def __neg__(self):
        return Jet384(-self.x, -self.d)

    def __sub__(self, other):
        return self + -Jet384.cast(other)

    def __rsub__(self, other):
        return Jet384.cast(other) + -self

    def __mul__(self, other):
        other = Jet384.cast(other)
        return Jet384(self.x * other.x,
                      self.d * other.x + self.x * other.d)

    __rmul__ = __mul__

    def reciprocal(self):
        return Jet384(self.x.reciprocal(),
                      -self.d / (self.x * self.x))

    def __truediv__(self, other):
        return self * Jet384.cast(other).reciprocal()

    def __rtruediv__(self, other):
        return Jet384.cast(other) / self

    def __pow__(self, exponent: int):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("nonnegative integer power required")
        if exponent == 0:
            return Jet384(1)
        return Jet384(self.x ** exponent,
                      exponent * (self.x ** (exponent - 1)) * self.d)

    def sqrt(self):
        root = self.x.sqrt()
        return Jet384(root, self.d / (2 * root))

    def log(self):
        return Jet384(interval_log(self.x), self.d / self.x)

    def record(self) -> dict:
        return {"value": self.x.record(), "derivative": self.d.record()}


def kernel_jet(t: Jet384, v: Jet384) -> Jet384:
    """Physical kernel U(t,v) and its t derivative."""

    a = 1 - t * v + t * t + t * t * t * v
    discriminant = a * a - 4 * t * t
    discriminant.x.positive("kernel discriminant")
    return 2 * t / (a + discriminant.sqrt())


def weights_jet(t: Jet384, q: Jet384, u: Jet384) -> tuple[Jet384, Jet384]:
    """Regularized V1,V2 and their t derivatives."""

    C = q - t
    uh = t * q / C
    fu = u / (1 - t * u)
    fh = uh / (1 - t * uh)
    dd = 1 / ((1 - t * u) * (1 - t * uh))
    L1 = fh / (1 - uh)
    L2 = fh * fh / (1 - uh)
    V1 = (dd + L1) / C
    V2 = ((fu + fh) * dd + L2) / C
    V1.x.positive("V1")
    V2.x.positive("V2")
    return V1, V2


def _tail_sums(q: I384, K: int) -> tuple[I384, I384]:
    """Return S0=sum q^k and S1=sum k q^(k-1), k>=K."""

    if K < 1:
        raise ValueError("tail sum requires K>=1")
    one_minus_q = 1 - q
    one_minus_q.positive("tail 1-q")
    qK = q ** K
    S0 = qK / one_minus_q
    S1 = (q ** (K - 1) * (K - (K - 1) * q)
          / (one_minus_q * one_minus_q))
    return S0, S1


def directed_jet(t: Jet384, q: Jet384,
                 value_target: F = TARGET_VALUE,
                 derivative_target: F = TARGET_DERIVATIVE,
                 ) -> tuple[Jet384, dict]:
    """Directed sum with an explicit value and derivative tail box."""

    q2 = q * q
    beta = (1 - t - t * q) / (1 - q2)
    gamma = q * (t - q * (1 - t)) / (1 - q2)
    endpoint = beta + gamma
    mden = I384(min(beta.x.lo, endpoint.x.lo),
                min(beta.x.hi, endpoint.x.hi), raw=True)
    beta.x.positive("directed beta")
    endpoint.x.positive("directed beta+gamma")
    mden.positive("directed denominator lower bound")
    q.x.positive("directed q")
    if q.x.hi >= SCALE:
        raise ArithmeticError("directed q is not below one")

    q_upper = I384(q.x.hi, q.x.hi, raw=True)
    q_upper.positive("directed q upper")
    if q_upper.hi >= SCALE:
        raise ArithmeticError("directed q upper is not below one")
    q2_upper = q_upper * q_upper
    t_abs = _abs_box(t.x)
    qprime_abs = _abs_box(q.d)
    beta_prime_abs = _abs_box(beta.d)
    gamma_prime_abs = _abs_box(gamma.d)
    gamma_abs = _abs_box(gamma.x)

    def tails(used: int) -> tuple[I384, I384]:
        S0, S1 = _tail_sums(q_upper, used)
        S02, S12 = _tail_sums(q2_upper, used)
        # d(q^(2k))/dt = 2 k q^(2k-1) q'.  S12 has the factor
        # k*(q^2)^(k-1), so the remaining q is explicit below.
        value = t_abs / mden * S0
        derivative = (
            (S0 + t_abs * qprime_abs * S1) / mden
            + t_abs / (mden * mden) * (
                beta_prime_abs * S0
                + gamma_prime_abs * S02
                + 2 * gamma_abs * qprime_abs * q_upper * S12
            )
        )
        return value, derivative

    total = Jet384(0)
    q_power = Jet384(1)
    q2_power = Jet384(1)
    used = 0
    value_limit = I384(value_target)
    derivative_limit = I384(derivative_target)
    while True:
        denominator = beta + gamma * q2_power
        denominator.x.positive("directed summand denominator")
        total += t * q_power / denominator
        used += 1
        q_power = q_power * q
        q2_power = q2_power * q2
        if used % 256 == 0 or used < 128:
            tail_value, tail_derivative = tails(used)
            if (tail_value.hi <= value_limit.hi
                    and tail_derivative.hi <= derivative_limit.hi):
                break
        if used > 3_000_000:
            raise RuntimeError("directed derivative tail did not close")

    tail_value, tail_derivative = tails(used)
    if tail_value.hi > value_limit.hi:
        raise ArithmeticError("directed value tail did not close")
    if tail_derivative.hi > derivative_limit.hi:
        raise ArithmeticError("directed derivative tail did not close")
    result = total + Jet384(
        I384(0, tail_value.hi, raw=True),
        I384(-tail_derivative.hi, tail_derivative.hi, raw=True),
    )
    result.x.positive("directed sum")
    return result, {
        "terms": used,
        "tail_value": tail_value,
        "tail_derivative": tail_derivative,
        "mden": mden,
        "q_upper": q_upper,
    }


def _choose_extra(
    good,
    *,
    guard: int = 2_000_000,
) -> int:
    high = 1
    while not good(high):
        high *= 2
        if high > guard:
            raise RuntimeError("prudent derivative tail exponent exceeded guard")
    low = 0
    while high - low > 1:
        mid = (low + high) // 2
        if good(mid):
            high = mid
        else:
            low = mid
    return high


def evaluate_derivative(
    t_box: I384,
    *,
    value_target: F = TARGET_VALUE,
    derivative_target: F = TARGET_DERIVATIVE,
) -> dict:
    """Evaluate F and F' over one complete rational t bracket."""

    t = Jet384(t_box, 1)
    q = kernel_jet(t, Jet384(1))
    q2 = q * q
    C = q - t
    D = 1 - t * q
    E = 1 - q2
    delta = t * t * E / C
    r = q * C / D
    gq = t - D * q
    z = 1 / gq
    epsilon = -q2.log()
    start = ceildiv(4 * SCALE, epsilon.x.lo) + 1
    C.x.positive("C")
    D.x.positive("D")
    E.x.positive("E")
    delta.x.positive("delta")
    r.x.positive("r")
    gq.x.negative("g(q)")
    z.x.negative("z0")

    v = Jet384(1)
    sum1 = Jet384(0)
    sum2 = Jet384(0)
    for _ in range(start):
        u = kernel_jet(t, v)
        V1, V2 = weights_jet(t, q, u)
        sum1 += z * V1
        sum2 += z * V2
        g = t - D * u
        denominator = g + delta
        if g.x.hi < 0:
            denominator.x.negative("pre-tail g+delta")
        else:
            denominator.x.positive("post-tail g+delta")
        ratio = r * g / denominator
        ratio.x.positive("z recurrence ratio")
        z = z * ratio
        z.x.negative("z recurrence sign")
        v = v * q2

    u_start = kernel_jet(t, v)
    g_start = t - D * u_start
    g_start.x.positive("g at tail start")
    g_infty = t * t * q
    g_infty.x.positive("g infinity")
    R = r * r
    R.x.positive("post-tail ratio")
    if R.x.hi >= SCALE:
        raise ArithmeticError("post-tail ratio is not below one")
    if r.x.hi >= SCALE:
        raise ArithmeticError("r is not below one")
    if R.x.hi >= r.x.lo:
        raise ArithmeticError("post-tail ratio is not below r")
    if r.x.hi >= q2.x.lo:
        raise ArithmeticError("r is not below exp(-epsilon)")

    # A complete interval bound for u_n' after the cutoff.  Since
    # v_n=q^(2n), n*q^(2n-1) decreases from `start` onward by the guard
    # above.  The kernel partials are evaluated on 0<=v<=v_start.
    v_box = I384(0, v.x.hi, raw=True)
    u_t_partial = kernel_jet(Jet384(t.x, 1), Jet384(v_box, 0)).d
    u_v_partial = kernel_jet(Jet384(t.x, 0), Jet384(v_box, 1)).d
    q_upper = I384(q.x.hi, q.x.hi, raw=True)
    q2_upper = q_upper * q_upper
    # The exact ratio test makes n*q^(2n-1) decreasing from the cutoff.
    if (start + 1) * q2_upper.hi > start * SCALE:
        raise ArithmeticError("post-tail n*q^(2n-1) is not monotone")
    v_prime_max = (2 * start * (q_upper ** (2 * start - 1))
                   * _abs_box(q.d))
    u_prime_max = _abs_box(u_t_partial) + _abs_box(u_v_partial) * v_prime_max
    g_prime_max = (1 + _abs_box(D.d) + _abs_box(D.x) * u_prime_max)
    delta_lower = I384(delta.x.lo, delta.x.lo, raw=True)
    delta_upper = _abs_box(delta.x)
    g_upper = _abs_box(g_infty.x)
    rho_prime_max = (
        _abs_box(r.d)
        + _abs_box(r.x) * (
            delta_upper * g_prime_max + g_upper * _abs_box(delta.d)
        ) / (delta_lower * delta_lower)
    )

    # The same box covers all post-cutoff weights and their derivatives.
    u_box = I384(t.x.lo, u_start.x.hi, raw=True)
    u_derivative_box = I384(-u_prime_max.hi, u_prime_max.hi, raw=True)
    V1_box_jet, V2_box_jet = weights_jet(
        Jet384(t.x, 1), Jet384(q.x, q.d),
        Jet384(u_box, u_derivative_box),
    )
    V1_max = _abs_box(V1_box_jet.x)
    V2_max = _abs_box(V2_box_jet.x)
    V1_derivative_max = _abs_box(V1_box_jet.d)
    V2_derivative_max = _abs_box(V2_box_jet.d)

    Q = q * t * t * E * (1 - t * t)
    Z_start = _abs_box(z.x)
    Z_derivative_start = _abs_box(z.d)
    R_upper = I384(R.x.hi, R.x.hi, raw=True)
    one_minus_R = 1 - R_upper
    one_minus_R.positive("1-R")
    s0 = 1 / one_minus_R
    s1 = R_upper / (one_minus_R * one_minus_R)

    def boxes(extra: int) -> dict[str, I384]:
        R_power = R_upper ** extra
        Z = Z_start * R_power
        Z_derivative = R_power * (
            Z_derivative_start
            + extra * Z_start * rho_prime_max / R_upper
        )

        def one(Vmax: I384, Vdmax: I384) -> tuple[I384, I384]:
            value = _abs_box(Q.x) * Z * Vmax * s0
            base = (
                Z * (_abs_box(Q.d) * Vmax + _abs_box(Q.x) * Vdmax)
                + _abs_box(Q.x) * Vmax * Z_derivative
            )
            derivative = (base * s0
                          + _abs_box(Q.x) * Vmax * Z
                          * rho_prime_max / R_upper * s1)
            return value, derivative

        P_value, P_derivative = one(V1_max, V1_derivative_max)
        H_value0, H_derivative0 = one(V2_max, V2_derivative_max)
        t2 = t * t
        H_value = _abs_box(t2.x) * H_value0
        H_derivative = (_abs_box(t2.x) * H_derivative0
                        + _abs_box(t2.d) * H_value0)
        return {
            "tail_P": P_value,
            "tail_P_derivative": P_derivative,
            "tail_H": H_value,
            "tail_H_derivative": H_derivative,
        }

    value_limit = I384(value_target)
    derivative_limit = I384(derivative_target)

    def good(extra: int) -> bool:
        b = boxes(extra)
        return (
            b["tail_P"].hi <= value_limit.hi
            and b["tail_H"].hi <= value_limit.hi
            and b["tail_P_derivative"].hi <= derivative_limit.hi
            and b["tail_H_derivative"].hi <= derivative_limit.hi
        )

    extra = _choose_extra(good)
    for _ in range(extra):
        u = kernel_jet(t, v)
        V1, V2 = weights_jet(t, q, u)
        sum1 += z * V1
        sum2 += z * V2
        g = t - D * u
        denominator = g + delta
        denominator.x.positive("post-tail g+delta")
        ratio = r * g / denominator
        ratio.x.positive("post-tail recurrence ratio")
        if ratio.x.hi >= SCALE:
            raise ArithmeticError("direct post-tail ratio is not below one")
        z = z * ratio
        z.x.negative("post-tail z sign")
        v = v * q2

    tail = boxes(extra)
    tailP = tail["tail_P"]
    tailH = tail["tail_H"]
    tailP_derivative = tail["tail_P_derivative"]
    tailH_derivative = tail["tail_H_derivative"]
    if tailP.hi > value_limit.hi or tailH.hi > value_limit.hi:
        raise ArithmeticError("prudent value tail did not close")
    if (tailP_derivative.hi > derivative_limit.hi
            or tailH_derivative.hi > derivative_limit.hi):
        raise ArithmeticError("prudent derivative tail did not close")

    # The omitted moment terms are negative because z_n<0 and V_j>0.
    P_boundary = -t * D * D / gq
    uh = t * q / C
    fh = uh / (1 - t * uh)
    L1 = fh / (1 - uh)
    L2 = fh * fh / (1 - uh)
    fq = q / D
    B1 = C / gq + L1 * P_boundary
    B2 = fq * C / gq + L2 * P_boundary
    P = B1 + Q * sum1 + Jet384(
        I384(-tailP.hi, 0, raw=True),
        I384(-tailP_derivative.hi, tailP_derivative.hi, raw=True),
    )
    H = t * t * (B2 + Q * sum2) + Jet384(
        I384(-tailH.hi, 0, raw=True),
        I384(-tailH_derivative.hi, tailH_derivative.hi, raw=True),
    )

    directed, directed_meta = directed_jet(
        t, q, value_target=value_target,
        derivative_target=derivative_target,
    )
    D_I = directed / (1 + directed)
    D_I.x.positive("D_I")
    if D_I.x.hi >= SCALE:
        raise ArithmeticError("D_I is not below one")
    Fvalue = ((3 - t - 2 * D_I) * P - 4 * H
              - (1 + t + 2 * D_I))

    return {
        "t": t,
        "q": q,
        "epsilon": epsilon,
        "P": P,
        "H": H,
        "D_I": D_I,
        "F": Fvalue,
        "tail": {
            "start_index": start,
            "extra_terms": extra,
            "final_index": start + extra,
            "R": R,
            "rho_prime_bound": rho_prime_max,
            "u_prime_bound": u_prime_max,
            "g_prime_bound": g_prime_max,
            "V1_box": V1_box_jet.x,
            "V2_box": V2_box_jet.x,
            "V1_derivative_box": V1_box_jet.d,
            "V2_derivative_box": V2_box_jet.d,
            "tail_P": tailP,
            "tail_H": tailH,
            "tail_P_derivative": tailP_derivative,
            "tail_H_derivative": tailH_derivative,
        },
        "directed_meta": directed_meta,
    }


def _record_tail(tail: dict) -> dict:
    out = {}
    for key, value in tail.items():
        if isinstance(value, (I384, Jet384)):
            out[key] = value.record()
        else:
            out[key] = value
    return out


def certify_index(index: int, seed: str) -> dict:
    centre = F(seed)
    half_width = BRACKET_HALF_WIDTHS[index]
    t_box = I384(centre - half_width, centre + half_width)
    result = evaluate_derivative(t_box)
    derivative = result["F"].d
    if derivative.hi >= 0:
        raise ArithmeticError(f"F derivative is not negative at N={index}")
    return {
        "index": index,
        "seed": seed,
        "t_half_width": str(half_width),
        "t_bracket": [str(centre - half_width), str(centre + half_width)],
        "F": result["F"].record(),
        "P": result["P"].record(),
        "H": result["H"].record(),
        "D_I": result["D_I"].record(),
        "tail": _record_tail(result["tail"]),
        "directed": {
            "D_I": result["D_I"].record(),
            "terms": result["directed_meta"]["terms"],
            "tail_value": result["directed_meta"]["tail_value"].record(),
            "tail_derivative": result["directed_meta"]["tail_derivative"].record(),
            "mden": result["directed_meta"]["mden"].record(),
        },
        "derivative_strictly_negative": True,
    }


def produce(indices: Iterable[int] = tuple(SEEDS)) -> dict:
    if not __debug__:
        raise RuntimeError("Run without -O: M8 interval assertions are required")
    indices = tuple(int(index) for index in indices)
    if (indices != tuple(sorted(indices))
            or len(set(indices)) != len(indices)
            or any(index not in SEEDS for index in indices)):
        raise ValueError("indices must be an increasing subset of the frozen seeds")
    rows = [certify_index(index, SEEDS[index]) for index in indices]
    return {
        "classification": (
            "EXACT FINITE W DERIVATIVE BRACKETS; 384-BIT OUTWARD INTERVAL JETS"
        ),
        "status": "pass",
        "interval_bits": BITS,
        "tail_value_target": str(TARGET_VALUE),
        "tail_derivative_target": str(TARGET_DERIVATIVE),
        "indices": list(indices),
        "source_scope": (
            "M7 endpoint signs and whole-bracket numerator boxes are frozen "
            "inputs; M8 certifies F_t'<0 on those same six brackets."
        ),
        "rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
