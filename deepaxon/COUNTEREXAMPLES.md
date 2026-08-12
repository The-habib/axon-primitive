# Four-State Evaluation & Counterexamples (deepaxon/COUNTEREXAMPLES.md)

## 1. Four-State Evaluation Model

Rather than binary boolean validation (`VALID` / `INVALID`), robust semantic contract evaluation requires a 4-state domain logic model:

| State Value | Technical Meaning | Example Scenario |
| :--- | :--- | :--- |
| **`TRUE`** | Payload satisfies invariant predicate deterministically. | $x = 100$, invariant $x > 0 \implies \text{TRUE}$. |
| **`FALSE`** | Payload violates invariant predicate. | $x = -50$, invariant $x > 0 \implies \text{FALSE}$. |
| **`UNKNOWN`** | Invariant depends on un-evaluated or missing external state. | Rule requires live database check ($x \in \text{DB}$). |
| **`UNPROVEN`** | Predicate execution exceeds stack limit or times out. | Complex recursive expression. |

---

## 2. Invariant Contradictions & Information Loss
When transformation $T$ discards field keys (e.g. $T(\{x: 10, y: 20\}) = \{y: 20\}$), any invariant referencing $x$ transitions from `TRUE` to `UNKNOWN` or `UNPROVEN`.
