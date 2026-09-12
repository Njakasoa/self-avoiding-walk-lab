"""Record the all-N>=32 scalar and product-component lemmas."""
import argparse
from proofs.m10_beta_real import produce as beta
from proofs.m10_structural_bounds import produce as structural
from proofs.m10_directed_monotone import produce as directed
from proofs.check_m3 import receipt
from src.provenance import run_record


def payload():
    if not __debug__:
        raise RuntimeError('Run without -O: beta interval engine uses assertions')
    receipt('m6-coefficient-v1')
    return {'status':'pass','real_beta_derivatives':beta(),
            'weight_and_product':structural(),
            'directed_monotonicity':directed(),
            'scope':'component lemmas only; full denominator phase sign and index coverage open'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=[
        'experiments/m10_structural_batch.py','proofs/m10_beta_real.py',
        'proofs/m10_structural_bounds.py','proofs/M10_BETA_REAL.md',
        'proofs/m10_directed_monotone.py','proofs/M10_DIRECTED_MONOTONICITY.md',
        'proofs/M10_POSITIVE_COMBINED_WEIGHT.md','proofs/M10_REAL_PHASE_PRODUCT.md',
        'proofs/M10_BARE_PHASE_DERIVATIVE.md','proofs/m7_finite_poles.py',
        'proofs/m5_phase_domain.py','proofs/M5_DIRECTED_REFINED.md',
        'proofs/M5_DIRECTED_LOG.md',
        'proofs/M6_DIRECTED_CONSTANT.md','proofs/M6_EFFECTIVE_PRODUCT.md',
        'proofs/M6_SHARP_KERNEL.md','proofs/M7_COMPLEX_KERNEL_SECTOR.md',
        'proofs/check_m3.py','results/m6-coefficient-v1/payload.json',
        'results/m6-coefficient-v1/metadata.json',
        'src/provenance.py','requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m10_structural_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'N_min':32,'bare_prefix':'n<=60N',
                      'scope':'scalar and positive-weight components only'},
                     sources,payload))


if __name__=='__main__':
    main()
