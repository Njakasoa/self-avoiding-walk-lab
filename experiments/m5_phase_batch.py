"""Source-frozen receipts for the M5 phase calibration and holdout.

The calibration mode calls :func:`experiments.m5_phase_diagnostics.run` with
its defaults and removes only the nondeterministic ``runtime_seconds`` field
before passing the payload to ``run_record``.  The validation mode is
deliberately separate: it reads a committed
``experiments/m5_holdout_protocol.json``, checks its calibration payload and
parameters, calls ``locate_root`` directly at the unique held-out index 512,
and compares the two pre-registered observables without refitting anything.

The protocol consumed by validation has this shape (all paths are repository
relative):

````json
{
  "schema_version": 1,
  "calibration_payload": "results/m5-phase-v1/payload.json",
  "calibration_payload_sha256": "...",
  "parameters": {
    "indices": [32, 64, 128, 256],
    "phases": ["0.75", "0.80", "0.85", "0.90"],
    "locator_dps": 52,
    "final_dps": 68,
    "locator_tail_scale": "9",
    "final_tail_scale": "12",
    "locator_D_tail_tolerance": "1e-12",
    "final_D_tail_tolerance": "1e-14",
    "refinement_steps": 8,
    "derivative_step": "1e-4",
    "max_seconds": 120.0,
    "certificate_payload": "results/w-critical-v1/payload.json"
  },
  "validation_index": 512,
  "theta_limit_midpoint": "...",
  "predictions": {
    "N2_sigma_minus_t": "...",
    "theta_limit_minus_theta_times_log_N": "..."
  },
  "tolerances": {
    "N2_sigma_minus_t": "...",
    "theta_limit_minus_theta_times_log_N": "..."
  }
}
````

Root should create and commit that protocol after the canonical calibration.
The tolerances are protocol data; this wrapper does not choose them.  The
intended policy is five times the largest calibration residual for each
observable.  A numerical comparison failure is retained in the validation
payload as ``passed: false`` rather than being discarded.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

from experiments import m5_phase_diagnostics as diagnostics
from src.provenance import ROOT, run_record, sha


PROTOCOL_DEFAULT = "experiments/m5_holdout_protocol.json"
CERTIFICATE_PAYLOAD = "results/w-critical-v1/payload.json"
OBSERVABLES = (
    "N2_sigma_minus_t",
    "theta_limit_minus_theta_times_log_N",
)


def _default_parameters() -> dict[str, Any]:
    """Return the exact diagnostic defaults used by calibration."""

    return {
        "indices": list(diagnostics.CALIBRATION_INDICES),
        "phases": list(diagnostics.DEFAULT_PHASES),
        "locator_dps": diagnostics.DEFAULT_LOCATOR_DPS,
        "final_dps": diagnostics.DEFAULT_FINAL_DPS,
        "locator_tail_scale": diagnostics.DEFAULT_LOCATOR_TAIL_SCALE,
        "final_tail_scale": diagnostics.DEFAULT_FINAL_TAIL_SCALE,
        "locator_D_tail_tolerance": diagnostics.DEFAULT_D_TAIL_TOLERANCE,
        "final_D_tail_tolerance": diagnostics.DEFAULT_FINAL_D_TAIL_TOLERANCE,
        "refinement_steps": 8,
        "derivative_step": "1e-4",
        "max_seconds": diagnostics.DEFAULT_MAX_SECONDS,
        "certificate_payload": CERTIFICATE_PAYLOAD,
    }


def _relative_path(value: str | Path, *, label: str) -> str:
    """Validate a repository-relative input path for provenance."""

    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{label} must be repository-relative: {value}")
    relative = path.as_posix()
    if not (ROOT / relative).is_file():
        raise FileNotFoundError(f"{label} does not exist: {relative}")
    return relative


def _read_json(relative: str, *, label: str) -> dict[str, Any]:
    path = ROOT / relative
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} is not valid JSON: {relative}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} must contain a JSON object: {relative}")
    return value


def _assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label} differs: expected {expected!r}, got {actual!r}")


def _calibration_source_paths() -> list[str]:
    """All files read by calibration or its numerical producer."""

    return [
        "experiments/m5_phase_batch.py",
        "experiments/m5_phase_diagnostics.py",
        "src/provenance.py",
        "requirements-lock.txt",
        CERTIFICATE_PAYLOAD,
    ]


def _validation_source_paths(protocol_path: str, calibration_path: str) -> list[str]:
    """All files read by validation, including the frozen references."""

    return _calibration_source_paths() + [protocol_path, calibration_path]


def _calibration_parameters_from_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Extract run controls from a completed calibration payload."""

    keys = (
        "indices",
        "phases",
        "locator_dps",
        "final_dps",
        "locator_tail_scale",
        "final_tail_scale",
        "locator_D_tail_tolerance",
        "final_D_tail_tolerance",
        "refinement_steps",
        "derivative_step",
        "max_seconds",
    )
    missing = [key for key in keys if key not in payload]
    if missing:
        raise ValueError(f"calibration payload lacks controls: {missing}")
    return {key: payload[key] for key in keys}


def _verify_protocol(protocol_path: str) -> tuple[dict[str, Any], dict[str, Any], str]:
    """Validate the committed holdout protocol and calibration payload."""

    protocol = _read_json(protocol_path, label="holdout protocol")
    _assert_equal(protocol.get("schema_version"), 1, "protocol schema_version")
    calibration_path = _relative_path(
        protocol.get("calibration_payload", ""),
        label="protocol calibration_payload",
    )
    recorded_hash = protocol.get("calibration_payload_sha256")
    if not isinstance(recorded_hash, str) or len(recorded_hash) != 64:
        raise ValueError("protocol calibration_payload_sha256 must be a SHA-256 hex string")
    actual_hash = sha(ROOT / calibration_path)
    _assert_equal(actual_hash, recorded_hash, "calibration payload SHA-256")

    calibration = _read_json(calibration_path, label="calibration payload")
    expected = _default_parameters()
    protocol_parameters = protocol.get("parameters")
    if not isinstance(protocol_parameters, dict):
        raise ValueError("protocol parameters must be an object")
    for key, value in expected.items():
        _assert_equal(protocol_parameters.get(key), value, f"protocol parameters.{key}")

    payload_parameters = _calibration_parameters_from_payload(calibration)
    for key, value in expected.items():
        if key == "certificate_payload":
            continue
        _assert_equal(payload_parameters[key], value, f"calibration payload {key}")
    _assert_equal(
        calibration.get("certificate_reference", {}).get("path"),
        expected["certificate_payload"],
        "calibration certificate reference",
    )
    _assert_equal(
        calibration.get("indices"),
        expected["indices"],
        "calibration indices",
    )
    _assert_equal(
        calibration.get("phases"),
        expected["phases"],
        "calibration phases",
    )
    _assert_equal(protocol.get("validation_index"), diagnostics.HELDOUT_INDEX, "validation index")
    calibration_indices = protocol_parameters.get("indices")
    if diagnostics.HELDOUT_INDEX in calibration_indices:
        raise ValueError("held-out N=512 must be absent from calibration indices")

    theta_limit = protocol.get("theta_limit_midpoint")
    if not isinstance(theta_limit, str):
        raise ValueError("protocol theta_limit_midpoint must be a decimal string")
    _assert_equal(
        theta_limit,
        calibration.get("certificate_reference", {}).get("theta_limit_midpoint"),
        "theta_limit_midpoint against calibration reference",
    )

    predictions = protocol.get("predictions")
    tolerances = protocol.get("tolerances")
    if not isinstance(predictions, dict) or not isinstance(tolerances, dict):
        raise ValueError("protocol predictions and tolerances must be objects")
    calibration_prediction = (
        calibration.get("calibration_fits", {}).get("prediction_for_heldout_512", {})
    )
    for key in OBSERVABLES:
        if not isinstance(predictions.get(key), str):
            raise ValueError(f"protocol prediction missing decimal string: {key}")
        if not isinstance(tolerances.get(key), str):
            raise ValueError(f"protocol tolerance missing decimal string: {key}")
        with diagnostics.mp.workdps(expected["final_dps"]):
            tolerance = diagnostics.mp.mpf(tolerances[key])
        if not tolerance > 0:
            raise ValueError(f"protocol tolerance must be positive: {key}")
        _assert_equal(
            predictions[key],
            calibration_prediction.get(key),
            f"protocol prediction {key} against calibration payload",
        )
    return protocol, calibration, calibration_path


def _calibration_producer() -> dict[str, Any]:
    """Run the diagnostic with defaults and remove only wall-clock output."""

    payload = diagnostics.run()
    payload.pop("runtime_seconds")
    return payload


def _validation_producer(
    protocol: dict[str, Any],
    calibration: dict[str, Any],
) -> dict[str, Any]:
    """Run the held-out root directly and preserve comparison failures."""

    parameters = protocol["parameters"]
    final_dps = int(parameters["final_dps"])
    started = time.perf_counter()
    deadline = started + float(parameters["max_seconds"])
    with diagnostics.mp.workdps(final_dps):
        locator_tail_scale = diagnostics.mp.mpf(str(parameters["locator_tail_scale"]))
        locator_d_tail_tolerance = diagnostics.mp.mpf(
            str(parameters["locator_D_tail_tolerance"])
        )
        final_tail_scale = diagnostics.mp.mpf(str(parameters["final_tail_scale"]))
        final_d_tail_tolerance = diagnostics.mp.mpf(
            str(parameters["final_D_tail_tolerance"])
        )
        derivative_step = diagnostics.mp.mpf(str(parameters["derivative_step"]))
        row = diagnostics.locate_root(
            diagnostics.HELDOUT_INDEX,
            list(parameters["phases"]),
            locator_dps=int(parameters["locator_dps"]),
            locator_tail_scale=locator_tail_scale,
            locator_d_tail_tolerance=locator_d_tail_tolerance,
            final_dps=final_dps,
            final_tail_scale=final_tail_scale,
            final_d_tail_tolerance=final_d_tail_tolerance,
            refinement_steps=int(parameters["refinement_steps"]),
            derivative_step=derivative_step,
            deadline=deadline,
        )
        theta_limit = diagnostics.mp.mpf(str(protocol["theta_limit_midpoint"]))
        theta_n = diagnostics.mp.mpf(str(row["theta_N"]))
        actual = {
            "N2_sigma_minus_t": diagnostics.mp.mpf(str(row["N2_sigma_minus_t_N"])),
            "theta_limit_minus_theta_times_log_N": (
                theta_limit - theta_n
            ) * diagnostics.mp.log(diagnostics.HELDOUT_INDEX),
        }
        comparisons: dict[str, Any] = {}
        for key in OBSERVABLES:
            predicted = diagnostics.mp.mpf(str(protocol["predictions"][key]))
            tolerance = diagnostics.mp.mpf(str(protocol["tolerances"][key]))
            error = abs(actual[key] - predicted)
            comparisons[key] = {
                "actual": diagnostics._decimal(actual[key]),
                "predicted": diagnostics._decimal(predicted),
                "absolute_error": diagnostics._decimal(error),
                "tolerance": diagnostics._decimal(tolerance),
                "passed": bool(error <= tolerance),
            }
        passed = all(item["passed"] for item in comparisons.values())
        elapsed = time.perf_counter() - started
        if elapsed > float(parameters["max_seconds"]):
            raise TimeoutError("M5 holdout validation exceeded max_seconds")
        return {
            "classification": "EXPLORATORY HELD-OUT VALIDATION DIAGNOSTIC ONLY",
            "status": "pass" if passed else "fail",
            "passed": passed,
            "warning": (
                "A failed tolerance comparison is retained as evidence; this "
                "payload does not refit predictions or establish an asymptotic theorem."
            ),
            "validation_index": diagnostics.HELDOUT_INDEX,
            "protocol": {
                "schema_version": protocol["schema_version"],
                "calibration_payload": protocol["calibration_payload"],
                "calibration_payload_sha256": protocol["calibration_payload_sha256"],
            },
            "calibration_reference": {
                "theta_limit_midpoint": protocol["theta_limit_midpoint"],
                "prediction_source": calibration["calibration_fits"][
                    "prediction_for_heldout_512"
                ],
            },
            "row": row,
            "comparisons": comparisons,
        }


def run(kind: str, experiment_id: str, protocol_path: str = PROTOCOL_DEFAULT) -> Path:
    """Create one source-frozen calibration or validation receipt."""

    if kind == "calibration":
        parameters = {"mode": "calibration", "diagnostic_defaults": _default_parameters()}
        command = f".venv/bin/python -m experiments.m5_phase_batch calibration {experiment_id}"
        return run_record(
            experiment_id,
            command,
            parameters,
            _calibration_source_paths(),
            _calibration_producer,
        )
    if kind != "validation":
        raise ValueError(f"unknown M5 batch kind: {kind}")

    protocol_rel = _relative_path(protocol_path, label="holdout protocol")
    protocol, calibration, calibration_path = _verify_protocol(protocol_rel)
    parameters = {
        "mode": "validation",
        "protocol": protocol_rel,
        "calibration_payload": calibration_path,
        "validation_index": diagnostics.HELDOUT_INDEX,
        "diagnostic_parameters": protocol["parameters"],
        "predictions": protocol["predictions"],
        "tolerances": protocol["tolerances"],
    }
    command = (
        f".venv/bin/python -m experiments.m5_phase_batch validation {experiment_id} "
        f"--protocol {protocol_rel}"
    )
    return run_record(
        experiment_id,
        command,
        parameters,
        _validation_source_paths(protocol_rel, calibration_path),
        lambda: _validation_producer(protocol, calibration),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("calibration", "validation"))
    parser.add_argument("experiment_id")
    parser.add_argument("--protocol", default=PROTOCOL_DEFAULT)
    args = parser.parse_args()
    print(run(args.kind, args.experiment_id, args.protocol))


if __name__ == "__main__":
    main()
