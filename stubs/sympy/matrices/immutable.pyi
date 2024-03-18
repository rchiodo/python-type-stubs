from typing import Any, Self
from sympy.matrices.dense import DenseMatrix
from sympy.matrices.expressions import MatrixExpr
from sympy.matrices.repmatrix import RepMatrix
from sympy.matrices.sparse import SparseRepMatrix

def sympify_matrix(arg):
    ...

def sympify_mpmath_matrix(arg) -> ImmutableDenseMatrix:
    ...

class ImmutableRepMatrix(RepMatrix, MatrixExpr):
    """Immutable matrix based on RepMatrix

    Uses DomainMAtrix as the internal representation.
    """
    def __new__(cls, *args, **kwargs):
        ...
    
    __hash__ = ...
    def copy(self) -> Self:
        ...
    
    @property
    def cols(self):
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def as_immutable(self) -> Self:
        ...
    
    def __setitem__(self, *args):
        ...
    
    def is_diagonalizable(self, reals_only=..., **kwargs) -> bool:
        ...
    
    is_diagonalizable = ...


class ImmutableDenseMatrix(DenseMatrix, ImmutableRepMatrix):
    """Create an immutable version of a matrix.

    Examples
    ========

    >>> from sympy import eye, ImmutableMatrix
    >>> ImmutableMatrix(eye(3))
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> _[0, 0] = 42
    Traceback (most recent call last):
    ...
    TypeError: Cannot set values of ImmutableDenseMatrix
    """
    _iterable = ...
    _class_priority = ...
    _op_priority = ...


ImmutableMatrix = ImmutableDenseMatrix
class ImmutableSparseMatrix(SparseRepMatrix, ImmutableRepMatrix):
    """Create an immutable version of a sparse matrix.

    Examples
    ========

    >>> from sympy import eye, ImmutableSparseMatrix
    >>> ImmutableSparseMatrix(1, 1, {})
    Matrix([[0]])
    >>> ImmutableSparseMatrix(eye(3))
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> _[0, 0] = 42
    Traceback (most recent call last):
    ...
    TypeError: Cannot set values of ImmutableSparseMatrix
    >>> _.shape
    (3, 3)
    """
    is_Matrix = ...
    _class_priority = ...


