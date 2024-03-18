
from typing import Any, Self

from sympy.core.basic import Basic


class EPath:
    __slots__ = ...
    def __new__(cls, path) -> EPath | Self:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def apply(self, expr, func, args=..., kwargs=...) -> Basic:
        ...
    
    def select(self, expr) -> list[Any]:
        ...
    


def epath(path, expr=..., func=..., args=..., kwargs=...) -> EPath | list[Any] | Basic:
    ...

