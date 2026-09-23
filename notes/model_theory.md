Model Theory is woven deeply throughout Phase 2 and Phase 4 of your curriculum. In fact, your textbooks cover the absolute landmarks of 20th-century model theory.
Model Theory is the study of the relationship between formal languages (syntax) and their interpretations (semantics/models). While Proof Theory asks "Can we construct a mechanical chain of steps to prove this statement?", Model Theory asks "What does it mean for this statement to be true in a specific mathematical universe?" [1]
Here is exactly where Model Theory appears in your 16-week textbook readings and connects to the historical papers on your list:

---

## 🏛️ The Model Theory Core in Your Syllabus## 🔹 1. The Definitive Foundation: Tarski Semantics (Week 5)

- Required Reading: [END] Chapter 2.2 (Truth and Models) & [HAR] Chapter 3.3 (The semantics of first-order logic).
- What you learn: This is the absolute starting point of modern model theory. You will learn Alfred Tarski's formal definition of truth (1926–1928). You will study how to mathematically define a Structure (a Model), establish a universe of discourse, and use a valuation function to calculate whether a first-order logic sentence is satisfied by that universe.

## 🔹 2. The Great Model Limits: Löwenheim-Skolem & Compactness (Weeks 6 & 7)

- Required Reading: [END] Chapter 2.5 (Soundness and Completeness Theorems) & Chapter 2.6 (Models of Theories).
- What you learn: You will study two of the most profound metatheorems in model theory:
- The Compactness Theorem: Proving that if every finite subset of a massive theory has a model, the entire infinite theory has a model.
  - The Löwenheim-Skolem Theorem (1915/1922): This theorem shatters the dream that first-order languages can perfectly pin down unique mathematical realities. You will explore Skolem's Paradox—proving that a first-order system designed to talk about massive, uncountable infinities (like the real number line) can accidentally be satisfied by a tiny, countable model (the size of whole numbers).
  - Non-Standard Models of Arithmetic: You will learn how the Peano axioms can be satisfied by "fake" universes containing infinite numbers sitting way past our normal whole numbers.

## 🔹 3. Applied Model Theory: Quantifier Elimination (Week 13)

- Required Reading: [HAR] Chapter 5.6 to 5.9 (Quantifier elimination, Presburger arithmetic, Real numbers).
- What you learn: You transition to constructive, algorithmic model theory. You will study Tarski’s 1948 proof that the first-order theory of Real Closed Fields (the geometry of real numbers with addition and multiplication) is completely decidable. You will look at how an SMT solver like Z3 uses algebraic geometry to eliminate quantifiers ($\forall, \exists$), reducing complex spatial model constraints into simple, solvable coordinates.

## 🔹 4. Fixed-Point Model Semantics: Datalog & Prolog (Weeks 15 & 16)

- Required Reading: [LLY] Chapter 2 (Semantics of Logic Programs) & [ULL (Vol. 2)] Chapter 13.
- What you learn: This is where model theory meets database storage engines. You will learn Herbrand Models (models built entirely out of the text strings of the language itself). You will use the Knaster-Tarski Fixed-Point Theorem to calculate the Least Herbrand Model—the unique, mathematically minimal universe that contains all the true facts deduced by a recursive database query.

---

## 📊 The Two Rival Structural Kingdoms

To help keep your bearings while reading your ledger, remember that your books continuously alternate between these two sides of the logic mirror:

| 🧩 Syntax & Proof Theory (Harrison / Sørensen)        | 🌍 Semantics & Model Theory (Enderton / Lloyd / Ullman)     |
| ----------------------------------------------------- | ----------------------------------------------------------- |
| Focuses on symbols, axioms, and derivation trees.     | Focuses on universes, domains, and mathematical structures. |
| Asks: "Can a machine find a path to derive this?"     | Asks: "In what worlds or data graphs is this formula true?" |
| Key Figures: Peano, Gentzen, Herbrand, J.A. Robinson. | Key Figures: Dedekind, Löwenheim, Skolem, Alfred Tarski.    |

By combining Enderton's philosophical focus on models with Harrison's algorithmic code implementations, you aren't just learning abstract model definitions—you are learning exactly how to write software that evaluates, queries, and verifies these mathematical universes in real time.
Your 16-week roadmap is perfectly configured to capture this balance.
Are you ready to log your final notebook preparation strategies for Week 1, or would you like to look at a quick example of how a Model/Structure is formally defined in Enderton Chapter 2.2 to preview Phase 2?

- We can look at a simple set-theoretic model of a number line.
- We can generate a Week 1 checklist for your reading journal.
