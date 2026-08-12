# AXON Claim Freeze (prosecution/AXON_CLAIM_FREEZE.md)

## 1. Frozen Core Assertion
AXON asserts the following single core technical claim:
> **"A data payload can be bound to its own executable invariant predicate logic such that the predicate logic is coupled into the payload's identity ($H = \text{hash}(\text{data} \mathbin{\Vert} \text{predicate})$), allowing any receiving system to execute data verification without external database rules, application validators, or out-of-band schema enforcement."**

---

## 2. Stripping Non-Core Infrastructure

The following components are classified strictly as **SUPPORTING INFRASTRUCTURE** and MUST NOT contribute to any claim of conceptual novelty:

- **SHA-256**: Existing standard hash function (FIPS 180-4).
- **Ed25519**: Existing standard asymmetric signature algorithm (RFC 8032).
- **CLI & JSON**: Existing tooling and serialization formats.
- **URI (`axon://`)**: Existing string addressing scheme.
- **SQLite / Disk Storage**: Existing storage machinery.
- **Android Termux Support**: Deployment environment / adoption capability.

---

## 3. AXON Without Everything Non-Essential

When SHA-256, Ed25519, CLI, JSON, URIs, and Termux support are removed, the remaining atomic concept is:

> **"Code-Data Coupled Identity (CDCI): Linking a data payload with an executable boolean predicate into a single immutable content-addressed identity hash."**

This atomic concept is the sole subject of the Novelty Trial.
