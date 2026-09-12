# M14 candidate: sharp critical variation and uniform kernel displacement

Status: new analytic component for independent review. Accepted M3--M13
sources remain unchanged. These inequalities alone do not bound the full
moment error or prove endpoint existence.

Let sigma=sqrt(2)-1, eta=1/sqrt(2), c=s_g(0),
u_0(s)=U(sigma,exp(-s)), and m(s,a)=log M(s,a), where M is the positive
exponential secant of M11. The critical logarithmic factor is

    psi(s)=lim_(e down to0) log R_e(s)/e.

## A nonsingular expression for the critical factor

The M11 factorization is

    R_e(s)=(ug/h)*(1-u_e(s)h)/(1-u_e(s)ug)
                    *M(s,sg)/M(s,sh).

At e=0, ug=h=eta. Since t'(0)=0 and q'(0)=-1/2, direct differentiation
of ug=t/(1-tq) and h=tq/(q-t) gives ug'(0)=-1/4 and h'(0)=1/4.
Also sg'(0)=eta/2, sh'(0)=-eta/2, using the M10 even quotient
beta(0)=eta and sh(e)=sg(-e). Taking first-order differences of the
three logarithms yields, for every s>=0,

    psi(s)=-eta - u_0(s)/(2*(1-eta*u_0(s)))
                    +eta*m_a(s,c).                  (1)

This does not differentiate the critical kernel with respect to t at
s=0. The kernel occurs in a log difference whose coefficient vanishes
at e=0; its continuity as e decreases to0 suffices for this limit.
The secant definition removes the apparent singularity at s=c.
Equation(1) agrees with the accepted psi by its defining first-order
factor limit.

The probability representation of M gives -1<m_a(s,c)<0 and
m_sa(s,c)=-Var(v)<=0. Thus s -> m_a(s,c) is nonincreasing with total
variation at most1. The function u_0 decreases from1 to sigma.
For A(u)=u/[2(1-eta*u)], A is increasing, and the identities

    A(1)=1+eta, A(sigma)=1-eta

follow from eta^2=1/2 and sigma=2eta-1. Consequently(1) gives

    TV_[0,infinity)(psi) <= 2eta+eta =3eta <17/8,
    -25/8 < -(1+3eta) < psi(s) < -1.                 (2)

The lower chain uses 3eta<17/8; the two nonconstant terms in(1) have
opposite monotonicity, so the triangle inequality for variation is needed.
The result does not assume that psi itself is monotone. No derivative
bound at s=0 or cancellation of singular reciprocals is used.

## Exact rectangle allowance

For every e>0, integer n>=0 and x=ne, bounded variation gives

    |e sum_(j=0)^(n-1) psi(je)-integral_0^x psi(s)ds|
       <=e*TV_[0,x](psi)<(17/8)e.                    (3)

For n=0 both sides on the left are zero. The bound includes the complete
half-line without truncating it. It replaces the much larger variation
allowance in M9, but does not on its own replace M9's finite-e Taylor
remainder for log R_e(s).

## Uniform kernel displacement below e/2

On .414<=t<sigma, v in[0,1], put

    B=t^(-1)+t-(1-t^2)v, Delta=B^2-4,
    A_t=t^(-2)-1-2tv, c_t=1-t^2.

The subscript on A_t here labels this expression, not a derivative of A(u)
above. The accepted kernel formulas give

    U_t=U*A_t/sqrt(Delta),
    U_tv=U*[A_t*c_t*(B+sqrt(Delta))-2t*Delta]/Delta^(3/2).

The exact rational endpoint ledger gives A_t>39/10, c_t>4/5,
B>=2, Delta<41/10 and2t<83/100 throughout this box. Hence the bracket
in U_tv is strictly larger than

    (39/10)*(4/5)*2-(83/100)*(41/10)>0.               (4)

Thus U_t increases with v. Integrating U_t in the parameter from t to
sigma and taking the endpoint limit if necessary gives

    0<=U(sigma,v)-U(t,v)
       <=U(sigma,1)-U(t,1)=1-q<e/2.                  (5)

The improper integral at(sigma,1) is justified by first integrating to
T<sigma and then using continuity of U. No bounded critical t derivative
is assumed. In the physical domain e<=1/180, M5 ensures t>.414 and
q=exp(-e/2). Therefore(5) is uniform for every s>=0 and includes s=0.

## Scope

The exact arithmetic ledger is `python -m proofs.m14_critical_variation`.
The identities and variation argument require analytic review separately.
To obtain a useful moment error one still needs a sharp finite-e
normalized-factor remainder, Gamma cumulative-mass control and weight
perturbation estimates. These results do not establish that error.
