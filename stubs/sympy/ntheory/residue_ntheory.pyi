from typing import Any, Generator
from sympy.core.function import UndefinedFunction
from sympy.utilities.decorator import deprecated

def n_order(a, n) -> int:
    r""" Returns the order of ``a`` modulo ``n``.

    Explanation
    ===========

    The order of ``a`` modulo ``n`` is the smallest integer
    ``k`` such that `a^k` leaves a remainder of 1 with ``n``.

    Parameters
    ==========

    a : integer
    n : integer, n > 1. a and n should be relatively prime

    Returns
    =======

    int : the order of ``a`` modulo ``n``

    Raises
    ======

    ValueError
        If `n \le 1` or `\gcd(a, n) \neq 1`.
        If ``a`` or ``n`` is not an integer.

    Examples
    ========

    >>> from sympy.ntheory import n_order
    >>> n_order(3, 7)
    6
    >>> n_order(4, 7)
    3

    See Also
    ========

    is_primitive_root
        We say that ``a`` is a primitive root of ``n``
        when the order of ``a`` modulo ``n`` equals ``totient(n)``

    """
    ...

def primitive_root(p, smallest=...) -> int | None:
    r""" Returns a primitive root of ``p`` or None.

    Explanation
    ===========

    For the definition of primitive root,
    see the explanation of ``is_primitive_root``.

    The primitive root of ``p`` exist only for
    `p = 2, 4, q^e, 2q^e` (``q`` is an odd prime).
    Now, if we know the primitive root of ``q``,
    we can calculate the primitive root of `q^e`,
    and if we know the primitive root of `q^e`,
    we can calculate the primitive root of `2q^e`.
    When there is no need to find the smallest primitive root,
    this property can be used to obtain a fast primitive root.
    On the other hand, when we want the smallest primitive root,
    we naively determine whether it is a primitive root or not.

    Parameters
    ==========

    p : integer, p > 1
    smallest : if True the smallest primitive root is returned or None

    Returns
    =======

    int | None :
        If the primitive root exists, return the primitive root of ``p``.
        If not, return None.

    Raises
    ======

    ValueError
        If `p \le 1` or ``p`` is not an integer.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import primitive_root
    >>> primitive_root(19)
    2
    >>> primitive_root(21) is None
    True
    >>> primitive_root(50, smallest=False)
    27

    See Also
    ========

    is_primitive_root

    References
    ==========

    .. [1] W. Stein "Elementary Number Theory" (2011), page 44
    .. [2] P. Hackman "Elementary Number Theory" (2009), Chapter C

    """
    ...

def is_primitive_root(a, p) -> bool:
    r""" Returns True if ``a`` is a primitive root of ``p``.

    Explanation
    ===========

    ``a`` is said to be the primitive root of ``p`` if `\gcd(a, p) = 1` and
    `\phi(p)` is the smallest positive number s.t.

        `a^{\phi(p)} \equiv 1 \pmod{p}`.

    where `\phi(p)` is Euler's totient function.

    The primitive root of ``p`` exist only for
    `p = 2, 4, q^e, 2q^e` (``q`` is an odd prime).
    Hence, if it is not such a ``p``, it returns False.
    To determine the primitive root, we need to know
    the prime factorization of ``q-1``.
    The hardness of the determination depends on this complexity.

    Parameters
    ==========

    a : integer
    p : integer, ``p`` > 1. ``a`` and ``p`` should be relatively prime

    Returns
    =======

    bool : If True, ``a`` is the primitive root of ``p``.

    Raises
    ======

    ValueError
        If `p \le 1` or `\gcd(a, p) \neq 1`.
        If ``a`` or ``p`` is not an integer.

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import totient
    >>> from sympy.ntheory import is_primitive_root, n_order
    >>> is_primitive_root(3, 10)
    True
    >>> is_primitive_root(9, 10)
    False
    >>> n_order(3, 10) == totient(10)
    True
    >>> n_order(9, 10) == totient(10)
    False

    See Also
    ========

    primitive_root

    """
    ...

def sqrt_mod(a, p, all_roots=...) -> list[int] | int | None:
    """
    Find a root of ``x**2 = a mod p``.

    Parameters
    ==========

    a : integer
    p : positive integer
    all_roots : if True the list of roots is returned or None

    Notes
    =====

    If there is no root it is returned None; else the returned root
    is less or equal to ``p // 2``; in general is not the smallest one.
    It is returned ``p // 2`` only if it is the only root.

    Use ``all_roots`` only when it is expected that all the roots fit
    in memory; otherwise use ``sqrt_mod_iter``.

    Examples
    ========

    >>> from sympy.ntheory import sqrt_mod
    >>> sqrt_mod(11, 43)
    21
    >>> sqrt_mod(17, 32, True)
    [7, 9, 23, 25]
    """
    ...

def sqrt_mod_iter(a, p, domain=...) -> Generator[int, Any, None]:
    """
    Iterate over solutions to ``x**2 = a mod p``.

    Parameters
    ==========

    a : integer
    p : positive integer
    domain : integer domain, ``int``, ``ZZ`` or ``Integer``

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import sqrt_mod_iter
    >>> list(sqrt_mod_iter(11, 43))
    [21, 22]

    See Also
    ========

    sqrt_mod : Same functionality, but you want a sorted list or only one solution.

    """
    ...

def is_quad_residue(a, p) -> bool:
    """
    Returns True if ``a`` (mod ``p``) is in the set of squares mod ``p``,
    i.e a % p in set([i**2 % p for i in range(p)]).

    Parameters
    ==========

    a : integer
    p : positive integer

    Returns
    =======

    bool : If True, ``x**2 == a (mod p)`` has solution.

    Raises
    ======

    ValueError
        If ``a``, ``p`` is not integer.
        If ``p`` is not positive.

    Examples
    ========

    >>> from sympy.ntheory import is_quad_residue
    >>> is_quad_residue(21, 100)
    True

    Indeed, ``pow(39, 2, 100)`` would be 21.

    >>> is_quad_residue(21, 120)
    False

    That is, for any integer ``x``, ``pow(x, 2, 120)`` is not 21.

    If ``p`` is an odd
    prime, an iterative method is used to make the determination:

    >>> from sympy.ntheory import is_quad_residue
    >>> sorted(set([i**2 % 7 for i in range(7)]))
    [0, 1, 2, 4]
    >>> [j for j in range(7) if is_quad_residue(j, 7)]
    [0, 1, 2, 4]

    See Also
    ========

    legendre_symbol, jacobi_symbol, sqrt_mod
    """
    ...

def is_nthpow_residue(a, n, m) -> bool:
    """
    Returns True if ``x**n == a (mod m)`` has solutions.

    References
    ==========

    .. [1] P. Hackman "Elementary Number Theory" (2009), page 76

    """
    ...

def nthroot_mod(a, n, p, all_roots=...) -> list[int] | int | list[Any] | None:
    """
    Find the solutions to ``x**n = a mod p``.

    Parameters
    ==========

    a : integer
    n : positive integer
    p : positive integer
    all_roots : if False returns the smallest root, else the list of roots

    Returns
    =======

        list[int] | int | None :
            solutions to ``x**n = a mod p``.
            The table of the output type is:

            ========== ========== ==========
            all_roots  has roots  Returns
            ========== ========== ==========
            True       Yes        list[int]
            True       No         []
            False      Yes        int
            False      No         None
            ========== ========== ==========

    Raises
    ======

        ValueError
            If ``a``, ``n`` or ``p`` is not integer.
            If ``n`` or ``p`` is not positive.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import nthroot_mod
    >>> nthroot_mod(11, 4, 19)
    8
    >>> nthroot_mod(11, 4, 19, True)
    [8, 11]
    >>> nthroot_mod(68, 3, 109)
    23

    References
    ==========

    .. [1] P. Hackman "Elementary Number Theory" (2009), page 76

    """
    ...

def quadratic_residues(p) -> list[int]:
    """
    Returns the list of quadratic residues.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import quadratic_residues
    >>> quadratic_residues(7)
    [0, 1, 2, 4]
    """
    ...

@deprecated("""\
The `sympy.ntheory.residue_ntheory.legendre_symbol` has been moved to `sympy.functions.combinatorial.numbers.legendre_symbol`.""", deprecated_since_version="1.13", active_deprecations_target='deprecated-ntheory-symbolic-functions')
def legendre_symbol(a, p) -> type[UndefinedFunction]:
    r"""
    Returns the Legendre symbol `(a / p)`.

    .. deprecated:: 1.13

        The ``legendre_symbol`` function is deprecated. Use :class:`sympy.functions.combinatorial.numbers.legendre_symbol`
        instead. See its documentation for more information. See
        :ref:`deprecated-ntheory-symbolic-functions` for details.

    For an integer ``a`` and an odd prime ``p``, the Legendre symbol is
    defined as

    .. math ::
        \genfrac(){}{}{a}{p} = \begin{cases}
             0 & \text{if } p \text{ divides } a\\
             1 & \text{if } a \text{ is a quadratic residue modulo } p\\
            -1 & \text{if } a \text{ is a quadratic nonresidue modulo } p
        \end{cases}

    Parameters
    ==========

    a : integer
    p : odd prime

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import legendre_symbol
    >>> [legendre_symbol(i, 7) for i in range(7)]
    [0, 1, 1, -1, 1, -1, -1]
    >>> sorted(set([i**2 % 7 for i in range(7)]))
    [0, 1, 2, 4]

    See Also
    ========

    is_quad_residue, jacobi_symbol

    """
    ...

@deprecated("""\
The `sympy.ntheory.residue_ntheory.jacobi_symbol` has been moved to `sympy.functions.combinatorial.numbers.jacobi_symbol`.""", deprecated_since_version="1.13", active_deprecations_target='deprecated-ntheory-symbolic-functions')
def jacobi_symbol(m, n) -> type[UndefinedFunction]:
    r"""
    Returns the Jacobi symbol `(m / n)`.

    .. deprecated:: 1.13

        The ``jacobi_symbol`` function is deprecated. Use :class:`sympy.functions.combinatorial.numbers.jacobi_symbol`
        instead. See its documentation for more information. See
        :ref:`deprecated-ntheory-symbolic-functions` for details.

    For any integer ``m`` and any positive odd integer ``n`` the Jacobi symbol
    is defined as the product of the Legendre symbols corresponding to the
    prime factors of ``n``:

    .. math ::
        \genfrac(){}{}{m}{n} =
            \genfrac(){}{}{m}{p^{1}}^{\alpha_1}
            \genfrac(){}{}{m}{p^{2}}^{\alpha_2}
            ...
            \genfrac(){}{}{m}{p^{k}}^{\alpha_k}
            \text{ where } n =
                p_1^{\alpha_1}
                p_2^{\alpha_2}
                ...
                p_k^{\alpha_k}

    Like the Legendre symbol, if the Jacobi symbol `\genfrac(){}{}{m}{n} = -1`
    then ``m`` is a quadratic nonresidue modulo ``n``.

    But, unlike the Legendre symbol, if the Jacobi symbol
    `\genfrac(){}{}{m}{n} = 1` then ``m`` may or may not be a quadratic residue
    modulo ``n``.

    Parameters
    ==========

    m : integer
    n : odd positive integer

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import jacobi_symbol, legendre_symbol
    >>> from sympy import S
    >>> jacobi_symbol(45, 77)
    -1
    >>> jacobi_symbol(60, 121)
    1

    The relationship between the ``jacobi_symbol`` and ``legendre_symbol`` can
    be demonstrated as follows:

    >>> L = legendre_symbol
    >>> S(45).factors()
    {3: 2, 5: 1}
    >>> jacobi_symbol(7, 45) == L(7, 3)**2 * L(7, 5)**1
    True

    See Also
    ========

    is_quad_residue, legendre_symbol
    """
    ...

@deprecated("""\
The `sympy.ntheory.residue_ntheory.mobius` has been moved to `sympy.functions.combinatorial.numbers.mobius`.""", deprecated_since_version="1.13", active_deprecations_target='deprecated-ntheory-symbolic-functions')
def mobius(n) -> type[UndefinedFunction]:
    """
    Mobius function maps natural number to {-1, 0, 1}

    .. deprecated:: 1.13

        The ``mobius`` function is deprecated. Use :class:`sympy.functions.combinatorial.numbers.mobius`
        instead. See its documentation for more information. See
        :ref:`deprecated-ntheory-symbolic-functions` for details.

    It is defined as follows:
        1) `1` if `n = 1`.
        2) `0` if `n` has a squared prime factor.
        3) `(-1)^k` if `n` is a square-free positive integer with `k`
           number of prime factors.

    It is an important multiplicative function in number theory
    and combinatorics.  It has applications in mathematical series,
    algebraic number theory and also physics (Fermion operator has very
    concrete realization with Mobius Function model).

    Parameters
    ==========

    n : positive integer

    Examples
    ========

    >>> from sympy.functions.combinatorial.numbers import mobius
    >>> mobius(13*7)
    1
    >>> mobius(1)
    1
    >>> mobius(13*7*5)
    -1
    >>> mobius(13**2)
    0

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/M%C3%B6bius_function
    .. [2] Thomas Koshy "Elementary Number Theory with Applications"

    """
    ...

def discrete_log(n, a, b, order=..., prime_order=...) -> int:
    """
    Compute the discrete logarithm of ``a`` to the base ``b`` modulo ``n``.

    This is a recursive function to reduce the discrete logarithm problem in
    cyclic groups of composite order to the problem in cyclic groups of prime
    order.

    It employs different algorithms depending on the problem (subgroup order
    size, prime order or not):

        * Trial multiplication
        * Baby-step giant-step
        * Pollard's Rho
        * Pohlig-Hellman

    Examples
    ========

    >>> from sympy.ntheory import discrete_log
    >>> discrete_log(41, 15, 7)
    3

    References
    ==========

    .. [1] https://mathworld.wolfram.com/DiscreteLogarithm.html
    .. [2] "Handbook of applied cryptography", Menezes, A. J., Van, O. P. C., &
        Vanstone, S. A. (1997).

    """
    ...

def quadratic_congruence(a, b, c, n) -> list[int] | list[Any]:
    r"""
    Find the solutions to `a x^2 + b x + c \equiv 0 \pmod{n}`.

    Parameters
    ==========

    a : int
    b : int
    c : int
    n : int
        A positive integer.

    Returns
    =======

    list[int] :
        A sorted list of solutions. If no solution exists, ``[]``.

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import quadratic_congruence
    >>> quadratic_congruence(2, 5, 3, 7) # 2x^2 + 5x + 3 = 0 (mod 7)
    [2, 6]
    >>> quadratic_congruence(8, 6, 4, 15) # No solution
    []

    See Also
    ========

    polynomial_congruence : Solve the polynomial congruence

    """
    ...

def polynomial_congruence(expr, m) -> list[int] | int | list[Any] | None:
    """
    Find the solutions to a polynomial congruence equation modulo m.

    Parameters
    ==========

    expr : integer coefficient polynomial
    m : positive integer

    Examples
    ========

    >>> from sympy.ntheory import polynomial_congruence
    >>> from sympy.abc import x
    >>> expr = x**6 - 2*x**5 -35
    >>> polynomial_congruence(expr, 6125)
    [3257]

    See Also
    ========

    sympy.polys.galoistools.gf_csolve : low level solving routine used by this routine

    """
    ...

def binomial_mod(n, m, k) -> int:
    """Compute ``binomial(n, m) % k``.

    Explanation
    ===========

    Returns ``binomial(n, m) % k`` using a generalization of Lucas'
    Theorem for prime powers given by Granville [1]_, in conjunction with
    the Chinese Remainder Theorem.  The residue for each prime power
    is calculated in time O(log^2(n) + q^4*log(n)log(p) + q^4*p*log^3(p)).

    Parameters
    ==========

    n : an integer
    m : an integer
    k : a positive integer

    Examples
    ========

    >>> from sympy.ntheory.residue_ntheory import binomial_mod
    >>> binomial_mod(10, 2, 6)  # binomial(10, 2) = 45
    3
    >>> binomial_mod(17, 9, 10)  # binomial(17, 9) = 24310
    0

    References
    ==========

    .. [1] Binomial coefficients modulo prime powers, Andrew Granville,
        Available: https://web.archive.org/web/20170202003812/http://www.dms.umontreal.ca/~andrew/PDF/BinCoeff.pdf
    """
    ...

