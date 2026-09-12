"""Exact arithmetic combination; analytic hypotheses are reviewed separately."""

import json
from fractions import Fraction as F

if not __debug__:
    raise RuntimeError("run without -O: M13 receipt guards are required")


def produce():
    pre_low = F(103, 50) * 2 / 32
    pre_high = F(103, 50) * F(31, 10) / 65
    boundary = F(6, 5) / 32**2
    middle = -F(9, 50)
    tail = F(1, 1000)
    total = pre_low + boundary + middle + tail
    checks = {
        "integer_case_split_no_gap": 64 + 1 == 65,
        "pre_low_upper": pre_low == F(103, 800),
        "pre_high_below_low": pre_high < pre_low,
        "boundary_upper": boundary == F(3, 2560),
        "total_upper": total == -F(3141, 64000),
        "uniform_negative_margin": total < -F(1, 25),
    }
    if not all(checks.values()):
        raise ArithmeticError("M13 combination inequality failed")
    return {
        "status": "pass",
        "checks": checks,
        "bounds": {"pre_low_upper": str(pre_low),
                   "pre_high_upper": str(pre_high),
                   "boundary_upper": str(boundary),
                   "middle_upper": str(middle), "tail_abs_upper": str(tail),
                   "full_derivative_upper": str(total)},
        "scope": {
            "N": "integer N>=32", "theta": "[4/5,9/10]",
            "analytic_conclusion": "F_theta<-1/25; at most one zero per full band",
            "noncancellation": "inherited M12: every zero has 1+P<-2",
            "all_index_existence": "NOT PROVED",
            "new_scan": "NONE",
            "arithmetic_only": True,
        },
    }


if __name__ == "__main__":
    print(json.dumps(produce(), indent=2, sort_keys=True))
