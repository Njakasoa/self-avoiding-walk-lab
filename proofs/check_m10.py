"""Fail-closed integration checks for the finite M10 receipts.

This verifier reads the canonical N=32 full-band and structural receipts,
replays only the inexpensive structural wrapper, and independently checks the
serialized full-band geometry.  It deliberately does not call the expensive
128-cell producer.  The result is a finite N=32 statement; full W coverage
for unlisted indices remains open.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from fractions import Fraction as F
from pathlib import Path
from typing import Any

from proofs.check_m3 import receipt


ROOT = Path(__file__).resolve().parents[1]
BITS = 384
SCALE = 1 << BITS
N = 32
CELL_COUNT = 128
PHASE_BAND = ["164/5", "329/10"]
TAIL_TARGET = F(1, 10**18)
M7_PAYLOAD_SHA256 = (
    "75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f"
)

DIAGNOSTIC_PATH = ROOT / "results" / "m9-coverage-diagnostics" / (
    "w-fullband-N32-full-128.json"
)
REVIEW_FIRST_CELL_PATH = ROOT / "results" / (
    "m10-full-band-review-first-cell-final.json"
)
FINAL_REVIEW_PATH = ROOT / "proofs" / "M10_FULL_BAND_FINAL_REVIEW.md"

REVIEW_SOURCE_SETS = {
    "proofs/M10_BETA_REVIEW.md": (
        "proofs/M10_BETA_REAL.md",
        "proofs/m10_beta_real.py",
    ),
    "proofs/M10_DIRECTED_REVIEW.md": (
        "proofs/M10_DIRECTED_MONOTONICITY.md",
        "proofs/m10_directed_monotone.py",
        "proofs/m10_structural_bounds.py",
    ),
    "proofs/M10_COMBINED_WEIGHT_REVIEW.md": (
        "proofs/M10_POSITIVE_COMBINED_WEIGHT.md",
        "proofs/M5_DIRECTED_LOG.md",
        "proofs/M5_DIRECTED_REFINED.md",
        "proofs/M6_DIRECTED_CONSTANT.md",
        "results/m6-coefficient-v1/payload.json",
    ),
    "proofs/M10_REAL_PRODUCT_REVIEW.md": (
        "proofs/M10_REAL_PHASE_PRODUCT.md",
        "proofs/M10_BARE_PHASE_DERIVATIVE.md",
    ),
}

EXPECTED_STRUCTURAL_COMPONENT_HASHES = {
    "real_beta_derivatives": (
        "7a04339811087b634dbab95557810a3e6c933571d5af60163b8a60d0e7a32734"
    ),
    "weight_and_product": (
        "49db78a15baa982f91cf2ada380c302fd404a743ba445788932ef89bf62c1093"
    ),
    "directed_monotonicity": (
        "f0210db9efbf79dbf5bc4ce6d871520c1b93238fad0ec7cda69993e225294c88"
    ),
}
EXPECTED_STRUCTURAL_WRAPPER_HASH = (
    "f8396447ace42f2674b35f2844fb0bd789bc557152ac8dda8fae3fc4da3bb7b8"
)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_path(path: Path) -> str:
    _require(path.is_file(), f"missing file for hash check: {path}")
    return _sha256_bytes(path.read_bytes())


def _canonical_json_hash(value: Any) -> str:
    encoded = json.dumps(value, indent=2, sort_keys=True) + "\n"
    return _sha256_bytes(encoded.encode())


def _load_json(path: Path) -> Any:
    _require(path.is_file(), f"missing JSON artifact: {path}")
    return json.loads(path.read_text())


def _fraction(value: Any, label: str) -> F:
    try:
        return F(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ArithmeticError(f"{label}: invalid rational {value!r}") from exc


def _interval(record: Any, label: str) -> tuple[F, F]:
    _require(isinstance(record, dict), f"{label}: interval record missing")
    required = {
        "lower_numerator",
        "upper_numerator",
        "denominator_power_of_two",
    }
    _require(required <= set(record), f"{label}: incomplete interval record")
    try:
        power = int(record["denominator_power_of_two"])
        lower = int(record["lower_numerator"])
        upper = int(record["upper_numerator"])
    except (TypeError, ValueError) as exc:
        raise ArithmeticError(f"{label}: non-integer interval field") from exc
    _require(power == BITS, f"{label}: expected {BITS}-bit interval")
    _require(lower <= upper, f"{label}: empty interval")
    return F(lower, SCALE), F(upper, SCALE)


def _jet(record: Any, label: str) -> tuple[tuple[F, F], tuple[F, F]]:
    _require(isinstance(record, dict), f"{label}: jet record missing")
    _require(
        {"value", "derivative"} <= set(record),
        f"{label}: incomplete Jet384 record",
    )
    return (
        _interval(record["value"], f"{label}.value"),
        _interval(record["derivative"], f"{label}.derivative"),
    )


def _ceil_scaled(value: F) -> int:
    return -((-value.numerator * SCALE) // value.denominator)


def _floor_scaled(value: F) -> int:
    return (value.numerator * SCALE) // value.denominator


def _check_i384_covering(record: Any, lower: F, upper: F, label: str) -> None:
    _require(
        isinstance(record, dict),
        f"{label}: missing I384 record",
    )
    expected = {
        "lower_numerator": str(_floor_scaled(lower)),
        "upper_numerator": str(_ceil_scaled(upper)),
        "denominator_power_of_two": BITS,
    }
    _require(record == expected, f"{label}: I384 rounding record mismatch")


def _check_phase_box(
    record: Any,
    phase_data_record: Any,
    label: str,
) -> None:
    _require(isinstance(record, dict), f"{label}: phase box missing")
    lower, upper = _interval(record.get("interval"), f"{label}.interval")
    listed_lower = _fraction(record.get("fraction_lower"), f"{label}.lower")
    listed_upper = _fraction(record.get("fraction_upper"), f"{label}.upper")
    _require(
        (lower, upper) == (listed_lower, listed_upper),
        f"{label}: listed fractions disagree with interval",
    )
    _require(
        record.get("strict_band") == ["32", "33"],
        f"{label}: wrong source-pole band",
    )
    _require(lower > 32 and upper < 33, f"{label}: not strictly in (32,33)")
    _require(
        phase_data_record == record["interval"],
        f"{label}: phase_data and band-check intervals differ",
    )


def _check_review_table(review_path: str, required_paths: tuple[str, ...]) -> dict:
    text = (ROOT / review_path).read_text()
    entries = {
        rel.strip(): digest
        for rel, digest in re.findall(
            r"^\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|",
            text,
            flags=re.MULTILINE,
        )
    }
    result = {}
    for rel in required_paths:
        _require(rel in entries, f"{review_path}: missing hash for {rel}")
        actual = _sha256_path(ROOT / rel)
        _require(
            entries[rel] == actual,
            f"{review_path}: stale or incorrect hash for {rel}",
        )
        result[rel] = actual
    return result


def _check_math_review_hashes() -> dict:
    checked = {}
    for review_path, source_paths in REVIEW_SOURCE_SETS.items():
        checked[review_path] = _check_review_table(review_path, source_paths)

    full_review = (ROOT / "proofs" / "M10_FULL_BAND_REVIEW.md").read_text()
    full_table = {
        rel.strip(): digest
        for rel, digest in re.findall(
            r"^\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|",
            full_review,
            flags=re.MULTILINE,
        )
    }
    for rel in (
        "proofs/m10_full_band.py",
        "experiments/m10_full_band_batch.py",
    ):
        _require(rel in full_table, f"M10 full review: missing hash for {rel}")
        _require(
            full_table[rel] == _sha256_path(ROOT / rel),
            f"M10 full review: stale or incorrect hash for {rel}",
        )
    _require("full W theory goal remains OPEN" in full_review,
             "M10 full review lost its open-scope statement")
    checked["proofs/M10_FULL_BAND_REVIEW.md"] = {
        rel: full_table[rel]
        for rel in (
            "proofs/m10_full_band.py",
            "experiments/m10_full_band_batch.py",
        )
    }

    final_review = FINAL_REVIEW_PATH.read_text()
    final_table = {
        rel.strip(): digest
        for rel, digest in re.findall(
            r"^\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|",
            final_review,
            flags=re.MULTILINE,
        )
    }
    final_sources = (
        "proofs/M10_FULL_BAND.md",
        "proofs/m10_full_band.py",
        "experiments/m10_full_band_batch.py",
    )
    for rel in final_sources:
        _require(rel in final_table,
                 f"M10 final review: missing hash for {rel}")
        _require(
            final_table[rel] == _sha256_path(ROOT / rel),
            f"M10 final review: stale or incorrect hash for {rel}",
        )
    _require(
        "full W theory goal remains OPEN" in final_review,
        "M10 final review lost its open-scope statement",
    )
    _require(
        "limited to N=32" in final_review and
        "unlisted finite indices" in final_review,
        "M10 final review lost its N=32-only limitation",
    )
    checked["proofs/M10_FULL_BAND_FINAL_REVIEW.md"] = {
        rel: final_table[rel] for rel in final_sources
    }
    return checked


def _check_review_first_cell(full_payload: dict) -> dict:
    review = _load_json(REVIEW_FIRST_CELL_PATH)
    _require(isinstance(review, dict), "first-cell review artifact is not a mapping")
    source_commit = review.get("source_commit")
    _require(isinstance(source_commit, str) and source_commit,
             "first-cell review has no source commit")
    try:
        subprocess.run(
            ["git", "cat-file", "-e", f"{source_commit}^{{commit}}"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as exc:
        raise ArithmeticError("first-cell review source commit is unavailable") from exc

    inputs = review.get("input_sha256")
    _require(isinstance(inputs, dict) and inputs,
             "first-cell review input hashes are missing")
    input_hashes = {}
    for rel, wanted in inputs.items():
        actual = _sha256_path(ROOT / rel)
        _require(
            actual == wanted,
            f"first-cell review input hash mismatch: {rel}",
        )
        input_hashes[rel] = actual

    result = review.get("result")
    _require(isinstance(result, dict), "first-cell review result is missing")
    _require(
        _canonical_json_hash(result) == review.get("output_sha256"),
        "first-cell review output hash mismatch",
    )
    _require(result.get("full_coverage") is False,
             "first-cell review unexpectedly claims full coverage")
    _require(result.get("partial_mode") is True,
             "first-cell review is not marked partial")
    _require(result.get("cells_requested") == [0],
             "first-cell review does not contain exactly cell 0")
    _require(len(result.get("cells", [])) == 1,
             "first-cell review cell count is not one")
    _require(
        result["cells"][0] == full_payload["cells"][0],
        "canonical full receipt cell 0 differs from independent review",
    )

    return {
        "source_commit": source_commit,
        "output_sha256": review["output_sha256"],
        "input_sha256": input_hashes,
        "cell0_matches_canonical": True,
    }


def _check_m7_transfer(full_payload: dict) -> dict:
    m7 = receipt("m7-finite-v1")
    _require(m7.get("status") == "pass", "M7 receipt is not passing")
    rows = [row for row in m7.get("rows", []) if row.get("index") == N]
    _require(len(rows) == 1, "M7 receipt does not contain one N=32 row")
    row = rows[0]
    source = row.get("phase_source_check", {})
    _require(source.get("source_pole_free") is True,
             "M7 N=32 source-pole exclusion is missing")
    _require(source.get("phase_band") == PHASE_BAND,
             "M7 N=32 phase band changed")

    left_f = _interval(row["left"]["F_certificate"], "M7 left F")
    right_f = _interval(row["right"]["F_certificate"], "M7 right F")
    numerator = _interval(
        row["uniform_numerator"]["P_plus_one_certificate"],
        "M7 1+P",
    )
    _require(left_f[0] > 0, "M7 left endpoint F is not positive")
    _require(right_f[1] < 0, "M7 right endpoint F is not negative")
    _require(numerator[1] < 0, "M7 whole-bracket 1+P is not negative")

    m7_path = ROOT / "results" / "m7-finite-v1" / "payload.json"
    m7_hash = _sha256_path(m7_path)
    _require(m7_hash == M7_PAYLOAD_SHA256, "M7 payload hash changed")
    frozen = full_payload.get("frozen_m7_n32", {})
    _require(frozen.get("payload_sha256") == m7_hash,
             "M10 frozen M7 hash does not match M7 receipt")
    _require(frozen.get("index") == N, "M10 frozen M7 index changed")
    _require(frozen.get("t_bracket") == row["t_bracket"],
             "M10 frozen M7 bracket differs from M7 receipt")
    _require(frozen.get("phase_band") == source["phase_band"],
             "M10 frozen M7 phase band differs from M7 receipt")
    _require(frozen.get("source_pole_free") is True,
             "M10 frozen M7 source-pole flag is false")
    _require(frozen.get("left_F_certificate") == row["left"]["F_certificate"],
             "M10 frozen left F certificate differs from M7")
    _require(frozen.get("right_F_certificate") == row["right"]["F_certificate"],
             "M10 frozen right F certificate differs from M7")
    _require(
        frozen.get("uniform_P_plus_one_certificate")
        == row["uniform_numerator"]["P_plus_one_certificate"],
        "M10 frozen 1+P certificate differs from M7",
    )

    outer_left, outer_right = map(F, full_payload["outer_t_bracket"])
    narrow_left, narrow_right = map(F, row["t_bracket"])
    _require(outer_left < narrow_left < narrow_right < outer_right,
             "M7 narrow bracket is not strictly contained in M10 outer band")
    containment = full_payload.get("containment", {})
    _require(containment.get("outer_contains_frozen_narrow_bracket") is True,
             "M10 containment flag is false")
    _require(containment.get("frozen_t_bracket") == row["t_bracket"],
             "M10 containment bracket differs from M7")
    return {
        "m7_payload_sha256": m7_hash,
        "endpoint_signs": True,
        "phase_band": PHASE_BAND,
        "source_pole_free": True,
        "noncancellation": True,
        "strict_containment": True,
    }


def _check_cell(cell: dict, index: int, left: F, right: F, diagnostic: dict) -> None:
    label = f"cell {index}"
    _require(cell.get("cell") == index, f"{label}: wrong cell index")
    _require(cell.get("t_bracket") == [str(left), str(right)],
             f"{label}: rational bracket mismatch")
    _check_i384_covering(
        cell.get("t_interval"), left, right, f"{label}.t_interval"
    )
    _require(
        cell.get("derivative") == diagnostic["F_derivative"],
        f"{label}: derivative differs from retained diagnostic",
    )
    _require(diagnostic.get("negative") is True,
             f"{label}: retained diagnostic is not negative")
    dlo, dhi = _interval(cell["derivative"], f"{label}.derivative")
    _require(dhi < 0, f"{label}: F_t upper endpoint is not negative")

    phase_data = cell.get("phase_data")
    _require(isinstance(phase_data, dict), f"{label}: phase_data missing")
    for name in ("a", "b", "epsilon", "q", "s_g", "s_h", "v_g", "v_h"):
        _interval(phase_data.get(name), f"{label}.phase_data.{name}")
    checks = cell.get("phase_band_checks")
    _require(isinstance(checks, dict), f"{label}: phase checks missing")
    for name in ("a", "b"):
        _check_phase_box(checks.get(name), phase_data[name],
                         f"{label}.phase_{name}")

    engine = cell.get("engine")
    _require(isinstance(engine, dict), f"{label}: complete engine missing")
    for name in ("t", "q", "epsilon", "P", "H", "D_I", "F"):
        _jet(engine.get(name), f"{label}.engine.{name}")
    _require(engine["t"]["value"] == cell["t_interval"],
             f"{label}: engine t interval differs from cell interval")
    _require(engine["F"]["derivative"] == cell["derivative"],
             f"{label}: engine F derivative differs from cell derivative")

    q_value, _ = _jet(engine["q"], f"{label}.engine.q")
    epsilon_value, _ = _jet(engine["epsilon"], f"{label}.engine.epsilon")
    di_value, _ = _jet(engine["D_I"], f"{label}.engine.D_I")
    _require(q_value[0] > 0 and q_value[1] < 1,
             f"{label}: q value is not in (0,1)")
    _require(epsilon_value[0] > 0 and epsilon_value[1] < F(1, 100),
             f"{label}: phase inverse epsilon is outside e<.01")
    _require(di_value[0] > 0 and di_value[1] < 1,
             f"{label}: D_I value is not in (0,1)")
    _require(phase_data["q"] == engine["q"]["value"],
             f"{label}: phase and engine q records differ")
    _require(phase_data["epsilon"] == engine["epsilon"]["value"],
             f"{label}: phase and engine epsilon records differ")

    tail = engine.get("tail")
    _require(isinstance(tail, dict), f"{label}: tail record missing")
    tail_i384 = {
        "rho_prime_bound",
        "u_prime_bound",
        "g_prime_bound",
        "V1_box",
        "V2_box",
        "V1_derivative_box",
        "V2_derivative_box",
        "tail_P",
        "tail_H",
        "tail_P_derivative",
        "tail_H_derivative",
    }
    for name in tail_i384:
        _interval(tail.get(name), f"{label}.engine.tail.{name}")
    _jet(tail.get("R"), f"{label}.engine.tail.R")
    _require(isinstance(tail.get("start_index"), int),
             f"{label}: tail start index missing")
    _require(isinstance(tail.get("extra_terms"), int),
             f"{label}: tail extra term count missing")
    _require(tail.get("final_index") ==
             tail["start_index"] + tail["extra_terms"],
             f"{label}: tail index ledger mismatch")
    for name in ("tail_P", "tail_H", "tail_P_derivative", "tail_H_derivative"):
        lo, hi = _interval(tail[name], f"{label}.engine.tail.{name}")
        _require(lo >= 0 and hi <= TAIL_TARGET,
                 f"{label}: prudent {name} exceeds 1e-18")

    directed = engine.get("directed_meta")
    _require(isinstance(directed, dict), f"{label}: directed tail record missing")
    for name in ("tail_value", "tail_derivative", "mden", "q_upper"):
        _interval(directed.get(name), f"{label}.engine.directed.{name}")
    for name in ("tail_value", "tail_derivative"):
        lo, hi = _interval(directed[name], f"{label}.engine.directed.{name}")
        _require(lo >= 0 and hi <= TAIL_TARGET,
                 f"{label}: directed {name} exceeds 1e-18")
    mden = _interval(directed["mden"], f"{label}.engine.directed.mden")
    qupper = _interval(directed["q_upper"], f"{label}.engine.directed.q_upper")
    _require(mden[0] > 0, f"{label}: directed minimum denominator is not positive")
    _require(qupper[0] > 0 and qupper[1] < 1,
             f"{label}: directed q upper is not in (0,1)")
    _require(isinstance(directed.get("terms"), int) and directed["terms"] > 0,
             f"{label}: directed term count missing")

    required_guards = {
        "m8_evaluate_derivative_completed",
        "m5_real_phase_inverse_domain_e_le_1_over_100",
        "physical_kernel_and_denominator_guards",
        "recurrence_sign_and_contraction_guards",
        "directed_geometric_tail_closed",
        "prudent_value_and_derivative_tails_closed",
        "F_t_derivative_strictly_negative",
    }
    guards = cell.get("guards")
    _require(isinstance(guards, dict), f"{label}: guard record missing")
    for name in required_guards:
        _require(guards.get(name) is True, f"{label}: guard failed: {name}")


def _check_full_band(full_payload: dict, diagnostic: dict) -> dict:
    _require(full_payload.get("status") == "pass", "M10 full receipt is not passing")
    _require(full_payload.get("classification") ==
             "EXACT N=32 FULL PHASE-BAND CERTIFICATE",
             "M10 receipt is not full-mode")
    _require(full_payload.get("index") == N, "M10 index changed")
    _require(full_payload.get("interval_bits") == BITS, "M10 interval precision changed")
    _require(full_payload.get("phase_band") == PHASE_BAND,
             "M10 phase band changed")
    _require(full_payload.get("cell_count") == CELL_COUNT,
             "M10 cell count changed")
    _require(full_payload.get("full_coverage") is True,
             "M10 receipt does not claim full coverage")
    _require(full_payload.get("partial_mode") is False,
             "M10 full receipt is marked partial")
    _require(full_payload.get("partition_adjacent") is True,
             "M10 partition adjacency flag is false")
    _require(full_payload.get("cells_requested") == list(range(CELL_COUNT)),
             "M10 requested cells are not exactly 0..127")
    _require(full_payload.get("cells_certified") == CELL_COUNT,
             "M10 certified cell count is not 128")
    _require(full_payload.get("scope") ==
             "N=32 and theta in [0.8,0.9] only; no claim for unlisted N "
             "or for poles outside this phase band",
             "M10 scope text changed")
    _require(full_payload.get("conclusion") ==
             "exactly one simple noncancelled W pole in the N=32 phase band "
             "theta in [0.8,0.9]",
             "M10 conclusion text changed or overclaims")
    _require("no claim for unlisted N" in full_payload["scope"],
             "M10 scope omits unlisted-index limitation")

    outer = full_payload.get("outer_t_bracket")
    _require(isinstance(outer, list) and len(outer) == 2,
             "M10 outer bracket is malformed")
    outer_left, outer_right = map(F, outer)
    _require(outer_left < outer_right, "M10 outer bracket is empty")
    _check_i384_covering(
        full_payload.get("outer_t_interval"),
        outer_left,
        outer_right,
        "M10.outer_t_interval",
    )

    endpoints = full_payload.get("endpoint_phase_intervals")
    _require(isinstance(endpoints, dict), "M10 endpoint phase records missing")
    left_edge = endpoints.get("left")
    right_edge = endpoints.get("right")
    _require(isinstance(left_edge, dict) and isinstance(right_edge, dict),
             "M10 endpoint phase records malformed")
    _require(left_edge.get("target") == "164/5" and
             left_edge.get("choose") == "lower",
             "M10 left endpoint target/side changed")
    _require(right_edge.get("target") == "329/10" and
             right_edge.get("choose") == "upper",
             "M10 right endpoint target/side changed")
    for edge, endpoint, relation, target in (
        (left_edge, outer_left, "a(t_outer)<target", F(164, 5)),
        (right_edge, outer_right, "a(t_outer)>target", F(329, 10)),
    ):
        _require(edge.get("bisection_iterations") == 80,
                 "M10 endpoint bisection count changed")
        _require(edge.get("outer_t") == str(endpoint),
                 "M10 endpoint t does not match outer bracket")
        cert = edge.get("outer_endpoint_certificate", {})
        _require(cert.get("verified") is True and cert.get("relation") == relation,
                 "M10 endpoint relation certificate failed")
        phase_lo, phase_hi = map(F, edge.get("outer_phase_fraction", []))
        phase_a = _interval(edge.get("outer_phase", {}).get("a"),
                            "M10 endpoint phase a")
        _require((phase_lo, phase_hi) == phase_a,
                 "M10 endpoint phase fractions disagree with interval")
        if relation == "a(t_outer)<target":
            _require(phase_hi < target, "M10 left phase endpoint misses target")
        else:
            _require(phase_lo > target, "M10 right phase endpoint misses target")
    _require(left_edge["outer_t"] == outer[0] and
             right_edge["outer_t"] == outer[1],
             "M10 endpoint records do not define outer bracket")

    rows = diagnostic.get("rows")
    _require(diagnostic.get("classification") ==
             "EXPLORATORY FULL-BAND SUBDIVISION; NOT A CANONICAL CERTIFICATE",
             "retained diagnostic classification changed")
    _require(diagnostic.get("index") == N and
             diagnostic.get("count") == CELL_COUNT and
             isinstance(rows, list) and len(rows) == CELL_COUNT,
             "retained diagnostic does not contain 128 N=32 rows")

    cells = full_payload.get("cells")
    _require(isinstance(cells, list) and len(cells) == CELL_COUNT,
             "M10 full receipt does not retain all cells")
    for index, (cell, diagnostic_row) in enumerate(zip(cells, rows)):
        left = outer_left + (outer_right - outer_left) * index / CELL_COUNT
        right = outer_left + (outer_right - outer_left) * (index + 1) / CELL_COUNT
        _require(diagnostic_row.get("cell") == index,
                 f"diagnostic cell order changed at {index}")
        _check_cell(cell, index, left, right, diagnostic_row)
    for previous, current in zip(cells, cells[1:]):
        _require(previous["t_bracket"][1] == current["t_bracket"][0],
                 "M10 cell partition has a gap or overlap")
    _require(cells[0]["t_bracket"][0] == outer[0] and
             cells[-1]["t_bracket"][1] == outer[1],
             "M10 cells do not reach both outer endpoints")
    return {
        "cells": CELL_COUNT,
        "outer_t_bracket": outer,
        "endpoint_phase_inequalities": True,
        "adjacent_geometry": True,
        "per_cell_phase_and_tail_checks": True,
        "per_cell_negative_F_t": True,
        "diagnostic_derivatives_equal": True,
    }


def _check_structural_receipt(structural_payload: dict) -> dict:
    _require(structural_payload.get("status") == "pass",
             "M10 structural receipt is not passing")
    _require(structural_payload.get("scope") ==
             "component lemmas only; full denominator phase sign and index coverage open",
             "M10 structural scope changed")
    _require("full denominator phase sign" in structural_payload["scope"],
             "M10 structural receipt lost open full-sign scope")

    structural_review = (ROOT / "proofs" /
                         "M10_STRUCTURAL_WRAPPER_REVIEW.md").read_text()
    _require(EXPECTED_STRUCTURAL_WRAPPER_HASH in structural_review,
             "structural wrapper review lacks final wrapper hash")
    wrapper_hash = _sha256_path(ROOT / "experiments" /
                                "m10_structural_batch.py")
    _require(wrapper_hash == EXPECTED_STRUCTURAL_WRAPPER_HASH,
             "structural wrapper hash differs from final review")
    _require("22 sources" in structural_review and
             "results/m6-coefficient-v1/payload.json" in structural_review,
             "structural wrapper review lacks final dependency correction")

    # Calling the wrapper replays only the three inexpensive component
    # producers.  It also exercises the wrapper's frozen M6 receipt input.
    from experiments.m10_structural_batch import payload as replay_payload

    replay = replay_payload()
    _require(replay == structural_payload,
             "structural wrapper replay differs from structural receipt")
    component_hashes = {}
    for name, expected in EXPECTED_STRUCTURAL_COMPONENT_HASHES.items():
        actual = _canonical_json_hash(structural_payload[name])
        _require(actual == expected,
                 f"structural component hash changed: {name}")
        _require(expected in structural_review,
                 f"structural review lacks component hash: {name}")
        component_hashes[name] = actual

    weight = structural_payload["weight_and_product"]
    _require(weight.get("full_F_phase_sign") == "NOT PROVED",
             "structural component overclaims full F phase sign")
    _require(weight.get("full_index_coverage") == "NOT PROVED",
             "structural component overclaims index coverage")
    return {
        "wrapper_sha256": wrapper_hash,
        "component_hashes": component_hashes,
        "replay_matches_receipt": True,
        "full_F_phase_sign": "NOT PROVED",
        "full_index_coverage": "NOT PROVED",
    }


def check() -> dict:
    if not __debug__:
        raise RuntimeError(
            "Run without -O: receipt and interval guards must remain enabled"
        )

    full_payload = receipt("m10-full-band-v1")
    structural_payload = receipt("m10-structural-v1")
    diagnostic = _load_json(DIAGNOSTIC_PATH)

    full_result = _check_full_band(full_payload, diagnostic)
    m7_result = _check_m7_transfer(full_payload)
    review_result = _check_review_first_cell(full_payload)
    structural_result = _check_structural_receipt(structural_payload)
    review_hashes = _check_math_review_hashes()

    return {
        "status": "PASS: M10 N=32 full-band and structural receipts verified",
        "receipts": ["m10-full-band-v1", "m10-structural-v1"],
        "full_band": full_result,
        "m7_transfer": m7_result,
        "first_cell_review": review_result,
        "structural": structural_result,
        "reviewed_source_hashes": review_hashes,
        "scope": "exactly one simple noncancelled W pole on the N=32 phase band theta in [0.8,0.9]",
        "full_W_coverage": "OPEN: no claim for unlisted N or complete asymptotic coverage",
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
