# AXON: Experimental Computational Data Protocol (`axon://`)

> An open protocol specification and data format that embeds self-evaluating bytecode invariants, structural type contracts, and state transition predicates directly inside content-addressed binary data payloads (`axon://`).

---

## 💡 What Is AXON?

**AXON** is an open protocol specification and data format that unites static data payloads with **self-evaluating executable invariant predicates**.

Traditional data formats (**JSON, CSV, Parquet**) carry static data bytes, relying on external application ORMs (**Zod, Pydantic**) or database engines (**SQLite, Postgres**) to validate domain business rules. When data is exported or transferred across systems, validation logic is lost.

AXON solves this by embedding stack-bounded invariant predicate evaluators and Ed25519 node signatures into the data payload (`axon://`), enabling zero-dependency data validation natively in Python, Node.js, C, Rust, or mobile Android Termux.

---

## 🗺️ Architecture

```
       Raw Data Payload
              │
              ▼
 ┌──────────────────────────┐
 │      axon://payload      │
 │                          │
 │  data bytes              │
 │  contentHash (SHA-256)   │
 │  type schema             │
 │  evaluator bytecode      │  <-- Embedded Invariant Predicate
 │  signature (Ed25519)     │
 └────────────┬─────────────┘
              │
    ┌─────────┼─────────┬─────────┐
    ▼         ▼         ▼         ▼
  Verify   Inspect   Evaluate   Derive
```

---

## ⚡ Quickstart Example

```bash
# 1. Create an AXON payload (TypeScript Engine A)
node --experimental-strip-types src/cli.ts create '{"val":100,"record_count":5}' > test_payload.json

# 2. Verify independently using Python Engine B (Zero Node.js / FFI dependencies!)
python3 axon_reader.py verify sample.axon
# Output: ✔ Python Engine B: AXON Primitive is 100% VALID & VERIFIED (axon://payload/509176665aff3b88)
```

---

## 📄 Protocol Trial & Specification Artifacts

- [`AXON_NOVELTY_TRIAL.md`](AXON_NOVELTY_TRIAL.md) — Novelty prosecution verdict (**Verdict: C — NOVEL PROTOCOL / DATA FORMAT SPECIFICATION**).
- [`INVENTION.md`](INVENTION.md) — Technical specification & formal mathematical model.
- [`prosecution/AXON_HISTORY.md`](prosecution/AXON_HISTORY.md) — 44-year historical prior art analysis (1982–2026).
- [`prosecution/reconstruct_tests.md`](prosecution/reconstruct_tests.md) — WASM & smart-contract counterexample reconstructions.
- [`prosecution/AXON_100_HOSTILE_OBJECTIONS.md`](prosecution/AXON_100_HOSTILE_OBJECTIONS.md) — 100 hostile engineering objections.
- [`prosecution/five_skeptical_reviewers.md`](prosecution/five_skeptical_reviewers.md) — Five skeptical reviewer reports.
