Yes, your curriculum covers both of Gödel's Incompleteness Theorems in complete, uncompromised, mathematical detail.
In fact, this is the grand climax of the first half of your syllabus. You will not just read about the theorems as philosophical trivia; your textbooks will force you to roll up your sleeves and walk through the actual step-by-step mathematical proofs.
Both Herbert Enderton (A Mathematical Introduction to Logic) and Sørensen & Urzyczyn (Lectures on the Curry-Howard Isomorphism) approach Gödel's breakthroughs, but they do so from opposite sides of the logic mirror.

---

## 1. The Pure Mathematical Approach (Enderton)

Enderton dedicates Chapter 3 to proving Gödel's theorems using classical model theory and recursive functions. He breaks the proof down into the three classic steps that Kurt Gödel invented in 1931:

- Gödel Numbering (Arithmetization of Syntax): You will learn how to turn raw logic symbols, formulas, and entire step-by-step proofs into unique, massive whole numbers. This allows a mathematical language (like arithmetic) to look at itself in the mirror and talk about its own structure using raw math.
- The Diagonal Lemma (The Self-Reference Step): Enderton walks you through the construction of a very special mathematical formula, traditionally called G. Using Gödel numbering, formula G mathematically asserts: "This formula has no proof inside this system."
- The First Theorem Proof: You will formally prove Gödel's First Incompleteness Theorem: If a formal system of math is consistent (doesn't contradict itself), then formula G is true, but it can never be proved using the rules of that system.
- The Second Theorem Proof: Enderton then shows you how to formalize the statement "This system is consistent" as its own Gödel number. He then proves Gödel's Second Incompleteness Theorem: A consistent system of mathematics can never prove its own consistency.

---

## 2. The Computer Science Approach (Sørensen & Urzyczyn)

Sørensen and Urzyczyn approach Gödel's theorems from the perspective of Type Theory and the Halting Problem.
Instead of dealing with the tedious arithmetic of Gödel numbering, they show you the beautiful modern shortcut discovered by computer scientists: Gödel's Incompleteness is just the logical consequence of the Halting Problem.

[ THE HALTING PROBLEM ] ─────────────────────────► [ GÖDEL'S INCOMPLETENESS ]
Computers can never write an Math systems can never prove
algorithm to check if _any_ program every true statement because some truths
will loop forever or finish running. hide behind infinite computer loops.

- Proof via Computation: You will study how, if a perfect and complete mathematical system existed, you could easily use it to build a computer program that solves the Halting Problem.
- The Contradiction: Since Alan Turing already proved that a Halting-solver is physically and mathematically impossible, the perfect math system cannot exist. Therefore, any consistent mathematical proof-checking language (like Lean, Agda, or basic arithmetic) must inherently be incomplete.

---

## The Ultimate Takeaway

By covering Gödel through both textbooks, you get the absolute complete picture:

1.  Enderton shows you the historical, internal mechanics of how the math breaks down from the inside via self-reference.
2.  Sørensen shows you the high-level perspective of why it breaks down due to the fundamental nature of computation.

Would you like to explore how the concept of self-reference works using a simple English analogy, or are you ready to jump into how to structure your weekly reading schedule to make sure you have the mathematical stamina to tackle Enderton's Chapter 3?
