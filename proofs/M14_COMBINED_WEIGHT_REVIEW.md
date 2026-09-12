# Independent review of M14 combined-weight transfer

Status: PASS for the relative weight comparison and conditional transfer. The discrete-sum approximation and endpoint existence remain unproved.

The finite and critical parameter vectors lie in the stated independent rectangle, as do their connecting segments. The lower ratio formula uses only positive factors and the independent lower endpoints; it gives a gap above.07 even with delta=.07 (approximately.070934). The new ledger's actual delta<=.05 rectangle has still greater margin. Thus all logarithms used in the segment argument are well-defined without imposing the physical equation on artificial intermediate points.

The inherited t,u partial bounds hold on this rectangle. The t partial is positive, so its prior upper estimate is also an absolute bound. The h estimate bounds the exact logarithmic V1 derivative by2t_h/(1-t_h*h_h)+1/(1-h_h) and the absolute R_h by2/(1-t_h*h_h)^2; it uses u<=1 throughout and is not restricted to the tail-only small-u box. The C derivative is exactly-1/C, and the declared lower C endpoint proves its absolute bound2. Holding the actual delta fixed removes any directed derivative term from this comparison.

The scalar differences follow by integration of the inherited derivative bounds to the critical endpoint; the new uniform kernel displacement applies at every s, including0. Integrating the log gradient consequently gives (22.02+25e)e. Since J increases in t and (1-exp(-e))/e<1, the normalized prefactor is below1; its absolute logarithm is bounded by the sum of the two nonnegative log losses. The inequality-log(1-z)<=z/(1-z) with z=e/2 yields the displayed prefactor bound. Combined with the weight allowance, the positive exponential series bound exp(x)<=1/(1-x) gives relative error at most391/50809<1/125 on the specified e domain.

The two sums are positive and finite. Their pointwise ratio comparison proves|S_e-Stilde_e|<(1/125)Stilde_e after summation, retaining the same exact T_n,K_n and the same delta. No approximation to either Gamma factors or the smooth product has been inserted at this step.

At criticality B1=sigma-1 and sigma^2 B2=-3sigma^2, so B00=-(1-sigma)^2+12sigma^2-3-sigma and B(0,delta)=B00+2delta*sigma. Subtracting this from Fhat gives S0(delta). Its delta slope is2[(1+P0)-sigma]<0 at both endpoints. Thus the delta=0 values are valid upper bounds, and the frozen critical interval data enclose both below3. Positivity independently follows from the positive critical integral and the rectangular weight gap.

Under the expressly missing hypothesis|Stilde_e-S0(delta)|<1/8, Stilde_e<3+1/8. The resulting sum error is strictly below(3+1/8)/125+1/8=3/20. The reviewed boundary partial is taken with delta fixed, exactly as required here; integration gives a boundary error below7e. Adding these yields a total error below4/25 and the stated conditional endpoint margins. This establishes a sufficient target only, not the target itself or existence on unlisted bands.

## Independent replay and approved hashes

Independently verified the frozen M5 critical receipt, then ran `.venv/bin/python -m proofs.m14_combined_weight_transfer`: all12 checks PASS. The nested endpoint producer also passed its own checks. Complete stdout SHA256: `588bcd5886f534d1ba7f68cb22501caea8cf0d756e23cc6c335eb9555d1cc1d1`.

| Path | SHA256 |
|---|---|
| proofs/M14_COMBINED_WEIGHT_TRANSFER.md | 5b091066d4778ab52b797d1133ef7f21a1d5339a8a3dd9e728263fb6f80232a1 |
| proofs/m14_combined_weight_transfer.py | ff97452b20a1f479220ba7ae643e5bd0678ac4cc2cd8a158d14f53dff86bb5de |

No material findings remain. Acceptance is conditional on the future1/8 discrete critical-weight sum estimate for integer N>=512 at the two endpoints. Remaining finite32..511 coverage is separate. A future receipt must also retain and verify the nested endpoint producer and frozen critical input dependencies.
