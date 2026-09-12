"""E1: exact memory3..11 comparison; isolated cases enforce total wall limits."""
import json,subprocess,sys,time
from pathlib import Path
from fractions import Fraction
from src.discovery_engine import memory_case
from src.provenance import run_record
ROOT=Path(__file__).resolve().parents[1]

def produce():
    cases=[]
    for memory in range(3,12):
        for symmetry,representation in [('none','memory'),('auto','memory'),('auto','equitable')]:
            config={'kind':'memory','memory':memory,'symmetry':symmetry,
                    'state_representation':representation,'iterations':120,
                    'max_states':100_000,'max_seconds':290}
            started=time.monotonic()
            try:
                child=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--case',json.dumps(config)],
                                     cwd=ROOT,capture_output=True,text=True,timeout=300,check=True)
                result=json.loads(child.stdout)
            except subprocess.TimeoutExpired:
                result={'config':config,'status':'RESOURCE_LIMIT','reason':'300-second complete-case cap',
                        'certificate':None,'runtime_seconds':time.monotonic()-started}
            cases.append(result)
            print(f"E1 m={memory} {symmetry}/{representation}: {result['status']} states={result.get('state_count')}",file=sys.stderr,flush=True)
    comparisons=[]
    for m in range(3,12):
        group=[r for r in cases if r['config']['memory']==m and r['status']=='CERTIFIED']
        uppers={Fraction(r['certificate']['upper']) for r in group}
        assert len(uppers)==1, 'exact same continuation certificate should survive these quotients'
        base=next(r for r in group if r['config']['state_representation']=='memory' and r['config']['symmetry']=='auto')
        compressed=next(r for r in group if r['config']['state_representation']=='equitable')
        comparisons.append({'memory':m,'orbit_states':base['state_count'],'equitable_states':compressed['state_count'],
                            'compression_ratio':str(Fraction(base['state_count'],compressed['state_count'])),
                            'upper':base['certificate']['upper'],'upper_display':base['certificate']['upper_decimal_display'],
                            'exact_bound_preserved':True})
    winner=max(comparisons,key=lambda c:Fraction(c['compression_ratio']))
    best=min(comparisons,key=lambda c:Fraction(c['upper']))
    # Observations selected by the computed measurements, not hard-coded examples.
    observations={'largest_orbit_to_equitable_reduction':winner,
                  'best_certified_bound_in_sweep':best,
                  'strict_reduction_memories':[r['memory'] for r in comparisons if r['equitable_states']<r['orbit_states']],
                  'resource_limited_configs':[r['config'] for r in cases if r['status']!='CERTIFIED'],
                  'novelty':'UNASSESSED; ordinary equitable compression is known, no novel theorem claimed',
                  'limitation':'post-construction reduction does not eliminate original graph build memory'}
    certified=[r for r in cases if r['status']=='CERTIFIED']
    budgets=[]
    for budget in [10,50,250,1000,10000,100000]:
        for cost in ['state_count','original_state_count']:
            contenders=[r for r in certified if r[cost]<=budget]
            if not contenders:continue
            pick=min(contenders,key=lambda r:(Fraction(r['certificate']['upper']),r[cost],r['runtime_seconds']))
            budgets.append({'budget':budget,'cost_dimension':cost,'config':pick['config'],
                            'upper':pick['certificate']['upper'],'cost':pick[cost],
                            'meaning':'certificate matrix' if cost=='state_count' else 'graph constructed before refinement'})
    observations['best_upper_at_state_budgets']=budgets
    observations['decreasing_equitable_size_with_more_memory']=[
        {'from_memory':a['memory'],'to_memory':b['memory'],
         'from_states':a['equitable_states'],'to_states':b['equitable_states'],
         'interpretation':'finite computed observation; no general monotonicity claim'}
        for a,b in zip(comparisons,comparisons[1:]) if b['equitable_states']<a['equitable_states']]
    return {'cases':cases,'comparisons':comparisons,'automatically_selected_observations':observations}

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--case':
        print(json.dumps(memory_case(json.loads(sys.argv[2])),sort_keys=True));raise SystemExit
    eid=sys.argv[1] if len(sys.argv)>1 else 'e1-compression-v1'
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/e1_compression.py {eid}',
       {'memories':list(range(3,12)),'max_states':100000,'wall_seconds_per_case':300},
       ['src/discovery_memory.py','src/discovery_engine.py','src/equitable.py','src/provenance.py',
        'experiments/e1_compression.py','proofs/DISCOVERY_MEMORY.md','proofs/EQUITABLE_COMPRESSION.md',
        'NORMALIZATION.md','requirements-lock.txt','environment/NEXT_GOAL_BRIEF.md'],produce))
