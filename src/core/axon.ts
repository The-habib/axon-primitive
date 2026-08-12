import * as crypto from 'node:crypto';

export interface AXONPayload {
  version: string; // "AXON/1.0"
  uri: string;     // "axon://payload/<hash>"
  contentHash: string;
  timestamp: number;
  data: Record<string, any>;
  schema: Record<string, string>;
  invariants: string[]; // e.g. ["val > 0", "record_count >= 1"]
  nodeId: string;
  signature: string;
}

export class AXONEngine {
  public static canonicalize(data: Record<string, any>): string {
    const keys = Object.keys(data).sort();
    const sortedObj: Record<string, any> = {};
    for (const key of keys) {
      sortedObj[key] = data[key];
    }
    return JSON.stringify(sortedObj);
  }

  public static hashPayload(data: Record<string, any>): string {
    const canonical = this.canonicalize(data);
    return crypto.createHash('sha256').update(canonical, 'utf8').digest('hex');
  }

  public static signPayload(hash: string, privateKeyPem?: string): { signature: string; publicKeyPem: string } {
    if (!privateKeyPem) {
      const { privateKey, publicKey } = crypto.generateKeyPairSync('ed25519');
      const sig = crypto.sign(null, Buffer.from(hash), privateKey).toString('hex');
      return {
        signature: sig,
        publicKeyPem: publicKey.export({ type: 'spki', format: 'pem' }).toString()
      };
    }
    const sig = crypto.sign(null, Buffer.from(hash), privateKeyPem).toString('hex');
    return { signature: sig, publicKeyPem: '' };
  }

  public static evaluateInvariants(data: Record<string, any>, invariants: string[]): { passed: boolean; failures: string[] } {
    const failures: string[] = [];
    for (const inv of invariants) {
      try {
        const keys = Object.keys(data);
        const vals = Object.values(data);
        const fn = new Function(...keys, `return Boolean(${inv});`);
        const ok = fn(...vals);
        if (!ok) failures.push(inv);
      } catch (err: any) {
        failures.push(`${inv} (Error: ${err.message})`);
      }
    }
    return { passed: failures.length === 0, failures };
  }

  public static createAXON(
    data: Record<string, any>,
    schema: Record<string, string>,
    invariants: string[] = [],
    nodeId: string = 'axon_node_01'
  ): AXONPayload {
    const contentHash = this.hashPayload(data);
    const { signature } = this.signPayload(contentHash);
    return {
      version: 'AXON/1.0',
      uri: `axon://payload/${contentHash.substring(0, 16)}`,
      contentHash,
      timestamp: Date.now(),
      data,
      schema,
      invariants,
      nodeId,
      signature
    };
  }

  public static verifyAXON(payload: AXONPayload): { valid: boolean; reason?: string } {
    const expectedHash = this.hashPayload(payload.data);
    if (expectedHash !== payload.contentHash) {
      return { valid: false, reason: `Content hash mismatch: expected ${expectedHash}, got ${payload.contentHash}` };
    }

    const invResult = this.evaluateInvariants(payload.data, payload.invariants);
    if (!invResult.passed) {
      return { valid: false, reason: `Invariant evaluation failed: ${invResult.failures.join(', ')}` };
    }

    return { valid: true };
  }
}
