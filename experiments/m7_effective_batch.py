"""Record exact arithmetic supporting the separately reviewed M7 theorem."""
import argparse
from src.provenance import run_record
from proofs.m7_complex_boxes import produce as complex_boxes
from proofs.m7_uniqueness_transfer import produce as transfer


def payload():
    return {
        'status': 'pass',
        'scope': 'arithmetic ledger; analytic proof and review are separate inputs',
        'N_unique': '10^120',
        'complex_boxes': complex_boxes(),
        'uniqueness_transfer': transfer(),
    }


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited interval checks use assertions')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args = parser.parse_args()
    sources = [
        'experiments/m7_effective_batch.py', 'proofs/m7_complex_boxes.py',
        'proofs/m7_uniqueness_transfer.py', 'proofs/m3_prudent_intervals.py',
        'proofs/m3_critical_integrals.py', 'proofs/M7_EFFECTIVE_DERIVATIVE.md',
        'proofs/M7_COMPLEX_SCALARS.md', 'proofs/M7_COMPLEX_KERNEL_SECTOR.md',
        'proofs/M7_COMPLEX_PRODUCT_DOMINATION.md', 'proofs/M7_REAL_TO_DERIVATIVE.md',
        'proofs/M7_UNIQUENESS_TRANSFER.md', 'proofs/M6_SHARP_KERNEL.md',
        'proofs/M6_REAL_MOMENT_RATE.md', 'proofs/M6_REAL_RATE_DOMAIN.md',
        'proofs/M6_EFFECTIVE_PRODUCT.md', 'proofs/M6_THRESHOLD.md',
        'proofs/M5_EFFECTIVE_KERNEL.md', 'proofs/M5_DIRECTED_REFINED.md',
        'proofs/M5_PHASE_DOMAIN.md', 'results/m5-critical-v1/payload.json',
        'results/m6-threshold-v1/payload.json',
        'src/provenance.py', 'requirements-lock.txt',
    ]
    command = f'.venv/bin/python -m experiments.m7_effective_batch {args.experiment_id}'
    print(run_record(args.experiment_id, command,
                     {'N_unique': '10^120', 'derivative_error_bound': '9/1000'},
                     sources, payload))


if __name__ == '__main__':
    main()
