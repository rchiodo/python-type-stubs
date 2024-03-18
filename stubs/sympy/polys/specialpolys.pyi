from typing import Any
from sympy.series.order import Order
from sympy.utilities import public

"""Functions for generating interesting polynomials, e.g. for benchmarking. """
@public
def swinnerton_dyer_poly(n, x=..., polys=...) -> Any:
    """Generates n-th Swinnerton-Dyer polynomial in `x`.

    Parameters
    ----------
    n : int
        `n` decides the order of polynomial
    x : optional
    polys : bool, optional
        ``polys=True`` returns an expression, otherwise
        (default) returns an expression.
    """
    ...

@public
def cyclotomic_poly(n, x=..., polys=...):
    """Generates cyclotomic polynomial of order `n` in `x`.

    Parameters
    ----------
    n : int
        `n` decides the order of polynomial
    x : optional
    polys : bool, optional
        ``polys=True`` returns an expression, otherwise
        (default) returns an expression.
    """
    ...

@public
def symmetric_poly(n, *gens, polys=...) -> Any | Order:
    """
    Generates symmetric polynomial of order `n`.

    Parameters
    ==========

    polys: bool, optional (default: False)
        Returns a Poly object when ``polys=True``, otherwise
        (default) returns an expression.
    """
    ...

@public
def random_poly(x, n, inf, sup, domain=..., polys=...) -> Any:
    """Generates a polynomial of degree ``n`` with coefficients in
    ``[inf, sup]``.

    Parameters
    ----------
    x
        `x` is the independent term of polynomial
    n : int
        `n` decides the order of polynomial
    inf
        Lower limit of range in which coefficients lie
    sup
        Upper limit of range in which coefficients lie
    domain : optional
         Decides what ring the coefficients are supposed
         to belong. Default is set to Integers.
    polys : bool, optional
        ``polys=True`` returns an expression, otherwise
        (default) returns an expression.
    """
    ...

@public
def interpolating_poly(n, x, X=..., Y=...) -> Order:
    """Construct Lagrange interpolating polynomial for ``n``
    data points. If a sequence of values are given for ``X`` and ``Y``
    then the first ``n`` values will be used.
    """
    ...

def fateman_poly_F_1(n) -> tuple[Any, Any, Any]:
    """Fateman's GCD benchmark: trivial GCD """
    ...

def dmp_fateman_poly_F_1(n, K) -> tuple[list[Any] | Any | list[list[Any]] | list[list[list[Any]] | Any | list[Any]], list[Any] | Any | list[list[Any]] | list[list[list[Any]] | Any | list[Any]], list[list[Any]] | Any | list[Any]]:
    """Fateman's GCD benchmark: trivial GCD """
    ...

def fateman_poly_F_2(n) -> tuple[Any, Any, Any]:
    """Fateman's GCD benchmark: linearly dense quartic inputs """
    ...

def dmp_fateman_poly_F_2(n, K) -> tuple[list[Any] | Any | list[list[Any]], list[Any] | Any | list[list[Any]], list[Any] | Any | list[list[Any]]]:
    """Fateman's GCD benchmark: linearly dense quartic inputs """
    ...

def fateman_poly_F_3(n) -> tuple[Any, Any, Any]:
    """Fateman's GCD benchmark: sparse inputs (deg f ~ vars f) """
    ...

def dmp_fateman_poly_F_3(n, K) -> tuple[list[Any] | Any | list[list[Any]] | list[list[list[Any]] | Any | list[Any]] | list[Any | list[Any] | list[list[Any] | Any | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]] | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]], list[Any] | Any | list[list[Any]] | list[Any | list[Any] | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]] | list[list[list[Any]] | Any | list[Any]] | list[Any | list[Any] | list[list[Any] | Any | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]] | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]], list[Any] | Any | list[Any | list[Any] | list[list[Any] | Any | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]] | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]] | list[list[Any]] | list[list[list[Any]] | Any | list[Any]]]:
    """Fateman's GCD benchmark: sparse inputs (deg f ~ vars f) """
    ...

def f_polys() -> tuple[Any, Any, Any, Any, Any, Any, Any]:
    ...

def w_polys() -> tuple[Any, Any]:
    ...

