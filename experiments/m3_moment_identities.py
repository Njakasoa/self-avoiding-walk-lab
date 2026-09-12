"""Exact symbolic identities for the prudent noncancellation search.

The critical differential equation is a formal scaling candidate. Checking its
rational algebra does not prove convergence of the discrete products to it.
"""
import json
import sympy as s


def produce():
    t, q, u, w = s.symbols('t q u w')
    C, D, E = q-t, 1-t*q, 1-q*q
    h = lambda x: t*q-C*x
    g = lambda x: t-D*x
    f = lambda x: x/(1-t*x)
    K = C*(1-t*t)/D
    k = q*C*C/(D*D)
    rel = t*q*q-(1-t+t*t+t**3)*q+t
    checks = {}

    def check(name, expression, kernel_relation=False):
        numerator = s.fraction(s.cancel(expression))[0]
        if kernel_relation:
            numerator = s.rem(numerator, rel, q)
        assert s.expand(numerator) == 0, name
        checks[name] = True

    F = u*D-(q*C+t*E*u)*w
    Fh = D*u*u*(1-2*t*w)-(q*C-t*u*(2*q*C+t*E*u))*w*w
    A = K*F/((1-t*u)*(1-t*w)*h(u))
    Ah = t*t*K*Fh/((1-t*u)**2*(1-t*w)**2*h(u))
    B = k*g(w)/h(u)
    check('A_difference_of_first_powers', A-K*(D*f(u)-q*C*f(w))/h(u))
    check('Ah_difference_of_squares', Ah-t*t*K*(D*f(u)**2-q*C*f(w)**2)/h(u))
    for power in (1, 2):
        Y = lambda x: D*(1-t*t)*f(x)**power/g(x)
        Ap = K*(D*f(u)**power-q*C*f(w)**power)/h(u)
        check(f'coboundary_power_{power}',
              Ap-(Y(u)-B*Y(w)-t*t*E*(1-t*t)*f(u)**power/(h(u)*g(u))))
    check('kernel_CD_identity', C*D-t*q*(1-t*t), True)
    check('h_minus_kg', h(u)-k*g(u)-C*E*(1-u)/D, True)
    check('first_boundary', q*(1-t*t)/D+q*D*(1-t*t)*f(q)/g(q)-C/g(q), True)
    check('second_boundary', t*t*q*q*(1-t*t)/D**2+q*t*t*D*(1-t*t)*f(q)**2/g(q)-t*t*f(q)*C/g(q), True)
    check('zeroth_moment_constant', -q*t*t*E*(1-t*t)/(C*E/D)+t*D*D, True)
    r = q*C/D
    delta = t*t*E/C
    check('product_recurrence', k*g(u)/h(u)-r/(1+delta/g(u)))

    sigma = s.sqrt(2)-1
    d = 1-sigma
    critical_rhs = (1-u)/(sigma-d*u)*(1/(u-sigma)-sigma/(1-sigma*u)-1/u)
    partial = ((2+s.sqrt(2))/(u-sigma)+s.sqrt(2)/(u-1/sigma)
               -1/s.sqrt(2)/(u-1/s.sqrt(2))-(1+s.sqrt(2))/u)
    assert s.simplify(critical_rhs-partial) == 0
    checks['formal_critical_ODE_partial_fractions'] = True
    return {'classification': 'EXACT IDENTITIES; critical scaling limit UNPROVED',
            'checks': checks, 'kernel_relation': str(rel),
            'formal_critical_exponent': '1/sqrt(2)',
            'scope': 'No noncancellation or discrete-to-continuum convergence theorem follows from these identities alone.'}


if __name__ == '__main__':
    print(json.dumps(produce(), indent=2))
