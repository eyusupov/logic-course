Yes, your curriculum covers the Theory of Computation and the Church-Turing Thesis in deep, mathematically rigorous detail.
In fact, it approaches this topic from two entirely different angles: the classical mathematical view (how it was discovered in the 1930s) and the modern functional programming view (how we think about it today).
Here is exactly how your textbooks unpack the limits of what computers can calculate:

---

## 1. The Classical View: Foundational Limits

Your first textbook, Herbert Enderton's A Mathematical Introduction to Logic, dedicates an entire final chapter (Chapter 3) to Undecidability and Definability.

- What you will study: Enderton introduces the formal definition of Recursive Functions (a mathematical way to define calculation without using a physical machine) and Turing Machines.
- The Church-Turing Thesis: Enderton thoroughly explains the Church-Turing Thesis—the profound assertion that our intuitive, human notion of "what is calculable" maps perfectly and exactly onto what a Turing machine can execute.
- The Big Proof: You will walk through a mathematically rigorous proof of the Halting Problem (Turing 1937) and show how it leads directly to Gödel's Incompleteness Theorem. You will prove that because computation has absolute limits, a perfect, all-knowing mathematical proof-machine is physically and logically impossible.

## 2. The Modern View: Computation as Evaluation

Your third textbook, Sørensen and Urzyczyn's Lectures on the Curry-Howard Isomorphism, covers computation from a purely computer-science perspective.

- What you will study: It focuses heavily on the Untyped Lambda Calculus (Alonzo Church's 1932/1936 model of computation).
- The Computational Connection: Instead of visualizing a Turing machine moving a paper tape left and right, you will learn how computation can be done entirely by rewriting strings of text using substitutions (called $\beta$-reduction).
- The Church-Turing Thesis (Revisited): Sørensen's book proves that the Lambda Calculus is "Turing-complete." You will learn how to build numbers, math operations, and recursive loops (using the famous Y Combinator) out of nothing but pure, unadulterated functions. It shows you the exact proof that Church's functional model is identical in power to Turing's machine model.

---

## How Your Books Divide the Theory of Computation

To keep your bearings while studying, it helps to understand how these two books complement each other:

                  [ THEORY OF COMPUTATION ]
                             │
       ┌─────────────────────┴─────────────────────┐
       ▼                                           ▼

[ ENDERTON: The Machine View ] [ SØRENSEN: The Functional View ]
• Focuses on Turing Machines. • Focuses on Lambda Calculus.
• Treats code like hardware steps. • Treats code like mathematical equations.
• Explains the Halting Problem. • Explains Halting via "Normalization".
• Proves what computers CANNOT do. • Explains exactly HOW programs execute.

## The Big Picture

By combining these texts, you get a much richer understanding of computation than a standard computer science student. A typical CS student only learns the machine view (Turing machines, states, and tapes).
Your curriculum forces you to see the magnificent truth of the Church-Turing Thesis: whether you build a mechanical computer out of gears, a modern microchip out of transistors, or a pure mathematical system out of lambda functions, they all hit the exact same boundaries of logic at the exact same moment.
Would you like to see how a simple loop or a number (like the number 2) is built out of pure functions in the Lambda Calculus to see how Church defined computation? Alternatively, we can map out a weekly reading schedule to balance Enderton's math chapters with Sørensen's computation chapters.
