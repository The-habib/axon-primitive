# Master Invention Audit — What AXON 1.0 Actually Invented (FINAL_INVENTION_AUDIT.md)

## 1. Zero-Bias Invention Audit

| System Candidate | Prior Art Precedent | Exact Overlap | AXON 1.0 Invention & Technical Difference |
| :--- | :--- | :--- | :--- |
| **Content Addressing** | Git Blobs, IPFS | SHA-256 Digest | **REUSED**: AXON reuses SHA-256 for $H_{\text{content}}$. |
| **Type System** | JSON Schema, Protobuf | Key types | **REUSED**: AXON uses standard structural schema definitions. |
| **Predicate Evaluator** | Google CEL, Rego/OPA | Expression trees | **COMPOSITION**: AXON embeds AP-L expressions into JSON packs. |
| **Authenticity** | Ed25519, Cosign | Asymmetric key signature | **REUSED**: AXON uses standard Ed25519 envelopes. |
| **Hierarchical Identity**| EVM Smart Contracts | State/Code Hash | **INVENTION / NOVEL PROTOCOL DESIGN**: Disentangling $H_{\text{content}}, H_{\text{contract}}, H_{\text{semantic}}$ in offline zero-WASM objects. |
| **Invariant Propagation**| Proof-Carrying Data | State transition claims | **ABSTRACTION**: $T : A \to B$ Hoare-triple state transformations over portable files. |

---

## 2. Final Invention Verdict

AXON did **NOT** invent SHA-256, Ed25519, JSON, or stack expressions.

AXON **INVENTED** the **AXON 1.0 Computational Data System Protocol (`axon://`)**—a lightweight, zero-dependency, open protocol specification and developer model for self-evaluating computational objects operational on rootless mobile devices.
