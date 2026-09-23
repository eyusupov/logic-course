from abc import ABC, abstractmethod
from dataclasses import dataclass


# 1. Define the Visitor Interface
class ExpressionVisitor(ABC):
    @abstractmethod
    def visit_var(self, expr: "Var"):
        pass

    @abstractmethod
    def visit_const(self, expr: "Const"):
        pass

    @abstractmethod
    def visit_add(self, expr: "Add"):
        pass

    @abstractmethod
    def visit_mul(self, expr: "Mul"):
        pass


# 2. Define the AST Nodes with an 'accept' method
class Expression(ABC):
    @abstractmethod
    def accept(self, visitor: ExpressionVisitor):
        pass


@dataclass(frozen=True)
class Var(Expression):
    name: str

    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_var(self)


@dataclass(frozen=True)
class Const(Expression):
    value: int

    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_const(self)


@dataclass(frozen=True)
class Add(Expression):
    left: Expression
    right: Expression

    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_add(self)


@dataclass(frozen=True)
class Mul(Expression):
    left: Expression
    right: Expression

    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_mul(self)


class Simplify1Visitor(ExpressionVisitor):
    def visit_var(self, expr: Var) -> Expression:
        return expr

    def visit_const(self, expr: Const) -> Expression:
        return expr

    def visit_add(self, expr: Add) -> Expression:
        left, right = expr.left, expr.right

        # Constant folding: Add(Const, Const)
        if isinstance(left, Const) and isinstance(right, Const):
            return Const(left.value + right.value)
        # Additive identity: Add(Const(0), x)
        if isinstance(left, Const) and left.value == 0:
            return right
        # Additive identity: Add(x, Const(0))
        if isinstance(right, Const) and right.value == 0:
            return left

        return expr

    def visit_mul(self, expr: Mul) -> Expression:
        left, right = expr.left, expr.right

        # Constant folding: Mul(Const, Const)
        if isinstance(left, Const) and isinstance(right, Const):
            return Const(left.value * right.value)
        # Multiplicative null: Mul(0, x) or Mul(x, 0)
        if (isinstance(left, Const) and left.value == 0) or (
            isinstance(right, Const) and right.value == 0
        ):
            return Const(0)
        # Multiplicative identity: Mul(1, x)
        if isinstance(left, Const) and left.value == 1:
            return right
        # Multiplicative identity: Mul(x, 1)
        if isinstance(right, Const) and right.value == 1:
            return left

        return expr


# Helper function to match the OCaml API
def simplify1(expr: Expression) -> Expression:
    return expr.accept(Simplify1Visitor())


class SimplifyVisitor(ExpressionVisitor):
    def visit_var(self, expr: Var) -> Expression:
        return simplify1(expr)

    def visit_const(self, expr: Const) -> Expression:
        return simplify1(expr)

    def visit_add(self, expr: Add) -> Expression:
        # Recursively simplify children first
        simplified_left = expr.left.accept(self)
        simplified_right = expr.right.accept(self)
        # Apply shallow simplification to the new node
        return simplify1(Add(simplified_left, simplified_right))

    def visit_mul(self, expr: Mul) -> Expression:
        # Recursively simplify children first
        simplified_left = expr.left.accept(self)
        simplified_right = expr.right.accept(self)
        # Apply shallow simplification to the new node
        return simplify1(Mul(simplified_left, simplified_right))


# Helper function to match the OCaml API
def simplify(expr: Expression) -> Expression:
    return expr.accept(SimplifyVisitor())
