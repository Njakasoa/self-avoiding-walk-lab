"""Large-index numerical diagnostics for the weakly prudent bridge phase.

This experiment evaluates the Bacher--Beaton formulae directly.  It uses the
closed form of the Proposition 8 recurrence

    G_k=(t/q)**k * (beta + gamma*q**(2*k)),

and the finite Bacher--Beaton summands for ``P`` and ``H``.  It then locates a
zero of

    F=(3-t-2*D_I)*P - 4*H - (1+t+2*D_I)

as a function of the phase ``theta``.  The output is exploratory numerical
evidence only.  It contains no interval enclosure and makes no assertion
about an infinite tail, a unique root, a first effective index, or a rate of
convergence.

The default run is a calibration sweep at N=32,64,128,256.  N=512 is
deliberately rejected unless ``--include-heldout-512`` is supplied; that flag
is reserved for a later validation run after the calibration predictions have
been recorded and reviewed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path
from typing import Any, Iterable, Sequence

import mpmath as mp


CALIBRATION_INDICES = (32, 64, 128, 256)
HELDOUT_INDEX = 512
DEFAULT_PHASES = ("0.75", "0.80", "0.85", "0.90")
DEFAULT_LOCATOR_DPS = 52
DEFAULT_FINAL_DPS = 68
DEFAULT_LOCATOR_TAIL_SCALE = "9"
DEFAULT_FINAL_TAIL_SCALE = "12"
DEFAULT_D_TAIL_TOLERANCE = "1e-12"
DEFAULT_FINAL_D_TAIL_TOLERANCE = "1e-14"
DEFAULT_MAX_SECONDS = 120.0


def _decimal(value: mp.mpf, digits: int = 36) -> str:
    """Render an mpmath value without converting through binary float."""

    return mp.nstr(value, digits)


def _check_deadline(deadline: float | None) -> None:
    if deadline is not None and time.perf_counter() >= deadline:
        raise TimeoutError("M5 phase diagnostics exceeded max_seconds")


def kernel(t: mp.mpf, v: mp.mpf) -> mp.mpf:
    """The physical formal-series branch U(t,v) from BB2014."""

    a = 1 - t * v + t * t + t**3 * v
    return 2 * t / (a + mp.sqrt(a * a - 4 * t * t))


def phase_coordinate(t: mp.mpf) -> mp.mpf:
    """Return the BB phase coordinate a(t)=log(v)/log(q^2)."""

    q = kernel(t, mp.mpf(1))
    one_minus_tq = 1 - t * q
    u = t / one_minus_tq
    v = (u - t) * (1 - t * u) / (t * (1 - t * t) * u)
    return mp.log(v) / mp.log(q * q)


def phase_parameter(
    index: int,
    theta: mp.mpf,
    *,
    bisection: int = 150,
) -> mp.mpf:
    """Invert the phase coordinate below sigma by monotone bisection."""

    target = mp.mpf(index) + mp.mpf(theta)
    lo = mp.mpf("0.4")
    # Keep the endpoint below the square-root branch point at the current
    # precision.  The margin is much smaller than the requested output error.
    hi = mp.sqrt(2) - 1 - mp.mpf(10) ** (-mp.mp.dps + 12)
    if not phase_coordinate(lo) < target < phase_coordinate(hi):
        raise ArithmeticError(
            f"phase target {target} was not bracketed at dps={mp.mp.dps}"
        )
    for _ in range(bisection):
        mid = (lo + hi) / 2
        if phase_coordinate(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def directed_ramp_closed(
    t: mp.mpf,
    *,
    q: mp.mpf | None = None,
    tail_tolerance: mp.mpf = mp.mpf("1e-12"),
    max_terms: int = 2_000_000,
    deadline: float | None = None,
) -> dict[str, mp.mpf | int]:
    """Evaluate D from the closed form of G_k, with a geometric tail bound.

    The recurrence solution is

        G_k=(t/q)^k*(beta+gamma*q^(2k)),
        t^(k+1)/G_k=t*q^k/(beta+gamma*q^(2k)).

    For real 0<t<sigma the denominator is at least
    ``min(beta, beta+gamma)=min(beta,1-t)``.  The omitted tail is therefore
    bounded by ``t/m*q**n/(1-q)`` after n terms.  This is a numerical bound
    used to stop the summation; it is not a certified output interval.
    """

    t = mp.mpf(t)
    q = kernel(t, mp.mpf(1)) if q is None else mp.mpf(q)
    q2 = q * q
    beta = (1 - t - t * q) / (1 - q2)
    gamma = q * (t - q * (1 - t)) / (1 - q2)
    minimum_denominator = min(beta, 1 - t)
    if not (minimum_denominator > 0 and 0 < q < 1):
        raise ArithmeticError("closed-form D summation left its physical real branch")

    total = mp.mpf(0)
    q_power = mp.mpf(1)
    q2_power = mp.mpf(1)
    tail_bound = mp.inf
    used = 0
    for k in range(max_terms):
        if k % 512 == 0:
            _check_deadline(deadline)
        total += t * q_power / (beta + gamma * q2_power)
        used = k + 1
        q_power *= q
        q2_power *= q2
        tail_bound = t / minimum_denominator * q_power / (1 - q)
        if used >= 100 and tail_bound <= tail_tolerance:
            break
    else:
        raise TimeoutError(
            f"closed-form D summation exceeded max_terms={max_terms}"
        )
    return {
        "D": total,
        "terms": used,
        "tail_bound": tail_bound,
        "beta": beta,
        "gamma": gamma,
    }


def prudent_sums(
    t: mp.mpf,
    terms: int,
    *,
    deadline: float | None = None,
) -> dict[str, mp.mpf | int]:
    """Evaluate the direct finite BB sums for P and H.

    The summands are copied into this module rather than importing the earlier
    phase probe, so the large-index experiment has an independent driver and
    exposes the actual term count used at every phase.
    """

    t = mp.mpf(t)
    q = kernel(t, mp.mpf(1))
    q2 = q * q
    one = 1 - t * q
    q_minus_t = q - t
    one_minus_q2 = 1 - q2
    total_p = mp.mpf(0)
    total_h = mp.mpf(0)
    product = mp.mpf(1)
    v = mp.mpf(1)
    last_term = mp.mpf(0)

    for n in range(int(terms)):
        if n % 256 == 0:
            _check_deadline(deadline)
        u = kernel(t, v)
        w = kernel(t, v * q2)
        h = t * q - q_minus_t * u
        A = (
            q_minus_t
            * (1 - t * t)
            * (
                u * one
                - (q * q_minus_t + t * one_minus_q2 * u) * w
            )
            / (one * (1 - t * u) * (1 - t * w) * h)
        )
        B = q * q_minus_t**2 * (t - one * w) / (one * one * h)
        A_hook = (
            t
            * t
            * (1 - t * t)
            * q_minus_t
            * (
                one * u * u * (1 - 2 * t * w)
                - (
                    q * q_minus_t
                    - t
                    * u
                    * (2 * q * q_minus_t + t * one_minus_q2 * u)
                )
                * w
                * w
            )
            / (one * (1 - t * u) ** 2 * (1 - t * w) ** 2 * h)
        )
        term_p = product * A
        term_h = product * A_hook
        total_p += term_p
        total_h += term_h
        last_term = max(abs(term_p), abs(term_h))
        product *= B
        v *= q2

    P = q * (1 - t * t) / one + q * total_p
    H = t * t * q2 * (1 - t * t) / (one * one) + q * total_h
    return {
        "P": P,
        "H": H,
        "last_term": last_term,
        "terms": int(terms),
    }


def _term_count(epsilon: mp.mpf, scale: mp.mpf, minimum: int = 2_000) -> int:
    """Select a reproducible O(1/epsilon) direct-sum length."""

    return max(minimum, int(mp.ceil(scale / epsilon)))


def evaluate_phase(
    index: int,
    theta: str | mp.mpf,
    *,
    dps: int,
    prudent_tail_scale: mp.mpf,
    d_tail_tolerance: mp.mpf,
    deadline: float | None = None,
) -> dict[str, mp.mpf | int | str]:
    """Evaluate one finite phase using direct P,H and closed-form D."""

    with mp.workdps(dps):
        # Parse decimal inputs inside the requested precision context.  This
        # avoids silently importing a phase at the process-default precision.
        theta_mp = mp.mpf(str(theta))
        _check_deadline(deadline)
        t = phase_parameter(index, theta_mp)
        q = kernel(t, mp.mpf(1))
        epsilon = -mp.log(q * q)
        terms = _term_count(epsilon, mp.mpf(prudent_tail_scale))
        directed = directed_ramp_closed(
            t,
            q=q,
            tail_tolerance=mp.mpf(d_tail_tolerance),
            deadline=deadline,
        )
        sums = prudent_sums(t, terms, deadline=deadline)
        D = mp.mpf(directed["D"])
        D_I = D / (1 + D)
        P = mp.mpf(sums["P"])
        H = mp.mpf(sums["H"])
        F = (3 - t - 2 * D_I) * P - 4 * H - (1 + t + 2 * D_I)
        return {
            "index": int(index),
            "theta": _decimal(theta_mp),
            "t": _decimal(t),
            "q": _decimal(q),
            "epsilon_minus_log_q2": _decimal(epsilon),
            "prudent_terms": int(terms),
            "P": _decimal(P),
            "H": _decimal(H),
            "P_plus_one": _decimal(P + 1),
            "D": _decimal(D),
            "D_I": _decimal(D_I),
            "D_terms": int(directed["terms"]),
            "D_tail_bound": _decimal(mp.mpf(directed["tail_bound"])),
            "last_prudent_term": _decimal(mp.mpf(sums["last_term"])),
            "F": _decimal(F),
        }


def _as_mp(row: dict[str, Any], key: str) -> mp.mpf:
    return mp.mpf(str(row[key]))


def _sign(value: mp.mpf) -> str:
    return "positive" if value > 0 else "negative" if value < 0 else "zero"


def _cache_key(index: int, theta: mp.mpf, dps: int, scale: mp.mpf, d_tol: mp.mpf) -> tuple[Any, ...]:
    return (int(index), _decimal(theta, 30), int(dps), _decimal(scale, 20), _decimal(d_tol, 20))


def locate_root(
    index: int,
    phases: Sequence[str],
    *,
    locator_dps: int,
    locator_tail_scale: mp.mpf,
    locator_d_tail_tolerance: mp.mpf,
    final_dps: int,
    final_tail_scale: mp.mpf,
    final_d_tail_tolerance: mp.mpf,
    refinement_steps: int,
    derivative_step: mp.mpf,
    deadline: float | None = None,
) -> dict[str, Any]:
    """Scan a fixed phase grid, then refine the first sign-changing bracket."""

    cache: dict[tuple[Any, ...], dict[str, Any]] = {}

    def evaluate_cached(
        theta: mp.mpf,
        *,
        dps: int,
        scale: mp.mpf,
        d_tol: mp.mpf,
    ) -> dict[str, Any]:
        with mp.workdps(dps):
            theta_local = mp.mpf(str(theta))
            key = _cache_key(index, theta_local, dps, scale, d_tol)
            if key not in cache:
                cache[key] = evaluate_phase(
                    index,
                    theta_local,
                    dps=dps,
                    prudent_tail_scale=scale,
                    d_tail_tolerance=d_tol,
                    deadline=deadline,
                )
            return cache[key]

    # Decimal strings are parsed at the locator precision, not at import time.
    with mp.workdps(locator_dps):
        scan_theta = [mp.mpf(str(value)) for value in phases]
        scan_rows = [
            evaluate_cached(
                theta,
                dps=locator_dps,
                scale=locator_tail_scale,
                d_tol=locator_d_tail_tolerance,
            )
            for theta in scan_theta
        ]
        brackets: list[tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
        for left, right in zip(scan_rows, scan_rows[1:]):
            left_theta, right_theta = mp.mpf(left["theta"]), mp.mpf(right["theta"])
            left_f, right_f = mp.mpf(left["F"]), mp.mpf(right["F"])
            if left_f == 0:
                brackets.append((left_theta, left_theta, left_f, left_f))
            elif left_f * right_f < 0:
                brackets.append((left_theta, right_theta, left_f, right_f))
        if not brackets:
            raise ArithmeticError(
                f"no sign-changing F bracket found for N={index} on phases={phases}"
            )
        a, b, fa, fb = brackets[0]
        history: list[dict[str, str]] = []
        x_previous, f_previous = a, fa
        x_current, f_current = b, fb
        for iteration in range(refinement_steps):
            _check_deadline(deadline)
            if abs(f_current - f_previous) == 0:
                x_trial = (a + b) / 2
            else:
                x_trial = x_current - f_current * (x_current - x_previous) / (f_current - f_previous)
                if not (a < x_trial < b):
                    x_trial = (a + b) / 2
            trial = evaluate_cached(
                x_trial,
                dps=locator_dps,
                scale=locator_tail_scale,
                d_tol=locator_d_tail_tolerance,
            )
            f_trial = mp.mpf(trial["F"])
            history.append(
                {
                    "iteration": str(iteration),
                    "theta": _decimal(x_trial),
                    "F": _decimal(f_trial),
                }
            )
            if f_trial == 0:
                a = b = x_trial
                fa = fb = f_trial
                break
            if fa * f_trial < 0:
                b, fb = x_trial, f_trial
            else:
                a, fa = x_trial, f_trial
            x_previous, f_previous = x_current, f_current
            x_current, f_current = x_trial, f_trial
        locator_theta = x_current
        if not (a <= locator_theta <= b):
            locator_theta = (a + b) / 2

    # Re-evaluate at the high-precision locator point.  One Newton correction
    # uses the same direct finite formula; it is not a fitted root.
    with mp.workdps(final_dps):
        theta0 = mp.mpf(str(locator_theta))
        root_row = evaluate_cached(
            theta0,
            dps=final_dps,
            scale=final_tail_scale,
            d_tol=final_d_tail_tolerance,
        )
        h = mp.mpf(derivative_step)
        left_row = evaluate_cached(
            theta0 - h,
            dps=final_dps,
            scale=final_tail_scale,
            d_tol=final_d_tail_tolerance,
        )
        right_row = evaluate_cached(
            theta0 + h,
            dps=final_dps,
            scale=final_tail_scale,
            d_tol=final_d_tail_tolerance,
        )
        derivative0 = (
            mp.mpf(right_row["F"]) - mp.mpf(left_row["F"])
        ) / (2 * h)
        if derivative0 != 0:
            theta1 = theta0 - mp.mpf(root_row["F"]) / derivative0
        else:
            theta1 = theta0
        if a < theta1 < b:
            corrected = evaluate_cached(
                theta1,
                dps=final_dps,
                scale=final_tail_scale,
                d_tol=final_d_tail_tolerance,
            )
            if abs(mp.mpf(corrected["F"])) < abs(mp.mpf(root_row["F"])):
                theta0, root_row = theta1, corrected
        # Derivative is recomputed at the selected point, so it is tied to the
        # reported theta rather than to the pre-correction locator.
        left_row = evaluate_cached(
            theta0 - h,
            dps=final_dps,
            scale=final_tail_scale,
            d_tol=final_d_tail_tolerance,
        )
        right_row = evaluate_cached(
            theta0 + h,
            dps=final_dps,
            scale=final_tail_scale,
            d_tol=final_d_tail_tolerance,
        )
        derivative = (
            mp.mpf(right_row["F"]) - mp.mpf(left_row["F"])
        ) / (2 * h)
        sigma = mp.sqrt(2) - 1
        t_root = mp.mpf(root_row["t"])
        return {
            "index": int(index),
            "scan": [
                {
                    "theta": row["theta"],
                    "F": row["F"],
                    "F_sign": _sign(mp.mpf(row["F"])),
                }
                for row in scan_rows
            ],
            "sign_changing_brackets": [
                [_decimal(x), _decimal(y)] for x, y, _, _ in brackets
            ],
            "locator_history": history,
            "theta_N": _decimal(theta0),
            "theta_N_locator_dps": locator_dps,
            "F_at_theta_N": root_row["F"],
            "F_theta_numeric": _decimal(derivative),
            "F_theta_step": _decimal(h),
            "t_N": root_row["t"],
            "sigma_minus_t_N": _decimal(sigma - t_root),
            "N2_sigma_minus_t_N": _decimal(index * index * (sigma - t_root)),
            "D_I_at_theta_N": root_row["D_I"],
            "P_plus_one_at_theta_N": root_row["P_plus_one"],
            "H_at_theta_N": root_row["H"],
            "prudent_terms_at_theta_N": root_row["prudent_terms"],
            "D_terms_at_theta_N": root_row["D_terms"],
            "D_tail_bound_at_theta_N": root_row["D_tail_bound"],
            "last_prudent_term_at_theta_N": root_row["last_prudent_term"],
            "locator_parameters": {
                "dps": locator_dps,
                "tail_scale": _decimal(locator_tail_scale),
                "D_tail_tolerance": _decimal(locator_d_tail_tolerance),
                "refinement_steps": refinement_steps,
            },
            "final_parameters": {
                "dps": final_dps,
                "tail_scale": _decimal(final_tail_scale),
                "D_tail_tolerance": _decimal(final_d_tail_tolerance),
            },
        }


def _certificate_midpoints(path: Path, dps: int) -> dict[str, Any]:
    """Read the existing critical certificate without changing it."""

    raw = path.read_bytes()
    payload = json.loads(raw.decode("utf-8"))
    if payload.get("classification") != "EXACT W LIMIT SIGNS; analytic transfer is separate":
        raise ValueError("unexpected w-critical-v1 classification")
    bits = int(payload["integrals"][0][0]["denominator_power_of_two"])
    with mp.workdps(dps):
        scale = mp.mpf(2) ** bits
        intervals: list[tuple[mp.mpf, mp.mpf]] = []
        for row in payload["integrals"]:
            for value in row:
                intervals.append(
                    (
                        mp.mpf(value["lower_numerator"]) / scale,
                        mp.mpf(value["upper_numerator"]) / scale,
                    )
                )
        midpoint = tuple((lo + hi) / 2 for lo, hi in intervals)
        sigma = mp.sqrt(2) - 1
        eta = 1 / mp.sqrt(2)
        d = 1 - sigma
        A = 1 / (sigma * sigma)

        def f0(theta: mp.mpf, values: Sequence[mp.mpf]) -> mp.mpf:
            j1_pre, j2_pre, j1_post, j2_post = values
            B = A * mp.sin(mp.pi * theta) / mp.sin(mp.pi * (eta - theta))
            P = -d - A * j1_pre + B * j1_post
            H = sigma * sigma * (-3 - A * j2_pre + B * j2_post)
            return d * P - 4 * H - (3 + sigma)

        def root_for(values: Sequence[mp.mpf]) -> mp.mpf:
            lo, hi = mp.mpf("0.8"), mp.mpf("0.9")
            flo, fhi = f0(lo, values), f0(hi, values)
            if not flo > 0 > fhi:
                raise ArithmeticError("certificate midpoint/corner lost endpoint signs")
            for _ in range(180):
                middle = (lo + hi) / 2
                if f0(middle, values) > 0:
                    lo = middle
                else:
                    hi = middle
            return (lo + hi) / 2

        midpoint_root = root_for(midpoint)
        # The four interval enclosures are independent inputs.  This corner
        # box is a conservative diagnostic for reference uncertainty; the
        # certificate itself proves endpoint signs, not this root enclosure.
        corners: list[mp.mpf] = []
        import itertools

        for choice in itertools.product((0, 1), repeat=4):
            values = tuple(intervals[i][choice[i]] for i in range(4))
            corners.append(root_for(values))
        return {
            "path": str(path),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bins": int(payload["bins"]),
            "power_bits": int(payload["power_bits"]),
            "integral_midpoints": [_decimal(value) for value in midpoint],
            "theta_limit_midpoint": _decimal(midpoint_root),
            "theta_limit_interval_corner_box": [
                _decimal(min(corners)),
                _decimal(max(corners)),
            ],
            "warning": (
                "The midpoint root is a fixed reference reconstructed from the "
                "existing interval certificate. It is not a new interval-certified "
                "root and is never fitted to finite N data."
            ),
        }


def _linear_fit(x_values: Sequence[mp.mpf], y_values: Sequence[mp.mpf]) -> dict[str, Any]:
    """Least-squares affine fit, used only for the calibration prediction."""

    if len(x_values) != len(y_values) or len(x_values) < 2:
        raise ValueError("at least two paired values are required")
    n = mp.mpf(len(x_values))
    sx = mp.fsum(x_values)
    sy = mp.fsum(y_values)
    sxx = mp.fsum(x * x for x in x_values)
    sxy = mp.fsum(x * y for x, y in zip(x_values, y_values))
    denominator = n * sxx - sx * sx
    if denominator == 0:
        raise ArithmeticError("singular calibration fit")
    slope = (n * sxy - sx * sy) / denominator
    intercept = (sy - slope * sx) / n
    residuals = [y - (intercept + slope * x) for x, y in zip(x_values, y_values)]
    return {
        "intercept": _decimal(intercept),
        "slope": _decimal(slope),
        "max_abs_residual": _decimal(max(abs(r) for r in residuals)),
    }


def run(
    *,
    indices: Iterable[int] = CALIBRATION_INDICES,
    phases: Iterable[str] = DEFAULT_PHASES,
    locator_dps: int = DEFAULT_LOCATOR_DPS,
    final_dps: int = DEFAULT_FINAL_DPS,
    locator_tail_scale: str = DEFAULT_LOCATOR_TAIL_SCALE,
    final_tail_scale: str = DEFAULT_FINAL_TAIL_SCALE,
    locator_d_tail_tolerance: str = DEFAULT_D_TAIL_TOLERANCE,
    final_d_tail_tolerance: str = DEFAULT_FINAL_D_TAIL_TOLERANCE,
    refinement_steps: int = 8,
    derivative_step: str = "1e-4",
    max_seconds: float = DEFAULT_MAX_SECONDS,
    include_heldout_512: bool = False,
    certificate_payload: str | Path = "results/w-critical-v1/payload.json",
) -> dict[str, Any]:
    """Run the calibration sweep and fixed-reference extrapolations."""

    selected = [int(index) for index in indices]
    if not selected or selected != sorted(set(selected)):
        raise ValueError("indices must be a nonempty strictly increasing list")
    if any(index > 256 for index in selected):
        if not include_heldout_512 or any(index != HELDOUT_INDEX for index in selected if index > 256):
            raise ValueError(
                "indices above 256 are held out; pass include_heldout_512 explicitly "
                "for the reserved N=512 validation"
            )
    if type(locator_dps) is not int or locator_dps < 35:
        raise ValueError("locator_dps must be an integer >= 35")
    if type(final_dps) is not int or final_dps < locator_dps:
        raise ValueError("final_dps must be >= locator_dps")
    if refinement_steps < 1:
        raise ValueError("refinement_steps must be positive")
    if max_seconds <= 0:
        raise ValueError("max_seconds must be positive")

    selected_phases = [str(value) for value in phases]
    if selected_phases != sorted(set(selected_phases)):
        raise ValueError("phases must be strictly increasing strings")
    # Parse only inside a precision context, then validate the actual values.
    with mp.workdps(max(final_dps, locator_dps)):
        phase_values = [mp.mpf(value) for value in selected_phases]
        if any(not (mp.mpf("0.70") < value < mp.mpf("0.95")) for value in phase_values):
            raise ValueError("phases must lie in the exploratory interval (0.70,0.95)")
        if len(phase_values) < 3:
            raise ValueError("at least three scan phases are required")

    started = time.perf_counter()
    deadline = started + float(max_seconds)
    locator_scale = str(locator_tail_scale)
    final_scale = str(final_tail_scale)
    locator_d_tol = str(locator_d_tail_tolerance)
    final_d_tol = str(final_d_tail_tolerance)
    cert_path = Path(certificate_payload)
    if not cert_path.exists():
        raise FileNotFoundError(cert_path)
    reference = _certificate_midpoints(cert_path, final_dps)
    rows: list[dict[str, Any]] = []
    # Convert all decimal controls while the final precision is active.  A
    # conversion at the process-default precision would silently round the
    # controls before locate_root enters its own workdps contexts.
    with mp.workdps(final_dps):
        locator_scale_mp = mp.mpf(locator_scale)
        locator_d_tol_mp = mp.mpf(locator_d_tol)
        final_scale_mp = mp.mpf(final_scale)
        final_d_tol_mp = mp.mpf(final_d_tol)
        derivative_step_mp = mp.mpf(str(derivative_step))
        for index in selected:
            _check_deadline(deadline)
            rows.append(
                locate_root(
                    index,
                    selected_phases,
                    locator_dps=locator_dps,
                    locator_tail_scale=locator_scale_mp,
                    locator_d_tail_tolerance=locator_d_tol_mp,
                    final_dps=final_dps,
                    final_tail_scale=final_scale_mp,
                    final_d_tail_tolerance=final_d_tol_mp,
                    refinement_steps=refinement_steps,
                    derivative_step=derivative_step_mp,
                    deadline=deadline,
                )
            )

    with mp.workdps(final_dps):
        theta_limit = mp.mpf(reference["theta_limit_midpoint"])
        sigma = mp.sqrt(2) - 1
        for row in rows:
            theta_n = mp.mpf(row["theta_N"])
            row["theta_limit_minus_theta_N"] = _decimal(theta_limit - theta_n)
            row["theta_limit_minus_theta_N_times_log_N"] = _decimal(
                (theta_limit - theta_n) * mp.log(row["index"])
            )

        calibration_rows = [row for row in rows if row["index"] <= 256]
        x_w = [mp.mpf(1) / row["index"] for row in calibration_rows]
        y_w = [mp.mpf(row["N2_sigma_minus_t_N"]) for row in calibration_rows]
        x_theta = [1 / mp.log(row["index"]) for row in calibration_rows]
        y_theta = [
            (theta_limit - mp.mpf(row["theta_N"])) * mp.log(row["index"])
            for row in calibration_rows
        ]
        fit_w = _linear_fit(x_w, y_w)
        fit_theta = _linear_fit(x_theta, y_theta)
        n_validation = mp.mpf(HELDOUT_INDEX)
        predicted_scaled_w_512 = mp.mpf(fit_w["intercept"]) + mp.mpf(fit_w["slope"]) / n_validation
        predicted_offset_512 = mp.mpf(fit_theta["intercept"]) + mp.mpf(fit_theta["slope"]) / mp.log(n_validation)
        predicted_theta_512 = theta_limit - predicted_offset_512 / mp.log(n_validation)
        elapsed = time.perf_counter() - started
        if elapsed > max_seconds:
            raise TimeoutError("M5 phase diagnostics exceeded max_seconds")
        return {
            "classification": "EXPLORATORY NUMERICAL AND CALIBRATION EXTRAPOLATION ONLY",
            "status": "held-out N=512 not run" if not include_heldout_512 else "explicit held-out validation requested",
            "warning": (
                "Finite direct sums and the closed-form D truncation are numerical. "
                "No tail, root uniqueness, sign persistence, rate theorem, or "
                "non-D-finiteness conclusion follows from this receipt."
            ),
            "runtime_seconds": elapsed,
            "max_seconds": max_seconds,
            "indices": selected,
            "calibration_indices": [row["index"] for row in calibration_rows],
            "heldout_index": HELDOUT_INDEX,
            "phases": selected_phases,
            "locator_dps": locator_dps,
            "final_dps": final_dps,
            "locator_tail_scale": locator_scale,
            "final_tail_scale": final_scale,
            "locator_D_tail_tolerance": locator_d_tol,
            "final_D_tail_tolerance": final_d_tol,
            "refinement_steps": refinement_steps,
            "derivative_step": str(derivative_step),
            "sigma": _decimal(sigma),
            "certificate_reference": reference,
            "rows": rows,
            "calibration_fits": {
                "N2_sigma_minus_t_vs_1_over_N": fit_w,
                "theta_offset_log_vs_1_over_log_N": fit_theta,
                "prediction_for_heldout_512": {
                    "N": HELDOUT_INDEX,
                    "N2_sigma_minus_t": _decimal(predicted_scaled_w_512),
                    "theta_limit_minus_theta_times_log_N": _decimal(predicted_offset_512),
                    "theta_N": _decimal(predicted_theta_512),
                    "warning": "Prediction is fixed using N<=256 only; N=512 is not included in either fit.",
                },
            },
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="write JSON to this path instead of stdout")
    parser.add_argument("--indices", nargs="+", type=int, default=list(CALIBRATION_INDICES))
    parser.add_argument("--phases", nargs="+", default=list(DEFAULT_PHASES))
    parser.add_argument("--locator-dps", type=int, default=DEFAULT_LOCATOR_DPS)
    parser.add_argument("--final-dps", type=int, default=DEFAULT_FINAL_DPS)
    parser.add_argument("--locator-tail-scale", default=DEFAULT_LOCATOR_TAIL_SCALE)
    parser.add_argument("--final-tail-scale", default=DEFAULT_FINAL_TAIL_SCALE)
    parser.add_argument("--locator-d-tail-tolerance", default=DEFAULT_D_TAIL_TOLERANCE)
    parser.add_argument("--final-d-tail-tolerance", default=DEFAULT_FINAL_D_TAIL_TOLERANCE)
    parser.add_argument("--refinement-steps", type=int, default=8)
    parser.add_argument("--derivative-step", default="1e-4")
    parser.add_argument("--max-seconds", type=float, default=DEFAULT_MAX_SECONDS)
    parser.add_argument("--certificate-payload", default="results/w-critical-v1/payload.json")
    parser.add_argument(
        "--include-heldout-512",
        action="store_true",
        help="explicitly permit the reserved N=512 validation run",
    )
    args = parser.parse_args()
    result = run(
        indices=args.indices,
        phases=args.phases,
        locator_dps=args.locator_dps,
        final_dps=args.final_dps,
        locator_tail_scale=args.locator_tail_scale,
        final_tail_scale=args.final_tail_scale,
        locator_d_tail_tolerance=args.locator_d_tail_tolerance,
        final_d_tail_tolerance=args.final_d_tail_tolerance,
        refinement_steps=args.refinement_steps,
        derivative_step=args.derivative_step,
        max_seconds=args.max_seconds,
        include_heldout_512=args.include_heldout_512,
        certificate_payload=args.certificate_payload,
    )
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
