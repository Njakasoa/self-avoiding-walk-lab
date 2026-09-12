# Exploratory whole-band interval checks

These are development diagnostics, not source-frozen or independently
reviewed certificates. They do not change the six-bracket M8 scope.

For N=32, exact point interval phase evaluations and rational bisection
construct outer t endpoints for phase[.8,.9]. A whole-interval derivative
evaluation fails the pre-tail g+delta exclusion because of interval width.
The first of16 uniform subdivisions completes but its derivative enclosure
contains both signs. Neither failure is a mathematical counterexample.

The first of128 subdivisions completes with a strictly negative derivative.
The full128-cell run subsequently completed in531.284seconds with every
derivative upper endpoint negative. The retained output is
w-fullband-N32-full-128.json; its adjacent rational intervals have no gaps.
This successful exploratory scan is still not an accepted certificate.
The scripts are retained as executed, including their /tmp
input/output paths; their headers explicitly identify exploratory scope.

The next obligation is to turn this into a portable
source-frozen producer, retain endpoint phase/source exclusions and every
cell enclosure, and independently audit coverage of the complete band.
Even that would cover only N=32 and would not bridge the remaining indices.
