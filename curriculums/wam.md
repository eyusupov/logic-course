- [AK] Hassan Aït-Kaci, Warren's Abstract Machine: A Tutorial Reconstruction (MIT Press / Available Open-Access).

## 🔹 Week 17: Memory Layouts, Choice Points, and Backtracking State

- Required Reading: [AK] Chapter 2 (The Purely Functional Machine) & Chapter 3 (The Control Structure).
- Core Concepts: Structuring the WAM memory areas: The Heap, the Stack, and the Trail; Allocating Environment Frames; Choice Points (saving the complete state of the machine before trying an alternative logic clause); The Trail Stack (unwinding pointer modifications during backtracking).

## 🔹 Week 18: Optimized Syntactic Unification in Hardware

- Required Reading: [AK] Chapter 4 (Unification) & Chapter 5 (Optimizations).
- Core Concepts: Compiling symbolic Prolog terms directly into flat WAM instructions (put_structure, get_variable, unify_value); Optimizing Robinson's Unification Algorithm into simple pointer-equality checks; Register allocation strategies.
- The Final Loop Close: This connects back to Week 8 (Unification) [HAR]. You see how the abstract symbol-matching algorithm you wrote in Month 2 is flattened into a low-level, high-performance sequence of register operations.

---

## 🎨 Updated Structural Landscape

By isolating the WAM to a postgraduate track, your computational paradigms remain cleanly partitioned:

```text
 [ PROLOG AS A LOGIC SYSTEM ] ────────► [ PROLOG AS A MACHINE DATA LOOP ] ────────► [ PROLOG AS BYTECODE ASSEMBLY ]
  Harrison Chapter 3.14                  Lloyd Chapter 3                            Aït-Kaci Chapters 2-5 (Optional)
  High-level OCaml functional            Abstract mathematical SLD-resolution       Low-level, stateful register
  recursive pattern interpreter.          fixed-points on data lattices.             virtualization architecture (WAM).
```

Keep your core 16 weeks locked down. Master the semantic and type-theoretic foundations first, then step down into the hardware compilation layer if your career goals require you to build logic compilers.
To finalize your planning and begin your first readings, let me know your immediate next step:

- Would you like to formally lock in this 16-week baseline and receive a final, unified copy of your syllabus?
- Or are you ready to get your OCaml workspace initialization scripts to start coding Phase 1?
