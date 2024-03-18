from typing import Any, Literal
from sympy.external.gmpy import GROUND_TYPES

"""Polynomial factorization routines in characteristic zero. """
if GROUND_TYPES == 'flint':
    ...
else:
    fmpz_poly = ...
def dup_trial_division(f, factors, K) -> list[Any]:
    """
    Determine multiplicities of factors for a univariate polynomial
    using trial division.
    """
    ...

def dmp_trial_division(f, factors, u, K) -> list[Any]:
    """
    Determine multiplicities of factors for a multivariate polynomial
    using trial division.
    """
    ...

def dup_zz_mignotte_bound(f, K):
    """
    The Knuth-Cohen variant of Mignotte bound for
    univariate polynomials in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = x**3 + 14*x**2 + 56*x + 64
    >>> R.dup_zz_mignotte_bound(f)
    152

    By checking `factor(f)` we can see that max coeff is 8

    Also consider a case that `f` is irreducible for example `f = 2*x**2 + 3*x + 4`
    To avoid a bug for these cases, we return the bound plus the max coefficient of `f`

    >>> f = 2*x**2 + 3*x + 4
    >>> R.dup_zz_mignotte_bound(f)
    6

    Lastly,To see the difference between the new and the old Mignotte bound
    consider the irreducible polynomial::

    >>> f = 87*x**7 + 4*x**6 + 80*x**5 + 17*x**4 + 9*x**3 + 12*x**2 + 49*x + 26
    >>> R.dup_zz_mignotte_bound(f)
    744

    The new Mignotte bound is 744 whereas the old one (SymPy 1.5.1) is 1937664.


    References
    ==========

    ..[1] [Abbott2013]_

    """
    ...

def dmp_zz_mignotte_bound(f, u, K):
    """Mignotte bound for multivariate polynomials in `K[X]`. """
    ...

def dup_zz_hensel_step(m, f, g, h, s, t, K) -> tuple[list[Any], list[Any], list[Any], list[Any]]:
    """
    One step in Hensel lifting in `Z[x]`.

    Given positive integer `m` and `Z[x]` polynomials `f`, `g`, `h`, `s`
    and `t` such that::

        f = g*h (mod m)
        s*g + t*h = 1 (mod m)

        lc(f) is not a zero divisor (mod m)
        lc(h) = 1

        deg(f) = deg(g) + deg(h)
        deg(s) < deg(h)
        deg(t) < deg(g)

    returns polynomials `G`, `H`, `S` and `T`, such that::

        f = G*H (mod m**2)
        S*G + T*H = 1 (mod m**2)

    References
    ==========

    .. [1] [Gathen99]_

    """
    ...

def dup_zz_hensel_lift(p, f, f_list, l, K) -> list[list[Any]]:
    r"""
    Multifactor Hensel lifting in `Z[x]`.

    Given a prime `p`, polynomial `f` over `Z[x]` such that `lc(f)`
    is a unit modulo `p`, monic pair-wise coprime polynomials `f_i`
    over `Z[x]` satisfying::

        f = lc(f) f_1 ... f_r (mod p)

    and a positive integer `l`, returns a list of monic polynomials
    `F_1,\ F_2,\ \dots,\ F_r` satisfying::

       f = lc(f) F_1 ... F_r (mod p**l)

       F_i = f_i (mod p), i = 1..r

    References
    ==========

    .. [1] [Gathen99]_

    """
    ...

def dup_zz_zassenhaus(f, K) -> list[Any]:
    """Factor primitive square-free polynomials in `Z[x]`. """
    ...

def dup_zz_irreducible_p(f, K) -> Literal[True] | None:
    """Test irreducibility using Eisenstein's criterion. """
    ...

def dup_cyclotomic_p(f, K, irreducible=...) -> bool:
    """
    Efficiently test if ``f`` is a cyclotomic polynomial.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = x**16 + x**14 - x**10 + x**8 - x**6 + x**2 + 1
    >>> R.dup_cyclotomic_p(f)
    False

    >>> g = x**16 + x**14 - x**10 - x**8 - x**6 + x**2 + 1
    >>> R.dup_cyclotomic_p(g)
    True

    References
    ==========

    Bradford, Russell J., and James H. Davenport. "Effective tests for
    cyclotomic polynomials." In International Symposium on Symbolic and
    Algebraic Computation, pp. 244-251. Springer, Berlin, Heidelberg, 1988.

    """
    ...

def dup_zz_cyclotomic_poly(n, K) -> list[Any]:
    """Efficiently generate n-th cyclotomic polynomial. """
    ...

def dup_zz_cyclotomic_factor(f, K) -> list[list[Any]] | list[Any] | None:
    """
    Efficiently factor polynomials `x**n - 1` and `x**n + 1` in `Z[x]`.

    Given a univariate polynomial `f` in `Z[x]` returns a list of factors
    of `f`, provided that `f` is in the form `x**n - 1` or `x**n + 1` for
    `n >= 1`. Otherwise returns None.

    Factorization is performed using cyclotomic decomposition of `f`,
    which makes this method much faster that any other direct factorization
    approach (e.g. Zassenhaus's).

    References
    ==========

    .. [1] [Weisstein09]_

    """
    ...

def dup_zz_factor_sqf(f, K) -> tuple[Any, list[Any]] | tuple[Any, list[list[Any] | Any]]:
    """Factor square-free (non-primitive) polynomials in `Z[x]`. """
    ...

def dup_zz_factor(f, K) -> tuple[Any, list[Any]] | tuple[Any, list[tuple[list[Any] | Any, Literal[1]]]]:
    """
    Factor (non square-free) polynomials in `Z[x]`.

    Given a univariate polynomial `f` in `Z[x]` computes its complete
    factorization `f_1, ..., f_n` into irreducibles over integers::

                f = content(f) f_1**k_1 ... f_n**k_n

    The factorization is computed by reducing the input polynomial
    into a primitive square-free polynomial and factoring it using
    Zassenhaus algorithm. Trial division is used to recover the
    multiplicities of factors.

    The result is returned as a tuple consisting of::

              (content(f), [(f_1, k_1), ..., (f_n, k_n))

    Examples
    ========

    Consider the polynomial `f = 2*x**4 - 2`::

        >>> from sympy.polys import ring, ZZ
        >>> R, x = ring("x", ZZ)

        >>> R.dup_zz_factor(2*x**4 - 2)
        (2, [(x - 1, 1), (x + 1, 1), (x**2 + 1, 1)])

    In result we got the following factorization::

                 f = 2 (x - 1) (x + 1) (x**2 + 1)

    Note that this is a complete factorization over integers,
    however over Gaussian integers we can factor the last term.

    By default, polynomials `x**n - 1` and `x**n + 1` are factored
    using cyclotomic decomposition to speedup computations. To
    disable this behaviour set cyclotomic=False.

    References
    ==========

    .. [1] [Gathen99]_

    """
    ...

def dmp_zz_wang_non_divisors(E, cs, ct, K) -> list[Any] | None:
    """Wang/EEZ: Compute a set of valid divisors.  """
    ...

def dmp_zz_wang_test_points(f, T, ct, A, u, K) -> tuple[Any, list[Any] | Any | list[list[Any]], list[Any | list[list[Any]] | list[Any]]]:
    """Wang/EEZ: Test evaluation points for suitability. """
    ...

def dmp_zz_wang_lead_coeffs(f, T, cs, E, H, A, u, K) -> tuple[Any, list[Any], list[Any]] | tuple[list[Any], list[Any], list[Any]]:
    """Wang/EEZ: Compute correct leading coefficients. """
    ...

def dup_zz_diophantine(F, m, p, K) -> list[Any]:
    """Wang/EEZ: Solve univariate Diophantine equations. """
    ...

def dmp_zz_diophantine(F, c, A, d, p, u, K) -> list[list[Any]] | list[list[Any] | Any | list[list[Any]]]:
    """Wang/EEZ: Solve multivariate Diophantine equations. """
    ...

def dmp_zz_wang_hensel_lifting(f, H, LC, A, p, u, K) -> list[Any]:
    """Wang/EEZ: Parallel Hensel lifting algorithm. """
    ...

def dmp_zz_wang(f, u, K, mod=..., seed=...) -> list[Any]:
    r"""
    Factor primitive square-free polynomials in `Z[X]`.

    Given a multivariate polynomial `f` in `Z[x_1,...,x_n]`, which is
    primitive and square-free in `x_1`, computes factorization of `f` into
    irreducibles over integers.

    The procedure is based on Wang's Enhanced Extended Zassenhaus
    algorithm. The algorithm works by viewing `f` as a univariate polynomial
    in `Z[x_2,...,x_n][x_1]`, for which an evaluation mapping is computed::

                      x_2 -> a_2, ..., x_n -> a_n

    where `a_i`, for `i = 2, \dots, n`, are carefully chosen integers.  The
    mapping is used to transform `f` into a univariate polynomial in `Z[x_1]`,
    which can be factored efficiently using Zassenhaus algorithm. The last
    step is to lift univariate factors to obtain true multivariate
    factors. For this purpose a parallel Hensel lifting procedure is used.

    The parameter ``seed`` is passed to _randint and can be used to seed randint
    (when an integer) or (for testing purposes) can be a sequence of numbers.

    References
    ==========

    .. [1] [Wang78]_
    .. [2] [Geddes92]_

    """
    ...

def dmp_zz_factor(f, u, K) -> tuple[Any, list[Any]] | tuple[Any, list[tuple[list[Any] | Any, Literal[1]]]]:
    r"""
    Factor (non square-free) polynomials in `Z[X]`.

    Given a multivariate polynomial `f` in `Z[x]` computes its complete
    factorization `f_1, \dots, f_n` into irreducibles over integers::

                 f = content(f) f_1**k_1 ... f_n**k_n

    The factorization is computed by reducing the input polynomial
    into a primitive square-free polynomial and factoring it using
    Enhanced Extended Zassenhaus (EEZ) algorithm. Trial division
    is used to recover the multiplicities of factors.

    The result is returned as a tuple consisting of::

             (content(f), [(f_1, k_1), ..., (f_n, k_n))

    Consider polynomial `f = 2*(x**2 - y**2)`::

        >>> from sympy.polys import ring, ZZ
        >>> R, x,y = ring("x,y", ZZ)

        >>> R.dmp_zz_factor(2*x**2 - 2*y**2)
        (2, [(x - y, 1), (x + y, 1)])

    In result we got the following factorization::

                    f = 2 (x - y) (x + y)

    References
    ==========

    .. [1] [Gathen99]_

    """
    ...

def dup_qq_i_factor(f, K0) -> tuple[Any, list[tuple[Any | list[Any], Any]]]:
    """Factor univariate polynomials into irreducibles in `QQ_I[x]`. """
    ...

def dup_zz_i_factor(f, K0) -> tuple[Any, list[Any]]:
    """Factor univariate polynomials into irreducibles in `ZZ_I[x]`. """
    ...

def dmp_qq_i_factor(f, u, K0) -> tuple[Any, list[tuple[Any | list[Any] | list[list[Any]], Any]]]:
    """Factor multivariate polynomials into irreducibles in `QQ_I[X]`. """
    ...

def dmp_zz_i_factor(f, u, K0) -> tuple[Any, list[Any]]:
    """Factor multivariate polynomials into irreducibles in `ZZ_I[X]`. """
    ...

def dup_ext_factor(f, K) -> tuple[Any, list[Any]] | tuple[Any, list[tuple[Any | list[Any], Literal[1]]]] | tuple[Any, list[tuple[list[Any] | list[int] | Any, float | int]]]:
    """Factor univariate polynomials over algebraic number fields. """
    ...

def dmp_ext_factor(f, u, K) -> tuple[Any, list[Any]] | tuple[Any, list[tuple[Any | list[Any], Literal[1]]]] | tuple[Any, list[tuple[list[Any] | list[int] | Any, float | int]]]:
    """Factor multivariate polynomials over algebraic number fields. """
    ...

def dup_gf_factor(f, K) -> tuple[Any, list[Any]]:
    """Factor univariate polynomials over finite fields. """
    ...

def dmp_gf_factor(f, u, K):
    """Factor multivariate polynomials over finite fields. """
    ...

def dup_factor_list(f, K0) -> tuple[Any, list[Any]]:
    """Factor univariate polynomials into irreducibles in `K[x]`. """
    ...

def dup_factor_list_include(f, K) -> list[tuple[list[Any], Literal[1]]]:
    """Factor univariate polynomials into irreducibles in `K[x]`. """
    ...

def dmp_factor_list(f, u, K0) -> tuple[Any, list[Any]]:
    """Factor multivariate polynomials into irreducibles in `K[X]`. """
    ...

def dmp_factor_list_include(f, u, K) -> list[tuple[list[Any], Literal[1]]] | list[tuple[list[list[Any]] | Any | list[Any], Literal[1]]]:
    """Factor multivariate polynomials into irreducibles in `K[X]`. """
    ...

def dup_irreducible_p(f, K) -> bool:
    """
    Returns ``True`` if a univariate polynomial ``f`` has no factors
    over its domain.
    """
    ...

def dmp_irreducible_p(f, u, K) -> bool:
    """
    Returns ``True`` if a multivariate polynomial ``f`` has no factors
    over its domain.
    """
    ...

