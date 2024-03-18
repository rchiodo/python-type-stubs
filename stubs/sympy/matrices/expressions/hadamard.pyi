from typing import Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matexpr import MatrixExpr

def hadamard_product(*matrices):
    """
    Return the elementwise (aka Hadamard) product of matrices.

    Examples
    ========

    >>> from sympy import hadamard_product, MatrixSymbol
    >>> A = MatrixSymbol('A', 2, 3)
    >>> B = MatrixSymbol('B', 2, 3)
    >>> hadamard_product(A)
    A
    >>> hadamard_product(A, B)
    HadamardProduct(A, B)
    >>> hadamard_product(A, B)[0, 1]
    A[0, 1]*B[0, 1]
    """
    ...

class HadamardProduct(MatrixExpr):
    """
    Elementwise product of matrix expressions

    Examples
    ========

    Hadamard product for matrix symbols:

    >>> from sympy import hadamard_product, HadamardProduct, MatrixSymbol
    >>> A = MatrixSymbol('A', 5, 5)
    >>> B = MatrixSymbol('B', 5, 5)
    >>> isinstance(hadamard_product(A, B), HadamardProduct)
    True

    Notes
    =====

    This is a symbolic object that simply stores its argument without
    evaluating it. To actually compute the product, use the function
    ``hadamard_product()`` or ``HadamardProduct.doit``
    """
    is_HadamardProduct = ...
    def __new__(cls, *args, evaluate=..., check=...) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def doit(self, **hints):
        ...
    


def canonicalize(x):
    """Canonicalize the Hadamard product ``x`` with mathematical properties.

    Examples
    ========

    >>> from sympy import MatrixSymbol, HadamardProduct
    >>> from sympy import OneMatrix, ZeroMatrix
    >>> from sympy.matrices.expressions.hadamard import canonicalize
    >>> from sympy import init_printing
    >>> init_printing(use_unicode=False)

    >>> A = MatrixSymbol('A', 2, 2)
    >>> B = MatrixSymbol('B', 2, 2)
    >>> C = MatrixSymbol('C', 2, 2)

    Hadamard product associativity:

    >>> X = HadamardProduct(A, HadamardProduct(B, C))
    >>> X
    A.*(B.*C)
    >>> canonicalize(X)
    A.*B.*C

    Hadamard product commutativity:

    >>> X = HadamardProduct(A, B)
    >>> Y = HadamardProduct(B, A)
    >>> X
    A.*B
    >>> Y
    B.*A
    >>> canonicalize(X)
    A.*B
    >>> canonicalize(Y)
    A.*B

    Hadamard product identity:

    >>> X = HadamardProduct(A, OneMatrix(2, 2))
    >>> X
    A.*1
    >>> canonicalize(X)
    A

    Absorbing element of Hadamard product:

    >>> X = HadamardProduct(A, ZeroMatrix(2, 2))
    >>> X
    A.*0
    >>> canonicalize(X)
    0

    Rewriting to Hadamard Power

    >>> X = HadamardProduct(A, A, A)
    >>> X
    A.*A.*A
    >>> canonicalize(X)
     .3
    A

    Notes
    =====

    As the Hadamard product is associative, nested products can be flattened.

    The Hadamard product is commutative so that factors can be sorted for
    canonical form.

    A matrix of only ones is an identity for Hadamard product,
    so every matrices of only ones can be removed.

    Any zero matrix will make the whole product a zero matrix.

    Duplicate elements can be collected and rewritten as HadamardPower

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
    """
    ...

def hadamard_power(base, exp) -> HadamardPower:
    ...

class HadamardPower(MatrixExpr):
    r"""
    Elementwise power of matrix expressions

    Parameters
    ==========

    base : scalar or matrix

    exp : scalar or matrix

    Notes
    =====

    There are four definitions for the hadamard power which can be used.
    Let's consider `A, B` as `(m, n)` matrices, and `a, b` as scalars.

    Matrix raised to a scalar exponent:

    .. math::
        A^{\circ b} = \begin{bmatrix}
        A_{0, 0}^b   & A_{0, 1}^b   & \cdots & A_{0, n-1}^b   \\
        A_{1, 0}^b   & A_{1, 1}^b   & \cdots & A_{1, n-1}^b   \\
        \vdots       & \vdots       & \ddots & \vdots         \\
        A_{m-1, 0}^b & A_{m-1, 1}^b & \cdots & A_{m-1, n-1}^b
        \end{bmatrix}

    Scalar raised to a matrix exponent:

    .. math::
        a^{\circ B} = \begin{bmatrix}
        a^{B_{0, 0}}   & a^{B_{0, 1}}   & \cdots & a^{B_{0, n-1}}   \\
        a^{B_{1, 0}}   & a^{B_{1, 1}}   & \cdots & a^{B_{1, n-1}}   \\
        \vdots         & \vdots         & \ddots & \vdots           \\
        a^{B_{m-1, 0}} & a^{B_{m-1, 1}} & \cdots & a^{B_{m-1, n-1}}
        \end{bmatrix}

    Matrix raised to a matrix exponent:

    .. math::
        A^{\circ B} = \begin{bmatrix}
        A_{0, 0}^{B_{0, 0}}     & A_{0, 1}^{B_{0, 1}}     &
        \cdots & A_{0, n-1}^{B_{0, n-1}}     \\
        A_{1, 0}^{B_{1, 0}}     & A_{1, 1}^{B_{1, 1}}     &
        \cdots & A_{1, n-1}^{B_{1, n-1}}     \\
        \vdots                  & \vdots                  &
        \ddots & \vdots                      \\
        A_{m-1, 0}^{B_{m-1, 0}} & A_{m-1, 1}^{B_{m-1, 1}} &
        \cdots & A_{m-1, n-1}^{B_{m-1, n-1}}
        \end{bmatrix}

    Scalar raised to a scalar exponent:

    .. math::
        a^{\circ b} = a^b
    """
    def __new__(cls, base, exp) -> Self:
        ...
    
    @property
    def base(self) -> Basic:
        ...
    
    @property
    def exp(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    


