"""Finite-memory SAW superlanguage, D4 orbit quotient, exact Collatz certificate."""
from collections import Counter
from fractions import Fraction

DIRECTIONS = ((1,0),(0,1),(-1,0),(0,-1))

def canonical(path):
    """Translate first vertex to origin; quotient by all eight lattice isometries."""
    x0,y0=path[0]
    p=tuple((x-x0,y-y0) for x,y in path)
    return min(tuple((sx*(y if swap else x),sy*(x if swap else y)) for x,y in p)
               for swap in (False,True) for sx in (-1,1) for sy in (-1,1))

def memory_automaton(memory, symmetry=True):
    if type(memory) is not int or memory < 1:
        raise ValueError('memory must be a positive integer')
    def normalize(p):
        if symmetry:return canonical(p)
        x0,y0=p[0];return tuple((x-x0,y-y0) for x,y in p)
    states={((0,0),)}
    for _ in range(memory):
        nxt=set()
        for p in states:
            x,y=p[-1]
            for dx,dy in DIRECTIONS:
                q=(x+dx,y+dy)
                if q not in p:nxt.add(normalize(p+(q,)))
        states=nxt
    states=sorted(states);index={s:i for i,s in enumerate(states)};rows=[]
    for p in states:
        row=Counter();x,y=p[-1]
        for dx,dy in DIRECTIONS:
            q=(x+dx,y+dy)
            if q not in p:row[index[normalize(p[1:]+(q,))]]+=1
        rows.append(dict(sorted(row.items())))
    return states,rows

def multiply(rows,v):
    return [sum(w*v[j] for j,w in row.items()) for row in rows]

def certificate(rows,iterations=60):
    if iterations<0:raise ValueError('iterations must be nonnegative')
    v=[1]*len(rows)
    for _ in range(iterations):
        nxt=multiply(rows,v)
        # A+I gives a strictly positive vector even if dead-end states exist.
        v=[a+b for a,b in zip(nxt,v)]
    av=multiply(rows,v)
    bound=max(Fraction(a,b) for a,b in zip(av,v))
    return {'classification':'CERTIFIED SPECTRAL BOUND','upper':str(bound),
            'upper_decimal_display':float(bound),'vector':[str(x) for x in v],
            'iterations':iterations}

def check_certificate(rows,cert):
    v=[int(x) for x in cert['vector']];u=Fraction(cert['upper'])
    if len(v)!=len(rows) or not v or min(v)<=0 or u<0:return False
    if any(not isinstance(w,int) or w<0 or j<0 or j>=len(v) for r in rows for j,w in r.items()):return False
    return all(u.denominator*a<=u.numerator*b for a,b in zip(multiply(rows,v),v))
