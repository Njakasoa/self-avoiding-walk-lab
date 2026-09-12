import json,time
from fractions import Fraction as F
from proofs.m7_finite_poles import I384,SEEDS,phase_data,SCALE
from proofs.m8_finite_derivatives import evaluate_derivative

def phase_edge(N,theta):
 seed=F(SEEDS[N]); lo=seed-F(1,10**7); hi=seed+F(1,10**7)
 target=N+F(theta)
 def box(t):return phase_data(I384(t))['a']
 if not F(box(lo).hi,SCALE)<target<F(box(hi).lo,SCALE):raise ArithmeticError('seed bracket')
 for _ in range(80):
  mid=(lo+hi)/2; b=box(mid)
  if F(b.hi,SCALE)<target:lo=mid
  elif F(b.lo,SCALE)>target:hi=mid
  else:raise ArithmeticError('phase precision')
 return lo,hi
start=time.monotonic(); N=32
left=phase_edge(N,'4/5');right=phase_edge(N,'9/10')
T=I384(left[0],right[1]);out={'index':N,'t_bracket':[str(left[0]),str(right[1])], 'classification':'EXPLORATORY FULL-BAND INTERVAL EVALUATION; NOT YET REVIEWED'}
try:
 r=evaluate_derivative(T)
 out['F']=r['F'].record();out['P']=r['P'].record();out['derivative_negative']=r['F'].d.hi<0
except Exception as ex:out['failure']=str(ex)
out['seconds']=time.monotonic()-start
open('/tmp/w-fullband-N32.json','w').write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
