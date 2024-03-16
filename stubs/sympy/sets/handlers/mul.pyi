from sympy.core import Basic, Expr
from sympy.sets.sets import Interval, Set

_set_mul = ...
_set_div = ...
@_set_mul.register(Basic, Basic)
def _(x, y) -> None:
    ...

@_set_mul.register(Set, Set)
def _(x, y) -> None:
    ...

@_set_mul.register(Expr, Expr)
def _(x, y):
    ...

@_set_mul.register(Interval, Interval)
def _(x, y) -> FiniteSet | Interval:
    """
    Multiplications in interval arithmetic
    https://en.wikipedia.org/wiki/Interval_arithmetic
    """
    ...

@_set_div.register(Basic, Basic)
def _(x, y) -> None:
    ...

@_set_div.register(Expr, Expr)
def _(x, y):
    ...

@_set_div.register(Set, Set)
def _(x, y) -> None:
    ...

@_set_div.register(Interval, Interval)
def _(x, y) -> FiniteSet | Interval | Any | ImageSet | Union:
    """
    Divisions in interval arithmetic
    https://en.wikipedia.org/wiki/Interval_arithmetic
    """
    ...

