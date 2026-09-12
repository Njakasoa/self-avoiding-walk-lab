"""Record the uniform real-sector noncancellation scalar certificate."""
import argparse
from proofs.check_m3 import receipt
from proofs.m12_noncancellation_bounds import produce
from src.provenance import run_record


def payload():
    if not __debug__:
        raise RuntimeError('Run without -O: interval and receipt guards required')
    receipt('m10-structural-v1')
    return produce()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=[
        'experiments/m12_noncancellation_batch.py',
        'proofs/m12_noncancellation_bounds.py','proofs/M12_UNIFORM_NONCANCELLATION.md',
        'proofs/m7_finite_poles.py','proofs/m8_finite_derivatives.py',
        'proofs/M7_FINITE_TAIL.md','proofs/M10_BETA_REAL.md',
        'proofs/M10_POSITIVE_COMBINED_WEIGHT.md','proofs/M10_DIRECTED_MONOTONICITY.md',
        'proofs/M11_WEIGHT_PHASE_BOUND.md','proofs/M6_EFFECTIVE_PRODUCT.md',
        'proofs/M5_DIRECTED_LOG.md','proofs/check_m3.py',
        'results/m10-structural-v1/payload.json','results/m10-structural-v1/metadata.json',
        'src/provenance.py','requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m12_noncancellation_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'N_min':32,'phase_band':['4/5','9/10'],
                      'claim':'F=0 implies 1+P<-2; existence and uniqueness open'},
                     sources,payload))


if __name__=='__main__':
    main()
