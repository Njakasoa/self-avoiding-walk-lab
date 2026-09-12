"""Finite falsification probe of the candidate Gamma-phase limit (numerical)."""
import json
import mpmath as mp
from experiments.m3_prudent_singularity_probe import kernel,evaluate


def phase_coordinate(t):
    q=kernel(t,1);D=1-t*q;u=t/D
    v=(u-t)*(1-t*u)/(t*(1-t*t)*u)
    return mp.log(v)/mp.log(q*q)


def parameter(N,theta):
    lo=mp.mpf('.4');hi=mp.sqrt(2)-1-mp.mpf('1e-50')
    target=N+mp.mpf(theta)
    assert phase_coordinate(lo)<target<phase_coordinate(hi)
    for _ in range(230):
        mid=(lo+hi)/2
        if phase_coordinate(mid)<target:lo=mid
        else:hi=mid
    return (lo+hi)/2


def produce():
    rows=[]
    with mp.workdps(90):
        for N in (8,16,32):
            for theta in ('0.30','0.35'):
                t=parameter(N,theta)
                first=evaluate(t,3200,90);second=evaluate(t,6400,100)
                rows.append({'N':N,'theta':theta,'t':str(t),
                             'P_plus_one':str(mp.mpf(second['P'])+1),
                             'H_plus_one':str(mp.mpf(second['hook'])+1),
                             'term_doubling_difference':str(max(abs(mp.mpf(first[k])-mp.mpf(second[k])) for k in ('P','hook')))})
    return {'classification':'FINITE NUMERICAL FALSIFICATION ONLY','cases':rows}


if __name__=='__main__':print(json.dumps(produce(),indent=2))
