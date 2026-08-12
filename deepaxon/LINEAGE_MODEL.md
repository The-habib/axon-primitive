# Lineage & Guarantee Propagation Model (deepaxon/LINEAGE_MODEL.md)

## 1. Lineage Chain Propagation
For a transformation lineage sequence $A \to B \to C \to D$:
- At step $A$: Invariant $\mathcal{C}_A = (x > 0)$ attached.
- At step $B = T_1(A)$: $T_1(x) = x + 5 \implies \mathcal{C}_B = (x' > 5)$ (Valid, inherited).
- At step $C = T_2(B)$: $T_2(x') = x' \times 2 \implies \mathcal{C}_C = (x'' > 10)$ (Valid, inherited).
- At step $D = T_3(C)$: $T_3(x'') = x'' - 20 \implies \mathcal{C}_D = (x''' > -10)$ (Weakened guarantee).

---

## 2. Theoretical Mapping
Semantic guarantee propagation across execution lineages directly maps to **Proof-Carrying Data (Chiesa et al. 2013)** and **Data Lineage Provenance Systems**.
