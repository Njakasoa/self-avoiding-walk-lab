"""One-point M11 decomposition diagnostic for the frozen M8 formulas.

This is deliberately an exploratory calculation.  It evaluates only
``N=32, theta=0.85``.  The phase point is a rational midpoint of an exact
80-bisection bracket, and its phase interval is checked with the frozen
``I384`` arithmetic.  The M8 moment sum and the directed sum below are
finite truncations, so the reported ``rest`` and all derivatives are not
certificates and make no statement for another ``N`` or phase.

The regularized M8 identity used here is

    P = B1 + Q sum_n z_n V1(u_n),
    H = t^2 (B2 + Q sum_n z_n V2(u_n)),
    F = (3-t-2 D_I) P - 4 H - (1+t+2 D_I).

Writing ``L_W=4t^2 V2-(3-t-2D_I)V1`` gives

    F = B - Q sum_n z_n L_W(u_n),
    B = (3-t-2D_I)B1 - 4t^2 B2 - (1+t+2D_I).

The finite sum is split into boundary, n=0..N, N+1..60N, and the
remaining computed terms.  ``mp.diff`` differentiates each fixed-index
component with respect to t; division by ``a'(t)`` converts it to a theta
derivative, where ``a(t)=s_g/e`` is the M5 phase coordinate.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, Tuple

import mpmath as mp


if not __debug__:  # Keep accidental optimized runs from silently weakening the probe.
    raise RuntimeError("m11_decomposition_probe.py must run without -O")


# The task is intentionally a single bounded point.
N = 32
THETA = mp.mpf("0.85")
TARGET_PHASE = Fraction(657, 20)  # N + theta = 32.85
PHASE_BISECTIONS = 80
MP_DPS = 70
MOMENT_END = 8000  # terms n=0,...,MOMENT_END-1; fixed exploratory truncation
DIRECTED_TERMS = 16000  # fixed exploratory truncation for D
SCALE = 1 << 384

ROOT = Path(__file__).resolve().parents[1]
RESULT_PATH = ROOT / "results" / "m11-decomposition-diagnostic.json"

# Running this file by path puts ``experiments/`` first on sys.path.  Make the
# repository root explicit so the source-frozen ``proofs`` namespace imports
# work in both ``python experiments/...`` and ``python -m ...`` invocations.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _load_exact_phase_tools():
    """Load frozen exact arithmetic lazily, after the script's own constants."""

    # Importing the producer is read-only and calls only its one-dimensional
    # phase-edge helper; it does not run the 128-cell scan.
    from proofs.m10_full_band import _phase_edge
    from proofs.m7_finite_poles import I384, phase_data

    return _phase_edge, I384, phase_data


def exact_phase_point() -> Dict[str, object]:
    """Return an exact rational midpoint and its I384 phase verification."""

    phase_edge, I384, phase_data = _load_exact_phase_tools()
    edge = phase_edge(TARGET_PHASE, choose="lower")
    if edge.get("bisection_iterations") != PHASE_BISECTIONS:
        raise AssertionError("frozen phase-edge helper used an unexpected bisection count")
    lo, hi = (Fraction(str(x)) for x in edge["root_t_bracket"])
    t_rat = (lo + hi) / 2
    t_box = I384(t_rat)
    pdata = phase_data(t_box)
    root_box = I384(lo, hi)
    root_phase = phase_data(root_box)["a"]
    lo_phase = phase_data(I384(lo))["a"]
    hi_phase = phase_data(I384(hi))["a"]
    a_box = pdata["a"]
    b_box = pdata["b"]

    # The bracket is exact; the midpoint is an exact rational evaluation point.
    # A midpoint need not have its tiny I384 phase interval contain the
    # irrational phase root, so retain the enclosing endpoint bracket and
    # require the midpoint phase to be within the displayed high-precision
    # tolerance of the target.
    a_lo = Fraction(a_box.lo, SCALE)
    a_hi = Fraction(a_box.hi, SCALE)
    if not (Fraction(32) < a_lo and a_hi < Fraction(33)):
        raise AssertionError(f"phase point is outside (32,33): {a_lo}, {a_hi}")
    phase_error = max(abs(a_lo - TARGET_PHASE), abs(a_hi - TARGET_PHASE))
    if phase_error >= Fraction(1, 10**20):
        raise AssertionError(f"80-bisection midpoint phase error too large: {phase_error}")
    lo_phase_fraction = (Fraction(lo_phase.lo, SCALE), Fraction(lo_phase.hi, SCALE))
    hi_phase_fraction = (Fraction(hi_phase.lo, SCALE), Fraction(hi_phase.hi, SCALE))
    if not (lo_phase_fraction[1] < TARGET_PHASE < hi_phase_fraction[0]):
        raise AssertionError("exact root endpoint phase intervals do not bracket target")
    root_phase_fraction = (Fraction(root_phase.lo, SCALE), Fraction(root_phase.hi, SCALE))
    if not (root_phase_fraction[0] <= TARGET_PHASE <= root_phase_fraction[1]):
        raise AssertionError("I384 phase image of exact root bracket misses target")

    return {
        "target_phase": str(TARGET_PHASE),
        "phase_bisections": PHASE_BISECTIONS,
        "root_bracket": {"lo": str(lo), "hi": str(hi)},
        "t_rational_midpoint": str(t_rat),
        "t_decimal_80": mp.nstr(mp.mpf(t_rat.numerator) / t_rat.denominator, 80),
        "phase_a_I384": {"lo": str(a_lo), "hi": str(a_hi)},
        "root_bracket_phase_a_I384": {
            "lo": str(root_phase_fraction[0]),
            "hi": str(root_phase_fraction[1]),
            "target_contained": True,
        },
        "root_endpoint_phase_a_I384": {
            "lo_endpoint": {"lo": str(lo_phase_fraction[0]), "hi": str(lo_phase_fraction[1])},
            "hi_endpoint": {"lo": str(hi_phase_fraction[0]), "hi": str(hi_phase_fraction[1])},
        },
        "phase_b_I384": {
            "lo": str(Fraction(b_box.lo, SCALE)),
            "hi": str(Fraction(b_box.hi, SCALE)),
        },
        "phase_midpoint_error_bound": str(phase_error),
        "phase_midpoint_interval_contains_target": a_lo <= TARGET_PHASE <= a_hi,
        "phase_root_bracket_interval_contains_target": True,
        "phase_target_bracketed_by_root_endpoints": True,
        "source": "proofs/m10_full_band.py:_phase_edge + proofs/m7_finite_poles.py:I384/phase_data",
        "_t_fraction": t_rat,
    }


def mp_kernel(t: mp.mpf, v: mp.mpf) -> mp.mpf:
    """The physical formal-series branch U(t,v) used by frozen M8."""

    alpha = 1 - t * v + t * t + t**3 * v
    return 2 * t / (alpha + mp.sqrt(alpha * alpha - 4 * t * t))


def mp_phase_coordinate(t: mp.mpf) -> mp.mpf:
    """M5 phase coordinate a(t)=s_g/e, with the same kernel convention."""

    q = mp_kernel(t, mp.mpf(1))
    C = q - t
    D = 1 - t * q
    v_g = q * (D - t * t) / (D * (1 - t * t))
    s_g = -mp.log(v_g)
    epsilon = -mp.log(q * q)
    return s_g / epsilon


def directed_sum_fixed(t: mp.mpf, terms: int = DIRECTED_TERMS) -> mp.mpf:
    """Finite closed-form directed ramp sum used by M8, with fixed length."""

    q = mp_kernel(t, mp.mpf(1))
    q2 = q * q
    beta = (1 - t - t * q) / (1 - q2)
    gamma = q * (t - q * (1 - t)) / (1 - q2)
    qk = mp.mpf(1)
    total = mp.mpf(0)
    for _ in range(terms):
        total += t * qk / (beta + gamma * qk * qk)
        qk *= q
    return total


def _m8_components(t: mp.mpf, moment_end: int = MOMENT_END) -> Dict[str, mp.mpf]:
    """Evaluate all fixed-truncation M8 components at a given t."""

    q = mp_kernel(t, mp.mpf(1))
    q2 = q * q
    C = q - t
    D = 1 - t * q
    E = 1 - q2
    delta = t * t * E / C
    r = q * C / D
    gq = t - D * q
    z = 1 / gq
    uh = t * q / C

    def f(x: mp.mpf) -> mp.mpf:
        return x / (1 - t * x)

    fh = f(uh)
    L1 = fh / (1 - uh)
    L2 = fh * fh / (1 - uh)

    def regularized_weights(u: mp.mpf) -> Tuple[mp.mpf, mp.mpf]:
        dd = 1 / ((1 - t * u) * (1 - t * uh))
        V1 = (dd + L1) / C
        V2 = ((f(u) + fh) * dd + L2) / C
        return V1, V2

    P_boundary = -t * D * D / gq
    uhat = uh
    fhat = uhat / (1 - t * uhat)
    fq = q / D
    B1 = C / gq + L1 * P_boundary
    B2 = fq * C / gq + L2 * P_boundary

    directed = directed_sum_fixed(t)
    D_I = directed / (1 + directed)
    c = 3 - t - 2 * D_I
    Q = q * t * t * E * (1 - t * t)
    boundary = c * B1 - 4 * t * t * B2 - (1 + t + 2 * D_I)

    pre = mp.mpf(0)
    post = mp.mpf(0)
    rest = mp.mpf(0)
    sum1 = mp.mpf(0)
    sum2 = mp.mpf(0)
    last_term = mp.mpf(0)
    v = mp.mpf(1)
    for n in range(moment_end):
        u = mp_kernel(t, v)
        V1, V2 = regularized_weights(u)
        # This sign convention matches the requested F=B-Q sum z_n L_W.
        LW = 4 * t * t * V2 - c * V1
        term = -Q * z * LW
        sum1 += z * V1
        sum2 += z * V2
        if n <= N:
            pre += term
        elif n <= 60 * N:
            post += term
        else:
            rest += term
        last_term = term
        # Frozen M8 recurrence: z_{n+1}=z_n*r*g_n/(g_n+delta),
        # with v_{n+1}=q^2 v_n.  This is the regularized continuation
        # recurrence, rather than the unregularized consecutive-g ratio.
        v *= q2
        g = t - D * u
        z *= r * g / (g + delta)

    P = B1 + Q * sum1
    H = t * t * (B2 + Q * sum2)
    F_direct = c * P - 4 * H - (1 + t + 2 * D_I)
    F_sum = boundary + pre + post + rest

    return {
        "boundary": boundary,
        "pre": pre,
        "post": post,
        "rest": rest,
        "F_sum": F_sum,
        "F_direct": F_direct,
        "P": P,
        "H": H,
        "D": directed,
        "D_I": D_I,
        "Q": Q,
        "r": r,
        "last_term": last_term,
        "B1": B1,
        "B2": B2,
        "u_hat": uhat,
        "f_hat": fhat,
        "delta": delta,
        "epsilon": -mp.log(q2),
    }


def _mp_str(x: mp.mpf, digits: int = 32) -> str:
    return mp.nstr(x, digits)


def _serialize_components(values: Dict[str, mp.mpf], names: Iterable[str]) -> Dict[str, str]:
    return {name: _mp_str(values[name]) for name in names}


def _directed_tail_proxy(values: Dict[str, mp.mpf], terms: int) -> mp.mpf:
    """A displayed heuristic only; no interval claim is made here."""

    q = mp.e ** (-values["epsilon"] / 2)
    # The summand ratio is asymptotically q.  Use a deliberately labelled
    # geometric proxy based on the final computed moment term.
    return abs(values["last_term"]) / max(mp.mpf("1e-30"), 1 - abs(q * q))


def run_probe() -> Dict[str, object]:
    with mp.workdps(MP_DPS):
        phase = exact_phase_point()
        t_rat = phase.pop("_t_fraction")
        t = mp.mpf(t_rat.numerator) / t_rat.denominator

        values = _m8_components(t, MOMENT_END)
        half_values = _m8_components(t, MOMENT_END // 2)

        # mp.diff is applied at fixed N, fixed 60N split, and fixed finite
        # truncation.  This is the requested high-precision local diagnostic,
        # not a derivative of an asymptotic or an infinite sum.
        a_prime = mp.diff(mp_phase_coordinate, t, addprec=18)
        derivative_t: Dict[str, mp.mpf] = {}
        derivative_theta: Dict[str, mp.mpf] = {}
        derivative_names = ("boundary", "pre", "post", "rest", "F_sum", "F_direct")
        for name in derivative_names:
            derivative_t[name] = mp.diff(
                lambda x, component=name: _m8_components(x, MOMENT_END)[component],
                t,
                addprec=18,
            )
            derivative_theta[name] = derivative_t[name] / a_prime

        # Real-point tail diagnostics.  They are intentionally reported as
        # proxies, since the fixed truncations are not interval estimates.
        q = mp.e ** (-values["epsilon"] / 2)
        directed_tail = abs(t / (1 - t)) * q**DIRECTED_TERMS / max(
            mp.mpf("1e-30"), 1 - q
        )
        moment_tail_proxy = _directed_tail_proxy(values, MOMENT_END)

        phase["t_rational_midpoint"] = phase["t_rational_midpoint"]
        output: Dict[str, object] = {
            "kind": "exploratory_m11_decomposition_diagnostic",
            "certificate": False,
            "claim_scope": "N=32, theta=0.85 only",
            "N": N,
            "theta": "0.85",
            "target_phase": str(TARGET_PHASE),
            "phase": phase,
            "truncation": {
                "moment_end_exclusive": MOMENT_END,
                "moment_indices": f"0..{MOMENT_END - 1}",
                "directed_terms": DIRECTED_TERMS,
                "pre_indices": "0..32",
                "post_indices": "33..1920",
                "rest_indices": f"1921..{MOMENT_END - 1}",
                "mp_dps": MP_DPS,
                "tail_status": "fixed finite truncation; omitted tail is not rigorously bounded",
            },
            "values": _serialize_components(
                values,
                ("boundary", "pre", "post", "rest", "F_sum", "F_direct", "P", "H", "D", "D_I", "Q", "r", "epsilon"),
            ),
            "theta_derivatives": {
                name: _mp_str(derivative_theta[name]) for name in derivative_names
            },
            "t_derivatives": {name: _mp_str(derivative_t[name]) for name in derivative_names},
            "derivative_method": {
                "phase_coordinate": "a(t)=s_g/e from M5 kernel",
                "conversion": "d/dtheta=(d/dt)/a'(t)",
                "mp_diff_addprec": 18,
                "fixed_indices": True,
            },
            "consistency": {
                "value_decomposition_minus_direct": _mp_str(values["F_sum"] - values["F_direct"]),
                "theta_derivative_sum_minus_direct": _mp_str(
                    derivative_theta["F_sum"] - derivative_theta["F_direct"]
                ),
                "boundary_pre_post_rest_sum": _mp_str(
                    values["boundary"] + values["pre"] + values["post"] + values["rest"]
                ),
                "half_to_full_drifts": {
                    name: _mp_str(values[name] - half_values[name])
                    for name in ("pre", "post", "rest", "F_sum", "F_direct")
                },
            },
            "tail_proxies_nonrigorous": {
                "directed_sum_geometric_proxy": _mp_str(directed_tail),
                "moment_last_term_geometric_proxy": _mp_str(moment_tail_proxy),
                "explanation": "These proxies diagnose truncation only; they are not certified remainders.",
            },
            "interpretation": {
                "largest_component_by_abs": max(
                    ("boundary", "pre", "post", "rest"),
                    key=lambda name: abs(values[name]),
                ),
                "largest_theta_derivative_by_abs": max(
                    derivative_names,
                    key=lambda name: abs(derivative_theta[name]),
                ),
                "note": "Use component signs and theta derivatives to identify the obstruction to a uniform post-negativity proof; no asymptotic conclusion is asserted.",
            },
        }

        # Convert the remaining exact Fraction values to JSON strings and
        # ensure the result is deterministic and self-describing.
        return output


def main() -> None:
    result = run_probe()
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
