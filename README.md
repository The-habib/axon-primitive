# AXON: Autonomous Executable Invariant Data Primitive (`axon://`)

> An open computing primitive that embeds self-evaluating bytecode invariants, structural type contracts, and state transition predicates directly inside content-addressed binary data payloads (`axon://`).

---

## 💡 What Is AXON?

**AXON** is an open specification and computing primitive that unites static data payloads with **self-evaluating executable invariant predicates**.

Traditional data formats (**JSON, CSV, Parquet**) carry static data bytes, relying on external application ORMs (**Zod, Pydantic**) or database engines (**SQLite, Postgres**) to validate domain business rules. When data is exported or transferred across systems, validation logic is lost.

AXON solves this by embedding stack-bounded invariant predicate evaluators and Ed25519 node signatures into the data payload (`axon://`), enabling zero-dependency data validation natively in Python, Node.js, C, Rust, or mobile Android Termux.

---

## 🗺️ Core Architecture

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

## ⚡ 60-Second Quickstart

### 1. Create an AXON Primitive (TypeScript Engine A)
```bash
node --experimental-strip-types src/cli.ts create '{"val":100,"record_count":5}' > my_data.json
```

### 2. Verify Independently (Python Engine B — 0 Dependencies!)
```bash
python3 axon_reader.py verify sample.axon
# Output: ✔ Python Engine B: AXON Primitive is 100% VALID & VERIFIED (axon://payload/509176665aff3b88)
```

---

## 📄 Specifications & Documentation
- [`INVENTION.md`](INVENTION.md) — Technical specification & formal mathematical model.
- [`computing_map.md`](computing_map.md) — 26-layer computing taxonomy & missing primitive analysis.
- [`100_HOSTILE_OBJECTIONS.md`](100_HOSTILE_OBJECTIONS.md) — 100 hostile objections & neutralization matrix.
- [`EXISTING_TECH_REBUILD.md`](EXISTING_TECH_REBUILD.md) — Existing-technology rebuild analysis.
- [`INCEPTION_VERDICT.md`](INCEPTION_VERDICT.md) — Inception verdict report.
