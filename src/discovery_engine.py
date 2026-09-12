"""Target-aware case execution. Resource-limited cases never carry certificates."""
import hashlib,json,resource,time
from fractions import Fraction
from src.discovery_memory import build_memory,exact_certificate,verify_bound,ResourceLimit

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()

def memory_case(config):
    allowed={'kind','lattice','boundary','width','weights','forbidden_words','symmetry','memory',
             'state_representation','iterations','max_states','max_seconds'}
    if set(config)-allowed:raise ValueError(f'unsupported parameters: {sorted(set(config)-allowed)}')
    if config.get('kind','memory')!='memory':raise ValueError('memory case required')
    representation=config.get('state_representation','memory')
    if representation not in ('memory','equitable'):raise ValueError('unsupported state representation')
    if 'memory' not in config:raise ValueError('memory required')
    kwargs={k:v for k,v in config.items() if k not in ('kind','state_representation','iterations')}
    begin=time.monotonic()
    try:model=build_memory(**kwargs)
    except ResourceLimit as error:
        return {'config':config,'status':'RESOURCE_LIMIT','reason':str(error),
                'certificate':None,'runtime_seconds':time.monotonic()-begin}
    rows=model['rows'];selected=rows;mapping=list(range(len(rows)));refine_seconds=0.0
    if representation=='equitable':
        from src.equitable import equitable_partition,quotient,verify_equitable,lift_vector
        start=time.monotonic();mapping=equitable_partition(rows);selected=quotient(rows,mapping)
        assert verify_equitable(rows,mapping,selected)
        refine_seconds=time.monotonic()-start
    start=time.monotonic();cert=exact_certificate(selected,config.get('iterations',120))
    assert verify_bound(selected,cert)
    spectral_seconds=time.monotonic()-start
    if representation=='equitable':
        lifted=dict(cert,vector=[str(x) for x in lift_vector(mapping,[int(x) for x in cert['vector']])],
                    empty_state_space=not rows)
        assert verify_bound(rows,lifted)
    return {'config':config,'status':'CERTIFIED','target':model['target'],
            'symmetry_order':model['symmetry_order'],'original_state_count':len(rows),
            'state_count':len(selected),'transition_count':sum(len(r) for r in selected),
            'original_transition_count':sum(len(r) for r in rows),
            'states_hash':digest(model['states']),'original_rows_hash':digest(rows),
            'mapping':mapping if representation=='equitable' else None,
            'rows':[{str(j):str(w) for j,w in row.items()} for row in selected],
            'certificate':cert,'build_seconds':model['build_seconds'],
            'baseline':{'method':'maximum outgoing weighted row sum',
                        'upper':str(max((sum(row.values()) for row in rows),default=0)),
                        'scope':'same target and constructed memory; elementary positive-ones certificate'},
            'refine_seconds':refine_seconds,'spectral_seconds':spectral_seconds,
            'runtime_seconds':time.monotonic()-begin,
            'peak_rss_kib_process':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'memory_scope':'peak of this case process; graph is built before equitable reduction'}

def bridge_case(config):
    """An irreducible dictionary gives a lower bound for the unrestricted square lattice."""
    allowed={'kind','lattice','max_n','max_span','max_seconds','state_representation'}
    if set(config)-allowed:raise ValueError(f'unsupported bridge parameters: {sorted(set(config)-allowed)}')
    if config.get('kind')!='bridges' or config.get('lattice','square')!='square':
        raise ValueError('bridges support the unweighted square lattice only')
    if config.get('state_representation','path')!='path':raise ValueError('bridges require path state representation')
    if 'max_n' not in config or type(config['max_n']) is not int or config['max_n']<1:
        raise ValueError('positive integer max_n required for a bridge certificate')
    if config.get('max_span')==0:raise ValueError('positive max_span or None required for a bridge certificate')
    from src.bridge_spans import enumerate_bridge_spans
    from src.bridges import lower_certificate
    begin=time.monotonic()
    try:
        model=enumerate_bridge_spans(config['max_n'],config.get('max_span'),config.get('max_seconds',300))
    except TimeoutError as error:
        return {'config':config,'status':'RESOURCE_LIMIT','reason':str(error),
                'certificate':None,'runtime_seconds':time.monotonic()-begin}
    cert=lower_certificate(model['irreducibles'])
    return {'config':config,'status':'CERTIFIED','target':{'lattice':'square','boundary':'plane','weights':['1']*4},
            'family':{'irreducible_max_length':config['max_n'],'irreducible_max_span':config.get('max_span'),
                      'concatenated_length_and_span':'unbounded'},
            'b_n_s':model['b_n_s'],'i_n_s':model['i_n_s'],'bridges':model['bridges'],
            'irreducibles':model['irreducibles'],'certificate':cert,
            'state_count':None,'state_scope':'depth-first enumeration; no stored transition graph',
            'baseline':{'method':'unit east irreducible only','lower':'1'},
            'runtime_seconds':time.monotonic()-begin,
            'peak_rss_kib_process':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}

def run_case(config):
    if not isinstance(config,dict):raise ValueError('case must be a parameter object')
    kind=config.get('kind','memory')
    if kind=='memory':return memory_case(config)
    if kind=='bridges':return bridge_case(config)
    if kind=='rectangle':return rectangle_case(config)
    raise ValueError(f'unsupported case kind: {kind}')

def rectangle_case(config):
    """Expose the existing all-vertex connectivity transfer baseline by width."""
    allowed={'kind','lattice','boundary','width','height','max_n','state_representation','max_seconds'}
    if set(config)-allowed:raise ValueError(f'unsupported rectangle parameters: {sorted(set(config)-allowed)}')
    if config.get('lattice','square')!='square' or config.get('boundary','rectangle')!='rectangle':
        raise ValueError('only square finite rectangles are supported')
    if config.get('state_representation','connectivity')!='connectivity':
        raise ValueError('rectangle requires connectivity state representation')
    w,h,n=config.get('width'),config.get('height'),config.get('max_n')
    if any(type(v) is not int or v<1 for v in [w,h]) or type(n) is not int or n<0:
        raise ValueError('positive width/height and nonnegative max_n required')
    if w*h>12 or n>11:raise ValueError('small transfer baseline supports at most12 vertices and max_n<=11')
    from math import isfinite
    cap=config.get('max_seconds',300)
    if isinstance(cap,bool) or not isinstance(cap,(int,float)) or not isfinite(cap) or cap<=0:
        raise ValueError('finite positive time cap required')
    from src.connectivity_tm import connectivity_counts
    from src.reference_enumerator import rectangle_counts
    start=time.monotonic();result=connectivity_counts(w,h,n);elapsed=time.monotonic()-start
    baseline_start=time.monotonic();baseline=rectangle_counts(w,h,n)
    baseline_seconds=time.monotonic()-baseline_start
    assert baseline==result['counts']
    if time.monotonic()-start>cap:
        return {'config':config,'status':'RESOURCE_LIMIT','certificate':None,
                'reason':'complete-case time cap exceeded','runtime_seconds':time.monotonic()-start}
    return {'config':config,'status':'EXACT_FINITE_COUNTS',
            'target':{'lattice':'square','boundary':'rectangle','width':w,'height':h,'root':[0,0]},
            'counts':result['counts'],'state_count':result['peak_states'],
            'state_representation':result['state_representation'],'edge_count':result['edge_count'],
            'certificate':None,'bound':None,'bound_scope':'finite rectangle counts do not imply an infinite-lattice bound',
            'baseline':{'method':'independent DFS','counts_equal':True,'runtime_seconds':baseline_seconds},
            'transfer_seconds':elapsed,'runtime_seconds':time.monotonic()-start,
            'peak_rss_kib_process':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}

if __name__=='__main__':
    import sys,subprocess
    from pathlib import Path
    if len(sys.argv)==3 and sys.argv[1]=='--child':
        print(json.dumps(run_case(json.loads(sys.argv[2])),sort_keys=True))
    elif len(sys.argv)==2:
        config=json.loads(Path(sys.argv[1]).read_text())
        cap=config.get('max_seconds',300)
        from math import isfinite
        if isinstance(cap,bool) or not isinstance(cap,(int,float)) or not isfinite(cap) or cap<=0:
            raise ValueError('finite positive complete-case time cap required')
        try:
            child=subprocess.run([sys.executable,'-m','src.discovery_engine','--child',json.dumps(config)],
                                 capture_output=True,text=True,timeout=cap,check=True)
            print(child.stdout,end='')
        except subprocess.TimeoutExpired:
            print(json.dumps({'config':config,'status':'RESOURCE_LIMIT','certificate':None,
                              'reason':'complete-case time cap exceeded'}))
    else:raise SystemExit('usage: python -m src.discovery_engine CONFIG.json')
