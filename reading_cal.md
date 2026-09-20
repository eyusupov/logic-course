# 🏛️ Master Curriculum: Mathematical Logic, Automated Reasoning, and Type Systems

## 📦 Core Textbooks & System Tickers

- [END] Herbert B. Enderton, A Mathematical Introduction to Logic (2nd Edition)
- [HAR] John Harrison, Handbook of Practical Logic and Automated Reasoning
- [SØR] Morten Heine Sørensen & Paweł Urzyczyn, Lectures on the Curry-Howard Isomorphism
- [LLY] J. W. Lloyd, Foundations of Logic Programming
- [ULL] Jeffrey D. Ullman, Principles of Database & Knowledge-Base Systems (Vols. 1 & 2)

---

## 📅 PHASE 1: Propositional Logic, Truth, and SAT (Weeks 1–4)

Core Objective: Master the absolute abstraction wall between syntax and semantics, unique structural parsing, and the algorithmic blueprint of automated SAT solvers.

## 🔹 Week 1: The Formalization of Syntax

- Required Reading:
  - [END] Chapter 1.0 (Informal Remarks on Formal Languages) & Chapter 1.1 (The Language of Sentential Logic).
  - [HAR] Chapter 1.5 (Syntax and semantics) & Chapter 1.6 (Symbolic computation and OCaml).
- Core Concepts: Inductive generation definitions of formulas; Object-language alphabet variables (пропозициональные буквы) versus meta-variables (метапеременные); Constructing logic grammar in memory using functional variants.
- Historical Blueprint: Structural foundation cleaning of Hermann Grassmann (1861).

## 🔹 Week 2: Grammars, Parsing Engines, and Inductive Rules

- Required Reading:
  - [END] Chapter 1.4 (Induction and Recursion).
  - [HAR] Chapter 1.7 (Parsing).
- Core Concepts: General Chomsky Type 2 (Context-Free) Grammars; Programming an LL(1) Recursive Descent Parser in OCaml; Defining mathematical induction and recursion over abstract string architectures.
- Historical Blueprint: Noam Chomsky's (1956) Context-Free Language Grammars. This week isolates pure parser mechanics—how a computer safely steps through text, processes strings, and manages lookahead boundaries before it applies any logic meanings.

## 🔹 Week 3: Propositional Mathematics, Truth, and Normal Forms

- Required Reading:
  - [END] Chapter 1.2 (Truth Assignments), Chapter 1.3 (A Parsing Algorithm), & Chapter 1.5 (Sentential Connectives).
  - [HAR] Chapter 2.1 to 2.3 (Syntax/Semantics of propositional logic, Validity, satisfiability, tautology) & Chapter 2.5, 2.6 (NNF, DNF, CNF).
- Core Concepts: Truth assignment mappings (истинностное означивание); Functional valuation functions; Tautologies (тождественно истинные формулы); Mathematical proofs of Unique Readability; Hooking your Week 2 parser up to map strings directly into proposition syntax trees; Converting logic arguments into Negation Normal Form (NNF) and Conjunctive Normal Form (CNF).
- Historical Blueprint: Emil Post's (1921) introduction of Truth Tables and Alfred Tarski's truth models. You take the general text parser you built last week and use it to execute actual propositional semantics and algebraic normal form translations.

## 🔹 Week 4: The Core SAT Solver (DPLL) & Compactness

- Required Reading:
  - [END] Chapter 1.7 (Compactness and Effectiveness).
  - [HAR] Chapter 2.9 (The Davis–Putnam procedure) & Chapter 2.12 (Compactness).
- Core Concepts: The DPLL Algorithm loop architecture; Clause manipulation and search-tree branch trimming; The Mathematical Compactness Theorem for propositional variables.
- Historical Blueprint: Davis & Putnam (1960).

## 🔹 Week 5: Quantifiers, Truth, and Models

- Required Reading:
  - [END] Chapter 2.0 (Preliminary Remarks), Chapter 2.1 (First-Order Languages), & Chapter 2.2 (Truth and Models).
  - [HAR] Chapter 3.1 to 3.3 (First-order logic implementation, Parsing, Semantics).
- Core Concepts: Tarski’s formal definition of Satisfaction and structures; Domains of discourse; Valuations of relations, constants, and function functions.
- Historical Blueprint: Richard Dedekind (1888), Giuseppe Peano (1889), and Tarski (1926-1928).

## 🔹 Week 6: Proof Calculi, Soundness, and Completeness

- Required Reading:
  - [END] Chapter 2.4 (A Deductive Calculus) & Chapter 2.5 (Soundness and Completeness Theorems).
- Core Concepts: Structural Proof Theory baselines; Syntactic deduction paths without semantic evaluation; Soundness rules vs. Completeness limits.

## 🔹 Week 7: Skolemization, Relativistic Models, and Herbrand's Theorem

- Required Reading:
  - [END] Chapter 2.6 (Models of Theories).
  - [HAR] Chapter 3.5 (Prenex normal form), Chapter 3.6 (Skolemization), & Chapter 3.8 (Mechanizing Herbrand’s theorem).
- Core Concepts: The Löwenheim-Skolem Theorem and Skolem's Paradox; Non-standard models of arithmetic; Stripping existential variables using Skolem Functions; Flattening First-Order Logic into propositional instances.
- Historical Blueprint: Löwenheim (1915), Thoralf Skolem (1920/1922), and Jacques Herbrand (1930).

## 🔹 Week 8: Unification and Automated Resolution Engines

- Required Reading:
  - [HAR] Chapter 3.9 (Unification) & Chapter 3.11 (Resolution).
- Core Concepts: Robinson’s syntactic Unification Algorithm for matching literals; The First-Order Resolution Principle; Creating mechanical proofs by refutation/contradiction.
- Historical Blueprint: J. A. Robinson (1963/1965).

---

## 📅 PHASE 3: Computability, Type Theory, and Curry-Howard (Weeks 9–12)

Core Objective: Dive directly into the historic limits of mathematical certainty, formalize computation as text translation, and crack the proof-as-program code bridge.

## 🔹 Week 9: Number Systems and Mathematical Foundations

- Required Reading:
  - [END] Chapter 3.0 (Number Theory), Chapter 3.1 (Natural Numbers with Successor), & Chapter 3.3 (A Subtheory of Number Theory).
- Core Concepts: Robinson Arithmetic and Peano Arithmetic structural frameworks; How defining basic number systems exposes structural gaps wide enough to hold entire computational machine rules.

## 🔹 Week 10: Gödel Numbering and Incompleteness

- Required Reading:
  - [END] Chapter 3.4 (Arithmetization of Syntax), Chapter 3.5 (Incompleteness and Undecidability), & Chapter 3.7 (Second Incompleteness Theorem).
  - [HAR] Chapter 7.1 to 7.4 (Hilbert’s programme, Tarski’s undecidability, Incompleteness, Gödel).
- Core Concepts: Turning logic syntax into numerical equations via Gödel Numbering; The Diagonal Lemma (Self-reference step); Proving Gödel's First and Second Incompleteness Theorems; Checking Tarski's Indefinability of Truth.
- Historical Blueprint: Kurt Gödel (1931) and Tarski (1936).

## 🔹 Week 11: The Theory of Computation (Recursive Functions & Lambda Calculus)

- Required Reading:
  - [END] Chapter 3.6 (Recursive Functions).
  - [SØR] Chapters 1 & 2 (Untyped λ-calculus & Substitution).
  - [HAR] Chapter 7.6 (Church’s theorem).
- Core Concepts: Unpacking the Chomsky Hierarchy Type 0 boundaries; Proving the Church-Turing Thesis; Computation modeled as functional substitution via β-reduction; Coding recursion loops with the Y Combinator.
- Historical Blueprint: Alan Turing (1937) and Alonzo Church (1932).

## 🔹 Week 12: Second-Order Structural Bridges (The Curry-Howard Isomorphism)

- Required Reading:
  - [END] Chapter 4.1 (Second-Order Languages) & Chapter 4.2 (Skolem Functions).
  - [SØR] Chapters 3 & 4 (Simply Typed λ-calculus & The Curry-Howard Isomorphism).
- Core Concepts: Intuitionistic Logic rules; Rejecting the law of the excluded middle; Bridging proof systems directly to program structures: Propositions-as-Types and Proofs-as-Programs.

---

## 📅 PHASE 4: SMT Engines, Dependent Types, and Applied Logic Systems (Weeks 13–16)

Core Objective: Map everything you have learned to enterprise computational tools—deconstructing background SMT math theories, dependent-type verifiers, and massive database logicians.

## 🔹 Week 13: Decidable Algebraic Theories (Inside Z3 Solver)

- Required Reading:
  - [HAR] Chapter 4.4 (Congruence closure) & Chapter 5.6 to 5.9 (Quantifier elimination, Presburger arithmetic, Real numbers).
- Core Concepts: Engineering background mathematical theories; Congruence Closure for equality processing; Quantifier Elimination algorithms for parsing arithmetic bounds automatically.
- Historical Blueprint: Rooted in Tarski's (1948) positive geometric decision algorithms.

## 🔹 Week 14: Dependent Type Systems (Inside Lean and Agda)

- Required Reading:
  - [SØR] Chapter 8 (The Barendregt Cube) & Chapter 11 (Dependent Types).
- Core Concepts: Calculus of Inductive Constructions; Engineering type parameters dependent directly on localized values; Creating the architecture of a Trusted Kernel for interactive proof assistants.

## 🔹 Week 15: Restricting Logic for Software & Storage Databases

- Required Reading:
  - [HAR] Chapter 3.14 (Horn clauses and Prolog).
  - [LLY] Chapters 1 & 2 (Syntax and Semantics of Logic Programs).
  - [ULL (Vol. 1)] Chapter 3 (Data Models: Relational Algebra and Relational Calculus).
- Core Concepts: Constraining open First-Order evaluation into strict Horn Clauses; Discovering that Relational Database Queries are structurally identical to First-Order Logic validation formulas.
- Historical Blueprint: Robert Kowalski and Maarten van Emden.

## 🔹 Week 16: The Logic Programming and Datalog Execution Loop

- Required Reading:
  - [LLY] Chapter 3 (SLD-Resolution and Logic Programming).
  - [ULL (Vol. 2)] Chapter 12 (Logic as a Query Language) & Chapter 13 (Efficient Evaluation of Monotone Rules).
- Core Concepts: SLD-Resolution mechanics; Processing Datalog rules at massive enterprise data scales; The Magic Sets compilation transformation; Watching the mathematical loop close: Logic explicitly executing as data storage optimization.
