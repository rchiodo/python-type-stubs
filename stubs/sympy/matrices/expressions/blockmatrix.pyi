from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matadd import MatAdd
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.matpow import MatPow
from sympy.matrices.expressions.special import GenericIdentity, GenericZeroMatrix
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.series.order import Order

class BlockMatrix(MatrixExpr):
    """A BlockMatrix is a Matrix comprised of other matrices.

    The submatrices are stored in a SymPy Matrix object but accessed as part of
    a Matrix Expression

    >>> from sympy import (MatrixSymbol, BlockMatrix, symbols,
    ...     Identity, ZeroMatrix, block_collapse)
    >>> n,m,l = symbols('n m l')
    >>> X = MatrixSymbol('X', n, n)
    >>> Y = MatrixSymbol('Y', m, m)
    >>> Z = MatrixSymbol('Z', n, m)
    >>> B = BlockMatrix([[X, Z], [ZeroMatrix(m,n), Y]])
    >>> print(B)
    Matrix([
    [X, Z],
    [0, Y]])

    >>> C = BlockMatrix([[Identity(n), Z]])
    >>> print(C)
    Matrix([[I, Z]])

    >>> print(block_collapse(C*B))
    Matrix([[X, Z + Z*Y]])

    Some matrices might be comprised of rows of blocks with
    the matrices in each row having the same height and the
    rows all having the same total number of columns but
    not having the same number of columns for each matrix
    in each row. In this case, the matrix is not a block
    matrix and should be instantiated by Matrix.

    >>> from sympy import ones, Matrix
    >>> dat = [
    ... [ones(3,2), ones(3,3)*2],
    ... [ones(2,3)*3, ones(2,2)*4]]
    ...
    >>> BlockMatrix(dat)
    Traceback (most recent call last):
    ...
    ValueError:
    Although this matrix is comprised of blocks, the blocks do not fill
    the matrix in a size-symmetric fashion. To create a full matrix from
    these arguments, pass them directly to Matrix.
    >>> Matrix(dat)
    Matrix([
    [1, 1, 2, 2, 2],
    [1, 1, 2, 2, 2],
    [1, 1, 2, 2, 2],
    [3, 3, 3, 4, 4],
    [3, 3, 3, 4, 4]])

    See Also
    ========
    sympy.matrices.matrixbase.MatrixBase.irregular
    """
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Any | Literal[0], Any | Literal[0]]:
        ...
    
    @property
    def blockshape(self):
        ...
    
    @property
    def blocks(self) -> Basic:
        ...
    
    @property
    def rowblocksizes(self) -> list[Any]:
        ...
    
    @property
    def colblocksizes(self) -> list[Any]:
        ...
    
    def structurally_equal(self, other) -> bool:
        ...
    
    def transpose(self) -> BlockMatrix:
        """Return transpose of matrix.

        Examples
        ========

        >>> from sympy import MatrixSymbol, BlockMatrix, ZeroMatrix
        >>> from sympy.abc import m, n
        >>> X = MatrixSymbol('X', n, n)
        >>> Y = MatrixSymbol('Y', m, m)
        >>> Z = MatrixSymbol('Z', n, m)
        >>> B = BlockMatrix([[X, Z], [ZeroMatrix(m,n), Y]])
        >>> B.transpose()
        Matrix([
        [X.T,  0],
        [Z.T, Y.T]])
        >>> _.transpose()
        Matrix([
        [X, Z],
        [0, Y]])
        """
        ...
    
    def schur(self, mat=..., generalized=...) -> Self:
        """Return the Schur Complement of the 2x2 BlockMatrix

        Parameters
        ==========

        mat : String, optional
            The matrix with respect to which the
            Schur Complement is calculated. 'A' is
            used by default

        generalized : bool, optional
            If True, returns the generalized Schur
            Component which uses Moore-Penrose Inverse

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix
        >>> m, n = symbols('m n')
        >>> A = MatrixSymbol('A', n, n)
        >>> B = MatrixSymbol('B', n, m)
        >>> C = MatrixSymbol('C', m, n)
        >>> D = MatrixSymbol('D', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])

        The default Schur Complement is evaluated with "A"

        >>> X.schur()
        -C*A**(-1)*B + D
        >>> X.schur('D')
        A - B*D**(-1)*C

        Schur complement with non-invertible matrices is not
        defined. Instead, the generalized Schur complement can
        be calculated which uses the Moore-Penrose Inverse. To
        achieve this, `generalized` must be set to `True`

        >>> X.schur('B', generalized=True)
        C - D*(B.T*B)**(-1)*B.T*A
        >>> X.schur('C', generalized=True)
        -A*(C.T*C)**(-1)*C.T*D + B

        Returns
        =======

        M : Matrix
            The Schur Complement Matrix

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If given matrix is non-invertible

        References
        ==========

        .. [1] Wikipedia Article on Schur Component : https://en.wikipedia.org/wiki/Schur_complement

        See Also
        ========

        sympy.matrices.matrixbase.MatrixBase.pinv
        """
        ...
    
    def LDUdecomposition(self) -> tuple[BlockMatrix, BlockDiagMatrix, BlockMatrix]:
        """Returns the Block LDU decomposition of
        a 2x2 Block Matrix

        Returns
        =======

        (L, D, U) : Matrices
            L : Lower Diagonal Matrix
            D : Diagonal Matrix
            U : Upper Diagonal Matrix

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix, block_collapse
        >>> m, n = symbols('m n')
        >>> A = MatrixSymbol('A', n, n)
        >>> B = MatrixSymbol('B', n, m)
        >>> C = MatrixSymbol('C', m, n)
        >>> D = MatrixSymbol('D', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])
        >>> L, D, U = X.LDUdecomposition()
        >>> block_collapse(L*D*U)
        Matrix([
        [A, B],
        [C, D]])

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If the matrix "A" is non-invertible

        See Also
        ========
        sympy.matrices.expressions.blockmatrix.BlockMatrix.UDLdecomposition
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LUdecomposition
        """
        ...
    
    def UDLdecomposition(self) -> tuple[BlockMatrix, BlockDiagMatrix, BlockMatrix]:
        """Returns the Block UDL decomposition of
        a 2x2 Block Matrix

        Returns
        =======

        (U, D, L) : Matrices
            U : Upper Diagonal Matrix
            D : Diagonal Matrix
            L : Lower Diagonal Matrix

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix, block_collapse
        >>> m, n = symbols('m n')
        >>> A = MatrixSymbol('A', n, n)
        >>> B = MatrixSymbol('B', n, m)
        >>> C = MatrixSymbol('C', m, n)
        >>> D = MatrixSymbol('D', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])
        >>> U, D, L = X.UDLdecomposition()
        >>> block_collapse(U*D*L)
        Matrix([
        [A, B],
        [C, D]])

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If the matrix "D" is non-invertible

        See Also
        ========
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LDUdecomposition
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LUdecomposition
        """
        ...
    
    def LUdecomposition(self) -> tuple[BlockMatrix, BlockMatrix]:
        """Returns the Block LU decomposition of
        a 2x2 Block Matrix

        Returns
        =======

        (L, U) : Matrices
            L : Lower Diagonal Matrix
            U : Upper Diagonal Matrix

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix, block_collapse
        >>> m, n = symbols('m n')
        >>> A = MatrixSymbol('A', n, n)
        >>> B = MatrixSymbol('B', n, m)
        >>> C = MatrixSymbol('C', m, n)
        >>> D = MatrixSymbol('D', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])
        >>> L, U = X.LUdecomposition()
        >>> block_collapse(L*U)
        Matrix([
        [A, B],
        [C, D]])

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If the matrix "A" is non-invertible

        See Also
        ========
        sympy.matrices.expressions.blockmatrix.BlockMatrix.UDLdecomposition
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LDUdecomposition
        """
        ...
    
    @property
    def is_Identity(self) -> bool:
        ...
    
    @property
    def is_structurally_symmetric(self) -> bool:
        ...
    
    def equals(self, other) -> bool:
        ...
    


class BlockDiagMatrix(BlockMatrix):
    """A sparse matrix with block matrices along its diagonals

    Examples
    ========

    >>> from sympy import MatrixSymbol, BlockDiagMatrix, symbols
    >>> n, m, l = symbols('n m l')
    >>> X = MatrixSymbol('X', n, n)
    >>> Y = MatrixSymbol('Y', m, m)
    >>> BlockDiagMatrix(X, Y)
    Matrix([
    [X, 0],
    [0, Y]])

    Notes
    =====

    If you want to get the individual diagonal blocks, use
    :meth:`get_diag_blocks`.

    See Also
    ========

    sympy.matrices.dense.diag
    """
    def __new__(cls, *mats) -> BlockDiagMatrix:
        ...
    
    @property
    def diag(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def blocks(self) -> ImmutableDenseMatrix:
        ...
    
    @property
    def shape(self) -> tuple[int, int]:
        ...
    
    @property
    def blockshape(self) -> tuple[int, int]:
        ...
    
    @property
    def rowblocksizes(self) -> list[Any]:
        ...
    
    @property
    def colblocksizes(self) -> list[Any]:
        ...
    
    def get_diag_blocks(self) -> tuple[Basic, ...]:
        """Return the list of diagonal blocks of the matrix.

        Examples
        ========

        >>> from sympy import BlockDiagMatrix, Matrix

        >>> A = Matrix([[1, 2], [3, 4]])
        >>> B = Matrix([[5, 6], [7, 8]])
        >>> M = BlockDiagMatrix(A, B)

        How to get diagonal blocks from the block diagonal matrix:

        >>> diag_blocks = M.get_diag_blocks()
        >>> diag_blocks[0]
        Matrix([
        [1, 2],
        [3, 4]])
        >>> diag_blocks[1]
        Matrix([
        [5, 6],
        [7, 8]])
        """
        ...
    


def block_collapse(expr) -> Any:
    """Evaluates a block matrix expression

    >>> from sympy import MatrixSymbol, BlockMatrix, symbols, Identity, ZeroMatrix, block_collapse
    >>> n,m,l = symbols('n m l')
    >>> X = MatrixSymbol('X', n, n)
    >>> Y = MatrixSymbol('Y', m, m)
    >>> Z = MatrixSymbol('Z', n, m)
    >>> B = BlockMatrix([[X, Z], [ZeroMatrix(m, n), Y]])
    >>> print(B)
    Matrix([
    [X, Z],
    [0, Y]])

    >>> C = BlockMatrix([[Identity(n), Z]])
    >>> print(C)
    Matrix([[I, Z]])

    >>> print(block_collapse(C*B))
    Matrix([[X, Z + Z*Y]])
    """
    ...

def bc_unpack(expr):
    ...

def bc_matadd(expr):
    ...

def bc_block_plus_ident(expr) -> MatAdd | GenericZeroMatrix:
    ...

def bc_dist(expr) -> BlockDiagMatrix | BlockMatrix:
    """ Turn  a*[X, Y] into [a*X, a*Y] """
    ...

def bc_matmul(expr) -> MatPow | GenericIdentity | Order | object:
    ...

def bc_transpose(expr) -> Any:
    ...

def bc_inverse(expr) -> BlockMatrix:
    ...

def blockinverse_1x1(expr) -> BlockMatrix:
    ...

def blockinverse_2x2(expr) -> BlockMatrix:
    ...

def deblock(B) -> BlockMatrix:
    """ Flatten a BlockMatrix of BlockMatrices """
    ...

def reblock_2x2(expr) -> BlockMatrix:
    """
    Reblock a BlockMatrix so that it has 2x2 blocks of block matrices.  If
    possible in such a way that the matrix continues to be invertible using the
    classical 2x2 block inversion formulas.
    """
    ...

def bounds(sizes) -> list[Any]:
    """ Convert sequence of numbers into pairs of low-high pairs

    >>> from sympy.matrices.expressions.blockmatrix import bounds
    >>> bounds((1, 10, 50))
    [(0, 1), (1, 11), (11, 61)]
    """
    ...

def blockcut(expr, rowsizes, colsizes) -> BlockMatrix:
    """ Cut a matrix expression into Blocks

    >>> from sympy import ImmutableMatrix, blockcut
    >>> M = ImmutableMatrix(4, 4, range(16))
    >>> B = blockcut(M, (1, 3), (1, 3))
    >>> type(B).__name__
    'BlockMatrix'
    >>> ImmutableMatrix(B.blocks[0, 1])
    Matrix([[1, 2, 3]])
    """
    ...

