from types import NotImplementedType
from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.core.power import Pow
from sympy.core.symbol import Symbol
from sympy.functions.elementary.miscellaneous import Max, Min
from sympy.matrices import SparseMatrix
from sympy.matrices.expressions.blockmatrix import BlockDiagMatrix, BlockMatrix
from sympy.matrices.expressions.permutation import PermutationMatrix
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.printing.defaults import Printable
from sympy.series.order import Order
from sympy.tensor.array.array_derivatives import ArrayDerivative
from sympy.utilities.iterables import NotIterable
from sympy.core.decorators import call_highest_priority
from sympy.core.logic import FuzzyBool
from sympy.matrices.kind import MatrixKind
from numpy import ndarray as NDArray

class MatrixBase(Printable):
    """All common matrix operations including basic arithmetic, shaping,
    and special matrices like `zeros`, and `eye`."""
    _op_priority = ...
    __array_priority__ = ...
    is_Matrix = ...
    _class_priority = ...
    _sympify = ...
    zero = ...
    one = ...
    _diff_wrt: bool = ...
    rows: int = ...
    cols: int = ...
    _simplify = ...
    def __eq__(self, other) -> bool:
        ...
    
    def __getitem__(self, key):
        """Implementations of __getitem__ should accept ints, in which
        case the matrix is indexed as a flat list, tuples (i,j) in which
        case the (i,j) entry is returned, slices, or mixed tuples (a,b)
        where a and b are any combination of slices and integers."""
        ...
    
    @property
    def shape(self) -> tuple[int, int]:
        """The shape (dimensions) of the matrix as the 2-tuple (rows, cols).

        Examples
        ========

        >>> from sympy import zeros
        >>> M = zeros(2, 3)
        >>> M.shape
        (2, 3)
        >>> M.rows
        2
        >>> M.cols
        3
        """
        ...
    
    def col_del(self, col):
        """Delete the specified column."""
        ...
    
    def col_insert(self, pos, other) -> Self:
        """Insert one or more columns at the given column position.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(3, 1)
        >>> M.col_insert(1, V)
        Matrix([
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]])

        See Also
        ========

        col
        row_insert
        """
        ...
    
    def col_join(self, other):
        """Concatenates two matrices along self's last and other's first row.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(1, 3)
        >>> M.col_join(V)
        Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1]])

        See Also
        ========

        col
        row_join
        """
        ...
    
    def col(self, j):
        """Elementary column selector.

        Examples
        ========

        >>> from sympy import eye
        >>> eye(2).col(0)
        Matrix([
        [1],
        [0]])

        See Also
        ========

        row
        col_del
        col_join
        col_insert
        """
        ...
    
    def extract(self, rowsList, colsList):
        r"""Return a submatrix by specifying a list of rows and columns.
        Negative indices can be given. All indices must be in the range
        $-n \le i < n$ where $n$ is the number of rows or columns.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(4, 3, range(12))
        >>> m
        Matrix([
        [0,  1,  2],
        [3,  4,  5],
        [6,  7,  8],
        [9, 10, 11]])
        >>> m.extract([0, 1, 3], [0, 1])
        Matrix([
        [0,  1],
        [3,  4],
        [9, 10]])

        Rows or columns can be repeated:

        >>> m.extract([0, 0, 1], [-1])
        Matrix([
        [2],
        [2],
        [5]])

        Every other row can be taken by using range to provide the indices:

        >>> m.extract(range(0, m.rows, 2), [-1])
        Matrix([
        [2],
        [8]])

        RowsList or colsList can also be a list of booleans, in which case
        the rows or columns corresponding to the True values will be selected:

        >>> m.extract([0, 1, 2, 3], [True, False, True])
        Matrix([
        [0,  2],
        [3,  5],
        [6,  8],
        [9, 11]])
        """
        ...
    
    def get_diag_blocks(self) -> list[Any]:
        """Obtains the square sub-matrices on the main diagonal of a square matrix.

        Useful for inverting symbolic matrices or solving systems of
        linear equations which may be decoupled by having a block diagonal
        structure.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y, z
        >>> A = Matrix([[1, 3, 0, 0], [y, z*z, 0, 0], [0, 0, x, 0], [0, 0, 0, 0]])
        >>> a1, a2, a3 = A.get_diag_blocks()
        >>> a1
        Matrix([
        [1,    3],
        [y, z**2]])
        >>> a2
        Matrix([[x]])
        >>> a3
        Matrix([[0]])

        """
        ...
    
    @classmethod
    def hstack(cls, *args) -> Any:
        """Return a matrix formed by joining args horizontally (i.e.
        by repeated application of row_join).

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> Matrix.hstack(eye(2), 2*eye(2))
        Matrix([
        [1, 0, 2, 0],
        [0, 1, 0, 2]])
        """
        ...
    
    def reshape(self, rows, cols):
        """Reshape the matrix. Total number of elements must remain the same.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 3, lambda i, j: 1)
        >>> m
        Matrix([
        [1, 1, 1],
        [1, 1, 1]])
        >>> m.reshape(1, 6)
        Matrix([[1, 1, 1, 1, 1, 1]])
        >>> m.reshape(3, 2)
        Matrix([
        [1, 1],
        [1, 1],
        [1, 1]])

        """
        ...
    
    def row_del(self, row):
        """Delete the specified row."""
        ...
    
    def row_insert(self, pos, other):
        """Insert one or more rows at the given row position.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(1, 3)
        >>> M.row_insert(1, V)
        Matrix([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]])

        See Also
        ========

        row
        col_insert
        """
        ...
    
    def row_join(self, other):
        """Concatenates two matrices along self's last and rhs's first column

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(3, 1)
        >>> M.row_join(V)
        Matrix([
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]])

        See Also
        ========

        row
        col_join
        """
        ...
    
    def diagonal(self, k=...):
        """Returns the kth diagonal of self. The main diagonal
        corresponds to `k=0`; diagonals above and below correspond to
        `k > 0` and `k < 0`, respectively. The values of `self[i, j]`
        for which `j - i = k`, are returned in order of increasing
        `i + j`, starting with `i + j = |k|`.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(3, 3, lambda i, j: j - i); m
        Matrix([
        [ 0,  1, 2],
        [-1,  0, 1],
        [-2, -1, 0]])
        >>> _.diagonal()
        Matrix([[0, 0, 0]])
        >>> m.diagonal(1)
        Matrix([[1, 1]])
        >>> m.diagonal(-2)
        Matrix([[-2]])

        Even though the diagonal is returned as a Matrix, the element
        retrieval can be done with a single index:

        >>> Matrix.diag(1, 2, 3).diagonal()[1]  # instead of [0, 1]
        2

        See Also
        ========

        diag
        """
        ...
    
    def row(self, i):
        """Elementary row selector.

        Examples
        ========

        >>> from sympy import eye
        >>> eye(2).row(0)
        Matrix([[1, 0]])

        See Also
        ========

        col
        row_del
        row_join
        row_insert
        """
        ...
    
    def todok(self) -> dict[Any, Any]:
        """Return the matrix as dictionary of keys.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix.eye(3)
        >>> M.todok()
        {(0, 0): 1, (1, 1): 1, (2, 2): 1}
        """
        ...
    
    def tolist(self) -> list[Any] | list[list[Any]]:
        """Return the Matrix as a nested Python list.

        Examples
        ========

        >>> from sympy import Matrix, ones
        >>> m = Matrix(3, 3, range(9))
        >>> m
        Matrix([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]])
        >>> m.tolist()
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        >>> ones(3, 0).tolist()
        [[], [], []]

        When there are no rows then it will not be possible to tell how
        many columns were in the original matrix:

        >>> ones(0, 3).tolist()
        []

        """
        ...
    
    def todod(M) -> dict[Any, Any]:
        """Returns matrix as dict of dicts containing non-zero elements of the Matrix

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[0, 1],[0, 3]])
        >>> A
        Matrix([
        [0, 1],
        [0, 3]])
        >>> A.todod()
        {0: {1: 1}, 1: {1: 3}}


        """
        ...
    
    def vec(self):
        """Return the Matrix converted into a one column matrix by stacking columns

        Examples
        ========

        >>> from sympy import Matrix
        >>> m=Matrix([[1, 3], [2, 4]])
        >>> m
        Matrix([
        [1, 3],
        [2, 4]])
        >>> m.vec()
        Matrix([
        [1],
        [2],
        [3],
        [4]])

        See Also
        ========

        vech
        """
        ...
    
    def vech(self, diagonal=..., check_symmetry=...):
        """Reshapes the matrix into a column vector by stacking the
        elements in the lower triangle.

        Parameters
        ==========

        diagonal : bool, optional
            If ``True``, it includes the diagonal elements.

        check_symmetry : bool, optional
            If ``True``, it checks whether the matrix is symmetric.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m=Matrix([[1, 2], [2, 3]])
        >>> m
        Matrix([
        [1, 2],
        [2, 3]])
        >>> m.vech()
        Matrix([
        [1],
        [2],
        [3]])
        >>> m.vech(diagonal=False)
        Matrix([[2]])

        Notes
        =====

        This should work for symmetric matrices and ``vech`` can
        represent symmetric matrices in vector form with less size than
        ``vec``.

        See Also
        ========

        vec
        """
        ...
    
    @classmethod
    def vstack(cls, *args) -> Any:
        """Return a matrix formed by joining args vertically (i.e.
        by repeated application of col_join).

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> Matrix.vstack(eye(2), 2*eye(2))
        Matrix([
        [1, 0],
        [0, 1],
        [2, 0],
        [0, 2]])
        """
        ...
    
    @classmethod
    def diag(kls, *args, strict=..., unpack=..., rows=..., cols=..., **kwargs):
        """Returns a matrix with the specified diagonal.
        If matrices are passed, a block-diagonal matrix
        is created (i.e. the "direct sum" of the matrices).

        kwargs
        ======

        rows : rows of the resulting matrix; computed if
               not given.

        cols : columns of the resulting matrix; computed if
               not given.

        cls : class for the resulting matrix

        unpack : bool which, when True (default), unpacks a single
        sequence rather than interpreting it as a Matrix.

        strict : bool which, when False (default), allows Matrices to
        have variable-length rows.

        Examples
        ========

        >>> from sympy import Matrix
        >>> Matrix.diag(1, 2, 3)
        Matrix([
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]])

        The current default is to unpack a single sequence. If this is
        not desired, set `unpack=False` and it will be interpreted as
        a matrix.

        >>> Matrix.diag([1, 2, 3]) == Matrix.diag(1, 2, 3)
        True

        When more than one element is passed, each is interpreted as
        something to put on the diagonal. Lists are converted to
        matrices. Filling of the diagonal always continues from
        the bottom right hand corner of the previous item: this
        will create a block-diagonal matrix whether the matrices
        are square or not.

        >>> col = [1, 2, 3]
        >>> row = [[4, 5]]
        >>> Matrix.diag(col, row)
        Matrix([
        [1, 0, 0],
        [2, 0, 0],
        [3, 0, 0],
        [0, 4, 5]])

        When `unpack` is False, elements within a list need not all be
        of the same length. Setting `strict` to True would raise a
        ValueError for the following:

        >>> Matrix.diag([[1, 2, 3], [4, 5], [6]], unpack=False)
        Matrix([
        [1, 2, 3],
        [4, 5, 0],
        [6, 0, 0]])

        The type of the returned matrix can be set with the ``cls``
        keyword.

        >>> from sympy import ImmutableMatrix
        >>> from sympy.utilities.misc import func_name
        >>> func_name(Matrix.diag(1, cls=ImmutableMatrix))
        'ImmutableDenseMatrix'

        A zero dimension matrix can be used to position the start of
        the filling at the start of an arbitrary row or column:

        >>> from sympy import ones
        >>> r2 = ones(0, 2)
        >>> Matrix.diag(r2, 1, 2)
        Matrix([
        [0, 0, 1, 0],
        [0, 0, 0, 2]])

        See Also
        ========
        eye
        diagonal
        .dense.diag
        .expressions.blockmatrix.BlockMatrix
        .sparsetools.banded
       """
        ...
    
    @classmethod
    def eye(kls, rows, cols=..., **kwargs):
        """Returns an identity matrix.

        Parameters
        ==========

        rows : rows of the matrix
        cols : cols of the matrix (if None, cols=rows)

        kwargs
        ======
        cls : class of the returned matrix
        """
        ...
    
    @classmethod
    def jordan_block(kls, size=..., eigenvalue=..., *, band=..., **kwargs):
        """Returns a Jordan block

        Parameters
        ==========

        size : Integer, optional
            Specifies the shape of the Jordan block matrix.

        eigenvalue : Number or Symbol
            Specifies the value for the main diagonal of the matrix.

            .. note::
                The keyword ``eigenval`` is also specified as an alias
                of this keyword, but it is not recommended to use.

                We may deprecate the alias in later release.

        band : 'upper' or 'lower', optional
            Specifies the position of the off-diagonal to put `1` s on.

        cls : Matrix, optional
            Specifies the matrix class of the output form.

            If it is not specified, the class type where the method is
            being executed on will be returned.

        Returns
        =======

        Matrix
            A Jordan block matrix.

        Raises
        ======

        ValueError
            If insufficient arguments are given for matrix size
            specification, or no eigenvalue is given.

        Examples
        ========

        Creating a default Jordan block:

        >>> from sympy import Matrix
        >>> from sympy.abc import x
        >>> Matrix.jordan_block(4, x)
        Matrix([
        [x, 1, 0, 0],
        [0, x, 1, 0],
        [0, 0, x, 1],
        [0, 0, 0, x]])

        Creating an alternative Jordan block matrix where `1` is on
        lower off-diagonal:

        >>> Matrix.jordan_block(4, x, band='lower')
        Matrix([
        [x, 0, 0, 0],
        [1, x, 0, 0],
        [0, 1, x, 0],
        [0, 0, 1, x]])

        Creating a Jordan block with keyword arguments

        >>> Matrix.jordan_block(size=4, eigenvalue=x)
        Matrix([
        [x, 1, 0, 0],
        [0, x, 1, 0],
        [0, 0, x, 1],
        [0, 0, 0, x]])

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Jordan_matrix
        """
        ...
    
    @classmethod
    def ones(kls, rows, cols=..., **kwargs):
        """Returns a matrix of ones.

        Parameters
        ==========

        rows : rows of the matrix
        cols : cols of the matrix (if None, cols=rows)

        kwargs
        ======
        cls : class of the returned matrix
        """
        ...
    
    @classmethod
    def zeros(kls, rows, cols=..., **kwargs):
        """Returns a matrix of zeros.

        Parameters
        ==========

        rows : rows of the matrix
        cols : cols of the matrix (if None, cols=rows)

        kwargs
        ======
        cls : class of the returned matrix
        """
        ...
    
    @classmethod
    def companion(kls, poly):
        """Returns a companion matrix of a polynomial.

        Examples
        ========

        >>> from sympy import Matrix, Poly, Symbol, symbols
        >>> x = Symbol('x')
        >>> c0, c1, c2, c3, c4 = symbols('c0:5')
        >>> p = Poly(c0 + c1*x + c2*x**2 + c3*x**3 + c4*x**4 + x**5, x)
        >>> Matrix.companion(p)
        Matrix([
        [0, 0, 0, 0, -c0],
        [1, 0, 0, 0, -c1],
        [0, 1, 0, 0, -c2],
        [0, 0, 1, 0, -c3],
        [0, 0, 0, 1, -c4]])
        """
        ...
    
    @classmethod
    def wilkinson(kls, n, **kwargs):
        """Returns two square Wilkinson Matrix of size 2*n + 1
        $W_{2n + 1}^-, W_{2n + 1}^+ =$ Wilkinson(n)

        Examples
        ========

        >>> from sympy import Matrix
        >>> wminus, wplus = Matrix.wilkinson(3)
        >>> wminus
        Matrix([
        [-3,  1,  0, 0, 0, 0, 0],
        [ 1, -2,  1, 0, 0, 0, 0],
        [ 0,  1, -1, 1, 0, 0, 0],
        [ 0,  0,  1, 0, 1, 0, 0],
        [ 0,  0,  0, 1, 1, 1, 0],
        [ 0,  0,  0, 0, 1, 2, 1],
        [ 0,  0,  0, 0, 0, 1, 3]])
        >>> wplus
        Matrix([
        [3, 1, 0, 0, 0, 0, 0],
        [1, 2, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 2, 1],
        [0, 0, 0, 0, 0, 1, 3]])

        References
        ==========

        .. [1] https://blogs.mathworks.com/cleve/2013/04/15/wilkinsons-matrices-2/
        .. [2] J. H. Wilkinson, The Algebraic Eigenvalue Problem, Claredon Press, Oxford, 1965, 662 pp.

        """
        ...
    
    def atoms(self, *types) -> set[Any]:
        """Returns the atoms that form the current object.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import Matrix
        >>> Matrix([[x]])
        Matrix([[x]])
        >>> _.atoms()
        {x}
        >>> Matrix([[x, y], [y, x]])
        Matrix([
        [x, y],
        [y, x]])
        >>> _.atoms()
        {x, y}
        """
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        """Returns the free symbols within the matrix.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import Matrix
        >>> Matrix([[x], [1]]).free_symbols
        {x}
        """
        ...
    
    def has(self, *patterns) -> bool:
        """Test whether any subexpression matches any of the patterns.

        Examples
        ========

        >>> from sympy import Matrix, SparseMatrix, Float
        >>> from sympy.abc import x, y
        >>> A = Matrix(((1, x), (0.2, 3)))
        >>> B = SparseMatrix(((1, x), (0.2, 3)))
        >>> A.has(x)
        True
        >>> A.has(y)
        False
        >>> A.has(Float)
        True
        >>> B.has(x)
        True
        >>> B.has(y)
        False
        >>> B.has(Float)
        True
        """
        ...
    
    def is_anti_symmetric(self, simplify=...) -> bool:
        """Check if matrix M is an antisymmetric matrix,
        that is, M is a square matrix with all M[i, j] == -M[j, i].

        When ``simplify=True`` (default), the sum M[i, j] + M[j, i] is
        simplified before testing to see if it is zero. By default,
        the SymPy simplify function is used. To use a custom function
        set simplify to a function that accepts a single argument which
        returns a simplified expression. To skip simplification, set
        simplify to False but note that although this will be faster,
        it may induce false negatives.

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> m = Matrix(2, 2, [0, 1, -1, 0])
        >>> m
        Matrix([
        [ 0, 1],
        [-1, 0]])
        >>> m.is_anti_symmetric()
        True
        >>> x, y = symbols('x y')
        >>> m = Matrix(2, 3, [0, 0, x, -y, 0, 0])
        >>> m
        Matrix([
        [ 0, 0, x],
        [-y, 0, 0]])
        >>> m.is_anti_symmetric()
        False

        >>> from sympy.abc import x, y
        >>> m = Matrix(3, 3, [0, x**2 + 2*x + 1, y,
        ...                   -(x + 1)**2, 0, x*y,
        ...                   -y, -x*y, 0])

        Simplification of matrix elements is done by default so even
        though two elements which should be equal and opposite would not
        pass an equality test, the matrix is still reported as
        anti-symmetric:

        >>> m[0, 1] == -m[1, 0]
        False
        >>> m.is_anti_symmetric()
        True

        If ``simplify=False`` is used for the case when a Matrix is already
        simplified, this will speed things up. Here, we see that without
        simplification the matrix does not appear anti-symmetric:

        >>> m.is_anti_symmetric(simplify=False)
        False

        But if the matrix were already expanded, then it would appear
        anti-symmetric and simplification in the is_anti_symmetric routine
        is not needed:

        >>> m = m.expand()
        >>> m.is_anti_symmetric(simplify=False)
        True
        """
        ...
    
    def is_diagonal(self) -> bool:
        """Check if matrix is diagonal,
        that is matrix in which the entries outside the main diagonal are all zero.

        Examples
        ========

        >>> from sympy import Matrix, diag
        >>> m = Matrix(2, 2, [1, 0, 0, 2])
        >>> m
        Matrix([
        [1, 0],
        [0, 2]])
        >>> m.is_diagonal()
        True

        >>> m = Matrix(2, 2, [1, 1, 0, 2])
        >>> m
        Matrix([
        [1, 1],
        [0, 2]])
        >>> m.is_diagonal()
        False

        >>> m = diag(1, 2, 3)
        >>> m
        Matrix([
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]])
        >>> m.is_diagonal()
        True

        See Also
        ========

        is_lower
        is_upper
        sympy.matrices.matrixbase.MatrixBase.is_diagonalizable
        diagonalize
        """
        ...
    
    @property
    def is_weakly_diagonally_dominant(self) -> bool | None:
        r"""Tests if the matrix is row weakly diagonally dominant.

        Explanation
        ===========

        A $n, n$ matrix $A$ is row weakly diagonally dominant if

        .. math::
            \left|A_{i, i}\right| \ge \sum_{j = 0, j \neq i}^{n-1}
            \left|A_{i, j}\right| \quad {\text{for all }}
            i \in \{ 0, ..., n-1 \}

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[3, -2, 1], [1, -3, 2], [-1, 2, 4]])
        >>> A.is_weakly_diagonally_dominant
        True

        >>> A = Matrix([[-2, 2, 1], [1, 3, 2], [1, -2, 0]])
        >>> A.is_weakly_diagonally_dominant
        False

        >>> A = Matrix([[-4, 2, 1], [1, 6, 2], [1, -2, 5]])
        >>> A.is_weakly_diagonally_dominant
        True

        Notes
        =====

        If you want to test whether a matrix is column diagonally
        dominant, you can apply the test after transposing the matrix.
        """
        ...
    
    @property
    def is_strongly_diagonally_dominant(self) -> bool | None:
        r"""Tests if the matrix is row strongly diagonally dominant.

        Explanation
        ===========

        A $n, n$ matrix $A$ is row strongly diagonally dominant if

        .. math::
            \left|A_{i, i}\right| > \sum_{j = 0, j \neq i}^{n-1}
            \left|A_{i, j}\right| \quad {\text{for all }}
            i \in \{ 0, ..., n-1 \}

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[3, -2, 1], [1, -3, 2], [-1, 2, 4]])
        >>> A.is_strongly_diagonally_dominant
        False

        >>> A = Matrix([[-2, 2, 1], [1, 3, 2], [1, -2, 0]])
        >>> A.is_strongly_diagonally_dominant
        False

        >>> A = Matrix([[-4, 2, 1], [1, 6, 2], [1, -2, 5]])
        >>> A.is_strongly_diagonally_dominant
        True

        Notes
        =====

        If you want to test whether a matrix is column diagonally
        dominant, you can apply the test after transposing the matrix.
        """
        ...
    
    @property
    def is_hermitian(self) -> Literal[False]:
        """Checks if the matrix is Hermitian.

        In a Hermitian matrix element i,j is the complex conjugate of
        element j,i.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy import I
        >>> from sympy.abc import x
        >>> a = Matrix([[1, I], [-I, 1]])
        >>> a
        Matrix([
        [ 1, I],
        [-I, 1]])
        >>> a.is_hermitian
        True
        >>> a[0, 0] = 2*I
        >>> a.is_hermitian
        False
        >>> a[0, 0] = x
        >>> a.is_hermitian
        >>> a[0, 1] = a[1, 0]*I
        >>> a.is_hermitian
        False
        """
        ...
    
    @property
    def is_Identity(self) -> FuzzyBool:
        ...
    
    @property
    def is_lower_hessenberg(self) -> bool:
        r"""Checks if the matrix is in the lower-Hessenberg form.

        The lower hessenberg matrix has zero entries
        above the first superdiagonal.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[1, 2, 0, 0], [5, 2, 3, 0], [3, 4, 3, 7], [5, 6, 1, 1]])
        >>> a
        Matrix([
        [1, 2, 0, 0],
        [5, 2, 3, 0],
        [3, 4, 3, 7],
        [5, 6, 1, 1]])
        >>> a.is_lower_hessenberg
        True

        See Also
        ========

        is_upper_hessenberg
        is_lower
        """
        ...
    
    @property
    def is_lower(self) -> bool:
        """Check if matrix is a lower triangular matrix. True can be returned
        even if the matrix is not square.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, [1, 0, 0, 1])
        >>> m
        Matrix([
        [1, 0],
        [0, 1]])
        >>> m.is_lower
        True

        >>> m = Matrix(4, 3, [0, 0, 0, 2, 0, 0, 1, 4, 0, 6, 6, 5])
        >>> m
        Matrix([
        [0, 0, 0],
        [2, 0, 0],
        [1, 4, 0],
        [6, 6, 5]])
        >>> m.is_lower
        True

        >>> from sympy.abc import x, y
        >>> m = Matrix(2, 2, [x**2 + y, y**2 + x, 0, x + y])
        >>> m
        Matrix([
        [x**2 + y, x + y**2],
        [       0,    x + y]])
        >>> m.is_lower
        False

        See Also
        ========

        is_upper
        is_diagonal
        is_lower_hessenberg
        """
        ...
    
    @property
    def is_square(self) -> bool:
        """Checks if a matrix is square.

        A matrix is square if the number of rows equals the number of columns.
        The empty matrix is square by definition, since the number of rows and
        the number of columns are both zero.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[1, 2, 3], [4, 5, 6]])
        >>> b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> c = Matrix([])
        >>> a.is_square
        False
        >>> b.is_square
        True
        >>> c.is_square
        True
        """
        ...
    
    def is_symbolic(self) -> bool:
        """Checks if any elements contain Symbols.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.is_symbolic()
        True

        """
        ...
    
    def is_symmetric(self, simplify=...) -> Literal[False]:
        """Check if matrix is symmetric matrix,
        that is square matrix and is equal to its transpose.

        By default, simplifications occur before testing symmetry.
        They can be skipped using 'simplify=False'; while speeding things a bit,
        this may however induce false negatives.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, [0, 1, 1, 2])
        >>> m
        Matrix([
        [0, 1],
        [1, 2]])
        >>> m.is_symmetric()
        True

        >>> m = Matrix(2, 2, [0, 1, 2, 0])
        >>> m
        Matrix([
        [0, 1],
        [2, 0]])
        >>> m.is_symmetric()
        False

        >>> m = Matrix(2, 3, [0, 0, 0, 0, 0, 0])
        >>> m
        Matrix([
        [0, 0, 0],
        [0, 0, 0]])
        >>> m.is_symmetric()
        False

        >>> from sympy.abc import x, y
        >>> m = Matrix(3, 3, [1, x**2 + 2*x + 1, y, (x + 1)**2, 2, 0, y, 0, 3])
        >>> m
        Matrix([
        [         1, x**2 + 2*x + 1, y],
        [(x + 1)**2,              2, 0],
        [         y,              0, 3]])
        >>> m.is_symmetric()
        True

        If the matrix is already simplified, you may speed-up is_symmetric()
        test by using 'simplify=False'.

        >>> bool(m.is_symmetric(simplify=False))
        False
        >>> m1 = m.expand()
        >>> m1.is_symmetric(simplify=False)
        True
        """
        ...
    
    @property
    def is_upper_hessenberg(self) -> bool:
        """Checks if the matrix is the upper-Hessenberg form.

        The upper hessenberg matrix has zero entries
        below the first subdiagonal.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[1, 4, 2, 3], [3, 4, 1, 7], [0, 2, 3, 4], [0, 0, 1, 3]])
        >>> a
        Matrix([
        [1, 4, 2, 3],
        [3, 4, 1, 7],
        [0, 2, 3, 4],
        [0, 0, 1, 3]])
        >>> a.is_upper_hessenberg
        True

        See Also
        ========

        is_lower_hessenberg
        is_upper
        """
        ...
    
    @property
    def is_upper(self) -> bool:
        """Check if matrix is an upper triangular matrix. True can be returned
        even if the matrix is not square.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, [1, 0, 0, 1])
        >>> m
        Matrix([
        [1, 0],
        [0, 1]])
        >>> m.is_upper
        True

        >>> m = Matrix(4, 3, [5, 1, 9, 0, 4, 6, 0, 0, 5, 0, 0, 0])
        >>> m
        Matrix([
        [5, 1, 9],
        [0, 4, 6],
        [0, 0, 5],
        [0, 0, 0]])
        >>> m.is_upper
        True

        >>> m = Matrix(2, 3, [4, 2, 5, 6, 1, 1])
        >>> m
        Matrix([
        [4, 2, 5],
        [6, 1, 1]])
        >>> m.is_upper
        False

        See Also
        ========

        is_lower
        is_diagonal
        is_upper_hessenberg
        """
        ...
    
    @property
    def is_zero_matrix(self) -> bool | None:
        """Checks if a matrix is a zero matrix.

        A matrix is zero if every element is zero.  A matrix need not be square
        to be considered zero.  The empty matrix is zero by the principle of
        vacuous truth.  For a matrix that may or may not be zero (e.g.
        contains a symbol), this will be None

        Examples
        ========

        >>> from sympy import Matrix, zeros
        >>> from sympy.abc import x
        >>> a = Matrix([[0, 0], [0, 0]])
        >>> b = zeros(3, 4)
        >>> c = Matrix([[0, 1], [0, 0]])
        >>> d = Matrix([])
        >>> e = Matrix([[x, 0], [0, 0]])
        >>> a.is_zero_matrix
        True
        >>> b.is_zero_matrix
        True
        >>> c.is_zero_matrix
        False
        >>> d.is_zero_matrix
        True
        >>> e.is_zero_matrix
        """
        ...
    
    def values(self) -> list[Any]:
        """Return non-zero values of self."""
        ...
    
    def adjoint(self):
        """Conjugate transpose or Hermitian conjugation."""
        ...
    
    def applyfunc(self, f):
        """Apply a function to each element of the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, lambda i, j: i*2+j)
        >>> m
        Matrix([
        [0, 1],
        [2, 3]])
        >>> m.applyfunc(lambda i: 2*i)
        Matrix([
        [0, 2],
        [4, 6]])

        """
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]:
        """Returns a tuple containing the (real, imaginary) part of matrix."""
        ...
    
    def conjugate(self):
        """Return the by-element conjugation.

        Examples
        ========

        >>> from sympy import SparseMatrix, I
        >>> a = SparseMatrix(((1, 2 + I), (3, 4), (I, -I)))
        >>> a
        Matrix([
        [1, 2 + I],
        [3,     4],
        [I,    -I]])
        >>> a.C
        Matrix([
        [ 1, 2 - I],
        [ 3,     4],
        [-I,     I]])

        See Also
        ========

        transpose: Matrix transposition
        H: Hermite conjugation
        sympy.matrices.matrixbase.MatrixBase.D: Dirac conjugation
        """
        ...
    
    def doit(self, **hints):
        ...
    
    def evalf(self, n=..., subs=..., maxn=..., chop=..., strict=..., quad=..., verbose=...):
        """Apply evalf() to each element of self."""
        ...
    
    def expand(self, deep=..., modulus=..., power_base=..., power_exp=..., mul=..., log=..., multinomial=..., basic=..., **hints):
        """Apply core.function.expand to each entry of the matrix.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import Matrix
        >>> Matrix(1, 1, [x*(x+1)])
        Matrix([[x*(x + 1)]])
        >>> _.expand()
        Matrix([[x**2 + x]])

        """
        ...
    
    @property
    def H(self):
        """Return Hermite conjugate.

        Examples
        ========

        >>> from sympy import Matrix, I
        >>> m = Matrix((0, 1 + I, 2, 3))
        >>> m
        Matrix([
        [    0],
        [1 + I],
        [    2],
        [    3]])
        >>> m.H
        Matrix([[0, 1 - I, 2, 3]])

        See Also
        ========

        conjugate: By-element conjugation
        sympy.matrices.matrixbase.MatrixBase.D: Dirac conjugation
        """
        ...
    
    def permute(self, perm, orientation=..., direction=...) -> None:
        r"""Permute the rows or columns of a matrix by the given list of
        swaps.

        Parameters
        ==========

        perm : Permutation, list, or list of lists
            A representation for the permutation.

            If it is ``Permutation``, it is used directly with some
            resizing with respect to the matrix size.

            If it is specified as list of lists,
            (e.g., ``[[0, 1], [0, 2]]``), then the permutation is formed
            from applying the product of cycles. The direction how the
            cyclic product is applied is described in below.

            If it is specified as a list, the list should represent
            an array form of a permutation. (e.g., ``[1, 2, 0]``) which
            would would form the swapping function
            `0 \mapsto 1, 1 \mapsto 2, 2\mapsto 0`.

        orientation : 'rows', 'cols'
            A flag to control whether to permute the rows or the columns

        direction : 'forward', 'backward'
            A flag to control whether to apply the permutations from
            the start of the list first, or from the back of the list
            first.

            For example, if the permutation specification is
            ``[[0, 1], [0, 2]]``,

            If the flag is set to ``'forward'``, the cycle would be
            formed as `0 \mapsto 2, 2 \mapsto 1, 1 \mapsto 0`.

            If the flag is set to ``'backward'``, the cycle would be
            formed as `0 \mapsto 1, 1 \mapsto 2, 2 \mapsto 0`.

            If the argument ``perm`` is not in a form of list of lists,
            this flag takes no effect.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.permute([[0, 1], [0, 2]], orientation='rows', direction='forward')
        Matrix([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]])

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.permute([[0, 1], [0, 2]], orientation='rows', direction='backward')
        Matrix([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]])

        Notes
        =====

        If a bijective function
        `\sigma : \mathbb{N}_0 \rightarrow \mathbb{N}_0` denotes the
        permutation.

        If the matrix `A` is the matrix to permute, represented as
        a horizontal or a vertical stack of vectors:

        .. math::
            A =
            \begin{bmatrix}
            a_0 \\ a_1 \\ \vdots \\ a_{n-1}
            \end{bmatrix} =
            \begin{bmatrix}
            \alpha_0 & \alpha_1 & \cdots & \alpha_{n-1}
            \end{bmatrix}

        If the matrix `B` is the result, the permutation of matrix rows
        is defined as:

        .. math::
            B := \begin{bmatrix}
            a_{\sigma(0)} \\ a_{\sigma(1)} \\ \vdots \\ a_{\sigma(n-1)}
            \end{bmatrix}

        And the permutation of matrix columns is defined as:

        .. math::
            B := \begin{bmatrix}
            \alpha_{\sigma(0)} & \alpha_{\sigma(1)} &
            \cdots & \alpha_{\sigma(n-1)}
            \end{bmatrix}
        """
        ...
    
    def permute_cols(self, swaps, direction=...) -> None:
        """Alias for
        ``self.permute(swaps, orientation='cols', direction=direction)``

        See Also
        ========

        permute
        """
        ...
    
    def permute_rows(self, swaps, direction=...) -> None:
        """Alias for
        ``self.permute(swaps, orientation='rows', direction=direction)``

        See Also
        ========

        permute
        """
        ...
    
    def refine(self, assumptions=...):
        """Apply refine to each element of the matrix.

        Examples
        ========

        >>> from sympy import Symbol, Matrix, Abs, sqrt, Q
        >>> x = Symbol('x')
        >>> Matrix([[Abs(x)**2, sqrt(x**2)],[sqrt(x**2), Abs(x)**2]])
        Matrix([
        [ Abs(x)**2, sqrt(x**2)],
        [sqrt(x**2),  Abs(x)**2]])
        >>> _.refine(Q.real(x))
        Matrix([
        [  x**2, Abs(x)],
        [Abs(x),   x**2]])

        """
        ...
    
    def replace(self, F, G, map=..., simultaneous=..., exact=...) -> tuple[Any, dict[Any, Any]]:
        """Replaces Function F in Matrix entries with Function G.

        Examples
        ========

        >>> from sympy import symbols, Function, Matrix
        >>> F, G = symbols('F, G', cls=Function)
        >>> M = Matrix(2, 2, lambda i, j: F(i+j)) ; M
        Matrix([
        [F(0), F(1)],
        [F(1), F(2)]])
        >>> N = M.replace(F,G)
        >>> N
        Matrix([
        [G(0), G(1)],
        [G(1), G(2)]])
        """
        ...
    
    def rot90(self, k=...) -> Self | None:
        """Rotates Matrix by 90 degrees

        Parameters
        ==========

        k : int
            Specifies how many times the matrix is rotated by 90 degrees
            (clockwise when positive, counter-clockwise when negative).

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> A = Matrix(2, 2, symbols('a:d'))
        >>> A
        Matrix([
        [a, b],
        [c, d]])

        Rotating the matrix clockwise one time:

        >>> A.rot90(1)
        Matrix([
        [c, a],
        [d, b]])

        Rotating the matrix anticlockwise two times:

        >>> A.rot90(-2)
        Matrix([
        [d, c],
        [b, a]])
        """
        ...
    
    def simplify(self, **kwargs):
        """Apply simplify to each element of the matrix.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, sin, cos
        >>> SparseMatrix(1, 1, [x*sin(y)**2 + x*cos(y)**2])
        Matrix([[x*sin(y)**2 + x*cos(y)**2]])
        >>> _.simplify()
        Matrix([[x]])
        """
        ...
    
    def subs(self, *args, **kwargs):
        """Return a new matrix with subs applied to each entry.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, Matrix
        >>> SparseMatrix(1, 1, [x])
        Matrix([[x]])
        >>> _.subs(x, y)
        Matrix([[y]])
        >>> Matrix(_).subs(y, x)
        Matrix([[x]])
        """
        ...
    
    def trace(self) -> int:
        """
        Returns the trace of a square matrix i.e. the sum of the
        diagonal elements.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.trace()
        5

        """
        ...
    
    def transpose(self):
        """
        Returns the transpose of the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.transpose()
        Matrix([
        [1, 3],
        [2, 4]])

        >>> from sympy import Matrix, I
        >>> m=Matrix(((1, 2+I), (3, 4)))
        >>> m
        Matrix([
        [1, 2 + I],
        [3,     4]])
        >>> m.transpose()
        Matrix([
        [    1, 3],
        [2 + I, 4]])
        >>> m.T == m.transpose()
        True

        See Also
        ========

        conjugate: By-element conjugation

        """
        ...
    
    @property
    def T(self):
        '''Matrix transposition'''
        ...
    
    @property
    def C(self):
        '''By-element conjugation'''
        ...
    
    def n(self, *args, **kwargs):
        """Apply evalf() to each element of self."""
        ...
    
    def xreplace(self, rule):
        """Return a new matrix with xreplace applied to each entry.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, Matrix
        >>> SparseMatrix(1, 1, [x])
        Matrix([[x]])
        >>> _.xreplace({x: y})
        Matrix([[y]])
        >>> Matrix(_).xreplace({y: x})
        Matrix([[x]])
        """
        ...
    
    def upper_triangular(self, k=...):
        """Return the elements on and above the kth diagonal of a matrix.
        If k is not specified then simply returns upper-triangular portion
        of a matrix

        Examples
        ========

        >>> from sympy import ones
        >>> A = ones(4)
        >>> A.upper_triangular()
        Matrix([
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 1]])

        >>> A.upper_triangular(2)
        Matrix([
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])

        >>> A.upper_triangular(-1)
        Matrix([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]])

        """
        ...
    
    def lower_triangular(self, k=...):
        """Return the elements on and below the kth diagonal of a matrix.
        If k is not specified then simply returns lower-triangular portion
        of a matrix

        Examples
        ========

        >>> from sympy import ones
        >>> A = ones(4)
        >>> A.lower_triangular()
        Matrix([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]])

        >>> A.lower_triangular(-2)
        Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0]])

        >>> A.lower_triangular(1)
        Matrix([
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

        """
        ...
    
    def __abs__(self):
        """Returns a new matrix with entry-wise absolute values."""
        ...
    
    @call_highest_priority('__radd__')
    def __add__(self, other) -> NotImplementedType | Any:
        """Return self + other, raising ShapeError if shapes do not match."""
        ...
    
    @call_highest_priority('__rtruediv__')
    def __truediv__(self, other):
        ...
    
    @call_highest_priority('__rmatmul__')
    def __matmul__(self, other) -> NotImplementedType | Any:
        ...
    
    def __mod__(self, other):
        ...
    
    @call_highest_priority('__rmul__')
    def __mul__(self, other) -> Any | NotImplementedType:
        """Return self*other where other is either a scalar or a matrix
        of compatible dimensions.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[1, 2, 3], [4, 5, 6]])
        >>> 2*A == A*2 == Matrix([[2, 4, 6], [8, 10, 12]])
        True
        >>> B = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> A*B
        Matrix([
        [30, 36, 42],
        [66, 81, 96]])
        >>> B*A
        Traceback (most recent call last):
        ...
        ShapeError: Matrices size mismatch.
        >>>

        See Also
        ========

        matrix_multiply_elementwise
        """
        ...
    
    def multiply(self, other, dotprodsimp=...) -> Any | NotImplementedType:
        """Same as __mul__() but with optional simplification.

        Parameters
        ==========

        dotprodsimp : bool, optional
            Specifies whether intermediate term algebraic simplification is used
            during matrix multiplications to control expression blowup and thus
            speed up calculation. Default is off.
        """
        ...
    
    def multiply_elementwise(self, other):
        """Return the Hadamard product (elementwise product) of A and B

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[0, 1, 2], [3, 4, 5]])
        >>> B = Matrix([[1, 10, 100], [100, 10, 1]])
        >>> A.multiply_elementwise(B)
        Matrix([
        [  0, 10, 200],
        [300, 40,   5]])

        See Also
        ========

        sympy.matrices.matrixbase.MatrixBase.cross
        sympy.matrices.matrixbase.MatrixBase.dot
        multiply
        """
        ...
    
    def __neg__(self):
        ...
    
    @call_highest_priority('__rpow__')
    def __pow__(self, exp):
        """Return self**exp a scalar or symbol."""
        ...
    
    def pow(self, exp, method=...):
        r"""Return self**exp a scalar or symbol.

        Parameters
        ==========

        method : multiply, mulsimp, jordan, cayley
            If multiply then it returns exponentiation using recursion.
            If jordan then Jordan form exponentiation will be used.
            If cayley then the exponentiation is done using Cayley-Hamilton
            theorem.
            If mulsimp then the exponentiation is done using recursion
            with dotprodsimp. This specifies whether intermediate term
            algebraic simplification is used during naive matrix power to
            control expression blowup and thus speed up calculation.
            If None, then it heuristically decides which method to use.

        """
        ...
    
    @call_highest_priority('__add__')
    def __radd__(self, other):
        ...
    
    @call_highest_priority('__matmul__')
    def __rmatmul__(self, other) -> NotImplementedType | Any:
        ...
    
    @call_highest_priority('__mul__')
    def __rmul__(self, other) -> Any | NotImplementedType:
        ...
    
    def rmultiply(self, other, dotprodsimp=...) -> Any | NotImplementedType:
        """Same as __rmul__() but with optional simplification.

        Parameters
        ==========

        dotprodsimp : bool, optional
            Specifies whether intermediate term algebraic simplification is used
            during matrix multiplications to control expression blowup and thus
            speed up calculation. Default is off.
        """
        ...
    
    @call_highest_priority('__sub__')
    def __rsub__(self, a):
        ...
    
    @call_highest_priority('__rsub__')
    def __sub__(self, a):
        ...
    
    def adjugate(self, method=...):
        ...
    
    def charpoly(self, x=..., simplify=...) -> Any:
        ...
    
    def cofactor(self, i, j, method=...):
        ...
    
    def cofactor_matrix(self, method=...):
        ...
    
    def det(self, method=..., iszerofunc=...) -> tuple[Any | Basic, bool] | Any | Basic | Order:
        ...
    
    def per(self):
        ...
    
    def minor(self, i, j, method=...):
        ...
    
    def minor_submatrix(self, i, j):
        ...
    
    def echelon_form(self, iszerofunc=..., simplify=..., with_pivots=...) -> tuple[Any, tuple[Any, ...]]:
        ...
    
    @property
    def is_echelon(self) -> bool:
        ...
    
    def rank(self, iszerofunc=..., simplify=...) -> int:
        ...
    
    def rref_rhs(self, rhs) -> tuple[Any, Any]:
        """Return reduced row-echelon form of matrix, matrix showing
        rhs after reduction steps. ``rhs`` must have the same number
        of rows as ``self``.

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> r1, r2 = symbols('r1 r2')
        >>> Matrix([[1, 1], [2, 1]]).rref_rhs(Matrix([r1, r2]))
        (Matrix([
        [1, 0],
        [0, 1]]), Matrix([
        [ -r1 + r2],
        [2*r1 - r2]]))
        """
        ...
    
    def rref(self, iszerofunc=..., simplify=..., pivots=..., normalize_last=...) -> tuple[Any, Any | tuple[Any, ...]]:
        ...
    
    def elementary_col_op(self, op=..., col=..., k=..., col1=..., col2=...) -> None:
        """Performs the elementary column operation `op`.

        `op` may be one of

            * ``"n->kn"`` (column n goes to k*n)
            * ``"n<->m"`` (swap column n and column m)
            * ``"n->n+km"`` (column n goes to column n + k*column m)

        Parameters
        ==========

        op : string; the elementary row operation
        col : the column to apply the column operation
        k : the multiple to apply in the column operation
        col1 : one column of a column swap
        col2 : second column of a column swap or column "m" in the column operation
               "n->n+km"
        """
        ...
    
    def elementary_row_op(self, op=..., row=..., k=..., row1=..., row2=...) -> None:
        """Performs the elementary row operation `op`.

        `op` may be one of

            * ``"n->kn"`` (row n goes to k*n)
            * ``"n<->m"`` (swap row n and row m)
            * ``"n->n+km"`` (row n goes to row n + k*row m)

        Parameters
        ==========

        op : string; the elementary row operation
        row : the row to apply the row operation
        k : the multiple to apply in the row operation
        row1 : one row of a row swap
        row2 : second row of a row swap or row "m" in the row operation
               "n->n+km"
        """
        ...
    
    def columnspace(self, simplify=...) -> list[Any]:
        ...
    
    def nullspace(self, simplify=..., iszerofunc=...) -> list[Any]:
        ...
    
    def rowspace(self, simplify=...) -> list[Any]:
        ...
    
    def orthogonalize(cls, *vecs, **kwargs) -> list[Any]:
        ...
    
    orthogonalize = ...
    def eigenvals(self, error_when_incomplete=..., **flags) -> list[Any] | dict[Any, Any] | dict[Any, int] | Any:
        ...
    
    def eigenvects(self, error_when_incomplete=..., iszerofunc=..., **flags) -> list[Any] | list[tuple[Any, Any, list[Any]]]:
        ...
    
    def is_diagonalizable(self, reals_only=..., **kwargs) -> bool:
        ...
    
    def diagonalize(self, reals_only=..., sort=..., normalize=...) -> tuple[Any, Any]:
        ...
    
    def bidiagonalize(self, upper=...):
        ...
    
    def bidiagonal_decomposition(self, upper=...) -> tuple[Any, Any, Any]:
        ...
    
    @property
    def is_positive_definite(self) -> bool:
        ...
    
    @property
    def is_positive_semidefinite(self) -> bool | None:
        ...
    
    @property
    def is_negative_definite(self) -> bool:
        ...
    
    @property
    def is_negative_semidefinite(self) -> bool | None:
        ...
    
    @property
    def is_indefinite(self) -> bool | None:
        ...
    
    def jordan_form(self, calc_transform=..., **kwargs) -> list[Any] | tuple[Any, ...]:
        ...
    
    def left_eigenvects(self, **flags) -> list[tuple[Any, Any, list[Any]]]:
        ...
    
    def singular_values(self) -> Any | list[Any]:
        ...
    
    def diff(self, *args, evaluate=..., **kwargs) -> ArrayDerivative:
        """Calculate the derivative of each element in the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.diff(x)
        Matrix([
        [1, 0],
        [0, 0]])

        See Also
        ========

        integrate
        limit
        """
        ...
    
    def integrate(self, *args, **kwargs):
        """Integrate each element of the matrix.  ``args`` will
        be passed to the ``integrate`` function.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.integrate((x, ))
        Matrix([
        [x**2/2, x*y],
        [     x,   0]])
        >>> M.integrate((x, 0, 2))
        Matrix([
        [2, 2*y],
        [2,   0]])

        See Also
        ========

        limit
        diff
        """
        ...
    
    def jacobian(self, X):
        """Calculates the Jacobian matrix (derivative of a vector-valued function).

        Parameters
        ==========

        ``self`` : vector of expressions representing functions f_i(x_1, ..., x_n).
        X : set of x_i's in order, it can be a list or a Matrix

        Both ``self`` and X can be a row or a column matrix in any order
        (i.e., jacobian() should always work).

        Examples
        ========

        >>> from sympy import sin, cos, Matrix
        >>> from sympy.abc import rho, phi
        >>> X = Matrix([rho*cos(phi), rho*sin(phi), rho**2])
        >>> Y = Matrix([rho, phi])
        >>> X.jacobian(Y)
        Matrix([
        [cos(phi), -rho*sin(phi)],
        [sin(phi),  rho*cos(phi)],
        [   2*rho,             0]])
        >>> X = Matrix([rho*cos(phi), rho*sin(phi)])
        >>> X.jacobian(Y)
        Matrix([
        [cos(phi), -rho*sin(phi)],
        [sin(phi),  rho*cos(phi)]])

        See Also
        ========

        hessian
        wronskian
        """
        ...
    
    def limit(self, *args):
        """Calculate the limit of each element in the matrix.
        ``args`` will be passed to the ``limit`` function.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.limit(x, 2)
        Matrix([
        [2, y],
        [1, 0]])

        See Also
        ========

        integrate
        diff
        """
        ...
    
    def berkowitz_charpoly(self, x=..., simplify=...) -> Any:
        ...
    
    def berkowitz_det(self) -> tuple[Any | Basic, bool] | Any | Basic | Order:
        """Computes determinant using Berkowitz method.

        See Also
        ========

        det
        """
        ...
    
    def berkowitz_eigenvals(self, **flags) -> list[Any] | dict[Any, Any] | dict[Any, int] | Any:
        """Computes eigenvalues of a Matrix using Berkowitz method."""
        ...
    
    def berkowitz_minors(self) -> tuple[Any, ...]:
        """Computes principal minors using Berkowitz method."""
        ...
    
    def berkowitz(self) -> tuple[tuple[Literal[1]]] | tuple[tuple[Literal[1]], *tuple[tuple[Any, ...], ...]]:
        ...
    
    def cofactorMatrix(self, method=...):
        ...
    
    def det_bareis(self):
        ...
    
    def det_LU_decomposition(self) -> tuple[Any | Basic, bool] | Any | Basic | Order:
        """Compute matrix determinant using LU decomposition.


        Note that this method fails if the LU decomposition itself
        fails. In particular, if the matrix has no inverse this method
        will fail.

        TODO: Implement algorithm for sparse matrices (SFF),
        http://www.eecis.udel.edu/~saunders/papers/sffge/it5.ps.

        See Also
        ========


        det
        berkowitz_det
        """
        ...
    
    def jordan_cell(self, eigenval, n):
        ...
    
    def jordan_cells(self, calc_transformation=...) -> tuple[Any, Any]:
        ...
    
    def minorEntry(self, i, j, method=...):
        ...
    
    def minorMatrix(self, i, j):
        ...
    
    def permuteBkwd(self, perm) -> None:
        """Permute the rows of the matrix with the given permutation in reverse."""
        ...
    
    def permuteFwd(self, perm) -> None:
        """Permute the rows of the matrix with the given permutation."""
        ...
    
    @property
    def kind(self) -> MatrixKind:
        ...
    
    def flat(self) -> list[Any]:
        ...
    
    def __array__(self, dtype=...) -> NDArray[Any, Any]:
        ...
    
    def __len__(self) -> int:
        """Return the number of elements of ``self``.

        Implemented mainly so bool(Matrix()) == False.
        """
        ...
    
    def __str__(self) -> str:
        ...
    
    @classmethod
    def irregular(cls, ntop, *matrices, **kwargs):
        """Return a matrix filled by the given matrices which
      are listed in order of appearance from left to right, top to
      bottom as they first appear in the matrix. They must fill the
      matrix completely.

      Examples
      ========

      >>> from sympy import ones, Matrix
      >>> Matrix.irregular(3, ones(2,1), ones(3,3)*2, ones(2,2)*3,
      ...   ones(1,1)*4, ones(2,2)*5, ones(1,2)*6, ones(1,2)*7)
      Matrix([
        [1, 2, 2, 2, 3, 3],
        [1, 2, 2, 2, 3, 3],
        [4, 2, 2, 2, 5, 5],
        [6, 6, 7, 7, 5, 5]])
      """
        ...
    
    def add(self, b):
        """Return self + b."""
        ...
    
    def condition_number(self):
        """Returns the condition number of a matrix.

        This is the maximum singular value divided by the minimum singular value

        Examples
        ========

        >>> from sympy import Matrix, S
        >>> A = Matrix([[1, 0, 0], [0, 10, 0], [0, 0, S.One/10]])
        >>> A.condition_number()
        100

        See Also
        ========

        singular_values
        """
        ...
    
    def copy(self):
        """
        Returns the copy of a matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.copy()
        Matrix([
        [1, 2],
        [3, 4]])

        """
        ...
    
    def cross(self, b):
        r"""
        Return the cross product of ``self`` and ``b`` relaxing the condition
        of compatible dimensions: if each has 3 elements, a matrix of the
        same type and shape as ``self`` will be returned. If ``b`` has the same
        shape as ``self`` then common identities for the cross product (like
        `a \times b = - b \times a`) will hold.

        Parameters
        ==========
            b : 3x1 or 1x3 Matrix

        See Also
        ========

        dot
        hat
        vee
        multiply
        multiply_elementwise
        """
        ...
    
    def hat(self):
        r"""
        Return the skew-symmetric matrix representing the cross product,
        so that ``self.hat() * b`` is equivalent to  ``self.cross(b)``.

        Examples
        ========

        Calling ``hat`` creates a skew-symmetric 3x3 Matrix from a 3x1 Matrix:

        >>> from sympy import Matrix
        >>> a = Matrix([1, 2, 3])
        >>> a.hat()
        Matrix([
        [ 0, -3,  2],
        [ 3,  0, -1],
        [-2,  1,  0]])

        Multiplying it with another 3x1 Matrix calculates the cross product:

        >>> b = Matrix([3, 2, 1])
        >>> a.hat() * b
        Matrix([
        [-4],
        [ 8],
        [-4]])

        Which is equivalent to calling the ``cross`` method:

        >>> a.cross(b)
        Matrix([
        [-4],
        [ 8],
        [-4]])

        See Also
        ========

        dot
        cross
        vee
        multiply
        multiply_elementwise
        """
        ...
    
    def vee(self):
        r"""
        Return a 3x1 vector from a skew-symmetric matrix representing the cross product,
        so that ``self * b`` is equivalent to  ``self.vee().cross(b)``.

        Examples
        ========

        Calling ``vee`` creates a vector from a skew-symmetric Matrix:

        >>> from sympy import Matrix
        >>> A = Matrix([[0, -3, 2], [3, 0, -1], [-2, 1, 0]])
        >>> a = A.vee()
        >>> a
        Matrix([
        [1],
        [2],
        [3]])

        Calculating the matrix product of the original matrix with a vector
        is equivalent to a cross product:

        >>> b = Matrix([3, 2, 1])
        >>> A * b
        Matrix([
        [-4],
        [ 8],
        [-4]])

        >>> a.cross(b)
        Matrix([
        [-4],
        [ 8],
        [-4]])

        ``vee`` can also be used to retrieve angular velocity expressions.
        Defining a rotation matrix:

        >>> from sympy import rot_ccw_axis3, trigsimp
        >>> from sympy.physics.mechanics import dynamicsymbols
        >>> theta = dynamicsymbols('theta')
        >>> R = rot_ccw_axis3(theta)
        >>> R
        Matrix([
        [cos(theta(t)), -sin(theta(t)), 0],
        [sin(theta(t)),  cos(theta(t)), 0],
        [            0,              0, 1]])

        We can retrive the angular velocity:

        >>> Omega = R.T * R.diff()
        >>> Omega = trigsimp(Omega)
        >>> Omega.vee()
        Matrix([
        [                      0],
        [                      0],
        [Derivative(theta(t), t)]])

        See Also
        ========

        dot
        cross
        hat
        multiply
        multiply_elementwise
        """
        ...
    
    @property
    def D(self):
        """Return Dirac conjugate (if ``self.rows == 4``).

        Examples
        ========

        >>> from sympy import Matrix, I, eye
        >>> m = Matrix((0, 1 + I, 2, 3))
        >>> m.D
        Matrix([[0, 1 - I, -2, -3]])
        >>> m = (eye(4) + I*eye(4))
        >>> m[0, 3] = 2
        >>> m.D
        Matrix([
        [1 - I,     0,      0,      0],
        [    0, 1 - I,      0,      0],
        [    0,     0, -1 + I,      0],
        [    2,     0,      0, -1 + I]])

        If the matrix does not have 4 rows an AttributeError will be raised
        because this property is only defined for matrices with 4 rows.

        >>> Matrix(eye(2)).D
        Traceback (most recent call last):
        ...
        AttributeError: Matrix has no attribute D.

        See Also
        ========

        sympy.matrices.matrixbase.MatrixBase.conjugate: By-element conjugation
        sympy.matrices.matrixbase.MatrixBase.H: Hermite conjugation
        """
        ...
    
    def dot(self, b, hermitian=..., conjugate_convention=...) -> Any:
        """Return the dot or inner product of two vectors of equal length.
        Here ``self`` must be a ``Matrix`` of size 1 x n or n x 1, and ``b``
        must be either a matrix of size 1 x n, n x 1, or a list/tuple of length n.
        A scalar is returned.

        By default, ``dot`` does not conjugate ``self`` or ``b``, even if there are
        complex entries. Set ``hermitian=True`` (and optionally a ``conjugate_convention``)
        to compute the hermitian inner product.

        Possible kwargs are ``hermitian`` and ``conjugate_convention``.

        If ``conjugate_convention`` is ``"left"``, ``"math"`` or ``"maths"``,
        the conjugate of the first vector (``self``) is used.  If ``"right"``
        or ``"physics"`` is specified, the conjugate of the second vector ``b`` is used.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> v = Matrix([1, 1, 1])
        >>> M.row(0).dot(v)
        6
        >>> M.col(0).dot(v)
        12
        >>> v = [3, 2, 1]
        >>> M.row(0).dot(v)
        10

        >>> from sympy import I
        >>> q = Matrix([1*I, 1*I, 1*I])
        >>> q.dot(q, hermitian=False)
        -3

        >>> q.dot(q, hermitian=True)
        3

        >>> q1 = Matrix([1, 1, 1*I])
        >>> q.dot(q1, hermitian=True, conjugate_convention="maths")
        1 - 2*I
        >>> q.dot(q1, hermitian=True, conjugate_convention="physics")
        1 + 2*I


        See Also
        ========

        cross
        multiply
        multiply_elementwise
        """
        ...
    
    def dual(self):
        """Returns the dual of a matrix.

        A dual of a matrix is:

        ``(1/2)*levicivita(i, j, k, l)*M(k, l)`` summed over indices `k` and `l`

        Since the levicivita method is anti_symmetric for any pairwise
        exchange of indices, the dual of a symmetric matrix is the zero
        matrix. Strictly speaking the dual defined here assumes that the
        'matrix' `M` is a contravariant anti_symmetric second rank tensor,
        so that the dual is a covariant second rank tensor.

        """
        ...
    
    def analytic_func(self, f, x):
        """
        Computes f(A) where A is a Square Matrix
        and f is an analytic function.

        Examples
        ========

        >>> from sympy import Symbol, Matrix, S, log

        >>> x = Symbol('x')
        >>> m = Matrix([[S(5)/4, S(3)/4], [S(3)/4, S(5)/4]])
        >>> f = log(x)
        >>> m.analytic_func(f, x)
        Matrix([
        [     0, log(2)],
        [log(2),      0]])

        Parameters
        ==========

        f : Expr
            Analytic Function
        x : Symbol
            parameter of f

        """
        ...
    
    def exp(self) -> Self:
        """Return the exponential of a square matrix.

        Examples
        ========

        >>> from sympy import Symbol, Matrix

        >>> t = Symbol('t')
        >>> m = Matrix([[0, 1], [-1, 0]]) * t
        >>> m.exp()
        Matrix([
        [    exp(I*t)/2 + exp(-I*t)/2, -I*exp(I*t)/2 + I*exp(-I*t)/2],
        [I*exp(I*t)/2 - I*exp(-I*t)/2,      exp(I*t)/2 + exp(-I*t)/2]])
        """
        ...
    
    def log(self, simplify=...) -> Self:
        """Return the logarithm of a square matrix.

        Parameters
        ==========

        simplify : function, bool
            The function to simplify the result with.

            Default is ``cancel``, which is effective to reduce the
            expression growing for taking reciprocals and inverses for
            symbolic matrices.

        Examples
        ========

        >>> from sympy import S, Matrix

        Examples for positive-definite matrices:

        >>> m = Matrix([[1, 1], [0, 1]])
        >>> m.log()
        Matrix([
        [0, 1],
        [0, 0]])

        >>> m = Matrix([[S(5)/4, S(3)/4], [S(3)/4, S(5)/4]])
        >>> m.log()
        Matrix([
        [     0, log(2)],
        [log(2),      0]])

        Examples for non positive-definite matrices:

        >>> m = Matrix([[S(3)/4, S(5)/4], [S(5)/4, S(3)/4]])
        >>> m.log()
        Matrix([
        [         I*pi/2, log(2) - I*pi/2],
        [log(2) - I*pi/2,          I*pi/2]])

        >>> m = Matrix(
        ...     [[0, 0, 0, 1],
        ...      [0, 0, 1, 0],
        ...      [0, 1, 0, 0],
        ...      [1, 0, 0, 0]])
        >>> m.log()
        Matrix([
        [ I*pi/2,       0,       0, -I*pi/2],
        [      0,  I*pi/2, -I*pi/2,       0],
        [      0, -I*pi/2,  I*pi/2,       0],
        [-I*pi/2,       0,       0,  I*pi/2]])
        """
        ...
    
    def is_nilpotent(self) -> bool:
        """Checks if a matrix is nilpotent.

        A matrix B is nilpotent if for some integer k, B**k is
        a zero matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
        >>> a.is_nilpotent()
        True

        >>> a = Matrix([[1, 0, 1], [1, 0, 0], [1, 1, 0]])
        >>> a.is_nilpotent()
        False
        """
        ...
    
    def key2bounds(self, keys) -> tuple[Any | int, Any | int, Any | int, Any | int]:
        """Converts a key with potentially mixed types of keys (integer and slice)
        into a tuple of ranges and raises an error if any index is out of ``self``'s
        range.

        See Also
        ========

        key2ij
        """
        ...
    
    def key2ij(self, key) -> list[int | slice] | tuple[int, int]:
        """Converts key into canonical form, converting integers or indexable
        items into valid integers for ``self``'s range or returning slices
        unchanged.

        See Also
        ========

        key2bounds
        """
        ...
    
    def normalized(self, iszerofunc=...):
        """Return the normalized version of ``self``.

        Parameters
        ==========

        iszerofunc : Function, optional
            A function to determine whether ``self`` is a zero vector.
            The default ``_iszero`` tests to see if each element is
            exactly zero.

        Returns
        =======

        Matrix
            Normalized vector form of ``self``.
            It has the same length as a unit vector. However, a zero vector
            will be returned for a vector with norm 0.

        Raises
        ======

        ShapeError
            If the matrix is not in a vector form.

        See Also
        ========

        norm
        """
        ...
    
    def norm(self, ord=...) -> Pow | Order | Max | Min:
        """Return the Norm of a Matrix or Vector.

        In the simplest case this is the geometric size of the vector
        Other norms can be specified by the ord parameter


        =====  ============================  ==========================
        ord    norm for matrices             norm for vectors
        =====  ============================  ==========================
        None   Frobenius norm                2-norm
        'fro'  Frobenius norm                - does not exist
        inf    maximum row sum               max(abs(x))
        -inf   --                            min(abs(x))
        1      maximum column sum            as below
        -1     --                            as below
        2      2-norm (largest sing. value)  as below
        -2     smallest singular value       as below
        other  - does not exist              sum(abs(x)**ord)**(1./ord)
        =====  ============================  ==========================

        Examples
        ========

        >>> from sympy import Matrix, Symbol, trigsimp, cos, sin, oo
        >>> x = Symbol('x', real=True)
        >>> v = Matrix([cos(x), sin(x)])
        >>> trigsimp( v.norm() )
        1
        >>> v.norm(10)
        (sin(x)**10 + cos(x)**10)**(1/10)
        >>> A = Matrix([[1, 1], [1, 1]])
        >>> A.norm(1) # maximum sum of absolute values of A is 2
        2
        >>> A.norm(2) # Spectral norm (max of |Ax|/|x| under 2-vector-norm)
        2
        >>> A.norm(-2) # Inverse spectral norm (smallest singular value)
        0
        >>> A.norm() # Frobenius Norm
        2
        >>> A.norm(oo) # Infinity Norm
        2
        >>> Matrix([1, -2]).norm(oo)
        2
        >>> Matrix([-1, 2]).norm(-oo)
        1

        See Also
        ========

        normalized
        """
        ...
    
    def print_nonzero(self, symb=...) -> None:
        """Shows location of non-zero entries for fast shape lookup.

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> m = Matrix(2, 3, lambda i, j: i*3+j)
        >>> m
        Matrix([
        [0, 1, 2],
        [3, 4, 5]])
        >>> m.print_nonzero()
        [ XX]
        [XXX]
        >>> m = eye(4)
        >>> m.print_nonzero("x")
        [x   ]
        [ x  ]
        [  x ]
        [   x]

        """
        ...
    
    def project(self, v):
        """Return the projection of ``self`` onto the line containing ``v``.

        Examples
        ========

        >>> from sympy import Matrix, S, sqrt
        >>> V = Matrix([sqrt(3)/2, S.Half])
        >>> x = Matrix([[1, 0]])
        >>> V.project(x)
        Matrix([[sqrt(3)/2, 0]])
        >>> V.project(-x)
        Matrix([[sqrt(3)/2, 0]])
        """
        ...
    
    def table(self, printer, rowstart=..., rowend=..., rowsep=..., colsep=..., align=...) -> str:
        r"""
        String form of Matrix as a table.

        ``printer`` is the printer to use for on the elements (generally
        something like StrPrinter())

        ``rowstart`` is the string used to start each row (by default '[').

        ``rowend`` is the string used to end each row (by default ']').

        ``rowsep`` is the string used to separate rows (by default a newline).

        ``colsep`` is the string used to separate columns (by default ', ').

        ``align`` defines how the elements are aligned. Must be one of 'left',
        'right', or 'center'.  You can also use '<', '>', and '^' to mean the
        same thing, respectively.

        This is used by the string printer for Matrix.

        Examples
        ========

        >>> from sympy import Matrix, StrPrinter
        >>> M = Matrix([[1, 2], [-33, 4]])
        >>> printer = StrPrinter()
        >>> M.table(printer)
        '[  1, 2]\n[-33, 4]'
        >>> print(M.table(printer))
        [  1, 2]
        [-33, 4]
        >>> print(M.table(printer, rowsep=',\n'))
        [  1, 2],
        [-33, 4]
        >>> print('[%s]' % M.table(printer, rowsep=',\n'))
        [[  1, 2],
        [-33, 4]]
        >>> print(M.table(printer, colsep=' '))
        [  1 2]
        [-33 4]
        >>> print(M.table(printer, align='center'))
        [ 1 , 2]
        [-33, 4]
        >>> print(M.table(printer, rowstart='{', rowend='}'))
        {  1, 2}
        {-33, 4}
        """
        ...
    
    def rank_decomposition(self, iszerofunc=..., simplify=...) -> tuple[Any, Any]:
        ...
    
    def cholesky(self, hermitian=...):
        ...
    
    def LDLdecomposition(self, hermitian=...):
        ...
    
    def LUdecomposition(self, iszerofunc=..., simpfunc=..., rankcheck=...) -> tuple[Any, Any, list[Any]]:
        ...
    
    def LUdecomposition_Simple(self, iszerofunc=..., simpfunc=..., rankcheck=...) -> tuple[Any, list[Any]]:
        ...
    
    def LUdecompositionFF(self) -> tuple[Any, Any, Any, Any]:
        ...
    
    def singular_value_decomposition(self) -> tuple[Any, Any, Any]:
        ...
    
    def QRdecomposition(self) -> tuple[Any, Any]:
        ...
    
    def upper_hessenberg_decomposition(self) -> tuple[Any, Any]:
        ...
    
    def diagonal_solve(self, rhs):
        ...
    
    def lower_triangular_solve(self, rhs):
        ...
    
    def upper_triangular_solve(self, rhs):
        ...
    
    def cholesky_solve(self, rhs):
        ...
    
    def LDLsolve(self, rhs):
        ...
    
    def LUsolve(self, rhs, iszerofunc=...):
        ...
    
    def QRsolve(self, b) -> Any:
        ...
    
    def gauss_jordan_solve(self, B, freevar=...) -> tuple[Self, Self, list[int]] | tuple[Self, Self]:
        ...
    
    def pinv_solve(self, B, arbitrary_matrix=...):
        ...
    
    def cramer_solve(self, rhs, det_method=...) -> Self:
        ...
    
    def solve(self, rhs, method=...):
        ...
    
    def solve_least_squares(self, rhs, method=...) -> Any:
        ...
    
    def pinv(self, method=...):
        ...
    
    def inverse_ADJ(self, iszerofunc=...):
        ...
    
    def inverse_BLOCK(self, iszerofunc=...) -> SparseMatrix | ImmutableDenseMatrix:
        ...
    
    def inverse_GE(self, iszerofunc=...):
        ...
    
    def inverse_LU(self, iszerofunc=...):
        ...
    
    def inverse_CH(self, iszerofunc=...):
        ...
    
    def inverse_LDL(self, iszerofunc=...):
        ...
    
    def inverse_QR(self, iszerofunc=...) -> Any:
        ...
    
    def inv(self, method=..., iszerofunc=..., try_block_diag=...) -> SparseMatrix:
        ...
    
    def connected_components(self) -> list[Any]:
        ...
    
    def connected_components_decomposition(self) -> tuple[PermutationMatrix, BlockDiagMatrix]:
        ...
    
    def strongly_connected_components(self) -> Any | list[Any]:
        ...
    
    def strongly_connected_components_decomposition(self, lower=...) -> tuple[PermutationMatrix, BlockMatrix]:
        ...
    
    _sage_ = ...


def classof(A, B):
    """
    Get the type of the result when combining matrices of different types.

    Currently the strategy is that immutability is contagious.

    Examples
    ========

    >>> from sympy import Matrix, ImmutableMatrix
    >>> from sympy.matrices.matrixbase import classof
    >>> M = Matrix([[1, 2], [3, 4]]) # a Mutable Matrix
    >>> IM = ImmutableMatrix([[1, 2], [3, 4]])
    >>> classof(M, IM)
    <class 'sympy.matrices.immutable.ImmutableDenseMatrix'>
    """
    ...

def a2idx(j, n=...) -> int:
    """Return integer after making positive and validating against n."""
    ...

class DeferredVector(Symbol, NotIterable):
    """A vector whose components are deferred (e.g. for use with lambdify).

    Examples
    ========

    >>> from sympy import DeferredVector, lambdify
    >>> X = DeferredVector( 'X' )
    >>> X
    X
    >>> expr = (X[0] + 2, X[2] + 3)
    >>> func = lambdify( X, expr)
    >>> func( [1, 2, 3] )
    (3, 6)
    """
    def __getitem__(self, i) -> Symbol:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    


