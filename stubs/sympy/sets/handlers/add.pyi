from sympy.core.numbers import Infinity, NegativeInfinity
from sympy.core import Basic, Expr
from sympy.sets import Interval

_set_add = ...
_set_sub = ...
@_set_add.register(Basic, Basic)
def _(x, y) -> None:
    ...

@_set_add.register(Expr, Expr)
def _(x, y):
    ...

@_set_add.register(Interval, Interval)
def _(x, y) -> FiniteSet | Interval:
    """
    Additions in interval arithmetic
    https://en.wikipedia.org/wiki/Interval_arithmetic
    """
    ...

@_set_add.register(Interval, Infinity)
def _(x, y) -> FiniteSet | Interval:
    ...

@_set_add.register(Interval, NegativeInfinity)
def _(x, y) -> FiniteSet | Interval:
    ...

@_set_sub.register(Basic, Basic)
def _(x, y) -> None:
    ...

@_set_sub.register(Expr, Expr)
def _(x, y):
    ...

@_set_sub.register(Interval, Interval)
def _(x, y) -> FiniteSet | Interval:
    """
    Subtractions in interval arithmetic
    https://en.wikipedia.org/wiki/Interval_arithmetic
    """
    ...

@_set_sub.register(Interval, Infinity)
def _(x, y) -> FiniteSet | Interval:
    ...

@_set_sub.register(Interval, NegativeInfinity)
def _(x, y) -> FiniteSet | Interval:
    ...

