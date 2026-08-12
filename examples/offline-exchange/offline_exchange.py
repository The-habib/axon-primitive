#!/usr/bin/env python3
"""
AXON 1.0 Offline-First Mobile Data Exchange Demonstrator (Phase 11)
Demonstrates zero-cloud device-to-device verifiable data transfer over mobile/Termux ARM64.
"""

import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from axon_sdk import Axon

def main():
    print("--- 📱 AXON 1.0 Offline Mobile Data Exchange Demo ---")

    # Phone A (Offline creation in Termux)
    phone_a_data = {
        "device": "Android_Phone_A",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "battery_pct": 88
    }
    phone_a_invariants = ["latitude >= -90.0", "latitude <= 90.0", "battery_pct > 10"]

    payload_a = Axon.create(phone_a_data, invariants=phone_a_invariants, node_id="termux_phone_a")
    print(f"✔ Phone A created offline payload: {payload_a.header['uri']}")

    # Transfer payload file via local Bluetooth/WiFi-Direct (Simulated)
    serialized_bytes = payload_a.to_json()
    print(f"✔ Transferred {len(serialized_bytes)} bytes over local transport (0.00 ms network time)")

    # Phone B (Offline verification in Termux)
    received_payload = json.loads(serialized_bytes)
    result = Axon.verify(received_payload)

    print(f"✔ Phone B Verification: State = {result.state}, Valid = {result.is_valid}")
    if result.is_valid:
        print("✔ Phone B accepted offline telemetry from Phone A")

if __name__ == '__main__':
    main()
