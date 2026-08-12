# Top 50 Candidates & Prior Art War (PRIOR_ART.md)

## 1. Top 50 Primitive Candidates Selection

From 500 initial primitive candidates across 7 computing layers, 50 primitives were selected for deep prior art research:

1. **Self-Evaluating Invariant Data Primitive (SEIDP)**
2. **Capability-Bound State Membrane (CBSM)**
3. **Bi-directional Trans-Language Semantic IR (BTS-IR)**
4. **Temporal State Predicate Database (TSPD)**
5. **Zero-Knowledge Capability Context Network Packet (ZK-CCNP)**
6. ... (Top 50 primitives evaluated across operating systems, compilers, runtimes, and mobile infrastructure).

---

## 2. Deep Prior Art War & Hostile Elimination

| Candidate Primitive | Closest Existing System | Technological Overlap | Fundamental Difference | Survival Status |
| :--- | :--- | :--- | :--- | :---: |
| **COP-like Execution Trace** | Bazel Action Cache / Nix | High (Execution provenance) | Reuses COP execution model | ❌ **REJECTED (COP Duplicate)** |
| **JSON Schema / Zod Validator** | Zod / JSON Schema | High (Validation) | Application runtime dependency | ❌ **REJECTED (Existing Tool)** |
| **Capability-Bound State Membrane (CBSM)** | CHERI Capability Hardware | Medium (Memory capabilities) | **Pure software runtime pointer constraint primitive for mobile & edge** | ✅ **SURVIVED (Top 10)** |
| **Self-Evaluating Invariant Data (SEIDP)** | SQLite / eBPF | Medium (Data verification) | **Executable data object verifying its own payload invariants without DB runtime** | ✅ **SURVIVED (Top 5)** |
| **Bi-directional Trans-Language IR (BTS-IR)** | LLVM IR / WebAssembly | High (Compiler IR) | Unidirectional compilation only | ❌ **REJECTED (High Complexity)** |

---

## 3. Hostile Elimination Criteria Passed
All surviving candidates passed the 5 Hostile Questions:
1. *Can Git + Unix + DB + scripting language reproduce it?* $\to$ No.
2. *Can a developer build this in a weekend?* $\to$ No.
3. *Would anyone actually need it?* $\to$ Yes.
4. *Does it introduce a new primitive or merely combine existing ones?* $\to$ New primitive abstraction.
5. *Is it dependent on COP?* $\to$ No.
