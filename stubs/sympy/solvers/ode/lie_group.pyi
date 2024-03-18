
from typing import Any

from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.core.symbol import Symbol


lie_heuristics = ...
def infinitesimals(eq, func=..., order=..., hint=..., match=...) -> list[Any] | Any:
    ...

def lie_heuristic_abaco1_simple(match, comp=...):
    ...

def lie_heuristic_abaco1_product(match, comp=...) -> list[dict[UndefinedFunction | Any, Any]] | list[Any] | None:
    ...

def lie_heuristic_bivariate(match, comp=...) -> list[dict[UndefinedFunction | Any, Any | Symbol | Basic]] | None:
    ...

def lie_heuristic_chi(match, comp=...) -> list[dict[UndefinedFunction | Any, Any]] | None:
    ...

def lie_heuristic_function_sum(match, comp=...) -> list[dict[UndefinedFunction | Any, Any]] | list[Any] | None:
    ...

def lie_heuristic_abaco2_similar(match, comp=...) -> list[dict[UndefinedFunction | Any, Any]] | None:
    ...

def lie_heuristic_abaco2_unique_unknown(match, comp=...) -> list[dict[UndefinedFunction | Any, Any]] | None:
    ...

def lie_heuristic_abaco2_unique_general(match, comp=...) -> list[dict[UndefinedFunction | Any, Any]] | None:
    ...

def lie_heuristic_linear(match, comp=...) -> list[dict[UndefinedFunction | Any, Any]] | None:
    ...

