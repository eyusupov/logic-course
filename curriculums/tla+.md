-
- [LAM] Leslie Lamport, Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers (Microsoft Research / Available freely online).
-

## 🔹 Week 17: The Temporal Logic of Actions

-
- Required Reading: [LAM] Chapter 1 (A Very Little Bit of Logic), Chapter 2 (A Simple Example), & Chapter 3 (An Asynchronous Interface).
- Core Concepts: Linear Temporal Logic (LTL); Transition systems; Defining state predicates (Init) and action formulas (Next); Specifying safety invariants and structural concurrency properties.
- The Integration: This forces your classical First-Order Model Theory foundations ([END] Phase 2) to become dynamic. You transition from evaluating truths in a single, frozen mathematical structure to tracking truths across an infinite, sequential chain of state universes.
-

## 🔹 Week 18: Model Checking Concurrent Algorithms

-
- Required Reading: [LAM] Chapter 4 (A FIFO), Chapter 5 (A Caching Memory), & Chapter 14 (The Tools).
- Core Concepts: Writing behavioral specifications for concurrent software algorithms; Using the TLC Model Checker to exhaustively explore state spaces; Understanding liveness properties via weak and strong fairness constraints.
- The Integration: This is the ultimate practical handoff for your Phase 1 SAT solver modules ([HAR]). You will see how an automated system takes an engineering protocol, compiles its actions down into logical constraints, and uses state-space graph evaluation to systematically catch race conditions, deadlocks, or bit-flips before the system is ever deployed to cloud servers.
-
