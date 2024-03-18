from typing import Any, Self
from sympy.core.expr import Expr
from sympy.matrices.expressions import MatrixExpr
from sympy.matrices.matrixbase import MatrixBase

class DiagonalMatrix(MatrixExpr):
    """DiagonalMatrix(M) will create a matrix expression that
    behaves as though all off-diagonal elements,
    `M[i, j]` where `i != j`, are zero.

    Examples
    ========

    >>> from sympy import MatrixSymbol, DiagonalMatrix, Symbol
    >>> n = Symbol('n', integer=True)
    >>> m = Symbol('m', integer=True)
    >>> D = DiagonalMatrix(MatrixSymbol('x', 2, 3))
    >>> D[1, 2]
    0
    >>> D[1, 1]
    x[1, 1]

    The length of the diagonal -- the lesser of the two dimensions of `M` --
    is accessed through the `diagonal_length` property:

    >>> D.diagonal_length
    2
    >>> DiagonalMatrix(MatrixSymbol('x', n + 1, n)).diagonal_length
    n

    When one of the dimensions is symbolic the other will be treated as
    though it is smaller:

    >>> tall = DiagonalMatrix(MatrixSymbol('x', n, 3))
    >>> tall.diagonal_length
    3
    >>> tall[10, 1]
    0

    When the size of the diagonal is not known, a value of None will
    be returned:

    >>> DiagonalMatrix(MatrixSymbol('x', n, m)).diagonal_length is None
    True

    """
    arg = ...
    shape = ...
    @property
    def diagonal_length(self) -> Expr | None:
        ...
    


class DiagonalOf(MatrixExpr):
    """DiagonalOf(M) will create a matrix expression that
    is equivalent to the diagonal of `M`, represented as
    a single column matrix.

    Examples
    ========

    >>> from sympy import MatrixSymbol, DiagonalOf, Symbol
    >>> n = Symbol('n', integer=True)
    >>> m = Symbol('m', integer=True)
    >>> x = MatrixSymbol('x', 2, 3)
    >>> diag = DiagonalOf(x)
    >>> diag.shape
    (2, 1)

    The diagonal can be addressed like a matrix or vector and will
    return the corresponding element of the original matrix:

    >>> diag[1, 0] == diag[1] == x[1, 1]
    True

    The length of the diagonal -- the lesser of the two dimensions of `M` --
    is accessed through the `diagonal_length` property:

    >>> diag.diagonal_length
    2
    >>> DiagonalOf(MatrixSymbol('x', n + 1, n)).diagonal_length
    n

    When only one of the dimensions is symbolic the other will be
    treated as though it is smaller:

    >>> dtall = DiagonalOf(MatrixSymbol('x', n, 3))
    >>> dtall.diagonal_length
    3

    When the size of the diagonal is not known, a value of None will
    be returned:

    >>> DiagonalOf(MatrixSymbol('x', n, m)).diagonal_length is None
    True

    """
    arg = ...
    @property
    def shape(self) -> tuple[Any | None, Any]:
        ...
    
    @property
    def diagonal_length(self) -> Any | None:
        ...
    


class DiagMatrix(MatrixExpr):
    """
    Turn a vector into a diagonal matrix.
    """
    def __new__(cls, vector) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def as_explicit(self):
        ...
    
    def doit(self, **hints) -> MatrixBase | DiagMatrix:
        ...
    


def diagonalize_vector(vector) -> MatrixBase | DiagMatrix:
    ...

