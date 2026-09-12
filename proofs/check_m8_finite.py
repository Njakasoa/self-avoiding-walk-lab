"""Check finite M8 receipts and their precise six-bracket scope."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from proofs.check_m3 import receipt
from experiments.m8_finite_batch import combine, decode

ROOT = Path(__file__).resolve().parents[1]


def check():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited receipt assertions required')
    data = receipt('m8-finite-v1')
    old = receipt('m7-finite-v1')
    if data['indices'] != [32,64,128,256,512,1024]:
        raise ArithmeticError('wrong finite scope')
    if [r['index'] for r in data['rows']] != data['indices']:
        raise ArithmeticError('missing or duplicate finite row')
    if combine(json.loads(json.dumps(data)), old) != data:
        raise ArithmeticError('residue recomputation differs')
    reviewer = json.loads((ROOT/'results/m8-finite-review-N32.json').read_text())
    independent = reviewer['corrected_wrapper_replay']
    for rel, wanted in reviewer['final_review_snapshot']['input_sha256'].items():
        if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() != wanted:
            raise ArithmeticError('reviewed source differs: '+rel)
    if independent['result']['rows'][0] != data['rows'][0]:
        raise ArithmeticError('independent N32 replay differs')
    target = Fraction(1,10**18)
    scale = 2**384
    summary = []
    for row in data['rows']:
        for key in ['tail_P','tail_H','tail_P_derivative','tail_H_derivative']:
            tail = decode(row['tail'][key])
            if tail.lo < 0 or Fraction(tail.hi,scale) > target:
                raise ArithmeticError('prudent tail too large')
        for key in ['tail_value','tail_derivative']:
            tail = decode(row['directed'][key])
            if tail.lo < 0 or Fraction(tail.hi,scale) > target:
                raise ArithmeticError('directed tail too large')
        decode(row['F']['derivative']).negative('F derivative')
        decode(row['residue_in_t']).negative('residue')
        summary.append({'index':row['index'],
                        'N_cubed_residue':row['N_cubed_residue']})
    return {'status':'PASS: six finite narrow-bracket uniqueness and residue receipts',
            'receipt':'m8-finite-v1', 'independent_replay_index':32,
            'rows':summary,
            'analytic_review':'proofs/M8_FINITE_REVIEW.md',
            'full_W_theory_goal':'OPEN: full bands and intervening indices unproved'}


if __name__ == '__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
