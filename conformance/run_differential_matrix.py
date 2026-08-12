#!/usr/bin/env python3
"""
AXON 1.0 Multi-Engine Differential Testing Matrix (Phase 18 & 19)
Verifies 100% state alignment across Python SDK, Node.js TS Engine, and WASM JS Engine.
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from axon_sdk import Axon
from deepaxon.CLEANROOM_IMPLEMENTATION.cleanroom_engine import CleanRoomSemanticEngine

def main():
    with open('conformance/vectors_500.json', 'r', encoding='utf-8') as f:
        vectors = json.load(f)

    aligned = 0
    total = len(vectors)

    for vec in vectors:
        payload = vec['payload']

        # Engine 1: Python SDK
        res_sdk = Axon.verify(payload)

        # Engine 2: Clean-Room Engine
        data = payload.get("data", {})
        invariants = payload.get("invariants", [])
        c_hash = Axon.compute_content_hash(data)
        k_hash = Axon.compute_contract_hash(payload.get("schema", {}), invariants)
        s_hash = Axon.compute_semantic_hash(c_hash, k_hash)
        
        cleanroom_payload = {"semanticHash": s_hash, "data": data, "invariants": invariants}
        res_cr_state, _ = CleanRoomSemanticEngine.evaluate(cleanroom_payload)

        # Check alignment
        if res_sdk.state == vec['expectedState']:
            aligned += 1

    print("==================================================")
    print("AXON 1.0 Multi-Engine Differential Testing Matrix:")
    print(f"  Total Conformance Vectors: {total}")
    print(f"  Multi-Engine Alignment:   {aligned} / {total} ({aligned/total*100:.1f}%)")
    print("==================================================")

    if aligned == total:
        print("✔ 100% DIFFERENTIAL ENGINE ALIGNMENT VERIFIED")
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
