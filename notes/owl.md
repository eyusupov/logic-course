Yes, the theory behind OWL (Web Ontology Language) fits into your curriculum perfectly.
In fact, you have unintentionally selected the exact combination of textbooks needed to completely deconstruct how OWL functions. The theory behind OWL is not an isolated branch of computer science; it is a direct application of the specific mathematical logic and automated reasoning systems you are about to study.
Here is exactly where the theory of OWL lives within your 20-week schedule:

---

## 1. What OWL Actually Is: Description Logics (Weeks 5 & 6)

- The Textbooks: [END] Chapter 2 (First-Order Logic) and [HAR] Chapter 3 (First-Order Logic Implementation).
- The Theory: Philosophically, OWL looks like a modern data tool used for the Semantic Web. Mechanically, OWL is a syntax for Description Logics (DL). Description Logics are a highly structured subset of standard First-Order Logic.
- What you learn: When you study how to construct predicates, domains, and properties in Enderton, you are learning the exact mathematical foundations of OWL's components (Classes, Individuals, and Object Properties).

## 2. Why OWL Has Sublanguages (OWL Lite, OWL DL): Decidability (Weeks 9 & 13)

- The Textbooks: [END] Chapter 3 (Undecidability) and [HAR] Chapter 5 (Decidable Problems).
- The Theory: Full First-Order Logic is undecidable (as you will prove in Week 9 via Turing and Church)—meaning a computer can get stuck in an infinite loop trying to prove if a statement is true or false.
- What you learn: To make OWL usable for enterprise software, computer scientists had to carefully restrict its grammar so that a computer is guaranteed to find an answer in a finite amount of time. In Week 13 (Decidable Problems), you will study the exact mathematical limits and algorithms used to isolate these "decidable subsets" of logic, showing you exactly why OWL DL can be computed reliably while full logic cannot.

## 3. How OWL "Thinks": Tableau Reasoning Engines (Week 8)

- The Textbook: [HAR] Chapter 3.10 (Tableaux).
- The Theory: If you give an OWL ontology a set of rules (e.g., "All Humans are Mammals. Socrates is a Human."), how does the computer infer that Socrates is a mammal? It does not use Prolog-style resolution. It uses a Tableau Algorithm (specifically, variants like $\mathcal{SHIQ}$ or $\mathcal{SHOIN}$).
- What you learn: John Harrison's Table of Contents explicitly includes Chapter 3.10: Tableaux. In Phase 2, you will learn the exact mathematics behind Tableau proof systems. You will understand how an OWL reasoner (like HermiT or Pellet) systematically breaks down statements, checks for contradictions, and automatically infers new knowledge from your data graphs.

---

## The Big Picture Integration

Your curriculum maps to OWL's architecture in a clean, linear stack:

[ OWL DATA / SENTENCE ] ───► [ DESCRIPTION LOGIC ] ───► [ TABLEAU SOLVER ] ───► [ ALGEBRAIC ADTs ]
The software format The mathematical format The execution engine The software component
(Semantic Web Syntax) (Enderton Chapter 2) (Harrison Chapter 3.10) (Manes & Arbib Phase 5)

By keeping Manes & Arbib for Phase 5, you get an added bonus: you will see how algebraic specifications define abstract data types. This allows you to understand how the graph data structures used by OWL (RDF Triples and Directed Acyclic Graphs) are securely represented and verified as software components.
You are fully equipped to understand every layer of OWL's theoretical engine. Have you gathered your physical copies of Enderton and Harrison to begin the Week 1 readings, or would you like to review any technical aspects of the OCaml environment configuration?
