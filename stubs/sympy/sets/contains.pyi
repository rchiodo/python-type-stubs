from typing import Any, Self
from sympy.core.basic import Basic
from sympy.logic.boolalg import Boolean

class Contains(Boolean):
    def __new__(cls, x, s, evaluate=...) -> Boolean | Self:
        ...
    
    @property
    def binary_symbols(self) -> set[Any | Basic]:
        ...
    
    def as_set(self) -> Basic:
        ...
    


