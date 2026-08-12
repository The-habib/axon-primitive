# AXON 1.0.0 Protocol Freeze Specification (AXON_1.0_PROTOCOL_FREEZE.md)

## 1. Frozen Specification Digest Manifest

The AXON 1.0.0 protocol semantics, canonicalization rules, AP-L grammar, identity hierarchy, and 4-state verification system are **FROZEN**.

| Specification Document | File Path | SHA-256 Digest | Status |
| :--- | :--- | :--- | :---: |
| **AXON Core Model** | [`docs/AXON_CORE_MODEL.md`](docs/AXON_CORE_MODEL.md) | `5a74e1160869...` | **FROZEN** |
| **Predicate Language** | [`docs/PREDICATE_LANGUAGE.md`](docs/PREDICATE_LANGUAGE.md) | `9b380f1e2901...` | **FROZEN** |
| **Security Model** | [`docs/SECURITY_MODEL.md`](docs/SECURITY_MODEL.md) | `0c4418a221f7...` | **FROZEN** |
| **500 Vectors Manifest** | [`conformance/vectors_500.json`](conformance/vectors_500.json) | `18402ff8390b...` | **FROZEN** |

---

## 2. Breaking Change Rules
Any modification to canonical JSON sorting, SHA-256 identity equations, signature headers, or AP-VM limits requires a major protocol version increment (`AXON/2.0`).
