"""Select findings from frozen sweeps; compare like targets under equal budgets."""
import json,sys
from pathlib import Path
from fractions import Fraction
from src.discovery_engine import memory_case
from src.provenance import run_record
ROOT=Path(__file__).resolve().parents[1]
FOLDERS=['e1-compression-v1','e2-spans-v1','e3-weights-v1','m2-variants-v2']

def produce():
    e1,e2,e3,variants=[json.loads((ROOT/'results'/f/'payload.json').read_text()) for f in FOLDERS]
    bridges=[c for c in e2['cases'] if c['status']=='complete']
    def brief(c):
        return {'max_n':c['max_n'],'max_span':c['max_span'],'dfs_nodes':c['stats']['dfs_nodes'],
                'lower':c['certificate']['lower'],'lower_display':c['certificate']['lower_decimal_display'],
                'runtime_seconds':c['runtime_seconds']}
    budgets=[]
    for budget in [100,1000,10000,100000,1000000,3000000,30000000]:
        eligible=[c for c in bridges if c['stats']['dfs_nodes']<=budget]
        if not eligible:continue
        best=max(eligible,key=lambda c:Fraction(c['certificate']['lower']))
        baseline=[c for c in eligible if c['max_span'] is None]
        base=max(baseline,key=lambda c:Fraction(c['certificate']['lower'])) if baseline else None
        budgets.append({'dfs_budget':budget,'best':brief(best),
                        'unrestricted_span_baseline':brief(base) if base else None,
                        'baseline_scope':'same sweep and DFS budget; absent if even n12 exceeds budget'})
    dominates=lambda a,b:(a['stats']['dfs_nodes']<=b['stats']['dfs_nodes'] and
                          Fraction(a['certificate']['lower'])>=Fraction(b['certificate']['lower']) and
                          (a['stats']['dfs_nodes']<b['stats']['dfs_nodes'] or
                           Fraction(a['certificate']['lower'])>Fraction(b['certificate']['lower'])))
    frontier=[brief(b) for b in bridges if not any(dominates(a,b) for a in bridges)]
    dominated=[{'dominated':brief(b),'dominates':brief(a)} for b in bridges for a in bridges if dominates(a,b)]
    equitable=[c for c in e1['cases'] if c['status']=='CERTIFIED' and c['config']['state_representation']=='equitable']
    transitions=[]
    for c in equitable:
        m=c['config']['memory']
        if m%2!=1:continue
        incoming={int(j) for row in c['rows'] for j,w in row.items() if Fraction(w)>0}
        absent=sorted(set(range(c['state_count']))-incoming)
        nxt=next((d for d in equitable if d['config']['memory']==m+1),None)
        transitions.append({'memory':m,'states':c['state_count'],'zero_indegree_classes':absent,
                            'prediction_next_memory':c['state_count']-len(absent),
                            'observed_next_memory':nxt['state_count'] if nxt else None,
                            'scope':'structural hypothesis; out-of-sweep validation recorded separately'})
    axis=e3['boundary_checks']['axis_x0_y1']['case']
    near=[]
    for x in ['1/100','1/1000','1/10000']:
        c=(e3['boundary_checks']['small_x1_over_1000_y1']['case'] if x=='1/1000' else
           memory_case({'kind':'memory','memory':3,'weights':[x,'1',x,'1'],
                        'state_representation':'equitable','max_seconds':60}))
        assert c['status']=='CERTIFIED'
        u=Fraction(c['certificate']['upper']);assert u>=1
        near.append({'x':x,'upper_minus_direct_axis_mu':str(u-1),'case':c})
    gap=Fraction(axis['certificate']['upper'])-1
    assert 0<=gap<Fraction(1,10**18)
    return {'input_experiments':FOLDERS,'bridge_equal_dfs_budget':budgets,
            'bridge_pareto_frontier':frontier,'bridge_dominated_cases':dominated,
            'memory_equal_state_budget':e1['automatically_selected_observations']['best_upper_at_state_budgets'],
            'linegraph_predictions':transitions,
            'weighted_family':e3['automatically_selected_cross_family_observations'],
            'axis_supplement':{'direct_mu':'1','axis_certificate_minus_mu':str(gap),
                               'near_axis_cases':near,
                               'observed_decreasing_gap':all(Fraction(a['upper_minus_direct_axis_mu'])>=Fraction(b['upper_minus_direct_axis_mu']) for a,b in zip(near,near[1:])),
                               'scope':'finite samples and a finite-iteration certificate, no convergence theorem'},
            'interpretation':'known methods; automatic finite observations do not establish novelty'}

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'discovery-findings-v1'
    paths=['experiments/discovery_findings.py','src/discovery_engine.py','src/discovery_memory.py',
           'src/equitable.py','src/provenance.py','proofs/DISCOVERY_MEMORY.md','DISCOVERY_ENGINE.md',
           'requirements-lock.txt','environment/NEXT_GOAL_BRIEF.md']
    paths += [f'results/{f}/{name}.json' for f in FOLDERS for name in ['payload','metadata']]
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/discovery_findings.py {eid}',
                     {'dfs_budgets':[100,1000,10000,100000,1000000,3000000,30000000]},paths,produce))
