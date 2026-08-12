#!/usr/bin/env python3
"""
AXON 1.0 Blind Clean-Room Verifier (gauntlet/blind_verifier.py)
Written 100% blindly from specification and conformance vectors without importing reference source code.
"""

import sys
import json
import hashlib

class BlindAXONVerifier:
    @staticmethod
    def canonical_json(val):
        if val is None:
            return "null"
        if isinstance(val, bool):
            return "true" if val else "false"
        if isinstance(val, (int, float)):
            return json.dumps(val)
        if isinstance(val, str):
            return json.dumps(val)
        if isinstance(val, list):
            return "[" + ",".join(BlindAXONVerifier.canonical_json(x) for x in val) + "]"
        if isinstance(val, dict):
            keys = sorted(val.keys())
            return "{" + ",".join(f"{json.dumps(k)}:{BlindAXONVerifier.canonical_json(val[k])}" for k in keys) + "}"
        return str(val)

    @staticmethod
    def sha256_text(text):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    @staticmethod
    def verify(payload):
        header = payload.get("header", {})
        data = payload.get("data", {})
        schema = payload.get("schema", {})
        invariants = payload.get("invariants", [])

        # 1. Content Hash Verification
        exp_c_hash = BlindAXONVerifier.sha256_text(BlindAXONVerifier.canonical_json(data))
        if exp_c_hash != header.get("contentHash"):
            return "FALSE"

        # 2. Contract Hash Verification
        c_schema = BlindAXONVerifier.canonical_json(schema)
        c_inv = BlindAXONVerifier.canonical_json(sorted(invariants))
        exp_k_hash = BlindAXONVerifier.sha256_text(f"{c_schema}:{c_inv}")
        if exp_k_hash != header.get("contractHash"):
            return "FALSE"

        # 3. Invariant Rule Evaluation
        for expr in invariants:
            try:
                res = eval(expr, {"__builtins__": {}}, data)
                if not bool(res):
                    return "FALSE"
            except Exception:
                return "FALSE"

        return "TRUE"

def main():
    with open('conformance/vectors_500.json', 'r', encoding='utf-8') as f:
        vectors = json.load(f)

    passed = 0
    total = len(vectors)

    for vec in vectors:
        state = BlindAXONVerifier.verify(vec['payload'])
        if state == vec['expectedState']:
            passed += 1

    print("==================================================")
    print("AXON 1.0 Blind Verifier Interoperability Test:")
    print(f"  Total Vectors: {total}")
    print(f"  PASSED:        {passed} / {total} ({passed/total*100:.1f}%)")
    print("==================================================")

    if passed == total:
        print("✔ 100% BLIND VERIFIER INTEROPERABILITY PASSED")
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
