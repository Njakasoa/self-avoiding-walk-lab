"""Bridges with strict initial minimum, weak terminal maximum; direct renewal cuts."""
from collections import Counter
from fractions import Fraction
DIRECTIONS=((1,0),(-1,0),(0,1),(0,-1))

def renewal_points(path):
    xs=[p[0] for p in path]
    return [k for k in range(1,len(path)-1)
            if max(xs[:k+1])==xs[k] and min(xs[k+1:])>xs[k]]

def enumerate_bridges(max_n):
    if type(max_n) is not int or max_n<0:raise ValueError('max_n must be nonnegative integer')
    b=[0]*(max_n+1);b[0]=1;i=[0]*(max_n+1);spans=[Counter() for _ in b]
    path=[(0,0)];seen=set(path)
    def visit(x,y,depth,max_x):
        if depth and x==max_x:
            b[depth]+=1;spans[depth][x]+=1
            if not renewal_points(path):i[depth]+=1
        if depth==max_n:return
        for dx,dy in DIRECTIONS:
            q=(x+dx,y+dy)
            if q[0]>0 and q not in seen:
                seen.add(q);path.append(q);visit(*q,depth+1,max(max_x,q[0]));path.pop();seen.remove(q)
    visit(0,0,0,0)
    return {'bridges':b,'irreducibles':i,'span_counts':[dict(sorted(s.items())) for s in spans]}

def renewal_inverse(b):
    """Independent formal-series inversion B=1/(1-I)."""
    i=[0]*len(b)
    for n in range(1,len(b)):i[n]=b[n]-sum(i[k]*b[n-k] for k in range(1,n))
    return i

def lower_certificate(irreducibles,bits=48):
    if len(irreducibles)<2 or irreducibles[1]<1 or any(x<0 for x in irreducibles):
        raise ValueError('nonnegative irreducible counts including unit bridge required')
    def value(z):return sum(a*z**n for n,a in enumerate(irreducibles))
    lo=Fraction(0);hi=Fraction(1)
    for _ in range(bits):
        mid=(lo+hi)/2
        if value(mid)<1:lo=mid
        else:hi=mid
    # I(hi)>=1 => root r<=hi => 1/r>=1/hi; family growth <= square μ.
    return {'classification':'RIGOROUS INTERVAL','root_low':str(lo),'root_high':str(hi),
            'lower':str(1/hi),'lower_decimal_display':float(1/hi),
            'I_at_low':str(value(lo)),'I_at_high':str(value(hi))}
