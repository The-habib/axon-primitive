# DEEPAXON Phase 3 & 4 — Theory & Literature Mapping (deepaxon/PRIOR_ART.md)

## 1. Programming-Language Theory Search (1960–2026)

### 1. Hoare Logic & Design by Contract (Hoare 1969, Meyer 1988)
- **Concept**: $\{ P \} C \{ Q \}$ where precondition $P$ holds before command $C$, guaranteeing postcondition $Q$.
- **AXON Overlap**: Invariant rules define preconditions and postconditions over data payload states.
- **Difference**: Hoare logic is a static program proof system; AXON transports dynamic boolean expressions serialized inside JSON payload files.

### 2. Refinement Calculi (Ralph-Johan Back 1980, Carroll Morgan 1990)
- **Concept**: Step-by-step mathematical transformation of high-level specifications into executable code while preserving invariants.
- **AXON Overlap**: Invariant propagation across data transformations ($T(A) \to B$).
- **Equivalent Formalism**: Refinement Calculi formally model invariant preservation across specification steps.

### 3. Abstract Interpretation (Patrick & Radhia Cousot 1977)
- **Concept**: Approximating runtime semantics over abstract domains (lattices) to prove invariant properties without full execution.
- **AXON Overlap**: Constraint algebra ($C_2 \sqsubseteq C_1$) and invariant inheritance.

### 4. Proof-Carrying Data (PCD - Alessandro Chiesa et al., 2013)
- **Concept**: Distributed computation where every state payload carries a recursive zero-knowledge proof ($\pi$) proving that the payload was produced by a valid state transformation satisfying predicate $\Phi$.
- **AXON Overlap**: Exactly maps to H10 / H7 (Invariant-preserving transformation lineage).
- **Finding**: **Proof-Carrying Data (PCD)** is the formal academic theoretical equivalent of AXON's invariant provenance claim.
