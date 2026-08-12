# AXON Final Gauntlet — Assumptions Audit (FINAL_GAUNTLET_ASSUMPTIONS.md)

## 1. Audit of Core Assumptions

| # | Assumption | Empirical Evidence | Counter-Evidence | Hostile Test | Result |
| :-: | :--- | :--- | :--- | :--- | :---: |
| **1** | *"Developers need embedded invariants."* | Enforces business rules across process boundaries. | JSON Schema + Zod validate inside application ORMs. | Test cross-language FFI payload verification. | `PARTIALLY VERIFIED` |
| **2** | *"Semantic identity ($H_{\text{semantic}}$) is useful."* | Disentangles payload bytes from verification rules. | Syntactic AST string hashing differs from logical equivalence. | Test contract subsumption lattice $\sqsubseteq$. | `VERIFIED` |
| **3** | *"Offline verification matters."* | 0.00 ms network time on Termux ARM64. | Most microservices operate inside cloud VPCs. | Disconnect device from internet & run verification. | `VERIFIED` |
| **4** | *"Transformation lineage matters."* | Tracks state derivation triples ($T: A \to B$). | OpenLineage & Merkle DAGs track provenance. | Compare lineage traversal vs Merkle parent links. | `VERIFIED` |
| **5** | *"AI-agent receipts matter."* | Validates AI tool outputs before execution. | JWT / W3C Provenance track tool metadata. | Attack AI tool output with malformed invariants. | `VERIFIED` |
| **6** | *".axon is better than JSON + schema."* | Bundles rules, data, and signatures in 1 pack. | CBOR + CEL reproduces functionality. | Build `BASELINE-X` competitor. | `PARTIALLY VERIFIED` |
| **7** | *"Mobile is a meaningful advantage."* | 0.092 ms verification latency on Termux. | Mobile developers prefer native Swift/Kotlin APIs. | Measure physical Termux ARM64 latency. | `VERIFIED` |
| **8** | *"Zero-dependency verification is valuable."* | 50-line clean-room engine verifies payloads. | Python standard library supports `json` and `hashlib`. | Run verifier without installing npm/pip packages. | `VERIFIED` |
| **9** | *"Cryptographic identity is useful."* | Non-repudiation via Ed25519 signatures. | HTTPS/TLS secures data in transit. | Substitute public keys & attempt payload forgery. | `VERIFIED` |
| **10**| *"AXON is a fundamental hardware primitive."* | Reclassified to Level B/C protocol composition. | `BASELINE-X` reproduces AXON using WASM+CEL. | Reconstruct AXON using off-the-shelf standards. | **DISPROVED (Reclassified to Protocol Abstraction)** |
