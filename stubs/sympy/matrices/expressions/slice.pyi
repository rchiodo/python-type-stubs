from typing import Any, Literal, Self
from sympy.core.function import UndefinedFunction
from sympy.matrices.expressions.matexpr import MatrixExpr

def normalize(i, parentsize) -> tuple[Any | Literal[0], Any, Any | Literal[1]]:
    ...

class MatrixSlice(MatrixExpr):
    """ A MatrixSlice of a Matrix Expression

    Examples
    ========

    >>> from sympy import MatrixSlice, ImmutableMatrix
    >>> M = ImmutableMatrix(4, 4, range(16))
    >>> M
    Matrix([
    [ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11],
    [12, 13, 14, 15]])

    >>> B = MatrixSlice(M, (0, 2), (2, 4))
    >>> ImmutableMatrix(B)
    Matrix([
    [2, 3],
    [6, 7]])
    """
    parent = ...
    rowslice = ...
    colslice = ...
    def __new__(cls, parent, rowslice, colslice) -> MatrixSlice | Self:
        ...
    
    @property
    def shape(self) -> tuple[Any | type[UndefinedFunction], Any | type[UndefinedFunction]]:
        ...
    
    @property
    def on_diag(self) -> Any:
        ...
    


def slice_of_slice(s, t) -> tuple[Any, Any, Any]:
    ...

def mat_slice_of_slice(parent, rowslice, colslice) -> MatrixSlice:
    """ Collapse nested matrix slices

    >>> from sympy import MatrixSymbol
    >>> X = MatrixSymbol('X', 10, 10)
    >>> X[:, 1:5][5:8, :]
    X[5:8, 1:5]
    >>> X[1:9:2, 2:6][1:3, 2]
    X[3:7:2, 4:5]
    """
    ...

