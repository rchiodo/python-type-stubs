from sympy.sets.sets import EmptySet, Set
from sympy.core.function import FunctionClass, Lambda
from sympy.sets import FiniteSet, Intersection, Interval, Range, Union
from sympy.sets.fancysets import Integers, Naturals, Reals

FunctionUnion = ...
_set_function = ...
@_set_function.register(FunctionClass, Set)
def _(f, x) -> None:
    ...

@_set_function.register(FunctionUnion, FiniteSet)
def _(f, x) -> FiniteSet:
    ...

@_set_function.register(Lambda, Interval)
def _(f, x):
    ...

@_set_function.register(FunctionClass, Interval)
def _(f, x) -> FiniteSet | Interval | ImageSet:
    ...

@_set_function.register(FunctionUnion, Union)
def _(f, x) -> FiniteSet | Union:
    ...

@_set_function.register(FunctionUnion, Intersection)
def _(f, x) -> FiniteSet | Intersection | Union | Complement | ImageSet:
    ...

@_set_function.register(FunctionUnion, EmptySet)
def _(f, x):
    ...

@_set_function.register(FunctionUnion, Set)
def _(f, x) -> FiniteSet | ImageSet:
    ...

@_set_function.register(FunctionUnion, Range)
def _(f, self) -> FiniteSet | Basic | ImageSet | None:
    ...

@_set_function.register(FunctionUnion, Integers)
def _(f, self) -> FiniteSet | ImageSet | None:
    ...

@_set_function.register(FunctionUnion, Naturals)
def _(f, self) -> Range | None:
    ...

@_set_function.register(FunctionUnion, Reals)
def _(f, self) -> None:
    ...

