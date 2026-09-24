from dataclasses import dataclass
from typing import Callable, Any
from syntax import parse_formula, Atom


# Assuming P is a wrapper class or just a string constructor for the atom value
# In Harrison's code, P(p) is a distinct type constructor for propositional variables.
@dataclass(frozen=True)
class P:
    name: str

    def __repr__(self):
        return self.name


def parse_propvar(vs: list[str], inp: list[str]) -> tuple[Atom[P], list[str]]:
    """
    Parses a single propositional variable.
    OCaml: p::oinp when p <> "(" -> Atom(P(p)), oinp
    """
    match inp:
        case [p, *oinp] if p != "(":
            return Atom(P(p)), oinp
        case _:
            raise ValueError("parse_propvar")


def make_parser(
    parser_func: Callable[[list[str]], tuple[Any, list[str]]],
) -> Callable[[list[str]], Any]:
    """
    Harrison's 'make_parser' wrapper. It runs the parser and ensures
    that the token stream is fully consumed (no leftover trailing tokens).
    """

    def wrapper(inp: list[str]) -> Any:
        ast, rest = parser_func(inp)
        if rest:
            raise ValueError(f"Extraneous tokens at end of formula: {rest}")
        return ast

    return wrapper


# Define the entrypoint function matching 'parse_prop_formula'
def parse_prop_formula(inp: list[str]) -> Formula[P]:
    # We pass None for ifn instead of an exception-throwing lambda,
    # and we pass an empty list [] for vs (bound variables)
    parser_closure = lambda tokens: parse_formula(
        ifn=None, afn=parse_propvar, vs=[], inp=tokens
    )
    return make_parser(parser_closure)(inp)
