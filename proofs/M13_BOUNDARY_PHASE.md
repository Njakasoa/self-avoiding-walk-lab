# M13 candidate: a uniform upper bound for the W boundary derivative

Status: component lemma for independent review; not a full F derivative
or existence theorem. Use N>=32, theta in[.8,.9] and e=e_N(theta).

The exact decomposition from M12 is

    F=B+sum_(n>=0) A0 T_n K_n L_W(u_n),
    B=(1-t+2delta_D)B1-4t^2 B2-(3+t)+2delta_D.

The definitions of B1 and B2 are those of M12_UNIFORM_NONCANCELLATION.
Treat B as a function B(e,delta), with delta independent for its partial
e derivative. The M10/M11/M12 bounds give

    sigma-1/(8*180^2)<=t<=sigma, 359/360<=q<=1,
    -1/(7*180)<=t_e<=0, q_e=-q/2,
    0<=delta<=.07, 1+B1>0.

These boxes contain every physical parameter pair and derivative; e>0
itself is still required for the phase inverse. The first derivative jets
in m13_boundary_bounds.py use e as their independent variable and give
delta the zero derivative, computing precisely B_e with delta held fixed.
The class name Jet384 imposes no choice of differentiation variable.

The exact I384/Jet384 calculation proves on this whole box

    -2<B<-7/5,
    -7<B_e<0.                                            (1)

The retained derivative interval is approximately[-6.62157,-3.78401];
these readable numbers are not substitutes for the exact dyadic endpoints.
The proof uses no phase scan and no differentiated asymptotic remainder.

The real directed monotonicity and phase inverse give delta_D,theta<=0,
e_theta<0 and |e_theta|<e/N. The chain rule therefore yields

    B_theta=B_e e_theta+2(1+B1)delta_D,theta
           <=B_e e_theta<7e/N
           <119/(100N^2)<6/(5N^2).                      (2)

The positive sign of 1+B1 is indispensable to dropping the directed
contribution. Taking its absolute value would lose this improvement.
Equation(2) bounds only the boundary term. Combining it with pre-crossing,
middle and distant-tail estimates remains necessary for F_theta<0.

The producer checks all needed denominators and returns exact value and
derivative intervals, with an optimization guard. Run
`python -m proofs.m13_boundary_bounds` without optimization.
