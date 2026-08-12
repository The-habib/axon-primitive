# Systems Comparison Matrix (deepaxon/SYSTEM_COMPARISON.md)

| System Family | Representative Technology | Primary Abstraction Model | AXON Overlap & Difference |
| :--- | :--- | :--- | :--- |
| **Content-Addressed Storage** | Git, IPFS, Venti | Immutable SHA-256 Merkle Blobs | AXON reuses SHA-256 CAS for data identity. |
| **Build & Package Closures** | Nix, Bazel, Buck | Hermetic Build Graphs | Nix versions package closures; AXON validates payload internal invariants. |
| **Policy-as-Code Engines** | OPA (Rego), Google CEL | Declarative Expression Evaluator | OPA evaluates policies against JSON; AXON couples policy into payload signature envelope. |
| **Smart Contract Runtimes** | Ethereum EVM, CosmWasm | Deterministic State Transitions | EVM state requires blockchain consensus ledger; AXON is an offline standalone file payload (`.axon`). |
| **Micro-Runtime Sandboxes** | WebAssembly (WASI), eBPF | Isolated Stack Bytecode Evaluator | WASM executes arbitrary WebAssembly modules; AXON uses lightweight boolean string expressions. |
