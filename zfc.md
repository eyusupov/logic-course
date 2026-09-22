Yes, Zermelo–Fraenkel set theory (ZFC) is covered extensively in your curriculum. It serves as the ultimate semantic foundation for the first half of your syllabus.
Because your course balances mathematical philosophy with raw computer code, you will study ZFC from two specific perspectives: as the formal model-theoretic universe where all of mathematics lives, and as a syntactic axiomatic system whose limits were exposed by computer science.
Here is exactly where ZFC appears in your textbooks and how it anchors your 16-week study plan:

---

## 1. Where ZFC Appears in Your Textbooks## 🔹 Chapter Zero: The Set-Theoretic Baseline (Week 1 Prep)

- The Text: [END] Chapter Zero (Useful Facts about Sets).
- What you learn: Enderton provides an uncompromised structural summary of functions, relations, sets, equinumerosity, and power sets. You will establish the exact mathematical notation used to build structures throughout the book.

## 🔹 Defining First-Order Models (Weeks 5 & 6)

- The Text: [END] Chapter 2.2 (Truth and Models).
- What you learn: When you study Tarski's Semantics, you will learn that a formal logical "Structure" (Model) is built completely out of sets. A universe of discourse is a set; a predicate variable is interpreted as a subset of that universe; an n-ary function is interpreted as a set of ordered tuples. You cannot define "truth" in first-order logic without using ZFC as your background engine.

## 🔹 The Limits of Set Theory (Weeks 7 & 10)

- The Text: [END] Chapter 2.6 (Models of Theories) & Chapter 3.5 (Gödel's Incompleteness Theorems).
- What you learn: This is where the curriculum exposes the fundamental crisis of mathematical foundations:
- The Löwenheim-Skolem Theorem (Week 7): You will study Skolem’s Paradox. ZFC is a first-order theory designed to prove the existence of massive, uncountable infinities (like the real number line). You will prove that if ZFC is consistent, it must have a countable model—a universe the size of basic whole numbers where all the axioms of set theory remain perfectly true.
  - Gödel's Second Incompleteness Theorem (Week 10): You will use arithmetic properties to prove that if ZFC is a consistent system, it can never prove its own consistency.

---

## 2. The Theoretical Disruption: ZFC vs. Type Theory

As you pass through Phase 3 (Weeks 11 & 12) and enter Sørensen & Urzyczyn's text, your curriculum will expose the magnificent design fork between standard math and computer code:

                      [ FOUNDATIONAL FORK ]
                                │
         ┌──────────────────────┴──────────────────────┐
         ▼                                             ▼

[ THE MATHEMATICIAN'S ROCK ] [ THE COMPUTER'S ROCK ]
ZFC Set Theory Type Theory & Lambda Calculus
(Enderton Weeks 1-10) (Sørensen Weeks 11-14)

• Untyped: Anything can be a set. • Typed: Every element has a strict type.
• Errors caught via Paradoxes (Russell's). • Errors caught via Type-Checking (Lean Kernel).
• Foundation based on standard truth. • Foundation based on constructive computation.

- ZFC solves logic bugs (like Russell's Paradox—the set of all sets that do not contain themselves) by enforcing strict axiomatic gatekeepers like the Axiom of Regularity.
- Type Theory (which powers Lean and Agda in Week 14) solves the exact same bugs by creating a hierarchy of "Universes" and strict variable types. In Type Theory, writing a paradoxical statement is impossible because it simply breaks the compiler's syntax formatting rules, failing to compile.

By mastering ZFC in the first 10 weeks via Enderton and then pivoting to Type Theory via Sørensen, you will fully understand why classical mathematicians choose sets to map out abstract geometries, while computer scientists choose type frameworks to build bulletproof verification software.
Your notebook is perfectly primed to balance both tracking systems. Are you ready to log your final Week 1 study targets, or would you like to review Enderton's Chapter Zero axioms first?
To ensure your workspace matches the curriculum perfectly, let me know if you need:

- The exact digital links/DOIs for the Datalog± research papers integrated into your advanced addendum.
- A quick overview of how Russell's Paradox is written in ZFC syntax versus how it breaks in a Typed Type Theory framework to preview Week 11.
- The terminal commands to set up your OCaml workspace for Harrison's Phase 1 labs.
