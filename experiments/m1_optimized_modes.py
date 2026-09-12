"""Exact packed-bitset and canonical memo enumeration comparison for brief8.2."""
import json,subprocess,sys,tempfile,time
from pathlib import Path
from src.reference_enumerator import counts
from src.provenance import run_record
ROOT=Path(__file__).resolve().parents[1]

def produce():
    external={int(n):int(v) for line in (ROOT/'data/A001411.txt').read_text().splitlines()
              if line.strip() and not line.startswith('#') for n,v in [line.split()]}
    started=time.perf_counter();reference=counts(12);reference_seconds=time.perf_counter()-started
    runs=[]
    with tempfile.TemporaryDirectory(prefix='saw-modes-') as td:
        binary=Path(td)/'saw_enum';flags=['-std=c++20','-O3','-DNDEBUG']
        subprocess.run(['g++',*flags,str(ROOT/'src/optimized_enumerator.cpp'),'-o',str(binary)],check=True)
        for mode,n in [('direct',0),('memo-small',0),('direct',1),('memo-small',1),
                       ('direct',12),('memo-small',12),('direct',20)]:
            args=[str(binary),'--json']+(['--memo-small'] if mode=='memo-small' else [])+[str(n)]
            started=time.perf_counter()
            rss_path=Path(td)/f'{mode}-{n}-rss.txt'
            completed=subprocess.run(['/usr/bin/time','-f','%M','-o',str(rss_path),*args],
                                     check=True,capture_output=True,text=True)
            elapsed=time.perf_counter()-started;actual=json.loads(completed.stdout)
            assert actual==[external[k] for k in range(n+1)]
            if n==12:assert actual==reference
            runs.append({'mode':mode,'max_n':n,'counts':actual,'seconds':elapsed,
                         'peak_rss_kib_child':int(rss_path.read_text().strip())})
    return {'classification':'EXACT INTEGER','reference_max_n':12,'reference_counts':reference,
            'reference_seconds':reference_seconds,'compiler_flags':flags,'runs':runs,
            'interpretation':'memo correctness is established by agreement; timing is one sample, not a confidence interval'}

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'm1-optimized-modes-v1'
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/m1_optimized_modes.py {eid}',
       {'reference_n':12,'memo_n':[0,1,12],'direct_n':[0,1,12,20]},
       ['src/reference_enumerator.py','src/optimized_enumerator.cpp','src/provenance.py',
        'experiments/m1_optimized_modes.py','data/A001411.txt','NORMALIZATION.md',
        'proofs/OPTIMIZED_ENUMERATOR.md','requirements-lock.txt'],produce))
