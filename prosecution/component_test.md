# Component vs Composition Audit (prosecution/component_test.md)

## 1. Technical Component Taxonomy Table

| AXON Component | Existing Prior Art | Classification | New? |
| :--- | :--- | :---: | :---: |
| **Content Addressing** | Git Blobs (2005), IPFS (2015), Merkle Trees (1979) | `EXISTING` | ❌ No |
| **Data Schema** | ASN.1 (1984), Protobuf (2008), JSON Schema (2012) | `EXISTING` | ❌ No |
| **Executable Predicate** | Lisp (1958), PostScript (1982), eBPF (2014), WASM (2017) | `EXISTING` | ❌ No |
| **Runtime Invariants** | Eiffel Contracts (1988), SQL CHECK (1992), Racket (2002) | `EXISTING` | ❌ No |
| **State Transitions** | State Machines, TLA+ (1999), EVM Smart Contracts (2015) | `EXISTING` | ❌ No |
| **Embedded Evaluator** | PostScript Engine, PDF JS, WASM Micro-Runtime | `EXISTING` | ❌ No |
| **Digital Signature** | RSA (1977), Ed25519 (2011), Signed Documents | `EXISTING` | ❌ No |
| **Self-Verification** | Proof-Carrying Code (Necula 1996), PCD (Chiesa 2013) | `VARIANT` | ❌ No |
| **Code-Data Coupled Identity**| EVM Bytecode+State, WASM Contract Objects | `COMBINATION` | ⚠️ Combination |

---

## 2. Mandatory Component vs Composition Determination

- **Is AXON novel because one individual component is novel?**: **NO**. Every individual building block (content hashing, schemas, stack predicates, Ed25519 signatures, state transitions) has decades of prior art in systems engineering.
- **Is AXON novel because known components were packaged together into an open protocol format?**: **YES**. AXON composes data serialization, deterministic predicate evaluation, and asymmetric signing into an open, lightweight file format (`.axon`) operational on rootless mobile devices.
