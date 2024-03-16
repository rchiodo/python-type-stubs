"""Useful utility decorators. """
def threaded_factory(func, use_add) -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """A factory for ``threaded`` decorators. """
    ...

def threaded(func) -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """Apply ``func`` to sub--elements of an object, including :class:`~.Add`.

    This decorator is intended to make it uniformly possible to apply a
    function to all elements of composite objects, e.g. matrices, lists, tuples
    and other iterable containers, or just expressions.

    This version of :func:`threaded` decorator allows threading over
    elements of :class:`~.Add` class. If this behavior is not desirable
    use :func:`xthreaded` decorator.

    Functions using this decorator must have the following signature::

      @threaded
      def function(expr, *args, **kwargs):

    """
    ...

def xthreaded(func) -> _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]:
    """Apply ``func`` to sub--elements of an object, excluding :class:`~.Add`.

    This decorator is intended to make it uniformly possible to apply a
    function to all elements of composite objects, e.g. matrices, lists, tuples
    and other iterable containers, or just expressions.

    This version of :func:`threaded` decorator disallows threading over
    elements of :class:`~.Add` class. If this behavior is not desirable
    use :func:`threaded` decorator.

    Functions using this decorator must have the following signature::

      @xthreaded
      def function(expr, *args, **kwargs):

    """
    ...

def conserve_mpmath_dps(func) -> Callable[..., Any]:
    """After the function finishes, resets the value of ``mpmath.mp.dps`` to
    the value it had before the function was run."""
    ...

class no_attrs_in_subclass:
    """Don't 'inherit' certain attributes from a base class

    >>> from sympy.utilities.decorator import no_attrs_in_subclass

    >>> class A(object):
    ...     x = 'test'

    >>> A.x = no_attrs_in_subclass(A, A.x)

    >>> class B(A):
    ...     pass

    >>> hasattr(A, 'x')
    True
    >>> hasattr(B, 'x')
    False

    """
    def __init__(self, cls, f) -> None:
        ...
    
    def __get__(self, instance, owner=...) -> Any:
        ...
    


def doctest_depends_on(exe=..., modules=..., disable_viewers=..., python_version=..., ground_types=...) -> Callable[..., type[Any] | Any]:
    """
    Adds metadata about the dependencies which need to be met for doctesting
    the docstrings of the decorated objects.

    ``exe`` should be a list of executables

    ``modules`` should be a list of modules

    ``disable_viewers`` should be a list of viewers for :func:`~sympy.printing.preview.preview` to disable

    ``python_version`` should be the minimum Python version required, as a tuple
    (like ``(3, 0)``)
    """
    ...

def public(obj) -> FunctionType | type:
    """
    Append ``obj``'s name to global ``__all__`` variable (call site).

    By using this decorator on functions or classes you achieve the same goal
    as by filling ``__all__`` variables manually, you just do not have to repeat
    yourself (object's name). You also know if object is public at definition
    site, not at some random location (where ``__all__`` was set).

    Note that in multiple decorator setup (in almost all cases) ``@public``
    decorator must be applied before any other decorators, because it relies
    on the pointer to object's global namespace. If you apply other decorators
    first, ``@public`` may end up modifying the wrong namespace.

    Examples
    ========

    >>> from sympy.utilities.decorator import public

    >>> __all__ # noqa: F821
    Traceback (most recent call last):
    ...
    NameError: name '__all__' is not defined

    >>> @public
    ... def some_function():
    ...     pass

    >>> __all__ # noqa: F821
    ['some_function']

    """
    ...

def memoize_property(propfunc) -> property:
    """Property decorator that caches the value of potentially expensive
    ``propfunc`` after the first evaluation. The cached value is stored in
    the corresponding property name with an attached underscore."""
    ...

def deprecated(message, *, deprecated_since_version, active_deprecations_target, stacklevel=...) -> Callable[..., type[wrapper] | _Wrapped[Callable[..., Any], Any, Callable[..., Any], Any]]:
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
    >>> @deprecated("""\
    ... The simplify_this(expr) function is deprecated. Use simplify(expr)
    ... instead.""", deprecated_since_version="1.1",
    ... active_deprecations_target='simplify-this-deprecation')
    ... def simplify_this(expr):
    ...     """
    ...     Simplify ``expr``.
    ...
    ...     .. deprecated:: 1.1
    ...
    ...        The ``simplify_this`` function is deprecated. Use :func:`simplify`
    ...        instead. See its documentation for more information. See
    ...        :ref:`simplify-this-deprecation` for details.
    ...
    ...     """
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

