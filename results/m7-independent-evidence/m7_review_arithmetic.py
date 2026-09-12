import sys,random,json,hashlib
from fractions import Fraction as F
sys.path.insert(0,'.')
from proofs.m7_finite_poles import I384,SCALE,interval_log,produce
rng=random.Random(72026)
def ends(a):return F(a.lo,SCALE),F(a.hi,SCALE)
def encl(a,l,h):assert ends(a)[0]<=l<=h<=ends(a)[1]
count=0
for _ in range(500):
 x=sorted([F(rng.randint(-10000,10000),rng.randint(1,1000)) for j in range(2)])
 y=sorted([F(rng.randint(-10000,10000),rng.randint(1,1000)) for j in range(2)])
 a,b=I384(*x),I384(*y); al,ah=ends(a);bl,bh=ends(b)
 encl(a+b,al+bl,ah+bh);encl(a-b,al-bh,ah-bl)
 p=[v*w for v in (al,ah) for w in (bl,bh)];encl(a*b,min(p),max(p))
 if not bl<=0<=bh:
  encl(b.reciprocal(),1/bh,1/bl)
  p=[v/w for v in (al,ah) for w in (bl,bh)];encl(a/b,min(p),max(p))
 c=I384(abs(x[0]),abs(x[0])+F(1,7)); s=c.sqrt();sl,sh=ends(s);cl,ch=ends(c)
 assert 0<=sl and sl*sl<=cl and sh*sh>=ch
 count+=1
negative=0
for fn in [lambda:I384(-1,1).reciprocal(),lambda:I384(-1).sqrt(),lambda:interval_log(I384(0)),lambda:I384(1)**-1,lambda:produce([2048]),lambda:produce([64,32])]:
 try: fn()
 except (ValueError,ArithmeticError):negative+=1
 else:raise AssertionError('negative input accepted')
# Independent log rational bound: log(1+x) lies [x-x²/2,x] for x>=0.
for x in [F(1,10**6),F(1,1000),F(1,10)]:
 a=interval_log(I384(1+x)); l,h=ends(a)
 assert l>=x-x*x/2 and h<=x
print(json.dumps({'random_interval_cases':count,'negative_inputs_rejected':negative,'log_inequality_checks':3,'status':'pass'},sort_keys=True))
