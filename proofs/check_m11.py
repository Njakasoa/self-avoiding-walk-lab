"""Check reviewed M11 derivative components without asserting a full W theorem."""
import hashlib
import json
import re
from pathlib import Path
from proofs.check_m3 import receipt

ROOT=Path(__file__).resolve().parents[1]


def check():
    if not __debug__:
        raise RuntimeError('Run without -O: receipt and interval guards required')
    from experiments.m11_phase_batch import payload
    data=receipt('m11-phase-v1')
    if data!=payload():
        raise ArithmeticError('M11 component replay differs from frozen receipt')
    reviews={
        'proofs/M11_DIRECTED_PHASE_REVIEW.md':[
            'proofs/M11_DIRECTED_PHASE_BOUND.md','proofs/m11_directed_phase_bounds.py'],
        'proofs/M11_WEIGHT_PHASE_REVIEW.md':[
            'proofs/M11_WEIGHT_PHASE_BOUND.md','proofs/m11_weight_phase_bounds.py'],
        'proofs/M11_SMOOTH_PHASE_REVIEW.md':[
            'proofs/M11_SMOOTH_PHASE_BOUND.md','proofs/m11_smooth_phase_bounds.py'],
        'proofs/M11_WRAPPER_REVIEW.md':['experiments/m11_phase_batch.py'],
    }
    hashes={}
    for review,files in reviews.items():
        body=(ROOT/review).read_text()
        table=dict((name.strip(),digest) for name,digest in re.findall(
            r'^\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|',body,re.MULTILINE))
        for name in files:
            digest=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            if table.get(name)!=digest:
                raise ArithmeticError('M11 source lacks matching review: '+name)
            hashes[name]=digest
    if data.get('full_F_phase_sign')!='NOT PROVED':
        raise ArithmeticError('M11 scope marker missing')
    return {'status':'PASS: reviewed M11 phase derivative components',
            'receipt':'m11-phase-v1', 'reviewed_source_hashes':hashes,
            'N_min':32, 'phase_band':['4/5','9/10'],
            'post_crossing_terms':'N+1<=n<=60N',
            'full_F_phase_sign':'NOT PROVED',
            'full_W_coverage':'OPEN: pre-crossing, boundary, tail and index connection remain'}


if __name__=='__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
