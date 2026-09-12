"""Exact power comparison and mass allowances for the strengthened middle bound."""
import json
from fractions import Fraction as F


def produce():
    tenth=F(75,41)**10*F(2,3)**7*F(31,64)**3
    mass=F(41,50)*F(1,4)*F(3,2)*F(11,10)*F(48,329)
    claims={
        'constant_remainder_positive': F(15,4)>F(75,41),
        'bare_mass_coefficient':tenth>F(11,10)**10,
        'subwindow_mass':mass>F(6,125),
        'middle_phase_margin':F(15,4)*F(6,125)==F(9,50),
    }
    if not all(claims.values()):
        raise ArithmeticError('strengthened middle allowance failed')
    return {'status':'pass','claims':claims,
            'coefficient_tenth_power':str(tenth),'subwindow_mass_lower':str(mass),
            'middle_phase_upper_allowance':'-9/50',
            'scope':'arithmetic only; power-sum lower bound and inherited analytic lemmas separate'}


if __name__=='__main__':
    print(json.dumps(produce(),indent=2,sort_keys=True))
