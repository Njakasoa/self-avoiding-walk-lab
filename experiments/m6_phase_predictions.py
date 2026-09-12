"""M6 phase predictions from frozen M5 inputs.

This module is a read-only calibration producer. It reads the 4096-bin
critical integral payload, the M5 phase rows at N=32,64,128,256, and the
separate held-out row at N=512. It computes the midpoint constants
theta_star, C1, C2 and b at 68 decimal digits, then evaluates the
second-order logarithmic phase approximation and the resummed phase equation
from proofs/M6_SECOND_ORDER.md and proofs/M6_RESUMMED_PHASE.md.

The N=1024 entries produced here are theoretical evaluations of those two
closed formulae. No finite-N W sum, root, or diagnostic is evaluated at
N=1024 in this module.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
CRITICAL_PAYLOAD = "results/m5-critical-v1/payload.json"
PHASE_PAYLOAD = "results/m5-phase-v1/payload.json"
HELDOUT_PAYLOAD = "results/m5-phase-holdout-v1/payload.json"

CALIBRATION_INDICES = (32, 64, 128, 256)
OBSERVED_INDICES = CALIBRATION_INDICES + (512,)
PREDICTION_INDICES = OBSERVED_INDICES + (1024,)
MODEL_NAMES = ("truncated_2nd", "resummed")
DEFAULT_DPS = 68
DEFAULT_PHASES = ("0.75", "0.80", "0.85", "0.90")

# The phase diagnostic controls are copied from M5. Only the wall-clock
# budget changes for the reserved M6 validation call.
DIAGNOSTIC_PARAMETERS: dict[str, Any] = {
    "calibration_indices": list(CALIBRATION_INDICES),
    "observed_holdout_index": 512,
    "validation_index": 1024,
    "phases": list(DEFAULT_PHASES),
    "locator_dps": 52,
    "final_dps": 68,
    "locator_tail_scale": "9",
    "final_tail_scale": "12",
    "locator_D_tail_tolerance": "1e-12",
    "final_D_tail_tolerance": "1e-14",
    "refinement_steps": 8,
    "derivative_step": "1e-4",
    "max_seconds": 360.0,
}


def _decimal(value: mp.mpf, digits: int = 48) -> str:
    """Render an mpmath value without a binary-float conversion."""

    return mp.nstr(value, digits)


def _read_json(relative: str) -> dict[str, Any]:
    path = ROOT / relative
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{relative} must contain a JSON object")
    return value


def _assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def _load_inputs() -> tuple[dict[str, Any], dict[int, dict[str, Any]], dict[str, Any]]:
    """Read only the frozen M5 payload fields used by calibration."""

    critical = _read_json(CRITICAL_PAYLOAD)
    _assert_equal(
        critical.get("classification"),
        "EXACT LIMIT-FUNCTION CERTIFICATE; finite asymptotics need analytic transfer",
        "critical payload classification",
    )
    _assert_equal(critical.get("bins"), 4096, "critical payload bins")
    integrals = critical.get("integrals")
    if (
        not isinstance(integrals, list)
        or len(integrals) != 2
        or any(not isinstance(row, list) or len(row) != 2 for row in integrals)
    ):
        raise ValueError("critical payload must contain two pairs of integrals")
    for row in integrals:
        for value in row:
            if int(value.get("denominator_power_of_two", -1)) != 384:
                raise ValueError("critical integral precision is not the expected 384 bits")

    phase = _read_json(PHASE_PAYLOAD)
    _assert_equal(
        phase.get("classification"),
        "EXPLORATORY NUMERICAL AND CALIBRATION EXTRAPOLATION ONLY",
        "phase payload classification",
    )
    phase_rows_raw = phase.get("rows")
    if not isinstance(phase_rows_raw, list):
        raise ValueError("M5 phase payload rows must be a list")
    phase_rows = {int(row["index"]): row for row in phase_rows_raw}
    if set(phase_rows) != set(CALIBRATION_INDICES):
        raise ValueError(
            "M6 calibration must use exactly the M5 phase rows N=32,64,128,256"
        )

    heldout = _read_json(HELDOUT_PAYLOAD)
    _assert_equal(
        heldout.get("classification"),
        "EXPLORATORY HELD-OUT VALIDATION DIAGNOSTIC ONLY",
        "held-out payload classification",
    )
    _assert_equal(heldout.get("validation_index"), 512, "held-out validation index")
    heldout_row = heldout.get("row")
    if not isinstance(heldout_row, dict) or int(heldout_row.get("index", -1)) != 512:
        raise ValueError("held-out payload must contain exactly the N=512 row")

    # These are observed inputs only. In particular, a future N=1024 row
    # cannot be smuggled into calibration under a different payload key.
    if 1024 in phase_rows or int(heldout_row.get("index", -1)) == 1024:
        raise ValueError("observed M5 inputs unexpectedly contain N=1024")
    return critical, phase_rows, heldout_row


def _midpoint(value: Mapping[str, Any], dps: int) -> mp.mpf:
    bits = int(value["denominator_power_of_two"])
    with mp.workdps(dps):
        scale = mp.mpf(2) ** bits
        lo = mp.mpf(str(value["lower_numerator"])) / scale
        hi = mp.mpf(str(value["upper_numerator"])) / scale
        return (lo + hi) / 2


def _critical_midpoints(
    critical: Mapping[str, Any], dps: int
) -> tuple[list[mp.mpf], mp.mpf]:
    integrals = critical["integrals"]
    values = [_midpoint(value, dps) for row in integrals for value in row]
    s_star = _midpoint(critical["s_star"]["exact"], dps)
    return values, s_star


def _profile(
    theta: mp.mpf,
    *,
    sigma: mp.mpf,
    eta: mp.mpf,
    A: mp.mpf,
    d: mp.mpf,
    pre1: mp.mpf,
    pre2: mp.mpf,
    post1: mp.mpf,
    post2: mp.mpf,
) -> dict[str, mp.mpf]:
    angle = mp.pi * (eta - theta)
    B = A * mp.sin(mp.pi * theta) / mp.sin(angle)
    P = -d - A * pre1 + post1 * B
    H = sigma * sigma * (-3 - A * pre2 + post2 * B)
    F0 = d * P - 4 * H - (3 + sigma)
    return {"B": B, "P": P, "H": H, "F0": F0}


def _bisect(
    function,
    lo: mp.mpf,
    hi: mp.mpf,
    *,
    increasing: bool,
    iterations: int = 240,
) -> mp.mpf:
    flo = function(lo)
    fhi = function(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if increasing:
        bracketed = flo < 0 < fhi
    else:
        bracketed = flo > 0 > fhi
    if not bracketed:
        raise ArithmeticError(
            f"root was not bracketed: f(lo)={flo!r}, f(hi)={fhi!r}"
        )
    for _ in range(iterations):
        middle = (lo + hi) / 2
        fmid = function(middle)
        if fmid == 0:
            return middle
        if increasing:
            if fmid > 0:
                hi = middle
            else:
                lo = middle
        elif fmid > 0:
            lo = middle
        else:
            hi = middle
    return (lo + hi) / 2


def _compute_constants(
    critical: Mapping[str, Any], dps: int = DEFAULT_DPS
) -> dict[str, mp.mpf]:
    """Compute M6 constants from midpoint critical integrals only."""

    with mp.workdps(dps):
        values, s_star = _critical_midpoints(critical, dps)
        pre1, pre2, post1, post2 = values
        sigma = mp.sqrt(2) - 1
        eta = 1 / mp.sqrt(2)
        A = 1 / (sigma * sigma)
        d = 1 - sigma

        def f0(theta: mp.mpf) -> mp.mpf:
            return _profile(
                theta,
                sigma=sigma,
                eta=eta,
                A=A,
                d=d,
                pre1=pre1,
                pre2=pre2,
                post1=post1,
                post2=post2,
            )["F0"]

        bracket = critical["unique_theta_star_bracket"]
        theta_lo = mp.mpf(str(bracket[0]))
        theta_hi = mp.mpf(str(bracket[1]))
        theta_star = _bisect(f0, theta_lo, theta_hi, increasing=False)

        angle = mp.pi * (eta - theta_star)
        sin_angle = mp.sin(angle)
        B = A * mp.sin(mp.pi * theta_star) / sin_angle
        B_prime = A * mp.pi * mp.sin(mp.pi * eta) / (sin_angle * sin_angle)
        p_star = sigma - A * pre1 + post1 * B
        p0 = sigma - A * pre1
        J = d * post1 - 4 * sigma * sigma * post2
        f_star = J * B_prime
        C1 = 2 * sigma * p_star / f_star
        c_D = (mp.log(4) - mp.digamma(2 + mp.sqrt(2))) / sigma
        b = sigma * (1 + c_D) - mp.log(s_star)
        C0 = (
            d * (-d - A * pre1)
            - 4 * sigma * sigma * (-3 - A * pre2)
            - (3 + sigma)
        )
        C2 = (
            C1 * (b + 2 * sigma * post1 / J)
            - mp.pi * (mp.cos(angle) / mp.sin(angle)) * C1 * C1
        )
        return {
            "sigma": sigma,
            "eta": eta,
            "s_star": s_star,
            "theta_star": theta_star,
            "c_D": c_D,
            "b": b,
            "C0": C0,
            "J": J,
            "p0": p0,
            "p_star": p_star,
            "f_star": f_star,
            "C1": C1,
            "C2": C2,
            "post1": post1,
        }


def _phase_B(theta: mp.mpf, constants: Mapping[str, mp.mpf]) -> mp.mpf:
    return constants["sigma"] ** -2 * mp.sin(mp.pi * theta) / mp.sin(
        mp.pi * (constants["eta"] - theta)
    )


def produce_calibration(dps: int = DEFAULT_DPS) -> dict[str, Any]:
    """Produce calibration and theoretical predictions without N=1024 data."""

    critical, phase_rows, heldout_row = _load_inputs()
    with mp.workdps(dps):
        constants = _compute_constants(critical, dps=dps)
        truncated: dict[str, str] = {}
        resummed: dict[str, str] = {}
        for index in PREDICTION_INDICES:
            N = mp.mpf(index)
            L = mp.log(N)
            truncated_theta = (
                constants["theta_star"]
                - constants["C1"] / L
                + constants["C2"] / (L * L)
            )
            delta_hat = constants["sigma"] / (L + constants["b"])
            B_target = -(
                constants["C0"] + 2 * delta_hat * constants["p0"]
            ) / (constants["J"] + 2 * delta_hat * constants["post1"])
            theta_resummed = _bisect(
                lambda theta: _phase_B(theta, constants) - B_target,
                mp.mpf("0.75"),
                mp.mpf("0.90"),
                increasing=True,
            )
            truncated[str(index)] = _decimal(truncated_theta)
            resummed[str(index)] = _decimal(theta_resummed)

        observed: dict[str, str] = {
            str(index): str(phase_rows[index]["theta_N"])
            for index in CALIBRATION_INDICES
        }
        observed["512"] = str(heldout_row["theta_N"])
        observed_512 = mp.mpf(observed["512"])
        tolerance = 2 * abs(mp.mpf(resummed["512"]) - observed_512)
        if not tolerance > 0:
            raise ArithmeticError("benchmark tolerance must be positive")
        errors = {
            "truncated_2nd": abs(mp.mpf(truncated["512"]) - observed_512),
            "resummed": abs(mp.mpf(resummed["512"]) - observed_512),
        }
        passes = {name: bool(errors[name] <= tolerance) for name in MODEL_NAMES}

        parameters = {
            "prediction_dps": dps,
            "critical_bins": 4096,
            "critical_midpoint_rule": "midpoint of each 384-bit interval",
            "calibration_indices": list(CALIBRATION_INDICES),
            "observed_indices": list(OBSERVED_INDICES),
            "prediction_indices": list(PREDICTION_INDICES),
            "models": list(MODEL_NAMES),
            "diagnostic": DIAGNOSTIC_PARAMETERS,
        }
        return {
            "classification": (
                "M6 PHASE PREDICTION CALIBRATION; theoretical N=1024 only; "
                "no finite N=1024 observation"
            ),
            "status": "calibration complete",
            "warning": (
                "The benchmark is a diagnostic comparison only. A failed "
                "two-order comparison is retained and does not refute the "
                "asymptotic theorem or the resummed formula."
            ),
            "parameters": parameters,
            "input_payloads": {
                "critical": CRITICAL_PAYLOAD,
                "phase_calibration": PHASE_PAYLOAD,
                "heldout_512": HELDOUT_PAYLOAD,
            },
            "constants": {
                key: _decimal(value) for key, value in constants.items()
            },
            "observed": observed,
            "predictions": {
                "truncated_2nd": truncated,
                "resummed": resummed,
            },
            "theoretical_only_indices": [1024],
            "tolerances": {
                "common_512_benchmark": _decimal(tolerance),
                "truncated_2nd": _decimal(tolerance),
                "resummed": _decimal(tolerance),
            },
            "benchmark": {
                "observed_index": 512,
                "rule": "2*abs(resummed[512]-observed[512])",
                "errors": {key: _decimal(value) for key, value in errors.items()},
                "passed": passes,
            },
        }


if __name__ == "__main__":
    print(json.dumps(produce_calibration(), indent=2, sort_keys=True))
