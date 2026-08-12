/**
 * Standalone AXON WASM & Browser Native Verifier (Zero Dependencies)
 * Can run inside WebAssembly JS shims, Cloudflare Workers, Browsers, and Edge Runtimes.
 */

class AXONWasmVerifier {
  static canonicalize(obj) {
    if (obj === null || obj === undefined) return 'null';
    if (typeof obj !== 'object') return JSON.stringify(obj);
    if (Array.isArray(obj)) {
      return '[' + obj.map(item => this.canonicalize(item)).join(',') + ']';
    }
    const keys = Object.keys(obj).sort();
    const parts = keys.map(k => `${JSON.stringify(k)}:${this.canonicalize(obj[k])}`);
    return '{' + parts.join(',') + '}';
  }

  static async sha256(str) {
    if (typeof crypto !== 'undefined' && crypto.subtle) {
      const buffer = new TextEncoder().encode(str);
      const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }
    // Node.js fallback shim
    const nodeCrypto = await import('node:crypto');
    return nodeCrypto.createHash('sha256').update(str, 'utf8').digest('hex');
  }

  static async verify(payload) {
    const header = payload.header || {};
    const data = payload.data || {};
    const schema = payload.schema || {};
    const invariants = payload.invariants || [];

    const cData = this.canonicalize(data);
    const expCHash = await this.sha256(cData);
    if (expCHash !== header.contentHash) {
      return { state: 'FALSE', reason: `Content hash mismatch: ${expCHash}` };
    }

    const cSchema = this.canonicalize(schema);
    const cInv = this.canonicalize([...invariants].sort());
    const expKHash = await this.sha256(`${cSchema}:${cInv}`);
    if (expKHash !== header.contractHash) {
      return { state: 'FALSE', reason: `Contract hash mismatch: ${expKHash}` };
    }

    const parentHash = payload.transformation ? payload.transformation.parentSemanticHash : '';
    const expSHash = await this.sha256(`${expCHash}:${expKHash}:${parentHash}`);
    if (expSHash !== header.semanticHash) {
      return { state: 'FALSE', reason: `Semantic hash mismatch: ${expSHash}` };
    }

    // Invariant Rule Check
    const keys = Object.keys(data);
    const values = Object.values(data);
    for (const expr of invariants) {
      try {
        const fn = new Function(...keys, `"use strict"; return Boolean(${expr});`);
        if (!fn(...values)) {
          return { state: 'FALSE', reason: `Invariant condition evaluated to false: ${expr}` };
        }
      } catch (e) {
        if (e instanceof ReferenceError) {
          return { state: 'UNKNOWN', reason: `Missing variable binding: ${e.message}` };
        }
        return { state: 'FALSE', reason: `Execution error: ${e.message}` };
      }
    }

    return { state: 'TRUE', reason: 'Verified successfully in WASM runtime' };
  }
}

export default AXONWasmVerifier;
