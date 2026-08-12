# AXON Predicate Language (AP-L) Specification (docs/PREDICATE_LANGUAGE.md)

## 1. Design & Non-Turing-Complete Grammar

AXON Predicate Language (AP-L) is a non-Turing-complete, side-effect-free, deterministic expression language designed for zero-dependency constraint evaluation.

### Formal Grammar (EBNF):
```ebnf
Expression  ::= LogicalOr ;
LogicalOr   ::= LogicalAnd ( "||" LogicalAnd )* ;
LogicalAnd  ::= Equality ( "&&" Equality )* ;
Equality    ::= Relational ( ( "==" | "!=" ) Relational )* ;
Relational  ::= Additive ( ( "<" | "<=" | ">" | ">=" ) Additive )* ;
Additive    ::= Multiplicative ( ( "+" | "-" ) Multiplicative )* ;
Multiplicative ::= Primary ( ( "*" | "/" | "%" ) Primary )* ;
Primary     ::= Identifier | Literal | "(" Expression ")" | FunctionCall ;
FunctionCall::= Identifier "(" [ Expression ( "," Expression )* ] ")" ;
Literal     ::= Number | String | Boolean | Null ;
```

---

## 2. Hard VM Resource Bounds

To prevent Denial-of-Service (DoS) and infinite loop attacks, every AP-VM instance enforces strict physical execution limits:

| Resource Metric | Maximum Allowed Limit | Enforcement Action |
| :--- | :---: | :--- |
| **Max VM Instructions** | **1,000 opcode steps** | Terminate execution $\to$ Return `UNVERIFIED` |
| **Max Stack Depth** | **64 frames** | Terminate execution $\to$ Return `UNVERIFIED` |
| **Max Heap Allocation** | **1,024 KB** | Terminate execution $\to$ Return `UNVERIFIED` |
| **Max String Length** | **65,536 chars** | Truncate string evaluation |
| **Max Execution Time** | **10.0 ms** | Terminate execution $\to$ Return `UNVERIFIED` |
