"""Record reviewed real phase derivative component certificates."""
import argparse
from proofs.check_m3 import receipt
from proofs.m11_directed_phase_bounds import produce as directed
from proofs.m11_weight_phase_bounds import produce as weight
from proofs.m11_smooth_phase_bounds import produce as smooth
from src.provenance import run_record


def payload():
    if not __debug__:
        raise RuntimeError('Run without -O: interval and receipt guards required')
    receipt('m10-structural-v1')
    return {'status':'pass', 'directed':directed(), 'weight':weight(),
            'smooth':smooth(),
            'scope':'real phase derivative components; complete W index coverage open',
            'full_F_phase_sign':'NOT PROVED'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=[
        'experiments/m11_phase_batch.py',
        'proofs/m11_directed_phase_bounds.py','proofs/M11_DIRECTED_PHASE_BOUND.md',
        'proofs/m11_weight_phase_bounds.py','proofs/M11_WEIGHT_PHASE_BOUND.md',
        'proofs/m11_smooth_phase_bounds.py','proofs/M11_SMOOTH_PHASE_BOUND.md',
        'proofs/M10_BETA_REAL.md','proofs/m10_beta_real.py',
        'proofs/M10_DIRECTED_MONOTONICITY.md',
        'proofs/M10_POSITIVE_COMBINED_WEIGHT.md',
        'proofs/M10_REAL_PHASE_PRODUCT.md','proofs/M10_BARE_PHASE_DERIVATIVE.md',
        'proofs/M5_DIRECTED_LOG.md','proofs/M5_DIRECTED_REFINED.md',
        'proofs/m5_phase_domain.py','proofs/m7_finite_poles.py',
        'proofs/M6_EFFECTIVE_PRODUCT.md','proofs/check_m3.py',
        'results/m10-structural-v1/payload.json',
        'results/m10-structural-v1/metadata.json',
        'src/provenance.py','requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m11_phase_batch {args.experiment_id}'
    print(run_record(args.experiment_id, command,
                     {'N_min':32,'phase_band':['4/5','9/10'],
                      'post_crossing_prefix':'N+1<=n<=60N'}, sources, payload))


if __name__=='__main__':
    main()
