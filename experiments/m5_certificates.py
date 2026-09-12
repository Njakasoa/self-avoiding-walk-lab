"""Source-frozen receipts for the first quantitative M5 lemmas."""
import argparse
from src.provenance import run_record


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: the interval engine requires assertions')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind',choices=['critical','phase-domain','directed-log'])
    parser.add_argument('experiment_id')
    args=parser.parse_args()
    sources=['experiments/m5_certificates.py','src/provenance.py','requirements-lock.txt',
             'proofs/W_NON_DFINITE.md','proofs/M5_MOMENT_RATE.md',
             'proofs/M5_DIRECTED_LOG.md','proofs/M5_PHASE_DOMAIN.md']
    if args.kind=='directed-log':
        from experiments.m5_directed_log_check import produce
        sources+=['experiments/m5_directed_log_check.py']
        params={'epsilon_values':['0.1','0.05','0.02','0.01','0.005','0.002'],
                'dps':80,'cutoff_factor':40}
    else:
        sources+=['proofs/m5_critical_pole.py','proofs/m3_critical_integrals.py',
                  'proofs/m3_prudent_intervals.py']
        if args.kind=='critical':
            from proofs.m5_critical_pole import produce
            params={'bins':4096,'power_bits':16}
        else:
            from proofs.m5_phase_domain import produce
            sources+=['proofs/m5_phase_domain.py']
            params={'epsilon_max':'1/100','N_phase_min':20,'N_directed_min':'2^108'}
    command=f'.venv/bin/python -m experiments.m5_certificates {args.kind} {args.experiment_id}'
    print(run_record(args.experiment_id,command,params,sources,produce))


if __name__=='__main__':
    main()
