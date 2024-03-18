
from typing import Any, Self

from sympy.core.logic import And


class Literal:
    def __new__(cls, lit, is_Not=...) -> OR | AND | Literal | Self:
        ...
    
    @property
    def arg(self):
        ...
    
    def rcall(self, expr) -> Self:
        ...
    
    def __invert__(self) -> Literal:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class OR:
    def __init__(self, *args) -> None:
        ...
    
    @property
    def args(self) -> list[Any]:
        ...
    
    def rcall(self, expr) -> Self:
        ...
    
    def __invert__(self) -> AND:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...


class AND:
    def __init__(self, *args) -> None:
        ...
    
    def __invert__(self) -> OR:
        ...
    
    @property
    def args(self) -> list[Any]:
        ...
    
    def rcall(self, expr) -> Self:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...


def to_NNF(expr, composite_map=...) -> OR | AND | Literal:
    ...

def distribute_AND_over_OR(expr) -> CNF | None:
    ...

class CNF:
    def __init__(self, clauses=...) -> None:
        ...
    
    def add(self, prop) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def extend(self, props) -> Self:
        ...
    
    def copy(self) -> CNF:
        ...
    
    def add_clauses(self, clauses) -> None:
        ...
    
    @classmethod
    def from_prop(cls, prop) -> Self:
        ...
    
    def __iand__(self, other) -> Self:
        ...
    
    def all_predicates(self) -> set[Any]:
        ...
    
    def rcall(self, expr) -> CNF | None:
        ...
    
    @classmethod
    def all_or(cls, *cnfs):
        ...
    
    @classmethod
    def all_and(cls, *cnfs):
        ...
    
    @classmethod
    def to_CNF(cls, expr) -> CNF | None:
        ...
    
    @classmethod
    def CNF_to_cnf(cls, cnf) -> And:
        ...
    


class EncodedCNF:
    def __init__(self, data=..., encoding=...) -> None:
        ...
    
    def from_cnf(self, cnf) -> None:
        ...
    
    @property
    def symbols(self) -> list[Any]:
        ...
    
    @property
    def variables(self) -> range:
        ...
    
    def copy(self) -> EncodedCNF:
        ...
    
    def add_prop(self, prop) -> None:
        ...
    
    def add_from_cnf(self, cnf) -> None:
        ...
    
    def encode_arg(self, arg) -> int:
        ...
    
    def encode(self, clause) -> set[int | Any]:
        ...
    


