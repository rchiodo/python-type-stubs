from typing import Any, Callable
from sympy.core import Add, Mul, Number, NumberSymbol, Pow
from sympy.core.logic import And, Or
from sympy.core.numbers import ImaginaryUnit
from sympy.functions.elementary.complexes import Abs
from sympy.logic.boolalg import Implies
from sympy.matrices.expressions import MatMul

def allargs(symbol, fact, expr) -> And:
    """
    Apply all arguments of the expression to the fact structure.

    Parameters
    ==========

    symbol : Symbol
        A placeholder symbol.

    fact : Boolean
        Resulting ``Boolean`` expression.

    expr : Expr

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.sathandlers import allargs
    >>> from sympy.abc import x, y
    >>> allargs(x, Q.negative(x) | Q.positive(x), x*y)
    (Q.negative(x) | Q.positive(x)) & (Q.negative(y) | Q.positive(y))

    """
    ...

def anyarg(symbol, fact, expr) -> Or:
    """
    Apply any argument of the expression to the fact structure.

    Parameters
    ==========

    symbol : Symbol
        A placeholder symbol.

    fact : Boolean
        Resulting ``Boolean`` expression.

    expr : Expr

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.sathandlers import anyarg
    >>> from sympy.abc import x, y
    >>> anyarg(x, Q.negative(x) & Q.positive(x), x*y)
    (Q.negative(x) & Q.positive(x)) | (Q.negative(y) & Q.positive(y))

    """
    ...

def exactlyonearg(symbol, fact, expr) -> Or:
    """
    Apply exactly one argument of the expression to the fact structure.

    Parameters
    ==========

    symbol : Symbol
        A placeholder symbol.

    fact : Boolean
        Resulting ``Boolean`` expression.

    expr : Expr

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.sathandlers import exactlyonearg
    >>> from sympy.abc import x, y
    >>> exactlyonearg(x, Q.positive(x), x*y)
    (Q.positive(x) & ~Q.positive(y)) | (Q.positive(y) & ~Q.positive(x))

    """
    ...

class ClassFactRegistry:
    """
    Register handlers against classes.

    Explanation
    ===========

    ``register`` method registers the handler function for a class. Here,
    handler function should return a single fact. ``multiregister`` method
    registers the handler function for multiple classes. Here, handler function
    should return a container of multiple facts.

    ``registry(expr)`` returns a set of facts for *expr*.

    Examples
    ========

    Here, we register the facts for ``Abs``.

    >>> from sympy import Abs, Equivalent, Q
    >>> from sympy.assumptions.sathandlers import ClassFactRegistry
    >>> reg = ClassFactRegistry()
    >>> @reg.register(Abs)
    ... def f1(expr):
    ...     return Q.nonnegative(expr)
    >>> @reg.register(Abs)
    ... def f2(expr):
    ...     arg = expr.args[0]
    ...     return Equivalent(~Q.zero(arg), ~Q.zero(expr))

    Calling the registry with expression returns the defined facts for the
    expression.

    >>> from sympy.abc import x
    >>> reg(Abs(x))
    {Q.nonnegative(Abs(x)), Equivalent(~Q.zero(x), ~Q.zero(Abs(x)))}

    Multiple facts can be registered at once by ``multiregister`` method.

    >>> reg2 = ClassFactRegistry()
    >>> @reg2.multiregister(Abs)
    ... def _(expr):
    ...     arg = expr.args[0]
    ...     return [Q.even(arg) >> Q.even(expr), Q.odd(arg) >> Q.odd(expr)]
    >>> reg2(Abs(x))
    {Implies(Q.even(x), Q.even(Abs(x))), Implies(Q.odd(x), Q.odd(Abs(x)))}

    """
    def __init__(self) -> None:
        ...
    
    def register(self, cls) -> Callable[..., Any]:
        ...
    
    def multiregister(self, *classes) -> Callable[..., Any]:
        ...
    
    def __getitem__(self, key) -> tuple[frozenset[Any], frozenset[Any]]:
        ...
    
    def __call__(self, expr) -> set[Any]:
        ...
    


class_fact_registry = ...
x = ...
@class_fact_registry.multiregister(Abs)
def _(expr) -> list[Any]:
    ...

@class_fact_registry.multiregister(Add)
def _(expr) -> list[Any]:
    ...

@class_fact_registry.register(Add)
def _(expr) -> Implies:
    ...

@class_fact_registry.multiregister(Mul)
def _(expr) -> list[Any]:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(Mul)
def _(expr) -> Implies:
    ...

@class_fact_registry.register(MatMul)
def _(expr) -> Implies:
    ...

@class_fact_registry.multiregister(Pow)
def _(expr) -> list[Any]:
    ...

_old_assump_getters = ...
@class_fact_registry.multiregister(Number, NumberSymbol, ImaginaryUnit)
def _(expr) -> list[Any]:
    ...

