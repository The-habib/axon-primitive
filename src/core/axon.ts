import * as crypto from 'node:crypto';
import { APVM, type VerificationState } from '../predicate/vm.ts';

export interface AXONHeader {
  version: string;     // "AXON/1.0"
  uri: string;         // "axon://payload/<semanticHash>"
  contentHash: string;
  contractHash: string;
  semanticHash: string;
  timestamp: number;
  nodeId: string;
}

export interface AXONTransformation {
  transformationId: string;
  precondition: string[];
  postcondition: string[];
  parentSemanticHash: string;
}

export interface AXONPayload {
  header: AXONHeader;
  schema: Record<string, string>;
  invariants: string[];
  data: Record<string, any>;
  transformation?: AXONTransformation;
  signature: string;
}

export class AXONEngine {
  public static canonicalize(obj: any): string {
    if (obj === null || obj === undefined) return 'null';
    if (typeof obj !== 'object') return JSON.stringify(obj);
    if (Array.isArray(obj)) {
      return '[' + obj.map(item => this.canonicalize(item)).join(',') + ']';
    }
    const keys = Object.keys(obj).sort();
    const parts = keys.map(k => `${JSON.stringify(k)}:${this.canonicalize(obj[k])}`);
    return '{' + parts.join(',') + '}';
  }

  public static computeContentHash(data: Record<string, any>): string {
    const cData = this.canonicalize(data);
    return crypto.createHash('sha256').update(cData, 'utf8').digest('hex');
  }

  public static computeContractHash(schema: Record<string, string>, invariants: string[]): string {
    const cSchema = this.canonicalize(schema);
    const cInv = this.canonicalize([...invariants].sort());
    return crypto.createHash('sha256').update(`${cSchema}:${cInv}`, 'utf8').digest('hex');
  }

  public static computeSemanticHash(contentHash: string, contractHash: string, parentHash: string = ''): string {
    return crypto.createHash('sha256').update(`${contentHash}:${contractHash}:${parentHash}`, 'utf8').digest('hex');
  }

  public static signHash(hash: string, privateKeyPem?: string): string {
    if (!privateKeyPem) {
      const { privateKey } = crypto.generateKeyPairSync('ed25519');
      return crypto.sign(null, Buffer.from(hash), privateKey).toString('hex');
    }
    return crypto.sign(null, Buffer.from(hash), privateKeyPem).toString('hex');
  }

  public static createAXON(
    data: Record<string, any>,
    schema: Record<string, string>,
    invariants: string[] = [],
    transformation?: AXONTransformation,
    nodeId: string = 'axon_node_01'
  ): AXONPayload {
    const contentHash = this.computeContentHash(data);
    const contractHash = this.computeContractHash(schema, invariants);
    const parentHash = transformation ? transformation.parentSemanticHash : '';
    const semanticHash = this.computeSemanticHash(contentHash, contractHash, parentHash);
    const signature = this.signHash(semanticHash);

    return {
      header: {
        version: 'AXON/1.0',
        uri: `axon://payload/${semanticHash.substring(0, 16)}`,
        contentHash,
        contractHash,
        semanticHash,
        timestamp: Date.now(),
        nodeId
      },
      schema,
      invariants,
      data,
      transformation,
      signature
    };
  }

  public static verifyAXON(payload: AXONPayload): { state: VerificationState; failures: string[] } {
    const expectedContentHash = this.computeContentHash(payload.data);
    if (expectedContentHash !== payload.header.contentHash) {
      return { state: 'FALSE', failures: [`Content hash mismatch: expected ${expectedContentHash}, got ${payload.header.contentHash}`] };
    }

    const expectedContractHash = this.computeContractHash(payload.schema, payload.invariants);
    if (expectedContractHash !== payload.header.contractHash) {
      return { state: 'FALSE', failures: [`Contract hash mismatch: expected ${expectedContractHash}, got ${payload.header.contractHash}`] };
    }

    const parentHash = payload.transformation ? payload.transformation.parentSemanticHash : '';
    const expectedSemanticHash = this.computeSemanticHash(expectedContentHash, expectedContractHash, parentHash);
    if (expectedSemanticHash !== payload.header.semanticHash) {
      return { state: 'FALSE', failures: [`Semantic hash mismatch: expected ${expectedSemanticHash}, got ${payload.header.semanticHash}`] };
    }

    if (!payload.signature) {
      return { state: 'UNVERIFIED', failures: ['Signature envelope missing'] };
    }

    // Evaluate AP-VM Invariants
    const evalResult = APVM.evaluateAll(payload.data, payload.invariants);
    return evalResult;
  }

  public static transform(
    parent: AXONPayload,
    transformFn: (data: Record<string, any>) => Record<string, any>,
    newSchema: Record<string, string>,
    additionalInvariants: string[] = []
  ): AXONPayload {
    const newData = transformFn(parent.data);
    const inheritedInvariants = parent.invariants.filter(inv => {
      // Retain invariant if keys exist in new data
      const keys = Object.keys(newData);
      return keys.some(k => inv.includes(k));
    });
    const combinedInvariants = Array.from(new Set([...inheritedInvariants, ...additionalInvariants]));

    const transformation: AXONTransformation = {
      transformationId: `tf_${Date.now()}`,
      precondition: parent.invariants,
      postcondition: combinedInvariants,
      parentSemanticHash: parent.header.semanticHash
    };

    return this.createAXON(newData, newSchema, combinedInvariants, transformation, parent.header.nodeId);
  }

  public static query(payloads: AXONPayload[], queryPredicate: string): AXONPayload[] {
    return payloads.filter(p => {
      const res = APVM.evaluateExpression(p.data, queryPredicate);
      return res.state === 'TRUE';
    });
  }
}
