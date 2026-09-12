"""Source-frozen exact certificate for the conditional second W coefficient."""
import argparse
from src.provenance import run_record
from proofs.m6_second_coefficient import produce


def main():
    if not __debug__: raise RuntimeError('Run without -O')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=['experiments/m6_coefficient_batch.py','proofs/m6_second_coefficient.py',
             'proofs/M6_SECOND_ORDER.md','proofs/m5_critical_pole.py',
             'proofs/m3_critical_integrals.py','proofs/m3_prudent_intervals.py',
             'results/m5-critical-v1/payload.json','src/provenance.py','requirements-lock.txt']
    command=f'.venv/bin/python -m experiments.m6_coefficient_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,{'digamma_shift':64,'critical_bins':4096},sources,produce))


if __name__=='__main__':
    main()
