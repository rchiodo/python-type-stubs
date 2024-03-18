"""Tools for solving inequalities and systems of inequalities. """
from typing import Any
from sympy.core.logic import And
from sympy.sets.sets import FiniteSet, Union


def solve_poly_inequality(poly, rel) -> list[Any]:
    """Solve a polynomial inequality with rational coefficients.

    Examples
    ========

    >>> from sympy import solve_poly_inequality, Poly
    >>> from sympy.abc import x

    >>> solve_poly_inequality(Poly(x, x, domain='ZZ'), '==')
    [{0}]

    >>> solve_poly_inequality(Poly(x**2 - 1, x, domain='ZZ'), '!=')
    [Interval.open(-oo, -1), Interval.open(-1, 1), Interval.open(1, oo)]

    >>> solve_poly_inequality(Poly(x**2 - 1, x, domain='ZZ'), '==')
    [{-1}, {1}]

    See Also
    ========
    solve_poly_inequalities
    """
    ...

def solve_poly_inequalities(polys) -> FiniteSet | Union:
    """Solve polynomial inequalities with rational coefficients.

    Examples
    ========

    >>> from sympy import Poly
    >>> from sympy.solvers.inequalities import solve_poly_inequalities
    >>> from sympy.abc import x
    >>> solve_poly_inequalities(((
    ... Poly(x**2 - 3), ">"), (
    ... Poly(-x**2 + 1), ">")))
    Union(Interval.open(-oo, -sqrt(3)), Interval.open(-1, 1), Interval.open(sqrt(3), oo))
    """
    ...

def solve_rational_inequalities(eqs):
    """Solve a system of rational inequalities with rational coefficients.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy import solve_rational_inequalities, Poly

    >>> solve_rational_inequalities([[
    ... ((Poly(-x + 1), Poly(1, x)), '>='),
    ... ((Poly(-x + 1), Poly(1, x)), '<=')]])
    {1}

    >>> solve_rational_inequalities([[
    ... ((Poly(x), Poly(1, x)), '!='),
    ... ((Poly(-x + 1), Poly(1, x)), '>=')]])
    Union(Interval.open(-oo, 0), Interval.Lopen(0, 1))

    See Also
    ========
    solve_poly_inequality
    """
    ...

def reduce_rational_inequalities(exprs, gen, relational=...):
    """Reduce a system of rational inequalities with rational coefficients.

    Examples
    ========

    >>> from sympy import Symbol
    >>> from sympy.solvers.inequalities import reduce_rational_inequalities

    >>> x = Symbol('x', real=True)

    >>> reduce_rational_inequalities([[x**2 <= 0]], x)
    Eq(x, 0)

    >>> reduce_rational_inequalities([[x + 2 > 0]], x)
    -2 < x
    >>> reduce_rational_inequalities([[(x + 2, ">")]], x)
    -2 < x
    >>> reduce_rational_inequalities([[x + 2]], x)
    Eq(x, -2)

    This function find the non-infinite solution set so if the unknown symbol
    is declared as extended real rather than real then the result may include
    finiteness conditions:

    >>> y = Symbol('y', extended_real=True)
    >>> reduce_rational_inequalities([[y + 2 > 0]], y)
    (-2 < y) & (y < oo)
    """
    ...

def reduce_abs_inequality(expr, rel, gen):
    """Reduce an inequality with nested absolute values.

    Examples
    ========

    >>> from sympy import reduce_abs_inequality, Abs, Symbol
    >>> x = Symbol('x', real=True)

    >>> reduce_abs_inequality(Abs(x - 5) - 3, '<', x)
    (2 < x) & (x < 8)

    >>> reduce_abs_inequality(Abs(x + 2)*3 - 13, '<', x)
    (-19/3 < x) & (x < 7/3)

    See Also
    ========

    reduce_abs_inequalities
    """
    ...

def reduce_abs_inequalities(exprs, gen) -> And:
    """Reduce a system of inequalities with nested absolute values.

    Examples
    ========

    >>> from sympy import reduce_abs_inequalities, Abs, Symbol
    >>> x = Symbol('x', extended_real=True)

    >>> reduce_abs_inequalities([(Abs(3*x - 5) - 7, '<'),
    ... (Abs(x + 25) - 13, '>')], x)
    (-2/3 < x) & (x < 4) & (((-oo < x) & (x < -38)) | ((-12 < x) & (x < oo)))

    >>> reduce_abs_inequalities([(Abs(x - 4) + Abs(3*x - 5) - 7, '<')], x)
    (1/2 < x) & (x < 4)

    See Also
    ========

    reduce_abs_inequality
    """
    ...

def solve_univariate_inequality(expr, gen, relational=..., domain=..., continuous=...):
    """Solves a real univariate inequality.

    Parameters
    ==========

    expr : Relational
        The target inequality
    gen : Symbol
        The variable for which the inequality is solved
    relational : bool
        A Relational type output is expected or not
    domain : Set
        The domain over which the equation is solved
    continuous: bool
        True if expr is known to be continuous over the given domain
        (and so continuous_domain() does not need to be called on it)

    Raises
    ======

    NotImplementedError
        The solution of the inequality cannot be determined due to limitation
        in :func:`sympy.solvers.solveset.solvify`.

    Notes
    =====

    Currently, we cannot solve all the inequalities due to limitations in
    :func:`sympy.solvers.solveset.solvify`. Also, the solution returned for trigonometric inequalities
    are restricted in its periodic interval.

    See Also
    ========

    sympy.solvers.solveset.solvify: solver returning solveset solutions with solve's output API

    Examples
    ========

    >>> from sympy import solve_univariate_inequality, Symbol, sin, Interval, S
    >>> x = Symbol('x')

    >>> solve_univariate_inequality(x**2 >= 4, x)
    ((2 <= x) & (x < oo)) | ((-oo < x) & (x <= -2))

    >>> solve_univariate_inequality(x**2 >= 4, x, relational=False)
    Union(Interval(-oo, -2), Interval(2, oo))

    >>> domain = Interval(0, S.Infinity)
    >>> solve_univariate_inequality(x**2 >= 4, x, False, domain)
    Interval(2, oo)

    >>> solve_univariate_inequality(sin(x) > 0, x, relational=False)
    Interval.open(0, pi)

    """
    ...

def reduce_inequalities(inequalities, symbols=...) -> And:
    """Reduce a system of inequalities with rational coefficients.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy import reduce_inequalities

    >>> reduce_inequalities(0 <= x + 3, [])
    (-3 <= x) & (x < oo)

    >>> reduce_inequalities(0 <= x + y*2 - 1, [x])
    (x < oo) & (x >= 1 - 2*y)
    """
    ...

