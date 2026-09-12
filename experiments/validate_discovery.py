"""Verify frozen scientific receipts and the already executed full-suite evidence."""
import hashlib,json,subprocess,sys
from pathlib import Path
from src.provenance import run_record
ROOT=Path(__file__).resolve().parents[1]
FOLDERS=['e1-compression-v1','e2-spans-v1','e3-weights-v1','m2-variants-v1',
         'm2-variants-v2','discovery-findings-v1','linegraph-candidate-v1']

def produce():
    check=subprocess.run([sys.executable,'proofs/check_discovery.py',*[f'results/{f}' for f in FOLDERS]],
                         cwd=ROOT,capture_output=True,text=True,check=True)
    evidence=json.loads((ROOT/'results/discovery-tests.json').read_text())
    assert evidence['exit_code']==0 and evidence['test_count']==49
    for rel,h in evidence['input_hashes'].items():
        frozen=subprocess.check_output(['git','show',f"{evidence['source_commit']}:{rel}"],cwd=ROOT)
        assert hashlib.sha256(frozen).hexdigest()==h
        assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==h,'tested source changed'
    candidate=json.loads((ROOT/'results/linegraph-candidate-v1/payload.json').read_text())
    assert candidate['prediction']['actual_q12']==candidate['prediction']['predicted_q12']==958
    report=ROOT/'results/linegraph-independent-report.md'
    assert hashlib.sha256(report.read_bytes()).hexdigest()==candidate['provenance']['report_sha256']
    for row in candidate['quotient_checks']:
        assert row['isomorphism']['isomorphic']==(row['memory']%2==1)
    return {'frozen_experiments':FOLDERS,'checker_stdout':check.stdout,
            'test_evidence':evidence,'tested_source_hashes_match_current':True,
            'independent_prediction_and_report_verified':True,
            'scope':'E1/E2/E3/M2 validated; no scientific novelty or publication asserted'}

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'discovery-validation-v1'
    paths=['experiments/validate_discovery.py','src/provenance.py','proofs/check_discovery.py',
           'results/discovery-tests.json','results/linegraph-independent-report.md',
           'results/discovery-astra-review.md','DISCOVERY_REPORT.md','DISCOVERY_ENGINE.md',
           'CLAIM_SELECTION.md','claims/CLAIM-0003.md','claims/CLAIM-0004.md',
           'references/LINEGRAPH_PRIOR_AUDIT.md','environment/NEXT_GOAL_BRIEF.md']
    paths += [f'results/{f}/{name}.json' for f in FOLDERS for name in ['payload','metadata']]
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/validate_discovery.py {eid}',{},paths,produce))
