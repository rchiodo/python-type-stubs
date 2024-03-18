
from functools import _Wrapped
from types import FunctionType
from typing import Any, Callable


def threaded_factory(func, use_add) -> _Wrapped[..., Any, ..., Any]:
    ...

def threaded(func) -> _Wrapped[..., Any, ..., Any]:
    ...

def xthreaded(func) -> _Wrapped[..., Any, ..., Any]:
    ...

def conserve_mpmath_dps(func) -> Callable[..., Any]:
    ...

class no_attrs_in_subclass:
    def __init__(self, cls, f) -> None:
        ...
    
    def __get__(self, instance, owner=...) -> Any:
        ...
    


def doctest_depends_on(exe=..., modules=..., disable_viewers=..., python_version=..., ground_types=...) -> Callable[..., type[Any] | Any]:
    ...

def public(obj) -> FunctionType | type:
    ...

def memoize_property(propfunc) -> property:
    ...

def deprecated(message, *, deprecated_since_version, active_deprecations_target, stacklevel=...) -> Callable[..., type[Any] | _Wrapped[..., Any, ..., Any]]:
    '''
    Mark a function as deprecated.

    This decorator should be used if an entire function or class is
    deprecated. If only a certain functionality is deprecated, you should use
    :func:`~.warns_deprecated_sympy` directly. This decorator is just a
    convenience. There is no functional difference between using this
    decorator and calling ``warns_deprecated_sympy()`` at the top of the
    function.

    The decorator takes the same arguments as
    :func:`~.warns_deprecated_sympy`. See its
    documentation for details on what the keywords to this decorator do.

    See the :ref:`deprecation-policy` document for details on when and how
    things should be deprecated in SymPy.

    Examples
    ========

    >>> from sympy.utilities.decorator import deprecated
    >>> from sympy import simplify
    ... active_deprecations_target='simplify-this-deprecation')
    ... def simplify_this(expr):
    ...     return simplify(expr)
    >>> from sympy.abc import x
    >>> simplify_this(x*(x + 1) - x**2) # doctest: +SKIP
    <stdin>:1: SymPyDeprecationWarning:
    <BLANKLINE>
    The simplify_this(expr) function is deprecated. Use simplify(expr)
    instead.
    <BLANKLINE>
    See https://docs.sympy.org/latest/explanation/active-deprecations.html#simplify-this-deprecation
    for details.
    <BLANKLINE>
    This has been deprecated since SymPy version 1.1. It
    will be removed in a future version of SymPy.
    <BLANKLINE>
      simplify_this(x)
    x

    See Also
    ========
    sympy.utilities.exceptions.SymPyDeprecationWarning
    sympy.utilities.exceptions.sympy_deprecation_warning
    sympy.utilities.exceptions.ignore_warnings
    sympy.testing.pytest.warns_deprecated_sympy

    '''
    ...

