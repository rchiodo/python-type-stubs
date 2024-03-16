from typing import Union as tUnion
from sympy.matrices.expressions.applyfunc import ElementwiseApplyFunction
from sympy.tensor.array.expressions.array_expressions import ArrayAdd, ArrayContraction, ArrayDiagonal, ArrayElement, ArrayElementwiseApplyFunc, ArrayTensorProduct, PermuteDims, ZeroArray

@_array2matrix.register(ZeroArray)
def _(expr: ZeroArray) -> ZeroMatrix | ZeroArray:
    ...

@_array2matrix.register(ArrayTensorProduct)
def _(expr: ArrayTensorProduct) -> Mul | ArrayTensorProduct:
    ...

@_array2matrix.register(ArrayContraction)
def _(expr: ArrayContraction) -> GenericIdentity | Order | object | Mul | ArrayTensorProduct | ZeroArray | ArrayContraction | Basic | PermuteDims | Trace | None:
    ...

@_array2matrix.register(ArrayDiagonal)
def _(expr: ArrayDiagonal) -> ArrayDiagonal:
    ...

@_array2matrix.register(PermuteDims)
def _(expr: PermuteDims) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims | Any | Transpose | Mul:
    ...

@_array2matrix.register(ArrayAdd)
def _(expr: ArrayAdd) -> MatAdd | GenericZeroMatrix | ZeroArray | ArrayAdd:
    ...

@_array2matrix.register(ArrayElementwiseApplyFunc)
def _(expr: ArrayElementwiseApplyFunc) -> MatrixExpr | ElementwiseApplyFunction | ArrayElementwiseApplyFunc:
    ...

@_array2matrix.register(ArrayElement)
def _(expr: ArrayElement) -> MatrixElement | ArrayElement:
    ...

@_remove_trivial_dims.register(ArrayTensorProduct)
def _(expr: ArrayTensorProduct) -> tuple[ArrayTensorProduct | Mul, List[int] | list[Any]]:
    ...

@_remove_trivial_dims.register(ArrayAdd)
def _(expr: ArrayAdd) -> tuple[ArrayAdd, list[Any]] | tuple[ArrayAdd, Any] | tuple[MatAdd | Any | GenericZeroMatrix | ZeroArray | ArrayAdd, Any]:
    ...

@_remove_trivial_dims.register(PermuteDims)
def _(expr: PermuteDims) -> tuple[Any | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims, List[int] | list[Any]]:
    ...

@_remove_trivial_dims.register(ArrayContraction)
def _(expr: ArrayContraction) -> tuple[Any, List[int]] | tuple[Basic | Any | ZeroArray | ArrayTensorProduct | ArrayContraction, list[int]]:
    ...

@_remove_trivial_dims.register(ArrayDiagonal)
def _(expr: ArrayDiagonal) -> tuple[Any | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims, List[int]] | tuple[Any | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims, list[Any]]:
    ...

@_remove_trivial_dims.register(ElementwiseApplyFunction)
def _(expr: ElementwiseApplyFunction) -> tuple[Any, list[Any]] | tuple[MatrixExpr | ElementwiseApplyFunction, list[Any]]:
    ...

@_remove_trivial_dims.register(ArrayElementwiseApplyFunc)
def _(expr: ArrayElementwiseApplyFunc) -> tuple[ArrayElementwiseApplyFunc, list[Any]]:
    ...

def convert_array_to_matrix(expr):
    r"""
    Recognize matrix expressions in codegen objects.

    If more than one matrix multiplication line have been detected, return a
    list with the matrix expressions.

    Examples
    ========

    >>> from sympy.tensor.array.expressions.from_indexed_to_array import convert_indexed_to_array
    >>> from sympy.tensor.array import tensorcontraction, tensorproduct
    >>> from sympy import MatrixSymbol, Sum
    >>> from sympy.abc import i, j, k, l, N
    >>> from sympy.tensor.array.expressions.from_matrix_to_array import convert_matrix_to_array
    >>> from sympy.tensor.array.expressions.from_array_to_matrix import convert_array_to_matrix
    >>> A = MatrixSymbol("A", N, N)
    >>> B = MatrixSymbol("B", N, N)
    >>> C = MatrixSymbol("C", N, N)
    >>> D = MatrixSymbol("D", N, N)

    >>> expr = Sum(A[i, j]*B[j, k], (j, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A*B
    >>> cg = convert_indexed_to_array(expr, first_indices=[k])
    >>> convert_array_to_matrix(cg)
    B.T*A.T

    Transposition is detected:

    >>> expr = Sum(A[j, i]*B[j, k], (j, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A.T*B
    >>> cg = convert_indexed_to_array(expr, first_indices=[k])
    >>> convert_array_to_matrix(cg)
    B.T*A

    Detect the trace:

    >>> expr = Sum(A[i, i], (i, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    Trace(A)

    Recognize some more complex traces:

    >>> expr = Sum(A[i, j]*B[j, i], (i, 0, N-1), (j, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    Trace(A*B)

    More complicated expressions:

    >>> expr = Sum(A[i, j]*B[k, j]*A[l, k], (j, 0, N-1), (k, 0, N-1))
    >>> cg = convert_indexed_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A*B.T*A.T

    Expressions constructed from matrix expressions do not contain literal
    indices, the positions of free indices are returned instead:

    >>> expr = A*B
    >>> cg = convert_matrix_to_array(expr)
    >>> convert_array_to_matrix(cg)
    A*B

    If more than one line of matrix multiplications is detected, return
    separate matrix multiplication factors embedded in a tensor product object:

    >>> cg = tensorcontraction(tensorproduct(A, B, C, D), (1, 2), (5, 6))
    >>> convert_array_to_matrix(cg)
    ArrayTensorProduct(A*B, C*D)

    The two lines have free indices at axes 0, 3 and 4, 7, respectively.
    """
    ...

def identify_hadamard_products(expr: tUnion[ArrayContraction, ArrayDiagonal]) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims:
    ...

def identify_removable_identity_matrices(expr) -> ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims:
    ...

def remove_identity_matrices(expr: ArrayContraction) -> tuple[Any | ZeroArray | ArrayTensorProduct | ArrayContraction | Basic | PermuteDims, list[int]]:
    ...

