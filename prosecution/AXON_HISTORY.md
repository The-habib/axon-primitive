# Historical Prior-Art Search & Decadal Taxonomy (prosecution/AXON_HISTORY.md)

## 1. Historical Literature Search (1960s–2020s)

### 1960s–1970s: The Foundations of Programmed Execution & Data Logic
- **1972 (Prolog - Colmerauer & Kowalski)**: Logic programming uniting data structures with executable Horn-clause evaluation. Prior art for declarative predicate evaluation over tuples.

### 1980s: Self-Describing Formats & Design by Contract
- **1982 (PostScript - Adobe Systems)**: Executable stack-based document language where the document is a program that draws itself upon execution. Direct prior art for code embedded in document files.
- **1984 (ASN.1 - ITU-T)**: Self-describing binary type serialization standard.
- **1988 (Eiffel Design by Contract - Bertrand Meyer)**: First-class `require`, `ensure`, and `invariant` clauses bound to class methods and data state.

### 1990s: Mobile Code, Active Messages & Proof-Carrying Code
- **1992 (Active Messages - Thorsten von Eicken et al., ISCA '92)**: Network packets carrying the address of an execution handler to process payload data immediately upon receipt. Direct prior art for executable network data.
- **1996 (Proof-Carrying Code - George Necula, OSDI '96)**: Binaries embedding formal safety proofs ($\mathcal{P}$) evaluated by the host before execution. Direct prior art for self-evaluating safety predicates embedded in payloads.
- **1997 (PDF with Embedded JavaScript - Adobe)**: PDF documents carrying embedded JavaScript code executed upon page render.

### 2000s: Content Addressing, Refinement Types & Contracts
- **2002 (Venti CAS - Plan 9, Sean Quinlan & Sean Dorward)**: SHA-1 content-addressed storage block system.
- **2002 (Racket Higher-Order Contracts - Findler & Felleisen, ICFP '02)**: Dynamic contract verification attached to data boundaries.
- **2004 (Nix Store - Eelco Dolstra)**: Content-addressed store paths binding source code to execution outputs.
- **2005 (Git Object Model - Linus Torvalds)**: SHA-1 Merkle tree commit objects.
- **2008 (LiquidHaskell - Ranjeet Jhala et al.)**: Refinement types embedding logical predicates into static type signatures.

### 2010s: Smart Contracts, eBPF, CEL & Proof-Carrying Data
- **2013 (Proof-Carrying Data - Alessandro Chiesa et al., EUROCRYPT '13)**: Distributed computations where every message carries a cryptographic proof of state correctness.
- **2014 (eBPF - Linux Kernel)**: Stack-bounded, verified bytecode executed inside the kernel to validate network packet invariants safely.
- **2015 (Ethereum EVM - Vitalik Buterin)**: Content-addressed smart contract code coupled with state storage executing deterministic transition rules.
- **2019 (Common Expression Language CEL - Google)**: Lightweight, non-Turing-complete, fast expression language designed for embedding constraint evaluation inside data structures.

### 2020s: CosmWasm & Move Bytecode
- **2020 (CosmWasm / Move VM)**: Content-addressed WebAssembly and Move modules executing deterministic state invariant checks over JSON/BCS payloads.

---

## 2. Key Takeaway from Historical Search
The concept of embedding executable predicates into data payloads is **NOT** a new discovery of 2026. It has evolved across **PostScript (1982)**, **Active Messages (1992)**, **Proof-Carrying Code (1996)**, **Proof-Carrying Data (2013)**, and **Google CEL (2019)** over 44 years of computing history.
