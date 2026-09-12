"""Bounded E3 anisotropic audit with exact He and memory certificates.

The producer keeps the symbolic ``m=1, n=2,3,4`` reproduction independent
from ``src.discovery_memory``.  Numeric-looking experiment inputs are encoded
as :class:`fractions.Fraction`; the only decimal values retained in a receipt
are display fields emitted by the existing memory certificate helper.  He
spectral certificates are converted to exact rational root brackets by integer
power comparisons, never by a floating-point root or eigenvalue.

The default sweep is deliberately bounded: memories 3, 5, 7, 9 and ratios
1/4, 1/2, 1, 2, 4, with withheld ratios 2/3, 3/2, 7/5 retained separately.
Each memory point runs in a child process with a 180-second outer timeout.
Resource or validation failures are recorded as errors and abort the producer;
there is no silent omission of a requested point.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from src.discovery_engine import memory_case
from src.discovery_memory import exact_certificate, verify_bound
from src.provenance import run_record
from src.weighted_he import (
    DEFAULT_X,
    DEFAULT_Y,
    build_he_matrix,
    compare_table1,
    matrix_invariants,
    table1_bound,
)


ROOT = Path(__file__).resolve().parents[1]
OUTER_TIMEOUT_SECONDS = 180
INNER_TIMEOUT_SECONDS = 175
CERTIFICATE_ITERATIONS = 120
MAIN_MEMORIES = (3, 5, 7, 9)
MAIN_RATIOS = tuple(Fraction(value) for value in ("1/4", "1/2", "1", "2", "4"))
WITHHELD_RATIOS = tuple(Fraction(value) for value in ("2/3", "3/2", "7/5"))
ALL_RATIOS = MAIN_RATIOS + WITHHELD_RATIOS
GEOMETRIC_TRIPLES = ((Fraction(1, 4), Fraction(1, 2), Fraction(1)),
                     (Fraction(1, 2), Fraction(1), Fraction(2)),
                     (Fraction(1), Fraction(2), Fraction(4)))


def _fraction(value: Fraction | int | str) -> Fraction:
    """Parse only exact rational input for experiment parameters."""

    if isinstance(value, (bool, float)):
        raise TypeError("boolean/float is not an exact rational experiment weight")
    result = value if isinstance(value, Fraction) else Fraction(value)
    if result < 0:
        raise ValueError("experiment weights must be nonnegative")
    return result


def _weight_vector(x: Fraction, y: Fraction) -> list[Fraction]:
    return [x, y, x, y]


def _config(
    memory: int,
    x: Fraction,
    y: Fraction,
    *,
    symmetry: str = "auto",
    representation: str = "equitable",
) -> dict[str, Any]:
    return {
        "kind": "memory",
        "memory": memory,
        "weights": _weight_vector(x, y),
        "symmetry": symmetry,
        "state_representation": representation,
        "iterations": CERTIFICATE_ITERATIONS,
        "max_states": 100_000,
        "max_seconds": INNER_TIMEOUT_SECONDS,
    }


def _json_config(config: dict[str, Any]) -> dict[str, Any]:
    result = dict(config)
    result["weights"] = [str(_fraction(weight)) for weight in config["weights"]]
    return result


def _child_memory_case(config: dict[str, Any]) -> dict[str, Any]:
    """Run one case when this file is invoked as a subprocess worker."""

    parsed = json.loads(config if isinstance(config, str) else json.dumps(config))
    parsed["weights"] = [_fraction(weight) for weight in parsed["weights"]]
    try:
        return memory_case(parsed)
    except Exception as error:  # parent turns this into an explicit failure
        return {
            "config": parsed,
            "status": "ERROR",
            "error_type": type(error).__name__,
            "reason": str(error),
        }


def _invoke_case(config: dict[str, Any]) -> dict[str, Any]:
    """Run one bounded child process and return its explicit status payload."""

    payload = json.dumps(_json_config(config), sort_keys=True)
    command = [sys.executable, str(Path(__file__).resolve()), "--memory-case", payload]
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=OUTER_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(
            f"memory case exceeded outer timeout {OUTER_TIMEOUT_SECONDS}s: {config}"
        ) from error
    if completed.returncode != 0:
        raise RuntimeError(
            f"memory worker exited {completed.returncode}: {completed.stderr.strip()}"
        )
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"memory worker returned non-JSON output: {completed.stdout!r}"
        ) from error
    result["outer_seconds"] = time.monotonic() - started
    return result


def _run_required_case(
    config: dict[str, Any], cache: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    """Run/cache a case and reject every non-certified status explicitly."""

    key = json.dumps(_json_config(config), sort_keys=True)
    if key not in cache:
        cache[key] = _invoke_case(config)
    result = cache[key]
    if result.get("status") != "CERTIFIED":
        raise RuntimeError(
            f"required memory point did not certify: {config}; "
            f"status={result.get('status')}, reason={result.get('reason')}"
        )
    return result


def _matrix_rows(matrix: sp.Matrix) -> list[dict[int, Fraction]]:
    """Convert a specialized exact SymPy matrix to sparse Fraction rows."""

    rows: list[dict[int, Fraction]] = []
    for i in range(matrix.rows):
        row: dict[int, Fraction] = {}
        for j in range(matrix.cols):
            value = sp.cancel(matrix[i, j])
            if value == 0:
                continue
            if not value.is_Rational:
                raise ValueError(f"specialized He matrix is not rational: {value}")
            row[j] = Fraction(int(value.p), int(value.q))
        rows.append(row)
    return rows


def rational_root_bracket(
    value: Fraction, degree: int, *, bits: int = 80
) -> tuple[Fraction, Fraction]:
    """Return exact ``lo <= value**(1/degree) <= hi`` by rational bisection."""

    value = _fraction(value)
    if type(degree) is not int or degree < 1:
        raise ValueError("degree must be a positive integer")
    if type(bits) is not int or bits < 1:
        raise ValueError("bits must be a positive integer")
    if value == 0:
        return Fraction(0), Fraction(0)
    low = Fraction(0)
    high = Fraction(1)
    while high**degree < value:
        high *= 2
    for _ in range(bits):
        middle = (low + high) / 2
        if middle**degree < value:
            low = middle
        else:
            high = middle
    if not (low**degree <= value <= high**degree):
        raise AssertionError("rational root bracket failed its power check")
    return low, high


def _he_case(
    n: int,
    ratio: Fraction,
    *,
    mode: str,
    iterations: int = CERTIFICATE_ITERATIONS,
) -> dict[str, Any]:
    """Build, certify, and serialize one exact positive-weight He matrix."""

    x = sp.Rational(ratio.numerator, ratio.denominator)
    y = sp.Integer(1)
    matrix = build_he_matrix(1, n, mode=mode, x=x, y=y)
    invariants = matrix_invariants(matrix)
    rows = _matrix_rows(matrix)
    certificate = exact_certificate(rows, iterations=iterations)
    if not verify_bound(rows, certificate):
        raise AssertionError(f"independent exact certificate rejected He {mode} n={n}")
    lambda_upper = Fraction(certificate["upper"])
    degree = n - 1
    root_low, root_high = rational_root_bracket(lambda_upper, degree)
    if any(value <= 0 for row in rows for value in row.values()):
        raise AssertionError(f"positive He matrix lost a positive entry: {mode} n={n}")
    return {
        "mode": mode,
        "n": n,
        "ratio": str(ratio),
        "matrix": [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)],
        "trace": str(invariants["trace"]),
        "discriminant": str(invariants["discriminant"]),
        "spectral_certificate": certificate,
        "root_degree": degree,
        "root_low": str(root_low),
        "root_high": str(root_high),
        "root_power_check": {
            "low_le_lambda": root_low**degree <= lambda_upper,
            "lambda_le_high": lambda_upper <= root_high**degree,
        },
        "primitive_check": True,
    }


def _memory_upper(result: dict[str, Any]) -> Fraction:
    try:
        return Fraction(result["certificate"]["upper"])
    except (KeyError, TypeError, ValueError) as error:
        raise RuntimeError(f"missing exact memory certificate: {result}") from error


def _memory_point_record(
    result: dict[str, Any], memory: int, ratio: Fraction, *, withheld: bool
) -> dict[str, Any]:
    return {
        "memory": memory,
        "ratio": str(ratio),
        "withheld_ratio": withheld,
        "upper_exact": str(_memory_upper(result)),
        "state_count": result["state_count"],
        "original_state_count": result["original_state_count"],
        "transition_count": result["transition_count"],
        "original_transition_count": result["original_transition_count"],
        "case": result,
    }


def _compare_bound_powers(
    memory_upper: Fraction, he_case: dict[str, Any]
) -> str:
    """Compare rational memory U with exact He root of rational lambda U."""

    degree = int(he_case["root_degree"])
    he_lambda = Fraction(he_case["spectral_certificate"]["upper"])
    memory_power = memory_upper**degree
    if memory_power < he_lambda:
        return "memory_lower_upper_bound"
    if memory_power > he_lambda:
        return "he_lower_upper_bound"
    return "equal_upper_bound"


def _finite_logconvexity(
    values: dict[str, Any],
    triples: tuple[tuple[Fraction, Fraction, Fraction], ...] = GEOMETRIC_TRIPLES,
) -> list[dict[str, Any]]:
    """Check finite geometric triples exactly and label the result tested-only."""

    checks: list[dict[str, Any]] = []
    for family, family_values in values.items():
        for left, middle, right in triples:
            try:
                l_value = family_values[str(left)]
                m_value = family_values[str(middle)]
                r_value = family_values[str(right)]
            except KeyError as error:
                raise RuntimeError(
                    f"missing required geometric-grid point for {family}: "
                    f"{error.args[0]}"
                ) from error
            # For He families these are exact spectral certificates L with
            # U=L**(1/(n-1)); the common degree cancels after squaring.  For
            # memory families they are already rational U values.
            holds = m_value**2 <= l_value * r_value
            checks.append({
                "family": family,
                "triple": [str(left), str(middle), str(right)],
                "holds": bool(holds),
                "tested_only": True,
                "interpretation": "finite certificate grid check; no log-convexity theorem claimed",
            })
    return checks


def produce() -> dict[str, Any]:
    """Produce the bounded E3 receipt payload."""

    table_checks: list[dict[str, Any]] = []
    for mode in ("saw", "sat"):
        for n in (2, 3, 4):
            compared = compare_table1(n, mode=mode, x=DEFAULT_X, y=DEFAULT_Y)
            if not compared["ok"]:
                raise AssertionError(f"independent Table 1 mismatch: {mode}, n={n}")
            table_checks.append({
                "mode": mode,
                "n": n,
                "trace": str(compared["actual"]["trace"]),
                "discriminant": str(compared["actual"]["discriminant"]),
                "trace_difference": str(compared["trace_difference"]),
                "discriminant_difference": str(compared["discriminant_difference"]),
                "exact_match": True,
            })

    cache: dict[str, dict[str, Any]] = {}
    memory_records: list[dict[str, Any]] = []
    memory_by_key: dict[tuple[int, Fraction, Fraction], dict[str, Any]] = {}
    for memory in MAIN_MEMORIES:
        for ratio in ALL_RATIOS:
            result = _run_required_case(
                _config(memory, ratio, Fraction(1)), cache
            )
            memory_by_key[(memory, ratio, Fraction(1))] = result
            memory_records.append(
                _memory_point_record(
                    result,
                    memory,
                    ratio,
                    withheld=ratio in WITHHELD_RATIOS,
                )
            )

    he_records: list[dict[str, Any]] = []
    he_by_key: dict[tuple[str, int, Fraction], dict[str, Any]] = {}
    for ratio in ALL_RATIOS:
        for mode in ("saw", "sat"):
            for n in (2, 3, 4):
                record = _he_case(n, ratio, mode=mode)
                he_by_key[(mode, n, ratio)] = record
                he_records.append(record)

    # Required cross-checks use m=3 and m=5 only, keeping the extra scaling
    # and exchange points bounded while retaining exact rational equalities.
    symmetry_checks: list[dict[str, Any]] = []
    for memory in (3, 5):
        base = _run_required_case(_config(memory, Fraction(1, 2), Fraction(1)), cache)
        scaled = _run_required_case(_config(memory, Fraction(3, 4), Fraction(3, 2)), cache)
        exchanged = _run_required_case(_config(memory, Fraction(1), Fraction(1, 2)), cache)
        base_upper = _memory_upper(base)
        scaled_upper = _memory_upper(scaled)
        exchanged_upper = _memory_upper(exchanged)
        scaling_ok = scaled_upper == Fraction(3, 2) * base_upper
        exchange_ok = exchanged_upper == base_upper
        if not scaling_ok or not exchange_ok:
            raise AssertionError(
                f"exact homogeneity/exchange check failed at memory {memory}: "
                f"scale={scaling_ok}, exchange={exchange_ok}"
            )
        symmetry_checks.append({
            "memory": memory,
            "base_weights": ["1/2", "1"],
            "scaled_weights": ["3/4", "3/2"],
            "exchanged_weights": ["1", "1/2"],
            "base_upper": str(base_upper),
            "scaled_upper": str(scaled_upper),
            "exchanged_upper": str(exchanged_upper),
            "scaling_factor": "3/2",
            "homogeneous_3_over_2": True,
            "exchange_x_y": True,
            "base_case": base,
            "scaled_case": scaled,
            "exchanged_case": exchanged,
        })

    axis_result = _run_required_case(_config(3, Fraction(0), Fraction(1)), cache)
    axis_upper = _memory_upper(axis_result)
    if axis_upper < 1:
        raise AssertionError(f"axis upper bound is below direct mu(0,1)=1: {axis_upper}")
    small_result = _run_required_case(
        _config(3, Fraction(1, 1000), Fraction(1)), cache
    )
    boundary_checks = {
        "axis_x0_y1": {
            "upper_exact": str(axis_upper),
            "direct_mu_exact": "1",
            "direct_axis_check": True,
            "he_theorem_applied": False,
            "case": axis_result,
        },
        "small_x1_over_1000_y1": {
            "upper_exact": str(_memory_upper(small_result)),
            "positive_weight_case": True,
            "case": small_result,
        },
    }

    mutant_config = _config(3, Fraction(1, 2), Fraction(1), symmetry="d4")
    mutant = _invoke_case(mutant_config)
    mutant_rejected = mutant.get("status") == "ERROR" and mutant.get("error_type") == "ValueError"
    if not mutant_rejected:
        raise AssertionError(f"anisotropic D4 mutant was not rejected: {mutant}")
    mutant_record = {
        "weights": ["1/2", "1", "1/2", "1"],
        "requested_symmetry": "d4",
        "rejected": True,
        "error_type": mutant.get("error_type"),
        "reason": mutant.get("reason"),
        "scientific_status": "control rejection; D4 does not preserve anisotropic weights",
    }

    memory_value_families: dict[str, dict[str, Fraction]] = {}
    for memory in MAIN_MEMORIES:
        memory_value_families[f"memory:{memory}"] = {
            str(ratio): _memory_upper(memory_by_key[(memory, ratio, Fraction(1))])
            for ratio in MAIN_RATIOS
        }
    for mode in ("saw", "sat"):
        for n in (2, 3, 4):
            memory_value_families[f"he:{mode}:{n}"] = {
                str(ratio): Fraction(he_by_key[(mode, n, ratio)]["spectral_certificate"]["upper"])
                for ratio in MAIN_RATIOS
            }
    logconvexity = _finite_logconvexity(memory_value_families)

    comparisons: list[dict[str, Any]] = []
    for memory in MAIN_MEMORIES:
        for ratio in ALL_RATIOS:
            memory_upper = _memory_upper(memory_by_key[(memory, ratio, Fraction(1))])
            candidates = [
                he_by_key[(mode, n, ratio)]
                for mode in ("saw", "sat")
                for n in (2, 3, 4)
            ]
            best = min(candidates, key=lambda item: Fraction(item["root_high"]))
            comparisons.append({
                "memory": memory,
                "ratio": str(ratio),
                "memory_upper": str(memory_upper),
                "best_he": {
                    "mode": best["mode"],
                    "n": best["n"],
                    "root_low": best["root_low"],
                    "root_high": best["root_high"],
                },
                "relation_by_exact_powers": _compare_bound_powers(memory_upper, best),
                "withheld_ratio": ratio in WITHHELD_RATIOS,
            })
    selected: list[dict[str, Any]] = []
    # Select one comparison per ratio.  Values at different anisotropy ratios
    # have different physical scales, so a single global minimum would be a
    # misleading cross-ratio "winner".  The normalized ratio below is only a
    # finite audit statistic, not an optimization claim.
    for ratio in ALL_RATIOS:
        candidates = [item for item in comparisons if item["ratio"] == str(ratio)]
        best_memory = min(candidates, key=lambda item: Fraction(item["memory_upper"]))
        best_he = min(
            [he_by_key[(mode, n, ratio)] for mode in ("saw", "sat") for n in (2, 3, 4)],
            key=lambda item: Fraction(item["root_high"]),
        )
        memory_upper = Fraction(best_memory["memory_upper"])
        he_upper = Fraction(best_he["root_high"])
        selected.append({
            "ratio": str(ratio),
            "best_memory": {
                "memory": best_memory["memory"],
                "upper": best_memory["memory_upper"],
            },
            "best_he": {
                "mode": best_he["mode"],
                "n": best_he["n"],
                "root_low": best_he["root_low"],
                "root_high": best_he["root_high"],
            },
            "relation_by_exact_powers": _compare_bound_powers(memory_upper, best_he),
            "memory_over_he_root_high": str(memory_upper / he_upper),
            "withheld_ratio": ratio in WITHHELD_RATIOS,
            "tested_only": True,
            "interpretation": "per-ratio finite comparison; no cross-ratio optimum or novelty claim",
        })

    return {
        "classification": "CERTIFIED SPECTRAL BOUND plus finite exact audit",
        "scientific_status": "KNOWN_METHOD; no novelty claim",
        "parameters": {
            "memories": list(MAIN_MEMORIES),
            "main_ratios": [str(ratio) for ratio in MAIN_RATIOS],
            "withheld_ratios": [str(ratio) for ratio in WITHHELD_RATIOS],
            "outer_timeout_seconds": OUTER_TIMEOUT_SECONDS,
            "inner_timeout_seconds": INNER_TIMEOUT_SECONDS,
            "certificate_iterations": CERTIFICATE_ITERATIONS,
        },
        "table1_reproduction": table_checks,
        "memory_cases": memory_records,
        "he_cases": he_records,
        "comparison_cases": comparisons,
        "automatically_selected_cross_family_observations": selected,
        "homogeneity_exchange_checks": symmetry_checks,
        "boundary_checks": boundary_checks,
        "anisotropic_d4_mutant": mutant_record,
        "finite_logconvexity_checks": logconvexity,
    }


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--memory-case":
        print(json.dumps(_child_memory_case(sys.argv[2]), sort_keys=True, default=str))
        raise SystemExit
    experiment_id = sys.argv[1] if len(sys.argv) > 1 else "e3-weights-v1"
    print(
        run_record(
            experiment_id,
            f"PYTHONPATH=. .venv/bin/python experiments/e3_weights.py {experiment_id}",
            {
                "memories": list(MAIN_MEMORIES),
                "main_ratios": [str(ratio) for ratio in MAIN_RATIOS],
                "withheld_ratios": [str(ratio) for ratio in WITHHELD_RATIOS],
                "outer_timeout_seconds": OUTER_TIMEOUT_SECONDS,
            },
            [
                "src/weighted_he.py",
                "experiments/e3_weights.py",
                "src/discovery_memory.py",
                "src/discovery_engine.py",
                "src/equitable.py",
                "src/provenance.py",
                "proofs/DISCOVERY_MEMORY.md",
                "proofs/EQUITABLE_COMPRESSION.md",
                "proofs/WEIGHTED_HE_REPRODUCTION.md",
                "NORMALIZATION.md",
                "environment/NEXT_GOAL_BRIEF.md",
                "requirements-lock.txt",
            ],
            produce,
        )
    )
