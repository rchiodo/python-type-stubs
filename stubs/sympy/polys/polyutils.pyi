from types import NotImplementedType
from typing import Any, Self
from sympy.external.gmpy import GROUND_TYPES
from sympy.series.order import Order

"""Useful utilities for higher level polynomial classes. """
_gens_order = ...
_max_order = ...
_re_gen = ...
illegal_types = ...
finf = ...
def parallel_dict_from_expr(exprs, **args) -> tuple[list[Any], Any]:
    """Transform expressions into a multinomial form. """
    ...

def dict_from_expr(expr, **args) -> tuple[Any, Any]:
    """Transform an expression into a multinomial form. """
    ...

def expr_from_dict(rep, *gens) -> Order:
    """Convert a multinomial form into an expression. """
    ...

parallel_dict_from_basic = ...
dict_from_basic = ...
basic_from_dict = ...
class PicklableWithSlots:
    """
    Mixin class that allows to pickle objects with ``__slots__``.

    Examples
    ========

    First define a class that mixes :class:`PicklableWithSlots` in::

        >>> from sympy.polys.polyutils import PicklableWithSlots
        >>> class Some(PicklableWithSlots):
        ...     __slots__ = ('foo', 'bar')
        ...
        ...     def __init__(self, foo, bar):
        ...         self.foo = foo
        ...         self.bar = bar

    To make :mod:`pickle` happy in doctest we have to use these hacks::

        >>> import builtins
        >>> builtins.Some = Some
        >>> from sympy.polys import polyutils
        >>> polyutils.Some = Some

    Next lets see if we can create an instance, pickle it and unpickle::

        >>> some = Some('abc', 10)
        >>> some.foo, some.bar
        ('abc', 10)

        >>> from pickle import dumps, loads
        >>> some2 = loads(dumps(some))

        >>> some2.foo, some2.bar
        ('abc', 10)

    """
    __slots__ = ...
    def __getstate__(self, cls=...) -> dict[Any, Any]:
        ...
    
    def __setstate__(self, d) -> None:
        ...
    


class IntegerPowerable:
    r"""
    Mixin class for classes that define a `__mul__` method, and want to be
    raised to integer powers in the natural way that follows. Implements
    powering via binary expansion, for efficiency.

    By default, only integer powers $\geq 2$ are supported. To support the
    first, zeroth, or negative powers, override the corresponding methods,
    `_first_power`, `_zeroth_power`, `_negative_power`, below.
    """
    def __pow__(self, e, modulo=...) -> NotImplementedType | Self:
        ...
    


_GF_types: tuple[type, ...]
if GROUND_TYPES == 'flint':
    _GF_types = ...
else:
    flint = ...
    _GF_types = ...
