"""Replay M6 receipts, exact arithmetic, reviewed hashes and held-out comparisons.

This integration audit checks provenance and arithmetic; independent reports
establish the analytic scope. It does not replace mathematical review.
"""
import hashlib
import json
from decimal import Decimal, localcontext
from pathlib import Path
from proofs.check_m3 import receipt

ROOT=Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited interval and receipt checks use assertions')
    names=['m6-coefficient-v1','m6-directed-v1','m6-phase-predictions-v1',
           'm6-threshold-v1','m6-phase-holdout-v1']
    data={name:receipt(name) for name in names}
    from proofs.m6_second_coefficient import produce as coefficients
    from experiments.m6_threshold_batch import payload as threshold
    from experiments.m6_phase_predictions import produce_calibration
    assert coefficients()==data['m6-coefficient-v1']
    assert threshold()==data['m6-threshold-v1']
    assert produce_calibration()==data['m6-phase-predictions-v1']
    reviewed={
        'proofs/M6_SECOND_ORDER.md':'proofs/M6_SECOND_ORDER_REVIEW.md',
        'proofs/m6_second_coefficient.py':'proofs/M6_COEFFICIENT_REVIEW.md',
        'proofs/M6_DIRECTED_CONSTANT.md':'proofs/M6_DIRECTED_REVIEW.md',
        'experiments/m6_directed_constant_check.py':'proofs/M6_DIRECTED_REVIEW.md',
        'proofs/M6_EFFECTIVE_PRODUCT.md':'proofs/M6_PRODUCT_RESUMMED_REVIEW.md',
        'proofs/M6_RESUMMED_PHASE.md':'proofs/M6_PRODUCT_RESUMMED_REVIEW.md',
        'proofs/M6_REAL_MOMENT_RATE.md':'proofs/M6_REAL_RATE_REVIEW.md',
        'proofs/M6_SHARP_KERNEL.md':'proofs/M6_SHARP_KERNEL_REVIEW.md',
        'proofs/m6_sharp_kernel_boxes.py':'proofs/M6_SHARP_KERNEL_REVIEW.md',
        'proofs/M6_THRESHOLD.md':'proofs/M6_THRESHOLD_REVIEW.md',
        'proofs/m6_threshold.py':'proofs/M6_THRESHOLD_REVIEW.md',
    }
    reviewed_hashes={}
    for source,report in reviewed.items():
        digest=sha(ROOT/source)
        assert digest in (ROOT/report).read_text(),(source,report)
        reviewed_hashes[source]=digest
    sharp_stdout=data['m6-threshold-v1']['sharp_box_arithmetic_stdout']
    assert hashlib.sha256(sharp_stdout.encode()).hexdigest() in (ROOT/'proofs/M6_SHARP_KERNEL_REVIEW.md').read_text()
    legacy={
        'proofs/W_NON_DFINITE.md':'351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a',
        'proofs/M3_NON_DFINITE_CANDIDATE.md':'e184726e834116e8eaf9d83926e571f40f4f2883eda1114b05c231872ec0a627',
        'publication/main.tex':'d020e1c1d58e08bc642e74d7da5a1f02df33eb42defcfd6053d1a7bf250fd0e0',
    }
    for source,digest in legacy.items():
        assert sha(ROOT/source)==digest,source
    from experiments.m6_phase_batch import _verify_protocol
    protocol,calibration,_=_verify_protocol('experiments/m6_phase_protocol.json')
    holdout=data['m6-phase-holdout-v1']
    assert holdout['validation_index']==1024 and holdout['refit'] is False
    assert '1024' not in calibration['observed']
    comparisons={}
    with localcontext() as ctx:
        ctx.prec=80
        actual=Decimal(holdout['row']['theta_N'])
        for model,record in holdout['comparisons'].items():
            prediction=Decimal(protocol['predictions'][model]['1024'])
            tolerance=Decimal(protocol['tolerances'][model])
            error=abs(actual-prediction)
            assert abs(error-Decimal(record['absolute_error']))<Decimal('1e-34')
            assert record['passed']==(error<=tolerance)
            comparisons[model]={'passed':record['passed'],'absolute_error':str(error)}
    return {'status':'PASS: provenance and integration arithmetic',
            'receipts':names,'reviewed_source_hashes':reviewed_hashes,
            'legacy_sources_unchanged':legacy,'heldout_comparisons':comparisons,
            'scope':'internal research draft; analytic review separate; threshold existence only'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
