LL(k), LL(1), LR(k), and related parsing grammars fit directly into Week 2 of your curriculum, specifically within Enderton’s Chapter 1.3 (A Parsing Algorithm) and Harrison’s Chapter 1.7 (Parsing).
These concepts represent the precise engineering boundary where Chomsky Type 2 (Context-Free) Grammars are restricted so that a computer program can parse a string deterministically in a single pass without guessing or backing up.
Here is exactly how they map to your weekly readings and why they are vital to your logic engine goals:

---

## 1. The Theory: Enderton’s Unique Readability (Week 2)

- The Text: [END] Chapter 1.3 & 1.4
- The Connection: Enderton spends a great deal of time proving the Unique Readability Theorem for propositional logic. He does this by showing that if you strictly enforce parentheses, every well-formed formula (WFF) maps to one—and only one—unique abstract syntax tree.
- The Grammar Fit: In the language of compiler design, the strict, fully parenthesized grammar of logic that Enderton defines is a beautifully simple LL(1) grammar. The "LL(1)" designation means the computer can read the string from Left-to-right, produce a Leftmost derivation tree, and it only needs to look ahead 1 single symbol (token) to know exactly which rule to apply.
- Example: If the parser reads an opening parenthesis (, it knows a nested compound sub-formula is starting. If it reads a variable letter A, it knows it has hit an atomic base term.

## 2. The Code: Harrison's Recursive Descent Parsers (Week 2)

- The Text: [HAR] Chapter 1.7 (Parsing)
- The Connection: While Enderton proves that unique parsing trees exist mathematically, John Harrison shows you how to write the software that constructs them.
- The Grammar Fit: Harrison implements what is called a Recursive Descent Parser in OCaml. Recursive descent is the definitive, standard coding pattern used to process LL(1) grammars. You will write OCaml functions that match tokens sequentially. Because the grammar is LL(1), your code will be elegant and direct—it will never have to save its state, backtrack, or clear memory variables because a lookahead of one character completely eliminates ambiguity.

---

## Why the Curriculum Skips LR(k) Code Implementation

You might notice that Harrison skips building LR(k) or LALR parsing engines (which read from left-to-right but construct a Rightmost derivation in reverse).

- The Reason: LR(k) grammars are much more powerful and flexible than LL(1) grammars—they allow you to parse complex programming languages like C++ or Java where you don't want to force the human programmer to write annoying parentheses around every single math operation. However, LR(k) parsers are too structurally complex to write by hand cleanly; they require massive, automated code generators (like yacc, bison, or menhir).
- The Logic Approach: Because the languages of formal mathematical logic are structurally pure and highly parenthesized, they fit comfortably inside the simpler LL(1) or LL(k) space. Writing a custom LL(1) recursive descent parser by hand in Week 2 gives you a deep, immediate look at how text morphs into an algorithmic logic tree, without forcing you to learn a bloated, external compiler-design tool.

---

## The Big Picture Transition in Week 2

[ RAW INPUT STRING ] ──────────► [ $LL(1)$ PARSER CODE ] ──────────► [ ABSTRACT SYNTAX TREE ]
"((A AND B) -> C)" Harrison Chapter 1.7 Enderton Chapter 1.3
(OCaml Token Matching) (Unique Readability Verified)

By completing Week 2, you will see that LL(1) parsing is the gatekeeper of your entire curriculum. Before an SMT solver can check a formula, before a database can evaluate a query, and before Lean can check a type proof, a deterministic, single-pass LL grammar engine must validate the text string and shape it into a perfect mathematical tree structure.
You have mapped out the entire theoretical hierarchy of your course! Are there any other specific parsing or compiler terms you want to contextualize before opening [END] Chapter 1.0 to launch your studies?
