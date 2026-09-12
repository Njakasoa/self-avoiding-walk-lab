"""Small exact edge-transfer using degrees and component partitions.
All vertices retained: pedagogical connectivity TM, not width-efficient frontier TM.
"""
from collections import defaultdict

def connectivity_counts(width,height,max_n):
    for name,value,minimum in [('width',width,1),('height',height,1),('max_n',max_n,0)]:
        if type(value) is not int or value<minimum:raise ValueError(f'{name} invalid')
    size=width*height
    edges=[]
    for y in range(height):
        for x in range(width):
            u=y*width+x
            if x+1<width:edges.append((u,u+1))
            if y+1<height:edges.append((u,u+width))
    # labels -1 = unused, others canonical component labels by vertex order.
    states={(tuple([0]*size),tuple([-1]*size)):1};peak=1
    for u,v in edges:
        nxt=defaultdict(int)
        for (degrees,labels),count in states.items():
            nxt[(degrees,labels)]+=count
            if sum(degrees)//2>=max_n or degrees[u]>= (1 if u==0 else 2) or degrees[v]>= (1 if v==0 else 2):continue
            if labels[u]>=0 and labels[u]==labels[v]:continue # cycle
            ds=list(degrees);ds[u]+=1;ds[v]+=1
            ls=list(labels);a,b=ls[u],ls[v]
            if a<0 and b<0:ls[u]=ls[v]=size
            elif a<0:ls[u]=b
            elif b<0:ls[v]=a
            else:ls=[a if q==b else q for q in ls]
            mapping={};canonical=[]
            for q in ls:
                if q<0:canonical.append(-1)
                else:
                    if q not in mapping:mapping[q]=len(mapping)
                    canonical.append(mapping[q])
            nxt[(tuple(ds),tuple(canonical))]+=count
        states=nxt;peak=max(peak,len(states))
    result=[0]*(max_n+1);result[0]=1
    for (degrees,labels),count in states.items():
        if degrees[0]!=1 or degrees.count(1)!=2:continue
        if len({q for q in labels if q>=0})!=1:continue
        result[sum(degrees)//2]+=count
    return {'counts':result,'peak_states':peak,'edge_count':len(edges),
            'state_representation':'all-vertex degrees and canonical component partition'}
