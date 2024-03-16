from sympy.core.decorators import call_highest_priority
from sympy.core.expr import Expr
from sympy.core.logic import FuzzyBool
from sympy.matrices.kind import MatrixKind

class MatrixExpr(Expr):
    """Superclass for Matrix Expressions

    MatrixExprs represent abstract matrices, linear transformations represented
    within a particular basis.

    Examples
    ========

    >>> from sympy import MatrixSymbol
    >>> A = MatrixSymbol('A', 3, 3)
    >>> y = MatrixSymbol('y', 3, 1)
    >>> x = (A.T*A).I * A * y

    See Also
    ========

    MatrixSymbol, MatAdd, MatMul, Transpose, Inverse
    """
    __slots__: tuple[str, ...] = ...
    _iterable = ...
    _op_priority = ...
    is_Matrix: bool = ...
    is_MatrixExpr: bool = ...
    is_Identity: FuzzyBool = ...
    is_Inverse = ...
    is_Transpose = ...
    is_ZeroMatrix = ...
    is_MatAdd = ...
    is_MatMul = ...
    is_commutative = ...
    is_number = ...
    is_symbol = ...
    is_scalar = ...
    kind: MatrixKind = ...
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Expr, Expr]:
        ...
    
    def __neg__(self) -> GenericIdentity | Order | object:
        ...
    
    def __abs__(self):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__radd__')
    def __add__(self, other) -> MatAdd | GenericZeroMatrix:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__add__')
    def __radd__(self, other) -> MatAdd | GenericZeroMatrix:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rsub__')
    def __sub__(self, other) -> MatAdd | GenericZeroMatrix:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__sub__')
    def __rsub__(self, other) -> MatAdd | GenericZeroMatrix:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rmul__')
    def __mul__(self, other) -> GenericIdentity | Order | object:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rmul__')
    def __matmul__(self, other) -> GenericIdentity | Order | object:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__mul__')
    def __rmul__(self, other) -> GenericIdentity | Order | object:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__mul__')
    def __rmatmul__(self, other) -> GenericIdentity | Order | object:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rpow__')
    def __pow__(self, other) -> Inverse | Basic | Identity | Any | MatPow:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__pow__')
    def __rpow__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rtruediv__')
    def __truediv__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__truediv__')
    def __rtruediv__(self, other):
        ...
    
    @property
    def rows(self) -> Expr:
        ...
    
    @property
    def cols(self) -> Expr:
        ...
    
    @property
    def is_square(self) -> bool | None:
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]:
        ...
    
    def adjoint(self) -> type[UndefinedFunction]:
        ...
    
    def as_coeff_Mul(self, rational=...) -> tuple[Any, Self]:
        """Efficiently extract the coefficient of a product."""
        ...
    
    def conjugate(self) -> type[UndefinedFunction]:
        ...
    
    def transpose(self) -> Any | Transpose:
        ...
    
    @property
    def T(self) -> Any | Transpose:
        '''Matrix transposition'''
        ...
    
    def inverse(self) -> Inverse:
        ...
    
    def inv(self) -> Inverse:
        ...
    
    def det(self) -> Determinant:
        ...
    
    @property
    def I(self) -> Inverse:
        ...
    
    def valid_index(self, i, j) -> Literal[False]:
        ...
    
    def __getitem__(self, key) -> MatrixSlice:
        ...
    
    def as_explicit(self) -> ImmutableDenseMatrix:
        """
        Returns a dense Matrix with elements represented explicitly

        Returns an object of type ImmutableDenseMatrix.

        Examples
        ========

        >>> from sympy import Identity
        >>> I = Identity(3)
        >>> I
        I
        >>> I.as_explicit()
        Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        as_mutable: returns mutable Matrix type

        """
        ...
    
    def as_mutable(self) -> Matrix:
        """
        Returns a dense, mutable matrix with elements represented explicitly

        Examples
        ========

        >>> from sympy import Identity
        >>> I = Identity(3)
        >>> I
        I
        >>> I.shape
        (3, 3)
        >>> I.as_mutable()
        Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        as_explicit: returns ImmutableDenseMatrix
        """
        ...
    
    def __array__(self):
        ...
    
    def equals(self, other) -> bool:
        """
        Test elementwise equality between matrices, potentially of different
        types

        >>> from sympy import Identity, eye
        >>> Identity(3).equals(eye(3))
        True
        """
        ...
    
    def canonicalize(self) -> Self:
        ...
    
    def as_coeff_mmul(self) -> tuple[Any, GenericIdentity | Any | Order | object | MatMul]:
        ...
    
    @staticmethod
    def from_index_summation(expr, first_index=..., last_index=..., dimensions=...):
        r"""
        Parse expression of matrices with explicitly summed indices into a
        matrix expression without indices, if possible.

        This transformation expressed in mathematical notation:

        `\sum_{j=0}^{N-1} A_{i,j} B_{j,k} \Longrightarrow \mathbf{A}\cdot \mathbf{B}`

        Optional parameter ``first_index``: specify which free index to use as
        the index starting the expression.

        Examples
        ========

        >>> from sympy import MatrixSymbol, MatrixExpr, Sum
        >>> from sympy.abc import i, j, k, l, N
        >>> A = MatrixSymbol("A", N, N)
        >>> B = MatrixSymbol("B", N, N)
        >>> expr = Sum(A[i, j]*B[j, k], (j, 0, N-1))
        >>> MatrixExpr.from_index_summation(expr)
        A*B

        Transposition is detected:

        >>> expr = Sum(A[j, i]*B[j, k], (j, 0, N-1))
        >>> MatrixExpr.from_index_summation(expr)
        A.T*B

        Detect the trace:

        >>> expr = Sum(A[i, i], (i, 0, N-1))
        >>> MatrixExpr.from_index_summation(expr)
        Trace(A)

        More complicated expressions:

        >>> expr = Sum(A[i, j]*B[k, j]*A[l, k], (j, 0, N-1), (k, 0, N-1))
        >>> MatrixExpr.from_index_summation(expr)
        A*B.T*A.T
        """
        ...
    
    def applyfunc(self, func) -> MatrixExpr | ElementwiseApplyFunction:
        ...
    


def get_postprocessor(cls) -> Callable[..., Any]:
    ...

class MatrixElement(Expr):
    parent = ...
    i = ...
    j = ...
    _diff_wrt = ...
    is_symbol = ...
    is_commutative = ...
    def __new__(cls, name, n, m) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    def doit(self, **hints):
        ...
    
    @property
    def indices(self) -> tuple[Basic, ...]:
        ...
    


class MatrixSymbol(MatrixExpr):
    """Symbolic representation of a Matrix object

    Creates a SymPy Symbol to represent a Matrix. This matrix has a shape and
    can be included in Matrix Expressions

    Examples
    ========

    >>> from sympy import MatrixSymbol, Identity
    >>> A = MatrixSymbol('A', 3, 4) # A 3 by 4 Matrix
    >>> B = MatrixSymbol('B', 4, 3) # A 4 by 3 Matrix
    >>> A.shape
    (3, 4)
    >>> 2*A*B + Identity(3)
    I + 2*A*B
    """
    is_commutative = ...
    is_symbol = ...
    _diff_wrt = ...
    def __new__(cls, name, n, m) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, Basic]:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def free_symbols(self) -> set[Self]:
        ...
    


def matrix_symbols(expr) -> list[Any]:
    ...

class _LeftRightArgs:
    r"""
    Helper class to compute matrix derivatives.

    The logic: when an expression is derived by a matrix `X_{mn}`, two lines of
    matrix multiplications are created: the one contracted to `m` (first line),
    and the one contracted to `n` (second line).

    Transposition flips the side by which new matrices are connected to the
    lines.

    The trace connects the end of the two lines.
    """
    def __init__(self, lines, higher=...) -> None:
        ...
    
    @property
    def first_pointer(self):
        ...
    
    @first_pointer.setter
    def first_pointer(self, value) -> None:
        ...
    
    @property
    def second_pointer(self):
        ...
    
    @second_pointer.setter
    def second_pointer(self, value) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def transpose(self) -> Self:
        ...
    
    def build(self) -> list[Any]:
        ...
    
    def matrix_form(self) -> Literal[1]:
        ...
    
    def rank(self) -> int:
        """
        Number of dimensions different from trivial (warning: not related to
        matrix rank).
        """
        ...
    
    def append_first(self, other) -> None:
        ...
    
    def append_second(self, other) -> None:
        ...
    


