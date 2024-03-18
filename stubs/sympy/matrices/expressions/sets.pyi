from typing import Self
from sympy.core.basic import Basic
from sympy.sets.sets import Set

class MatrixSet(Set):
    """
    MatrixSet represents the set of matrices with ``shape = (n, m)`` over the
    given set.

    Examples
    ========

    >>> from sympy.matrices import MatrixSet
    >>> from sympy import S, I, Matrix
    >>> M = MatrixSet(2, 2, set=S.Reals)
    >>> X = Matrix([[1, 2], [3, 4]])
    >>> X in M
    True
    >>> X = Matrix([[1, 2], [I, 4]])
    >>> X in M
    False

    """
    is_empty = ...
    def __new__(cls, n, m, set) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def set(self) -> Basic:
        ...
    


