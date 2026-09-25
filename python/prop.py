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
    atoms,
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


# ------------------------------------------------------------------------- #
# Generates all possible truth combinations for a list of atoms             #
# ------------------------------------------------------------------------- #
def onallvaluations(
    subfn: Callable[[Callable[[P], bool]], bool], v: Callable[[P], bool], ats: list[P]
) -> bool:
    """
    Recursively tests all combinations of variable truth assignments.
    OCaml: let rec onallvaluations subfn v ats = ...
    """
    match ats:
        case []:
            return subfn(v)
        case [p, *ps]:
            # Create updated valuations v' for True and False cases
            # if q == p then t else v(q)
            def v_prime(t: bool):
                return lambda q: t if q == p else v(q)

            # The OCaml code uses '&' which forces evaluation of both branches
            left = onallvaluations(subfn, v_prime(False), ps)
            right = onallvaluations(subfn, v_prime(True), ps)
            return left and right
        case _:
            return False


# ------------------------------------------------------------------------- #
# Top-level Truth Table Printer Interface                                    #
# ------------------------------------------------------------------------- #
def print_truthtable(fm: Formula[P]) -> None:
    """
    Computes and formats a clean textual truth table for a formula.
    """
    # 1. Gather all unique atoms using your previously translated function
    ats: list[P] = atoms(fm)

    # 2. Determine column formatting width
    # In OCaml: width = itlist (max ** String.length ** pname) ats 5 + 1
    # We find the max name length among atoms, fallback to 5, and add 1
    max_atom_len = max([len(a.name) for a in ats]) if ats else 0
    width = max(max_atom_len, 5) + 1

    # Text alignments helpers using Python's native string format padding
    def truthstring(p: bool) -> str:
        s = "true" if p else "false"
        return f"{s:<{width}}"  # Left-align with dynamic spaces

    # 3. Create the printer callback for individual rows
    def mk_row(v: Callable[[P], bool]) -> bool:
        # Map values across atoms and format them
        lis = "".join(truthstring(v(x)) for x in ats)
        ans = truthstring(eval_formula(fm, v))
        print(f"{lis}| {ans}")
        return True

    # 4. Construct Header Interface
    header_atoms = "".join(f"{x.name:<{width}}" for x in ats)
    print(f"{header_atoms}| formula")

    separator = "-" * (width * len(ats) + 9)
    print(separator)

    # 5. Populate rows using a dummy fallback base valuation lambda x: False
    onallvaluations(mk_row, lambda _: False, ats)

    print(separator)


def tautology(fm: Formula[P]) -> bool:
    return onallvaluations(lambda v: eval_formula(fm, v), lambda _: False, atoms(fm))


def unsatisfiable(fm: Formula[P]) -> bool:
    return tautology(Not(fm))


def satisfiable(fm: Formula[P]) -> bool:
    return not (unsatisfiable(fm))
