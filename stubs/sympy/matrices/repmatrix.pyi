from typing import Any, Self
from sympy.matrices.dense import MutableDenseMatrix
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.polys.matrices import DomainMatrix
from sympy.matrices.matrixbase import MatrixBase
from sympy.matrices.kind import MatrixKind

class RepMatrix(MatrixBase):
    """Matrix implementation based on DomainMatrix as an internal representation.

    The RepMatrix class is a superclass for Matrix, ImmutableMatrix,
    SparseMatrix and ImmutableSparseMatrix which are the main usable matrix
    classes in SymPy. Most methods on this class are simply forwarded to
    DomainMatrix.
    """
    _rep: DomainMatrix
    def __eq__(self, other) -> bool:
        ...
    
    def to_DM(self, domain=..., **kwargs) -> DomainMatrix:
        """Convert to a :class:`~.DomainMatrix`.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2], [3, 4]])
        >>> M.to_DM()
        DomainMatrix({0: {0: 1, 1: 2}, 1: {0: 3, 1: 4}}, (2, 2), ZZ)

        The :meth:`DomainMatrix.to_Matrix` method can be used to convert back:

        >>> M.to_DM().to_Matrix() == M
        True

        The domain can be given explicitly or otherwise it will be chosen by
        :func:`construct_domain`. Any keyword arguments (besides ``domain``)
        are passed to :func:`construct_domain`:

        >>> from sympy import QQ, symbols
        >>> x = symbols('x')
        >>> M = Matrix([[x, 1], [1, x]])
        >>> M
        Matrix([
        [x, 1],
        [1, x]])
        >>> M.to_DM().domain
        ZZ[x]
        >>> M.to_DM(field=True).domain
        ZZ(x)
        >>> M.to_DM(domain=QQ[x]).domain
        QQ[x]

        See Also
        ========

        DomainMatrix
        DomainMatrix.to_Matrix
        DomainMatrix.convert_to
        DomainMatrix.choose_domain
        construct_domain
        """
        ...
    
    def flat(self) -> list[Any]:
        ...
    
    def copy(self):
        ...
    
    @property
    def kind(self) -> MatrixKind:
        ...
    
    def __getitem__(self, key) -> MatrixElement | list[Any]:
        ...
    
    def equals(self, other, failing_expression=...) -> bool:
        """Applies ``equals`` to corresponding elements of the matrices,
        trying to prove that the elements are equivalent, returning True
        if they are, False if any pair is not, and None (or the first
        failing expression if failing_expression is True) if it cannot
        be decided if the expressions are equivalent or not. This is, in
        general, an expensive operation.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x
        >>> A = Matrix([x*(x - 1), 0])
        >>> B = Matrix([x**2 - x, 0])
        >>> A == B
        False
        >>> A.simplify() == B.simplify()
        True
        >>> A.equals(B)
        True
        >>> A.equals(2)
        False

        See Also
        ========
        sympy.core.expr.Expr.equals
        """
        ...
    
    def inv_mod(M, m) -> MutableDenseMatrix:
        r"""
        Returns the inverse of the integer matrix ``M`` modulo ``m``.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.inv_mod(5)
        Matrix([
        [3, 1],
        [4, 2]])
        >>> A.inv_mod(3)
        Matrix([
        [1, 1],
        [0, 1]])

        """
        ...
    
    def lll(self, delta=...):
        """LLL-reduced basis for the rowspace of a matrix of integers.

        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm.

        The implementation is provided by :class:`~DomainMatrix`. See
        :meth:`~DomainMatrix.lll` for more details.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 0, 0, 0, -20160],
        ...             [0, 1, 0, 0, 33768],
        ...             [0, 0, 1, 0, 39578],
        ...             [0, 0, 0, 1, 47757]])
        >>> M.lll()
        Matrix([
        [ 10, -3,  -2,  8,  -4],
        [  3, -9,   8,  1, -11],
        [ -3, 13,  -9, -3,  -9],
        [-12, -7, -11,  9,  -1]])

        See Also
        ========

        lll_transform
        sympy.polys.matrices.domainmatrix.DomainMatrix.lll
        """
        ...
    
    def lll_transform(self, delta=...) -> tuple[Any, Any]:
        """LLL-reduced basis and transformation matrix.

        Performs the Lenstra–Lenstra–Lovász (LLL) basis reduction algorithm.

        The implementation is provided by :class:`~DomainMatrix`. See
        :meth:`~DomainMatrix.lll_transform` for more details.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 0, 0, 0, -20160],
        ...             [0, 1, 0, 0, 33768],
        ...             [0, 0, 1, 0, 39578],
        ...             [0, 0, 0, 1, 47757]])
        >>> B, T = M.lll_transform()
        >>> B
        Matrix([
        [ 10, -3,  -2,  8,  -4],
        [  3, -9,   8,  1, -11],
        [ -3, 13,  -9, -3,  -9],
        [-12, -7, -11,  9,  -1]])
        >>> T
        Matrix([
        [ 10, -3,  -2,  8],
        [  3, -9,   8,  1],
        [ -3, 13,  -9, -3],
        [-12, -7, -11,  9]])

        The transformation matrix maps the original basis to the LLL-reduced
        basis:

        >>> T * M == B
        True

        See Also
        ========

        lll
        sympy.polys.matrices.domainmatrix.DomainMatrix.lll_transform
        """
        ...
    


class MutableRepMatrix(RepMatrix):
    """Mutable matrix based on DomainMatrix as the internal representation"""
    is_zero = ...
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    def copy(self) -> Self:
        ...
    
    def as_mutable(self) -> Self:
        ...
    
    def __setitem__(self, key, value) -> None:
        """

        Examples
        ========

        >>> from sympy import Matrix, I, zeros, ones
        >>> m = Matrix(((1, 2+I), (3, 4)))
        >>> m
        Matrix([
        [1, 2 + I],
        [3,     4]])
        >>> m[1, 0] = 9
        >>> m
        Matrix([
        [1, 2 + I],
        [9,     4]])
        >>> m[1, 0] = [[0, 1]]

        To replace row r you assign to position r*m where m
        is the number of columns:

        >>> M = zeros(4)
        >>> m = M.cols
        >>> M[3*m] = ones(1, m)*2; M
        Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 2]])

        And to replace column c you can assign to position c:

        >>> M[2] = ones(m, 1)*4; M
        Matrix([
        [0, 0, 4, 0],
        [0, 0, 4, 0],
        [0, 0, 4, 0],
        [2, 2, 4, 2]])
        """
        ...
    
    def col_op(self, j, f) -> None:
        """In-place operation on col j using two-arg functor whose args are
        interpreted as (self[i, j], i).

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.col_op(1, lambda v, i: v + 2*M[i, 0]); M
        Matrix([
        [1, 2, 0],
        [0, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        col
        row_op
        """
        ...
    
    def col_swap(self, i, j) -> None:
        """Swap the two given columns of the matrix in-place.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 0], [1, 0]])
        >>> M
        Matrix([
        [1, 0],
        [1, 0]])
        >>> M.col_swap(0, 1)
        >>> M
        Matrix([
        [0, 1],
        [0, 1]])

        See Also
        ========

        col
        row_swap
        """
        ...
    
    def row_op(self, i, f) -> None:
        """In-place operation on row ``i`` using two-arg functor whose args are
        interpreted as ``(self[i, j], j)``.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.row_op(1, lambda v, j: v + 2*M[0, j]); M
        Matrix([
        [1, 0, 0],
        [2, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        row
        zip_row_op
        col_op

        """
        ...
    
    def row_mult(self, i, factor) -> None:
        """Multiply the given row by the given factor in-place.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.row_mult(1,7); M
        Matrix([
        [1, 0, 0],
        [0, 7, 0],
        [0, 0, 1]])

        """
        ...
    
    def row_add(self, s, t, k) -> None:
        """Add k times row s (source) to row t (target) in place.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.row_add(0, 2,3); M
        Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [3, 0, 1]])
        """
        ...
    
    def row_swap(self, i, j) -> None:
        """Swap the two given rows of the matrix in-place.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[0, 1], [1, 0]])
        >>> M
        Matrix([
        [0, 1],
        [1, 0]])
        >>> M.row_swap(0, 1)
        >>> M
        Matrix([
        [1, 0],
        [0, 1]])

        See Also
        ========

        row
        col_swap
        """
        ...
    
    def zip_row_op(self, i, k, f) -> None:
        """In-place operation on row ``i`` using two-arg functor whose args are
        interpreted as ``(self[i, j], self[k, j])``.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.zip_row_op(1, 0, lambda v, u: v + 2*u); M
        Matrix([
        [1, 0, 0],
        [2, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        row
        row_op
        col_op

        """
        ...
    
    def copyin_list(self, key, value) -> None:
        """Copy in elements from a list.

        Parameters
        ==========

        key : slice
            The section of this matrix to replace.
        value : iterable
            The iterable to copy values from.

        Examples
        ========

        >>> from sympy import eye
        >>> I = eye(3)
        >>> I[:2, 0] = [1, 2] # col
        >>> I
        Matrix([
        [1, 0, 0],
        [2, 1, 0],
        [0, 0, 1]])
        >>> I[1, :2] = [[3, 4]]
        >>> I
        Matrix([
        [1, 0, 0],
        [3, 4, 0],
        [0, 0, 1]])

        See Also
        ========

        copyin_matrix
        """
        ...
    
    def copyin_matrix(self, key, value) -> None:
        """Copy in values from a matrix into the given bounds.

        Parameters
        ==========

        key : slice
            The section of this matrix to replace.
        value : Matrix
            The matrix to copy values from.

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> M = Matrix([[0, 1], [2, 3], [4, 5]])
        >>> I = eye(3)
        >>> I[:3, :2] = M
        >>> I
        Matrix([
        [0, 1, 0],
        [2, 3, 0],
        [4, 5, 1]])
        >>> I[0, 1] = M
        >>> I
        Matrix([
        [0, 0, 1],
        [2, 2, 3],
        [4, 4, 5]])

        See Also
        ========

        copyin_list
        """
        ...
    
    def fill(self, value) -> None:
        """Fill self with the given value.

        Notes
        =====

        Unless many values are going to be deleted (i.e. set to zero)
        this will create a matrix that is slower than a dense matrix in
        operations.

        Examples
        ========

        >>> from sympy import SparseMatrix
        >>> M = SparseMatrix.zeros(3); M
        Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]])
        >>> M.fill(1); M
        Matrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]])

        See Also
        ========

        zeros
        ones
        """
        ...
    


