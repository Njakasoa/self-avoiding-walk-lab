"""Target-preserving discovery across explicit supported parameter variants."""
import json,sys,subprocess
from pathlib import Path
from fractions import Fraction
from src.discovery_engine import run_case
from src.provenance import run_record
ROOT=Path(__file__).resolve().parents[1]

def produce():
    cases=[]
    families=[{'lattice':'square'}, {'lattice':'triangular'},
              {'lattice':'square','boundary':'strip','width':2},
              {'lattice':'square','boundary':'strip','width':3},
              {'lattice':'square','forbidden_words':[[0,0]]},
              {'lattice':'triangular','weights':['2','1','1','2','1','1']}]
    for family in families:
        for memory in [3,5]:
            for representation in ['memory','equitable']:
                config=dict(family,kind='memory',memory=memory,state_representation=representation,max_seconds=60)
                child=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--case',json.dumps(config)],
                                     cwd=ROOT,capture_output=True,text=True,timeout=60,check=True)
                cases.append(json.loads(child.stdout))
    # These controls are explicit invalid combinations, never silently ignored.
    mutants=[{'kind':'memory','memory':3,'weights':['2','1','2','1'],'symmetry':'d4'},
             {'kind':'memory','memory':3,'boundary':'torus'},
             {'kind':'memory','memory':3,'width':2},
             {'kind':'memory','memory':3,'lattice':'honeycomb'},
             {'kind':'bridges','max_n':8,'weights':[1,1,1,1]},
             {'kind':'memory','memory':3,'state_representation':'connectivity'},
             {'kind':'memory','memory':3,'max_span':2}]
    rejected=[]
    for config in mutants:
        try:run_case(config)
        except ValueError as error:rejected.append({'config':config,'reason':str(error)})
        else:raise AssertionError(f'unsupported config accepted: {config}')
    resource=run_case({'kind':'memory','memory':5,'max_states':2})
    assert resource['status']=='RESOURCE_LIMIT' and resource['certificate'] is None
    observations=[]
    for family in families:
        group=[r for r in cases if all(r['config'].get(k)==v for k,v in family.items())
               and r['config']==dict(family,kind='memory',memory=r['config']['memory'],
                                    state_representation=r['config']['state_representation'],max_seconds=60)]
        assert len(group)==4
        best=min(group,key=lambda r:Fraction(r['certificate']['upper']))
        for m in [3,5]:
            pair=[r for r in group if r['config']['memory']==m]
            assert pair[0]['certificate']['upper']==pair[1]['certificate']['upper']
        observations.append({'target':best['target'],'best_config':best['config'],
                             'best_upper':best['certificate']['upper'],
                             'upper_display':best['certificate']['upper_decimal_display'],
                             'label':'computed bound for this target only; no novelty claim'})
    rectangles=[]
    for width in [2,3,4]:
        cfg={'kind':'rectangle','width':width,'height':3,'max_n':7,'max_seconds':60}
        child=subprocess.run([sys.executable,str(Path(__file__).resolve()),'--case',json.dumps(cfg)],
                             cwd=ROOT,capture_output=True,text=True,timeout=60,check=True)
        rectangles.append(json.loads(child.stdout))
    bridge=run_case({'kind':'bridges','max_n':8,'max_span':2})
    return {'cases':cases,'rectangle_cases':rectangles,'bridge_interface_control':bridge,
            'rejected_combinations':rejected,'resource_limit_control':resource,
            'automatically_selected_observations':observations,
            'scope_counterexample':{'forbidden_word':[0,0],'excluded_full_square_SAW':[[0,0],[1,0],[2,0]],
                                    'consequence':'motif-restricted bounds do not certify unrestricted square SAWs'}}

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--case':
        print(json.dumps(run_case(json.loads(sys.argv[2])),sort_keys=True));raise SystemExit
    eid=sys.argv[1] if len(sys.argv)>1 else 'm2-variants-v1'
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/m2_variants.py {eid}',
        {'memories':[3,5],'wall_seconds_per_case':60},
        ['src/discovery_engine.py','src/discovery_memory.py','src/equitable.py','src/provenance.py',
         'src/connectivity_tm.py','src/reference_enumerator.py','src/bridges.py','src/bridge_spans.py',
         'experiments/m2_variants.py','proofs/DISCOVERY_MEMORY.md','proofs/EQUITABLE_COMPRESSION.md',
         'requirements-lock.txt','environment/NEXT_GOAL_BRIEF.md'],produce))
