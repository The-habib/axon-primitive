# AXON v1.0 Reality Competitor Matrix (REALITY_COMPETITOR_MATRIX.md)

## 1. Multi-Dimensional Technology Comparison

| Evaluation Metric | JSON Schema | CBOR + CEL | Pydantic / Zod | OPA (Rego) | WASM Modules | AXON 1.0 (`.axon`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Self-Evaluating Invariants** | ❌ No | ⚠️ Partial | ❌ No | ❌ No | ⚠️ Partial | ✅ **YES** |
| **Embedded Payload Signature** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ✅ **YES** |
| **Cross-Language Verification**| ✅ Yes | ✅ Yes | ❌ No (Single) | ⚠️ Partial | ✅ Yes | ✅ **YES** |
| **Zero Cloud Dependencies** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ **YES** |
| **Rootless Mobile (Termux)** | ✅ Yes | ✅ Yes | ⚠️ Partial | ❌ Complex | ⚠️ Complex | ✅ **YES** |
| **State Transformation Lineage**| ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ✅ **YES** |
| **Hierarchical Identity** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ✅ **YES** |
| **4-State Verification System** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ✅ **YES** |

---

## 2. Competitive Reality Summary
Existing tools (JSON Schema, Pydantic, Zod) validate structural types on a single node or inside an ORM.

AXON's primary distinction is offering a **Self-Evaluating, Signed, Content-Addressed Object Format (`.axon`)** that bundles data payloads, AP-VM invariant rules, and transformation lineage triples into a zero-dependency file verified across Python, Node.js, and Android Termux ARM64.
