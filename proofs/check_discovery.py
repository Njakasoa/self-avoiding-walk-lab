"""Independent exact saved-certificate verifier; no discovery producer imports.

E1 matrices are rebuilt geometrically at every completed memory. Other memory
variants have their rational inequalities checked here and small geometric
models compared in tests/test_discovery.py. Bridge geometry is independently
tested there; this file checks each complete saved bivariate renewal identity.
"""
import hashlib,json,subprocess,sys
from pathlib import Path
from fractions import Fraction
from collections import Counter
from itertools import product

ROOT=Path(__file__).resolve().parents[1]

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()

def receipt(folder):
    folder=Path(folder);meta=json.loads((folder/'metadata.json').read_text())
    for name,wanted in meta['input_hashes'].items():
        data=subprocess.check_output(['git','show',f"{meta['git_commit']}:{name}"],cwd=ROOT)
        assert hashlib.sha256(data).hexdigest()==wanted,name
    for name,wanted in meta['output_hashes'].items():
        assert hashlib.sha256((folder/name).read_bytes()).hexdigest()==wanted,name
    return json.loads((folder/'payload.json').read_text())

def inequality(rows,certificate):
    vector=[Fraction(x) for x in certificate['vector']];upper=Fraction(certificate['upper'])
    assert len(vector)==len(rows) and upper>=0
    if not rows:assert upper==0 and certificate['empty_state_space'];return
    assert all(v>0 and v.denominator==1 for v in vector)
    for i,row in enumerate(rows):
        assert all(0<=int(j)<len(rows) and Fraction(w)>=0 for j,w in row.items())
        assert sum(Fraction(w)*vector[int(j)] for j,w in row.items())<=upper*vector[i]

def original_square(memory,symmetry):
    def normalize(path):
        x0,y0=path[0];path=tuple((x-x0,y-y0) for x,y in path)
        if symmetry=='none':return path
        candidates=[]
        for reflection in [False,True]:
            p=tuple((x,-y if reflection else y) for x,y in path)
            for _ in range(4):
                candidates.append(p);p=tuple((-y,x) for x,y in p)
        return min(candidates)
    def extensions(p):
        x,y=p[-1]
        return [q for q in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if q not in p]
    layer={((0,0),)}
    for _ in range(memory):layer={normalize(p+(q,)) for p in layer for q in extensions(p)}
    states=sorted(layer);index={p:i for i,p in enumerate(states)}
    rows=[{j:Fraction(w) for j,w in Counter(index[normalize(p[1:]+(q,))] for q in extensions(p)).items()} for p in states]
    return states,rows

def e1(data):
    rebuilt={};checked=0
    for case in data['cases']:
        if case['status']!='CERTIFIED':assert case['certificate'] is None;continue
        cfg=case['config'];key=(cfg['memory'],cfg['symmetry'])
        if key not in rebuilt:rebuilt[key]=original_square(*key)
        states,rows=rebuilt[key]
        assert digest(states)==case['states_hash'] and digest(rows)==case['original_rows_hash']
        assert len(rows)==case['original_state_count']
        saved=[{int(j):Fraction(w) for j,w in r.items()} for r in case['rows']]
        if cfg['state_representation']=='equitable':
            mapping=case['mapping'];assert len(mapping)==len(rows)
            assert set(mapping)==set(range(len(saved)))
            for i,row in enumerate(rows):
                aggregated=Counter()
                for j,w in row.items():aggregated[mapping[j]]+=w
                assert dict(aggregated)==saved[mapping[i]],'AP != PB'
            lifted=dict(case['certificate'],vector=[case['certificate']['vector'][k] for k in mapping])
            inequality(rows,lifted)
            # Not used to select the partition or positive certificate vector.
            original=[1]*len(rows);compressed=[1]*len(saved)
            for _ in range(17):
                original=[sum(w*original[j] for j,w in row.items()) for row in rows]
                compressed=[sum(w*compressed[j] for j,w in row.items()) for row in saved]
                assert original==[compressed[k] for k in mapping]
        else:assert rows==saved
        inequality(saved,case['certificate']);checked+=1
    return checked

def bridge_certificate(irreducibles,cert):
    assert irreducibles[0]==0 and all(type(a) is int and a>=0 for a in irreducibles)
    lo,hi=Fraction(cert['root_low']),Fraction(cert['root_high'])
    f=lambda z:sum(a*z**n for n,a in enumerate(irreducibles))
    assert 0<=lo<=hi<=1 and f(lo)<=1<=f(hi)
    assert Fraction(cert['lower'])==1/hi

def scan(value):
    """Find all independently checkable exact certificate objects in a payload."""
    checked=0
    if isinstance(value,dict):
        if 'matrix' in value and 'spectral_certificate' in value:
            weights=[Fraction(value['ratio']),Fraction(1)]
            n=value['n'];expected=[];steps=[(1,0),(0,1),(-1,0),(0,-1)]
            for first in [0,1]:
                row=[Fraction(0),Fraction(0)]
                for suffix in product(range(4),repeat=n-1):
                    word=(first,)+suffix;path=[(0,0)];edges=set();weight=Fraction(1)
                    for direction in word:
                        dx,dy=steps[direction];x,y=path[-1];q=x+dx,y+dy
                        edge=tuple(sorted([path[-1],q]))
                        if (q in path if value['mode']=='saw' else edge in edges):break
                        edges.add(edge);path.append(q);weight*=weights[direction%2]
                    else:row[word[-1]%2]+=weight/weights[first]
                expected.append(row)
            matrix=[[Fraction(w) for w in row] for row in value['matrix']]
            assert matrix==expected,'independent He overlap matrix mismatch'
            inequality([{j:w for j,w in enumerate(row)} for row in matrix],value['spectral_certificate'])
            degree=value['root_degree'];upper=Fraction(value['spectral_certificate']['upper'])
            assert degree==n-1 and Fraction(value['root_low'])**degree<=upper<=Fraction(value['root_high'])**degree
            checked+=1
        if 'rows' in value and isinstance(value.get('certificate'),dict) and 'upper' in value['certificate']:
            inequality(value['rows'],value['certificate']);checked+=1
        if 'b_n_s' in value and 'i_n_s' in value:
            bs=[{int(s):c for s,c in row.items()} for row in value['b_n_s']]
            irr=[{int(s):c for s,c in row.items()} for row in value['i_n_s']]
            assert bs[0]=={0:1} and irr[0]=={}
            for n in range(1,len(bs)):
                actual=Counter()
                for k in range(1,n+1):
                    for s,a in irr[k].items():
                        for t,b in bs[n-k].items():actual[s+t]+=a*b
                cap=max((s for row in bs for s in row),default=0)
                assert {s:c for s,c in actual.items() if s<=cap}==bs[n]
            if 'certificate' in value:bridge_certificate([sum(r.values()) for r in irr],value['certificate'])
            checked+=1
        for child in value.values():checked+=scan(child)
    elif isinstance(value,list):
        for child in value:checked+=scan(child)
    return checked

if __name__=='__main__':
    for folder in sys.argv[1:]:
        data=receipt(folder);count=scan(data)
        if 'comparisons' in data and 'e1-' in str(folder):count+=e1(data)
        print(f'PASS {folder}: frozen receipts, {count} certificate/geometry checks')
