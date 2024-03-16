from typing import Callable, Self
from sympy.core.basic import Basic

"""
Functions and wrapper object to call assumption property and predicate
query with same syntax.

In SymPy, there are two assumption systems. Old assumption system is
defined in sympy/core/assumptions, and it can be accessed by attribute
such as ``x.is_even``. New assumption system is defined in
sympy/assumptions, and it can be accessed by predicates such as
``Q.even(x)``.

Old assumption is fast, while new assumptions can freely take local facts.
In general, old assumption is used in evaluation method and new assumption
is used in refinement method.

In most cases, both evaluation and refinement follow the same process, and
the only difference is which assumption system is used. This module provides
``is_[...]()`` functions and ``AssumptionsWrapper()`` class which allows
using two systems with same syntax so that parallel code implementation can be
avoided.

Examples
========

For multiple use, use ``AssumptionsWrapper()``.

>>> from sympy import Q, Symbol
>>> from sympy.assumptions.wrapper import AssumptionsWrapper
>>> x = Symbol('x')
>>> _x = AssumptionsWrapper(x, Q.even(x))
>>> _x.is_integer
True
>>> _x.is_odd
False

For single use, use ``is_[...]()`` functions.

>>> from sympy.assumptions.wrapper import is_infinite
>>> a = Symbol('a')
>>> print(is_infinite(a))
None
>>> is_infinite(a, Q.finite(a))
False

"""
def make_eval_method(fact) -> Callable[..., bool | None]:
    ...

class AssumptionsWrapper(Basic):
    """
    Wrapper over ``Basic`` instances to call predicate query by
    ``.is_[...]`` property

    Parameters
    ==========

    expr : Basic

    assumptions : Boolean, optional

    Examples
    ========

    >>> from sympy import Q, Symbol
    >>> from sympy.assumptions.wrapper import AssumptionsWrapper
    >>> x = Symbol('x', even=True)
    >>> AssumptionsWrapper(x).is_integer
    True
    >>> y = Symbol('y')
    >>> AssumptionsWrapper(y, Q.even(y)).is_integer
    True

    With ``AssumptionsWrapper``, both evaluation and refinement can be supported
    by single implementation.

    >>> from sympy import Function
    >>> class MyAbs(Function):
    ...     @classmethod
    ...     def eval(cls, x, assumptions=True):
    ...         _x = AssumptionsWrapper(x, assumptions)
    ...         if _x.is_nonnegative:
    ...             return x
    ...         if _x.is_negative:
    ...             return -x
    ...     def _eval_refine(self, assumptions):
    ...         return MyAbs.eval(self.args[0], assumptions)
    >>> MyAbs(x)
    MyAbs(x)
    >>> MyAbs(x).refine(Q.positive(x))
    x
    >>> MyAbs(Symbol('y', negative=True))
    -y

    """
    def __new__(cls, expr, assumptions=...) -> Self:
        ...
    
    _eval_is_algebraic = ...
    _eval_is_antihermitian = ...
    _eval_is_commutative = ...
    _eval_is_complex = ...
    _eval_is_composite = ...
    _eval_is_even = ...
    _eval_is_extended_negative = ...
    _eval_is_extended_nonnegative = ...
    _eval_is_extended_nonpositive = ...
    _eval_is_extended_nonzero = ...
    _eval_is_extended_positive = ...
    _eval_is_extended_real = ...
    _eval_is_finite = ...
    _eval_is_hermitian = ...
    _eval_is_imaginary = ...
    _eval_is_infinite = ...
    _eval_is_integer = ...
    _eval_is_irrational = ...
    _eval_is_negative = ...
    _eval_is_noninteger = ...
    _eval_is_nonnegative = ...
    _eval_is_nonpositive = ...
    _eval_is_nonzero = ...
    _eval_is_odd = ...
    _eval_is_polar = ...
    _eval_is_positive = ...
    _eval_is_prime = ...
    _eval_is_rational = ...
    _eval_is_real = ...
    _eval_is_transcendental = ...
    _eval_is_zero = ...


def is_infinite(obj, assumptions=...) -> bool | None:
    ...

def is_extended_real(obj, assumptions=...) -> bool | None:
    ...

def is_extended_nonnegative(obj, assumptions=...) -> bool | None:
    ...

