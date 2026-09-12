"""Exact local cancellation in Q[t]/Phi_48; not a computer proof of global theorem."""
import sys
import sympy as s
from src.provenance import run_record

def produce():
    t=s.Symbol('t');phi=s.cyclotomic_poly(48,t)
    def rem(expr):return str(s.rem(s.expand(expr),phi,t))
    # Embed t=exp(i*pi/24). Inverse powers replaced by positive residues mod48.
    mu=t**3+t**45
    pair=t**36+t**12
    triple_numerator=mu+t**21+t**27
    rows={'cyclotomic_polynomial':str(phi),'pair_remainder':rem(pair),
          'triple_numerator_remainder':rem(triple_numerator),
          'mu_polynomial_remainder':rem(mu**4-4*mu**2+2),
          'classification':'EXACT INTEGER','scope':'local scalar cancellations only',
          'embedding':'t=exp(i*pi/24); mu=2cos(pi/8)>0'}
    assert all(rows[k]=='0' for k in ['pair_remainder','triple_numerator_remainder','mu_polynomial_remainder'])
    # Exact positive radical identifies physical root, rather than just a polynomial root.
    radical=s.sqrt(2+s.sqrt(2))
    assert s.simplify(2*s.cos(s.pi/8)-radical)==0
    rows['mu_exact']=str(radical);rows['critical_fugacity']=str(1/radical)
    rows['wrong_phase_mutant_remainder']=rem(mu+t**20+t**28)
    assert rows['wrong_phase_mutant_remainder']!='0'
    return rows

if __name__=='__main__':
    eid=sys.argv[1] if len(sys.argv)>1 else 'honeycomb-control-v1'
    print(run_record(eid,f'PYTHONPATH=. .venv/bin/python experiments/honeycomb_control.py {eid}',{},
        ['experiments/honeycomb_control.py','src/provenance.py','requirements-lock.txt',
         'papers/duminil-copin-smirnov-1007.0575.pdf'],produce))
