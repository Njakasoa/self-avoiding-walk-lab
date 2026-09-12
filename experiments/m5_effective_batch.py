"""Record the final exact arithmetic of the effective M5 W threshold."""
import argparse
from src.provenance import run_record
from proofs.m5_effective_threshold import produce
from proofs.m5_weight_boxes import produce as weight_boxes


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=['experiments/m5_effective_batch.py','proofs/m5_effective_threshold.py',
             'proofs/m5_weight_boxes.py',
             'src/provenance.py','requirements-lock.txt',
             'proofs/M5_EFFECTIVE_KERNEL.md','proofs/M5_EFFECTIVE_GAMMA.md',
             'proofs/M5_EFFECTIVE_WEIGHTS.md','proofs/M5_EFFECTIVE_THRESHOLD.md',
             'results/m5-critical-v1/payload.json']
    command=f'.venv/bin/python -m experiments.m5_effective_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'N0_expression':'2^(10^120)','scope':'W existence and noncancellation'},
                     sources,lambda: {'weight_boxes':weight_boxes(),
                                      'threshold_arithmetic':produce(),
                                      'status':'pass'}))


if __name__=='__main__':
    main()
