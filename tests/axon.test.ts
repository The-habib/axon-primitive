import test from 'node:test';
import assert from 'node:assert';
import { AXONEngine } from '../src/core/axon.ts';

test('AXON Engine A - Create, Invariant Evaluation, and Cryptographic Verification', () => {
  const data = { val: 100, record_count: 5 };
  const schema = { val: "number", record_count: "number" };
  const invariants = ["val > 0", "record_count >= 1"];

  const payload = AXONEngine.createAXON(data, schema, invariants);
  assert.ok(payload.uri.startsWith('axon://payload/'));
  assert.strictEqual(payload.contentHash.length, 64);

  const verification = AXONEngine.verifyAXON(payload);
  assert.strictEqual(verification.valid, true);

  // Invariant failure test
  const invalidData = { val: -50, record_count: 5 };
  const invalidPayload = AXONEngine.createAXON(invalidData, schema, invariants);
  const invalidVerify = AXONEngine.verifyAXON(invalidPayload);
  assert.strictEqual(invalidVerify.valid, false);
});
