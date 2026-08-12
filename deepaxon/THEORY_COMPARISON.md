# Theoretical Comparison Matrix (deepaxon/THEORY_COMPARISON.md)

| Theoretical Formalism | Primary Academic Literature | Shared Abstraction | Technical Gap vs AXON |
| :--- | :--- | :--- | :--- |
| **Hoare Logic** | Hoare (CACM 1969) | Pre/Post-condition triples $\{P\} C \{Q\}$ | Hoare logic is static proof; AXON is dynamic serialized JSON payload checks. |
| **Refinement Types** | Jhala et al. (LiquidHaskell 2008) | Predicate constraints $\{x \mid P(x)\}$ | Refinement types operate at compile time in Haskell/F*; AXON operates at runtime across language FFI boundaries. |
| **Proof-Carrying Data (PCD)** | Chiesa et al. (EUROCRYPT 2013) | Payload carrying proof of predicate $\Phi$ | PCD uses heavy ZK-SNARK cryptographic proofs; AXON uses lightweight Ed25519 signatures and JS/Python string expressions. |
| **Abstract Interpretation** | Cousot & Cousot (POPL 1977) | Galois connections & constraint lattices | Abstract interpretation computes sound over-approximations; AXON evaluates exact concrete instances. |
