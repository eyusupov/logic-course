The Chomsky Hierarchy fits directly into Phase 3 (Weeks 9–11) and Phase 1 (Week 2) of your curriculum.
While the hierarchy was originally developed by linguist Noam Chomsky to classify human grammatical structures, computer scientists quickly realized it is actually a map of computation classes [1]. Each level of the Chomsky hierarchy describes a language of a specific complexity, the exact type of formal grammar needed to generate it, and the exact type of physical or virtual machine needed to parse it.

---

## Where the Chomsky Hierarchy Fits into Your Schedule

[ CHOMSKY HIERARCHY LEVELS ]
Type 3: Regular ──────────► Type 2: Context-Free ────► Type 1: Context-Sensitive ──► Type 0: Unrestricted
(Automata / Regex) (Parsing Algorithms) (Linear Bounded) (Turing / Recursive)
│ │ │
▼ ▼ ▼
[ WEEK 2: HARRISON 1.7 ] [ WEEK 2: ENDERTON 1.3 ] [ WEEK 9-11: COMPUTABILITY ]
Tokenizing strings. Unique Readability & Tree Parsing. Turing Machines & Lambda Calculus.

## 1. Type 3: Regular Grammars (Weeks 1 & 2)

-
- The Machine: Finite Automata (DFA/NFA) with zero auxiliary memory [1].
- Where it fits: Harrison Chapter 1.7 (Parsing). When writing an automated solver, the first step is lexing (tokenizing) a raw string like "A AND (B -> C)" into discrete parts. This relies completely on Regular Expressions [1].
-

## 2. Type 2: Context-Free Grammars (Week 2)

-
- The Machine: Pushdown Automata (machines with a simple LIFO stack memory) [1].
- Where it fits: Enderton Chapter 1.3 (A Parsing Algorithm) & Harrison Chapter 1.7. The syntax of formal logic is strictly a Context-Free Language [1]. You cannot parse logic with a simple finite automaton because a regex cannot match matching pairs of parentheses arbitrarily deep. Enderton's rigorous mathematical proof of Unique Readability is structurally a proof that the context-free grammar of propositional logic is completely unambiguous.
-

## 3. Type 1: Context-Sensitive Grammars (Week 7)

-
- The Machine: Linear Bounded Automata (Turing machines with a memory tape restricted to the length of the input string).
- Where it fits: Harrison Chapter 3.6 (Skolemization). First-order logic variables and substitution domains introduce context dependencies (e.g., a variable x bound by a ∀ x modifier creates a context that dictates how formulas deep inside its scope behave).
-

## 4. Type 0: Unrestricted Grammars / Recursively Enumerable (Weeks 9–11)

-
- The Machine: The full, unrestricted Turing Machine or the Untyped Lambda Calculus [1].
- Where it fits: Enderton Chapter 3.6 (Recursive Functions) & Sørensen Chapters 1–2. This is the peak of the hierarchy. Type 0 languages represent anything that can be computed by a universal machine. When you study the Halting Problem and Gödel's Incompleteness Theorem, you are discovering the absolute structural edge of the Type 0 boundary—the point where human mathematics encounters questions that no unrestricted grammar or computer can solve.
-

---

## The Chomsky Structural Map

The hierarchy explicitly illustrates that each layer is a restricted subset of the layer above it:

## The Synthesis: Grammars as Logics

By tracking the Chomsky Hierarchy across your textbooks, you will see a profound philosophical connection: A grammar is just a logical system of rules, and a machine is just an execution of those rules.

-
- When you read Harrison’s parsing chapters, you will watch Type 3 and Type 2 systems assemble code strings.
- When you read Enderton’s computability chapters, you will watch Type 0 systems define what is physically calculable in the universe.
-

Would you like to look at the exact context-free grammar rules that Enderton uses in Chapter 1.1 to show how a well-formed formula is constructed, or should we review how OCaml manages algebraic data types to implement Type 2 syntax trees?
