"""Exact finite-memory superlanguages with explicit lattice/domain/weight target.

A finite strip or forbidden motif changes the target. Its upper certificate
is never relabelled an upper bound for all unrestricted square-lattice SAWs.
"""
from collections import Counter
from fractions import Fraction
from math import lcm,isfinite
from numbers import Real
from time import monotonic

SQUARE=((1,0),(0,1),(-1,0),(0,-1))
TRIANGULAR=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))

class ResourceLimit(RuntimeError):
    """No partial construction from this exception is a certified matrix."""

def _linear(p,m):
    a,b,c,d=m;x,y=p;return a*x+b*y,c*x+d*y

def _group(lattice):
    if lattice=='square':
        return sorted({(sx,0,0,sy) for sx in [-1,1] for sy in [-1,1]}|
                      {(0,sx,sy,0) for sx in [-1,1] for sy in [-1,1]})
    mats=set();basis=((1,0),(0,1))
    for _ in range(6):
        u,v=basis;mats.add((u[0],v[0],u[1],v[1]))
        mats.add((u[1],v[1],u[0],v[0]))
        basis=tuple((-y,x+y) for x,y in basis)
    return sorted(mats)

def build_memory(memory,*,lattice='square',boundary='plane',width=None,
                 weights=None,forbidden_words=(),symmetry='auto',
                 max_states=100_000,max_seconds=300):
    if type(memory) is not int or memory<1:raise ValueError('positive integer memory required')
    if lattice not in ('square','triangular'):raise ValueError('unsupported lattice')
    if boundary not in ('plane','strip'):raise ValueError('unsupported boundary')
    if boundary=='plane' and width is not None:raise ValueError('width applies only to strip')
    if boundary=='strip' and (type(width) is not int or width<1):raise ValueError('positive strip width required')
    if symmetry not in ('none','auto','d4'):raise ValueError('unsupported symmetry')
    if type(max_states) is not int or max_states<1:raise ValueError('positive state cap required')
    if isinstance(max_seconds,bool) or not isinstance(max_seconds,Real) or not isfinite(max_seconds) or max_seconds<=0:raise ValueError('finite positive time cap required')
    directions=SQUARE if lattice=='square' else TRIANGULAR
    if weights is None:weights=[1]*len(directions)
    if len(weights)!=len(directions):raise ValueError('one weight per direction required')
    if any(isinstance(w,(bool,float)) for w in weights):raise ValueError('exact rational weights required')
    weights=tuple(Fraction(w) for w in weights)
    if any(w<0 for w in weights):raise ValueError('nonnegative weights required')
    motifs=frozenset(tuple(word) for word in forbidden_words)
    if any(not word or len(word)>memory+1 or any(type(i) is not int or not 0<=i<len(directions) for i in word) for word in motifs):
        raise ValueError('motifs must use valid direction indices and fit memory+1')
    dir_index={v:i for i,v in enumerate(directions)}
    group=[]
    for mat in _group(lattice):
        # A strip uses fixed absolute y; only affine reflections along its axes preserve it.
        if boundary=='strip' and (mat[1]!=0 or mat[2]!=0):continue
        perm=tuple(dir_index[_linear(d,mat)] for d in directions)
        if any(weights[i]!=weights[perm[i]] for i in range(len(weights))):continue
        if frozenset(tuple(perm[i] for i in word) for word in motifs)!=motifs:continue
        group.append(mat)
    if symmetry=='none':group=[(1,0,0,1)]
    if symmetry=='d4' and (lattice!='square' or len(group)!=8):
        raise ValueError('D4 does not preserve this lattice, domain, weights or motifs')
    def norm(path):
        candidates=[]
        for mat in group:
            transformed=[_linear(p,mat) for p in path]
            if boundary=='strip' and mat[3]<0:
                transformed=[(x,y+width-1) for x,y in transformed]
            x0,y0=transformed[0]
            candidates.append(tuple((x-x0,y-y0 if boundary=='plane' else y) for x,y in transformed))
        return min(candidates)
    def permitted(path,q):
        if q in path:return False
        if boundary=='strip' and not 0<=q[1]<width:return False
        if not motifs:return True
        p=path+(q,)
        word=tuple(dir_index[(b[0]-a[0],b[1]-a[1])] for a,b in zip(p,p[1:]))
        return not any(len(bad)<=len(word) and word[-len(bad):]==bad for bad in motifs)
    begin=monotonic();ticks=0
    def budget(size):
        nonlocal ticks
        if size>max_states:raise ResourceLimit(f'state cap {max_states} exceeded; no complete matrix')
        ticks+=1
        if ticks%128==0 and monotonic()-begin>max_seconds:raise ResourceLimit('time cap exceeded; no complete matrix')
    layer=set()
    for y in (range(width) if boundary=='strip' else [0]):
        layer.add(norm(((0,y),)));budget(len(layer))
    for _ in range(memory):
        nxt=set()
        for path in layer:
            x,y=path[-1]
            for dx,dy in directions:
                q=x+dx,y+dy
                if permitted(path,q):nxt.add(norm(path+(q,)));budget(len(nxt))
            budget(len(nxt))
        layer=nxt
    states=sorted(layer);index={p:i for i,p in enumerate(states)};rows=[]
    for path in states:
        row=Counter();x,y=path[-1]
        for i,(dx,dy) in enumerate(directions):
            q=x+dx,y+dy
            if permitted(path,q) and weights[i]:row[index[norm(path[1:]+(q,))]]+=weights[i]
        rows.append(dict(sorted(row.items())));budget(len(states))
    if monotonic()-begin>max_seconds:raise ResourceLimit('time cap exceeded; no complete matrix')
    return {'states':states,'rows':rows,'symmetry_order':len(group),
            'target':{'lattice':lattice,'boundary':boundary,'width':width,
                      'weights':[str(w) for w in weights],
                      'forbidden_words':[list(w) for w in sorted(motifs)]},
            'build_seconds':monotonic()-begin}

def exact_certificate(rows,iterations=120):
    """Scale rational A to integer B; v=(B+sI)^k1, s=max row sum.

This choice is homogeneous in weights, unlike a fixed additive identity shift.
All returned decimals are displays only. Empty states imply no arbitrarily long
accepted walks, so growth is zero and the certificate records the empty case.
"""
    if type(iterations) is not int or iterations<0:raise ValueError('nonnegative integer iterations required')
    n=len(rows)
    if any(type(j) is not int or not 0<=j<n or isinstance(w,(bool,float)) or Fraction(w)<0 for row in rows for j,w in row.items()):
        raise ValueError('invalid nonnegative rational matrix')
    q=lcm(*(Fraction(w).denominator for row in rows for w in row.values()))
    scaled=[{j:int(Fraction(w)*q) for j,w in row.items()} for row in rows]
    shift=max((sum(row.values()) for row in scaled),default=0);v=[1]*n
    if shift:
        for _ in range(iterations):v=[shift*v[i]+sum(w*v[j] for j,w in row.items()) for i,row in enumerate(scaled)]
    av=[sum(w*v[j] for j,w in row.items()) for row in scaled]
    upper=max((Fraction(a,q*b) for a,b in zip(av,v)),default=Fraction(0))
    return {'classification':'CERTIFIED SPECTRAL BOUND','upper':str(upper),
            'upper_decimal_display':float(upper),'vector':[str(x) for x in v],
            'iterations':iterations,'integer_scale':q,'integer_shift':shift,
            'empty_state_space':n==0}

def verify_bound(rows,cert):
    try:
        if any(isinstance(x,(bool,float)) or Fraction(x).denominator!=1 for x in cert['vector']):return False
        v=[int(Fraction(x)) for x in cert['vector']];u=Fraction(cert['upper']);n=len(rows)
        if len(v)!=n or any(x<=0 for x in v) or u<0:return False
        if not n:return u==0 and cert.get('empty_state_space') is True
        if any(type(j) is not int or not 0<=j<n or isinstance(w,(bool,float)) or Fraction(w)<0 for row in rows for j,w in row.items()):return False
        return all(sum(Fraction(w)*v[j] for j,w in row.items())<=u*v[i] for i,row in enumerate(rows))
    except (KeyError,ValueError,TypeError,ZeroDivisionError):return False
