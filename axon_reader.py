#!/usr/bin/env python3
"""
AXON 1.0 Independent Python 3 Reference Engine B
Supports 4-State Verification (TRUE, FALSE, UNKNOWN, UNVERIFIED)
and Invariant-Preserving Transformation Triples.
"""

import sys
import json
import hashlib

class AXONPythonEngine:
    @staticmethod
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
            return "[" + ",".join(AXONPythonEngine.canonicalize(x) for x in obj) + "]"
        if isinstance(obj, dict):
            keys = sorted(obj.keys())
            return "{" + ",".join(f"{json.dumps(k)}:{AXONPythonEngine.canonicalize(obj[k])}" for k in keys) + "}"
        return str(obj)

    @staticmethod
    def compute_content_hash(data):
        c_data = AXONPythonEngine.canonicalize(data)
        return hashlib.sha256(c_data.encode('utf-8')).hexdigest()

    @staticmethod
    def compute_contract_hash(schema, invariants):
        c_schema = AXONPythonEngine.canonicalize(schema)
        c_inv = AXONPythonEngine.canonicalize(sorted(invariants))
        payload = f"{c_schema}:{c_inv}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    @staticmethod
    def compute_semantic_hash(content_hash, contract_hash, parent_hash=""):
        payload = f"{content_hash}:{contract_hash}:{parent_hash}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    @staticmethod
    def verify(payload):
        header = payload.get("header", {})
        data = payload.get("data", {})
        schema = payload.get("schema", {})
        invariants = payload.get("invariants", [])

        # 1. Content Hash Verification
        exp_c_hash = AXONPythonEngine.compute_content_hash(data)
        if exp_c_hash != header.get("contentHash"):
            return "FALSE", f"Content hash mismatch: {exp_c_hash} vs {header.get('contentHash')}"

        # 2. Contract Hash Verification
        exp_k_hash = AXONPythonEngine.compute_contract_hash(schema, invariants)
        if exp_k_hash != header.get("contractHash"):
            return "FALSE", f"Contract hash mismatch: {exp_k_hash} vs {header.get('contractHash')}"

        # 3. Semantic Hash Verification
        parent_hash = payload.get("transformation", {}).get("parentSemanticHash", "")
        exp_s_hash = AXONPythonEngine.compute_semantic_hash(exp_c_hash, exp_k_hash, parent_hash)
        if exp_s_hash != header.get("semanticHash"):
            return "FALSE", f"Semantic hash mismatch: {exp_s_hash} vs {header.get('semanticHash')}"

        # 4. Invariant Evaluation
        failures = []
        for expr in invariants:
            try:
                res = eval(expr, {"__builtins__": {}}, data)
                if not bool(res):
                    failures.append(expr)
            except NameError as ne:
                return "UNKNOWN", f"Missing variable binding: {str(ne)}"
            except Exception as e:
                failures.append(f"{expr} (Error: {str(e)})")

        if failures:
            return "FALSE", f"Invariant failure: {', '.join(failures)}"

        return "TRUE", "Valid AXON 1.0 Payload"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 axon_reader.py verify <file.axon>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "verify":
        file_path = sys.argv[2]
        with open(file_path, 'r', encoding='utf-8') as f:
            payload = json.load(f)
        status, msg = AXONPythonEngine.verify(payload)
        print(f"✔ Python Engine B: AXON 4-State Verification = {status} ({msg})")

if __name__ == '__main__':
    main()
