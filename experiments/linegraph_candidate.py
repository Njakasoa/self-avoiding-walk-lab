"""Freeze and execute the separate candidate verifier with its own receipt."""
import json,subprocess,sys
from pathlib import Path
from src.provenance import run_record
ROOT=Path(__file__).resolve().parents[1]

def produce():
    child=subprocess.run([sys.executable,'proofs/check_linegraph_candidate.py','--json'],cwd=ROOT,
                         capture_output=True,text=True,timeout=300,check=True)
    result=json.loads(child.stdout)
    assert result['prediction']['prediction_matches']
    for c in result['quotient_checks']:
        assert c['isomorphism']['isomorphic']==(c['memory']%2==1)
    assert all(c['equal']==(c['memory']%2==1) for c in result['direct_linegraph_checks'])
    assert all(not c['equal'] for c in result['triangular_control'])
    return result

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'linegraph-candidate-v1'
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/linegraph_candidate.py {eid}',
        {'memories':[9,10,11,12],'predicted_q12':958,'max_seconds':300},
        ['experiments/linegraph_candidate.py','proofs/check_linegraph_candidate.py','src/provenance.py',
         'NORMALIZATION.md','proofs/FINITE_MEMORY.md','proofs/EQUITABLE_COMPRESSION.md',
         'proofs/ODD_EVEN_LINEGRAPH.md','environment/NEXT_GOAL_BRIEF.md','requirements-lock.txt'],produce))
