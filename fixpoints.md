Yes, fixed-points (fixpoints) are covered extensively in the final weeks of your curriculum, specifically during Phase 3 and Phase 4 (Weeks 11, 12, 15, and 16).
Because your course explicitly bridges mathematical philosophy with computer science, you will study fixpoints from two completely different, brilliant angles: syntactic/computational fixpoints (how to create loops in code) and semantic/lattice fixpoints (how to calculate the absolute meaning of a database query or a logic program).
Here is exactly where and how they appear in your 16-week schedule:

---

## 1. Functional Fixpoints: The Y Combinator (Weeks 11 & 12)

- The Textbooks: [SØR] Chapters 1 & 2 (Untyped λ-calculus) and [HAR] Chapter 7.6 (Church's Theorem).
- The Concept: In pure, untyped Lambda Calculus, functions do not have names, which means a function cannot call itself directly to create a loop (like recursion). Alonzo Church solved this by inventing the Fixpoint Combinator (most famously the Y Combinator: $Y = \lambda f. (\lambda x. f (x x)) (\lambda x. f (x x))$).
- What you learn: You will prove that for any lambda expression F, the term Y F calculates a structural fixpoint such that $Y F \equiv F(Y F)$. This is how you mathematically define loops, factorials, and infinite recursion out of nothing but basic functions.

## 2. Semantic Fixpoints: Tarski’s Fixed-Point Theorem (Weeks 15 & 16)

- The Textbooks: [LLY] Chapter 2 & 3 (Semantics of Logic Programs) and [ULL (Vol. 2)] Chapter 13 (Efficient Evaluation of Monotone Rules).
- The Concept: When a computer executes a Prolog program or evaluates a recursive Datalog database query (e.g., "Find all ancestors of John" or "Find all routing paths between Amsterdam and Tokyo"), it cannot use a simple loop. It relies on Alfred Tarski’s legendary lattice-theory breakthrough: The Knaster-Tarski Fixed-Point Theorem.
- What you learn:
- The Immediate Consequence Operator ($T_P$): Lloyd teaches you how a logic program acts as a mathematical operator ($T_P$) that takes a set of facts and spits out new facts deduced from your code rules.
  - Least Fixed-Point (LFP): You will learn how the database engine evaluates your query by starting with the empty set (∅), applying the $T_P$ operator repeatedly ($T_P(\emptyset)$, $T_P(T_P(\emptyset))$, ...), and climbing up a mathematical lattice until the set stops growing. That exact mathematical resting point is the Least Fixed-Point, which represents the mathematically complete and correct answer to your code's query.

---

## The Synthesis of Fixpoints in Your Syllabus

                              [ THE FIXPOINT SEESAW ]
                                         │
         ┌───────────────────────────────┴───────────────────────────────┐
         ▼                                                               ▼

[ SYNTACTIC / CODE FIXPOINT ] [ SEMANTIC / DATA FIXPOINT ]
Weeks 11-12 ([SØR]) Weeks 15-16 ([LLY] & [ULL])
The Y Combinator Least Fixed-Point (LFP)
"How do we write code that "How do we calculate the complete
loops infinitely?" meaning of recursive data rules?"

By tracking fixpoints through Sørensen, Lloyd, and Ullman, you will see one of the most stunning unifications in computer science: the exact same abstract algebraic property that allows a functional programming language to run a loop is what allows an enterprise database engine to calculate deep, recursive relationships across millions of data rows with absolute mathematical certainty.
Would you like to preview how the Y Combinator works using a simple computational trace, or should we look at the exact OCaml commands needed to set up your workspace environment for Week 1?
