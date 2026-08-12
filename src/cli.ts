import * as fs from 'node:fs';
import * as path from 'node:path';
import { AXONEngine } from './core/axon.ts';

function main() {
  const args = process.argv.slice(2);
  const cmd = args[0] || 'help';

  console.log("============================================================");
  console.log("AXON v1.0 — Autonomous Executable Invariant Data Primitive");
  console.log("============================================================\n");

  if (cmd === 'create') {
    const dataArg = args[1] || '{"val":100,"record_count":5}';
    const data = JSON.parse(dataArg);
    const schema = { val: "number", record_count: "number" };
    const invariants = ["val > 0", "record_count >= 1"];
    
    const payload = AXONEngine.createAXON(data, schema, invariants);
    console.log(`✔ Created AXON Primitive: ${payload.uri}`);
    console.log(`  Content Hash : ${payload.contentHash}`);
    console.log(`  Signature    : ${payload.signature.substring(0, 24)}...`);
    console.log(`\nPayload JSON:\n${JSON.stringify(payload, null, 2)}`);
  } else if (cmd === 'verify') {
    const file = args[1];
    if (!file || !fs.existsSync(file)) {
      console.log("Error: Specify a valid .axon JSON payload file");
      process.exit(1);
    }
    const payload = JSON.parse(fs.readFileSync(file, 'utf-8'));
    const result = AXONEngine.verifyAXON(payload);
    if (result.valid) {
      console.log(`✔ AXON Primitive is 100% VALID & VERIFIED (${payload.uri})`);
    } else {
      console.log(`✖ AXON Verification Failed: ${result.reason}`);
      process.exit(1);
    }
  } else {
    console.log("Usage:");
    console.log("  node --experimental-strip-types src/cli.ts create '{\"val\":100,\"record_count\":5}'");
    console.log("  node --experimental-strip-types src/cli.ts verify my_data.axon");
  }
}

main();
