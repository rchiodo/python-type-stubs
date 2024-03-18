from sympy import Basic, Pow
from sympy.functions.special.tensor_functions import KroneckerDelta
from sympy.tensor.array.expressions.array_expressions import ArrayAdd, ArrayContraction, ArrayDiagonal, ArrayElement, ArrayElementwiseApplyFunc, ArrayTensorProduct, PermuteDims, ZeroArray


def convert_indexed_to_array(expr, first_indices=...) -> ArrayElement | Basic | ZeroArray | ArrayTensorProduct | ArrayContraction | PermuteDims | ArrayDiagonal | KroneckerDelta | ArrayAdd | ArrayElementwiseApplyFunc | Pow:
    r"""
    Parse indexed expression into a form useful for code generation.

    Examples
    ========

    >>> from sympy.tensor.array.expressions.from_indexed_to_array import convert_indexed_to_array
    >>> from sympy import MatrixSymbol, Sum, symbols

    >>> i, j, k, d = symbols("i j k d")
    >>> M = MatrixSymbol("M", d, d)
    >>> N = MatrixSymbol("N", d, d)

    Recognize the trace in summation form:

    >>> expr = Sum(M[i, i], (i, 0, d-1))
    >>> convert_indexed_to_array(expr)
    ArrayContraction(M, (0, 1))

    Recognize the extraction of the diagonal by using the same index `i` on
    both axes of the matrix:

    >>> expr = M[i, i]
    >>> convert_indexed_to_array(expr)
    ArrayDiagonal(M, (0, 1))

    This function can help perform the transformation expressed in two
    different mathematical notations as:

    `\sum_{j=0}^{N-1} A_{i,j} B_{j,k} \Longrightarrow \mathbf{A}\cdot \mathbf{B}`

    Recognize the matrix multiplication in summation form:

    >>> expr = Sum(M[i, j]*N[j, k], (j, 0, d-1))
    >>> convert_indexed_to_array(expr)
    ArrayContraction(ArrayTensorProduct(M, N), (1, 2))

    Specify that ``k`` has to be the starting index:

    >>> convert_indexed_to_array(expr, first_indices=[k])
    ArrayContraction(ArrayTensorProduct(N, M), (0, 3))
    """
    ...

