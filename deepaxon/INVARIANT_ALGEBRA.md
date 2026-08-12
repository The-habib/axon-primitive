# Invariant Algebra Analysis (deepaxon/INVARIANT_ALGEBRA.md)

## 1. Constraint Ordering & Lattice Subsumption
Let $\mathcal{C}_1$ and $\mathcal{C}_2$ be boolean predicate functions over data domain $\mathcal{D}$. We define constraint ordering $\sqsubseteq$ by logical implication:
$$\mathcal{C}_2 \sqsubseteq \mathcal{C}_1 \iff (\forall x \in \mathcal{D}, \mathcal{C}_2(x) \implies \mathcal{C}_1(x))$$

- **Subsumption / Strengthening**: $\mathcal{C}_2 = (x \ge 10)$ is stronger than $\mathcal{C}_1 = (x \ge 0)$, written $\mathcal{C}_2 \sqsubseteq \mathcal{C}_1$.
- **Conjunction / Meet ($\sqcap$)**: $\mathcal{C}_1 \sqcap \mathcal{C}_2 = \lambda x. (\mathcal{C}_1(x) \land \mathcal{C}_2(x))$.
- **Disjunction / Join ($\sqcup$)**: $\mathcal{C}_1 \sqcup \mathcal{C}_2 = \lambda x. (\mathcal{C}_1(x) \lor \mathcal{C}_2(x))$.
- **Contradiction**: $\mathcal{C}_1 = (x > 10) \land \mathcal{C}_2 = (x < 5) \implies \bot$ (Unsatisfiable).

---

## 2. Abstract Interpretation Mapping
Constraint ordering $\sqsubseteq$ directly maps to **Abstract Interpretation Lattices** (Cousot & Cousot 1977).
