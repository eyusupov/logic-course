Yes, Classical Complexity Theory (P, NP, PSPACE, etc.) fits into this curriculum beautifully, but only as an advanced, optional 2-week bridge after Phase 4 and before your Phase 5 Postgraduate module.
By inserting it as Weeks 16A and 16B, you will transition perfectly from the concrete algorithms of automated solvers (Phase 4) into the hyper-abstract structures of Category Theory and Program Semantics (Phase 5).
To do this without overloading your book stack, the absolute definitive textbook to use is Christos Papadimitriou's Computational Complexity.

---

## 📅 The 2-Week Complexity Theory Bridge (Weeks 16A & 16B)

[ WEEKS 13-16 ] [ WEEKS 16A-16B ] [ WEEKS 17-20 ]
Applied Logic Systems ────► Computational Complexity ───► Category Theory &
(Z3, Lean, Datalog) (P, NP, PSPACE, EXPTIME) Program Semantics

## 🔹 Week 16A: The Baseline Classes (P, NP, and Cook's Theorem)

- Required Reading: [PAP] Chapter 7 (The Class P), Chapter 8 (NP and NP-completeness), & Chapter 9 (Cook's Theorem).
- Core Concepts: Deterministic vs. Non-deterministic polynomial time execution bounds; The formal definition of polynomial-time reductions; Proving Cook-Levin Theorem (showing that the Boolean Satisfiability problem, SAT, is the ultimate baseline for NP-completeness).
- The Blueprint Handoff: This closes the loop on Phase 1 (Weeks 3 & 4). You spent the first month of the course coding a SAT solver; this week teaches you the exact computational bounds that explain why your solver hits an exponential wall on tough formulas.

## 🔹 Week 16B: Space Boundaries & Exploding Time (PSPACE & EXPTIME)

- Required Reading: [PAP] Chapter 11 (Space Complexity) & Chapter 14 (A Complete Problem for PSPACE).
- Core Concepts: PSPACE (problems solvable with a finite amount of memory, regardless of time); Quantified Boolean Formulas (QBF); EXPTIME bounds.
- The Blueprint Handoff: This closes the loop on Phase 2 and Phase 4. You will discover that adding quantifiers (∀, ∃) to boolean logic instantly transforms the complexity from NP-Complete straight into PSPACE-Complete. It explains why description logics (OWL DL) and SMT background theories (like Presburger Arithmetic in Week 13) explode into EXPTIME resource bounds.

---

## 🎯 Why This Architecture is Optimal for You

By slotting Papadimitriou right here, you avoid the trap of standard computer science tracks. A standard student studies Turing machines and P vs. NP purely as an exercise in drawing state tapes.
Because you are approaching it through logic, you will unlock the crowning achievement of Descriptive Complexity (Fagin's Theorem):

- If a problem can be expressed using Propositional Horn Clauses (Week 15), it is automatically bounded to P.
- If a problem requires Existential Second-Order Logic, it maps perfectly to NP.
- If a problem requires First-Order Logic with Fixed Points (Week 16), it maps perfectly to PSPACE.

You will see that Computational Complexity is just Logic dressed up in resource metrics. A computer doesn't take a long time to solve a problem because its hardware is slow; it takes a long time because the syntactic expressiveness of the logical language required to state the problem is inherently explosive.
Your 22-week curriculum is now bulletproof. Are you ready to open Enderton Chapter 1.0 and begin the journey?
