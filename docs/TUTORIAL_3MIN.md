# AXON 3-Minute Quickstart Tutorial (docs/TUTORIAL_3MIN.md)

## Goal
Install AXON, create a computational object, and verify it in under 3 minutes.

---

## Step 1: 1-Command Installation (30 Seconds)
```bash
pip install axon-primitive
# or
npm install axon-primitive
```

---

## Step 2: Create & Verify an AXON Object (90 Seconds)

### Python (3 Lines of Code):
```python
from axon_sdk import Axon

# 1. Create payload with self-evaluating contract rules
obj = Axon.create({"val": 100, "user": "alice"}, invariants=["val > 0", "user != ''"])

# 2. Run 4-state verification
result = obj.verify()
print(f"Verified: {result.is_valid}") # Output: True
```

### Command Line Interface (CLI):
```bash
axon-py verify examples/production/01_ai_agent_tool_output.json
# Output: ✔ Python Engine B: AXON 4-State Verification = TRUE (Valid AXON 1.0 Payload)
```

Congratulations! You have verified your first portable AXON computational object in under 3 minutes.
