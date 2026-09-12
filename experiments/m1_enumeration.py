"""Freeze-backed exact counts, timings and two transfer-state representations."""
import json,subprocess,sys,tempfile,time
from pathlib import Path
from src.reference_enumerator import counts,rectangle_counts
from src.transfer_matrix import transfer_counts
from src.connectivity_tm import connectivity_counts
from src.provenance import run_record

ROOT=Path(__file__).resolve().parents[1]

def produce():
    expected={int(n):int(v) for line in (ROOT/'data/A001411.txt').read_text().splitlines()
              if line.strip() and not line.startswith('#') for n,v in [line.split()]}
    started=time.perf_counter();ref=counts(14);ref_seconds=time.perf_counter()-started
    assert all(ref[n]==expected[n] for n in range(len(ref)))
    with tempfile.TemporaryDirectory(prefix='saw-m1-') as td:
        binary=Path(td)/'saw_enum';flags=['-std=c++20','-O3','-DNDEBUG']
        subprocess.run(['g++',*flags,str(ROOT/'src/optimized_enumerator.cpp'),'-o',str(binary)],check=True)
        started=time.perf_counter();common=json.loads(subprocess.check_output([str(binary),'--json','14']));common_seconds=time.perf_counter()-started
        assert common==ref
        started=time.perf_counter();cpp=json.loads(subprocess.check_output([str(binary),'--json','20']));cpp_seconds=time.perf_counter()-started
        assert all(cpp[n]==expected[n] for n in range(len(cpp)))
    boxes=[]
    for w,h in [(1,1),(1,5),(2,2),(2,3),(3,2),(3,3),(3,4)]:
        n=w*h
        started=time.perf_counter();dfs=rectangle_counts(w,h,n);dfs_seconds=time.perf_counter()-started
        started=time.perf_counter();occupation=transfer_counts(w,h,n);occupation_seconds=time.perf_counter()-started
        started=time.perf_counter();connectivity=connectivity_counts(w,h,n);connectivity_seconds=time.perf_counter()-started
        assert dfs==occupation==connectivity['counts']
        boxes.append({'width':w,'height':h,'max_n':n,'counts':dfs,'dfs_seconds':dfs_seconds,
                      'occupation_seconds':occupation_seconds,'connectivity_seconds':connectivity_seconds,
                      'connectivity_peak_states':connectivity['peak_states']})
    return {'classification':'EXACT INTEGER','reference_max_n':14,'reference_counts':ref,
            'reference_seconds':ref_seconds,'cpp_common_n14_seconds':common_seconds,
            'cpp_max_n':20,'cpp_counts':cpp,'cpp_seconds':cpp_seconds,'compiler_flags':flags,
            'finite_boxes':boxes}

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'm1-enumeration-v1'
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/m1_enumeration.py {eid}',
       {'reference_n':14,'optimized_n':20},
       ['src/reference_enumerator.py','src/optimized_enumerator.cpp','src/transfer_matrix.py',
        'src/connectivity_tm.py','src/provenance.py','experiments/m1_enumeration.py',
        'data/A001411.txt','NORMALIZATION.md','proofs/TRANSFER_MATRIX.md',
        'proofs/CONNECTIVITY_TM.md','requirements-lock.txt'],produce))
