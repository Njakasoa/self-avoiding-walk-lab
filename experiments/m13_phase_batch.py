"""Record the reviewed M13 uniform real phase-derivative package."""

from __future__ import annotations

import argparse
import contextlib
import io
import json

from proofs.check_m3 import receipt
from proofs.m13_boundary_bounds import produce as boundary
from proofs.m13_mass_bounds import produce as mass
from proofs.m13_middle_bounds import produce as middle
from proofs.m13_middle_strengthened import produce as middle_strengthened
from proofs.m13_pre_phase_bounds import main as pre_phase_main
from proofs.m13_tail_bounds import produce as tail
from proofs.m13_combination_bounds import produce as combination
from src.provenance import run_record


def _pre_phase_payload() -> dict:
    """Replay the pre-phase producer, whose historical API prints JSON."""
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        pre_phase_main()
    text = output.getvalue().strip()
    try:
        result = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ArithmeticError("M13 pre-phase replay did not return JSON") from exc
    if not isinstance(result, dict) or result.get("status") != "pass":
        raise ArithmeticError("M13 pre-phase arithmetic replay did not pass")
    return result


def payload() -> dict:
    if not __debug__:
        raise RuntimeError("Run without -O: interval and receipt guards required")

    # The M13 producers use both the frozen finite phase geometry and the
    # reviewed scalar/product package.  Validate both receipts before replay.
    receipt("m7-finite-v1")
    receipt("m10-structural-v1")
    receipt("m11-phase-v1")
    receipt("m12-noncancellation-v1")

    result = {
        "status": "pass",
        "domain": {
            "N": "integer N>=32",
            "theta": "[4/5,9/10]",
            "phase_inverse": "physical real phase e_N(theta)>0",
        },
        "boundary": boundary(),
        "middle": middle(),
        "middle_strengthened": middle_strengthened(),
        "mass": mass(),
        "pre_phase": _pre_phase_payload(),
        "tail": tail(),
        "combination": combination(),
        "full_F_phase_sign": "F_theta<-3141/64000<-1/25",
        "existence_or_uniqueness": (
            "at most one zero per full band; every zero is simple and yields "
            "a noncancelled W pole; all-index existence NOT PROVED"
        ),
        "all_index_existence": "NOT PROVED",
        "new_scan": "NONE",
        "scope": (
            "uniform real phase derivative and full-band at-most-one theorem "
            "for integer N>=32; no all-index existence claim"
        ),
    }
    return result


def main() -> None:
    if not __debug__:
        raise RuntimeError("Run without -O: receipt and interval guards required")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment_id")
    args = parser.parse_args()
    sources = [
        "experiments/m13_phase_batch.py",
        "proofs/m13_boundary_bounds.py",
        "proofs/M13_BOUNDARY_PHASE.md",
        "proofs/m13_middle_bounds.py",
        "proofs/M13_MIDDLE_MASS.md",
        "proofs/m13_middle_strengthened.py",
        "proofs/M13_MIDDLE_STRENGTHENED.md",
        "proofs/m13_mass_bounds.py",
        "proofs/M13_PRE_MASS.md",
        "proofs/m13_pre_phase_bounds.py",
        "proofs/M13_PRE_CROSSING_RESEARCH.md",
        "proofs/m13_tail_bounds.py",
        "proofs/M13_TAIL_PHASE_BOUND.md",
        "proofs/m13_combination_bounds.py",
        "proofs/M13_UNIFORM_PHASE_DERIVATIVE.md",
        "proofs/m7_finite_poles.py",
        "proofs/M7_FINITE_TAIL.md",
        "proofs/m8_finite_derivatives.py",
        "proofs/M8_FINITE_DERIVATIVES.md",
        "proofs/m5_phase_domain.py",
        "proofs/M5_DIRECTED_LOG.md",
        "proofs/M5_DIRECTED_REFINED.md",
        "proofs/m10_beta_real.py",
        "proofs/M10_BETA_REAL.md",
        "proofs/M10_DIRECTED_MONOTONICITY.md",
        "proofs/M10_POSITIVE_COMBINED_WEIGHT.md",
        "proofs/M10_REAL_PHASE_PRODUCT.md",
        "proofs/M10_BARE_PHASE_DERIVATIVE.md",
        "proofs/M11_DIRECTED_PHASE_BOUND.md",
        "proofs/m11_directed_phase_bounds.py",
        "proofs/M11_WEIGHT_PHASE_BOUND.md",
        "proofs/m11_weight_phase_bounds.py",
        "proofs/M11_SMOOTH_PHASE_BOUND.md",
        "proofs/m11_smooth_phase_bounds.py",
        "proofs/M6_EFFECTIVE_PRODUCT.md",
        "proofs/M6_SHARP_KERNEL.md",
        "proofs/M6_REAL_MOMENT_RATE.md",
        "proofs/M12_UNIFORM_NONCANCELLATION.md",
        "proofs/m12_noncancellation_bounds.py",
        "experiments/m11_phase_batch.py",
        "experiments/m12_noncancellation_batch.py",
        "results/m11-phase-v1/payload.json",
        "results/m11-phase-v1/metadata.json",
        "proofs/check_m3.py",
        "results/m7-finite-v1/payload.json",
        "results/m7-finite-v1/metadata.json",
        "results/m10-structural-v1/payload.json",
        "results/m10-structural-v1/metadata.json",
        "results/m12-noncancellation-v1/payload.json",
        "results/m12-noncancellation-v1/metadata.json",
        "src/provenance.py",
        "requirements-lock.txt",
    ]
    command = f".venv/bin/python -m experiments.m13_phase_batch {args.experiment_id}"
    print(
        run_record(
            args.experiment_id,
            command,
            {
                "N_min": 32,
                "phase_band": ["4/5", "9/10"],
                "claim": "F_theta<-3141/64000<-1/25",
                "all_index_existence": "NOT PROVED",
                "new_scan": "NONE",
            },
            sources,
            payload,
        )
    )


if __name__ == "__main__":
    main()
