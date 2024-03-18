from types import NotImplementedType
from typing import Any, Generator, Self
from sympy import ImmutableDenseNDimArray, ImmutableSparseNDimArray
from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.core.kind import Kind
from sympy.printing.defaults import Printable
from sympy.tensor.array.array_derivatives import ArrayDerivative
from sympy.tensor.array.expressions.array_expressions import ArrayContraction, ArrayTensorProduct, PermuteDims, ZeroArray

class ArrayKind(Kind):
    """
    Kind for N-dimensional array in SymPy.

    This kind represents the multidimensional array that algebraic
    operations are defined. Basic class for this kind is ``NDimArray``,
    but any expression representing the array can have this.

    Parameters
    ==========

    element_kind : Kind
        Kind of the element. Default is :obj:NumberKind `<sympy.core.kind.NumberKind>`,
        which means that the array contains only numbers.

    Examples
    ========

    Any instance of array class has ``ArrayKind``.

    >>> from sympy import NDimArray
    >>> NDimArray([1,2,3]).kind
    ArrayKind(NumberKind)

    Although expressions representing an array may be not instance of
    array class, it will have ``ArrayKind`` as well.

    >>> from sympy import Integral
    >>> from sympy.tensor.array import NDimArray
    >>> from sympy.abc import x
    >>> intA = Integral(NDimArray([1,2,3]), x)
    >>> isinstance(intA, NDimArray)
    False
    >>> intA.kind
    ArrayKind(NumberKind)

    Use ``isinstance()`` to check for ``ArrayKind` without specifying
    the element kind. Use ``is`` with specifying the element kind.

    >>> from sympy.tensor.array import ArrayKind
    >>> from sympy.core import NumberKind
    >>> boolA = NDimArray([True, False])
    >>> isinstance(boolA.kind, ArrayKind)
    True
    >>> boolA.kind is ArrayKind(NumberKind)
    False

    See Also
    ========

    shape : Function to return the shape of objects with ``MatrixKind``.

    """
    def __new__(cls, element_kind=...) -> Self:
        ...
    
    def __repr__(self):
        ...
    


class NDimArray(Printable):
    """N-dimensional array.

    Examples
    ========

    Create an N-dim array of zeros:

    >>> from sympy import MutableDenseNDimArray
    >>> a = MutableDenseNDimArray.zeros(2, 3, 4)
    >>> a
    [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    Create an N-dim array from a list;

    >>> a = MutableDenseNDimArray([[2, 3], [4, 5]])
    >>> a
    [[2, 3], [4, 5]]

    >>> b = MutableDenseNDimArray([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])
    >>> b
    [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]

    Create an N-dim array from a flat list with dimension shape:

    >>> a = MutableDenseNDimArray([1, 2, 3, 4, 5, 6], (2, 3))
    >>> a
    [[1, 2, 3], [4, 5, 6]]

    Create an N-dim array from a matrix:

    >>> from sympy import Matrix
    >>> a = Matrix([[1,2],[3,4]])
    >>> a
    Matrix([
    [1, 2],
    [3, 4]])
    >>> b = MutableDenseNDimArray(a)
    >>> b
    [[1, 2], [3, 4]]

    Arithmetic operations on N-dim arrays

    >>> a = MutableDenseNDimArray([1, 1, 1, 1], (2, 2))
    >>> b = MutableDenseNDimArray([4, 4, 4, 4], (2, 2))
    >>> c = a + b
    >>> c
    [[5, 5], [5, 5]]
    >>> a - b
    [[-3, -3], [-3, -3]]

    """
    _diff_wrt = ...
    is_scalar = ...
    def __new__(cls, iterable, shape=..., **kwargs) -> ImmutableDenseNDimArray:
        ...
    
    def __getitem__(self, index):
        ...
    
    def __len__(self):
        """Overload common function len(). Returns number of elements in array.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(3, 3)
        >>> a
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        >>> len(a)
        9

        """
        ...
    
    @property
    def shape(self):
        """
        Returns array shape (dimension).

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(3, 3)
        >>> a.shape
        (3, 3)

        """
        ...
    
    def rank(self):
        """
        Returns rank of array.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(3,4,5,6,3)
        >>> a.rank()
        5

        """
        ...
    
    def diff(self, *args, **kwargs) -> ArrayDerivative:
        """
        Calculate the derivative of each element in the array.

        Examples
        ========

        >>> from sympy import ImmutableDenseNDimArray
        >>> from sympy.abc import x, y
        >>> M = ImmutableDenseNDimArray([[x, y], [1, x*y]])
        >>> M.diff(x)
        [[1, 0], [0, y]]

        """
        ...
    
    def applyfunc(self, f) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        """Apply a function to each element of the N-dim array.

        Examples
        ========

        >>> from sympy import ImmutableDenseNDimArray
        >>> m = ImmutableDenseNDimArray([i*2+j for i in range(2) for j in range(2)], (2, 2))
        >>> m
        [[0, 1], [2, 3]]
        >>> m.applyfunc(lambda i: 2*i)
        [[0, 2], [4, 6]]
        """
        ...
    
    def tolist(self) -> list[Any]:
        """
        Converting MutableDenseNDimArray to one-dim list

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray([1, 2, 3, 4], (2, 2))
        >>> a
        [[1, 2], [3, 4]]
        >>> b = a.tolist()
        >>> b
        [[1, 2], [3, 4]]
        """
        ...
    
    def __add__(self, other) -> NotImplementedType | Self:
        ...
    
    def __sub__(self, other) -> NotImplementedType | Self:
        ...
    
    def __mul__(self, other) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        ...
    
    def __rmul__(self, other) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        ...
    
    def __truediv__(self, other) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def __neg__(self) -> ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __eq__(self, other) -> bool:
        """
        NDimArray instances can be compared to each other.
        Instances equal if they have same shape and data.

        Examples
        ========

        >>> from sympy import MutableDenseNDimArray
        >>> a = MutableDenseNDimArray.zeros(2, 3)
        >>> b = MutableDenseNDimArray.zeros(2, 3)
        >>> a == b
        True
        >>> c = a.reshape(3, 2)
        >>> c == b
        False
        >>> a[0,0] = 1
        >>> b[0,0] = 2
        >>> a == b
        False
        """
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def transpose(self) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | ImmutableSparseNDimArray | ImmutableDenseNDimArray:
        ...
    
    def conjugate(self):
        ...
    
    def adjoint(self) -> type[UndefinedFunction]:
        ...
    


class ImmutableNDimArray(NDimArray, Basic):
    _op_priority = ...
    def __hash__(self) -> int:
        ...
    
    def as_immutable(self) -> Self:
        ...
    
    def as_mutable(self):
        ...
    


