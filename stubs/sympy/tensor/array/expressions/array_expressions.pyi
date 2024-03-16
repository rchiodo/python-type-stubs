import typing
from typing import List, Optional, Tuple as tTuple
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.expr import Expr

class _ArrayExpr(Expr):
    shape: tTuple[Expr, ...]
    def __getitem__(self, item) -> ArrayElement:
        ...
    


class ArraySymbol(_ArrayExpr):
    """
    Symbol representing an array expression
    """
    def __new__(cls, symbol, shape: typing.Iterable) -> ArraySymbol:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    @property
    def shape(self) -> Basic:
        ...
    
    def as_explicit(self) -> ImmutableDenseNDimArray:
        ...
    


class ArrayElement(Expr):
    """
    An element of an array.
    """
    _diff_wrt = ...
    is_symbol = ...
    is_commutative = ...
    def __new__(cls, name, indices) -> Self:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    @property
    def indices(self) -> Basic:
        ...
    


class ZeroArray(_ArrayExpr):
    """
    Symbolic array of zeros. Equivalent to ``ZeroMatrix`` for matrices.
    """
    def __new__(cls, *shape) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    def as_explicit(self):
        ...
    


class OneArray(_ArrayExpr):
    """
    Symbolic array of ones.
    """
    def __new__(cls, *shape) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    def as_explicit(self) -> ImmutableDenseNDimArray:
        ...
    


class _CodegenArrayAbstract(Basic):
    @property
    def subranks(self):
        """
        Returns the ranks of the objects in the uppermost tensor product inside
        the current object.  In case no tensor products are contained, return
        the atomic ranks.

        Examples
        ========

        >>> from sympy.tensor.array import tensorproduct, tensorcontraction
        >>> from sympy import MatrixSymbol
        >>> M = MatrixSymbol("M", 3, 3)
        >>> N = MatrixSymbol("N", 3, 3)
        >>> P = MatrixSymbol("P", 3, 3)

        Important: do not confuse the rank of the matrix with the rank of an array.

        >>> tp = tensorproduct(M, N, P)
        >>> tp.subranks
        [2, 2, 2]

        >>> co = tensorcontraction(tp, (1, 2), (3, 4))
        >>> co.subranks
        [2, 2, 2]
        """
        ...
    
    def subrank(self) -> int:
        """
        The sum of ``subranks``.
        """
        ...
    
    @property
    def shape(self):
        ...
    
    def doit(self, **hints):
        ...
    


class ArrayTensorProduct(_CodegenArrayAbstract):
    r"""
    Class to represent the tensor product of array-like objects.
    """
    def __new__(cls, *args, **kwargs) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | Self:
        ...
    
    def as_explicit(self) -> NDimArray | ImmutableDenseNDimArray | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ImmutableSparseNDimArray:
        ...
    


class ArrayAdd(_CodegenArrayAbstract):
    r"""
    Class for elementwise array additions.
    """
    def __new__(cls, *args, **kwargs) -> ZeroArray | Self:
        ...
    
    def as_explicit(self) -> Any:
        ...
    


class PermuteDims(_CodegenArrayAbstract):
    r"""
    Class to represent permutation of axes of arrays.

    Examples
    ========

    >>> from sympy.tensor.array import permutedims
    >>> from sympy import MatrixSymbol
    >>> M = MatrixSymbol("M", 3, 3)
    >>> cg = permutedims(M, [1, 0])

    The object ``cg`` represents the transposition of ``M``, as the permutation
    ``[1, 0]`` will act on its indices by switching them:

    `M_{ij} \Rightarrow M_{ji}`

    This is evident when transforming back to matrix form:

    >>> from sympy.tensor.array.expressions.from_array_to_matrix import convert_array_to_matrix
    >>> convert_array_to_matrix(cg)
    M.T

    >>> N = MatrixSymbol("N", 3, 2)
    >>> cg = permutedims(N, [1, 0])
    >>> cg.shape
    (2, 3)

    There are optional parameters that can be used as alternative to the permutation:

    >>> from sympy.tensor.array.expressions import ArraySymbol, PermuteDims
    >>> M = ArraySymbol("M", (1, 2, 3, 4, 5))
    >>> expr = PermuteDims(M, index_order_old="ijklm", index_order_new="kijml")
    >>> expr
    PermuteDims(M, (0 2 1)(3 4))
    >>> expr.shape
    (3, 1, 2, 5, 4)

    Permutations of tensor products are simplified in order to achieve a
    standard form:

    >>> from sympy.tensor.array import tensorproduct
    >>> M = MatrixSymbol("M", 4, 5)
    >>> tp = tensorproduct(M, N)
    >>> tp.shape
    (4, 5, 3, 2)
    >>> perm1 = permutedims(tp, [2, 3, 1, 0])

    The args ``(M, N)`` have been sorted and the permutation has been
    simplified, the expression is equivalent:

    >>> perm1.expr.args
    (N, M)
    >>> perm1.shape
    (3, 2, 5, 4)
    >>> perm1.permutation
    (2 3)

    The permutation in its array form has been simplified from
    ``[2, 3, 1, 0]`` to ``[0, 1, 3, 2]``, as the arguments of the tensor
    product `M` and `N` have been switched:

    >>> perm1.permutation.array_form
    [0, 1, 3, 2]

    We can nest a second permutation:

    >>> perm2 = permutedims(perm1, [1, 0, 2, 3])
    >>> perm2.shape
    (2, 3, 5, 4)
    >>> perm2.permutation.array_form
    [1, 0, 3, 2]
    """
    def __new__(cls, expr, permutation=..., index_order_old=..., index_order_new=..., **kwargs) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | Self:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def permutation(self) -> Basic:
        ...
    
    def nest_permutation(self) -> Self | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ArrayAdd:
        r"""
        DEPRECATED.
        """
        ...
    
    def as_explicit(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        ...
    


class ArrayDiagonal(_CodegenArrayAbstract):
    r"""
    Class to represent the diagonal operator.

    Explanation
    ===========

    In a 2-dimensional array it returns the diagonal, this looks like the
    operation:

    `A_{ij} \rightarrow A_{ii}`

    The diagonal over axes 1 and 2 (the second and third) of the tensor product
    of two 2-dimensional arrays `A \otimes B` is

    `\Big[ A_{ab} B_{cd} \Big]_{abcd} \rightarrow \Big[ A_{ai} B_{id} \Big]_{adi}`

    In this last example the array expression has been reduced from
    4-dimensional to 3-dimensional. Notice that no contraction has occurred,
    rather there is a new index `i` for the diagonal, contraction would have
    reduced the array to 2 dimensions.

    Notice that the diagonalized out dimensions are added as new dimensions at
    the end of the indices.
    """
    def __new__(cls, expr, *diagonal_indices, **kwargs) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | Self:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def diagonal_indices(self) -> tuple[Basic, ...]:
        ...
    
    def as_explicit(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ArrayDiagonal | ImmutableDenseNDimArray | Any:
        ...
    


class ArrayElementwiseApplyFunc(_CodegenArrayAbstract):
    def __new__(cls, function, element) -> Self:
        ...
    
    @property
    def function(self) -> Basic:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    
    def as_explicit(self):
        ...
    


class ArrayContraction(_CodegenArrayAbstract):
    r"""
    This class is meant to represent contractions of arrays in a form easily
    processable by the code printers.
    """
    def __new__(cls, expr, *contraction_indices, **kwargs) -> Basic | ZeroArray | ArrayTensorProduct | Self:
        ...
    
    def __mul__(self, other) -> Self:
        ...
    
    def __rmul__(self, other) -> Self:
        ...
    
    def split_multiple_contractions(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims:
        """
        Recognize multiple contractions and attempt at rewriting them as paired-contractions.

        This allows some contractions involving more than two indices to be
        rewritten as multiple contractions involving two indices, thus allowing
        the expression to be rewritten as a matrix multiplication line.

        Examples:

        * `A_ij b_j0 C_jk` ===> `A*DiagMatrix(b)*C`

        Care for:
        - matrix being diagonalized (i.e. `A_ii`)
        - vectors being diagonalized (i.e. `a_i0`)

        Multiple contractions can be split into matrix multiplications if
        not more than two arguments are non-diagonals or non-vectors.
        Vectors get diagonalized while diagonal matrices remain diagonal.
        The non-diagonal matrices can be at the beginning or at the end
        of the final matrix multiplication line.
        """
        ...
    
    def flatten_contraction_of_diagonal(self) -> Self | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction:
        ...
    
    @property
    def free_indices(self):
        ...
    
    @property
    def free_indices_to_position(self) -> dict[Any, Any]:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def contraction_indices(self) -> tuple[Basic, ...]:
        ...
    
    def sort_args_by_name(self) -> Self | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction:
        """
        Sort arguments in the tensor product so that their order is lexicographical.

        Examples
        ========

        >>> from sympy.tensor.array.expressions.from_matrix_to_array import convert_matrix_to_array
        >>> from sympy import MatrixSymbol
        >>> from sympy.abc import N
        >>> A = MatrixSymbol("A", N, N)
        >>> B = MatrixSymbol("B", N, N)
        >>> C = MatrixSymbol("C", N, N)
        >>> D = MatrixSymbol("D", N, N)

        >>> cg = convert_matrix_to_array(C*D*A*B)
        >>> cg
        ArrayContraction(ArrayTensorProduct(A, D, C, B), (0, 3), (1, 6), (2, 5))
        >>> cg.sort_args_by_name()
        ArrayContraction(ArrayTensorProduct(A, D, B, C), (0, 3), (1, 4), (2, 7))
        """
        ...
    
    def as_explicit(self) -> Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | ImmutableDenseNDimArray | Any:
        ...
    


class Reshape(_CodegenArrayAbstract):
    """
    Reshape the dimensions of an array expression.

    Examples
    ========

    >>> from sympy.tensor.array.expressions import ArraySymbol, Reshape
    >>> A = ArraySymbol("A", (6,))
    >>> A.shape
    (6,)
    >>> Reshape(A, (3, 2)).shape
    (3, 2)

    Check the component-explicit forms:

    >>> A.as_explicit()
    [A[0], A[1], A[2], A[3], A[4], A[5]]
    >>> Reshape(A, (3, 2)).as_explicit()
    [[A[0], A[1]], [A[2], A[3]], [A[4], A[5]]]

    """
    def __new__(cls, expr, shape) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def expr(self):
        ...
    
    def doit(self, *args, **kwargs) -> Reshape:
        ...
    
    def as_explicit(self) -> Self | Array:
        ...
    


class _ArgE:
    """
    The ``_ArgE`` object contains references to the array expression
    (``.element``) and a list containing the information about index
    contractions (``.indices``).

    Index contractions are numbered and contracted indices show the number of
    the contraction. Uncontracted indices have ``None`` value.

    For example:
    ``_ArgE(M, [None, 3])``
    This object means that expression ``M`` is part of an array contraction
    and has two indices, the first is not contracted (value ``None``),
    the second index is contracted to the 4th (i.e. number ``3``) group of the
    array contraction object.
    """
    indices: List[Optional[int]]
    def __init__(self, element, indices: Optional[List[Optional[int]]] = ...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...


class _IndPos:
    """
    Index position, requiring two integers in the constructor:

    - arg: the position of the argument in the tensor product,
    - rel: the relative position of the index inside the argument.
    """
    def __init__(self, arg: int, rel: int) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __iter__(self) -> Generator[int, Any, None]:
        ...
    


class _EditArrayContraction:
    """
    Utility class to help manipulate array contraction objects.

    This class takes as input an ``ArrayContraction`` object and turns it into
    an editable object.

    The field ``args_with_ind`` of this class is a list of ``_ArgE`` objects
    which can be used to easily edit the contraction structure of the
    expression.

    Once editing is finished, the ``ArrayContraction`` object may be recreated
    by calling the ``.to_array_contraction()`` method.
    """
    def __init__(self, base_array: typing.Union[ArrayContraction, ArrayDiagonal, ArrayTensorProduct]) -> None:
        ...
    
    def insert_after(self, arg: _ArgE, new_arg: _ArgE) -> None:
        ...
    
    def get_new_contraction_index(self) -> int:
        ...
    
    def refresh_indices(self) -> None:
        ...
    
    def merge_scalars(self) -> None:
        ...
    
    def to_array_contraction(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims:
        ...
    
    def get_contraction_indices(self) -> List[List[int]]:
        ...
    
    def get_mapping_for_index(self, ind) -> List[_IndPos]:
        ...
    
    def get_contraction_indices_to_ind_rel_pos(self) -> List[List[_IndPos]]:
        ...
    
    def count_args_with_index(self, index: int) -> int:
        """
        Count the number of arguments that have the given index.
        """
        ...
    
    def get_args_with_index(self, index: int) -> List[_ArgE]:
        """
        Get a list of arguments having the given index.
        """
        ...
    
    @property
    def number_of_diagonal_indices(self) -> int:
        ...
    
    def track_permutation_start(self) -> None:
        ...
    
    def track_permutation_merge(self, destination: _ArgE, from_element: _ArgE) -> None:
        ...
    
    def get_absolute_free_range(self, arg: _ArgE) -> typing.Tuple[int, int]:
        """
        Return the range of the free indices of the arg as absolute positions
        among all free indices.
        """
        ...
    
    def get_absolute_range(self, arg: _ArgE) -> typing.Tuple[int, int]:
        """
        Return the absolute range of indices for arg, disregarding dummy
        indices.
        """
        ...
    


def get_rank(expr) -> int:
    ...

def get_shape(expr) -> tuple[()]:
    ...

def nest_permutation(expr) -> PermuteDims | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | ArrayAdd:
    ...

