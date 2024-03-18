r"""
This module is intended for solving recurrences or, in other words,
difference equations. Currently supported are linear, inhomogeneous
equations with polynomial or rational coefficients.

The solutions are obtained among polynomials, rational functions,
hypergeometric terms, or combinations of hypergeometric term which
are pairwise dissimilar.

``rsolve_X`` functions were meant as a low level interface
for ``rsolve`` which would use Mathematica's syntax.

Given a recurrence relation:

    .. math:: a_{k}(n) y(n+k) + a_{k-1}(n) y(n+k-1) +
              ... + a_{0}(n) y(n) = f(n)

where `k > 0` and `a_{i}(n)` are polynomials in `n`. To use
``rsolve_X`` we need to put all coefficients in to a list ``L`` of
`k+1` elements the following way:

    ``L = [a_{0}(n), ..., a_{k-1}(n), a_{k}(n)]``

where ``L[i]``, for `i=0, \ldots, k`, maps to
`a_{i}(n) y(n+i)` (`y(n+i)` is implicit).

For example if we would like to compute `m`-th Bernoulli polynomial
up to a constant (example was taken from rsolve_poly docstring),
then we would use `b(n+1) - b(n) = m n^{m-1}` recurrence, which
has solution `b(n) = B_m + C`.

Then ``L = [-1, 1]`` and `f(n) = m n^(m-1)` and finally for `m=4`:

>>> from sympy import Symbol, bernoulli, rsolve_poly
>>> n = Symbol('n', integer=True)

>>> rsolve_poly([-1, 1], 4*n**3, n)
C0 + n**4 - 2*n**3 + n**2

>>> bernoulli(4, n)
n**4 - 2*n**3 + n**2 - 1/30

For the sake of completeness, `f(n)` can be:

    [1] a polynomial               -> rsolve_poly
    [2] a rational function        -> rsolve_ratio
    [3] a hypergeometric function  -> rsolve_hyper
"""
from typing import Any


def rsolve_poly(coeffs, f, n, shift=..., **hints):
    r"""
    Given linear recurrence operator `\operatorname{L}` of order
    `k` with polynomial coefficients and inhomogeneous equation
    `\operatorname{L} y = f`, where `f` is a polynomial, we seek for
    all polynomial solutions over field `K` of characteristic zero.

    The algorithm performs two basic steps:

        (1) Compute degree `N` of the general polynomial solution.
        (2) Find all polynomials of degree `N` or less
            of `\operatorname{L} y = f`.

    There are two methods for computing the polynomial solutions.
    If the degree bound is relatively small, i.e. it's smaller than
    or equal to the order of the recurrence, then naive method of
    undetermined coefficients is being used. This gives a system
    of algebraic equations with `N+1` unknowns.

    In the other case, the algorithm performs transformation of the
    initial equation to an equivalent one for which the system of
    algebraic equations has only `r` indeterminates. This method is
    quite sophisticated (in comparison with the naive one) and was
    invented together by Abramov, Bronstein and Petkovsek.

    It is possible to generalize the algorithm implemented here to
    the case of linear q-difference and differential equations.

    Lets say that we would like to compute `m`-th Bernoulli polynomial
    up to a constant. For this we can use `b(n+1) - b(n) = m n^{m-1}`
    recurrence, which has solution `b(n) = B_m + C`. For example:

    >>> from sympy import Symbol, rsolve_poly
    >>> n = Symbol('n', integer=True)

    >>> rsolve_poly([-1, 1], 4*n**3, n)
    C0 + n**4 - 2*n**3 + n**2

    References
    ==========

    .. [1] S. A. Abramov, M. Bronstein and M. Petkovsek, On polynomial
           solutions of linear operator equations, in: T. Levelt, ed.,
           Proc. ISSAC '95, ACM Press, New York, 1995, 290-296.

    .. [2] M. Petkovsek, Hypergeometric solutions of linear recurrences
           with polynomial coefficients, J. Symbolic Computation,
           14 (1992), 243-264.

    .. [3] M. Petkovsek, H. S. Wilf, D. Zeilberger, A = B, 1996.

    """
    ...

def rsolve_ratio(coeffs, f, n, **hints) -> tuple[Any, Any] | None:
    r"""
    Given linear recurrence operator `\operatorname{L}` of order `k`
    with polynomial coefficients and inhomogeneous equation
    `\operatorname{L} y = f`, where `f` is a polynomial, we seek
    for all rational solutions over field `K` of characteristic zero.

    This procedure accepts only polynomials, however if you are
    interested in solving recurrence with rational coefficients
    then use ``rsolve`` which will pre-process the given equation
    and run this procedure with polynomial arguments.

    The algorithm performs two basic steps:

        (1) Compute polynomial `v(n)` which can be used as universal
            denominator of any rational solution of equation
            `\operatorname{L} y = f`.

        (2) Construct new linear difference equation by substitution
            `y(n) = u(n)/v(n)` and solve it for `u(n)` finding all its
            polynomial solutions. Return ``None`` if none were found.

    The algorithm implemented here is a revised version of the original
    Abramov's algorithm, developed in 1989. The new approach is much
    simpler to implement and has better overall efficiency. This
    method can be easily adapted to the q-difference equations case.

    Besides finding rational solutions alone, this functions is
    an important part of Hyper algorithm where it is used to find
    a particular solution for the inhomogeneous part of a recurrence.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.solvers.recurr import rsolve_ratio
    >>> rsolve_ratio([-2*x**3 + x**2 + 2*x - 1, 2*x**3 + x**2 - 6*x,
    ... - 2*x**3 - 11*x**2 - 18*x - 9, 2*x**3 + 13*x**2 + 22*x + 8], 0, x)
    C0*(2*x - 3)/(2*(x**2 - 1))

    References
    ==========

    .. [1] S. A. Abramov, Rational solutions of linear difference
           and q-difference equations with polynomial coefficients,
           in: T. Levelt, ed., Proc. ISSAC '95, ACM Press, New York,
           1995, 285-289

    See Also
    ========

    rsolve_hyper
    """
    ...

def rsolve_hyper(coeffs, f, n, **hints):
    r"""
    Given linear recurrence operator `\operatorname{L}` of order `k`
    with polynomial coefficients and inhomogeneous equation
    `\operatorname{L} y = f` we seek for all hypergeometric solutions
    over field `K` of characteristic zero.

    The inhomogeneous part can be either hypergeometric or a sum
    of a fixed number of pairwise dissimilar hypergeometric terms.

    The algorithm performs three basic steps:

        (1) Group together similar hypergeometric terms in the
            inhomogeneous part of `\operatorname{L} y = f`, and find
            particular solution using Abramov's algorithm.

        (2) Compute generating set of `\operatorname{L}` and find basis
            in it, so that all solutions are linearly independent.

        (3) Form final solution with the number of arbitrary
            constants equal to dimension of basis of `\operatorname{L}`.

    Term `a(n)` is hypergeometric if it is annihilated by first order
    linear difference equations with polynomial coefficients or, in
    simpler words, if consecutive term ratio is a rational function.

    The output of this procedure is a linear combination of fixed
    number of hypergeometric terms. However the underlying method
    can generate larger class of solutions - D'Alembertian terms.

    Note also that this method not only computes the kernel of the
    inhomogeneous equation, but also reduces in to a basis so that
    solutions generated by this procedure are linearly independent

    Examples
    ========

    >>> from sympy.solvers import rsolve_hyper
    >>> from sympy.abc import x

    >>> rsolve_hyper([-1, -1, 1], 0, x)
    C0*(1/2 - sqrt(5)/2)**x + C1*(1/2 + sqrt(5)/2)**x

    >>> rsolve_hyper([-1, 1], 1 + x, x)
    C0 + x*(x + 1)/2

    References
    ==========

    .. [1] M. Petkovsek, Hypergeometric solutions of linear recurrences
           with polynomial coefficients, J. Symbolic Computation,
           14 (1992), 243-264.

    .. [2] M. Petkovsek, H. S. Wilf, D. Zeilberger, A = B, 1996.
    """
    ...

def rsolve(f, y, init=...):
    r"""
    Solve univariate recurrence with rational coefficients.

    Given `k`-th order linear recurrence `\operatorname{L} y = f`,
    or equivalently:

    .. math:: a_{k}(n) y(n+k) + a_{k-1}(n) y(n+k-1) +
              \cdots + a_{0}(n) y(n) = f(n)

    where `a_{i}(n)`, for `i=0, \ldots, k`, are polynomials or rational
    functions in `n`, and `f` is a hypergeometric function or a sum
    of a fixed number of pairwise dissimilar hypergeometric terms in
    `n`, finds all solutions or returns ``None``, if none were found.

    Initial conditions can be given as a dictionary in two forms:

        (1) ``{  n_0  : v_0,   n_1  : v_1, ...,   n_m  : v_m}``
        (2) ``{y(n_0) : v_0, y(n_1) : v_1, ..., y(n_m) : v_m}``

    or as a list ``L`` of values:

        ``L = [v_0, v_1, ..., v_m]``

    where ``L[i] = v_i``, for `i=0, \ldots, m`, maps to `y(n_i)`.

    Examples
    ========

    Lets consider the following recurrence:

    .. math:: (n - 1) y(n + 2) - (n^2 + 3 n - 2) y(n + 1) +
              2 n (n + 1) y(n) = 0

    >>> from sympy import Function, rsolve
    >>> from sympy.abc import n
    >>> y = Function('y')

    >>> f = (n - 1)*y(n + 2) - (n**2 + 3*n - 2)*y(n + 1) + 2*n*(n + 1)*y(n)

    >>> rsolve(f, y(n))
    2**n*C0 + C1*factorial(n)

    >>> rsolve(f, y(n), {y(0):0, y(1):3})
    3*2**n - 3*factorial(n)

    See Also
    ========

    rsolve_poly, rsolve_ratio, rsolve_hyper

    """
    ...

