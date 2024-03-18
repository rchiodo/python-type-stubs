
from ast import Eq
from typing import Any, Literal

from sympy.core.relational import Ne, Relational


class UnhandledInput(Exception):
    ...


ALLOWED_PRED = ...
HANDLE_NEGATION = ...
class LRASolver:
    def __init__(self, A, slack_variables, nonslack_variables, enc_to_boundary, s_subs, testing_mode) -> None:
        ...
    
    @staticmethod
    def from_encoded_cnf(encoded_cnf, testing_mode=...) -> tuple[LRASolver, list[Any]]:
        ...
    
    def reset_bounds(self) -> None:
        ...
    
    def assert_lit(self, enc_constraint) -> tuple[Literal[False], list[Any]] | None:
        ...
    
    def check(self) -> tuple[Literal[True], dict[Any, Any]] | tuple[Literal[False], list[Any]]:
        ...
    


class Boundary:
    def __init__(self, var, const, upper, equality, strict=...) -> None:
        ...
    
    @staticmethod
    def from_upper(var) -> tuple[Boundary, Literal[-1, 1]]:
        ...
    
    @staticmethod
    def from_lower(var) -> tuple[Boundary, Literal[-1, 1]]:
        ...
    
    def get_negated(self) -> Boundary:
        ...
    
    def get_inequality(self) -> Eq | Relational | Ne:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class LRARational:
    def __init__(self, rational, delta) -> None:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __add__(self, other) -> LRARational:
        ...
    
    def __sub__(self, other) -> LRARational:
        ...
    
    def __mul__(self, other) -> LRARational:
        ...
    
    def __getitem__(self, index) -> Any:
        ...
    
    def __repr__(self) -> str:
        ...
    


class LRAVariable:
    def __init__(self, var) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


