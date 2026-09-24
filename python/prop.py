from dataclasses import dataclass
from typing import Callable, Any, Union
from formulas import (
    parse_formula,
    T,
    _True,
    _False,
    Atom,
    And,
    Or,
    Not,
    Imp,
    Iff,
    Formula,
    print_qformula,
)


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
    def parser_closure(tokens: list[str]) -> tuple[Formula, list[str]]:
        return parse_formula(ifn=None, afn=parse_propvar, vs=[], inp=tokens)

    return make_parser(parser_closure)(inp)


# Interpretation of formulas
def eval_formula(fm: Formula[T], v: Union[Callable[[T], bool], dict[T, bool]]) -> bool:
    """
    Evaluates the truth value of a propositional formula given a valuation function or dict v.
    """

    # Helper to resolve atom values safely whether 'v' is a dict or a function
    def get_valuation(atom_val: T) -> bool:
        if isinstance(v, dict):
            return v[atom_val]
        return v(atom_val)

    match fm:
        case _False():
            return False

        case _True():
            return True

        case Atom(value):
            return get_valuation(value)

        case Not(p):
            return not eval_formula(p, v)

        case And(p, q):
            return eval_formula(p, v) and eval_formula(q, v)

        case Or(p, q):
            return eval_formula(p, v) or eval_formula(q, v)

        case Imp(p, q):
            return (not eval_formula(p, v)) or eval_formula(q, v)

        case Iff(p, q):
            return eval_formula(p, v) == eval_formula(q, v)

        case _:
            raise TypeError(f"Cannot evaluate non-propositional formula node: {fm}")


def print_propvar(_: int, p: P) -> str:
    return p.name


def print_prop_formula(fm: Formula[P]) -> None:
    print_qformula(print_propvar, fm)
