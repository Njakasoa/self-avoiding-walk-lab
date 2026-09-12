"""Verify M9 arithmetic and reviewed sources without claiming full W coverage."""
import hashlib
import json
from pathlib import Path
from proofs.check_m3 import receipt
from proofs.m9_linear_bounds import produce

ROOT=Path(__file__).resolve().parents[1]


def check():
    if not __debug__:
        raise RuntimeError('Run without -O: provenance receipt uses assertions')
    data=receipt('m9-linear-v1')
    if data!=produce():
        raise ArithmeticError('M9 arithmetic replay differs')
    assignments={
        'proofs/M9_PRODUCT_VARIATION.md':'proofs/M9_KERNEL_REVIEW.md',
        'proofs/M9_COMPLEX_KERNEL_LINEAR.md':'proofs/M9_KERNEL_REVIEW.md',
        'proofs/M9_LINEAR_MOMENT_RATE.md':'proofs/M9_MOMENT_REVIEW.md',
        'proofs/M9_UNIQUENESS_THRESHOLD.md':'proofs/M9_THRESHOLD_REVIEW.md',
        'proofs/M9_PHASE_RESIDUE_RATE.md':'proofs/M9_QUANTITATIVE_REVIEW.md',
        'proofs/m9_linear_bounds.py':'proofs/M9_QUANTITATIVE_REVIEW.md',
        'experiments/m9_linear_batch.py':'proofs/M9_QUANTITATIVE_REVIEW.md',
    }
    hashes={}
    for rel,review in assignments.items():
        digest=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
        if digest not in (ROOT/review).read_text():
            raise ArithmeticError('source not in corresponding review: '+rel)
        hashes[rel]=digest
    return {'status':'PASS: M9 linear-rate arithmetic and source provenance',
            'reviewed_source_hashes':hashes,
            'receipt':'m9-linear-v1', 'N_unique':'10^27',
            'moment_error':'10^21/N', 'phase_error_rate':'O(1/N)',
            'position_error_rate':'O(1/N^4)',
            'normalized_residue_error_rate':'O(log(N)^2/N)',
            'full_W_theory_goal':'OPEN: finite-to-asymptotic index coverage unproved'}


if __name__=='__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
