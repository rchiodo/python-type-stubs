
from typing import Any, Literal


def dpll_satisfiable(expr) -> dict[Any, Any] | Literal[False]:
    ...

def dpll(clauses, symbols, model) -> Literal[False]:
    ...

def dpll_int_repr(clauses, symbols, model) -> Literal[False]:
    ...

def pl_true_int_repr(clause, model=...) -> bool | None:
    ...

def unit_propagate(clauses, symbol) -> list[Any]:
    ...

def unit_propagate_int_repr(clauses, s) -> list[Any]:
    ...

def find_pure_symbol(symbols, unknown_clauses) -> tuple[Any, bool] | tuple[None, None]:
    ...

def find_pure_symbol_int_repr(symbols, unknown_clauses) -> tuple[Any, Literal[True]] | tuple[Any, Literal[False]] | tuple[None, None]:
    ...

def find_unit_clause(clauses, model) -> tuple[Any | bool, Any | bool] | tuple[None, None]:
    ...

def find_unit_clause_int_repr(clauses, model) -> tuple[Any, Literal[False]] | tuple[Any, Literal[True]] | tuple[None, None]:
    ...

