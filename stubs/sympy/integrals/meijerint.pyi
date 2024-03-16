from sympy.core.symbol import Dummy

"""
Integrate functions by rewriting them as Meijer G-functions.

There are three user-visible functions that can be used by other parts of the
sympy library to solve various integration problems:

- meijerint_indefinite
- meijerint_definite
- meijerint_inversion

They can be used to compute, respectively, indefinite integrals, definite
integrals over intervals of the real line, and inverse laplace-type integrals
(from c-I*oo to c+I*oo). See the respective docstrings for details.

The main references for this are:

[L] Luke, Y. L. (1969), The Special Functions and Their Approximations,
    Volume 1

[R] Kelly B. Roach.  Meijer G Function Representations.
    In: Proceedings of the 1997 International Symposium on Symbolic and
    Algebraic Computation, pages 205-211, New York, 1997. ACM.

[P] A. P. Prudnikov, Yu. A. Brychkov and O. I. Marichev (1990).
    Integrals and Series: More Special Functions, Vol. 3,.
    Gordon and Breach Science Publisher
"""
z = ...
timeit = ...
class _CoeffExpValueError(ValueError):
    """
    Exception raised by _get_coeff_exp, for internal use only.
    """
    ...


_dummies: dict[tuple[str, str], Dummy] = ...
_lookup_table = ...
def meijerint_indefinite(f, x) -> Piecewise | Basic | None:
    """
    Compute an indefinite integral of ``f`` by rewriting it as a G function.

    Examples
    ========

    >>> from sympy.integrals.meijerint import meijerint_indefinite
    >>> from sympy import sin
    >>> from sympy.abc import x
    >>> meijerint_indefinite(sin(x), x)
    -cos(x)
    """
    ...

@timeit
def meijerint_definite(f, x, a, b):
    """
    Integrate ``f`` over the interval [``a``, ``b``], by rewriting it as a product
    of two G functions, or as a single G function.

    Return res, cond, where cond are convergence conditions.

    Examples
    ========

    >>> from sympy.integrals.meijerint import meijerint_definite
    >>> from sympy import exp, oo
    >>> from sympy.abc import x
    >>> meijerint_definite(exp(-x**2), x, -oo, oo)
    (sqrt(pi), True)

    This function is implemented as a succession of functions
    meijerint_definite, _meijerint_definite_2, _meijerint_definite_3,
    _meijerint_definite_4. Each function in the list calls the next one
    (presumably) several times. This means that calling meijerint_definite
    can be very costly.
    """
    ...

def meijerint_inversion(f, x, t) -> Piecewise | None:
    r"""
    Compute the inverse laplace transform
    $\int_{c+i\infty}^{c-i\infty} f(x) e^{tx}\, dx$,
    for real c larger than the real part of all singularities of ``f``.

    Note that ``t`` is always assumed real and positive.

    Return None if the integral does not exist or could not be evaluated.

    Examples
    ========

    >>> from sympy.abc import x, t
    >>> from sympy.integrals.meijerint import meijerint_inversion
    >>> meijerint_inversion(1/x, x, t)
    Heaviside(t)
    """
    ...

