"""Source-frozen M6 phase prediction calibration and N=1024 validation.

Calibration is a pure replay of frozen M5 payloads. It computes midpoint
constants and two theoretical phase predictions at N=32,64,128,256,512,1024;
the calibration never evaluates a finite-N diagnostic at N=1024.

Root creates and commits the protocol after calibration. The protocol shape is

{
  "schema_version": 1,
  "calibration_payload": "results/m6-phase-predictions-v1/payload.json",
  "calibration_payload_sha256": "...",
  "parameters": { ...exact calibration parameters... },
  "constants": { ...exact calibration constants... },
  "predictions": {
    "truncated_2nd": {"32": "...", ..., "1024": "..."},
    "resummed": {"32": "...", ..., "1024": "..."}
  },
  "tolerances": { ...exact calibration tolerances... },
  "observed_holdout_index": 512,
  "validation_index": 1024
}

Validation verifies those fields and the calibration hash, rejects any
observed N=1024 input, then calls m5_phase_diagnostics.locate_root(1024)
directly. It never calls m5_phase_diagnostics.run() and never refits either
prediction. Truncation and resummed comparisons remain separate pass/fail
diagnostics.
"""

from __future__ import annotations

import argparse
import copy
import json
import time
from pathlib import Path
from typing import Any

from experiments import m6_phase_predictions as predictions
from src.provenance import ROOT, run_record, sha


PROTOCOL_DEFAULT = "experiments/m6_phase_protocol.json"


def _expected_parameters() -> dict[str, Any]:
    return {
        "prediction_dps": predictions.DEFAULT_DPS,
        "critical_bins": 4096,
        "critical_midpoint_rule": "midpoint of each 384-bit interval",
        "calibration_indices": list(predictions.CALIBRATION_INDICES),
        "observed_indices": list(predictions.OBSERVED_INDICES),
        "prediction_indices": list(predictions.PREDICTION_INDICES),
        "models": list(predictions.MODEL_NAMES),
        "diagnostic": copy.deepcopy(predictions.DIAGNOSTIC_PARAMETERS),
    }


def _relative_path(value: str | Path, *, label: str) -> str:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{label} must be repository-relative: {value}")
    relative = path.as_posix()
    if not (ROOT / relative).is_file():
        raise FileNotFoundError(f"{label} does not exist: {relative}")
    return relative


def _read_json(relative: str, *, label: str) -> dict[str, Any]:
    try:
        value = json.loads((ROOT / relative).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} is not valid JSON: {relative}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{label} must contain a JSON object: {relative}")
    return value


def _assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def _base_source_paths() -> list[str]:
    """Every imported source and frozen input used by either mode."""

    return [
        "experiments/m6_phase_batch.py",
        "experiments/m6_phase_predictions.py",
        "experiments/m5_phase_diagnostics.py",
        "proofs/M6_DIRECTED_CONSTANT.md",
        "proofs/M6_SECOND_ORDER.md",
        "proofs/M6_RESUMMED_PHASE.md",
        "src/provenance.py",
        "requirements-lock.txt",
        predictions.CRITICAL_PAYLOAD,
        predictions.PHASE_PAYLOAD,
        predictions.HELDOUT_PAYLOAD,
    ]


def _validation_source_paths(protocol_path: str, calibration_path: str) -> list[str]:
    return _base_source_paths() + [protocol_path, calibration_path]


def _validate_calibration_payload(payload: dict[str, Any]) -> None:
    _assert_equal(
        payload.get("classification"),
        "M6 PHASE PREDICTION CALIBRATION; theoretical N=1024 only; no finite N=1024 observation",
        "calibration classification",
    )
    _assert_equal(payload.get("parameters"), _expected_parameters(), "calibration parameters")
    _assert_equal(
        payload.get("input_payloads"),
        {
            "critical": predictions.CRITICAL_PAYLOAD,
            "phase_calibration": predictions.PHASE_PAYLOAD,
            "heldout_512": predictions.HELDOUT_PAYLOAD,
        },
        "calibration input payloads",
    )
    observed = payload.get("observed")
    if not isinstance(observed, dict):
        raise ValueError("calibration observed data must be an object")
    _assert_equal(
        sorted(int(index) for index in observed),
        list(predictions.OBSERVED_INDICES),
        "calibration observed indices",
    )
    if "1024" in observed or 1024 in observed:
        raise ValueError("calibration observed data contains forbidden N=1024")
    _assert_equal(payload.get("theoretical_only_indices"), [1024], "theoretical-only index")

    model_predictions = payload.get("predictions")
    if not isinstance(model_predictions, dict):
        raise ValueError("calibration predictions must be an object")
    for model in predictions.MODEL_NAMES:
        values = model_predictions.get(model)
        if not isinstance(values, dict):
            raise ValueError(f"missing calibration model predictions: {model}")
        _assert_equal(
            sorted(int(index) for index in values),
            list(predictions.PREDICTION_INDICES),
            f"calibration prediction indices for {model}",
        )

    tolerances = payload.get("tolerances")
    if not isinstance(tolerances, dict):
        raise ValueError("calibration tolerances must be an object")
    for key in ("common_512_benchmark", "truncated_2nd", "resummed"):
        value = tolerances.get(key)
        if not isinstance(value, str):
            raise ValueError(f"calibration tolerance {key} must be a decimal string")
        from experiments import m6_phase_predictions as _prediction_module

        with _prediction_module.mp.workdps(predictions.DEFAULT_DPS):
            if not _prediction_module.mp.mpf(value) > 0:
                raise ValueError(f"calibration tolerance {key} must be positive")
    benchmark = payload.get("benchmark")
    if not isinstance(benchmark, dict):
        raise ValueError("calibration benchmark must be an object")
    _assert_equal(benchmark.get("observed_index"), 512, "benchmark observed index")
    _assert_equal(
        benchmark.get("rule"),
        "2*abs(resummed[512]-observed[512])",
        "benchmark tolerance rule",
    )
    _assert_equal(
        set(benchmark.get("passed", {})),
        set(predictions.MODEL_NAMES),
        "benchmark model pass/fail keys",
    )


def _verify_protocol(
    protocol_path: str,
) -> tuple[dict[str, Any], dict[str, Any], str]:
    protocol = _read_json(protocol_path, label="M6 phase protocol")
    _assert_equal(protocol.get("schema_version"), 1, "protocol schema_version")
    calibration_path = _relative_path(
        protocol.get("calibration_payload", ""),
        label="protocol calibration_payload",
    )
    recorded_hash = protocol.get("calibration_payload_sha256")
    if not isinstance(recorded_hash, str) or len(recorded_hash) != 64:
        raise ValueError("protocol calibration_payload_sha256 must be a SHA-256 hex string")
    _assert_equal(sha(ROOT / calibration_path), recorded_hash, "calibration payload SHA-256")

    calibration = _read_json(calibration_path, label="M6 calibration payload")
    _validate_calibration_payload(calibration)
    _assert_equal(protocol.get("parameters"), calibration["parameters"], "protocol parameters")
    _assert_equal(protocol.get("constants"), calibration["constants"], "protocol constants")
    _assert_equal(protocol.get("predictions"), calibration["predictions"], "protocol predictions")
    _assert_equal(protocol.get("tolerances"), calibration["tolerances"], "protocol tolerances")
    _assert_equal(protocol.get("observed_holdout_index"), 512, "protocol observed index")
    _assert_equal(protocol.get("validation_index"), 1024, "protocol validation index")
    if "observed" in protocol:
        observed = protocol["observed"]
        if not isinstance(observed, dict) or "1024" in observed or 1024 in observed:
            raise ValueError("protocol observed data contains forbidden N=1024")
    return protocol, calibration, calibration_path


def _calibration_producer() -> dict[str, Any]:
    return predictions.produce_calibration()


def _validation_producer(
    protocol: dict[str, Any],
    calibration: dict[str, Any],
) -> dict[str, Any]:
    from experiments import m5_phase_diagnostics as diagnostics

    diagnostic_parameters = protocol["parameters"]["diagnostic"]
    final_dps = int(diagnostic_parameters["final_dps"])
    started = time.perf_counter()
    deadline = started + float(diagnostic_parameters["max_seconds"])
    with diagnostics.mp.workdps(final_dps):
        locator_tail_scale = diagnostics.mp.mpf(
            str(diagnostic_parameters["locator_tail_scale"])
        )
        locator_d_tail_tolerance = diagnostics.mp.mpf(
            str(diagnostic_parameters["locator_D_tail_tolerance"])
        )
        final_tail_scale = diagnostics.mp.mpf(
            str(diagnostic_parameters["final_tail_scale"])
        )
        final_d_tail_tolerance = diagnostics.mp.mpf(
            str(diagnostic_parameters["final_D_tail_tolerance"])
        )
        derivative_step = diagnostics.mp.mpf(
            str(diagnostic_parameters["derivative_step"])
        )
        # Deliberately call locate_root directly: validation must not call
        # m5_phase_diagnostics.run() or regenerate/refit calibration values.
        row = diagnostics.locate_root(
            1024,
            list(diagnostic_parameters["phases"]),
            locator_dps=int(diagnostic_parameters["locator_dps"]),
            locator_tail_scale=locator_tail_scale,
            locator_d_tail_tolerance=locator_d_tail_tolerance,
            final_dps=final_dps,
            final_tail_scale=final_tail_scale,
            final_d_tail_tolerance=final_d_tail_tolerance,
            refinement_steps=int(diagnostic_parameters["refinement_steps"]),
            derivative_step=derivative_step,
            deadline=deadline,
        )
        actual_theta = diagnostics.mp.mpf(str(row["theta_N"]))
        comparisons: dict[str, Any] = {}
        for model in predictions.MODEL_NAMES:
            predicted = diagnostics.mp.mpf(
                str(protocol["predictions"][model]["1024"])
            )
            tolerance = diagnostics.mp.mpf(
                str(protocol["tolerances"][model])
            )
            error = abs(actual_theta - predicted)
            comparisons[model] = {
                "actual": diagnostics._decimal(actual_theta),
                "predicted": diagnostics._decimal(predicted),
                "absolute_error": diagnostics._decimal(error),
                "tolerance": diagnostics._decimal(tolerance),
                "passed": bool(error <= tolerance),
            }
        elapsed = time.perf_counter() - started
        if elapsed > float(diagnostic_parameters["max_seconds"]):
            raise TimeoutError("M6 N=1024 validation exceeded max_seconds")
        return {
            "classification": "M6 N=1024 DIRECT VALIDATION DIAGNOSTIC ONLY",
            "status": "pass" if all(item["passed"] for item in comparisons.values()) else "fail",
            "passed": {model: item["passed"] for model, item in comparisons.items()},
            "validation_index": 1024,
            "observed_input_index": 512,
            "refit": False,
            "locator": "experiments.m5_phase_diagnostics.locate_root",
            "protocol": {
                "schema_version": protocol["schema_version"],
                "calibration_payload": protocol["calibration_payload"],
                "calibration_payload_sha256": protocol["calibration_payload_sha256"],
            },
            "calibration_constants": calibration["constants"],
            "row": row,
            "comparisons": comparisons,
            "warning": (
                "The two model comparisons are retained separately. A failed "
                "second-order comparison is diagnostic evidence only and is not "
                "a refutation of the asymptotic theorem."
            ),
        }


def run(
    kind: str,
    experiment_id: str,
    protocol_path: str = PROTOCOL_DEFAULT,
) -> Path:
    """Create one source-frozen M6 calibration or validation receipt."""

    if kind == "calibration":
        parameters = {
            "mode": "calibration",
            "parameters": _expected_parameters(),
        }
        command = (
            f".venv/bin/python -m experiments.m6_phase_batch "
            f"calibration {experiment_id}"
        )
        return run_record(
            experiment_id,
            command,
            parameters,
            _base_source_paths(),
            _calibration_producer,
        )
    if kind != "validation":
        raise ValueError(f"unknown M6 phase batch kind: {kind}")

    protocol_rel = _relative_path(protocol_path, label="M6 phase protocol")
    protocol, calibration, calibration_path = _verify_protocol(protocol_rel)
    parameters = {
        "mode": "validation",
        "protocol": protocol_rel,
        "calibration_payload": calibration_path,
        "validation_index": 1024,
        "diagnostic_parameters": protocol["parameters"]["diagnostic"],
        "predictions": protocol["predictions"],
        "tolerances": protocol["tolerances"],
    }
    command = (
        f".venv/bin/python -m experiments.m6_phase_batch validation "
        f"{experiment_id} --protocol {protocol_rel}"
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
