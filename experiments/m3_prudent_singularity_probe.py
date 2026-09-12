"""Exploratory BB2014 meromorphic continuation; numeric, never a certificate.

P and hook P are transcribed from Propositions14/16. Real evaluations beyond
the first pole are analytic-continuation probes, not convergent positive-series
evaluations. Tail convergence and increased precision must be checked separately.
"""
import json
import mpmath as mp

def kernel(t,v):
    a=1-t*v+t*t+t**3*v
    return 2*t/(a+mp.sqrt(a*a-4*t*t))

def evaluate(t,terms=300,dps=60):
    with mp.workdps(dps):
        t=mp.mpf(t);q=kernel(t,1);one=1-t*q
        total=mp.mpf(0);hook=mp.mpf(0);prod=mp.mpf(1);last=None
        for n in range(terms):
            v=q**(2*n);a=kernel(t,v);b=kernel(t,v*q*q)
            h=t*q-(q-t)*a
            A=(q-t)*(1-t*t)*(a*one-(q*(q-t)+t*(1-q*q)*a)*b)/(one*(1-t*a)*(1-t*b)*h)
            B=q*(q-t)**2*(t-one*b)/(one**2*h)
            Ah=t*t*(1-t*t)*(q-t)*(
                one*a*a*(1-2*t*b)-(q*(q-t)-t*a*(2*q*(q-t)+t*(1-q*q)*a))*b*b
                )/(one*(1-t*a)**2*(1-t*b)**2*h)
            total+=prod*A;hook+=prod*Ah;last=max(abs(prod*A),abs(prod*Ah));prod*=B
        P=q*(1-t*t)/one+q*total
        Ph=t*t*q*q*(1-t*t)/(one*one)+q*hook
        return {'t':str(t),'q':str(q),'P':str(P),'hook':str(Ph),
                'irreducible':str((P-Ph)/(1+P)),'last_term_magnitude':str(last),
                'terms':terms,'dps':dps}

def pole(k,dps=60):
    with mp.workdps(dps):
        low=mp.mpf('0.39');high=mp.sqrt(2)-1-mp.mpf(10)**(-dps+10)
        def f(t):
            q=kernel(t,1);return t*q-(q-t)*kernel(t,q**(2*k))
        assert f(low)>0 and f(high)<0
        for _ in range(dps*4):
            mid=(low+high)/2
            if f(mid)>0:low=mid
            else:high=mid
        return (low+high)/2

def produce():
    mp.mp.dps=70
    poles=[pole(k,70) for k in range(6)]
    intervals=[]
    for a,b in zip(poles,poles[1:]):
        eps=(b-a)/100000
        vals=[evaluate(t,500,70) for t in [a+eps,(a+b)/2,b-eps]]
        intervals.append({'left_pole':str(a),'right_pole':str(b),'samples':vals})
    roots=[]
    for a,b in zip(poles,poles[1:]):
        low=a+(b-a)/100000;high=b-(b-a)/100000
        assert mp.mpf(evaluate(low,700,70)['P'])<-1<mp.mpf(evaluate(high,700,70)['P'])
        for _ in range(65):
            mid=(low+high)/2
            if mp.mpf(evaluate(mid,700,70)['P'])<-1:low=mid
            else:high=mid
        t=(low+high)/2;first=evaluate(t,700,70);second=evaluate(t,1400,100)
        roots.append({'t':str(t),'bracket_low':str(low),'bracket_high':str(high),
                      'P_plus_one':str(mp.mpf(second['P'])+1),
                      'hook_plus_one':str(mp.mpf(second['hook'])+1),
                      'double_terms_hook_difference':str(abs(mp.mpf(first['hook'])-mp.mpf(second['hook']))),
                      'classification':'NUMERIC root, not interval-certified'})
    return {'classification':'EXPLORATORY NUMERIC ONLY','poles':[str(t) for t in poles],
            'intervals':intervals,'P_equals_minus_one_roots':roots,'positive_control':evaluate('0.1',300,70)}

if __name__=='__main__':print(json.dumps(produce(),indent=2))
