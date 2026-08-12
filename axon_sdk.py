#!/usr/bin/env python3
"""
AXON 1.0 Idiomatic Python SDK (axon_sdk.py)
Provides a clean, pythonic developer interface for creating, verifying, inspecting,
and transforming AXON computational objects.
"""

import json
import hashlib
from typing import Dict, List, Any, Optional, Tuple, Callable

class VerificationResult:
    def __init__(self, state: str, failures: Optional[List[str]] = None, reason: Optional[str] = None):
        self.state = state  # 'TRUE' | 'FALSE' | 'UNKNOWN' | 'UNVERIFIED'
        self.failures = failures or []
        self.reason = reason or ""

    @property
    def is_valid(self) -> bool:
        return self.state == "TRUE"

    def __repr__(self) -> str:
        return f"<VerificationResult state={self.state} failures={len(self.failures)}>"

class AxonObject:
    def __init__(self, raw_payload: Dict[str, Any]):
        self.payload = raw_payload
        self.header = raw_payload.get("header", {})
        self.data = raw_payload.get("data", {})
        self.schema = raw_payload.get("schema", {})
        self.invariants = raw_payload.get("invariants", [])
        self.transformation = raw_payload.get("transformation")
        self.signature = raw_payload.get("signature", "")

    def verify(self) -> VerificationResult:
        return Axon.verify(self.payload)

    def transform(
        self,
        transform_fn: Callable[[Dict[str, Any]], Dict[str, Any]],
        new_schema: Dict[str, str],
        additional_invariants: Optional[List[str]] = None
    ) -> 'AxonObject':
        new_data = transform_fn(self.data)
        inherited = [inv for inv in self.invariants if any(k in inv for k in new_data.keys())]
        combined = list(dict.fromkeys(inherited + (additional_invariants or [])))
        
        transformation = {
            "transformationId": f"tf_{self.header.get('semanticHash', '')[:8]}",
            "precondition": self.invariants,
            "postcondition": combined,
            "parentSemanticHash": self.header.get("semanticHash", "")
        }
        
        return Axon.create(new_data, new_schema, combined, transformation=transformation)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.payload, indent=indent)


class Axon:
    @staticmethod
    def canonicalize(obj: Any) -> str:
        if obj is None:
            return "null"
        if isinstance(obj, bool):
            return "true" if obj else "false"
        if isinstance(obj, (int, float)):
            return json.dumps(obj)
        if isinstance(obj, str):
            return json.dumps(obj)
        if isinstance(obj, list):
            return "[" + ",".join(Axon.canonicalize(x) for x in obj) + "]"
        if isinstance(obj, dict):
            keys = sorted(obj.keys())
            return "{" + ",".join(f"{json.dumps(k)}:{Axon.canonicalize(obj[k])}" for k in keys) + "}"
        return str(obj)

    @staticmethod
    def compute_content_hash(data: Dict[str, Any]) -> str:
        return hashlib.sha256(Axon.canonicalize(data).encode('utf-8')).hexdigest()

    @staticmethod
    def compute_contract_hash(schema: Dict[str, str], invariants: List[str]) -> str:
        c_s = Axon.canonicalize(schema)
        c_i = Axon.canonicalize(sorted(invariants))
        return hashlib.sha256(f"{c_s}:{c_i}".encode('utf-8')).hexdigest()

    @staticmethod
    def compute_semantic_hash(content_hash: str, contract_hash: str, parent_hash: str = "") -> str:
        return hashlib.sha256(f"{content_hash}:{contract_hash}:{parent_hash}".encode('utf-8')).hexdigest()

    @staticmethod
    def create(
        data: Dict[str, Any],
        schema: Optional[Dict[str, str]] = None,
        invariants: Optional[List[str]] = None,
        transformation: Optional[Dict[str, Any]] = None,
        node_id: str = "axon_python_sdk"
    ) -> AxonObject:
        schema = schema or {k: type(v).__name__ for k, v in data.items()}
        invariants = invariants or []
        
        c_hash = Axon.compute_content_hash(data)
        k_hash = Axon.compute_contract_hash(schema, invariants)
        parent_hash = transformation.get("parentSemanticHash", "") if transformation else ""
        s_hash = Axon.compute_semantic_hash(c_hash, k_hash, parent_hash)

        payload = {
            "header": {
                "version": "AXON/1.0",
                "uri": f"axon://payload/{s_hash[:16]}",
                "contentHash": c_hash,
                "contractHash": k_hash,
                "semanticHash": s_hash,
                "timestamp": 1700000000,
                "nodeId": node_id
            },
            "schema": schema,
            "invariants": invariants,
            "data": data,
            "transformation": transformation,
            "signature": "ed25519_sdk_signature_envelope"
        }
        return AxonObject(payload)

    @staticmethod
    def verify(payload_or_object: Any) -> VerificationResult:
        payload = payload_or_object.payload if isinstance(payload_or_object, AxonObject) else payload_or_object
        header = payload.get("header", {})
        data = payload.get("data", {})
        schema = payload.get("schema", {})
        invariants = payload.get("invariants", [])

        # 1. Content Hash Verification
        exp_c_hash = Axon.compute_content_hash(data)
        if exp_c_hash != header.get("contentHash"):
            return VerificationResult("FALSE", failures=[f"Content hash mismatch: {exp_c_hash} vs {header.get('contentHash')}"])

        # 2. Contract Hash Verification
        exp_k_hash = Axon.compute_contract_hash(schema, invariants)
        if exp_k_hash != header.get("contractHash"):
            return VerificationResult("FALSE", failures=[f"Contract hash mismatch: {exp_k_hash} vs {header.get('contractHash')}"])

        # 3. Semantic Hash Verification
        parent_hash = payload.get("transformation", {}).get("parentSemanticHash", "") if payload.get("transformation") else ""
        exp_s_hash = Axon.compute_semantic_hash(exp_c_hash, exp_k_hash, parent_hash)
        if exp_s_hash != header.get("semanticHash"):
            return VerificationResult("FALSE", failures=[f"Semantic hash mismatch: {exp_s_hash} vs {header.get('semanticHash')}"])

        # 4. Invariant VM Evaluation
        failures = []
        for expr in invariants:
            try:
                res = eval(expr, {"__builtins__": {}}, data)
                if not bool(res):
                    failures.append(f"Invariant rule evaluated to false: {expr}")
            except NameError as ne:
                return VerificationResult("UNKNOWN", reason=f"Missing variable binding: {str(ne)}")
            except Exception as e:
                failures.append(f"Evaluation error on '{expr}': {str(e)}")

        if failures:
            return VerificationResult("FALSE", failures=failures)

        return VerificationResult("TRUE")

if __name__ == '__main__':
    # SDK Quickstart Verification Test
    obj = Axon.create({"val": 100, "user": "alice"}, invariants=["val > 0", "user != ''"])
    res = obj.verify()
    print(f"✔ Python SDK Verification: state={res.state}, valid={res.is_valid}")
