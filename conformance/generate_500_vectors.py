#!/usr/bin/env python3
"""
AXON 1.0 Conformance Suite Generator: Creates 500 Deterministic Vectors
"""

import json
import hashlib

def canonicalize(obj):
    if obj is None:
        return "null"
    if isinstance(obj, bool):
        return "true" if obj else "false"
    if isinstance(obj, (int, float)):
        return json.dumps(obj)
    if isinstance(obj, str):
        return json.dumps(obj)
    if isinstance(obj, list):
        return "[" + ",".join(canonicalize(x) for x in obj) + "]"
    if isinstance(obj, dict):
        keys = sorted(obj.keys())
        return "{" + ",".join(f"{json.dumps(k)}:{canonicalize(obj[k])}" for k in keys) + "}"
    return str(obj)

def compute_content_hash(data):
    return hashlib.sha256(canonicalize(data).encode('utf-8')).hexdigest()

def compute_contract_hash(schema, invariants):
    c_s = canonicalize(schema)
    c_i = canonicalize(sorted(invariants))
    return hashlib.sha256(f"{c_s}:{c_i}".encode('utf-8')).hexdigest()

def compute_semantic_hash(content_hash, contract_hash, parent_hash=""):
    return hashlib.sha256(f"{content_hash}:{contract_hash}:{parent_hash}".encode('utf-8')).hexdigest()

def generate_vector(idx):
    val = idx * 10
    record_count = (idx % 20) + 1
    data = {"val": val, "record_count": record_count, "tag": f"vector_{idx}"}
    schema = {"val": "number", "record_count": "number", "tag": "string"}
    invariants = ["val >= 0", "record_count >= 1"]

    c_hash = compute_content_hash(data)
    k_hash = compute_contract_hash(schema, invariants)
    s_hash = compute_semantic_hash(c_hash, k_hash)

    # Intentionally inject invalid cases for negative testing
    expected_state = "TRUE"
    if idx % 10 == 9:
        data["val"] = -100 # Invariant failure -> FALSE
        expected_state = "FALSE"
        c_hash = compute_content_hash(data) # update content hash to pass hash check but fail invariant
    elif idx % 25 == 24:
        c_hash = "0" * 64 # Tampered content hash -> FALSE
        expected_state = "FALSE"

    return {
        "id": f"vec_{idx:03d}",
        "expectedState": expected_state,
        "payload": {
            "header": {
                "version": "AXON/1.0",
                "uri": f"axon://payload/{s_hash[:16]}",
                "contentHash": c_hash,
                "contractHash": k_hash,
                "semanticHash": s_hash,
                "timestamp": 1700000000 + idx,
                "nodeId": "axon_test_node"
            },
            "schema": schema,
            "invariants": invariants,
            "data": data,
            "signature": "simulated_ed25519_signature"
        }
    }

def main():
    vectors = [generate_vector(i) for i in range(500)]
    with open('conformance/vectors_500.json', 'w', encoding='utf-8') as f:
        json.dump(vectors, f, indent=2)
    print("✔ Successfully generated 500 deterministic AXON 1.0 test vectors in conformance/vectors_500.json")

if __name__ == '__main__':
    main()
