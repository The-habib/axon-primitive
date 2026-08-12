# AXON 1.0 Core Model Specification (docs/AXON_CORE_MODEL.md)

## 1. The 6-Component Computational Object

An **AXON 1.0 Computational Object** is defined as the 6-tuple:
$$\mathcal{A} = \langle D, \mathcal{S}, \mathcal{C}, I, T, \mathcal{L} \rangle$$

Where:
1. **Data Payload ($D$)**: Canonical UTF-8 JSON data stream.
2. **Type Schema ($\mathcal{S}$)**: Structural type constraints (`number`, `string`, `boolean`, `array`, `object`).
3. **Constraint Set ($\mathcal{C}$)**: List of deterministic boolean expressions written in AXON Predicate Language.
4. **Identity Hierarchy ($I$)**: Cryptographic identity tuple $\langle H_{\text{content}}, H_{\text{contract}}, H_{\text{semantic}} \rangle$.
5. **Transformation ($T$)**: State transition function $T : \mathcal{A}_{\text{in}} \to \mathcal{A}_{\text{out}}$.
6. **Lineage Graph ($\mathcal{L}$)**: Directed acyclic graph edges linking parent semantic hashes.

---

## 2. Cryptographic Identity Hierarchy

- **Content Identity ($H_{\text{content}}$)**:
  $$H_{\text{content}} = \text{SHA256}(\text{Canonicalize}(D))$$
- **Contract Identity ($H_{\text{contract}}$)**:
  $$H_{\text{contract}} = \text{SHA256}(\text{Canonicalize}(\mathcal{S}) \mathbin{\Vert} \text{Canonicalize}(\mathcal{C}))$$
- **Semantic Identity ($H_{\text{semantic}}$)**:
  $$H_{\text{semantic}} = \text{SHA256}(H_{\text{content}} \mathbin{\Vert} H_{\text{contract}} \mathbin{\Vert} H_{\text{parent\_semantic}})$$

---

## 3. 4-State Verification System

Verification returns a discrete 4-state result:
- **`TRUE`**: Content hash matches AND all invariants evaluate to boolean `true`.
- **`FALSE`**: Content hash tampered OR any invariant evaluates to boolean `false`.
- **`UNKNOWN`**: Evaluation depends on missing or un-evaluated variable bindings.
- **`UNVERIFIED`**: Signature proof missing or cryptographic signature invalid.
