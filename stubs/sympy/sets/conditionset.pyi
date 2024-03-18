from typing import Any, Self
from sympy.core.logic import And
from sympy.sets.sets import Complement, FiniteSet, Intersection, Set, Union

adummy = ...
class ConditionSet(Set):
    r"""
    Set of elements which satisfies a given condition.

    .. math:: \{x \mid \textrm{condition}(x) = \texttt{True}, x \in S\}

    Examples
    ========

    >>> from sympy import Symbol, S, ConditionSet, pi, Eq, sin, Interval
    >>> from sympy.abc import x, y, z

    >>> sin_sols = ConditionSet(x, Eq(sin(x), 0), Interval(0, 2*pi))
    >>> 2*pi in sin_sols
    True
    >>> pi/2 in sin_sols
    False
    >>> 3*pi in sin_sols
    False
    >>> 5 in ConditionSet(x, x**2 > 4, S.Reals)
    True

    If the value is not in the base set, the result is false:

    >>> 5 in ConditionSet(x, x**2 > 4, Interval(2, 4))
    False

    Notes
    =====

    Symbols with assumptions should be avoided or else the
    condition may evaluate without consideration of the set:

    >>> n = Symbol('n', negative=True)
    >>> cond = (n > 0); cond
    False
    >>> ConditionSet(n, cond, S.Integers)
    EmptySet

    Only free symbols can be changed by using `subs`:

    >>> c = ConditionSet(x, x < 1, {x, z})
    >>> c.subs(x, y)
    ConditionSet(x, x < 1, {y, z})

    To check if ``pi`` is in ``c`` use:

    >>> pi in c
    False

    If no base set is specified, the universal set is implied:

    >>> ConditionSet(x, x < 1).base_set
    UniversalSet

    Only symbols or symbol-like expressions can be used:

    >>> ConditionSet(x + 1, x + 1 < 1, S.Integers)
    Traceback (most recent call last):
    ...
    ValueError: non-symbol dummy not recognized in condition

    When the base set is a ConditionSet, the symbols will be
    unified if possible with preference for the outermost symbols:

    >>> ConditionSet(x, x < y, ConditionSet(z, z + y < 2, S.Integers))
    ConditionSet(x, (x < y) & (x + y < 2), Integers)

    """
    def __new__(cls, sym, condition, base_set=...) -> Set | FiniteSet | Intersection | Union | Complement | Self:
        ...
    
    sym = ...
    condition = ...
    base_set = ...
    @property
    def free_symbols(self) -> Any:
        ...
    
    @property
    def bound_symbols(self) -> list[Any]:
        ...
    
    def as_relational(self, other) -> And:
        ...
    


