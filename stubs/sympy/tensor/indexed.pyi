from typing import Any, Self, Tuple
from sympy import Basic, MatrixBase, NDimArray
from sympy.core import Expr
from sympy.utilities.iterables import NotIterable

class IndexException(Exception):
    ...


class Indexed(Expr):
    is_Indexed = ...
    is_symbol = ...
    is_Atom = ...
    def __new__(cls, base, *args, **kw_args) -> Self:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    @property
    def assumptions0(self) -> dict[Any, Any]:
        ...
    
    @property
    def base(self) -> Basic:
        ...
    
    @property
    def indices(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def rank(self) -> int:
        ...
    
    @property
    def shape(self) -> Tuple:
        ...
    
    @property
    def ranges(self) -> list[Any]:
        ...
    
    @property
    def free_symbols(self) -> set[Self | Basic] | set[Basic]:
        ...
    
    @property
    def expr_free_symbols(self) -> set[Self]:
        ...
    


class IndexedBase(Expr, NotIterable):
    is_symbol = ...
    is_Atom = ...
    def __new__(cls, label, shape=..., *, offset=..., strides=..., **kw_args) -> MatrixBase | NDimArray | Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def assumptions0(self) -> dict[Any, Any]:
        ...
    
    def __getitem__(self, indices, **kw_args) -> Indexed:
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def strides(self):
        ...
    
    @property
    def offset(self):
        ...
    
    @property
    def label(self) -> Basic:
        ...
    


class Idx(Expr):
    is_integer = ...
    is_finite = ...
    is_real = ...
    is_symbol = ...
    is_Atom = ...
    _diff_wrt = ...
    def __new__(cls, label, range=..., **kw_args) -> Self:
        ...
    
    @property
    def label(self) -> Basic:
        ...
    
    @property
    def lower(self) -> None:
        ...
    
    @property
    def upper(self) -> None:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    @property
    def free_symbols(self) -> set[Self]:
        ...
    


