"""Rational identities locating actual W poles rather than cancelled J poles."""
import json
import sympy as sp


def produce():
    P,H,di,t = sp.symbols('P H di t')
    J = (P-H)/(1+P)
    irreducible = 4*J-2*di-t
    F = (3-t-2*di)*P-4*H-(1+t+2*di)
    checks = {
        'I_minus_one_numerator': sp.cancel((irreducible-1)*(1+P)-F),
        'W_quotient_identity': sp.cancel(irreducible/(1-irreducible)+1+(1+P)/F),
        'critical_F_specialization': sp.expand(F.subs(di,1)-((1-t)*P-4*H-(3+t)))
    }
    for name,value in checks.items():
        if value != 0:
            raise ArithmeticError(f'Failed symbolic identity: {name}')
    return {'classification': 'EXACT RATIONAL IDENTITIES',
            'checks': {name: True for name in checks}, 'F': str(F)}


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2, sort_keys=True))
