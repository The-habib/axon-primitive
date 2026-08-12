#!/usr/bin/env python3
"""
Generates 20 Production-Grade AXON 1.0 Real-World Workloads
"""

import os
import json
import hashlib

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
        return "[" + ",".join(canonicalize(x) for x in obj) + "]"
    if isinstance(obj, dict):
        keys = sorted(obj.keys())
        return "{" + ",".join(f"{json.dumps(k)}:{canonicalize(obj[k])}" for k in keys) + "}"
    return str(obj)

def create_workload(filename, data, schema, invariants, node_id="production_node"):
    c_hash = hashlib.sha256(canonicalize(data).encode('utf-8')).hexdigest()
    k_hash = hashlib.sha256(f"{canonicalize(schema)}:{canonicalize(sorted(invariants))}".encode('utf-8')).hexdigest()
    s_hash = hashlib.sha256(f"{c_hash}:{k_hash}:".encode('utf-8')).hexdigest()

    payload = {
        "header": {
            "version": "AXON/1.0",
            "uri": f"axon://production/{s_hash[:16]}",
            "contentHash": c_hash,
            "contractHash": k_hash,
            "semanticHash": s_hash,
            "timestamp": 1700000000,
            "nodeId": node_id
        },
        "schema": schema,
        "invariants": invariants,
        "data": data,
        "signature": "ed25519_production_signature_envelope"
    }

    os.makedirs('examples/production', exist_ok=True)
    with open(f"examples/production/{filename}", 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)

def main():
    # 1. AI Agent Tool Output
    create_workload("01_ai_agent_tool_output.json", 
                    {"tool": "calculator", "result": 42, "confidence": 0.99}, 
                    {"tool": "string", "result": "number", "confidence": "number"}, 
                    ["confidence >= 0.95", "result == 42"])

    # 2. CSV ETL Pipeline
    create_workload("02_csv_etl_pipeline.json", 
                    {"rows_processed": 5000, "error_count": 0}, 
                    {"rows_processed": "number", "error_count": "number"}, 
                    ["rows_processed > 0", "error_count == 0"])

    # 3. Financial Transaction
    create_workload("03_financial_transaction.json", 
                    {"account_id": "ACC_9981", "amount": 250.0, "balance_after": 1250.0}, 
                    {"account_id": "string", "amount": "number", "balance_after": "number"}, 
                    ["amount > 0", "balance_after >= 0"])

    # 4. IoT Sensor Stream
    create_workload("04_iot_sensor_stream.json", 
                    {"device_id": "sensor_arm64", "temp_celsius": 22.5, "humidity": 45.0}, 
                    {"device_id": "string", "temp_celsius": "number", "humidity": "number"}, 
                    ["temp_celsius >= -40", "temp_celsius <= 85"])

    # 5. Mobile Offline Sync
    create_workload("05_mobile_offline_sync.json", 
                    {"device": "Termux_ARM64", "local_changes": 12, "sync_status": "PENDING"}, 
                    {"device": "string", "local_changes": "number", "sync_status": "string"}, 
                    ["local_changes >= 0"])

    # 6. ML Feature Store
    create_workload("06_ml_feature_store.json", 
                    {"feature_vector": [0.1, 0.4, 0.9], "dimension": 3}, 
                    {"feature_vector": "array", "dimension": "number"}, 
                    ["dimension == 3"])

    # 7. API Gateway Payload
    create_workload("07_api_gateway_payload.json", 
                    {"status_code": 200, "latency_ms": 14.2}, 
                    {"status_code": "number", "latency_ms": "number"}, 
                    ["status_code == 200", "latency_ms < 100"])

    # 8. Scientific Dataset
    create_workload("08_scientific_dataset.json", 
                    {"sample_id": "SAMPLE_404", "pressure_pascal": 101325.0}, 
                    {"sample_id": "string", "pressure_pascal": "number"}, 
                    ["pressure_pascal > 0"])

    # 9. Build Artifact Metadata
    create_workload("09_build_artifact_metadata.json", 
                    {"target": "axon_arm64.bin", "checksum_match": True}, 
                    {"target": "string", "checksum_match": "boolean"}, 
                    ["checksum_match == True"])

    # 10. User Authentication Claim
    create_workload("10_user_authentication_claim.json", 
                    {"user_id": "usr_771", "role": "admin", "token_valid": True}, 
                    {"user_id": "string", "role": "string", "token_valid": "boolean"}, 
                    ["token_valid == True"])

    # Generate remaining 10 workloads
    for i in range(11, 21):
        create_workload(f"{i:02d}_production_workload.json", 
                        {"workload_id": i, "status_ok": True}, 
                        {"workload_id": "number", "status_ok": "boolean"}, 
                        ["workload_id >= 11", "status_ok == True"])

    print("✔ Successfully generated 20 Production Workloads in examples/production/")

if __name__ == '__main__':
    main()
