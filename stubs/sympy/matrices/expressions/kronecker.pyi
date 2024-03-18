from types import NotImplementedType
from typing import Any, Self
from sympy.matrices.expressions.matadd import MatAdd
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import GenericIdentity, GenericZeroMatrix, Identity
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.series.order import Order

def kronecker_product(*matrices) -> Any | NotImplementedType | GenericIdentity | Order | object | Identity:
    ...

class KroneckerProduct(MatrixExpr):
    is_KroneckerProduct = ...
    def __new__(cls, *args, check=...) -> ImmutableDenseMatrix | Identity | Self:
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def structurally_equal(self, other) -> bool:
        '''Determine whether two matrices have the same Kronecker product structure

        Examples
        ========

        >>> from sympy import KroneckerProduct, MatrixSymbol, symbols
        >>> m, n = symbols(r'm, n', integer=True)
        >>> A = MatrixSymbol('A', m, m)
        >>> B = MatrixSymbol('B', n, n)
        >>> C = MatrixSymbol('C', m, m)
        >>> D = MatrixSymbol('D', n, n)
        >>> KroneckerProduct(A, B).structurally_equal(KroneckerProduct(C, D))
        True
        >>> KroneckerProduct(A, B).structurally_equal(KroneckerProduct(D, C))
        False
        >>> KroneckerProduct(A, B).structurally_equal(C)
        False
        '''
        ...
    
    def has_matching_shape(self, other) -> bool | NotImplementedType:
        '''Determine whether two matrices have the appropriate structure to bring matrix
        multiplication inside the KroneckerProdut

        Examples
        ========
        >>> from sympy import KroneckerProduct, MatrixSymbol, symbols
        >>> m, n = symbols(r'm, n', integer=True)
        >>> A = MatrixSymbol('A', m, n)
        >>> B = MatrixSymbol('B', n, m)
        >>> KroneckerProduct(A, B).has_matching_shape(KroneckerProduct(B, A))
        True
        >>> KroneckerProduct(A, B).has_matching_shape(KroneckerProduct(A, B))
        False
        >>> KroneckerProduct(A, B).has_matching_shape(A)
        False
        '''
        ...
    
    def doit(self, **hints) -> Any | NotImplementedType | GenericIdentity | Order | object:
        ...
    


def validate(*args) -> None:
    ...

def extract_commutative(kron) -> Any | NotImplementedType | GenericIdentity | Order | object:
    ...

def matrix_kronecker_product(*matrices):
    ...

def explicit_kronecker_product(kron):
    ...

rules = ...
canonicalize = ...
def kronecker_mat_add(expr) -> GenericZeroMatrix | MatAdd:
    ...

def kronecker_mat_mul(expr):
    ...

def kronecker_mat_pow(expr) -> ImmutableDenseMatrix | Identity | KroneckerProduct:
    ...

def combine_kronecker(expr) -> Any:
    ...

