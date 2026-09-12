"""Standalone verifier: no producer imports, exact arithmetic only.
Checks frozen source provenance, every outgoing direction against geometric
states, D4 orbit destinations and all rational inequalities. No trust in
stored matrix or displayed decimals. Bridge coefficients are checked algebraically here; independent geometric
replay is performed by the separate test implementation and reviewer.
"""
import hashlib,json,subprocess,sys
from fractions import Fraction
from pathlib import Path

def norm(path):
    x,y=path[0];p=[(a-x,b-y) for a,b in path]
    variants=[]
    for a,b in ((1,1),(1,-1),(-1,1),(-1,-1)):
        variants.append(tuple((a*x,b*y) for x,y in p))
        variants.append(tuple((a*y,b*x) for x,y in p))
    return min(variants)

def check(folder):
    folder=Path(folder);data=json.loads((folder/'payload.json').read_text());meta=json.loads((folder/'metadata.json').read_text())
    root=Path(__file__).resolve().parents[1]
    for rel,h in meta['input_hashes'].items():
        content=subprocess.check_output(['git','show',f"{meta['git_commit']}:{rel}"],cwd=root)
        assert hashlib.sha256(content).hexdigest()==h,rel
    for rel,h in meta['output_hashes'].items():assert hashlib.sha256((folder/rel).read_bytes()).hexdigest()==h
    for a in data['automata']:
        states=[tuple(tuple(q) for q in p) for p in a['states']];index={p:i for i,p in enumerate(states)}
        assert len(index)==a['state_count']==len(a['rows'])
        # Independent generation proves completeness, not just validity of listed rows.
        layer={((0,0),)}
        for _ in range(a['memory']):
            new=set()
            for p in layer:
                x,y=p[-1]
                for q in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if q not in p:new.add(norm(p+(q,)))
            layer=new
        assert layer==set(states)
        cert=a['certificate'];v=list(map(int,cert['vector']));u=Fraction(cert['upper'])
        assert len(v)==len(states) and min(v)>0
        for idx,p in enumerate(states):
            actual={};x,y=p[-1]
            for q in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if q not in p:
                    j=index[norm(p[1:]+(q,))];actual[j]=actual.get(j,0)+1
            assert actual=={int(k):val for k,val in a['rows'][idx].items()}
            assert sum(w*v[j] for j,w in actual.items())*u.denominator<=u.numerator*v[idx]
    b=data['bridges'];coeff=b['irreducibles'];assert coeff[0]==0 and all(type(x)==int and x>=0 for x in coeff)
    assert b['bridges'][0]==1
    for n in range(1,len(coeff)):assert b['bridges'][n]==sum(coeff[k]*b['bridges'][n-k] for k in range(1,n+1))
    c=b['certificate'];lo,hi=Fraction(c['root_low']),Fraction(c['root_high'])
    f=lambda z:sum(a*z**n for n,a in enumerate(coeff))
    assert 0<=lo<=hi and f(lo)<=1<=f(hi) and Fraction(c['lower'])==1/hi
    print('PASS: frozen inputs, output hashes, complete automata, exact spectral inequalities, renewal algebra and root interval')
    print('Scope: bridge geometric count validity is checked independently by tests, not inferred from this algebra alone.')

if __name__=='__main__':check(sys.argv[1])
