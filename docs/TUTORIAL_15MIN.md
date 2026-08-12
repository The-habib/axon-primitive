# AXON 15-Minute Transformation & Lineage Tutorial (docs/TUTORIAL_15MIN.md)

## Goal
Build an invariant-preserving state transformation pipeline $T : A \to B$ with lineage tracking in 15 minutes.

---

## Python Implementation:
```python
from axon_sdk import Axon

# 1. Create Parent Object A
parent = Axon.create({"val": 50}, invariants=["val >= 0"])
print(f"Parent Semantic Hash: {parent.header['semanticHash']}")

# 2. Transform A -> B while inheriting invariants
child = parent.transform(
    transform_fn=lambda d: {"val": d["val"] + 10, "status": "ACTIVE"},
    new_schema={"val": "number", "status": "string"},
    additional_invariants=["status == 'ACTIVE'"]
)

# 3. Verify Child Object B and inspect Lineage
res = child.verify()
print(f"Child Verification: {res.state}")
print(f"Parent Link: {child.transformation['parentSemanticHash']}")
```
