"""Finite outward-rounded certificates for the weakly-prudent W poles.

The numerical phase rows in the M5/M6 receipts are used only as rational
seeds.  Every quantity used for a conclusion in this module is recomputed
with 384-bit dyadic intervals.  In particular, the prudent moments are
summed with the regularized ``V`` weights and the omitted tail is bounded by
the exact recurrence for ``z``; no floating-point value or last-term test is
used.

The output is a finite certificate only.  It does not assert uniqueness of a
zero in a bracket and it does not fill the indices between the rows listed in
``SEEDS``.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from math import isqrt
from typing import Iterable


BITS = 384
SCALE = 1 << BITS


def ceildiv(a: int, b: int) -> int:
    return -((-a) // b)


def _floor_fraction(num: int, den: int) -> int:
    if den <= 0:
        raise ValueError("positive denominator required")
    return num // den


def _ceil_fraction(num: int, den: int) -> int:
    if den <= 0:
        raise ValueError("positive denominator required")
    return -((-num) // den)


class I384:
    """Closed dyadic intervals with endpoints scaled by ``2**BITS``."""

    __slots__ = ("lo", "hi")

    def __init__(self, a, b=None, *, raw: bool = False):
        if raw:
            self.lo, self.hi = int(a), int(a if b is None else b)
        else:
            aa = F(a)
            bb = F(a if b is None else b)
            self.lo = _floor_fraction(aa.numerator * SCALE, aa.denominator)
            self.hi = _ceil_fraction(bb.numerator * SCALE, bb.denominator)
        if self.lo > self.hi:
            raise ArithmeticError("empty dyadic interval")

    @staticmethod
    def cast(x) -> "I384":
        return x if isinstance(x, I384) else I384(x)

    def __add__(self, other):
        b = I384.cast(other)
        return I384(self.lo + b.lo, self.hi + b.hi, raw=True)

    __radd__ = __add__

    def __neg__(self):
        return I384(-self.hi, -self.lo, raw=True)

    def __sub__(self, other):
        return self + -I384.cast(other)

    def __rsub__(self, other):
        return I384.cast(other) + -self

    def __mul__(self, other):
        b = I384.cast(other)
        products = [self.lo * b.lo, self.lo * b.hi,
                    self.hi * b.lo, self.hi * b.hi]
        return I384(min(products) // SCALE,
                    ceildiv(max(products), SCALE), raw=True)

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ArithmeticError("division interval contains zero")
        # The reciprocal is monotone decreasing.  Computing both endpoint
        # values also handles a wholly negative interval without a sign case.
        values = [F(SCALE * SCALE, self.lo),
                  F(SCALE * SCALE, self.hi)]
        lo, hi = min(values), max(values)
        return I384(_floor_fraction(lo.numerator, lo.denominator),
                    _ceil_fraction(hi.numerator, hi.denominator), raw=True)

    def __truediv__(self, other):
        return self * I384.cast(other).reciprocal()

    def __rtruediv__(self, other):
        return I384.cast(other) / self

    def __pow__(self, exponent: int):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("nonnegative integer power required")
        result, base = I384(1), self
        n = exponent
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n //= 2
        return result

    def sqrt(self):
        if self.lo < 0:
            raise ArithmeticError("negative square-root interval")
        lo = isqrt(self.lo * SCALE)
        hi = isqrt(self.hi * SCALE)
        if hi * hi < self.hi * SCALE:
            hi += 1
        return I384(lo, hi, raw=True)

    def abs_upper(self):
        value = max(abs(self.lo), abs(self.hi))
        return I384(value, value, raw=True)

    def positive(self, label: str = "interval") -> None:
        if self.lo <= 0:
            raise ArithmeticError(f"{label} is not strictly positive")

    def negative(self, label: str = "interval") -> None:
        if self.hi >= 0:
            raise ArithmeticError(f"{label} is not strictly negative")

    def record(self) -> dict[str, str | int]:
        return {
            "lower_numerator": str(self.lo),
            "upper_numerator": str(self.hi),
            "denominator_power_of_two": BITS,
        }


def interval_log(x: I384, terms: int = 192) -> I384:
    """Outward enclosure of log(x) using the atanh series."""

    x.positive("log argument")
    y = (x - 1) / (x + 1)
    radius = y.abs_upper()
    if radius.hi >= SCALE:
        raise ArithmeticError("atanh log series does not converge")
    total = I384(0)
    power = y
    for k in range(terms):
        total += 2 * power / (2 * k + 1)
        power = power * y * y
    rho = F(radius.hi, SCALE)
    # 2*rho^(2*terms+1)/((2*terms+1)*(1-rho^2)) is a positive tail bound.
    tail = (2 * (rho ** (2 * terms + 1)) /
            ((2 * terms + 1) * (1 - rho * rho)))
    return total + I384(-tail, tail)


def kernel(t: I384, v: I384) -> I384:
    """Physical formal-series branch U(t,v)."""

    a = 1 - t * v + t * t + t * t * t * v
    discriminant = a * a - 4 * t * t
    discriminant.positive("kernel discriminant")
    return 2 * t / (a + discriminant.sqrt())


def phase_data(t: I384) -> dict[str, I384]:
    """Enclose the two source-pole phase coordinates a and b."""

    q = kernel(t, I384(1))
    C = q - t
    D = 1 - t * q
    v_g = q * (D - t * t) / (D * (1 - t * t))
    v_h = (C - t * t * q) / (q * C * (1 - t * t))
    epsilon = -interval_log(q * q)
    s_g = -interval_log(v_g)
    s_h = -interval_log(v_h)
    a = s_g / epsilon
    b = s_h / epsilon
    return {"q": q, "epsilon": epsilon, "v_g": v_g, "v_h": v_h,
            "s_g": s_g, "s_h": s_h, "a": a, "b": b}


def directed_sum(t: I384, tolerance: F = F(1, 10**30)) -> tuple[I384, dict]:
    """Positive D sum with an explicit geometric remainder."""

    q = kernel(t, I384(1))
    q2 = q * q
    beta = (1 - t - t * q) / (1 - q2)
    gamma = q * (t - q * (1 - t)) / (1 - q2)
    endpoint = beta + gamma
    beta.positive("directed beta")
    endpoint.positive("directed beta+gamma")
    mden = I384(min(beta.lo, endpoint.lo),
                min(beta.hi, endpoint.hi), raw=True)
    mden.positive("directed denominator lower bound")
    q.positive("directed q")
    if q.hi >= SCALE:
        raise ArithmeticError("directed q is not below one")

    total = I384(0)
    q_power = I384(1)
    q2_power = I384(1)
    used = 0
    target = I384(tolerance)
    tail = I384(1)
    one_minus_q = 1 - q
    one_minus_q.positive("1-q")
    # The loop is linear in 1/epsilon but uses only rational interval steps;
    # the check is deliberately infrequent to avoid needless divisions.
    while True:
        denominator = beta + gamma * q2_power
        denominator.positive("directed summand denominator")
        total += t * q_power / denominator
        used += 1
        q_power = q_power * q
        q2_power = q2_power * q2
        if used % 1024 == 0 or used < 128:
            tail = t / mden * q_power / one_minus_q
            if tail.hi <= target.hi and used >= 128:
                break
        if used > 3_000_000:
            raise RuntimeError("directed interval tail did not close")
    # The omitted summands are positive, so append [0,tail] rather than a
    # symmetric error box.
    D = I384(total.lo, total.hi + tail.hi, raw=True)
    D.positive("directed sum")
    return D, {"terms": used, "tail": tail}


def weights(t: I384, q: I384, u: I384) -> tuple[I384, I384]:
    """Regularized V1,V2, valid also at the removable h-zero."""

    C = q - t
    uh = t * q / C
    fu = u / (1 - t * u)
    fh = uh / (1 - t * uh)
    dd = 1 / ((1 - t * u) * (1 - t * uh))
    L1 = fh / (1 - uh)
    L2 = fh * fh / (1 - uh)
    V1 = (dd + L1) / C
    V2 = ((fu + fh) * dd + L2) / C
    V1.positive("V1")
    V2.positive("V2")
    return V1, V2


def _tail_power(base_upper: int, initial: I384, target: I384) -> int:
    """Smallest k found by exact interval binary search with initial*R^k."""

    base = I384(base_upper, base_upper, raw=True)
    if initial.hi <= target.hi:
        return 0
    high = 1
    while (initial * (base ** high)).hi > target.hi:
        high *= 2
        if high > 2_000_000:
            raise RuntimeError("tail exponent search exceeded guard")
    low = 0
    while high - low > 1:
        mid = (low + high) // 2
        if (initial * (base ** mid)).hi <= target.hi:
            high = mid
        else:
            low = mid
    return high


def _ceil_mesh(epsilon: I384, s0: int = 4) -> int:
    epsilon.positive("epsilon")
    # n*epsilon.lo/SCALE >= s0, hence n >= s0*SCALE/epsilon.lo.
    return ceildiv(s0 * SCALE, epsilon.lo) + 1


def evaluate_moments(t: I384, *, tail_target: F = F(1, 10**27)) -> dict:
    """Evaluate P,H,F and a uniform numerator box at one t interval."""

    phase = phase_data(t)
    q, epsilon = phase["q"], phase["epsilon"]
    q2 = q * q
    C = q - t
    D = 1 - t * q
    E = 1 - q2
    C.positive("C")
    D.positive("D")
    E.positive("E")
    delta = t * t * E / C
    delta.positive("delta")
    r = q * C / D
    r.positive("r")
    gq = t - D * q
    gq.negative("g(q)")
    z = 1 / gq
    z.negative("z0")

    # The exact boundary part of the regularized moment identities.
    V1_all, V2_all = weights(t, q, I384(t.lo, q.hi, raw=True))
    # This is a direct rational box on the actual finite t interval; it does
    # not import the asymptotic M5 weight-domain restriction.
    if V1_all.hi >= 40 * SCALE or V2_all.hi >= 40 * SCALE:
        raise ArithmeticError("finite V-weight box exceeded 40")
    S0 = -t * D * D / gq
    f_q = q / (1 - t * q)
    # Compute the scalar L_j separately from the variable-u regularized
    # weights; this keeps the boundary dependencies transparent.
    uh = t * q / C
    f_h = uh / (1 - t * uh)
    L1 = f_h / (1 - uh)
    L2 = f_h * f_h / (1 - uh)
    B1 = C / gq + L1 * S0
    B2 = f_q * C / gq + L2 * S0
    Q = q * t * t * E * (1 - t * t)
    Q.positive("Q")

    # First reach a point with s=n*epsilon>=4.  At this point the exact
    # physical monotonicity gives g(u_n)>0 for every subsequent n.
    start = _ceil_mesh(epsilon)
    v = I384(1)
    sum1, sum2 = I384(0), I384(0)
    for n in range(start):
        u = kernel(t, v)
        V1, V2 = weights(t, q, u)
        sum1 += z * V1
        sum2 += z * V2
        g = t - D * u
        denominator = g + delta
        if g.hi < 0:
            denominator.negative("pre-tail g+delta")
        else:
            denominator.positive("post-tail g+delta")
        ratio = r * g / denominator
        ratio.positive("z recurrence ratio")
        z = z * ratio
        z.negative("z recurrence sign")
        v = v * q2

    # For s>=4, g is positive and g<=g_infty=t^2*q because u>=t.  The
    # first post-tail value is checked mechanically; monotonicity of U in v
    # then keeps g positive for every later mesh point.
    u_start = kernel(t, v)
    g_start = t - D * u_start
    g_start.positive("g at s>=4 tail start")
    g_infty = t * t * q
    g_infty.positive("g infinity")
    # Since q*C + (1-q^2)=D, g_infty/(g_infty+delta)=q*C/D=r.
    # Keeping this as r*r avoids an unnecessary dependency widening.
    R = r * r
    R.positive("post-tail ratio")
    if R.hi >= SCALE:
        raise ArithmeticError("post-tail ratio is not below one")
    if r.hi >= SCALE:
        raise ArithmeticError("r is not below one")
    if R.hi >= r.lo:
        raise ArithmeticError("post-tail ratio is not below r")
    if r.hi >= q2.lo:
        raise ArithmeticError("r is not below exp(-epsilon)=q^2")
    z_abs = I384(-z.lo, -z.lo, raw=True)
    V1_max = I384(max(abs(V1_all.lo), abs(V1_all.hi)),
                   max(abs(V1_all.lo), abs(V1_all.hi)), raw=True)
    V2_max = I384(max(abs(V2_all.lo), abs(V2_all.hi)),
                   max(abs(V2_all.lo), abs(V2_all.hi)), raw=True)
    initial_tail_P = Q * z_abs * V1_max / (1 - R)
    initial_tail_H = t * t * Q * z_abs * V2_max / (1 - R)
    initial_tail_F = 3 * initial_tail_P + 4 * initial_tail_H
    target = I384(tail_target)
    extra = _tail_power(R.hi, initial_tail_F, target)
    final = start + extra

    # Continue from n=start through n=final-1, retaining all terms through
    # the last point.  The omitted tail then carries the exact R**extra bound.
    for n in range(start, final):
        u = kernel(t, v)
        V1, V2 = weights(t, q, u)
        sum1 += z * V1
        sum2 += z * V2
        g = t - D * u
        denominator = g + delta
        denominator.positive("post-tail g+delta")
        ratio = r * g / denominator
        ratio.positive("post-tail recurrence ratio")
        if ratio.hi >= SCALE:
            raise ArithmeticError("direct post-tail ratio is not below one")
        z = z * ratio
        z.negative("post-tail z sign")
        v = v * q2

    # Re-evaluate the geometric remainder from the final z; use the same
    # R bound.  This gives a direct, auditable final tail receipt.
    z_abs_final = I384(-z.lo, -z.lo, raw=True)
    tail_sum1 = z_abs_final * V1_max / (1 - R)
    tail_sum2 = z_abs_final * V2_max / (1 - R)
    tailP = Q * tail_sum1
    tailH = t * t * Q * tail_sum2
    tailF = 3 * tailP + 4 * tailH
    if tailF.hi > target.hi:
        raise ArithmeticError("final prudent tail did not meet target")
    # z and both regularized weights are negative/positive respectively, so
    # the omitted moment sums are negative.  The symmetric F error bound is
    # retained for endpoint sign decisions and reported explicitly.
    P = B1 + Q * sum1
    H = t * t * (B2 + Q * sum2)

    directed, dmeta = directed_sum(t)
    DI = directed / (1 + directed)
    DI.positive("D_I")
    if DI.hi >= SCALE:
        raise ArithmeticError("D_I is not below one")
    Fvalue = (3 - t - 2 * DI) * P - 4 * H - (1 + t + 2 * DI)
    Pplus = P + 1
    # A symmetric interval is valid even though the sign of the tail is known.
    Fcert = Fvalue + I384(-tailF.hi, tailF.hi, raw=True)
    Pcert = Pplus + I384(-tailP.hi, tailP.hi, raw=True)
    return {
        "phase": phase,
        "P": P,
        "H": H,
        "P_plus_one": Pplus,
        "F": Fvalue,
        "F_certificate": Fcert,
        "P_plus_one_certificate": Pcert,
        "directed": directed,
        "D_I": DI,
        "tail": {
            "start_index": start,
            "extra_terms": extra,
            "final_index": final,
            "R": R,
            "tail_P": tailP,
            "tail_H": tailH,
            "tail_F": tailF,
            "V1_box": V1_all,
            "V2_box": V2_all,
        },
        "directed_meta": dmeta,
    }


# These are only seeds copied from the already recorded M5/M6 diagnostics.
# The certificate itself never trusts their numerical residuals.
SEEDS = {
    32: "0.41421207394799683735264571222663623",
    64: "0.414213185158662864277074445373505154",
    128: "0.414213467408871231663879913007615537",
    256: "0.414213538547559642617307852519257466",
    512: "0.414213556405979324775984842665373891",
    1024: "0.414213560879958311290325902232183328",
}

# The seed residuals become smaller with N while the phase sensitivity
# dtheta/dt increases.
# These widths are fixed rational choices, all far below the [.8,.9] phase
# band, and are enlarged at the low indices only enough to dominate the
# retained diagnostic residuals.
BRACKET_HALF_WIDTHS = {
    32: F(1, 10**20),
    64: F(1, 10**21),
    128: F(1, 10**22),
    256: F(1, 10**23),
    512: F(1, 10**23),
    1024: F(1, 10**24),
}


def _record_interval(x: I384) -> dict:
    return x.record()


def certify_index(index: int, seed: str) -> dict:
    centre = F(seed)
    half_width = BRACKET_HALF_WIDTHS[index]
    lo = centre - half_width
    hi = centre + half_width
    t_lo = I384(lo)
    t_hi = I384(hi)
    t_box = I384(lo, hi)
    left = evaluate_moments(t_lo)
    right = evaluate_moments(t_hi)
    uniform = evaluate_moments(t_box)
    a = uniform["phase"]["a"]
    b = uniform["phase"]["b"]
    phase_ok = (5 * (a.lo - index * SCALE) > 4 * SCALE
                and 10 * (a.hi - index * SCALE) < 9 * SCALE
                and b.lo > index * SCALE
                and b.hi < (index + 1) * SCALE)
    # The exact interval checks are intentionally strict.  If a seed ever
    # falls outside the claimed phase band or source-pole-free strip, this
    # routine fails rather than silently downgrading the certificate.
    if not phase_ok:
        raise ArithmeticError(f"phase/source-pole check failed at N={index}")
    if left["F_certificate"].lo <= 0:
        raise ArithmeticError(f"left endpoint F sign failed at N={index}")
    if right["F_certificate"].hi >= 0:
        raise ArithmeticError(f"right endpoint F sign failed at N={index}")
    if uniform["P_plus_one_certificate"].hi >= 0:
        raise ArithmeticError(f"uniform W numerator sign failed at N={index}")
    return {
        "index": index,
        "seed": seed,
        "t_half_width": str(half_width),
        "t_bracket": [str(lo), str(hi)],
        "phase_source_check": {
            "a": _record_interval(a),
            "b": _record_interval(b),
            "phase_band": [str(index + F(4, 5)), str(index + F(9, 10))],
            "source_pole_free": True,
        },
        "left": {
            "t": _record_interval(t_lo),
            "F_certificate": _record_interval(left["F_certificate"]),
            "P_plus_one_certificate": _record_interval(left["P_plus_one_certificate"]),
            "tail": _record_tail(left["tail"]),
            "directed": _record_directed(left),
        },
        "right": {
            "t": _record_interval(t_hi),
            "F_certificate": _record_interval(right["F_certificate"]),
            "P_plus_one_certificate": _record_interval(right["P_plus_one_certificate"]),
            "tail": _record_tail(right["tail"]),
            "directed": _record_directed(right),
        },
        "uniform_numerator": {
            "t": _record_interval(t_box),
            "P_plus_one_certificate": _record_interval(
                uniform["P_plus_one_certificate"]),
            "tail": _record_tail(uniform["tail"]),
        },
    }


def _record_tail(tail: dict) -> dict:
    result = {}
    for key, value in tail.items():
        if isinstance(value, I384):
            result[key] = value.record()
        else:
            result[key] = value
    return result


def _record_directed(result: dict) -> dict:
    return {
        "D": result["directed"].record(),
        "D_I": result["D_I"].record(),
        "terms": result["directed_meta"]["terms"],
        "tail": result["directed_meta"]["tail"].record(),
    }


def produce(indices: Iterable[int] = tuple(SEEDS)) -> dict:
    if not __debug__:
        raise RuntimeError("Run without -O: M7 interval assertions are required")
    indices = tuple(int(index) for index in indices)
    if indices != tuple(sorted(indices)) or any(index not in SEEDS for index in indices):
        raise ValueError("indices must be an increasing subset of the frozen seeds")
    rows = [certify_index(index, SEEDS[index]) for index in indices]
    return {
        "classification": "EXACT FINITE W POLE BRACKETS; 384-BIT OUTWARD INTERVALS",
        "status": "pass",
        "interval_bits": BITS,
        "tail_target": "1e-27",
        "indices": list(indices),
        "bracket_half_widths": {str(k): str(v)
                                for k, v in BRACKET_HALF_WIDTHS.items()},
        "source_seed_scope": (
            "M5/M6 finite diagnostic decimals are seeds only; all signs, tails, "
            "phase coordinates and numerator boxes are recomputed exactly."
        ),
        "rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
