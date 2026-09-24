from formulas import lex, atoms
from prop import (
    parse_prop_formula,
    print_prop_formula,
    P,
    eval_formula,
    print_truthtable,
)


# A valid propositional syntax string
raw_input = "p /\\ q ==> ~r"
print(f"1. Raw User Input:   '{raw_input}'")

# Execute Lexer
tokens = lex(raw_input)
print(f"2. Lexed Tokens:     {tokens}")

# Pass tokens to the propositional parser wrapper
parsed_ast = parse_prop_formula(tokens)
print(f"3. Generated AST:    {parsed_ast}")

# Pass the AST to the printer interface
print("4. Final Printout:   ", end="")
print_prop_formula(parsed_ast)

eval_ = eval_formula(parsed_ast, {P("p"): True, P("q"): True, P("r"): True})
print(f"5. Eval result:      {eval_}")

atoms_ = atoms(parsed_ast)
print(f"6. Atoms:            {atoms_}")

print("7. Truth table:")
print_truthtable(parsed_ast)
