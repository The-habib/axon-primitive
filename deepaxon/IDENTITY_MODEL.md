# Identity Model Analysis (deepaxon/IDENTITY_MODEL.md)

## 1. Four Concepts of Identity

1. **Data Identity ($H_{\text{data}}$)**: Hashing raw canonical data bytes ($\text{SHA256}(\text{data})$).
2. **Constraint Identity ($H_{\text{rules}}$)**: Hashing invariant expression strings ($\text{SHA256}(\text{predicates})$).
3. **Program Identity ($H_{\text{prog}}$)**: Hashing transformation script logic ($\text{SHA256}(\text{transform\_code})$).
4. **Semantic Identity ($H_{\text{semantic}}$)**: Unified hash binding data, schema, invariant rules, and transformation lineage into a single Merkle leaf:
$$H_{\text{semantic}} = \text{SHA256}(H_{\text{data}} \mathbin{\Vert} H_{\text{rules}} \mathbin{\Vert} H_{\text{parent\_semantic}})$$

---

## 2. Experimental Disambiguation Matrix

| Test Case | Payload Bytes ($D$) | Invariants ($\mathcal{C}$) | $H_{\text{data}}$ | $H_{\text{rules}}$ | $H_{\text{semantic}}$ | Identity Result |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Same Data, Same Rules** | $\{ \text{val}: 100 \}$ | `val > 0` | Match | Match | Match | **IDENTICAL** |
| **Same Data, Different Rules** | $\{ \text{val}: 100 \}$ | `val > 50` | Match | Mismatch | Mismatch | **Data Same; Semantic Identity Differs** |
| **Different Data, Same Rules** | $\{ \text{val}: 200 \}$ | `val > 0` | Mismatch | Match | Mismatch | **Rules Same; Semantic Identity Differs** |
