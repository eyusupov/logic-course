import re

from abc import ABC
from dataclasses import dataclass
from typing import TypeVar, Generic, Callable, Optional

# Define a TypeVar to represent the generic 'a
T = TypeVar("T")


# The base class inherits from Generic[T] to mirror ('a) formula
class Formula(ABC, Generic[T]):
    pass


@dataclass(frozen=True)
class _False(Formula[T]):
    pass


@dataclass(frozen=True)
class _True(Formula[T]):
    pass


@dataclass(frozen=True)
class Atom(Formula[T]):
    value: T  # This holds the type 'a (e.g., a string, int, etc.)


@dataclass(frozen=True)
class Not(Formula[T]):
    formula: Formula[T]


@dataclass(frozen=True)
class And(Formula[T]):
    left: Formula[T]
    right: Formula[T]


@dataclass(frozen=True)
class Or(Formula[T]):
    left: Formula[T]
    right: Formula[T]


@dataclass(frozen=True)
class Imp(Formula[T]):
    left: Formula[T]
    right: Formula[T]


@dataclass(frozen=True)
class Iff(Formula[T]):
    left: Formula[T]
    right: Formula[T]


@dataclass(frozen=True)
class Forall(Formula[T]):
    variable: str
    formula: Formula[T]


@dataclass(frozen=True)
class Exists(Formula[T]):
    variable: str
    formula: Formula[T]


# Parsing


def lex(formula_str: str) -> list[str]:
    """
    Takes a raw string formula and breaks it into a list of logical tokens.
    Slashes and arrows are matched first to prevent partial token cutting.
    """
    # 1. Compile the regex pattern
    # Order matters: check multi-character symbols first (e.g. '<=>' before '~')
    token_pattern = re.compile(
        r"(?:"
        r"<=>"  # Bi-implication
        r"|==>"  # Implication
        r"|/\\"  # Conjunction (/\)
        r"|\\/"  # Disjunction (\/)
        r"|[().~]"  # Single character symbols: ( ) . ~
        r"|[a-zA-Z0-9_]+"  # Words, variables, names, "forall", "exists"
        r")"
    )

    # 2. Find all matches in the input string
    return token_pattern.findall(formula_str)


def parse_right_infix(
    opsym: str,
    constructor: Callable[[Formula, Formula], Formula],
    subparser: Callable[[list[str]], tuple[Formula, list[str]]],
    inp: list[str],
) -> tuple[Formula, list[str]]:
    """Idiomatic right-associative infix parser using a clean loop."""
    left, rest = subparser(inp)

    if rest and rest[0] == opsym:
        # Recursively parse the right side to enforce right-associativity
        right, final_rest = parse_right_infix(opsym, constructor, subparser, rest[1:])
        return constructor(left, right), final_rest

    return left, rest


def parse_atomic_formula(
    ifn: Optional[Callable[[list[str], list[str]], tuple[Formula, list[str]]]],
    afn: Callable[[list[str], list[str]], tuple[Formula, list[str]]],
    vs: list[str],
    inp: list[str],
) -> tuple[Formula, list[str]]:
    match inp:
        case []:
            raise ValueError("formula expected")
        case ["false", *rest]:
            return _False(), rest
        case ["true", *rest]:
            return _True(), rest
        case ["(", *rest]:
            # 1. Idiomatically check if a custom infix parser was provided
            if ifn is not None:
                result = ifn(vs, inp)
                if result is not None:  # Assuming ifn returns None if it doesn't match
                    return result

            # 2. Clean fallback to default parenthesized grouping
            ast, after_body = parse_formula(ifn, afn, vs, rest)
            if after_body and after_body[0] == ")":
                return ast, after_body[1:]
            raise ValueError("Closing bracket expected")

        case ["~", *rest]:
            ast, final_rest = parse_atomic_formula(ifn, afn, vs, rest)
            return Not(ast), final_rest
        case ["forall", x, *rest]:
            return parse_quant(ifn, afn, [x] + vs, Forall, x, rest)
        case ["exists", x, *rest]:
            return parse_quant(ifn, afn, [x] + vs, Exists, x, rest)
        case _:
            return afn(vs, inp)


def parse_quant(
    ifn: Callable, afn: Callable, vs: list[str], qcon: Callable, x: str, inp: list[str]
) -> tuple[Formula, list[str]]:
    match inp:
        case []:
            raise ValueError("Body of quantified term expected")
        case [y, *rest]:
            if y == ".":
                ast, final_rest = parse_formula(ifn, afn, vs, rest)
                return qcon(x, ast), final_rest
            else:
                return parse_quant(ifn, afn, [y] + vs, qcon, y, rest)


def parse_formula(
    ifn: Callable, afn: Callable, vs: list[str], inp: list[str]
) -> tuple[Formula, list[str]]:
    # Clearer functional abstraction with flat argument chains
    def parse_layer1(i):
        return parse_atomic_formula(ifn, afn, vs, i)

    def parse_layer2(i):
        return parse_right_infix("/\\", And, parse_layer1, i)

    def parse_layer3(i):
        return parse_right_infix("\\/", Or, parse_layer2, i)

    def parse_layer4(i):
        return parse_right_infix("==>", Imp, parse_layer3, i)

    return parse_right_infix("<=>", Iff, parse_layer4, inp)


# Printing

# ------------------------------------------------------------------------- #
# Helper to unwrap grouped quantifiers like 'forall x y z .'                 #
# ------------------------------------------------------------------------- #


def strip_quant(fm: Formula[T]) -> tuple[list[str], Formula[T]]:
    """Recursively extracts a sequence of contiguous matching quantifiers."""
    match fm:
        case Forall(x, inner):
            if isinstance(inner, Forall):
                xs, q = strip_quant(inner)
                return [x] + xs, q
            return [x], inner

        case Exists(x, inner):
            if isinstance(inner, Exists):
                xs, q = strip_quant(inner)
                return [x] + xs, q
            return [x], inner

        case _:
            return [], fm


# ------------------------------------------------------------------------- #
# Idiomatic Stringifier Functions (Replacing Imperative Side-Effect Printers) #
# ------------------------------------------------------------------------- #


def format_formula(
    afn_printer: Callable[[int, T], str], pr: int, fm: Formula[T]
) -> str:
    """Recursively converts a formula to a string using operator precedence."""

    # Simple formatting helper that conditionally adds brackets
    def bracket(condition: bool, content: str) -> str:
        return f"({content})" if condition else content

    match fm:
        case _False():
            return "false"

        case _True():
            return "true"

        case Atom(value):
            return afn_printer(pr, value)

        case Not(p):
            # OCaml uses print_prefix (newpr+1) -> 10 + 1 = 11
            inner = format_formula(afn_printer, 11, p)
            return bracket(pr > 10, f"~{inner}")

        case And(p, q):
            # Right-associative infix: left child gets newpr+1, right child gets newpr
            left = format_formula(afn_printer, 9, p)
            right = format_formula(afn_printer, 8, q)
            return bracket(pr > 8, f"{left} /\\ {right}")

        case Or(p, q):
            left = format_formula(afn_printer, 7, p)
            right = format_formula(afn_printer, 6, q)
            return bracket(pr > 6, f"{left} \\/ {right}")

        case Imp(p, q):
            left = format_formula(afn_printer, 5, p)
            right = format_formula(afn_printer, 4, q)
            return bracket(pr > 4, f"{left} ==> {right}")

        case Iff(p, q):
            left = format_formula(afn_printer, 3, p)
            right = format_formula(afn_printer, 2, q)
            return bracket(pr > 2, f"{left} <=> {right}")

        case Forall(_) | Exists(_):
            qname = "forall" if isinstance(fm, Forall) else "exists"
            bvs, body = strip_quant(fm)

            variables_str = " ".join(bvs)
            body_str = format_formula(afn_printer, 0, body)

            return bracket(pr > 0, f"{qname} {variables_str}. {body_str}")

        case _:
            raise TypeError(f"Unknown formula instance type {fm}")


def print_qformula(afn_printer: Callable[[int, T], str], fm: Formula[T]) -> None:
    """The final interface function matching 'print_qformula pfn fm'."""
    formula_str = format_formula(afn_printer, 0, fm)
    print(f"<<{formula_str}>>")
