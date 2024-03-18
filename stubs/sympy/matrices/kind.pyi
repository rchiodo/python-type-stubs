from typing import Self
from sympy.core.kind import Kind, _NumberKind
from sympy.core.mul import Mul

class MatrixKind(Kind):
    """
    Kind for all matrices in SymPy.

    Basic class for this kind is ``MatrixBase`` and ``MatrixExpr``,
    but any expression representing the matrix can have this.

    Parameters
    ==========

    element_kind : Kind
        Kind of the element. Default is
        :class:`sympy.core.kind.NumberKind`,
        which means that the matrix contains only numbers.

    Examples
    ========

    Any instance of matrix class has kind ``MatrixKind``:

    >>> from sympy import MatrixSymbol
    >>> A = MatrixSymbol('A', 2, 2)
    >>> A.kind
    MatrixKind(NumberKind)

    An expression representing a matrix may not be an instance of
    the Matrix class, but it will have kind ``MatrixKind``:

    >>> from sympy import MatrixExpr, Integral
    >>> from sympy.abc import x
    >>> intM = Integral(A, x)
    >>> isinstance(intM, MatrixExpr)
    False
    >>> intM.kind
    MatrixKind(NumberKind)

    Use ``isinstance()`` to check for ``MatrixKind`` without specifying the
    element kind. Use ``is`` to check the kind including the element kind:

    >>> from sympy import Matrix
    >>> from sympy.core import NumberKind
    >>> from sympy.matrices import MatrixKind
    >>> M = Matrix([1, 2])
    >>> isinstance(M.kind, MatrixKind)
    True
    >>> M.kind is MatrixKind(NumberKind)
    True

    See Also
    ========

    sympy.core.kind.NumberKind
    sympy.core.kind.UndefinedKind
    sympy.core.containers.TupleKind
    sympy.sets.sets.SetKind

    """
    def __new__(cls, element_kind=...) -> Self:
        ...
    
    def __repr__(self):
        ...
    


@Mul._kind_dispatcher.register(_NumberKind, MatrixKind)
def num_mat_mul(k1, k2) -> MatrixKind:
    """
    Return MatrixKind. The element kind is selected by recursive dispatching.
    Do not need to dispatch in reversed order because KindDispatcher
    searches for this automatically.
    """
    ...

@Mul._kind_dispatcher.register(MatrixKind, MatrixKind)
def mat_mat_mul(k1, k2) -> MatrixKind:
    """
    Return MatrixKind. The element kind is selected by recursive dispatching.
    """
    ...

