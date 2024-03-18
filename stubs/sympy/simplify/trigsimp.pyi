from typing import Any
from sympy.core.basic import Basic
from sympy.series.order import Order


def trigsimp_groebner(expr, hints=..., quick=..., order=..., polynomial=...) -> Order | Any:
    """
    Simplify trigonometric expressions using a groebner basis algorithm.

    Explanation
    ===========

    This routine takes a fraction involving trigonometric or hyperbolic
    expressions, and tries to simplify it. The primary metric is the
    total degree. Some attempts are made to choose the simplest possible
    expression of the minimal degree, but this is non-rigorous, and also
    very slow (see the ``quick=True`` option).

    If ``polynomial`` is set to True, instead of simplifying numerator and
    denominator together, this function just brings numerator and denominator
    into a canonical form. This is much faster, but has potentially worse
    results. However, if the input is a polynomial, then the result is
    guaranteed to be an equivalent polynomial of minimal degree.

    The most important option is hints. Its entries can be any of the
    following:

    - a natural number
    - a function
    - an iterable of the form (func, var1, var2, ...)
    - anything else, interpreted as a generator

    A number is used to indicate that the search space should be increased.
    A function is used to indicate that said function is likely to occur in a
    simplified expression.
    An iterable is used indicate that func(var1 + var2 + ...) is likely to
    occur in a simplified .
    An additional generator also indicates that it is likely to occur.
    (See examples below).

    This routine carries out various computationally intensive algorithms.
    The option ``quick=True`` can be used to suppress one particularly slow
    step (at the expense of potentially more complicated results, but never at
    the expense of increased total degree).

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy import sin, tan, cos, sinh, cosh, tanh
    >>> from sympy.simplify.trigsimp import trigsimp_groebner

    Suppose you want to simplify ``sin(x)*cos(x)``. Naively, nothing happens:

    >>> ex = sin(x)*cos(x)
    >>> trigsimp_groebner(ex)
    sin(x)*cos(x)

    This is because ``trigsimp_groebner`` only looks for a simplification
    involving just ``sin(x)`` and ``cos(x)``. You can tell it to also try
    ``2*x`` by passing ``hints=[2]``:

    >>> trigsimp_groebner(ex, hints=[2])
    sin(2*x)/2
    >>> trigsimp_groebner(sin(x)**2 - cos(x)**2, hints=[2])
    -cos(2*x)

    Increasing the search space this way can quickly become expensive. A much
    faster way is to give a specific expression that is likely to occur:

    >>> trigsimp_groebner(ex, hints=[sin(2*x)])
    sin(2*x)/2

    Hyperbolic expressions are similarly supported:

    >>> trigsimp_groebner(sinh(2*x)/sinh(x))
    2*cosh(x)

    Note how no hints had to be passed, since the expression already involved
    ``2*x``.

    The tangent function is also supported. You can either pass ``tan`` in the
    hints, to indicate that tan should be tried whenever cosine or sine are,
    or you can pass a specific generator:

    >>> trigsimp_groebner(sin(x)/cos(x), hints=[tan])
    tan(x)
    >>> trigsimp_groebner(sinh(x)/cosh(x), hints=[tanh(x)])
    tanh(x)

    Finally, you can use the iterable form to suggest that angle sum formulae
    should be tried:

    >>> ex = (tan(x) + tan(y))/(1 - tan(x)*tan(y))
    >>> trigsimp_groebner(ex, hints=[(tan, x, y)])
    tan(x + y)
    """
    ...

_trigs = ...
def trigsimp(expr, inverse=..., **opts) -> Any:
    """Returns a reduced expression by using known trig identities.

    Parameters
    ==========

    inverse : bool, optional
        If ``inverse=True``, it will be assumed that a composition of inverse
        functions, such as sin and asin, can be cancelled in any order.
        For example, ``asin(sin(x))`` will yield ``x`` without checking whether
        x belongs to the set where this relation is true. The default is False.
        Default : True

    method : string, optional
        Specifies the method to use. Valid choices are:

        - ``'matching'``, default
        - ``'groebner'``
        - ``'combined'``
        - ``'fu'``
        - ``'old'``

        If ``'matching'``, simplify the expression recursively by targeting
        common patterns. If ``'groebner'``, apply an experimental groebner
        basis algorithm. In this case further options are forwarded to
        ``trigsimp_groebner``, please refer to
        its docstring. If ``'combined'``, it first runs the groebner basis
        algorithm with small default parameters, then runs the ``'matching'``
        algorithm. If ``'fu'``, run the collection of trigonometric
        transformations described by Fu, et al. (see the
        :py:func:`~sympy.simplify.fu.fu` docstring). If ``'old'``, the original
        SymPy trig simplification function is run.
    opts :
        Optional keyword arguments passed to the method. See each method's
        function docstring for details.

    Examples
    ========

    >>> from sympy import trigsimp, sin, cos, log
    >>> from sympy.abc import x
    >>> e = 2*sin(x)**2 + 2*cos(x)**2
    >>> trigsimp(e)
    2

    Simplification occurs wherever trigonometric functions are located.

    >>> trigsimp(log(e))
    log(2)

    Using ``method='groebner'`` (or ``method='combined'``) might lead to
    greater simplification.

    The old trigsimp routine can be accessed as with method ``method='old'``.

    >>> from sympy import coth, tanh
    >>> t = 3*tanh(x)**7 - 2/coth(x)**7
    >>> trigsimp(t, method='old') == t
    True
    >>> trigsimp(t)
    tanh(x)**7

    """
    ...

def exptrigsimp(expr) -> Order:
    """
    Simplifies exponential / trigonometric / hyperbolic functions.

    Examples
    ========

    >>> from sympy import exptrigsimp, exp, cosh, sinh
    >>> from sympy.abc import z

    >>> exptrigsimp(exp(z) + exp(-z))
    2*cosh(z)
    >>> exptrigsimp(cosh(z) - sinh(z))
    exp(-z)
    """
    ...

def trigsimp_old(expr, *, first=..., **opts):
    """
    Reduces expression by using known trig identities.

    Notes
    =====

    deep:
    - Apply trigsimp inside all objects with arguments

    recursive:
    - Use common subexpression elimination (cse()) and apply
    trigsimp recursively (this is quite expensive if the
    expression is large)

    method:
    - Determine the method to use. Valid choices are 'matching' (default),
    'groebner', 'combined', 'fu' and 'futrig'. If 'matching', simplify the
    expression recursively by pattern matching. If 'groebner', apply an
    experimental groebner basis algorithm. In this case further options
    are forwarded to ``trigsimp_groebner``, please refer to its docstring.
    If 'combined', first run the groebner basis algorithm with small
    default parameters, then run the 'matching' algorithm. 'fu' runs the
    collection of trigonometric transformations described by Fu, et al.
    (see the `fu` docstring) while `futrig` runs a subset of Fu-transforms
    that mimic the behavior of `trigsimp`.

    compare:
    - show input and output from `trigsimp` and `futrig` when different,
    but returns the `trigsimp` value.

    Examples
    ========

    >>> from sympy import trigsimp, sin, cos, log, cot
    >>> from sympy.abc import x
    >>> e = 2*sin(x)**2 + 2*cos(x)**2
    >>> trigsimp(e, old=True)
    2
    >>> trigsimp(log(e), old=True)
    log(2*sin(x)**2 + 2*cos(x)**2)
    >>> trigsimp(log(e), deep=True, old=True)
    log(2)

    Using `method="groebner"` (or `"combined"`) can sometimes lead to a lot
    more simplification:

    >>> e = (-sin(x) + 1)/cos(x) + cos(x)/(-sin(x) + 1)
    >>> trigsimp(e, old=True)
    (1 - sin(x))/cos(x) + cos(x)/(1 - sin(x))
    >>> trigsimp(e, method="groebner", old=True)
    2/cos(x)

    >>> trigsimp(1/cot(x)**2, compare=True, old=True)
          futrig: tan(x)**2
    cot(x)**(-2)

    """
    ...

_trigpat = ...
_idn = ...
_midn = ...
_one = ...
def futrig(e, *, hyper=..., **kwargs) -> Basic | Order:
    """Return simplified ``e`` using Fu-like transformations.
    This is not the "Fu" algorithm. This is called by default
    from ``trigsimp``. By default, hyperbolics subexpressions
    will be simplified, but this can be disabled by setting
    ``hyper=False``.

    Examples
    ========

    >>> from sympy import trigsimp, tan, sinh, tanh
    >>> from sympy.simplify.trigsimp import futrig
    >>> from sympy.abc import x
    >>> trigsimp(1/tan(x)**2)
    tan(x)**(-2)

    >>> futrig(sinh(x)/tanh(x))
    cosh(x)

    """
    ...

