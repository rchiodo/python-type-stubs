from typing import Self
from sympy.core.kind import Kind, _NumberKind
from sympy.core.mul import Mul

class MatrixKind(Kind):
    def __new__(cls, element_kind=...) -> Self:
        ...
    
    def __repr__(self):
        ...
    


@Mul._kind_dispatcher.register(_NumberKind, MatrixKind)
def num_mat_mul(k1, k2) -> MatrixKind:
    ...

@Mul._kind_dispatcher.register(MatrixKind, MatrixKind)
def mat_mat_mul(k1, k2) -> MatrixKind:
    ...

