import json,time
from fractions import Fraction as F
from proofs.m7_finite_poles import I384
from proofs.m8_finite_derivatives import evaluate_derivative
old=json.load(open('/tmp/w-fullband-N32.json')); lo,hi=map(F,old['t_bracket']);count=16; rows=[];start=time.monotonic()
for k in range(count):
 left=lo+(hi-lo)*k/count;right=lo+(hi-lo)*(k+1)/count
 row={'cell':k,'t_bracket':[str(left),str(right)]}
 try:
  r=evaluate_derivative(I384(left,right)); row['F_derivative']=r['F'].d.record();row['negative']=r['F'].d.hi<0
 except Exception as ex:row['failure']=str(ex)
 rows.append(row)
 if 'failure' in row or not row.get('negative',False):break
out={'classification':'EXPLORATORY FULL-BAND SUBDIVISION; NOT A CANONICAL CERTIFICATE','index':32,'count':count,'rows':rows,'seconds':time.monotonic()-start}
open('/tmp/w-fullband-N32-subdivision.json','w').write(json.dumps(out,indent=2)+'\n'); print(json.dumps({'completed_cells':len(rows),'last':rows[-1],'seconds':out['seconds']},indent=2))
