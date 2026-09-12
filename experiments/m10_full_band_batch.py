"""Record source-frozen full-band N=32 W uniqueness certification."""
import argparse
from proofs.check_m3 import receipt
from proofs.m10_full_band import produce
from src.provenance import run_record


def payload():
    if not __debug__:
        raise RuntimeError('Run without -O: inherited interval/receipt guards required')
    receipt('m7-finite-v1')
    return produce()


def main():
    if not __debug__:
        raise RuntimeError('Run without -O')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=[
        'experiments/m10_full_band_batch.py','proofs/m10_full_band.py',
        'proofs/M10_FULL_BAND.md','proofs/m8_finite_derivatives.py',
        'proofs/M8_FINITE_DERIVATIVES.md','proofs/m7_finite_poles.py',
        'proofs/M7_FINITE_TAIL.md','proofs/m5_phase_domain.py',
        'proofs/M5_DIRECTED_REFINED.md','proofs/check_m3.py',
        'proofs/W_NON_DFINITE.md','results/m7-finite-v1/payload.json',
        'results/m7-finite-v1/metadata.json','src/provenance.py',
        'requirements-lock.txt',
    ]
    command=f'.venv/bin/python -m experiments.m10_full_band_batch {args.experiment_id}'
    print(run_record(args.experiment_id,command,
                     {'index':32,'phase_band':['4/5','9/10'],
                      'cells':128,'bits':384,'scope':'one complete N=32 phase band'},
                     sources,payload))


if __name__=='__main__':
    main()
