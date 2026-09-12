"""Canonical final test and archived-experiment validation receipt."""
import json,subprocess,sys
from pathlib import Path
from src.provenance import run_record
ROOT=Path(__file__).resolve().parents[1]

def produce():
    test=subprocess.run([sys.executable,'-m','pytest','-q'],cwd=ROOT,capture_output=True,text=True,check=True)
    check=subprocess.run([sys.executable,'proofs/check_certificates.py','results/m1-certificates-v2'],cwd=ROOT,capture_output=True,text=True,check=True)
    a=json.loads((ROOT/'results/m1-certificates-v1/payload.json').read_text())
    b=json.loads((ROOT/'results/m1-certificates-v2/payload.json').read_text());assert a==b
    import hashlib
    folders=['m1-certificates-v1','m1-certificates-v2','m1-enumeration-v1','honeycomb-control-v1','m1-optimized-modes-v1']
    verified=0
    for folder in folders:
        path=ROOT/'results'/folder;meta=json.loads((path/'metadata.json').read_text())
        for rel,h in meta['input_hashes'].items():
            content=subprocess.check_output(['git','show',f"{meta['git_commit']}:{rel}"],cwd=ROOT)
            assert hashlib.sha256(content).hexdigest()==h;verified+=1
        for rel,h in meta['output_hashes'].items():assert hashlib.sha256((path/rel).read_bytes()).hexdigest()==h
    return {'pytest_stdout':test.stdout,'pytest_stderr':test.stderr,'checker_stdout':check.stdout,
            'scientific_v1_v2_identical':True,'verified_source_receipt_entries':verified,'folders':folders,
            'independent_review':'results/astra-review.md','tester_report':'results/tester-report.md'}

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'm1-validation-v2'
    paths=[str(p.relative_to(ROOT)) for folder in ['src','tests','experiments','proofs'] for p in (ROOT/folder).glob('*') if p.suffix in ['.py','.cpp','.md']]
    paths+=['requirements-lock.txt','data/A001411.txt','results/astra-review.md','results/tester-report.md']
    for folder in ['m1-certificates-v1','m1-certificates-v2','m1-enumeration-v1','honeycomb-control-v1','m1-optimized-modes-v1']:
        paths += [f'results/{folder}/metadata.json',f'results/{folder}/payload.json']
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/validate_m1.py {eid}',{},paths,produce))
