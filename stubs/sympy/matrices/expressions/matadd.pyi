from typing import Self
from sympy.core.add import Add
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import GenericZeroMatrix

class MatAdd(MatrixExpr, Add):
    """A Sum of Matrix Expressions

    MatAdd inherits from and operates like SymPy Add

    Examples
    ========

    >>> from sympy import MatAdd, MatrixSymbol
    >>> A = MatrixSymbol('A', 5, 5)
    >>> B = MatrixSymbol('B', 5, 5)
    >>> C = MatrixSymbol('C', 5, 5)
    >>> MatAdd(A, B, C)
    A + B + C
    """
    is_MatAdd = ...
    identity = ...
    def __new__(cls, *args, evaluate=..., check=..., _sympify=...) -> GenericZeroMatrix | MatAdd | Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def could_extract_minus_sign(self) -> bool:
        ...
    
    def expand(self, **kwargs) -> MatAdd:
        ...
    
    def doit(self, **hints) -> MatAdd:
        ...
    


factor_of = ...
matrix_of = ...
def combine(cnt, mat):
    ...

def merge_explicit(matadd) -> MatAdd:
    """ Merge explicit MatrixBase arguments

    Examples
    ========

    >>> from sympy import MatrixSymbol, eye, Matrix, MatAdd, pprint
    >>> from sympy.matrices.expressions.matadd import merge_explicit
    >>> A = MatrixSymbol('A', 2, 2)
    >>> B = eye(2)
    >>> C = Matrix([[1, 2], [3, 4]])
    >>> X = MatAdd(A, B, C)
    >>> pprint(X)
        [1  0]   [1  2]
    A + [    ] + [    ]
        [0  1]   [3  4]
    >>> pprint(merge_explicit(X))
        [2  2]
    A + [    ]
        [3  5]
    """
    ...

rules = ...
canonicalize = ...
