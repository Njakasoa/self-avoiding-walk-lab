"""Exact symbolic and rational checks for M8 residue and primitive identities."""
from fractions import Fraction as F
import json
import sympy as sp


def produce():
    checks = {}

    def zero(name, expression):
        if sp.cancel(expression) != 0:
            raise ArithmeticError(name)
        checks[name] = True

    C, J, p, z, A, c, delta, kappa, j0, sigma = sp.symbols(
        'C J p z A c delta kappa j0 sigma')
    B = -(C+2*delta*p)/(J+2*delta*z)
    Q = B**2+2*A*c*B+A**2
    original = -j0*(p+z*B)/((J+2*delta*z)*kappa*Q)
    D = (C+2*delta*p)**2-2*A*c*(C+2*delta*p)*(J+2*delta*z)+A**2*(J+2*delta*z)**2
    closed = -j0*(p*J-z*C)/(kappa*D)
    zero('phase_eliminated_residue_identity', original-closed)
    D0 = D.subs(delta,0)
    alpha = sp.diff(D,delta).subs(delta,0)/D0
    B0 = -C/J
    Q0 = B0**2+2*A*c*B0+A**2
    C1 = 2*sigma*(p+z*B0)/(J*kappa*Q0)
    first_factor = C1*2*kappa*(B0+A*c)-4*sigma*z/J
    zero('first_log_coefficient_agrees', first_factor+alpha*sigma)
    x, b, al, be = sp.symbols('x b alpha beta')
    a1 = 2*b+al*sigma
    a2 = b*b+al*sigma*b+be*sigma*sigma
    coeff = [sp.Integer(1), -al*sigma]
    coeff.append(b*b-a1*coeff[1]-a2)
    for _ in range(3,8):
        coeff.append(sp.expand(-a1*coeff[-1]-a2*coeff[-2]))
    residual = sp.Poly(sp.expand((1+a1*x+a2*x*x)*sum(v*x**i for i,v in enumerate(coeff))-(1+b*x)**2),x)
    for i in range(8):
        zero(f'logarithmic_recurrence_order_{i}', residual.nth(i))
    a, beta, n, T = sp.symbols('a beta n T')
    bbare = a-beta
    Tnext = (a-n)/(bbare-n)*T
    zero('bare_product_primitive_step', (n+1-a)*Tnext-(n-a)*T-(1-beta)*Tnext)
    zero('bare_product_primitive_initial', (-a+bbare+1)/(1-beta)-1)
    for index,(aa,bb) in enumerate([(F(43,5),F(79,10)),(F(164,5),F(321,10)),(F(7,5),F(4,5))]):
        beta_r=aa-bb; t=F(1); terms=[]; primitives=[]
        for nn in range(80):
            terms.append(t);primitives.append((nn-aa)*t/(1-beta_r))
            t=t*(aa-nn)/(bb-nn)
        weights=[F(7,8)**nn/(nn+1) for nn in range(80)]
        lhs=sum(t*w for t,w in zip(terms,weights))
        rhs=primitives[-1]*weights[-1]+(bb+1)*weights[0]/(1-beta_r)+sum(primitives[nn]*(weights[nn]-weights[nn+1]) for nn in range(79))
        if lhs != rhs:
            raise ArithmeticError('weighted summation identity')
        checks[f'weighted_primitive_case_{index}']=True
    return {'status':'pass', 'classification':'EXACT ALGEBRA; asymptotic and analytic arguments separate', 'checks':checks}


if __name__ == '__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
