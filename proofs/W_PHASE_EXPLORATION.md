# Weakly prudent bridge quotient: finite phase exploration

Status: **FINITE NUMERICAL FALSIFICATION ONLY**. This note records bounded
numerical evidence for the weakly prudent bridge denominator. It is not a proof
that $W$ is non-D-finite, and it does not certify an infinite sum, a tail, a
phase limit, or an all-index sign.

The Bacher--Beaton identities used here are Proposition 8 and equations (1)--(3)
of the 2014 paper, transcribed in `references/bacher-beaton-2014.txt`:

$$
W=I/(1-I),\qquad I=4J-2D_I-t,\qquad J=(P-H)/(1+P),\qquad D_I=D/(1+D).
$$

The directed-ramp series is

$$
D=\sum_{k\ge0} t^{k+1}/G_k,
$$

with $G_{-1}=1$, $G_0=1-t$, and
$G_k=(1-t+t^2+t^3)G_{k-1}-t^2G_{k-2}$. Clearing $1+P$ gives

$$
F=(I-1)(1+P)=(3-t-2D_I)P-4H-(1+t+2D_I).
$$

The probe also reports the diagnostic obtained after substituting the limiting
value $D_I=1$:

$$
F_{D_I=1}=(1-t)P-4H-(3+t),\qquad
F-F_{D_I=1}=2(1-D_I)(P+1).
$$

The diagnostic is useful for the phase limit, but it is not the finite
denominator test. At the tested indices $D_I$ is still only about $0.912$ to
$0.939$.

## Independent probe

`experiments/w_phase_probe.py` directly implements the Bacher--Beaton kernel
branch $U$, the $P,H$ summands, and the $G_k$ recurrence. The phase parameter
solves

$$
a(t)=N+\theta,\qquad a(t)=\log(v(t))/\log(q(t)^2),
$$

using $q=U(t,1)$ and the same $v(t)$ coordinate as the M3 phase probe. The
tested phases lie above $\eta=1/\sqrt{2}$, where the formal Gamma connection
factor $A\sin(\pi\theta)/\sin(\pi(\eta-\theta))$ is negative.

The root integration receipts are the exploratory full sweep
`results/w-phase-v1/` and the finer run `results/w-phase-fine-v1/`. They were
run with 90 decimal digits and a cooperative 180-second budget. The prudent
summand schedule uses a base of `max(2000, ceil(12/epsilon))`, doubled for the
stability comparison, with `epsilon=-log(q^2)`. The $D$ recurrence stops when
its final term is below $10^{-55}$ times the current sum.

The recorded `doubling_drift` values are computed after serialization to 32
significant decimal characters. A displayed zero means agreement at that
serialized precision, not exact agreement at the full 90-digit working
precision. The runtime limit is cooperative: deadline checks occur between
subcomputations and do not forcibly interrupt a nested evaluation.

## Exploratory full sweep

Receipt command:

```text
.venv/bin/python -m experiments.w_research_batch phase w-phase-v1
```

Parameters are $N=8,16,32,64$ and
$\theta\in\{0.75,0.80,0.85,0.87,0.90\}$. The producer took 36.6328 seconds
and generated 20 cases. The final rows are:

| $N$ | $\theta$ | $D_I$ | $P+1$ | $F$ | $F_{D_I=1}$ | $I-1$ |
|---:|---:|---:|---:|---:|---:|---:|
| 8  | 0.75 | 0.911818 | -15.6455 | +1.00467 | +3.76397 | -0.064215 |
| 8  | 0.80 | 0.911929 | -7.48890 | -0.273335 | +1.04577 | +0.036499 |
| 8  | 0.85 | 0.912040 | -4.96568 | -0.668554 | +0.205014 | +0.134635 |
| 8  | 0.87 | 0.912083 | -4.37078 | -0.761716 | +0.006812 | +0.174275 |
| 8  | 0.90 | 0.912149 | -3.69147 | -0.868085 | -0.219486 | +0.235160 |
| 16 | 0.75 | 0.922811 | -15.4857 | +1.33477 | +3.72541 | -0.086194 |
| 16 | 0.80 | 0.922855 | -7.41583 | -0.108665 | +1.03552 | +0.014653 |
| 16 | 0.85 | 0.922899 | -4.91816 | -0.555377 | +0.203017 | +0.112924 |
| 16 | 0.87 | 0.922916 | -4.32918 | -0.660710 | +0.006712 | +0.152618 |
| 16 | 0.90 | 0.922942 | -3.65661 | -0.780994 | -0.217452 | +0.213584 |
| 32 | 0.75 | 0.931503 | -15.4031 | +1.59536 | +3.70550 | -0.103574 |
| 32 | 0.80 | 0.931520 | -7.37718 | +0.019735 | +1.03011 | -0.002675 |
| 32 | 0.85 | 0.931537 | -4.89277 | -0.467984 | +0.201959 | +0.095648 |
| 32 | 0.87 | 0.931544 | -4.30690 | -0.582997 | +0.006666 | +0.135363 |
| 32 | 0.90 | 0.931555 | -3.63786 | -0.714337 | -0.216349 | +0.196362 |
| 64 | 0.75 | 0.938490 | -15.3607 | +1.80563 | +3.69529 | -0.117549 |
| 64 | 0.80 | 0.938497 | -7.35710 | +0.122345 | +1.02730 | -0.016630 |
| 64 | 0.85 | 0.938505 | -4.87952 | -0.398728 | +0.201409 | +0.081715 |
| 64 | 0.87 | 0.938507 | -4.29526 | -0.521607 | +0.006645 | +0.121438 |
| 64 | 0.90 | 0.938512 | -3.62804 | -0.661933 | -0.215769 | +0.182449 |

At $\theta=0.80$, literal $F$ changes from negative at $N=8,16$ to positive
at $N=32,64$. At $\theta=0.90$, it remains negative. The $D_I=1$ diagnostic
is positive at 0.80 and negative at 0.90 for every tested $N$, with a crossing
near 0.87. The finite correction is therefore material and must be controlled
in any analytic transfer.

## Finer run

Receipt command:

```text
.venv/bin/python -m experiments.w_research_batch phase-fine w-phase-fine-v1
```

This run used $N=32,64$ and phases
$0.84,0.85,0.86,0.87,0.88,0.89,0.90$. At $N=64$, the literal $F$ values in
increasing phase order were

$$
-0.32449,-0.39873,-0.46387,-0.52161,-0.57322,-0.61973,-0.66193.
$$

Thus the finite-$D_I$ values stay negative throughout this finer window at
these indices, even though the $D_I=1$ diagnostic crosses near 0.87. This is a
finite convergence observation only.

## Provenance

Both receipts were made at commit
`9a63181dc11100fa4dfccdea510650976383ffb3` with a dirty worktree. The key
hashes recorded in their metadata are:

| input/output | SHA-256 |
|---|---|
| `experiments/w_phase_probe.py` | `1065ef70ccba30603ea6ee0e0bff7c957b0f3d6a6edee83dde9ada0f90197211` |
| `experiments/w_research_batch.py` | `2647d41a37b4575a6728d38b2faf237f5c67b5bacf9a82060ed663456eceb5b1` |
| `papers/bacher-beaton-2014.pdf` | `04205e9fafa5330cb518e4c22a3db6f5677cddc915342fae83acbe076039b2c0` |
| `proofs/M3_NON_DFINITE_CANDIDATE.md` | `e184726e834116e8eaf9d83926e571f40f4f2883eda1114b05c231872ec0a627` |
| `proofs/W_DIRECTED_RAMPS.md` | `35414207069e48a40c9d4d27cef0eb9c139a211a2a0185ea6480e91dc2cc2b61` |
| `proofs/W_NON_DFINITE.md` | `351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a` |
| `results/w-phase-v1/payload.json` | `fd304ce9c064561c3de61779d68e415079f01906923ec3490af01a78e5894ef6` |
| `results/w-phase-fine-v1/payload.json` | `5ff35381d8d1014e1169eaff3ef26772acd9dcf6239a1b98cb8ac8fa0dbfa73d` |

No finite check here establishes a uniform sign, an infinite zero family, or
non-D-finiteness of $W$. The receipts are exploratory inputs for independent
analytic and interval work.
