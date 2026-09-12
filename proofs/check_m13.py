"""Fail-closed verification of the reviewed M13 phase package.

The checker replays the canonical component receipt, verifies the exact
combination margin, and requires an independent hash table for every released
M13 mathematical source and for this wrapper/checker pair.  The conclusion is
strict phase decrease and whole-band at-most-one uniqueness; existence for
every index remains outside the receipt.
"""

from __future__ import annotations

import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path
from typing import Any

from proofs.check_m3 import receipt


ROOT = Path(__file__).resolve().parents[1]


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def _sha256(path: Path) -> str:
    _require(path.is_file(), f"missing reviewed source: {path}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _review_table(review: str, paths: tuple[str, ...]) -> dict[str, str]:
    review_path = ROOT / review
    _require(review_path.is_file(), f"missing final M13 review: {review}")
    text = review_path.read_text()
    table = {
        name.strip(): digest
        for name, digest in re.findall(
            r"^\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|",
            text,
            flags=re.MULTILINE,
        )
    }
    result: dict[str, str] = {}
    for rel in paths:
        _require(rel in table, f"{review}: missing hash for {rel}")
        actual = _sha256(ROOT / rel)
        _require(table[rel] == actual, f"{review}: stale hash for {rel}")
        result[rel] = actual
    return result


def _check_reviews() -> dict[str, dict[str, str]]:
    component_reviews = {
        "proofs/M13_BOUNDARY_REVIEW.md": (
            "proofs/M13_BOUNDARY_PHASE.md",
            "proofs/m13_boundary_bounds.py",
        ),
        "proofs/M13_MIDDLE_REVIEW.md": (
            "proofs/M13_MIDDLE_MASS.md",
            "proofs/m13_middle_bounds.py",
        ),
        "proofs/M13_MIDDLE_STRENGTHENED_REVIEW.md": (
            "proofs/M13_MIDDLE_STRENGTHENED.md",
            "proofs/m13_middle_strengthened.py",
        ),
        "proofs/M13_PRE_MASS_REVIEW.md": (
            "proofs/M13_PRE_MASS.md",
            "proofs/m13_mass_bounds.py",
            "proofs/m7_finite_poles.py",
        ),
        "proofs/M13_PRE_PHASE_REVIEW.md": (
            "proofs/M13_PRE_CROSSING_RESEARCH.md",
            "proofs/m13_pre_phase_bounds.py",
        ),
        "proofs/M13_TAIL_REVIEW.md": (
            "proofs/M13_TAIL_PHASE_BOUND.md",
            "proofs/m13_tail_bounds.py",
        ),
        "proofs/M13_COMBINATION_REVIEW.md": (
            "proofs/M13_UNIFORM_PHASE_DERIVATIVE.md",
            "proofs/m13_combination_bounds.py",
        ),
    }
    checked = {
        review: _review_table(review, paths)
        for review, paths in component_reviews.items()
    }
    checked["proofs/M13_WRAPPER_REVIEW.md"] = _review_table(
        "proofs/M13_WRAPPER_REVIEW.md",
        ("experiments/m13_phase_batch.py", "proofs/check_m13.py"),
    )
    return checked


def _check_components(data: dict[str, Any]) -> dict[str, Any]:
    _require(data.get("status") == "pass", "M13 wrapper status is not pass")
    _require(
        data.get("domain")
        == {
            "N": "integer N>=32",
            "theta": "[4/5,9/10]",
            "phase_inverse": "physical real phase e_N(theta)>0",
        },
        "M13 domain marker changed",
    )

    boundary = data.get("boundary", {})
    _require(boundary.get("status") == "pass", "M13 boundary component failed")
    _require(
        boundary.get("B_theta_upper_allowance") == "6/(5*N^2)",
        "M13 boundary allowance changed",
    )
    _require(all(boundary.get("claims", {}).values()), "M13 boundary claims failed")

    middle = data.get("middle", {})
    _require(middle.get("status") == "pass", "M13 middle component failed")
    _require(
        middle.get("middle_phase_upper_allowance") == "-3/56",
        "M13 preliminary middle allowance changed",
    )
    _require(all(middle.get("claims", {}).values()), "M13 middle claims failed")

    strengthened = data.get("middle_strengthened", {})
    _require(
        strengthened.get("status") == "pass",
        "M13 strengthened middle component failed",
    )
    _require(
        strengthened.get("middle_phase_upper_allowance") == "-9/50",
        "M13 strengthened middle allowance changed",
    )
    _require(
        all(strengthened.get("claims", {}).values()),
        "M13 strengthened middle claims failed",
    )

    mass = data.get("mass", {})
    _require(mass.get("status") == "pass", "M13 mass component failed")
    mass_claims = mass.get("claims", {})
    _require(mass_claims.get("mass_general") is True, "M13 general mass bound failed")
    _require(
        mass_claims.get("mass_low_indices") is True,
        "M13 low-index mass bound failed",
    )
    _require(all(mass_claims.values()), "M13 mass claims failed")

    pre_phase = data.get("pre_phase", {})
    _require(pre_phase.get("status") == "pass", "M13 pre-phase component failed")
    pre_claims = pre_phase.get("claims", {})
    _require(
        pre_claims.get("pre_upper_lt_2.06") is True,
        "M13 pre-phase relative derivative allowance failed",
    )
    _require(all(pre_claims.values()), "M13 pre-phase claims failed")

    tail = data.get("tail", {})
    _require(tail.get("status") == "pass", "M13 tail component failed")
    tail_claims = tail.get("claims", {})
    _require(
        tail_claims.get("absolute_tail_derivative_lt_1e_minus_3") is True,
        "M13 tail derivative allowance failed",
    )
    _require(
        tail_claims.get("full_F_phase_sign") == "NOT PROVED",
        "M13 tail scope marker changed",
    )
    _require(
        tail_claims.get("existence_or_uniqueness") == "NOT PROVED",
        "M13 tail existence scope changed",
    )

    return {
        "boundary": boundary.get("B_theta_upper_allowance"),
        "middle": middle.get("middle_phase_upper_allowance"),
        "mass_general": mass_claims.get("mass_general"),
        "mass_low_indices": mass_claims.get("mass_low_indices"),
        "pre_phase": pre_claims.get("pre_upper_lt_2.06"),
        "tail": tail_claims.get("absolute_tail_derivative_lt_1e_minus_3"),
    }


def _check_combination(data: dict[str, Any]) -> dict[str, str]:
    combination = data.get("combination", {})
    _require(combination.get("status") == "pass", "M13 combination failed")
    checks = combination.get("checks", {})
    _require(all(checks.values()), "M13 combination arithmetic checks failed")
    bounds = combination.get("bounds", {})
    _require(
        bounds.get("full_derivative_upper") == "-3141/64000",
        "M13 combined derivative margin changed",
    )
    _require(
        combination.get("scope", {}).get("all_index_existence") == "NOT PROVED",
        "M13 combination existence scope changed",
    )
    _require(
        combination.get("scope", {}).get("new_scan") == "NONE",
        "M13 combination scan scope changed",
    )

    # Recheck the displayed case split independently of the producer.
    pre_low = F(103, 50) * 2 / 32
    pre_high = F(103, 50) * F(31, 10) / 65
    boundary = F(6, 5) / 32**2
    total = pre_low + boundary - F(9, 50) + F(1, 1000)
    _require(pre_low == F(103, 800), "M13 low-index arithmetic changed")
    _require(pre_high < pre_low, "M13 high-index case is not dominated")
    _require(total == -F(3141, 64000), "M13 exact total changed")
    _require(total < -F(1, 25), "M13 strict margin failed")

    return {
        "full_derivative_upper": bounds["full_derivative_upper"],
        "strictly_below_minus_1_over_25": True,
        "all_index_existence": "NOT PROVED",
        "new_scan": "NONE",
    }


def check() -> dict[str, Any]:
    if not __debug__:
        raise RuntimeError("Run without -O: receipt and review guards required")

    from experiments.m13_phase_batch import payload

    frozen = receipt("m13-phase-v1")
    replay = payload()
    _require(frozen == replay, "M13 component replay differs from frozen receipt")
    component_summary = _check_components(frozen)
    combination_summary = _check_combination(frozen)
    reviewed = _check_reviews()

    _require(
        frozen.get("full_F_phase_sign") == "F_theta<-3141/64000<-1/25",
        "M13 full derivative scope marker changed",
    )
    _require(
        frozen.get("all_index_existence") == "NOT PROVED",
        "M13 all-index existence marker changed",
    )
    _require(frozen.get("new_scan") == "NONE", "M13 new-scan marker changed")

    return {
        "status": "PASS: reviewed M13 uniform real phase derivative package",
        "receipt": "m13-phase-v1",
        "domain": {"N_min": 32, "phase_band": ["4/5", "9/10"]},
        "components": component_summary,
        "combination": combination_summary,
        "reviewed_source_hashes": reviewed,
        "conclusion": (
            "F_theta<-3141/64000<-1/25; at most one zero per band, and any "
            "zero yields a simple noncancelled W pole"
        ),
        "all_index_existence": "NOT PROVED",
        "full_W_coverage": (
            "OPEN: existence for intermediate 32<=N<10^27 remains unproved "
            "apart from frozen finite checkpoints"
        ),
        "new_scan": "NONE",
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
