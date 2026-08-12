#!/usr/bin/env python3
"""
AXON 1.0 Irreducible Minimal Engine (gauntlet/axon_minimal.py)
Implemented in 40 lines of pure standard Python.
"""
import json, hashlib

class AXONMinimal:
    @staticmethod
    def canonicalize(obj):
        if isinstance(obj, dict):
            return "{" + ",".join(f"{json.dumps(k)}:{AXONMinimal.canonicalize(obj[k])}" for k in sorted(obj.keys())) + "}"
        if isinstance(obj, list):
            return "[" + ",".join(AXONMinimal.canonicalize(x) for x in obj) + "]"
        return json.dumps(obj) if isinstance(obj, str) else str(obj)

    @staticmethod
    def pack(data: dict, invariants: list) -> dict:
        c_data = AXONMinimal.canonicalize(data)
        c_inv = AXONMinimal.canonicalize(sorted(invariants))
        h_sem = hashlib.sha256(f"{c_data}:{c_inv}".encode('utf-8')).hexdigest()
        return {"semanticHash": h_sem, "data": data, "invariants": invariants}

    @staticmethod
    def verify(obj: dict) -> bool:
        c_data = AXONMinimal.canonicalize(obj["data"])
        c_inv = AXONMinimal.canonicalize(sorted(obj["invariants"]))
        exp_hash = hashlib.sha256(f"{c_data}:{c_inv}".encode('utf-8')).hexdigest()
        if exp_hash != obj["semanticHash"]:
            return False
        for inv in obj["invariants"]:
            try:
                if not bool(eval(inv, {"__builtins__": {}}, obj["data"])): return False
            except Exception: return False
        return True

if __name__ == '__main__':
    pack = AXONMinimal.pack({"val": 100}, ["val > 0"])
    print(f"✔ Irreducible Minimal Engine Verification: {AXONMinimal.verify(pack)} (Hash: {pack['semanticHash'][:16]})")
