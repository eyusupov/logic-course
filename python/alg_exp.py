# Code from chapter 1.6

from abc import ABC
from dataclasses import dataclass


# Define the base class for the expression AST
class Expression(ABC):
    pass


@dataclass(frozen=True)
class Var(Expression):
    name: str


@dataclass(frozen=True)
class Const(Expression):
    value: int


@dataclass(frozen=True)
class Add(Expression):
    left: Expression
    right: Expression


@dataclass(frozen=True)
class Mul(Expression):
    left: Expression
    right: Expression


def simplify1(expr: Expression) -> Expression:
    match expr:
        # Constant folding
        case Add(Const(m), Const(n)):
            return Const(m + n)
        case Mul(Const(m), Const(n)):
            return Const(m * n)

        # Additive identity
        case Add(Const(0), x) | Add(x, Const(0)):
            return x

        # Multiplicative null element
        case Mul(Const(0), _) | Mul(_, Const(0)):
            return Const(0)

        # Multiplicative identity
        case Mul(Const(1), x) | Mul(x, Const(1)):
            return x

        # Fallback / No simplification possible
        case _:
            return expr


def simplify(expr: Expression) -> Expression:
    match expr:
        case Add(e1, e2):
            return simplify1(Add(simplify(e1), simplify(e2)))
        case Mul(e1, e2):
            return simplify1(Mul(simplify(e1), simplify(e2)))
        case _:
            return simplify1(expr)


print(Add(Mul(Const(2), Var("x")), Var("y")))

e = Add(Mul(Add(Mul(Const(0), Var("x")), Const(1)), Const(3)), Const(12))
print(simplify(e))
