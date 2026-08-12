# Decidability & Restricted Semantic Identity (semantic-identity/DECIDABILITY.md)

## 1. The Halting & Equivalence Boundary (Rice's Theorem)

By Rice's Theorem, given two arbitrary programs $P_1$ and $P_2$, determining whether $\forall x, P_1(x) == P_2(x)$ is **UNDECIDABLE**.

Therefore, attempting to compute a "Universal Semantic Hash" for arbitrary Turing-complete functions is mathematically impossible.

---

## 2. Decidable Restricted Semantic Domain

To make Semantic Identity computable, the contract expression domain $\mathcal{L}_{\text{pred}}$ is strictly restricted to:

1. **Non-Turing-Complete Stack Expressions**: Quantifier-free boolean expressions over primitive types (integers, floats, strings, booleans).
2. **Side-Effect Free Functions**: Pure functions with zero file system, network, or OS clock access.
3. **Canonical AST Representation**: Predicate strings are parsed into canonical Abstract Syntax Trees (AST) with alphabetically sorted keys and normalized operators ($x \ge 0 \equiv 0 \le x$).
4. **Bounded Evaluation Time**: Predicate evaluation is stack-bounded ($\le 64$ stack frames) and constant-time execution bounded.

---

## 3. Decidable Equivalence Theorem
Under language restriction $\mathcal{L}_{\text{pred}}$, semantic equivalence $\mathcal{C}_1 \equiv_{\text{sem}} \mathcal{C}_2$ is **DECIDABLE** via canonical AST normalization.
