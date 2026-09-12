from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
q=Q(15,22); M=10**8+100; E=Q(5656,10**9); m=92
# Sum derivative tail with a recurrence independent of closed-form producer.
k=m+1
s0=1/(1-q); s1=q*s0*s0; s2=q*(1+q)*s0**3
A=2*M*q**k*s0
B=40*M*q**k*(k*k*s0+2*k*s1+s2)
der=20*m*m*(E+A)+B
assert der<Q(1033,1000)
assert -6+4*der+Q(3,5)+Q(18,10**114)+Q(480000,10**57)<-1
assert Q(35,10)*Q(149,1000)**3/(Q(17,10)*34)>Q(1,6000)
assert 8*Q(11,10)*Q(17,100)**3<Q(1,20)
assert Q(75,10)*Q(37,10000)/Q(27,5)<Q(6,1000)
assert Q(18,10)*Q(37,10000)+Q(16*10**6,10**57)<1
assert Q(75,8)+Q(8,7*10**57)<10
# Exact finite telescoping tests, including sign-changing products.
for a,b in [(Q(17,5),Q(23,10)),(Q(3,2),Q(7,3))]:
 t=Q(1); prev=-(b+1)/(1-a+b)
 for n in range(20):
  cur=(n-a)*t/(1-a+b)
  assert cur-prev==t
  prev=cur;t*= (a-n)/(b-n)
print(json.dumps({'derivative_bound_decimal_summary':float(der),'checks':'pass','classification':'exact rational checks; decimal summary only'},sort_keys=True,indent=2))
