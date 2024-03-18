from typing import Any

from sympy.concrete.products import Product
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.core.relational import Eq, Equality, Ne, Relational
from sympy.core.symbol import Dummy
from sympy.functions.elementary.complexes import Abs
from sympy.series.order import Order


def separatevars(expr, symbols=..., dict=..., force=...) -> dict[str, Any] | dict[Any, list[Any]] | Order | Abs | type[UndefinedFunction] | Any | None:
    ...

def posify(eq) -> tuple[Any, dict[Any, Any]] | tuple[Any, dict[Dummy, Any]]:
    ...

def hypersimp(f, k) -> None:
    ...

def hypersimilar(f, g, k):
    ...

def signsimp(expr, evaluate=...) -> Expr | Relational | Basic | Order | Eq | Ne | Add | tuple[Any, dict[Any, Any]]:
    ...

def simplify(expr, ratio=..., measure=..., rational=..., inverse=..., doit=..., **kwargs):
    ...

def sum_simplify(s, **kwargs) -> Order:
    ...

def sum_combine(s_t) -> Order:
    ...

def factor_sum(self, limits=..., radical=..., clear=..., fraction=..., sign=...) -> Basic | Any | Add | Order | Mul:
    ...

def sum_add(self, other, method=...) -> Basic | Any | Add | Order | Mul:
    ...

def product_simplify(s, **kwargs) -> Order:
    ...

def product_mul(self, other, method=...) -> Equality | Relational | Ne | Product | Order:
    ...

def logcombine(expr, force=...):
    ...

def inversecombine(expr):
    ...

def kroneckersimp(expr) -> None:
    ...

def besselsimp(expr):
    ...

def nthroot(expr, n, max_len=..., prec=...) -> Mul | Pow | Order | Add | None:
    ...

def nsimplify(expr, constants=..., tolerance=..., full=..., rational=..., rational_conversion=...):
    ...

def clear_coefficients(expr, rhs=...) -> tuple[Any, Any] | tuple[Any | Expr | Relational | Basic | Order | Eq | Ne | Add | tuple[Any, dict[Any, Any]], Any]:
    ...

def nc_simplify(expr, deep=...):
    '''
    Simplify a non-commutative expression composed of multiplication
    and raising to a power by grouping repeated subterms into one power.
    Priority is given to simplifications that give the fewest number
    of arguments in the end (for example, in a*b*a*b*c*a*b*c simplifying
    to (a*b)**2*c*a*b*c gives 5 arguments while a*b*(a*b*c)**2 has 3).
    If ``expr`` is a sum of such terms, the sum of the simplified terms
    is returned.

    Keyword argument ``deep`` controls whether or not subexpressions
    nested deeper inside the main expression are simplified. See examples
    below. Setting `deep` to `False` can save time on nested expressions
    that do not need simplifying on all levels.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.simplify.simplify import nc_simplify
    >>> a, b, c = symbols("a b c", commutative=False)
    >>> nc_simplify(a*b*a*b*c*a*b*c)
    a*b*(a*b*c)**2
    >>> expr = a**2*b*a**4*b*a**4
    >>> nc_simplify(expr)
    a**2*(b*a**4)**2
    >>> nc_simplify(a*b*a*b*c**2*(a*b)**2*c**2)
    ((a*b)**2*c**2)**2
    >>> nc_simplify(a*b*a*b + 2*a*c*a**2*c*a**2*c*a)
    (a*b)**2 + 2*(a*c*a)**3
    >>> nc_simplify(b**-1*a**-1*(a*b)**2)
    a*b
    >>> nc_simplify(a**-1*b**-1*c*a)
    (b*a)**(-1)*c*a
    >>> expr = (a*b*a*b)**2*a*c*a*c
    >>> nc_simplify(expr)
    (a*b)**4*(a*c)**2
    >>> nc_simplify(expr, deep=False)
    (a*b*a*b)**2*(a*c)**2

    '''
    ...

def dotprodsimp(expr, withsimp=...) -> tuple[Any | Basic, bool] | Any | Basic:
    ...

bottom_up = ...
walk = ...
