"""Explore symbolic H/V partition stability and a naive isotropic orientation lift."""
import json,sys
from collections import Counter,defaultdict
from fractions import Fraction
from src.discovery_memory import build_memory
from src.equitable import equitable_partition,quotient,verify_equitable

def produce(memories=(3,5,7,9,11,12)):
    def normalized(mapping):
        labels={}
        return [labels.setdefault(k,len(labels)) for k in mapping]
    result=[]
    for m in memories:
        model=build_memory(m,weights=[3,1,3,1]);base=model['rows']
        hv=[{j:divmod(int(w),3) for j,w in row.items()} for row in base]
        assert all(sum(h for h,v in row.values())<=2 and sum(v for h,v in row.values())<=2 for row in hv)
        memberships={};sizes={}
        for x in [Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)]:
            rows=[{j:x*h+v for j,(h,v) in row.items()} for row in hv]
            p=equitable_partition(rows);q=quotient(rows,p);assert verify_equitable(rows,p,q)
            memberships[str(x)]=p;sizes[str(x)]=len(q)
        iso=memberships['1'];generic=memberships['3']
        groups=defaultdict(set);liftgroups=defaultdict(list)
        for i,(a,b) in enumerate(zip(iso,generic)):
            groups[a].add(b)
            state=model['states'][i];axis=int(state[-1][0]==state[-2][0])
            liftgroups[(a,axis)].append(i)
        witness=None
        for (iso_class,axis),indices in liftgroups.items():
            first=indices[0]
            other=next((j for j in indices if generic[j]!=generic[first]),None)
            if other is not None:
                witness={'isotropic_class':iso_class,'last_axis':axis,
                         'first_path':model['states'][first],'second_path':model['states'][other],
                         'first_HV_out_counts':[sum(p[k] for p in hv[first].values()) for k in [0,1]],
                         'second_HV_out_counts':[sum(p[k] for p in hv[other].values()) for k in [0,1]]}
                break
        result.append({'memory':m,'D2_states':len(base),'partition_sizes':sizes,
                       'generic_blocks_per_isotropic_block':dict(Counter(map(len,groups.values()))),
                       'isotropic_plus_last_axis_suffices':witness is None,'counterexample':witness,
                       'exceptional_ratios_differ_from_generic':{
                           x:normalized(memberships[x])!=normalized(generic) for x in ['1/2','2']}})
    return {'classification':'EXACT FINITE EXPLORATION; novelty unestablished','cases':result,
            'possible_exceptional_ratios':['1/2','1','2'],
            'reason':'each destination-class signature is h*x+v with 0<=h,v<=2; outside listed slopes numeric equality forces both coefficient equalities'}

if __name__=='__main__':print(json.dumps(produce(),sort_keys=True,indent=2))
