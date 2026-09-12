"""Verify the uniform noncancellation component and its reviewed source bytes."""
import hashlib
import json
import re
from pathlib import Path
from proofs.check_m3 import receipt

ROOT=Path(__file__).resolve().parents[1]


def check():
    if not __debug__:
        raise RuntimeError('Run without -O: receipt and interval guards required')
    from experiments.m12_noncancellation_batch import payload
    data=receipt('m12-noncancellation-v1')
    if data!=payload():
        raise ArithmeticError('M12 replay differs from receipt')
    body=(ROOT/'proofs/M12_NONCANCELLATION_REVIEW.md').read_text()
    table=dict((name.strip(),digest) for name,digest in re.findall(
        r'^\|\s*([^|]+?)\s*\|\s*([0-9a-f]{64})\s*\|',body,re.MULTILINE))
    hashes={}
    for name in ['proofs/M12_UNIFORM_NONCANCELLATION.md',
                 'proofs/m12_noncancellation_bounds.py',
                 'experiments/m12_noncancellation_batch.py']:
        digest=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        if table.get(name)!=digest:
            raise ArithmeticError('M12 source lacks matching review: '+name)
        hashes[name]=digest
    if data.get('numerator_upper_at_F_zero')!='-2' or data.get('existence_and_uniqueness')!='NOT PROVED':
        raise ArithmeticError('M12 scope changed')
    return {'status':'PASS: uniform real-sector W noncancellation component',
            'receipt':'m12-noncancellation-v1','reviewed_source_hashes':hashes,
            'domain':'N>=32, theta in[4/5,9/10]',
            'conclusion':'F=0 implies 1+P<-2',
            'full_W_coverage':'OPEN: zero existence and uniqueness not established for all indices'}


if __name__=='__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
