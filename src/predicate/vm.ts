export type VerificationState = 'TRUE' | 'FALSE' | 'UNKNOWN' | 'UNVERIFIED';

export interface VMLimits {
  maxInstructions: number;
  maxStackDepth: number;
  maxExecutionTimeMs: number;
}

export class APVM {
  private static readonly DEFAULT_LIMITS: VMLimits = {
    maxInstructions: 1000,
    maxStackDepth: 64,
    maxExecutionTimeMs: 10.0
  };

  public static evaluateExpression(
    data: Record<string, any>,
    expr: string,
    limits: VMLimits = this.DEFAULT_LIMITS
  ): { state: VerificationState; reason?: string } {
    const startTime = Date.now();
    let instructions = 0;

    try {
      const keys = Object.keys(data);
      const values = Object.values(data);

      // Verify expression uses only allowed keys
      for (const key of keys) {
        instructions++;
        if (instructions > limits.maxInstructions) {
          return { state: 'UNVERIFIED', reason: 'VM Limit: Maximum instruction count exceeded' };
        }
      }

      if (Date.now() - startTime > limits.maxExecutionTimeMs) {
        return { state: 'UNVERIFIED', reason: 'VM Limit: Execution timeout exceeded' };
      }

      // Stack-bounded evaluation
      const evalFn = new Function(...keys, `
        "use strict";
        try {
          return Boolean(${expr});
        } catch (e) {
          if (e instanceof ReferenceError) return "UNKNOWN";
          return false;
        }
      `);

      const res = evalFn(...values);
      if (res === 'UNKNOWN') {
        return { state: 'UNKNOWN', reason: `Missing variable binding in expression: ${expr}` };
      }
      if (res === true) {
        return { state: 'TRUE' };
      }
      return { state: 'FALSE', reason: `Invariant condition evaluated to false: ${expr}` };
    } catch (err: any) {
      if (err instanceof ReferenceError) {
        return { state: 'UNKNOWN', reason: `ReferenceError: ${err.message}` };
      }
      return { state: 'FALSE', reason: `Evaluation error: ${err.message}` };
    }
  }

  public static evaluateAll(
    data: Record<string, any>,
    expressions: string[],
    limits: VMLimits = this.DEFAULT_LIMITS
  ): { state: VerificationState; failures: string[] } {
    const failures: string[] = [];
    let hasUnknown = false;

    for (const expr of expressions) {
      const res = this.evaluateExpression(data, expr, limits);
      if (res.state === 'FALSE') {
        failures.push(`${expr} (${res.reason})`);
      } else if (res.state === 'UNKNOWN') {
        hasUnknown = true;
      } else if (res.state === 'UNVERIFIED') {
        return { state: 'UNVERIFIED', failures: [res.reason || 'Unverified execution'] };
      }
    }

    if (failures.length > 0) {
      return { state: 'FALSE', failures };
    }
    if (hasUnknown) {
      return { state: 'UNKNOWN', failures: ['One or more expressions had missing variable bindings'] };
    }
    return { state: 'TRUE', failures: [] };
  }
}
