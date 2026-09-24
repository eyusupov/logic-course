Complexity classes are covered implicitly through the structural and algorithmic boundaries of your curriculum, but they are treated from the perspective of decidability and automated solver resource limits rather than a classical Complexity Theory textbook (which would focus on drawing Turing machine configurations or calculating time/space bounds like P vs. NP). [1, 2, 3]
Your curriculum focuses on Computability and Proof Theory, answering "Is it logically possible for a computer to solve this, and how can it check a proof?" rather than "How many milliseconds will it take?" [3]
Even so, you will encounter the exact mathematical logic rules that define major complexity classes: [1, 4]

## 1. Where Complexity Bounds Occur in Your Schedule

-
- Propositional Logic & NP-Completeness (Weeks 3 & 4):
  When you build a DPLL SAT Solver in [HAR] Chapter 2, you are handling the absolute definitive baseline problem of the NP complexity class: the Boolean Satisfiability Problem (SAT). Harrison walks you through the combinatorial explosion that occurs when trying to verify logic trees, giving you an immediate, practical understanding of why NP-Complete problems require specialized heuristic architectures. [1, 5]
- First-Order Logic & Undecidability (Weeks 9, 10, & 11):
  When you prove the Halting Problem and Gödel's Incompleteness Theorems in [END] Chapter 3, you are passing completely beyond standard complexity classes (like P, NP, or PSPACE) and entering the territory of Recursively Enumerable (RE) and Co-RE language classes. You will formally calculate the line where problems stop being hard and become literally impossible to compute. [1, 4]
- Decidable Subsets & PSPACE/EXPTIME Limits (Week 13):
  When you shift to [HAR] Chapter 5 (Decidable Problems) and [ULL], you will dissect background mathematical "theories" used by modern tools like Z3 and OWL DL reasoners. You will explicitly study the complexity limits of different mathematical systems:
- Presburger Arithmetic (integer addition) is decidable, but lives in 2-EXPTIME (exponentially explosive time constraints).
  - Real Closed Fields (Tarski’s geometric algorithms) run in exponential space bounds.
  - Description Logics (OWL DL) are mathematically bounded to PSPACE, NEXPTIME, or 2-EXPTIME limits depending on the exact expressiveness of their constraints.
-

---

## 2. The Theoretical Synthesis: Logic is Complexity

By the end of your education, your post-graduate studies in Manes & Arbib [M&A] will expose you to an elegant realization known as Descriptive Complexity Theory:

[ LOGICAL FORMALISM CLASS ] [ COMPUTATIONAL COMPLEXITY CLASS ]
Propositional Horn Clauses (Week 15) ───────────► Polynomial Time (P)
First-Order Logic (Week 5) ───────────► PSPACE (with fixed points)
Second-Order Existential Logic ───────────► NP
Unrestricted First-Order Logic ───────────► Undecidable (Beyond ALL resource classes)

You will see that a computational complexity class is not just an arbitrary measurement of computer hardware speed—it is the exact reflection of the syntactic strength of a logic language. Restricting what a programmer can express in their code (such as limiting logic rules to Horn Clauses in Prolog/Datalog) automatically traps the program's runtime inside a safe, efficient polynomial-time (P) execution envelope. [1, 2]
Your curriculum tracks these performance boundaries continuously through actual solver implementations. You are fully prepared to start Week 1 with this conceptual overview.

[1] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/Complexity_class)
[2] [https://www.cs.ox.ac.uk](https://www.cs.ox.ac.uk/teaching/courses/2022-2023/complexity/)
[3] [https://medium.com](https://medium.com/@parvekarvedant24/complexity-classes-630c8b7563f1)
[4] [https://ncatlab.org](https://ncatlab.org/nlab/show/complexity+class)
[5] [https://cseducators.stackexchange.com](https://cseducators.stackexchange.com/questions/3971/how-do-i-construct-a-basic-lesson-on-computational-complexity-and-undecidability)
