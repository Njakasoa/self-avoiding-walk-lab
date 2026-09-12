"""Source-frozen exact ledger for the improved M6 W existence threshold."""
import argparse
import io
from contextlib import redirect_stdout
from src.provenance import run_record
from proofs.m6_threshold import produce
from proofs.m6_sharp_kernel_boxes import main as sharp_boxes

def payload():
    stream=io.StringIO()
    with redirect_stdout(stream):
        sharp_boxes()
    return {'threshold_arithmetic':produce(),'sharp_box_arithmetic_stdout':stream.getvalue(),
            'status':'pass','scope':'analytic proof and independent review are separate inputs'}

def main():
    if not __debug__:
        raise RuntimeError('Run without -O')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=[
        'experiments/m6_threshold_batch.py','proofs/m6_threshold.py',
        'proofs/m6_sharp_kernel_boxes.py',
        'proofs/m6_second_coefficient.py','proofs/m3_prudent_intervals.py',
        'proofs/m3_critical_integrals.py','proofs/m5_critical_pole.py',
        'proofs/M6_THRESHOLD.md','proofs/M6_SHARP_KERNEL.md',
        'proofs/M6_REAL_MOMENT_RATE.md','proofs/M6_EFFECTIVE_PRODUCT.md',
        'proofs/M6_REAL_RATE_DOMAIN.md',
        'proofs/M6_DIRECTED_CONSTANT.md','proofs/M5_EFFECTIVE_WEIGHTS.md',
        'proofs/M5_EFFECTIVE_GAMMA.md','proofs/M5_PHASE_DOMAIN.md',
        'proofs/M5_EFFECTIVE_KERNEL.md','proofs/M5_DIRECTED_LOG.md',
        'proofs/m5_weight_boxes.py',
        'results/m5-critical-v1/payload.json','src/provenance.py',
        'requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m6_threshold_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'N0':'10^46','B':'10^12','scope':'existence and noncancellation'},
                     sources,payload))

if __name__=='__main__':
    main()
