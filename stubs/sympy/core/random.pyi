"""
When you need to use random numbers in SymPy library code, import from here
so there is only one generator working for SymPy. Imports from here should
behave the same as if they were being imported from Python's random module.
But only the routines currently used in SymPy are included here. To use others
import ``rng`` and access the method directly. For example, to capture the
current state of the generator use ``rng.getstate()``.

There is intentionally no Random to import from here. If you want
to control the state of the generator, import ``seed`` and call it
with or without an argument to set the state.

Examples
========

>>> from sympy.core.random import random, seed
>>> assert random() < 1
>>> seed(1); a = random()
>>> b = random()
>>> seed(1); c = random()
>>> assert a == c
>>> assert a != b  # remote possibility this will fail

"""
rng = ...
choice = ...
random = ...
randint = ...
randrange = ...
sample = ...
shuffle = ...
uniform = ...
_assumptions_rng = ...
_assumptions_shuffle = ...
def seed(a=..., version=...) -> None:
    ...

def random_complex_number(a=..., b=..., c=..., d=..., rational=..., tolerance=...):
    """
    Return a random complex number.

    To reduce chance of hitting branch cuts or anything, we guarantee
    b <= Im z <= d, a <= Re z <= c

    When rational is True, a rational approximation to a random number
    is obtained within specified tolerance, if any.
    """
    ...

def verify_numerically(f, g, z=..., tol=..., a=..., b=..., c=..., d=...) -> bool:
    """
    Test numerically that f and g agree when evaluated in the argument z.

    If z is None, all symbols will be tested. This routine does not test
    whether there are Floats present with precision higher than 15 digits
    so if there are, your results may not be what you expect due to round-
    off errors.

    Examples
    ========

    >>> from sympy import sin, cos
    >>> from sympy.abc import x
    >>> from sympy.core.random import verify_numerically as tn
    >>> tn(sin(x)**2 + cos(x)**2, 1, x)
    True
    """
    ...

def test_derivative_numerically(f, z, tol=..., a=..., b=..., c=..., d=...) -> bool:
    """
    Test numerically that the symbolically computed derivative of f
    with respect to z is correct.

    This routine does not test whether there are Floats present with
    precision higher than 15 digits so if there are, your results may
    not be what you expect due to round-off errors.

    Examples
    ========

    >>> from sympy import sin
    >>> from sympy.abc import x
    >>> from sympy.core.random import test_derivative_numerically as td
    >>> td(sin(x), x)
    True
    """
    ...

