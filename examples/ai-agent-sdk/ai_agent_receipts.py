#!/usr/bin/env python3
"""
AXON 1.0 AI Agent Tool Receipt & Verification SDK Example (Phase 12 & 13)
Demonstrates AI Tool Execution Output validation via AXON Object Receipts.
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from axon_sdk import Axon, AxonObject

class AIAgentReceiptManager:
    @staticmethod
    def generate_tool_receipt(agent_id: str, tool_name: str, parameters: dict, result: dict, invariant_rules: list) -> AxonObject:
        payload_data = {
            "agent_id": agent_id,
            "tool_name": tool_name,
            "parameters": parameters,
            "result": result
        }
        schema = {
            "agent_id": "string",
            "tool_name": "string",
            "parameters": "object",
            "result": "object"
        }
        return Axon.create(payload_data, schema, invariant_rules, node_id=f"agent_{agent_id}")

    @staticmethod
    def verify_tool_receipt(receipt: AxonObject) -> bool:
        res = receipt.verify()
        return res.is_valid

def main():
    print("--- 🤖 AI Agent Tool Execution Receipt Demo ---")
    
    # 1. AI Agent executes a tool function
    agent_id = "agent_llm_alpha"
    tool_name = "database_query"
    parameters = {"query": "SELECT balance FROM users WHERE id = 101"}
    result = {"user_id": 101, "balance": 1500.0, "currency": "USD"}
    invariants = ["result['balance'] >= 0", "result['currency'] == 'USD'"]

    # 2. Agent wraps tool output into AXON receipt
    receipt = AIAgentReceiptManager.generate_tool_receipt(agent_id, tool_name, parameters, result, invariants)
    print(f"✔ AI Agent generated receipt: {receipt.header['uri']}")

    # 3. Downstream system verifies receipt
    is_valid = AIAgentReceiptManager.verify_tool_receipt(receipt)
    print(f"✔ Downstream Verification Result: {'ACCEPTED' if is_valid else 'REJECTED'}")

if __name__ == '__main__':
    main()
