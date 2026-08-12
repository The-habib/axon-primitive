# Critical Identity Definitions & Taxonomy (semantic-identity/DEFINITIONS.md)

## 1. Five-Level Identity Taxonomy

| Identity Level | Technical Question Answered | Hashing Formula | System Example |
| :--- | :--- | :--- | :--- |
| **1. Content Identity** | "Are these raw payload bytes 100% identical?" | $H_{\text{content}} = \text{SHA256}(\text{Data})$ | Git Blob, IPFS Block |
| **2. Structural Identity** | "Do these objects share the same layout/schema?" | $H_{\text{type}} = \text{SHA256}(\text{Schema})$ | Protobuf Descriptor |
| **3. Behavioral Identity** | "Do these routines yield identical outputs for all inputs?" | Observational Equivalence ($\sim_{\text{obs}}$) | Program Equivalence (Undecidable) |
| **4. Contract Identity** | "Do these objects carry identical boolean invariants?" | $H_{\text{contract}} = \text{SHA256}(\text{Predicates})$ | Eiffel Invariant Signature |
| **5. Semantic Identity** | "Do these objects represent identical data bound to identical contracts?" | $H_{\text{semantic}} = \text{SHA256}(H_{\text{content}} \mathbin{\Vert} H_{\text{contract}})$ | **Semantic Object Identity** |

---

## 2. Simplest Experiment: Disambiguating Data vs Contract Identity

Consider two computational objects:
- **Object A**: Data $= \{x: 100\}$, Contract $= (x \ge 0)$.
- **Object B**: Data $= \{x: 100\}$, Contract $= (x \ge 50)$.

### Evaluation Across Identity Levels:
- **Content Identity Level**: $H_{\text{content}}(A) == H_{\text{content}}(B)$ (**MATCH** — Both payloads are $\{x: 100\}$).
- **Contract Identity Level**: $H_{\text{contract}}(A) \ne H_{\text{contract}}(B)$ (**MISMATCH** — $x \ge 0$ vs $x \ge 50$).
- **Semantic Identity Level**: $H_{\text{semantic}}(A) \ne H_{\text{semantic}}(B)$ (**MISMATCH** — Distinct semantic objects).
- **Subsumption Lattice Level**: Contract B refines Contract A ($C_B \sqsubseteq C_A$), meaning $B$ is a **valid semantic refinement** of $A$.

This proves that **Semantic Identity** is a distinct, hierarchical identity model.
