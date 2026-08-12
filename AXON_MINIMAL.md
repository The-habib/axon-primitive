# AXON Irreducible Minimal Protocol Specification (AXON_MINIMAL.md)

## 1. Stripped Core Definition

The irreducible atomic model of AXON is the 3-tuple:
$$A_{\text{minimal}} = \langle D, \mathcal{C}, H_{\text{semantic}} \rangle$$

Where:
- $D$ is a canonical UTF-8 JSON data payload.
- $\mathcal{C}$ is a list of side-effect-free, non-Turing-complete boolean predicate expressions.
- $H_{\text{semantic}} = \text{SHA256}(\text{Canonicalize}(D) \mathbin{\Vert} \text{Canonicalize}(\mathcal{C}))$.

---

## 2. Stripped Features
Everything else—type schemas, node IDs, signatures, transformation descriptors, CLI frameworks—is **SUPPORTING INFRASTRUCTURE** or **PROTOCOL CONVENIENCE ENVELOPES**.
