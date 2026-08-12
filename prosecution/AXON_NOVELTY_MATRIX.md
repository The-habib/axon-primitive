# AXON Novelty Matrix (prosecution/AXON_NOVELTY_MATRIX.md)

## 1. Technical Novelty Evaluation Matrix

| Technical Claim | Prior Art / Existing Systems | Exact Overlap | Exact Difference | Reproducible by Existing Tools? | Novel Component? | Novel Composition? | New Primitive? | Confidence | Verdict |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Content Addressing** | Git, IPFS, Merkle Trees | SHA-256 hashing over bytes | None | Yes | No | No | No | 100% | `EXISTING` |
| **Data Schema** | Protobuf, JSON Schema, ASN.1 | Type field descriptors | None | Yes | No | No | No | 100% | `EXISTING` |
| **Executable Predicate** | Google CEL, eBPF, PostScript | Stack boolean expressions | Embedded in JSON file | Yes (via WASM/CEL) | No | Yes | No | 95% | `VARIANT` |
| **State Invariants** | SQL CHECK, Eiffel Contracts | Boolean predicate rules | Portable JSON pack | Yes (via SQLite) | No | Yes | No | 95% | `VARIANT` |
| **Digital Signatures** | Ed25519, Cosign, RSA | Asymmetric signing | Signed payload hash | Yes | No | No | No | 100% | `EXISTING` |
| **Code-Data Coupling** | EVM Bytecode, Move VM | Payload identity binding | Offline zero-WASM file | Yes (WASM + CBOR) | No | Yes | No | 90% | `COMPOSITION` |
| **Overall Protocol Format**| None (Specific `.axon` schema) | None | Zero-dependency `.axon` format | Partial (Requires spec) | No | Yes | No | 95% | `NOVEL PROTOCOL` |

---

## 2. Verdict Determination
AXON is classified as **Level C — NOVEL PROTOCOL / DATA FORMAT SPECIFICATION** (with Level B traits as a **SIGNIFICANT NEW COMPUTATIONAL ABSTRACTION** for edge/mobile data integrity).
