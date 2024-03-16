from typing import Literal, Self
from sympy.assumptions import AppliedPredicate
from sympy.core import Basic, Symbol
from sympy.core.numbers import NaN, Number
from sympy.logic.boolalg import And, BooleanFalse, BooleanTrue, Equivalent, Implies, Not, Or
from sympy.assumptions.predicates.common import CommutativePredicate, IsTruePredicate

"""
This module defines base class for handlers and some core handlers:
``Q.commutative`` and ``Q.is_true``.
"""
class AskHandler:
    """Base class that all Ask Handlers must inherit."""
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    


class CommonHandler(AskHandler):
    """Defines some useful methods common to most Handlers. """
    @staticmethod
    def AlwaysTrue(expr, assumptions) -> Literal[True]:
        ...
    
    @staticmethod
    def AlwaysFalse(expr, assumptions) -> Literal[False]:
        ...
    
    @staticmethod
    def AlwaysNone(expr, assumptions) -> None:
        ...
    
    NaN = ...


@CommutativePredicate.register(Symbol)
def _(expr, assumptions) -> bool:
    """Objects are expected to be commutative unless otherwise stated"""
    ...

@CommutativePredicate.register(Basic)
def _(expr, assumptions) -> bool:
    ...

@CommutativePredicate.register(Number)
def _(expr, assumptions) -> Literal[True]:
    ...

@CommutativePredicate.register(NaN)
def _(expr, assumptions) -> Literal[True]:
    ...

@IsTruePredicate.register(bool)
def _(expr, assumptions):
    ...

@IsTruePredicate.register(BooleanTrue)
def _(expr, assumptions) -> Literal[True]:
    ...

@IsTruePredicate.register(BooleanFalse)
def _(expr, assumptions) -> Literal[False]:
    ...

@IsTruePredicate.register(AppliedPredicate)
def _(expr, assumptions) -> bool | None:
    ...

@IsTruePredicate.register(Not)
def _(expr, assumptions) -> bool | None:
    ...

@IsTruePredicate.register(Or)
def _(expr, assumptions) -> bool | None:
    ...

@IsTruePredicate.register(And)
def _(expr, assumptions) -> bool | None:
    ...

@IsTruePredicate.register(Implies)
def _(expr, assumptions) -> bool | None:
    ...

@IsTruePredicate.register(Equivalent)
def _(expr, assumptions) -> bool | None:
    ...

def test_closed_group(expr, assumptions, key) -> bool | None:
    """
    Test for membership in a group with respect
    to the current operation.
    """
    ...

