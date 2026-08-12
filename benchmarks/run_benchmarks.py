#!/usr/bin/env python3
"""
AXON 1.0 Performance & Competitive Benchmark Suite
"""

import sys
import os
import time
import json
import hashlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from axon_reader import AXONPythonEngine

def benchmark_payload_size(size_kb):
    padding = "X" * (size_kb * 1024)
    data = {"val": 100, "padding": padding}
    schema = {"val": "number", "padding": "string"}
    invariants = ["val > 0", "len(padding) > 0"]

    c_hash = AXONPythonEngine.compute_content_hash(data)
    k_hash = AXONPythonEngine.compute_contract_hash(schema, invariants)
    s_hash = AXONPythonEngine.compute_semantic_hash(c_hash, k_hash)

    payload = {
        "header": {"version": "AXON/1.0", "contentHash": c_hash, "contractHash": k_hash, "semanticHash": s_hash},
        "data": data, "schema": schema, "invariants": invariants
    }

    t0 = time.perf_counter()
    iterations = 50
    for _ in range(iterations):
        AXONPythonEngine.verify(payload)
    t1 = time.perf_counter()

    avg_ms = ((t1 - t0) / iterations) * 1000.0
    return avg_ms

def main():
    print("==================================================")
    print("AXON 1.0 Physical Verification Latency Benchmarks:")
    print("==================================================")

    sizes = [1, 10, 100, 1000]
    for sz in sizes:
        lat = benchmark_payload_size(sz)
        print(f"  Payload Size: {sz:4d} KB  --> Measured Verification Latency: {lat:.3f} ms")

    print("==================================================")
    print("Competitive Architectural Comparison Matrix:")
    print("==================================================")
    print("  Tool          Zero Cloud  Offline Mobile  Self-Evaluating  Portable Pack")
    print("  JSON Schema      YES           YES              NO              NO")
    print("  Pydantic         YES           NO (Python only) NO              NO")
    print("  AXON 1.0         YES           YES (Termux)     YES             YES")
    print("==================================================")

if __name__ == '__main__':
    main()
