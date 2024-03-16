from typing import Any
from sympy.concrete.summations import Sum
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.relational import Equality, Ne, Relational
from sympy.functions.elementary.piecewise import Piecewise

"""
This module implements sums and products containing the Kronecker Delta function.

References
==========

.. [1] https://mathworld.wolfram.com/KroneckerDelta.html

"""
@cacheit
def deltaproduct(f, limit) -> Equality | Relational | Ne | Any:
    """
    Handle products containing a KroneckerDelta.

    See Also
    ========

    deltasummation
    sympy.functions.special.tensor_functions.KroneckerDelta
    sympy.concrete.products.product
    """
    ...

@cacheit
def deltasummation(f, limit, no_piecewise=...) -> Equality | Relational | Ne | Basic | Piecewise | Sum:
    """
    Handle summations containing a KroneckerDelta.

    Explanation
    ===========

    The idea for summation is the following:

    - If we are dealing with a KroneckerDelta expression, i.e. KroneckerDelta(g(x), j),
      we try to simplify it.

      If we could simplify it, then we sum the resulting expression.
      We already know we can sum a simplified expression, because only
      simple KroneckerDelta expressions are involved.

      If we could not simplify it, there are two cases:

      1) The expression is a simple expression: we return the summation,
         taking care if we are dealing with a Derivative or with a proper
         KroneckerDelta.

      2) The expression is not simple (i.e. KroneckerDelta(cos(x))): we can do
         nothing at all.

    - If the expr is a multiplication expr having a KroneckerDelta term:

      First we expand it.

      If the expansion did work, then we try to sum the expansion.

      If not, we try to extract a simple KroneckerDelta term, then we have two
      cases:

      1) We have a simple KroneckerDelta term, so we return the summation.

      2) We did not have a simple term, but we do have an expression with
         simplified KroneckerDelta terms, so we sum this expression.

    Examples
    ========

    >>> from sympy import oo, symbols
    >>> from sympy.abc import k
    >>> i, j = symbols('i, j', integer=True, finite=True)
    >>> from sympy.concrete.delta import deltasummation
    >>> from sympy import KroneckerDelta
    >>> deltasummation(KroneckerDelta(i, k), (k, -oo, oo))
    1
    >>> deltasummation(KroneckerDelta(i, k), (k, 0, oo))
    Piecewise((1, i >= 0), (0, True))
    >>> deltasummation(KroneckerDelta(i, k), (k, 1, 3))
    Piecewise((1, (i >= 1) & (i <= 3)), (0, True))
    >>> deltasummation(k*KroneckerDelta(i, j)*KroneckerDelta(j, k), (k, -oo, oo))
    j*KroneckerDelta(i, j)
    >>> deltasummation(j*KroneckerDelta(i, j), (j, -oo, oo))
    i
    >>> deltasummation(i*KroneckerDelta(i, j), (i, -oo, oo))
    j

    See Also
    ========

    deltaproduct
    sympy.functions.special.tensor_functions.KroneckerDelta
    sympy.concrete.sums.summation
    """
    ...

