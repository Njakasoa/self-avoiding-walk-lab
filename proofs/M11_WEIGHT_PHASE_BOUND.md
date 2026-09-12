# M11 candidate: phase control of the complete regularized weight

Status: analytic component for independent review. Assume N>=32,
theta in[.8,.9], e=e_N(theta), and all the reviewed M10 scalar and
weight lemmas and M11_DIRECTED_PHASE_BOUND. No full F_N sign follows.
All partial derivatives below explicitly hold the other arguments fixed.

Set h=tq/(q-t), C=q-t, delta=delta_D, u_n=U(t,exp(-ne)). Define

    A0=Q(-z_0), Q=q t^2(1-q^2)(1-t^2),
    z_0=1/[t-(1-tq)q],
    L=V1[4t^2 R-(1-t+2delta)],
    V1=(1-tuh)/[C(1-tu)(1-th)(1-h)],
    R=h/(1-th)+u(1-h)/[(1-tu)(1-tuh)].

The M10 lower gap gives L>.07V1>0. We prove, uniformly in every
integer n>=0,

    partial_theta log[A0 L(u_n)] <11/N.             (1)

## Favorable scalar contributions

The physical kernel equation yields exactly

    t(1+q^2)-q=-qt(1-t-t^2),
    A0=t(1-t^2)(1-exp(-e))/(1-t-t^2)>0.             (2)

Write J(t)=t(1-t^2)/(1-t-t^2). On .414<t<.4143,

    0<J_t/J=1/t-2t/(1-t^2)+(1+2t)/(1-t-t^2)<7.

Positivity uses 1-3t^2>0, and the upper bound follows by dropping the
negative term and using the displayed rational endpoints. Since
-e/7<t_e<0 and exp(e)-1<2e on0<e<=1/180,

    partial_e log A0 >-e+1/(2e)>0.

Thus partial_theta log A0<0.
Also

    C_e=-q/2-t_e<0,
    h_e=q(q t_e+t^2/2)/C^2>0.

The latter sign follows from q t_e+t^2/2> -e/7+.414^2/2>0.
Therefore C_theta>0 and h_theta<0. At fixed t,u,delta,C,

    partial_h log V1=-tu/(1-tuh)+t/(1-th)+1/(1-h)>0,
    R_h=1/(1-th)^2-u/(1-tuh)^2>=0,

since 0<u<=1. Hence partial_h L>0. Moreover partial_C log L=-1/C.
The h and C contributions to partial_theta log L are both nonpositive.

## Uniform motion of the kernel point, including n=0

Put v=exp(-ne), x=ne and

    B=t^-1+t-(1-t^2)v,
    U=2/[B+sqrt(B^2-4)].

Since B(t,1)=2cosh(e/2), one has

    B-2 >= e^2/4+(1-t^2)(1-v),
    sqrt(B^2-4)>=sqrt(e^2+3(1-v)).                  (3)

Here 1-t^2>3/4. Implicit differentiation gives

    U_t=U(t^-2-1-2tv)/sqrt(B^2-4),
    U_v=U(1-t^2)/sqrt(B^2-4).

Both are positive, U<=q<1, and t^-2<6. Therefore

    U_t t_theta < (6/e)e^2/(7N)=6e/(7N).

For x>0, v_theta=n v|e_theta|<xv/N and
xv<=1-v, so (3) gives

    U_v v_theta <=xv/[N sqrt(3(1-v))]<3/(5N).

For n=0 this second term is zero; the first bound still applies because
e>0. Consequently every n>=0 satisfies

    0<u_n,theta < [6/(7*180)+3/5]/N <.61/N.         (4)

This estimate uses the positive e gap at v=1 and never differentiates
the critical square root there.

## Remaining weight derivatives

M10 proves 0<partial_u log L<16. To bound the partial t derivative,
hold h,C,u,delta fixed. Let t_h=.4143, h_h=.71, h_l=.706,
d=1-t_h, d_h=1-t_h h_h. Direct differentiation gives the upper bounds

    R <= Rmax=h_h/d_h+(1-h_l)/(d d_h),
    R_t <= Rtmax=h_h^2/d_h^2
             +(1-h_l)[1/(d^2 d_h)+h_h/(d d_h^2)],
    partial_t log V1 <=1/d+h_h/d_h,
    partial_t log L <=1/d+h_h/d_h
             +[8t_h Rmax+4t_h^2 Rtmax+1]/.07 <200.  (5)

For (5), R_t is positive, as is the derivative of 4t^2R+t-1-2delta,
so its quotient is bounded using the positive .07 gap. The possibly
negative first term in partial_t log V1 is discarded safely. All
rational inequalities are in the companion arithmetic checker.
Now t_theta<e^2/(7N), so this contribution is less than .001/N.
The M11 directed result supplies the remaining delta contribution,
which lies in[0,1.12/N).

Dropping the three favorable contributions (A0,h,C), the chain rule,
(4),(5), and the directed bound prove

    partial_theta log[A0 L(u_n)]
       < [.001+16*.61+1.12]/N =10.881/N<11/N.

## Product consequence and remaining obstacle

Write the exact M6 factorization as

    -Q z_n L(u_n)=A0 T_n K_n L(u_n),
    K_n=r^n product_(j<n) R_e(je)>0.

The secant sign proof for R_e applies here: s_g>.15 and
s_h=s_g-beta e>.15-.72/180>0; g_e is increasing and concave on
the complete half-line. This extends that sign argument to the present
domain without importing M6's small-e Taylor estimates.
The a,b values lie in the same integer strip by the M10 beta bounds,
so T_n>0 and all the displayed logarithms are defined.

For N+1<=n<=60N, the reviewed M10 bare-product result and (1) imply

    partial_theta log[A0 T_n L(u_n)]
       <-1435/342+11/N <=-1435/342+11/32<-3.85.      (6)

Thus the regularized post-crossing weight, including its prefactor and
directed parameter, already has a uniform negative margin before the
smooth factor K_n is included. Controlling partial_theta log K_n,
the pre-crossing sum, the boundary terms and the distant tail remains
necessary. Equation (6) alone proves no monotonicity of F_N.
