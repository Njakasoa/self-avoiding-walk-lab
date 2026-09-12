# Finite H/V partition strata and a failed orientation shortcut

Status: exact elementary observation and finite exploration; novelty unresolved.
This is supporting evidence, not an accepted M3 contribution.

Use a fixed D2 state space, with horizontal edge weight x>0 and vertical edge
weight 1. For any current partition and any target block, an outgoing signature
is h*x+v with integers 0<=h,v<=2: a square-lattice vertex has at most two edges
on each axis. Two signatures differ by a*x+b with integers |a|,|b|<=2.
Unless both coefficients vanish, a positive zero can only be 1/2, 1, or 2.
Thus, at every refinement iteration and every x outside that exceptional set,
numeric equality of signatures is exactly coefficientwise equality. Induction
from the one-block partition proves that the coarsest outgoing equitable
partition is constant on all positive nonexceptional x, including across the
intervals separated by the exceptional set. Evaluating at x=3 realizes that
symbolic partition exactly. This does not assert that each exception actually
changes the partition.

The probe reconstructs H/V multiplicities on the fixed D2 graph from weights
3 and 1. A destination has vertical multiplicity at most two, so divmod(w,3)
recovers its horizontal and vertical counts without ambiguity. The script
checks the resulting degree bounds, performs exact Fraction refinement, and
compares normalized memberships (raw partition label numbers have no meaning).

For memories 3,5,7,9,11,12, generic class counts are respectively
6,22,93,413,1968,1918, while isotropic counts are 3,11,47,207,983,958.
Neither x=1/2 nor x=2 changes the generic partition in these finite cases.
Canonical replay is required before using these values as frozen evidence.

The tempting shortcut 'isotropic class plus last step axis' is false. It first
fails at memory 9 among the tested memories. Two paths in the same isotropic
class and both ending in a horizontal step are:

    (0,0),(-1,0),(-2,0),(-2,-1),(-2,-2),(-1,-2),(0,-2),(1,-2),(1,-1),(0,-1)
    (0,0),(-1,0),(-1,-1),(-1,-2),(-1,-3),(0,-3),(1,-3),(1,-2),(1,-1),(0,-1)

The first has one horizontal legal outgoing edge; the second has one vertical
legal outgoing edge. Their next-step weighted continuation totals are x and 1.
This is an explicit counterexample to the shortcut, independent of numerical
Perron approximations. It is not evidence of a new connective-constant bound.
