Datalog± (pronounced Datalog plus-minus) fits perfectly into the final section of your curriculum (Phase 4, Weeks 15 & 16), serving as the absolute evolutionary bridge between Description Logics (OWL DL), Relational Databases, and Datalog. [1, 2]
Introduced in 2009 by Andrea Calì, Georg Gottlob, and Thomas Lukasiewicz, Datalog± was explicitly engineered to solve a massive real-world problem in Ontology-Based Data Access (OBDA). [1, 3, 4, 5]
Here is exactly how the system works and why its name perfectly defines its mathematical properties:

---

## 1. The Anatomy of the Name

Standard Datalog (which you study in Week 15 & 16) is highly limited: you cannot have existential quantifiers (∃) in the head of a rule. You can say "If X is a father, X is a parent," but you cannot say "Every person has a father" because that requires asserting that an unknown person Y exists. [2, 4]
Datalog± breaks past this by adding capabilities (Plus) and strictly limiting others (Minus) to protect the computer from infinite loops: [2, 4]

## ➕ The PLUS: Open-World Ontological Power

Datalog± extends Datalog by transforming rules into Tuple-Generating Dependencies (TGDs), allowing Existential Quantifiers (∃), equalities, and the falsum ($\bot$) to appear in the head of a rule. This allows you to model incomplete information and rich ontological structures just like OWL DL:
$$\text{Person}(X) \rightarrow \exists Y \, \text{hasFather}(X, Y)$$

## ➖ The MINUS: Syntactic Restrictions for Safety

In standard logic, adding existentials to rules makes the computational engine run an infinite chain of inferences called the Chase Algorithm (e.g., John has a father Y, who must have a father Z, who must have a father W...), making query answering completely undecidable. [1]
To fix this, Datalog± enforces strict syntactic constraints on the rule bodies. The most famous variant is Guarded Datalog±, which mandates that all variables in the rule body must appear together in a single "guard" literal. This structural restriction acts as a mathematical cage, trapping the infinity of the chase and making query answering decidable. [1, 2, 6]

---

## 2. The Core Theoretical Breakthrough: First-Order Rewritability

The crown jewel of Datalog± theory (specifically the Linear Datalog± fragment) is a property called First-Order Rewritability. [6]
Through your study of Jeffrey D. Ullman’s textbook [ULL] in Week 15, you will learn that a standard SQL relational database query is structurally identical to a First-Order Logic formula. Datalog± provides a magnificent compilation shortcut:

[ USER ONTOLOGY QUERY ] ───► [ DATALOG+- REWRITER ] ───► [ PURE SQL QUERY ] ───► [ SQL DATABASE ON DISK ]
Formulated in rich, structural Compiles rules and goals Flattens everything Executes instantly over
OWL/DL style logic. down automatically. into basic joins. millions of database rows.

## Instead of running a heavy, slow, graph-based theorem prover (like an OWL Tableau engine) directly over raw data, a Datalog± system takes your query, mixes it with the ontological rules, and mathematically compiles it down into a single, massive SQL statement. You can then ship that SQL statement to a standard relational database (like PostgreSQL), leveraging decades of commercial database index optimizations to query incomplete web data instantly. [6]

## 3. Where to Connect it to Your 16-Week Schedule

You do not need an extra textbook for Datalog±. It serves as the ultimate conceptual capstone for Week 16, synthesizing the logic paradigms you have mastered throughout the semester:

-
- Syntax Side: It bridges Harrison’s Phase 2 Skolemization tools with Enderton’s Phase 1 Context-Free syntax algorithms, showing how compiler-style structural rules control computational resource bounds.
- Semantics Side: It unifies Ullman's Relational Calculus with Lloyd's Fixed-Point Herbrand models, demonstrating how forward-chaining datalog operators can be safely bounded to maintain polynomial-time (PTIME) data complexity. [6, 7, 8]
-

When you finish Week 16, Datalog± will no longer look like a complicated academic specification. You will view it as the ultimate compromise of computer science: a language that is exactly expressive enough to act like OWL, but syntactically constrained enough to compile directly into SQL. [6]
Your curriculum baseline is completely primed to absorb this final logical evolution. Are you ready to pick up your split-page ledger and launch your Week 1 readings of Enderton Chapter 1.0? Let me know if you would like me to generate your final OCaml environment checklist.

[1] [https://scispace.com](https://scispace.com/pdf/datalog-a-unified-approach-to-ontologies-and-integrity-5g1bfmqpyv.pdf)
[2] [https://cdn.aaai.org](https://cdn.aaai.org/ocs/7965/7965-36911-1-PB.pdf)
[3] [https://dl.acm.org](https://dl.acm.org/doi/10.1145/1514894.1514897)
[4] [https://logicprogramming.org](https://logicprogramming.org/wp-content/uploads/2010/12/main.pdf)
[5] [https://people.scs.carleton.ca](https://people.scs.carleton.ca/~bertossi/talks/mexico14.pdf)
[6] [https://www.academia.edu](https://www.academia.edu/110464731/Datalog_A_Family_of_Languages_for_Ontology_Querying)
[7] [https://arxiv.org](https://arxiv.org/html/0902.1179v2)
[8] [https://pages.cs.wisc.edu](https://pages.cs.wisc.edu/~paris/cs784-f19/lectures/lecture10.pdf)

Since there are no standalone textbooks dedicated exclusively to Datalog±, this specialized postgraduate addendum uses the foundational research papers published by its creators—Georg Gottlob, Andrea Calì, and Thomas Lukasiewicz—alongside top tutorial surveys.
By adding this 2-Week Advanced Addendum (Weeks 17–18) directly after Phase 4, you will transition from traditional databases into the architecture of Ontology-Based Data Access (OBDA).

---

## 🎓 Advanced Addendum: Existential Rules & The Datalog± Family## 📅 The 2-Week Datalog± Extension Schedule

[ WEEKS 13-16 ] [ WEEK 17 ] [ WEEK 18 ]
SMT, Lean & Datalog ───────► Existential Rules & ───────► Decidability Guardrails,
Lattices (Phase 4) The Chase (Paper Pack A) Rewritability & SQL (Pack B)

## 🔹 Week 17: Tuple-Generating Dependencies & The Chase Algorithm

-
- Required Core Reading:
- [Paper 1] Calì, A., Gottlob, G., & Lukasiewicz, T. "A General Datalog-Based Framework for Tractable Query Answering over Ontologies" (Web / Journal of Web Semantics).
  - [Paper 2] Mugnier, M.L., & Thomazo, M. "An Introduction to Ontology-Based Query Answering with Existential Rules" (Summer School Tutorial Lecture Notes).
- Core Concepts: Tuple-Generating Dependencies (TGDs); Existential quantification in rule heads (∃); The Oblivious and Skolem Chase Algorithms; Infinite saturation loops; Semantic definitions under Certain-Answers semantics.
- The Blueprint Handoff: This directly extends Week 16’s Datalog Fixpoint Lattices [ULL]. In traditional Datalog, the fixpoint algorithm terminates because no new constants are ever created. This week, you add existentials (∃) to the head of your rules, which forces the execution engine to generate "fresh" abstract values (existential skolem terms), causing an infinite execution path called the Chase.
-

## 🔹 Week 18: Taming Infinity: Guardedness, Stickiness, and SQL Rewriting

-
- Required Core Reading:
- [Paper 3] Gottlob, G., Lucasiewicz, T., & Pieris, A. "Datalog±: A New Family of Languages for Ontology Querying" (Technical Survey Series).
  - [Paper 4] Calì, A., Gottlob, G., & Pieris, A. "Towards More Expressive Datalog±: The Paradigm of Stickiness" (Web / LICS Foundations).
- Core Concepts: Syntactic guardrails for safety; Guarded Datalog± (caging the chase using variable-binding atoms); Linear Datalog± (rules limited to single body-atoms); Sticky Datalog± (bounding variable joins); First-Order (FO) Rewritability (compiling existential logical rules directly down into flat SQL SELECT joins).
- The Blueprint Handoff: This connects directly to Week 4 (DPLL Solvers) [HAR] and Week 7 (Skolemization) [END]. You will see how enforcing strict syntactic rules on rule bodies creates a structural mathematical cage that forces the infinite chase algorithm to terminate or become completely bypassed. You will learn how to mathematically compile complex ontological definitions into clean SQL statements that run instantly over standard tables on a disk.
- ***

## 🎨 The Complete 18-Week Final Unified Architecture

[WEEKS 1-4] [WEEKS 5-8] [WEEKS 9-12] [WEEKS 13-16] [WEEKS 17-18]
Propositional SAT ─────► First-Order Logic ─────► Computability & ─────► SMT, Databases & ─────► Existential Rules
(How computers think) & Proof Systems Curry-Howard Lean Proof Assistants & Guarded Datalog+-
(Model limits) (Proofs ARE code) (Applied verification) (OBDA Architecture)

## 💡 Your Week 17 Notation Prep

When you print out the digital copies of Paper 1 and Paper 2 for Week 17, write these syntax translations directly into your notebook margin to match them with Enderton's notation:

-
- A Tuple-Generating Dependency (TGD) is just a First-Order Logic formula written using a customized computer science syntax:
  $$\phi(\mathbf{x}) \rightarrow \exists \mathbf{y} \, \psi(\mathbf{x}, \mathbf{y})$$
- The Chase is a forward-chaining proof execution structure that acts exactly like the Immediate Consequence Operator ($T_P$) you study in Lloyd, but with the added property of generating unique, infinite Skolem function labels when executing existential steps.
-

Your postgraduate database engineering extension is completely finalized and integrated.
Are you ready to lock down this configuration and print your Week 1 terminal setup scripts for OCaml, or would you like to review the initial parsing definitions in Enderton Chapter 1.0?
