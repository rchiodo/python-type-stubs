from sympy.utilities import public

r"""
Efficient functions for generating Appell sequences.

An Appell sequence is a zero-indexed sequence of polynomials `p_i(x)`
satisfying `p_{i+1}'(x)=(i+1)p_i(x)` for all `i`. This definition leads
to the following iterative algorithm:

.. math :: p_0(x) = c_0,\ p_i(x) = i \int_0^x p_{i-1}(t)\,dt + c_i

The constant coefficients `c_i` are usually determined from the
just-evaluated integral and `i`.

Appell sequences satisfy the following identity from umbral calculus:

.. math :: p_n(x+y) = \sum_{k=0}^n \binom{n}{k} p_k(x) y^{n-k}

References
==========

.. [1] https://en.wikipedia.org/wiki/Appell_sequence
.. [2] Peter Luschny, "An introduction to the Bernoulli function",
       https://arxiv.org/abs/2009.06743
"""
def dup_bernoulli(n, K) -> list[Any]:
    """Low-level implementation of Bernoulli polynomials."""
    ...

@public
def bernoulli_poly(n, x=..., polys=...):
    r"""Generates the Bernoulli polynomial `\operatorname{B}_n(x)`.

    `\operatorname{B}_n(x)` is the unique polynomial satisfying

    .. math :: \int_{x}^{x+1} \operatorname{B}_n(t) \,dt = x^n.

    Based on this, we have for nonnegative integer `s` and integer
    `a` and `b`

    .. math :: \sum_{k=a}^{b} k^s = \frac{\operatorname{B}_{s+1}(b+1) -
            \operatorname{B}_{s+1}(a)}{s+1}

    which is related to Jakob Bernoulli's original motivation for introducing
    the Bernoulli numbers, the values of these polynomials at `x = 1`.

    Examples
    ========

    >>> from sympy import summation
    >>> from sympy.abc import x
    >>> from sympy.polys import bernoulli_poly
    >>> bernoulli_poly(5, x)
    x**5 - 5*x**4/2 + 5*x**3/3 - x/6

    >>> def psum(p, a, b):
    ...     return (bernoulli_poly(p+1,b+1) - bernoulli_poly(p+1,a)) / (p+1)
    >>> psum(4, -6, 27)
    3144337
    >>> summation(x**4, (x, -6, 27))
    3144337

    >>> psum(1, 1, x).factor()
    x*(x + 1)/2
    >>> psum(2, 1, x).factor()
    x*(x + 1)*(2*x + 1)/6
    >>> psum(3, 1, x).factor()
    x**2*(x + 1)**2/4

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.

    See Also
    ========

    sympy.functions.combinatorial.numbers.bernoulli

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Bernoulli_polynomials
    """
    ...

def dup_bernoulli_c(n, K) -> list[Any]:
    """Low-level implementation of central Bernoulli polynomials."""
    ...

@public
def bernoulli_c_poly(n, x=..., polys=...):
    r"""Generates the central Bernoulli polynomial `\operatorname{B}_n^c(x)`.

    These are scaled and shifted versions of the plain Bernoulli polynomials,
    done in such a way that `\operatorname{B}_n^c(x)` is an even or odd function
    for even or odd `n` respectively:

    .. math :: \operatorname{B}_n^c(x) = 2^n \operatorname{B}_n
            \left(\frac{x+1}{2}\right)

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    """
    ...

def dup_genocchi(n, K) -> list[Any]:
    """Low-level implementation of Genocchi polynomials."""
    ...

@public
def genocchi_poly(n, x=..., polys=...):
    r"""Generates the Genocchi polynomial `\operatorname{G}_n(x)`.

    `\operatorname{G}_n(x)` is twice the difference between the plain and
    central Bernoulli polynomials, so has degree `n-1`:

    .. math :: \operatorname{G}_n(x) = 2 (\operatorname{B}_n(x) -
            \operatorname{B}_n^c(x))

    The factor of 2 in the definition endows `\operatorname{G}_n(x)` with
    integer coefficients.

    Parameters
    ==========

    n : int
        Degree of the polynomial plus one.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.

    See Also
    ========

    sympy.functions.combinatorial.numbers.genocchi
    """
    ...

def dup_euler(n, K) -> list[Any]:
    """Low-level implementation of Euler polynomials."""
    ...

@public
def euler_poly(n, x=..., polys=...):
    r"""Generates the Euler polynomial `\operatorname{E}_n(x)`.

    These are scaled and reindexed versions of the Genocchi polynomials:

    .. math :: \operatorname{E}_n(x) = -\frac{\operatorname{G}_{n+1}(x)}{n+1}

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.

    See Also
    ========

    sympy.functions.combinatorial.numbers.euler
    """
    ...

def dup_andre(n, K) -> list[Any]:
    """Low-level implementation of Andre polynomials."""
    ...

@public
def andre_poly(n, x=..., polys=...):
    r"""Generates the Andre polynomial `\mathcal{A}_n(x)`.

    This is the Appell sequence where the constant coefficients form the sequence
    of Euler numbers ``euler(n)``. As such they have integer coefficients
    and parities matching the parity of `n`.

    Luschny calls these the *Swiss-knife polynomials* because their values
    at 0 and 1 can be simply transformed into both the Bernoulli and Euler
    numbers. Here they are called the Andre polynomials because
    `|\mathcal{A}_n(n\bmod 2)|` for `n \ge 0` generates what Luschny calls
    the *Andre numbers*, A000111 in the OEIS.

    Examples
    ========

    >>> from sympy import bernoulli, euler, genocchi
    >>> from sympy.abc import x
    >>> from sympy.polys import andre_poly
    >>> andre_poly(9, x)
    x**9 - 36*x**7 + 630*x**5 - 5124*x**3 + 12465*x

    >>> [andre_poly(n, 0) for n in range(11)]
    [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]
    >>> [euler(n) for n in range(11)]
    [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]
    >>> [andre_poly(n-1, 1) * n / (4**n - 2**n) for n in range(1, 11)]
    [1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66]
    >>> [bernoulli(n) for n in range(1, 11)]
    [1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66]
    >>> [-andre_poly(n-1, -1) * n / (-2)**(n-1) for n in range(1, 11)]
    [-1, -1, 0, 1, 0, -3, 0, 17, 0, -155]
    >>> [genocchi(n) for n in range(1, 11)]
    [-1, -1, 0, 1, 0, -3, 0, 17, 0, -155]

    >>> [abs(andre_poly(n, n%2)) for n in range(11)]
    [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521]

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.

    See Also
    ========

    sympy.functions.combinatorial.numbers.andre

    References
    ==========

    .. [1] Peter Luschny, "An introduction to the Bernoulli function",
           https://arxiv.org/abs/2009.06743
    """
    ...

