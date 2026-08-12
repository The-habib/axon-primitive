#!/usr/bin/env python3
"""
AXON 1.0 500-Vector Matrix Runner
Executes all 500 test vectors across independent reference engines.
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from axon_reader import AXONPythonEngine

def main():
    with open('conformance/vectors_500.json', 'r', encoding='utf-8') as f:
        vectors = json.load(f)

    passed = 0
    failed = 0

    for vec in vectors:
        vec_id = vec['id']
        expected = vec['expectedState']
        payload = vec['payload']

        status, msg = AXONPythonEngine.verify(payload)
        if status == expected:
            passed += 1
        else:
            failed += 1
            print(f"❌ MISMATCH in {vec_id}: expected {expected}, got {status} ({msg})")

    print("==================================================")
    print(f"AXON 1.0 500-Vector Matrix Runner Results:")
    print(f"  Total Vectors: {len(vectors)}")
    print(f"  PASSED:        {passed} ({passed / len(vectors) * 100:.1f}%)")
    print(f"  FAILED:        {failed}")
    print("==================================================")

    if failed == 0:
        print("✔ 100% CONFORMANCE MATRIX PASSED")
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
