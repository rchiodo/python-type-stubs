from typing import Literal
from sympy.core import Add, Basic, Expr, Float, Mul, Pow
from sympy.core.numbers import ImaginaryUnit, Infinity, Integer, NaN, NegativeInfinity, NumberSymbol, Rational
from sympy.functions import Abs, im, re
from sympy.assumptions.predicates.ntheory import CompositePredicate, EvenPredicate, OddPredicate, PrimePredicate

"""
Handlers for keys related to number theory: prime, even, odd, etc.
"""
@PrimePredicate.register(Expr)
def _(expr, assumptions):
    ...

@PrimePredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@PrimePredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@PrimePredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    """
    Integer**Integer     -> !Prime
    """
    ...

@PrimePredicate.register(Integer)
def _(expr, assumptions) -> bool:
    ...

@PrimePredicate.register_many(Rational, Infinity, NegativeInfinity, ImaginaryUnit)
def _(expr, assumptions) -> Literal[False]:
    ...

@PrimePredicate.register(Float)
def _(expr, assumptions) -> bool | None:
    ...

@PrimePredicate.register(NumberSymbol)
def _(expr, assumptions) -> bool | None:
    ...

@PrimePredicate.register(NaN)
def _(expr, assumptions) -> None:
    ...

@CompositePredicate.register(Expr)
def _(expr, assumptions):
    ...

@CompositePredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@EvenPredicate.register(Expr)
def _(expr, assumptions):
    ...

@EvenPredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@EvenPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    """
    Even * Integer    -> Even
    Even * Odd        -> Even
    Integer * Odd     -> ?
    Odd * Odd         -> Odd
    Even * Even       -> Even
    Integer * Integer -> Even if Integer + Integer = Odd
    otherwise         -> ?
    """
    ...

@EvenPredicate.register(Add)
def _(expr, assumptions) -> bool | None:
    """
    Even + Odd  -> Odd
    Even + Even -> Even
    Odd  + Odd  -> Even

    """
    ...

@EvenPredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@EvenPredicate.register(Integer)
def _(expr, assumptions) -> bool:
    ...

@EvenPredicate.register_many(Rational, Infinity, NegativeInfinity, ImaginaryUnit)
def _(expr, assumptions) -> Literal[False]:
    ...

@EvenPredicate.register(NumberSymbol)
def _(expr, assumptions) -> bool | None:
    ...

@EvenPredicate.register(Abs)
def _(expr, assumptions) -> bool | None:
    ...

@EvenPredicate.register(re)
def _(expr, assumptions) -> bool | None:
    ...

@EvenPredicate.register(im)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@EvenPredicate.register(NaN)
def _(expr, assumptions) -> None:
    ...

@OddPredicate.register(Expr)
def _(expr, assumptions):
    ...

@OddPredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

