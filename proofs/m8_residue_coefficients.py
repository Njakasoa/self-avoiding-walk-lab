"""Exact interval enclosure for the first logarithmic W-residue coefficient.

The input is the frozen M5 critical-integral payload.  This file certifies
only coefficients of the limiting expansion; the finite-N transfer is the
analytic statement in ``M8_RESIDUE_EXPANSION.md``.
"""
import json
from fractions import Fraction as F
from pathlib import Path

from proofs.m3_prudent_intervals import I
from proofs.m3_critical_integrals import pi_interval, sine, compact


ROOT = Path(__file__).resolve().parents[1]


def produce():
    if not __debug__:
        raise RuntimeError("Run without -O: interval assertions are required")
    raw = json.loads((ROOT / "results/m5-critical-v1/payload.json").read_text())

    def recover(x):
        if x["denominator_power_of_two"] != 384:
            raise ValueError("unexpected source precision")
        return I(int(x["lower_numerator"]), int(x["upper_numerator"]), raw=True)

    (pre1, _pre2), (post1, _post2) = [
        [recover(x) for x in row] for row in raw["integrals"]
    ]
    sigma = I(2).sqrt() - 1
    eta = 1 / (sigma + 1)
    A = 1 / (sigma * sigma)
    theta = I(F(raw["unique_theta_star_bracket"][0]),
              F(raw["unique_theta_star_bracket"][1]))
    s_star = recover(raw["s_star"]["exact"])
    pi = pi_interval()

    J = (1 - sigma) * post1 - 4 * sigma * sigma * _post2
    angle = pi * (eta - theta)
    sin_angle = sine(angle)
    B = A * sine(pi * theta) / sin_angle
    B_prime = A * pi * sine(pi * eta) / (sin_angle * sin_angle)
    p_star = sigma - A * pre1 + post1 * B
    f_star = J * B_prime
    # C1 is the positive magnitude in theta_N=theta*-C1/log(N)+O(log^-2 N).
    C1 = 2 * sigma * p_star / f_star
    C_res = -p_star * s_star * s_star / (8 * f_star)
    # Combine the two affine-profile terms before interval multiplication.
    # This avoids artificial dependency loss in
    # C1*F0''/F0' - 4*sigma*P0'/F0'.
    alpha = pi * eta
    cos_alpha = sine(pi / 2 + alpha)
    p0 = sigma - A * pre1
    Q = B * B + 2 * A * cos_alpha * B + A * A
    numerator = ((p0 - post1 * A * cos_alpha) * B
                 + p0 * A * cos_alpha - post1 * A * A)
    residue_log_factor = (4 * sigma / J) * numerator / Q
    # First correction in N^3 Res W = C_res + C_res_log/log(N)+O(log^-2 N).
    C_res_log = C_res * residue_log_factor
    if not (C1.lo > 0 and C_res.hi < 0):
        raise ArithmeticError("critical coefficient signs failed")

    def record(x):
        return {"exact": x.record(), "display": compact(x, 12)}

    return {
        "classification": "EXACT LIMIT-COEFFICIENT ENCLOSURE; finite transfer is analytic",
        "critical_input": "results/m5-critical-v1/payload.json",
        "theta_star_bracket": raw["unique_theta_star_bracket"],
        "phase_C1": record(C1),
        "N_cubed_residue_C0": record(C_res),
        "N_cubed_residue_C1_log": record(C_res_log),
        "residue_log_factor": record(residue_log_factor),
        "status": "pass",
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
