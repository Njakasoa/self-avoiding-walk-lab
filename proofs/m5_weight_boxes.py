"""Exact rational-box Jacobian bounds for the regularized M5 weights.

Uses rational intervals and first-order automatic differentiation. This
checker covers rational factors only, not kernel square-root perturbations.
"""
from fractions import Fraction as F
import json


class Box:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        if self.lo>self.hi: raise ValueError('empty box')
    def __add__(self, y):
        y=box(y); return Box(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self): return Box(-self.hi,-self.lo)
    def __sub__(self,y): return self+-box(y)
    def __rsub__(self,y): return box(y)+-self
    def __mul__(self,y):
        y=box(y); p=[self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return Box(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,y):
        y=box(y)
        if y.lo<=0<=y.hi: raise ZeroDivisionError('box crosses zero')
        return self*Box(1/y.hi,1/y.lo)
    def __rtruediv__(self,y): return box(y)/self
    def absmax(self): return max(abs(self.lo),abs(self.hi))


def box(x): return x if isinstance(x,Box) else Box(x)


class Jet:
    def __init__(self,v,d=None):
        self.v=box(v); self.d=[box(x) for x in ([0]*4 if d is None else d)]
    def __add__(self,y):
        y=jet(y); return Jet(self.v+y.v,[a+b for a,b in zip(self.d,y.d)])
    __radd__=__add__
    def __neg__(self): return Jet(-self.v,[-x for x in self.d])
    def __sub__(self,y): return self+-jet(y)
    def __rsub__(self,y): return jet(y)+-self
    def __mul__(self,y):
        y=jet(y); return Jet(self.v*y.v,[a*y.v+self.v*b for a,b in zip(self.d,y.d)])
    __rmul__=__mul__
    def __truediv__(self,y):
        y=jet(y)
        return Jet(self.v/y.v,[(a*y.v-self.v*b)/(y.v*y.v) for a,b in zip(self.d,y.d)])
    def __rtruediv__(self,y): return jet(y)/self


def jet(x): return x if isinstance(x,Jet) else Jet(x)


def produce():
    bounds=[(F(2,5),F(83,200)),(F(99,100),1),(F(2,5),1),(F(99,100),1)]
    t,q,u,a=[Jet(Box(lo,hi),[int(i==j) for j in range(4)])
             for i,(lo,hi) in enumerate(bounds)]
    C=q-t; D=1-t*q; uh=t*q/C
    def f(v): return v/(1-t*v)
    fh=f(uh); fu=f(u)
    L1=fh/(1-uh); L2=fh*fh/(1-uh)
    dd=1/((1-t*u)*(1-t*uh))
    V1=(dd+L1)/C; V2=((fu+fh)*dd+L2)/C
    g=t-D*q; S0=-t*D*D/g
    B1=C/g+L1*S0
    B2=f(q)*C/g+L2*S0
    Qe=q*t*t*a*(1-t*t)
    items={'V1':V1,'V2':V2,'boundary_P':B1,'boundary_H_over_t2':B2,'Q_over_e':Qe}
    out={}
    for name,j in items.items():
        size=j.v.absmax(); lip=sum(d.absmax() for d in j.d)
        if size>=10**6 or lip>=10**6:
            raise ArithmeticError((name,size,lip))
        out[name]={'value_box':[str(j.v.lo),str(j.v.hi)],
                   'value_abs_upper':str(size),
                   'gradient_L1_upper':str(lip),
                   'bounded_by_one_million':True}
    return {'classification':'EXACT RATIONAL WEIGHT BOXES AND JACOBIANS',
            'variable_order':['t','q','u','a=(1-exp(-e))/e'],
            'boxes':[[str(a),str(b)] for a,b in bounds],
            'bounds':out,'status':'pass'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
