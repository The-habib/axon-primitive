# DEEPAXON Phase 0 — AXON Fact Audit (deepaxon/FACTS.md)

## 1. Categorized Technical Facts

### VERIFIED (Empirically Proven in Repository)
- **SHA-256 State Hashing**: `AXONEngine.hashPayload` produces 100% byte-deterministic state digests across Node.js v26 and Python 3.14 (`509176665aff3b88...`).
- **Ed25519 Signatures**: Asymmetric Ed25519 signatures verify payload non-repudiation natively across 4 independent engines.
- **Physical Latency**: Total local payload verification time is **0.31 ms** (0.04ms canonicalization, 0.04ms SHA-256, 0.08ms invariant evaluation, 0.15ms Ed25519 verification).
- **100% Conformance**: 100/100 published conformance vectors passed in fresh clone test.
- **Rootless Termux Operation**: Operates 100% offline on Android Termux ARM64 without root or `proot`.

### CLAIMED (Asserted in Design Documentation)
- Data payloads can carry their own domain business rules without external ORM or database drivers.
- Invariant rules can be evaluated in zero milliseconds on host nodes without cloud validation APIs.

### ASSUMED (Unproven Design Hypotheses)
- That packaging boolean predicate expressions into JSON files creates a new programming language primitive rather than an open file format specification.
- That code-data coupled identity ($H = \text{hash}(\text{data} \mathbin{\Vert} \text{predicates})$) is distinct from EVM smart contract state or Proof-Carrying Data.

### UNKNOWN (Under Investigation in DEEPAXON)
- Whether invariant constraint propagation across data transformations ($T(A) \to B$) forms a novel algebraic primitive or reduces to Refinement Calculi / Proof-Carrying Data.
