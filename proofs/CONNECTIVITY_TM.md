# Connectivity-state edge transfer: bounded finite-grid comparison

For a rectangle with a distinguished corner root, process each undirected edge
once with two choices: excluded or included. State records every vertex's degree
and the partition into connected components of included edges. Unused vertices
carry label -1. Reject degree>2, root degree>1, and every edge within a component
(cycle). Include multiplicities when different partial edge sets merge.

Invariant: all retained partial graphs are disjoint unions of simple paths.
The canonical component labels and degrees determine all future legal edge
choices. At termination accept exactly one nonempty connected component, root
degree1, and exactly two degree1 vertices. Add the zero-step path separately.
An accepted edge set is a simple path rooted at one endpoint, with a unique
traversal direction. Hence it contributes exactly one rooted oriented SAW.
Reversal is not an extra factor because the distinguished root is fixed.

This is a connectivity-state transfer matrix but retains all vertices, including
those behind the cut. It compares independently with length-transfer occupation
states in src/transfer_matrix.py. It is NOT the compressed frontier TM of Jensen
and has no competitive asymptotic complexity. A future sweep may forget closed
vertices only with a proof that no detached component can be accepted later.
No finite rectangle rate is identified with an infinite-strip connective constant.
Topological TM uses sector topology and numerical infinite-width extrapolation;
M1 studies its literature but does not implement that record-scale method.
