"""Verify the M8 analytic milestone; this does not close the full W goal."""
import hashlib
import json
from pathlib import Path
from proofs.check_m3 import receipt
from experiments.m8_analytic_batch import payload

ROOT=Path(__file__).resolve().parents[1]


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited receipts and intervals use assertions')
    data=receipt('m8-analytic-v1')
    if data != payload():
        raise ArithmeticError('M8 analytic payload replay differs')
    sources=[
        'M8_COMPLEX_DOMAIN.md','M8_CHEBYSHEV_THRESHOLD.md',
        'M8_EFFECTIVE_PHASE.md','M8_RESUMMED_RESIDUE.md',
        'M8_RESIDUE_EXPANSION.md','M8_DISCRETE_PRIMITIVE.md',
        'm8_chebyshev_threshold.py','m8_residue_coefficients.py','m8_algebra.py',
    ]
    report=(ROOT/'proofs/M8_ANALYTIC_REVIEW.md').read_text()
    hashes={}
    for name in sources:
        path='proofs/'+name
        digest=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
        if digest not in report:
            raise ArithmeticError('unreviewed source '+path)
        hashes[path]=digest
    bounds=data['threshold_phase_residue_bounds']
    if bounds['N_unique']!='10^57' or bounds['joint_derivative_allowance']!='1033/1000':
        raise ArithmeticError('wrong threshold scope')
    coefficients=data['residue_coefficients']
    for key in ['N_cubed_residue_C0','N_cubed_residue_C1_log']:
        if int(coefficients[key]['exact']['upper_numerator'])>=0:
            raise ArithmeticError('residue coefficient sign')
    # All previously accepted M7 source receipts remain verifiable as well.
    receipt('m7-effective-v1')
    receipt('m7-finite-v1')
    return {
        'status':'PASS: M8 analytic milestone provenance and arithmetic',
        'receipt':'m8-analytic-v1','reviewed_source_hashes':hashes,
        'N_unique':'10^57','first_log_residue_coefficient_negative':True,
        'full_W_theory_goal':'OPEN: accessible-to-asymptotic coverage not established',
        'discrete_primitive_scope':'identity only; sharper moment rate unproved',
    }


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
