#!/usr/bin/env python3
"""
Semantic Identity Engine #1: Pure Python 3 Implementation
"""
import json, hashlib

class SemanticIdentityEngine:
    @staticmethod
    def compute_semantic_identity(data, invariants):
        c_data = json.dumps({k: data[k] for k in sorted(data.keys())}, separators=(',', ':'))
        c_inv = json.dumps(sorted(invariants), separators=(',', ':'))
        payload = f"{c_data}:{c_inv}"
        content_hash = hashlib.sha256(c_data.encode('utf-8')).hexdigest()
        contract_hash = hashlib.sha256(c_inv.encode('utf-8')).hexdigest()
        semantic_hash = hashlib.sha256(payload.encode('utf-8')).hexdigest()
        return {
            "content_hash": content_hash,
            "contract_hash": contract_hash,
            "semantic_hash": semantic_hash
        }

if __name__ == '__main__':
    res = SemanticIdentityEngine.compute_semantic_identity({"val": 100}, ["val > 0"])
    print(f"✔ Python Engine #1 Semantic Identity: {res['semantic_hash']}")
