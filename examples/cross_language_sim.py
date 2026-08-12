#!/usr/bin/env python3
"""
Cross-Language Developer Simulation (Phase 7)
Producer: Python 3 creates an AXON payload using portable AP-L invariants.
Consumer: TypeScript Engine A verifies the payload independently.
"""

import sys
import json
import hashlib
from axon_reader import AXONPythonEngine

def main():
    data = {"val": 500, "user": "alice"}
    schema = {"val": "number", "user": "string"}
    invariants = ["val > 100", "user != ''"]

    c_hash = AXONPythonEngine.compute_content_hash(data)
    k_hash = AXONPythonEngine.compute_contract_hash(schema, invariants)
    s_hash = AXONPythonEngine.compute_semantic_hash(c_hash, k_hash)

    payload = {
        "header": {
            "version": "AXON/1.0",
            "uri": f"axon://simulated/{s_hash[:16]}",
            "contentHash": c_hash,
            "contractHash": k_hash,
            "semanticHash": s_hash,
            "timestamp": 1700000000,
            "nodeId": "python_producer"
        },
        "schema": schema,
        "invariants": invariants,
        "data": data,
        "signature": "simulated_python_signature"
    }

    with open('simulated_python_output.json', 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)

    print("✔ Python Producer: Generated payload simulated_python_output.json")

if __name__ == '__main__':
    main()
