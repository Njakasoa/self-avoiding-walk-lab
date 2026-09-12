"""Portable exact N=32 full-phase-band derivative certificate.

The producer uses the frozen M8 interval-jet engine on rational adjacent
cells.  It is deliberately scoped to the phase band [0.8, 0.9] at N=32.
The default call certifies all 128 cells; produce(cell_subset=[...]) is an
explicit partial review mode and never claims full-band coverage.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable

from proofs.m7_finite_poles import BITS, SCALE, I384, SEEDS, phase_data
from proofs.m8_finite_derivatives import Jet384, evaluate_derivative


N = 32
CELL_COUNT = 128
PHASE_LEFT = F(4, 5)
PHASE_RIGHT = F(9, 10)
PHASE_SEED_HALF_WIDTH = F(1, 10**7)
PHASE_BISECTIONS = 80
M7_PAYLOAD_SHA256 = (
    "75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f"
)
ROOT = Path(__file__).resolve().parents[1]


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def _record(value: Any) -> Any:
    """Serialize every I384/Jet384 object and preserve exact rational strings."""

    if isinstance(value, I384):
        return value.record()
    if isinstance(value, Jet384):
        return value.record()
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _record(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_record(item) for item in value]
    return value


def _interval_fraction(box: I384) -> tuple[F, F]:
    return F(box.lo, SCALE), F(box.hi, SCALE)


def _record_phase_box(box: I384, lower: F, upper: F, label: str) -> dict:
    lo, hi = _interval_fraction(box)
    _require(lo > lower, f"{label}: lower endpoint is not strictly above band")
    _require(hi < upper, f"{label}: upper endpoint is not strictly below band")
    return {
        "interval": box.record(),
        "fraction_lower": str(lo),
        "fraction_upper": str(hi),
        "strict_band": [str(lower), str(upper)],
    }


def _phase_edge(target: F, *, choose: str) -> dict[str, Any]:
    """Bisect a seed bracket until endpoint phase intervals separate target."""

    if choose not in {"lower", "upper"}:
        raise ValueError("choose must be lower or upper")
    seed = F(SEEDS[N])
    lo = seed - PHASE_SEED_HALF_WIDTH
    hi = seed + PHASE_SEED_HALF_WIDTH
    initial_lo, initial_hi = lo, hi

    left_phase = phase_data(I384(lo))["a"]
    right_phase = phase_data(I384(hi))["a"]
    left_a = _interval_fraction(left_phase)
    right_a = _interval_fraction(right_phase)
    _require(left_a[1] < target, "initial phase lower endpoint misses target")
    _require(right_a[0] > target, "initial phase upper endpoint misses target")

    for _ in range(PHASE_BISECTIONS):
        mid = (lo + hi) / 2
        phase_box = phase_data(I384(mid))["a"]
        phase_lo, phase_hi = _interval_fraction(phase_box)
        if phase_hi < target:
            lo = mid
        elif phase_lo > target:
            hi = mid
        else:
            raise ArithmeticError(
                "phase bisection interval still straddles target after "
                f"{PHASE_BISECTIONS} iterations"
            )

    outer_t = lo if choose == "lower" else hi
    outer_phase = phase_data(I384(outer_t))
    outer_a = outer_phase["a"]
    outer_lo, outer_hi = _interval_fraction(outer_a)
    if choose == "lower":
        _require(
            outer_hi < target,
            "left outer endpoint phase interval does not certify a(target)-",
        )
    else:
        _require(
            outer_lo > target,
            "right outer endpoint phase interval does not certify a(target)+",
        )

    return {
        "target": str(target),
        "choose": choose,
        "initial_t_bracket": [str(initial_lo), str(initial_hi)],
        "bisection_iterations": PHASE_BISECTIONS,
        "root_t_bracket": [str(lo), str(hi)],
        "outer_t": outer_t,
        "outer_phase": outer_phase,
        "outer_phase_fraction": [str(outer_lo), str(outer_hi)],
        "outer_endpoint_certificate": {
            "verified": True,
            "relation": (
                "a(t_outer)<target"
                if choose == "lower" else
                "a(t_outer)>target"
            ),
        },
    }


def _load_frozen_m7_n32() -> dict[str, Any]:
    """Load and validate the accepted narrow N=32 M7 existence row."""

    path = ROOT / "results" / "m7-finite-v1" / "payload.json"
    _require(path.is_file(), f"missing frozen M7 payload: {path}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    _require(digest == M7_PAYLOAD_SHA256, "frozen M7 payload hash changed")
    payload = json.loads(path.read_text())
    _require(payload.get("status") == "pass", "M7 payload is not accepted")
    _require(payload.get("indices") == [32, 64, 128, 256, 512, 1024],
             "M7 index scope changed")
    rows = [row for row in payload.get("rows", []) if row.get("index") == N]
    _require(len(rows) == 1, "M7 payload does not contain one N=32 row")
    row = rows[0]
    _require(row.get("phase_source_check", {}).get("source_pole_free") is True,
             "M7 N=32 source-pole check missing")
    phase_band = row["phase_source_check"]["phase_band"]
    _require(
        [F(phase_band[0]), F(phase_band[1])] == [N + PHASE_LEFT, N + PHASE_RIGHT],
        "M7 N=32 phase band changed",
    )

    left_f = _interval_fraction_from_record(row["left"]["F_certificate"])
    right_f = _interval_fraction_from_record(row["right"]["F_certificate"])
    numerator = _interval_fraction_from_record(
        row["uniform_numerator"]["P_plus_one_certificate"]
    )
    _require(left_f[0] > 0, "frozen M7 N=32 left F sign is not positive")
    _require(right_f[1] < 0, "frozen M7 N=32 right F sign is not negative")
    _require(numerator[1] < 0, "frozen M7 N=32 numerator is not negative")

    return {
        "payload_sha256": digest,
        "index": N,
        "t_bracket": list(row["t_bracket"]),
        "phase_band": list(phase_band),
        "source_pole_free": True,
        "left_F_certificate": row["left"]["F_certificate"],
        "right_F_certificate": row["right"]["F_certificate"],
        "uniform_P_plus_one_certificate": (
            row["uniform_numerator"]["P_plus_one_certificate"]
        ),
        "existence_and_noncancellation": (
            "accepted frozen M7 N=32 narrow bracket"
        ),
    }


def _interval_fraction_from_record(record: dict[str, Any]) -> tuple[F, F]:
    power = int(record["denominator_power_of_two"])
    denominator = 1 << power
    return (
        F(int(record["lower_numerator"]), denominator),
        F(int(record["upper_numerator"]), denominator),
    )


def _validate_m7_containment(
    outer_left: F, outer_right: F, frozen: dict[str, Any]
) -> dict[str, Any]:
    narrow_left, narrow_right = (
        F(frozen["t_bracket"][0]),
        F(frozen["t_bracket"][1]),
    )
    _require(outer_left < narrow_left, "outer band misses M7 narrow left edge")
    _require(narrow_right < outer_right, "outer band misses M7 narrow right edge")
    return {
        "outer_contains_frozen_narrow_bracket": True,
        "frozen_t_bracket": [str(narrow_left), str(narrow_right)],
    }


def _validate_engine_guards(result: dict[str, Any]) -> dict[str, Any]:
    """Check and label the guards enforced by evaluate_derivative."""

    q = result["q"]
    epsilon = result["epsilon"]
    d_i = result["D_I"]
    _require(q.x.lo > 0 and q.x.hi < SCALE, "kernel q is not in (0,1)")
    _require(epsilon.x.lo > 0, "kernel epsilon is not positive")
    _require(
        epsilon.x.hi * 100 < SCALE,
        "phase inverse epsilon is outside the M5 e<=1/100 domain",
    )
    _require(0 < d_i.x.lo and d_i.x.hi < SCALE,
             "D_I is not in (0,1)")

    tail = result["tail"]
    r_box = tail["R"]
    _require(0 < r_box.x.lo and r_box.x.hi < SCALE,
             "post-tail ratio box is not in (0,1)")
    target = F(1, 10**18)
    for name in (
        "tail_P",
        "tail_H",
        "tail_P_derivative",
        "tail_H_derivative",
    ):
        box = tail[name]
        lo, hi = _interval_fraction(box)
        _require(lo >= 0, f"{name} has a negative lower bound")
        _require(hi <= target, f"{name} exceeds the full-tail target")

    directed = result["directed_meta"]
    for name in ("tail_value", "tail_derivative"):
        lo, hi = _interval_fraction(directed[name])
        _require(lo >= 0, f"directed {name} has a negative lower bound")
        _require(hi <= target, f"directed {name} exceeds the tail target")
    mden = directed["mden"]
    q_upper = directed["q_upper"]
    _require(mden.lo > 0, "directed minimum denominator is not positive")
    _require(q_upper.lo > 0 and q_upper.hi < SCALE,
             "directed q upper box is not in (0,1)")

    derivative = result["F"].d
    _require(derivative.hi < 0, "F_t derivative is not strictly negative")

    return {
        "m8_evaluate_derivative_completed": True,
        "m5_real_phase_inverse_domain_e_le_1_over_100": True,
        "physical_kernel_and_denominator_guards": True,
        "recurrence_sign_and_contraction_guards": True,
        "directed_geometric_tail_closed": True,
        "prudent_value_and_derivative_tails_closed": True,
        "F_t_derivative_strictly_negative": True,
    }


def _certify_cell(cell: int, left: F, right: F) -> dict[str, Any]:
    _require(left < right, f"cell {cell} has empty rational bracket")
    t_box = I384(left, right)
    phase = phase_data(t_box)
    phase_a = _record_phase_box(
        phase["a"], F(N), F(N + 1),
        f"cell {cell} phase a",
    )
    phase_b = _record_phase_box(
        phase["b"], F(N), F(N + 1),
        f"cell {cell} phase b",
    )
    result = evaluate_derivative(t_box)
    guards = _validate_engine_guards(result)
    return {
        "cell": cell,
        "t_bracket": [str(left), str(right)],
        "t_interval": t_box.record(),
        "phase_band_checks": {"a": phase_a, "b": phase_b},
        "phase_data": _record(phase),
        "derivative": result["F"].d.record(),
        "guards": guards,
        "engine": _record(result),
    }


def _normalize_subset(cell_subset: Iterable[int] | int | None) -> tuple[int, ...]:
    if cell_subset is None:
        return tuple(range(CELL_COUNT))
    if isinstance(cell_subset, int):
        subset = (cell_subset,)
    else:
        subset = tuple(int(cell) for cell in cell_subset)
    _require(bool(subset), "cell_subset must not be empty")
    _require(
        subset == tuple(sorted(set(subset))),
        "cell_subset must be sorted and contain distinct cells",
    )
    _require(all(0 <= cell < CELL_COUNT for cell in subset),
             "cell_subset contains an invalid cell")
    return subset


def produce(cell_subset: Iterable[int] | int | None = None) -> dict[str, Any]:
    """Produce the N=32 full-band or explicitly partial certificate."""

    if not __debug__:
        raise RuntimeError(
            "Run without -O: M8 interval and source guards are required"
        )

    subset = _normalize_subset(cell_subset)
    frozen_m7 = _load_frozen_m7_n32()
    left_edge = _phase_edge(N + PHASE_LEFT, choose="lower")
    right_edge = _phase_edge(N + PHASE_RIGHT, choose="upper")
    outer_left = left_edge["outer_t"]
    outer_right = right_edge["outer_t"]
    _require(outer_left < outer_right, "outer full-band t interval is empty")
    containment = _validate_m7_containment(
        outer_left, outer_right, frozen_m7
    )

    cells = []
    for cell in subset:
        left = outer_left + (outer_right - outer_left) * cell / CELL_COUNT
        right = (
            outer_left
            + (outer_right - outer_left) * (cell + 1) / CELL_COUNT
        )
        cells.append(_certify_cell(cell, left, right))

    full = cell_subset is None
    if full:
        _require(len(cells) == CELL_COUNT, "full mode did not produce 128 cells")
        _require(
            [cell["cell"] for cell in cells] == list(range(CELL_COUNT)),
            "full mode cell list is not complete",
        )
        _require(
            cells[0]["t_bracket"][0] == str(outer_left)
            and cells[-1]["t_bracket"][1] == str(outer_right),
            "full mode does not reach both outer endpoints",
        )
        for previous, current in zip(cells, cells[1:]):
            _require(
                previous["t_bracket"][1] == current["t_bracket"][0],
                "full mode rational cell partition has a gap or overlap",
            )

    return {
        "classification": (
            "EXACT N=32 FULL PHASE-BAND CERTIFICATE"
            if full else
            "PARTIAL N=32 CELL REVIEW; DOES NOT CLAIM FULL COVERAGE"
        ),
        "status": "pass",
        "index": N,
        "phase_band": [str(N + PHASE_LEFT), str(N + PHASE_RIGHT)],
        "cell_count": CELL_COUNT,
        "cells_requested": list(subset),
        "cells_certified": len(cells),
        "full_coverage": full,
        "partial_mode": not full,
        "partition_adjacent": full,
        "interval_bits": BITS,
        "phase_bisection_iterations": PHASE_BISECTIONS,
        "outer_t_bracket": [str(outer_left), str(outer_right)],
        "outer_t_interval": I384(outer_left, outer_right).record(),
        "endpoint_phase_intervals": {
            "left": _record(left_edge),
            "right": _record(right_edge),
        },
        "frozen_m7_n32": frozen_m7,
        "containment": containment,
        "cells": cells,
        "scope": (
            "N=32 and theta in [0.8,0.9] only; no claim for unlisted N "
            "or for poles outside this phase band"
        ),
        "conclusion": (
            "exactly one simple noncancelled W pole in the N=32 phase band "
            "theta in [0.8,0.9]"
            if full else
            "partial cell evidence only; no full-band conclusion"
        ),
    }


def produce_first_cell() -> dict[str, Any]:
    """Run the bounded first-cell review without a full-coverage claim."""

    return produce(cell_subset=(0,))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--first-cell", action="store_true",
        help="certify cell 0 only and explicitly avoid a full-band claim",
    )
    args = parser.parse_args()
    data = produce_first_cell() if args.first_cell else produce()
    print(json.dumps(data, indent=2, sort_keys=True))
