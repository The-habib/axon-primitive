# DEEPAXON Phase 2 — 10 Competing Hypotheses (deepaxon/HYPOTHESES.md)

## 1. Hypothesis Matrix

| # | Hypothesis Name | Technical Definition | Closest Prior Art | Alleged Unique Claim | Fatal Weakness |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **H1** | **Self-Validating Data** | Data carrying embedded validation rules. | PostScript (1982), PDF JS | Automatic self-verification | Exists in PostScript / PDF JS. |
| **H2** | **Executable Data** | Data that executes code upon inspection. | Active Messages (1992) | Executable payload bytes | Security risks; exists in eBPF. |
| **H3** | **Constraint-Carrying Value**| Values carrying runtime refinement types. | Refinement Types (LiquidHaskell) | Typed dynamic constraints | Reduces to dynamic contract checking. |
| **H4** | **Semantic Data Object** | Data carrying formal domain rules. | OWL / RDF Schemas | Domain-aware data | Declarative RDF already models this. |
| **H5** | **Code-Data Coupled Identity**| Identity hash derived from data + code. | EVM Smart Contracts (2015) | Identity-bound validators | Exists in Ethereum EVM state. |
| **H6** | **Contract-Carrying Value** | Eiffel contracts serialized with JSON. | Eiffel (1988), Racket Contracts | Portable contract checks | Reduces to contract serialization. |
| **H7** | **Invariant-Preserving Transformation** | Hoare-triple state transition over data ($T: A \to B$). | Hoare Logic (1969), Refinement Calculi | **Verifiable Invariant Lineage Propagation** | High complexity; requires formal verifier. |
| **H8** | **Typed Artifact** | Artifacts with structural type headers. | Protobuf (2008), FlatBuffers | Typed binary objects | Standard schema formats solve this. |
| **H9** | **Executable Schema** | Schema containing executable rules. | Google CEL (2019), Rego/OPA | Schema-embedded expressions | Exists in CEL and OPA. |
| **H10** | **Semantic Lineage Node** | Provenance graph carrying invariant claims. | Proof-Carrying Data (Chiesa 2013) | Provenance guarantee propagation | ZK-SNARK PCD already models this. |

---

## 2. Strongest Surviving Candidate: H7 (Invariant-Preserving Transformation)
H7 ($T : \langle D_1, \mathcal{C}_1 \rangle \to \langle D_2, \mathcal{C}_2 \rangle$) is the only hypothesis that explores **Invariant Propagation Across State Transformations**.
