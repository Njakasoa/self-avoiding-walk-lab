"""Record exact allowances for the linear moment bound and W threshold."""
import argparse
from src.provenance import run_record
from proofs.m9_linear_bounds import produce


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=[
        'experiments/m9_linear_batch.py','proofs/m9_linear_bounds.py',
        'proofs/M9_PRODUCT_VARIATION.md','proofs/M9_COMPLEX_KERNEL_LINEAR.md',
        'proofs/M9_LINEAR_MOMENT_RATE.md','proofs/M9_UNIQUENESS_THRESHOLD.md',
        'proofs/M9_PHASE_RESIDUE_RATE.md','proofs/M8_EFFECTIVE_PHASE.md',
        'proofs/M8_RESUMMED_RESIDUE.md',
        'proofs/M8_DISCRETE_PRIMITIVE.md','proofs/M8_CHEBYSHEV_THRESHOLD.md',
        'proofs/M8_COMPLEX_DOMAIN.md','proofs/M5_EFFECTIVE_WEIGHTS.md',
        'proofs/M6_SHARP_KERNEL.md','proofs/M6_REAL_MOMENT_RATE.md',
        'proofs/M6_REAL_RATE_DOMAIN.md','proofs/M6_DIRECTED_CONSTANT.md',
        'proofs/M6_THRESHOLD.md','proofs/M7_UNIQUENESS_TRANSFER.md',
        'proofs/M7_COMPLEX_KERNEL_SECTOR.md','proofs/M7_COMPLEX_SCALARS.md',
        'proofs/M7_COMPLEX_PRODUCT_DOMINATION.md','proofs/M7_EFFECTIVE_DERIVATIVE.md',
        'proofs/M7_REAL_TO_DERIVATIVE.md','proofs/M5_DIRECTED_REFINED.md',
        'results/m5-critical-v1/payload.json','results/m7-effective-v1/payload.json',
        'src/provenance.py','requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m9_linear_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'moment_error':'1e21*e','N_unique':'10^27',
                      'scope':'asymptotic threshold improvement; finite coverage open'},
                     sources,produce))


if __name__=='__main__':
    main()
