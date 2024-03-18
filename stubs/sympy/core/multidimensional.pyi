"""
Provides functionality for multidimensional usage of scalar-functions.

Read the vectorize docstring for more details.
"""
from functools import _Wrapped
from typing import Any, Callable


def apply_on_element(f, args, kwargs, n) -> list[list[Any] | Any]:
    """
    Returns a structure with the same dimension as the specified argument,
    where each basic element is replaced by the function f applied on it. All
    other arguments stay the same.
    """
    ...

def iter_copy(structure) -> list[Any]:
    """
    Returns a copy of an iterable object (also copying all embedded iterables).
    """
    ...

def structure_copy(structure) -> list[Any]:
    """
    Returns a copy of the given structure (numpy-array, list, iterable, ..).
    """
    ...

class vectorize:
    """
    Generalizes a function taking scalars to accept multidimensional arguments.

    Examples
    ========

    >>> from sympy import vectorize, diff, sin, symbols, Function
    >>> x, y, z = symbols('x y z')
    >>> f, g, h = list(map(Function, 'fgh'))

    >>> @vectorize(0)
    ... def vsin(x):
    ...     return sin(x)

    >>> vsin([1, x, y])
    [sin(1), sin(x), sin(y)]

    >>> @vectorize(0, 1)
    ... def vdiff(f, y):
    ...     return diff(f, y)

    >>> vdiff([f(x, y, z), g(x, y, z), h(x, y, z)], [x, y, z])
    [[Derivative(f(x, y, z), x), Derivative(f(x, y, z), y), Derivative(f(x, y, z), z)], [Derivative(g(x, y, z), x), Derivative(g(x, y, z), y), Derivative(g(x, y, z), z)], [Derivative(h(x, y, z), x), Derivative(h(x, y, z), y), Derivative(h(x, y, z), z)]]
    """
    def __init__(self, *mdargs) -> None:
        ...

    def __call__(self, f: Any) -> _Wrapped[..., Any, ..., list[list[Any] | Any] | Any]:
        """
        Returns a wrapper for the one-dimensional function that can handle
        multidimensional arguments.
        """
        ...
    


