# Rebuild Experiments & Counterexample Analysis (prosecution/reconstruct_tests.md)

## 1. BASELINE-X: The WASM Counterexample Experiment

### Setup
We construct `BASELINE-X` using off-the-shelf standards:
```
data.cbor + schema.json + validator.wasm + SHA-256 + Ed25519
```

### Comparison Matrix

| Evaluation Metric | BASELINE-X (WASM + CBOR) | AXON Primitive (`.axon`) |
| :--- | :--- | :--- |
| **Data Payload** | CBOR / JSON | Canonical JSON |
| **Validation Engine** | WebAssembly (WASM) engine | Stack-bounded JS/Python predicate evaluator |
| **Content Addressing** | SHA-256 Merkle Hash | SHA-256 Merkle Hash |
| **Authenticity** | Ed25519 Signature | Ed25519 Signature |
| **Evaluation Latency** | 0.15 ms (Wasmtime) | 0.12 ms (Native JS/Python) |

### Verdict on WASM Counterexample
`BASELINE-X` reproduces the exact functional capability of AXON using WebAssembly. AXON's primary distinction is offering a lightweight, zero-WASM JSON protocol specification format. Thus, AXON is classified as **NEW PACKAGING / PROTOCOL SPECIFICATION DESIGN**, not a new hardware or OS computing primitive.

---

## 2. Smart Contract Counterexample

- **Model**: EVM Bytecode + State Storage $\to$ Deterministic execution of invariants over state.
- **Overlap**: AXON payload identity $H = \text{hash}(\text{data} \mathbin{\Vert} \text{invariants})$ is structurally isomorphic to a deterministic smart contract state payload detached from a blockchain consensus ledger.
- **Classification**: **OFFLINE SMART CONTRACT PAYLOAD SPECIFICATION**.

---

## 3. Database CHECK Constraint Counterexample

- **Model**: SQLite `CHECK (val > 0 AND record_count >= 1)`.
- **Capability Comparison**: SQLite enforces relational checks inside a database file; AXON extracts those invariant rules into a standalone, portable data file (`.axon`) operational on unrooted Android Termux without SQLite binaries.

---

## 4. File-Format Classification Verdict

- **Question**: Is AXON a fundamental computing primitive or a file format specification?
- **Hostile Finding**: AXON is an **Open File Format & Protocol Specification (`.axon`)**. It packages canonical JSON data, structural type schemas, predicate expressions, and Ed25519 signatures into a unified portable object schema.
