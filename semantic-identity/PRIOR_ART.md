# Semantic Hashing & Prior-Art Literature Map (semantic-identity/PRIOR_ART.md)

## 1. Deep Literature Search across 6 Domains

### Domain 1: Observational & Program Equivalence
- **Rice's Theorem (1953)**: Proves that any non-trivial semantic property of arbitrary Turing-complete programs is **UNDECIDABLE**.
- **Observational / Contextual Equivalence (Plotkin 1977, Milner 1980)**: $e_1 \approx_{\text{obs}} e_2 \iff \forall C, C[e_1] \Downarrow v \iff C[e_2] \Downarrow v$.
- **Implication for Semantic Identity**: Exact semantic hashing over general Turing-complete code is mathematically impossible. Semantic identity MUST be restricted to decidable, non-Turing-complete predicate domains.

### Domain 2: Type Theory (Refinement Types & Dependent Records)
- **Refinement Types (LiquidHaskell - Jhala et al. 2008)**: $\{ x : \tau \mid P(x) \}$ attaching logical predicates to base types.
- **Dependent Records (Coq / Agda / Idris)**: Records where field types depend on preceding field values.
- **Relationship**: Semantic identity is the **serialized, content-addressed runtime representation of Refinement Types**.

### Domain 3: Design by Contract & Contract Systems
- **Eiffel Design by Contract (Meyer 1988)**: `require` / `ensure` / `invariant`.
- **Racket Higher-Order Contracts (Findler & Felleisen 2002)**: Runtime contract enforcement at module boundaries.

### Domain 4: Build System Fingerprinting
- **Nix Derivations (Dolstra 2004)**: Derivation hashes $H_{\text{drv}} = \text{SHA256}(\text{inputs} \mathbin{\Vert} \text{builder} \mathbin{\Vert} \text{args} \mathbin{\Vert} \text{env})$.
- **Bazel Action Cache Keys**: $H_{\text{action}} = \text{SHA256}(\text{command} \mathbin{\Vert} \text{inputs} \mathbin{\Vert} \text{toolchain})$.

### Domain 5: Smart Contract Code & State Hashing
- **Ethereum EVM State Architecture**: `codeHash` ($\text{Keccak256}(\text{EVMBytecode})$) and `storageRoot` ($\text{MerklePatriciaTrie}(\text{State})$).

### Domain 6: Proof-Carrying Data
- **Proof-Carrying Data (Chiesa et al. 2013)**: Distributed message payload bound to recursive ZK-SNARK proof $\pi$ proving compliance with state predicate $\Phi$.
