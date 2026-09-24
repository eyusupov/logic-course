from prop import parse_prop_formula, P
from syntax import lex, print_qformula


# coding: utf-8
# Define our propositional atom printer matching our P object structure
def custom_p_printer(pr: int, p_obj: P) -> str:
    return p_obj.name


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
print_qformula(custom_p_printer, parsed_ast)
