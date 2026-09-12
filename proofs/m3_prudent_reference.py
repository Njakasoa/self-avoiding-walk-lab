"""Direct small NE-prudent ramp/hook enumeration, independent of kernel formulas."""
from collections import Counter

def counts(max_n=12):
    p=[0]*(max_n+1);hook=[0]*(max_n+1)
    path=[(0,0)];directions=[(1,0),(0,1),(-1,0),(0,-1)]
    def visit(xmax,ymax):
        depth=len(path)-1;x,y=path[-1]
        if depth and x==xmax and y==ymax:
            p[depth]+=1
            k=1
            while k+1<len(path) and path[k+1]==(path[k][0]-1,path[k][1]):k+=1
            if k>1 and k<depth and all(q[1]>1 for q in path[k+1:]):hook[depth]+=1
        if depth==max_n:return
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if ny<=0:continue
            # Prudent: no previously visited site on the whole forward ray.
            if any((a==x and (b-y)*dy>0) if dy else (b==y and (a-x)*dx>0) for a,b in path):continue
            xx,yy=max(xmax,nx),max(ymax,ny)
            if nx!=xx and ny!=yy:continue
            path.append((nx,ny));visit(xx,yy);path.pop()
    visit(0,0)
    return {'ramp_counts':p,'hook_counts':hook,'max_n':max_n}

if __name__=='__main__':
    import json
    print(json.dumps(counts()))
