"""Square-free decomposition algorithms and related tools. """
from typing import Any, Literal


def dup_sqf_p(f, K) -> bool:
    """
    Return ``True`` if ``f`` is a square-free polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sqf_p(x**2 - 2*x + 1)
    False
    >>> R.dup_sqf_p(x**2 - 1)
    True

    """
    ...

def dmp_sqf_p(f, u, K) -> bool:
    """
    Return ``True`` if ``f`` is a square-free polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sqf_p(x**2 + 2*x*y + y**2)
    False
    >>> R.dmp_sqf_p(x**2 + y**2)
    True

    """
    ...

def dup_sqf_norm(f, K) -> tuple[int, Any | list[Any], tuple[Any, list[Any]] | Any | tuple[list[list[Any]], list[Any]] | tuple[list[list[Any]] | Any | list[Any], list[Any]] | list[list[Any]] | list[Any]]:
    """
    Square-free norm of ``f`` in ``K[x]``, useful over algebraic domains.

    Returns ``s``, ``f``, ``r``, such that ``g(x) = f(x-sa)`` and ``r(x) = Norm(g(x))``
    is a square-free polynomial over K, where ``a`` is the algebraic extension of ``K``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> from sympy import sqrt

    >>> K = QQ.algebraic_field(sqrt(3))
    >>> R, x = ring("x", K)
    >>> _, X = ring("x", QQ)

    >>> s, f, r = R.dup_sqf_norm(x**2 - 2)

    >>> s == 1
    True
    >>> f == x**2 + K([QQ(-2), QQ(0)])*x + 1
    True
    >>> r == X**4 - 10*X**2 + 1
    True

    """
    ...

def dmp_sqf_norm(f, u, K) -> tuple[int, Any | list[Any], tuple[Any, list[Any]] | Any | tuple[list[list[Any]], list[Any]] | tuple[list[list[Any]] | Any | list[Any], list[Any]] | list[list[Any]] | list[Any]] | tuple[int, Any | list[Any] | list[list[Any]] | list[Any | list[Any]], tuple[Any, list[Any]] | Any | tuple[list[list[Any]], list[Any]] | tuple[list[list[Any]] | Any | list[Any], list[Any]] | list[list[Any]] | list[Any]]:
    """
    Square-free norm of ``f`` in ``K[X]``, useful over algebraic domains.

    Returns ``s``, ``f``, ``r``, such that ``g(x) = f(x-sa)`` and ``r(x) = Norm(g(x))``
    is a square-free polynomial over K, where ``a`` is the algebraic extension of ``K``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> from sympy import I

    >>> K = QQ.algebraic_field(I)
    >>> R, x, y = ring("x,y", K)
    >>> _, X, Y = ring("x,y", QQ)

    >>> s, f, r = R.dmp_sqf_norm(x*y + y**2)

    >>> s == 1
    True
    >>> f == x*y + y**2 + K([QQ(-1), QQ(0)])*y
    True
    >>> r == X**2*Y**2 + 2*X*Y**3 + Y**4 + Y**2
    True

    """
    ...

def dmp_norm(f, u, K) -> tuple[Any, list[Any]] | tuple[list[list[Any]], list[Any]] | tuple[list[list[Any]] | Any | list[Any], list[Any]] | list[list[Any]] | list[Any]:
    """
    Norm of ``f`` in ``K[X1, ..., Xn]``, often not square-free.
    """
    ...

def dup_gf_sqf_part(f, K) -> list[Any] | list[int]:
    """Compute square-free part of ``f`` in ``GF(p)[x]``. """
    ...

def dmp_gf_sqf_part(f, u, K):
    """Compute square-free part of ``f`` in ``GF(p)[X]``. """
    ...

def dup_sqf_part(f, K) -> list[Any] | list[int]:
    """
    Returns square-free part of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sqf_part(x**3 - 3*x - 2)
    x**2 - x - 2

    """
    ...

def dmp_sqf_part(f, u, K) -> list[Any] | list[int] | list[list[Any]]:
    """
    Returns square-free part of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sqf_part(x**3 + 2*x**2*y + x*y**2)
    x**2 + x*y

    """
    ...

def dup_gf_sqf_list(f, K, all=...) -> tuple[Any, list[Any]]:
    """Compute square-free decomposition of ``f`` in ``GF(p)[x]``. """
    ...

def dmp_gf_sqf_list(f, u, K, all=...):
    """Compute square-free decomposition of ``f`` in ``GF(p)[X]``. """
    ...

def dup_sqf_list(f, K, all=...) -> tuple[Any, list[Any]]:
    """
    Return square-free decomposition of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = 2*x**5 + 16*x**4 + 50*x**3 + 76*x**2 + 56*x + 16

    >>> R.dup_sqf_list(f)
    (2, [(x + 1, 2), (x + 2, 3)])
    >>> R.dup_sqf_list(f, all=True)
    (2, [(1, 1), (x + 1, 2), (x + 2, 3)])

    """
    ...

def dup_sqf_list_include(f, K, all=...) -> list[tuple[list[Any], Literal[1]]]:
    """
    Return square-free decomposition of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = 2*x**5 + 16*x**4 + 50*x**3 + 76*x**2 + 56*x + 16

    >>> R.dup_sqf_list_include(f)
    [(2, 1), (x + 1, 2), (x + 2, 3)]
    >>> R.dup_sqf_list_include(f, all=True)
    [(2, 1), (x + 1, 2), (x + 2, 3)]

    """
    ...

def dmp_sqf_list(f, u, K, all=...) -> tuple[Any, list[Any]] | tuple[Any, list[tuple[list[Any], Any]]]:
    """
    Return square-free decomposition of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x**5 + 2*x**4*y + x**3*y**2

    >>> R.dmp_sqf_list(f)
    (1, [(x + y, 2), (x, 3)])
    >>> R.dmp_sqf_list(f, all=True)
    (1, [(1, 1), (x + y, 2), (x, 3)])

    """
    ...

def dmp_sqf_list_include(f, u, K, all=...) -> list[tuple[list[Any], Literal[1]]] | list[tuple[list[list[Any]] | Any | list[Any], Literal[1]]]:
    """
    Return square-free decomposition of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x**5 + 2*x**4*y + x**3*y**2

    >>> R.dmp_sqf_list_include(f)
    [(1, 1), (x + y, 2), (x, 3)]
    >>> R.dmp_sqf_list_include(f, all=True)
    [(1, 1), (x + y, 2), (x, 3)]

    """
    ...

def dup_gff_list(f, K) -> list[Any]:
    """
    Compute greatest factorial factorization of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_gff_list(x**5 + 2*x**4 - x**3 - 2*x**2)
    [(x, 1), (x + 2, 4)]

    """
    ...

def dmp_gff_list(f, u, K) -> list[Any]:
    """
    Compute greatest factorial factorization of ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    """
    ...

