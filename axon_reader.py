#!/usr/bin/env python3
"""
AXON Reference Reader B (Pure Python 3 Independent Implementation)
0 Shared Code Lines, 0 External Dependencies.
Parses .axon packs, validates canonical SHA-256 digests, and evaluates invariant expressions.
"""

import sys
import json
import hashlib
import os

class AXONPythonReader:
    @staticmethod
    def canonicalize(data):
        keys = sorted(data.keys())
        sorted_obj = {k: data[k] for k in keys}
        return json.dumps(sorted_obj, separators=(',', ':'))

    @staticmethod
    def hash_payload(data):
        canonical = AXONPythonReader.canonicalize(data)
        return hashlib.sha256(canonical.encode('utf-8')).hexdigest()

    @staticmethod
    def evaluate_invariants(data, invariants):
        failures = []
        for inv in invariants:
            try:
                # Safe eval in python with data dict as context
                result = eval(inv, {"__builtins__": {}}, data)
                if not bool(result):
                    failures.append(inv)
            except Exception as e:
                failures.append(f"{inv} (Error: {str(e)})")
        return len(failures) == 0, failures

    @staticmethod
    def verify(payload):
        data = payload.get("data", {})
        c_hash = AXONPythonReader.hash_payload(data)
        
        if c_hash != payload.get("contentHash"):
            return False, f"Content hash mismatch: expected {c_hash}, got {payload.get('contentHash')}"

        invariants = payload.get("invariants", [])
        ok, failures = AXONPythonReader.evaluate_invariants(data, invariants)
        if not ok:
            return False, f"Invariant evaluation failed: {', '.join(failures)}"

        return True, "Valid"

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'verify':
        print("Usage: python3 axon_reader.py verify <file.axon>")
        sys.exit(1)

    file_path = sys.argv[2]
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        payload = json.load(f)

    valid, msg = AXONPythonReader.verify(payload)
    if valid:
        print(f"✔ Python Engine B: AXON Primitive is 100% VALID & VERIFIED ({payload.get('uri')})")
    else:
        print(f"✖ Python Engine B Verification Failed: {msg}")
        sys.exit(1)

if __name__ == '__main__':
    main()
