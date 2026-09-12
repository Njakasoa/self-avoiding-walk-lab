# M9 candidate: effective linear phase error and normalized residue rate

Status: candidate for review, conditional on the M9 linear moment and
N>=10^27 uniqueness theorems. This extends the M8 quantitative arguments
with new constants and domains; the old source files remain unchanged.

For N>=10^27 put L=logN, E(N)=10^21/N, and retain the exact M8
approximations d_hat=sigma/(L+b),

    F_hat_N(theta)=F0(theta)+2d_hat*(1+P0(theta)),
    theta_hat_N: F_hat_N(theta_hat_N)=0,
    r_hat_N=-j0*(1+P0(theta_hat_N))/F_hat_N'(theta_hat_N),
    j0=s*^2/8.

The M8 rational expression for r_hat and all its fixed inverse-logarithmic
coefficients are unchanged.

## Explicit phase and position bounds

M9_UNIQUENESS_THRESHOLD proves D>L/sigma and d_hat<sigma/L<1/125.
The proof of M8_EFFECTIVE_PHASE equation(3) uses only that directed lower
bound, the M6 directed remainder and the real phase inverse. All hold here.
It yields |delta_N-d_hat|<19/(N logN), without differentiating a remainder.
Thus

    |F_N-F_hat_N|<=4E(N)+2/N^2+285/(N logN).

The critical derivative margins give F_hat_N'<-6+150/125=-24/5.
Its left endpoint exceeds1-15/125>0; the right is negative. Its zero
therefore exists uniquely in the same band. At the unique true zero,
the real mean-value theorem proves

    |theta_N-theta_hat_N|<=R_theta(N),
    R_theta(N)=(5/24)[4E(N)+2/N^2+285/(N logN)].       (1)

The unchanged kernel expansion and phase inverse give
0<t_N'<1/(7N^3). Evaluating the full analytic kernel at theta_hat_N gives

    |w_N-t_N(theta_hat_N)|<=R_theta(N)/(7N^3).        (2)

Consequently the phase error is O(1/N), and the position error is O(1/N^4).
At N>=10^27, logN>54 gives R_theta(N)<8.34*10^-7 and the right side
of(2) below1.2*10^-7/N^3. These are rigorous allowances, not fitted errors.

## Explicit normalized residue bound

For any integer m>=1 use the M8 tails A_m,B_m with M=10^8+100, q=15/22:

    E1(N,m)=20m^2[E(N)+A_m]+B_m,
    Z(N,m)=4E1(N,m)+10/N^2+2850/(N logN)+480000/N
                                                    +1300R_theta(N),
    R_res(N,m)=.004[E(N)+75R_theta(N)]+7.5/N+.006Z(N,m).

Then

    |N^3 Res_(t=w_N)W-r_hat_N|<=R_res(N,m).           (3)

Here is the domain and constant audit of the M8 proof. The exact phase
Jacobian J_N=N^3 t_N' still satisfies |J_N-j0|<1/N and
.0028<J_N<.004: its proof requires only the M7 kernel remainder and
1.8*.0037+16*10^6/N<1, true from N>=10^27. The numerator error remains
E+75R_theta. The same-phase derivative error remains
4E1+10/N^2+2850/(N logN)+480000/N. The sole curvature change is

    |F_hat_N''|<(26+150/125)*45=1224<1300.

M9 supplies |F_N'|>3.9>1 independently of the chosen m, while
|F_hat_N'|>24/5. The quotient decomposition in M8 therefore retains
the coefficients .004 and7.5; its final coefficient is bounded by

    7.5*.0037/(24/5)=.00578125<.006.

This proves(3) for every m, including choices whose separate E1 bound
is too large to establish uniqueness on its own.

For the asymptotic rate choose m=ceil(4logN), not ceil(logN).
Since log(22/15)>1/4, q^m<=N^(-4log(22/15))=O(1/N).
The two tails and the real interpolation term consequently give

    E1(N,m)=O(log^2(N)/N),
    N^3 Res W=r_hat_N+O(log^2(N)/N).                  (4)

The M8 exact rational expression still determines every fixed logarithmic
coefficient, now with the stronger algebraic remainder(4). This remains
a fixed-order asymptotic statement, not a uniform expansion with growing
logarithmic truncation order.

Finally the fixed-degree M9 estimate gives |F_N'|<29. Combining it with
3.5<|1+P_N|<8 and .0028<J_N<.004 preserves the convenient bounds

    -1/(20N^3)<Res W<-1/(6000N^3), N>=10^27.

All statements concern the restricted W family and the stated phase bands.
They do not fill the gap between the accessible finite certificates and N=10^27.
