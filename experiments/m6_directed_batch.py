"""Source-frozen numerical replay of the M6 directed constant diagnostics."""
import argparse
import contextlib
import io
from src.provenance import run_record
from experiments.m6_directed_constant_check import main as check


def produce():
    out=io.StringIO()
    with contextlib.redirect_stdout(out): check()
    return {'classification':'NUMERICAL DIAGNOSTIC ONLY; analytic error proof is separate',
            'status':'pass','stdout':out.getvalue()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=['experiments/m6_directed_batch.py','experiments/m6_directed_constant_check.py',
             'proofs/M6_DIRECTED_CONSTANT.md','src/provenance.py','requirements-lock.txt']
    command=f'.venv/bin/python -m experiments.m6_directed_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
        {'epsilon_values':['.01','.005','.002','.001','.0005'],'dps':60,'tail_x':50},
        sources,produce))


if __name__=='__main__':
    main()
