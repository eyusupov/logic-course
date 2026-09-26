# 🏛️ Master Curriculum: Mathematical Logic, Automated Reasoning, and Type Systems

## 📦 Core Textbooks & System Tickers

- [END] Herbert B. Enderton, A Mathematical Introduction to Logic (2nd Edition)
- [HAR] John Harrison, Handbook of Practical Logic and Automated Reasoning
- [SØR] Morten Heine Sørensen & Paweł Urzyczyn, Lectures on the Curry-Howard Isomorphism
- [LLY] J. W. Lloyd, Foundations of Logic Programming
- [ULL] Jeffrey D. Ullman, Principles of Database & Knowledge-Base Systems (Vols. 1 & 2)
- [TAPL] Benjamin C. Pierce, Types and Programming Languages
- [ATTAPL] Benjamin C. Pierce, Advanced Topics in Types and Programming Languages

---

## 📅 PHASE 1: Propositional Logic, Truth, and SAT (Weeks 1–4)

Core Objective: Master the absolute abstraction wall between syntax and semantics, unique structural parsing, and the algorithmic blueprint of automated SAT solvers.

## 🔹 Week 1: The Formalization of Syntax

- Required Reading:
  - [END] Chapter 1.0 (Informal Remarks on Formal Languages) & Chapter 1.1 (The Language of Sentential Logic).
  - [HAR] Chapter 1.5 (Syntax and semantics) & Chapter 1.6 (Symbolic computation and OCaml).
- Core Concepts: Inductive generation definitions of formulas; Object-language alphabet variables (пропозициональные буквы) versus meta-variables (метапеременные); Constructing logic grammar in memory using functional variants.
- Historical Blueprint: Structural foundation cleaning of Hermann Grassmann (1861).

## 🔹 Week 2: Semantics and Truth Foundations

- Required Reading:
  - [END] Chapter 1.2 (Truth Assignments) & Chapter 1.4 (Induction and Recursion).
  - [HAR] Chapter 2.1 to 2.3 (Syntax/Semantics of propositional logic, Validity, satisfiability, tautology).
- Core Concepts: Truth assignment functions (истинностное означивание); The Principle of Structural Induction; Proving meta-theorems about valuations recursively; Mathematical definitions of validity, satisfiability, and tautology (тождественно истинные формулы).
- Historical Blueprint: Early algebraic foundations of Boolean functions and the semantic truth models of Alfred Tarski.

## 🔹 Week 3: Parsing Engines and Normal Forms

- Required Reading:
  - [END] Chapter 1.3 (A Parsing Algorithm) & Chapter 1.5 (Sentential Connectives).
  - [HAR] Chapter 1.7 (Parsing) & Chapter 2.5, 2.6 (NNF, DNF, CNF).
- Core Concepts: Deterministic tree-structure construction; Mathematical proofs of Unique Readability; Designing an LL(1) recursive descent parser in code; Converting parsed abstract syntax trees into Negation Normal Form (NNF) and Conjunctive Normal Form (CNF).
- Historical Blueprint: The formalization of Context-Free Grammars (Chomsky Type 2) and their reduction to algorithmic compiler tokenizers.

## 🔹 Week 4: The Core SAT Solver (DPLL) & Compactness

- Required Reading:
  - [END] Chapter 1.7 (Compactness and Effectiveness).
  - [HAR] Chapter 2.9 (The Davis–Putnam procedure), Section 2.10 (Stålmarck’s method), Section 2.11 (Binary decision diagrams), Chapter 2.12 (Compactness).
- Core Concepts: The DPLL Algorithm loop architecture; Clause manipulation and search-tree branch trimming; The Mathematical Compactness Theorem for propositional variables.
- Historical Blueprint: Davis & Putnam (1960).

---

## 📅 PHASE 2: First-Order Logic, Model Theory, and Resolution (Weeks 5–8)

Core Objective: Expand your logic language to capture variables and infinity quantifiers, evaluate structural truth universes, and engineer general automated theorem proving.

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
  - [HAR] Chapter 3.9 (Unification), Chapter 3.11 (Resolution), Chapter 3.13: Refinements of Resolution
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

## 🔹 Week 11: The Theory of Computation (The Untyped Engine)

- Required Reading:
  - [END] Chapter 3.6 (Recursive Functions).
  - [SØR] Chapters 1 & 2 (Untyped λ-calculus & Substitution).
  - [HAR] Chapter 7.6 (Church’s theorem).
  - [TAPL] Chapters 5, 6, & 7 (Untyped Lambda-Calculus, An OCaml Type-free Implementation).
- Core Concepts: Proving the Church-Turing Thesis; Functional computation via β-reduction; Managing variable scopes using De Bruijn indices; Writing a raw, untyped term evaluator in OCaml.

## 🔹 Week 12: The Propositional Isomorphism (STLC)

- Required Reading:
  - [SØR] Chapters 3 & 4 (Simply Typed λ-calculus & The Curry-Howard Isomorphism).
  - [TAPL] Chapters 8, 9, & 11 (Type Systems, Simply Typed Lambda-Calculus, Simple Extensions).
- Core Concepts: Intuitionistic Propositional Logic vs. Classical Logic; Proving Type Safety via Progress (a well-typed term never gets stuck) and Preservation (evaluation preserves types); Unifying logical deduction steps with language type-checking.

## 🔹 Week 13: Higher-Order Systems & Substructural Resource Logic

- Required Reading:
  - [SØR] Chapter 5 (The Polymorphic λ-calculus / System F).
  - [END] Chapter 4.1 & 4.2 (Second-Order Languages).
  - [ATTAPL] Chapter 1 (Substructural Type Systems).
- Core Concepts: Quantifying over type variables (∀ T) in System F vs. quantifying over properties (∀ P) in classical model universes; Parametric polymorphism; Linear and Affine Logic (rejecting structural rules of Weakening and Contraction to force resources to be used exactly once).

---

## 📅 PHASE 4: SMT Engines, Dependent Types, and Applied Data Logics (Weeks 14–16)

## 🔹 Week 14: Decidable Algebraic Theories & Type Inference (Inside Z3 Solver)

- Required Reading:
  - [HAR] Chapter 4.4 (Congruence closure) & Chapter 5.6 to 5.9 (Quantifier elimination, Presburger arithmetic).
  - [TAPL] Chapter 22 (Type Reconstruction).
  - [ATTAPL] Chapter 10 (The Essence of ML Type Inference).
- Core Concepts: Background mathematical decision theories; Constraint-based Hindley-Milner type inference; Realizing that compiler type reconstruction is a modified variation of logical unification.

## 🔹 Week 15: Dependent Type Systems & Proof-Carrying Code (Inside Lean and Agda)

- Required Reading:
  - [SØR] Chapter 8 (The Barendregt Cube) & Chapter 11 (Dependent Types).
  - [ATTAPL] Chapter 4 (Proof-Carrying Code).
- Core Concepts: Calculus of Inductive Constructions; Engineering type parameters dependent directly on localized values; Creating the architecture of a Trusted Kernel; Validating mobile, untrusted executable binaries using attached mathematical proof terms.

## 🔹 Week 16: The Database Crunch (Horn Clauses, Logic Programming, and Datalog)

- Required Reading:
  - [HAR] Chapter 3.14 (Horn clauses and Prolog).
  - [LLY] Chapters 1, 2, & 3 (Syntax, Semantics, and SLD-Resolution of Logic Programs).
  - [ULL] Vol. 1 Ch. 3 (Relational Calculus) & Vol. 2 Ch. 12 & 13 (Datalog Evaluation & Monotone Rules).
- Core Concepts: Constraining First-Order Logic into linear Horn structures; Backward-chaining SLD-Resolution vs. Forward-chaining Datalog evaluation; Evaluating recursive queries using the Knaster-Tarski Least Fixed-Point (LFP) theorem on data lattices.
