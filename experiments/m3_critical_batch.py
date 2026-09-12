"""Source-frozen records for the non-D-finiteness candidate and falsifiers."""
import argparse
from src.provenance import run_record


def run(kind, run_id):
    sources=['experiments/m3_critical_batch.py','src/provenance.py']
    if kind=='identities':
        from experiments.m3_moment_identities import produce as root_checks
        from experiments.m3_coboundary_probe import exact_checks
        def producer():return {'root':root_checks(),'independent':exact_checks()}
        sources+=['experiments/m3_moment_identities.py','experiments/m3_coboundary_probe.py']
        params={'arithmetic':'exact symbolic'}
    elif kind=='integrals':
        from proofs.m3_critical_integrals import produce as producer
        sources+=['proofs/m3_critical_integrals.py','proofs/m3_prudent_intervals.py',
                  'proofs/M3_NON_DFINITE_CANDIDATE.md','proofs/M3_CRITICAL_PRODUCT.md',
                  'papers/bacher-beaton-2014.pdf','requirements-lock.txt']
        params={'bins':2048,'power_bits':16,'interval_bits':384}
    elif kind=='phase':
        from experiments.m3_phase_probe import produce as producer
        sources+=['experiments/m3_phase_probe.py','experiments/m3_prudent_singularity_probe.py',
                  'requirements-lock.txt']
        params={'N':[8,16,32],'theta':['0.30','0.35'],'terms':[3200,6400]}
    elif kind=='asymptotic':
        from experiments.m3_prudent_asymptotic_probe import run as producer
        sources+=['experiments/m3_prudent_asymptotic_probe.py',
                  'experiments/m3_prudent_singularity_probe.py','requirements-lock.txt']
        params={'indices':[8,16,32],'terms':[400,800,1600,3200],'dps':100,'pole_dps':120,'max_seconds':300}
    else:raise ValueError(kind)
    return run_record(run_id,f'PYTHONPATH=. .venv/bin/python experiments/m3_critical_batch.py {kind} --run-id {run_id}',params,sources,producer)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('kind',choices=['identities','integrals','phase','asymptotic'])
    p.add_argument('--run-id',required=True)
    args=p.parse_args();print(run(args.kind,args.run_id))
