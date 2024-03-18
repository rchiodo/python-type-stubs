from typing import Literal, Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matexpr import MatrixExpr

class ZeroMatrix(MatrixExpr):
    """The Matrix Zero 0 - additive identity

    Examples
    ========

    >>> from sympy import MatrixSymbol, ZeroMatrix
    >>> A = MatrixSymbol('A', 3, 5)
    >>> Z = ZeroMatrix(3, 5)
    >>> A + Z
    A
    >>> Z*A.T
    0
    """
    is_ZeroMatrix = ...
    def __new__(cls, m, n) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, Basic]:
        ...
    


class GenericZeroMatrix(ZeroMatrix):
    """
    A zero matrix without a specified shape

    This exists primarily so MatAdd() with no arguments can return something
    meaningful.
    """
    def __new__(cls) -> Self:
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def cols(self):
        ...
    
    @property
    def shape(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class Identity(MatrixExpr):
    """The Matrix Identity I - multiplicative identity

    Examples
    ========

    >>> from sympy import Identity, MatrixSymbol
    >>> A = MatrixSymbol('A', 3, 5)
    >>> I = Identity(3)
    >>> I*A
    A
    """
    is_Identity = ...
    def __new__(cls, n) -> Self:
        ...
    
    @property
    def rows(self) -> Basic:
        ...
    
    @property
    def cols(self) -> Basic:
        ...
    
    @property
    def shape(self) -> tuple[Basic, Basic]:
        ...
    
    @property
    def is_square(self) -> Literal[True]:
        ...
    


class GenericIdentity(Identity):
    """
    An identity matrix without a specified shape

    This exists primarily so MatMul() with no arguments can return something
    meaningful.
    """
    def __new__(cls) -> Self:
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def cols(self):
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def is_square(self) -> Literal[True]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class OneMatrix(MatrixExpr):
    """
    Matrix whose all entries are ones.
    """
    def __new__(cls, m, n, evaluate=...) -> Identity | Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def is_Identity(self):
        ...
    
    def as_explicit(self):
        ...
    
    def doit(self, **hints) -> Self:
        ...
    


