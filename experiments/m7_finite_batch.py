"""Freeze and record exact finite W pole brackets at already observed indices."""
import argparse
from src.provenance import run_record
from proofs.m7_finite_poles import produce

def main():
    if not __debug__:
        raise RuntimeError('Run without -O')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    indices=[32,64,128,256,512,1024]
    sources=[
        'experiments/m7_finite_batch.py','proofs/m7_finite_poles.py',
        'proofs/M7_FINITE_TAIL.md','proofs/M3_NON_DFINITE_CANDIDATE.md',
        'proofs/W_NON_DFINITE.md','results/m5-phase-v1/payload.json',
        'results/m5-phase-holdout-v1/payload.json',
        'results/m6-phase-holdout-v1/payload.json',
        'src/provenance.py','requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m7_finite_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'indices':indices,'bits':384,'scope':'finite existence and noncancellation'},
                     sources,lambda:produce(indices)))

if __name__=='__main__':
    main()
