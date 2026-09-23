To help you navigate Week 1 using the Russian mathematical logic tradition, it is highly useful to know that Russian textbooks (like those by Kolmogorov and Dragalin, or Mendelson's translation) use very stable, specific terminology. Russian mathematical prose tends to be slightly more descriptive and deeply rooted in Bourbaki-style structuralism.
Here is the master translation index for the core terms you will encounter in Chapter 1 of Enderton, paired with their precise equivalents in the Russian mathematical tradition.

---

## 🏛️ Core Syntax & Language (Синтаксис и язык)

- Sentential Logic / Propositional Logic
- 🇷🇺 Исчисление высказываний (or Логика высказываний)
  - Note: Russian tradition heavily favors "высказывание" (utterance/statement) over "предложение" (sentence) when referring to the logical calculus.
- Sentence / Proposition
- 🇷🇺 Высказывание (or Пропозициональная переменная)
- Well-Formed Formula (WFF)
- 🇷🇺 Правильно построенная формула (ППФ)
  - Note: You will often see this abbreviated as just формула once the context is established.
- Connectives
- 🇷🇺 Логические связки (or Логические операции)
- Material Implication ($\to$)
- 🇷🇺 Материальная импликация (often just Импликация)
  - Note: The "if-then" arrow. The left side is called the антецедент (antecedent) or посылка (premise), and the right side is the консеквент (consequent) or заключение (conclusion).
- Negation ($\neg$)
- 🇷🇺 Отрицание
- Conjunction ($\land$ or $\&$)
- 🇷🇺 Конъюнкция (colloquially: логическое «И»)
- Disjunction ($\lor$)
- 🇷🇺 Дизъюнкция (colloquially: логическое «ИЛИ»)

---

## 🧬 Induction & System Rules (Индукция и правила)

- Unique Readability
- 🇷🇺 Теорема об однозначной читаемости (or Однозначность разбора)
  - Note: This is Enderton's tedious proof showing that formulas aren't ambiguous. In Russian computer science, this is often linked to однозначность грамматики.
- Mathematical Induction
- 🇷🇺 Математическая индукция
- Inductive Definition / Recursive Definition
- 🇷🇺 Индуктивное определение / Рекурсивное определение
- Base Case / Induction Step
- 🇷🇺 База индукции / Индукционный шаг (or Шаг индукции)

---

## 🌍 Semantics & Truth (Семантика и истинностные значения)

- Truth Assignment ($v$)
- 🇷🇺 Истинностное означивание (or simply Означивание, sometimes Распределение истинностных значений)
  - Note: Enderton uses the function $v$ to assign True/False to variables. In Russian, applying a function to assign these values is called означивание.
- Truth Value
- 🇷🇺 Истинностное значение (or Значение истинности)
  - Enderton's $T$ and $F$ map to И (Истина / True) and Л (Ложь / False), or frequently 1 and 0 in computer science contexts.
- Tautology
- 🇷🇺 Тавтология (or Тождественно истинная формула)
  - Note: Russian textbooks lean heavily on "Тождественно истинная" (identically true) to emphasize that the formula is a law of logic regardless of input.
- Satisfiable
- 🇷🇺 Выполнимая формула
  - Note: A formula is satisfiable if there is at least one row in a truth table where it evaluates to True (1).
- Unsatisfiable / Contradiction
- 🇷🇺 Невыполнимая формула / Противоречие (or Тождественно ложная формула)
- Truth Table
- 🇷🇺 Таблица истинности

---

## ⚠️ A Meta-Language Warning for Russian Readers

When Enderton uses lowercase Greek letters like $\alpha, \beta, \phi$ to talk about formulas, he is using a meta-language (метаязык).
In Russian literature, these are strictly referred to as метапеременные (metavariables). Be careful not to confuse them with the actual variables inside the language formula, which are usually English letters ($A, B, C$ or $p, q, r$), referred to as пропозициональные буквы (propositional letters).

---

Would you like to preview Enderton's exact mathematical layout for an induction proof translated into this Russian terminology style, or are you ready to jump directly into your Week 1 reading?
