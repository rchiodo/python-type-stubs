from typing import Any
from sympy.utilities import public

"""Efficient functions for generating orthogonal polynomials."""
def dup_jacobi(n, a, b, K) -> list[Any]:
    """Low-level implementation of Jacobi polynomials."""
    ...

@public
def jacobi_poly(n, a, b, x=..., polys=...):
    r"""Generates the Jacobi polynomial `P_n^{(a,b)}(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    a
        Lower limit of minimal domain for the list of coefficients.
    b
        Upper limit of minimal domain for the list of coefficients.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

def dup_gegenbauer(n, a, K) -> list[Any]:
    """Low-level implementation of Gegenbauer polynomials."""
    ...

def gegenbauer_poly(n, a, x=..., polys=...):
    r"""Generates the Gegenbauer polynomial `C_n^{(a)}(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    a
        Decides minimal domain for the list of coefficients.
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

def dup_chebyshevt(n, K) -> list[Any]:
    """Low-level implementation of Chebyshev polynomials of the first kind."""
    ...

def dup_chebyshevu(n, K) -> list[Any]:
    """Low-level implementation of Chebyshev polynomials of the second kind."""
    ...

@public
def chebyshevt_poly(n, x=..., polys=...):
    r"""Generates the Chebyshev polynomial of the first kind `T_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

@public
def chebyshevu_poly(n, x=..., polys=...):
    r"""Generates the Chebyshev polynomial of the second kind `U_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

def dup_hermite(n, K) -> list[Any]:
    """Low-level implementation of Hermite polynomials."""
    ...

def dup_hermite_prob(n, K) -> list[Any]:
    """Low-level implementation of probabilist's Hermite polynomials."""
    ...

@public
def hermite_poly(n, x=..., polys=...):
    r"""Generates the Hermite polynomial `H_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

@public
def hermite_prob_poly(n, x=..., polys=...):
    r"""Generates the probabilist's Hermite polynomial `He_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

def dup_legendre(n, K) -> list[Any]:
    """Low-level implementation of Legendre polynomials."""
    ...

@public
def legendre_poly(n, x=..., polys=...):
    r"""Generates the Legendre polynomial `P_n(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

def dup_laguerre(n, alpha, K) -> list[Any]:
    """Low-level implementation of Laguerre polynomials."""
    ...

@public
def laguerre_poly(n, x=..., alpha=..., polys=...):
    r"""Generates the Laguerre polynomial `L_n^{(\alpha)}(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    alpha : optional
        Decides minimal domain for the list of coefficients.
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

def dup_spherical_bessel_fn(n, K) -> list[Any]:
    """Low-level implementation of fn(n, x)."""
    ...

def dup_spherical_bessel_fn_minus(n, K) -> list[Any]:
    """Low-level implementation of fn(-n, x)."""
    ...

def spherical_bessel_fn(n, x=..., polys=...):
    """
    Coefficients for the spherical Bessel functions.

    These are only needed in the jn() function.

    The coefficients are calculated from:

    fn(0, z) = 1/z
    fn(1, z) = 1/z**2
    fn(n-1, z) + fn(n+1, z) == (2*n+1)/z * fn(n, z)

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.

    Examples
    ========

    >>> from sympy.polys.orthopolys import spherical_bessel_fn as fn
    >>> from sympy import Symbol
    >>> z = Symbol("z")
    >>> fn(1, z)
    z**(-2)
    >>> fn(2, z)
    -1/z + 3/z**3
    >>> fn(3, z)
    -6/z**2 + 15/z**4
    >>> fn(4, z)
    1/z - 45/z**3 + 105/z**5

    """
    ...

