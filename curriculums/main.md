# Master Curriculum: Mathematical Logic, Automated Reasoning, and Type Systems## Core Textbooks & System Tickers

- [LAMR] Jeremy Avigad, Marijn Heule, & Wojciech Nawrocki, Logic and Mechanized Reasoning
- [HAR] John Harrison, Handbook of Practical Logic and Automated Reasoning
- [SØR] Morten Heine Sørensen & Paweł Urzyczyn, Lectures on the Curry-Howard Isomorphism
- [LLY] J. W. Lloyd, Foundations of Logic Programming
- [ULL] Jeffrey D. Ullman, Principles of Database & Knowledge-Base Systems (Vols. 1 & 2)
- [TAPL] Benjamin C. Pierce, Types and Programming Languages
- [ATTAPL] Benjamin C. Pierce (Ed.), Advanced Topics in Types and Programming Languages

---

## PHASE 1: Propositional Logic, Functional Environments, and SAT (Weeks 1–4)## Week 1: Foundations, Mathematical Induction, and OCaml Core

- Required Reading:
  - [LAMR] Chapter 1 (Introduction) & Chapter 2 (Mathematical Background: Sections 2.1–2.4).
  - [HAR] Chapter 1.5 (Syntax and semantics) & Chapter 1.6 (Symbolic computation and OCaml).
- Core Concepts: Induction and recursion on natural numbers; Complete induction; Generalized structural induction; Program invariants; Object-language variables versus meta-variables.

## Week 2: Lean as a Programming Language & Parsing Engines

- Required Reading:
  - [LAMR] Chapter 3 (Lean as a Programming Language: Sections 3.1–3.4).
  - [HAR] Chapter 1.7 (Parsing).
- Core Concepts: Using Lean 4 as a functional programming language; Declaring inductive data types; Using Lean 4 as an imperative programming language (monads, state mutable tracking); Writing an LL(1) Recursive Descent Parser in OCaml.

## Week 3: Propositional Logic Syntax, Semantics, and Implementation

- Required Reading:
  - [LAMR] Chapter 4 (Propositional Logic) & Chapter 5 (Implementing Propositional Logic).
  - [HAR] Chapter 2.1 to 2.3 & Chapter 2.5, 2.6 (NNF, DNF, CNF).
- Core Concepts: Propositional syntax and semantics; Calculating with propositions; Complete sets of connectives; Implementing propositional syntax/semantics trees in code; Automating Negation Normal Form (NNF), Disjunctive Normal Form (DNF), and Conjunctive Normal Form (CNF) data structures.

## Week 4: SAT Solvers, CDCL Mechanics, and Binary Decision Diagrams

- Required Reading:
  - [LAMR] Chapter 6 (Decision Procedures for Propositional Logic) & Chapter 7 (Using SAT Solvers).
  - [HAR] Chapter 2.9 (The Davis–Putnam procedure), Section 2.10 (Stålmarck's Method), & Section 2.11 (Binary Decision Diagrams).
- Core Concepts: The Tseitin Transformation; Unit propagation and the pure literal rule; The DPLL backtracking algorithm; Autarkies and 2-SAT; Conflict-Driven Clause Learning (CDCL) basics; Encoding problems (Grid coloring, NumberMind); Reduced Ordered Binary Decision Diagrams (ROBDDs).

---

## PHASE 2: Proof Systems, First-Order Logic, and Equality Procedures (Weeks 5–8)

## Week 5: Propositional Proof Systems & Interactive Proof Assistance

- Required Reading:
  - [LAMR] Chapter 8 (Proof Systems for Propositional Logic) & Chapter 9 (Using Lean as a Proof Assistant).
- Core Concepts: Axiomatic systems; Propositional Resolution; Implementing resolution engines; Resolution vs. DPLL; Sequent calculus; Natural deduction; Propositional Compactness; Writing structured proofs and proof terms natively inside Lean 4.

## Week 6: First-Order Logic Syntax and Semantics

- Required Reading:
  - [LAMR] Chapter 10 (First-Order Logic: Sections 10.1–10.4).
  - [HAR] Chapter 3.1 to 3.3 (First-order logic syntax, semantics, and models).
- Core Concepts: First-order language syntax; Quantified variables, predicates, and functions; Tarski's formal definition of satisfaction structures; First-order normal forms.

## Week 7: Implementing First-Order Logic, Herbrand's Theorem, and Unification

- Required Reading:
  - [LAMR] Chapter 11 (Implementing First-Order Logic: Sections 11.1–11.4).
  - [HAR] Chapter 3.5 (Prenex normal form), 3.6 (Skolemization), & 3.8 (Herbrand's theorem).
- Core Concepts: Representing and evaluating terms and formulas in code; Robinson’s Syntactic Unification Algorithm; Prenex normal form transformations; Outer Skolemization; Reducing First-Order Logic to infinite propositional instances via Herbrand Terms.

## Week 8: Decision Procedures for Equality

- Required Reading:
  - [LAMR] Chapter 12 (Decision Procedures for Equality: Sections 12.1–12.3).
  - [HAR] Chapter 4.4 (Congruence closure).
- Core Concepts: The logical properties of Equality; Implementing the Congruence Closure Algorithm via E-graphs/union-find data structures; Deciding universal sentences with equality.

---

## PHASE 3: Interactive Verification, Computability, and Type Theory (Weeks 9–13)## Week 9: Equality, Induction in Lean, and Metatheorem Foundations

- Required Reading:
  - [LAMR] Chapter 13 (Equality and Induction in Lean: Sections 13.1–13.2).
  - [HAR] Chapter 7.1 (Context of Gödel's proof), 7.2 (Gödel numbering), 7.3 (Incompleteness), & 7.4 (Further meta-theorems).
- Core Concepts: Equational reasoning tactics in Lean 4; Writing structural induction proofs inside a proof assistant; Arithmetization of syntax (Gödel numbering); The Diagonal Self-Reference Lemma; Gödel's First and Second Incompleteness Theorems.

## Week 10: Decision Procedures for Arithmetic & Undecidability Limits

- Required Reading:
  - [LAMR] Chapter 14 (Decision Procedures for Arithmetic: Sections 14.1–14.5).
  - [HAR] Chapter 7.5 (Solvability and undecidability) & Chapter 7.6 (Church’s theorem).
- Core Concepts: Linear Real Arithmetic (LRA); Implementing the Fourier-Motzkin Elimination Algorithm; Linear Integer Arithmetic (LIA / Presburger arithmetic); Other decidable algebraic theories vs. the Undecidability of the Halting Problem and Church's Theorem.

## Week 11: Satisfiability Modulo Theories (SMT) & The Untyped Engine

- Required Reading:
  - [LAMR] Chapter 15 (Using SMT Solvers: Sections 15.1–15.5).
  - [SØR] Chapter 1 (Untyped lambda-calculus) & Chapter 2 (Substitution).
  - [TAPL] Chapters 5, 6, & 7 (Untyped Lambda-Calculus, An OCaml Type-free Implementation).
- Core Concepts: SMT-LIB Format standard; Encoding constraints (Magic squares, almost squares); Calling SMT solvers directly from Lean 4; Software verification applications; Functional calculation foundations via β-reduction; Managing variable scopes using De Bruijn Indices.

## Week 12: Simply Typed Lambda Calculus (STLC) & The Curry-Howard Isomorphism

- Required Reading:
  - [SØR] Chapter 3 (Simply typed lambda-calculus) & Chapter 4 (The Curry-Howard Isomorphism).
  - [TAPL] Chapters 8, 9, & 11 (Type Systems, Simply Typed Lambda-Calculus, Simple Extensions).
- Core Concepts: Intuitionistic Propositional Logic; The Brouwer-Heyting-Kolmogorov (BHK) interpretation; Proving Type Safety via Progress and Preservation invariants; Mapping Propositions-as-Types and Proofs-as-Programs.

## Week 13: Higher-Order Systems & Substructural Resource Tracking

- Required Reading:
  - [SØR] Chapter 5 (The Polymorphic lambda-calculus / System F).
  - [ATTAPL] Chapter 1 (Substructural Type Systems).
- Core Concepts: Quantifying over type variables (∀ T) inside System F; Parametric polymorphism; Linear Logic and Affine Logic constraints (forbidding the structural rules of Weakening and Contraction to enforce exact, single-use pointer and memory lifecycle tracking).

---

## PHASE 4: Advanced Type Inference, Verification Kernels, and Enterprise Data Engines (Weeks 14–16)## Week 14: Automated Type Reconstruction & ML Inference Engines

- Required Reading:
  - [TAPL] Chapter 22 (Type Reconstruction).
  - [ATTAPL] Chapter 10 (The Essence of ML Type Inference).
- Core Concepts: Constraint-based type reconstruction; Generating type variable constraints; Hindley-Milner type inference extensions; Unifying type equations via automated substitution sweeps.

## Week 15: Dependent Types & Proof-Carrying Software Architecture

- Required Reading:
  - [SØR] Chapter 8 (The Barendregt Cube) & Chapter 11 (Dependent Types).
  - [ATTAPL] Chapter 4 (Proof-Carrying Code).
- Core Concepts: The Lambda Cube classification boundaries; Dependent Type Theory (Π-types where types depend on runtime execution values); Calculus of Inductive Constructions; Building a Trusted Kernel compilation environment; Embedding structural mathematical proof terms into untrusted executable bytecode binaries.

## Week 16: Horn Clauses, Logic Programming, and Recursive Datalog Engines

- Required Reading:
  - [HAR] Chapter 3.14 (Horn clauses and Prolog).
  - [LLY] Chapters 1, 2, & 3 (Syntax, Semantics, and SLD-Resolution of Logic Programs).
  - [ULL] Vol. 1 Ch. 3 (Relational Calculus) & Vol. 2 Ch. 12 & 13 (Datalog Evaluation & Monotone Rules).
- Core Concepts: Constraining First-Order Logic into deterministic linear Horn structures; Backward-chaining SLD-Resolution execution structures vs. Forward-chaining monotone data cascades; Compiling recursive database query matrices by calculating the unique Least Fixed-Point (LFP) via the Knaster-Tarski Theorem on bounded data lattices.

---

## The Streamlined 16-Week Grid View

[WEEK 11] [WEEK 12] [WEEK 13] [WEEK 14] [WEEK 15] [WEEK 16]
SMT & Untyped λ Simply Typed STLC System F & LinLogic Type Inference ADTs Dependent Type CoC Prolog & Datalog
(LAMR 15 / TAPL 5-7) (TAPL 8-11) (ATTAPL 1) (TAPL 22) (SØR 8, 11) (LLY 1-3 / ULL 12-13)
[Vid: Lambda Calc] [Vid: OPLSS STλC] [Vid: System F] [Vid: Unification] [Vid: Lambda Cube] [Vid: Data Resolution]
