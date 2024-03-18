from typing import Any, Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import Identity, OneMatrix, ZeroMatrix

class PermutationMatrix(MatrixExpr):
    """A Permutation Matrix

    Parameters
    ==========

    perm : Permutation
        The permutation the matrix uses.

        The size of the permutation determines the matrix size.

        See the documentation of
        :class:`sympy.combinatorics.permutations.Permutation` for
        the further information of how to create a permutation object.

    Examples
    ========

    >>> from sympy import Matrix, PermutationMatrix
    >>> from sympy.combinatorics import Permutation

    Creating a permutation matrix:

    >>> p = Permutation(1, 2, 0)
    >>> P = PermutationMatrix(p)
    >>> P = P.as_explicit()
    >>> P
    Matrix([
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]])

    Permuting a matrix row and column:

    >>> M = Matrix([0, 1, 2])
    >>> Matrix(P*M)
    Matrix([
    [1],
    [2],
    [0]])

    >>> Matrix(M.T*P)
    Matrix([[2, 0, 1]])

    See Also
    ========

    sympy.combinatorics.permutations.Permutation
    """
    def __new__(cls, perm) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    @property
    def is_Identity(self):
        ...
    
    def doit(self, **hints) -> Identity | Self:
        ...
    
    _eval_adjoint = ...


class MatrixPermute(MatrixExpr):
    r"""Symbolic representation for permuting matrix rows or columns.

    Parameters
    ==========

    perm : Permutation, PermutationMatrix
        The permutation to use for permuting the matrix.
        The permutation can be resized to the suitable one,

    axis : 0 or 1
        The axis to permute alongside.
        If `0`, it will permute the matrix rows.
        If `1`, it will permute the matrix columns.

    Notes
    =====

    This follows the same notation used in
    :meth:`sympy.matrices.matrixbase.MatrixBase.permute`.

    Examples
    ========

    >>> from sympy import Matrix, MatrixPermute
    >>> from sympy.combinatorics import Permutation

    Permuting the matrix rows:

    >>> p = Permutation(1, 2, 0)
    >>> A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> B = MatrixPermute(A, p, axis=0)
    >>> B.as_explicit()
    Matrix([
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3]])

    Permuting the matrix columns:

    >>> B = MatrixPermute(A, p, axis=1)
    >>> B.as_explicit()
    Matrix([
    [2, 3, 1],
    [5, 6, 4],
    [8, 9, 7]])

    See Also
    ========

    sympy.matrices.matrixbase.MatrixBase.permute
    """
    def __new__(cls, mat, perm, axis=...) -> Self:
        ...
    
    def doit(self, deep=..., **hints) -> Basic | PermutationMatrix | ZeroMatrix | OneMatrix | MatrixPermute | Self:
        ...
    
    @property
    def shape(self):
        ...
    


