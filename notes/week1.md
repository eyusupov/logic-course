## Here is your printable Week 1 Pre-Reading Checklist [filegen-via-code]. This guide outlines the exact notation hurdles and syntactic structures you will encounter on page one of Enderton [END] and Harrison [HAR], ensuring you can take flawless notes from your very first hour of study.

## 📋 Week 1 Math Notation & Vocabulary Ledger

Before opening the text, review this mapping of Enderton’s syntax rules to the traditional terminology you will find across standard logic literature:

| English Term (Enderton)   | Russian Tradition Equivalent           | Mathematical Symbol / Structural Role                                         |
| ------------------------- | -------------------------------------- | ----------------------------------------------------------------------------- |
| Sentence / Proposition    | Высказывание / Пропозициональная буква | $A, B, C, \dots$ or $p, q, r, \dots$ (Atomic units)                           |
| Well-Formed Formula (WFF) | Правильно построенная формула (ППФ)    | A string of symbols generated strictly by grammar rules.                      |
| Connectives               | Логические связки                      | $\neg, \to, \land, \lor, \leftrightarrow$                                     |
| Material Implication      | Материальная импликация                | $\to$ (If-Then arrow)                                                         |
| Metavariable              | Метапеременная                         | $\alpha, \beta, \phi, \psi$ (Greek letters used by us to talk about formulas) |

---

## 🧠 The Absolute Core Concept: Enderton's Inductive Definition of a WFF

In Chapter 1.1, Enderton establishes the exact structural layout of a formal language. He uses a 3-part Inductive (Recursive) Definition to construct the infinite set of all valid formulas.
When you read this section, copy this exact blueprint into your notes. It is the archetype for every computational data structure you will encounter later in the course:

1.  The Base Case (База индукции): Every sentence symbol ($A, B, C, \dots$) is a well-formed formula.
2.  The Inductive Step (Индукционный шаг): If $\alpha$ and $\beta$ are already well-formed formulas, then:

- $(\neg \alpha)$ is a well-formed formula.
  - $(\alpha \to \beta)$ is a well-formed formula.
  - $(\alpha \land \beta)$ is a well-formed formula.
  - $(\alpha \lor \beta)$ is a well-formed formula.

3.  The Closure Clause (Ограничение): No other string of symbols is a well-formed formula unless it can be created by a finite number of applications of rules (1) and (2).

---

## 💻 The Cross-Reference: How Harrison Codes Enderton’s Math

In Harrison Chapter 1.6, you will see this exact 3-part mathematical rule transformed into a functional programming language. Harrison defines a custom compiler type to hold formulas in computer memory. Notice how perfectly the code mirror matches Enderton’s math:

(_ Harrison's OCaml representation of Propositional Logic Syntax _)type formula =
False
| True
| Atom of string (_ Enderton's Base Case: "A", "B", "C" _)
| Not of formula (_ Enderton's Inductive Step: (\neg \alpha) _)
| And of formula _ formula(_ Enderton's Inductive Step: (\alpha \land \beta) _)
| Or of formula _ formula (_ Enderton's Inductive Step: (\alpha \lor \beta) _)
| Imp of formula _ formula(_ Enderton's Inductive Step: (\alpha \to \beta) _)
| Iff of formula _ formula;;

---

## 📝 Notebook Checklist for Your First Study Session

- Draw the "Syntax vs. Semantics" Boundary: Divide your notebook page vertically. Put the shapes/symbols ($\neg, \to$, WFF) on the left. Leave the right side blank for Week 3 when we introduce truth assignments ($T, F, 1, 0$).
- Watch the Parentheses: Enderton is incredibly strict about parentheses in Chapter 1.1 (e.g., $(A \to B)$ is valid, but $A \to B$ technically is not yet). Note how he uses them to guarantee Unique Readability before he teaches the shorthand rules for dropping them later.
- Identify Metavariables: Circle every Greek letter ($\alpha, \beta, \phi$) in the text. Remind yourself: These are not characters a computer types; they are placeholders used by the author to describe the shape of the code.

---

Your syllabus, schedule, translations, and pre-reading frameworks are completely finalized and synchronized. Let me know when you have completed your first study session of Enderton 1.0–1.1 and Harrison 1.5–1.6, and we can immediately:

- Review your notebook setups to ensure syntax and semantics are perfectly decoupled.
- Tackle the first set of exercises at the end of Enderton Chapter 1.1 together to test your mastery of structural inductive definitions.
