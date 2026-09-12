"""Canonical run, e.g. PYTHONPATH=. .venv/bin/python experiments/m1_certificates.py m1-certificates-v1."""
import sys
from src.automaton import memory_automaton,certificate,check_certificate
from src.bridges import enumerate_bridges,renewal_inverse,lower_certificate
from src.provenance import run_record

def produce():
    automata=[]
    for m in range(1,9):
        states,rows=memory_automaton(m)
        cert=certificate(rows,120)
        assert check_certificate(rows,cert)
        automata.append({'memory':m,'state_count':len(states),'states':states,
                         'rows':rows,'certificate':cert})
    bridges=enumerate_bridges(12)
    assert bridges['irreducibles']==renewal_inverse(bridges['bridges'])
    bridges['certificate']=lower_certificate(bridges['irreducibles'])
    return {'automata':automata,'bridges':bridges}

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'm1-certificates-v1'
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/m1_certificates.py {eid}',
          {'memories':list(range(1,9)),'bridge_max_n':12,'power_iterations':120},
          ['src/automaton.py','src/bridges.py','src/provenance.py','experiments/m1_certificates.py',
           'NORMALIZATION.md','proofs/FINITE_MEMORY.md','proofs/BRIDGE_RENEWAL.md','requirements-lock.txt'],produce))
