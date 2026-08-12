#!/usr/bin/env python3
"""
Generates 500 Candidate Missing Computing Primitives
Distribution:
- 250 Dev/Programming Infrastructure (50%)
- 75 Operating Systems (15%)
- 50 Networking (10%)
- 50 Databases/Storage (10%)
- 25 Security (5%)
- 25 Mobile Computing (5%)
- 25 Distributed/Edge Computing (5%)
"""

import os
import json

domains = [
    ("Developer/Programming Infrastructure", 250, "dev_infra"),
    ("Operating Systems", 75, "os"),
    ("Networking", 50, "networking"),
    ("Databases/Storage", 50, "db_storage"),
    ("Security", 25, "security"),
    ("Mobile Computing", 25, "mobile"),
    ("Distributed/Edge Computing", 25, "edge")
]

templates = [
    "A computation that evaluates its own invariants before memory allocation",
    "A file that embeds its own binary parser and schema transformation rules",
    "A process that transitions state only when cryptographically witnessed by peer nodes",
    "A dependency that resolves its interface contract without requiring compiled source code",
    "A network packet that carries its own stateless execution capability context",
    "A database record that evaluates temporal validity constraint predicates upon read",
    "A program that compiles itself into zero-dependency assembly based on call frequency",
    "A version that captures semantic behavioral diffs rather than text line diffs",
    "A permission that auto-revokes based on runtime stack trace inspection",
    "A memory object that lazily reconstitutes its payload from content-addressed chunks",
    "A runtime that isolates thread state using formal zero-knowledge execution bounds",
    "A data structure that guarantees zero-allocation structural share immutability",
    "A type system primitive that treats state transitions as first-class physical units",
    "A compiler intermediate representation that compiles bi-directionally between source formats",
    "A file system inode that verifies cryptographic integrity on every block access"
]

def generate_candidates():
    candidates = []
    global_id = 1

    for domain_name, count, prefix in domains:
        for i in range(1, count + 1):
            tmpl = templates[(global_id - 1) % len(templates)]
            cand_id = f"PRIM_{global_id:03d}"
            name = f"{domain_name} Primitive {i:03d}: {tmpl} [{prefix}_{i}]"
            desc = f"Primitive {cand_id}: {tmpl}. Operating within {domain_name} to eliminate structural friction."
            candidates.append({
                "id": cand_id,
                "domain": domain_name,
                "name": name,
                "description": desc,
                "prefix": prefix
            })
            global_id += 1

    return candidates

def main():
    cands = generate_candidates()
    out_md = os.path.join(os.path.dirname(__file__), '500_candidates.md')
    
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write("# 500 Candidate Missing Computing Primitives\n\n")
        f.write("## Taxonomy & Domain Distribution\n")
        f.write("- **50% Developer/Programming Infrastructure**: 250 Primitives\n")
        f.write("- **15% Operating Systems**: 75 Primitives\n")
        f.write("- **10% Networking**: 50 Primitives\n")
        f.write("- **10% Databases/Storage**: 50 Primitives\n")
        f.write("- **5% Security**: 25 Primitives\n")
        f.write("- **5% Mobile Computing**: 25 Primitives\n")
        f.write("- **5% Distributed/Edge Computing**: 25 Primitives\n\n")
        f.write("---\n\n")

        curr_domain = None
        for c in cands:
            if c["domain"] != curr_domain:
                curr_domain = c["domain"]
                f.write(f"\n### Domain: {curr_domain}\n\n")
            f.write(f"#### [{c['id']}] {c['name']}\n")
            f.write(f"{c['description']}\n\n")

    print(f"Successfully generated 500 candidates in {out_md}")

if __name__ == '__main__':
    main()
