"""Record source-frozen M8 threshold, phase and residue arithmetic."""
import argparse
from src.provenance import run_record
from proofs.m8_chebyshev_threshold import produce as threshold
from proofs.m8_residue_coefficients import produce as coefficients
from proofs.m8_algebra import produce as algebra


def payload():
    if not __debug__:
        raise RuntimeError('Run without -O: residue interval engine uses assertions')
    return {'status':'pass', 'threshold_phase_residue_bounds':threshold(),
            'residue_coefficients':coefficients(), 'algebra':algebra(),
            'scope':'analytic research advance; full W coverage goal remains open'}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=[
        'experiments/m8_analytic_batch.py','proofs/m8_chebyshev_threshold.py',
        'proofs/m8_residue_coefficients.py','proofs/m8_algebra.py',
        'proofs/M8_COMPLEX_DOMAIN.md','proofs/M8_CHEBYSHEV_THRESHOLD.md',
        'proofs/M8_EFFECTIVE_PHASE.md','proofs/M8_RESUMMED_RESIDUE.md',
        'proofs/M8_RESIDUE_EXPANSION.md','proofs/M8_DISCRETE_PRIMITIVE.md',
        'proofs/m3_prudent_intervals.py','proofs/m3_critical_integrals.py',
        'proofs/m5_critical_pole.py','proofs/M5_W_QUANTITATIVE.md',
        'proofs/M5_MOMENT_RATE.md','proofs/M5_DIRECTED_REFINED.md',
        'proofs/M6_REAL_MOMENT_RATE.md','proofs/M6_REAL_RATE_DOMAIN.md',
        'proofs/M6_SHARP_KERNEL.md','proofs/M6_DIRECTED_CONSTANT.md',
        'proofs/M6_RESUMMED_PHASE.md','proofs/M6_THRESHOLD.md',
        'proofs/M7_COMPLEX_SCALARS.md','proofs/M7_COMPLEX_KERNEL_SECTOR.md',
        'proofs/M7_COMPLEX_PRODUCT_DOMINATION.md','proofs/M7_EFFECTIVE_DERIVATIVE.md',
        'proofs/M7_REAL_TO_DERIVATIVE.md','proofs/M7_UNIQUENESS_TRANSFER.md',
        'results/m5-critical-v1/payload.json','results/m7-effective-v1/payload.json',
        'src/provenance.py','requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m8_analytic_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'N_unique':'10^57','chebyshev_degree':92,'rho':'22/15'},
                     sources,payload))


if __name__=='__main__':
    main()
