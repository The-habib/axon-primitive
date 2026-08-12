#!/usr/bin/env python3
"""
Clean-Room Semantic Contract Engine (DEEPAXON Phase 23)
Written strictly from deepaxon/CLEANROOM_SPEC.md without importing any AXON source code.
Proves the abstraction is independent of AXON implementation details.
"""

import sys
import json
import hashlib
import os

class CleanRoomSemanticEngine:
    @staticmethod
    def canonicalize(obj):
        if isinstance(obj, dict):
            return json.dumps({k: obj[k] for k in sorted(obj.keys())}, separators=(',', ':'))
        if isinstance(obj, list):
            return json.dumps(obj, separators=(',', ':'))
        return str(obj)

    @staticmethod
    def compute_semantic_hash(data, invariants):
        c_data = CleanRoomSemanticEngine.canonicalize(data)
        c_inv = CleanRoomSemanticEngine.canonicalize(sorted(invariants))
        payload = f"{c_data}:{c_inv}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    @staticmethod
    def evaluate(payload):
        data = payload.get("data", {})
        invariants = payload.get("invariants", [])
        expected_hash = payload.get("semanticHash", "")

        c_hash = CleanRoomSemanticEngine.compute_semantic_hash(data, invariants)
        if c_hash != expected_hash:
            return "FALSE", f"Semantic hash mismatch: expected {c_hash}, got {expected_hash}"

        failures = []
        for inv in invariants:
            try:
                res = eval(inv, {"__builtins__": {}}, data)
                if not bool(res):
                    failures.append(inv)
            except NameError as ne:
                return "UNKNOWN", f"Missing variable binding for predicate: {str(ne)}"
            except Exception as e:
                failures.append(f"{inv} (Error: {str(e)})")

        if failures:
            return "FALSE", f"Invariant failure: {', '.join(failures)}"
        
        return "TRUE", "Valid Semantic Object"

def main():
    sample_data = {"val": 100, "record_count": 5}
    sample_inv = ["val > 0", "record_count >= 1"]
    s_hash = CleanRoomSemanticEngine.compute_semantic_hash(sample_data, sample_inv)

    sample_object = {
        "semanticHash": s_hash,
        "data": sample_data,
        "invariants": sample_inv
    }

    status, msg = CleanRoomSemanticEngine.evaluate(sample_object)
    print(f"✔ Clean-Room Engine Result: {status} ({msg})")

if __name__ == '__main__':
    main()
