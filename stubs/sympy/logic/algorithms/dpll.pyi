"""Implementation of DPLL algorithm

Further improvements: eliminate calls to pl_true, implement branching rules,
efficient unit propagation.

References:
  - https://en.wikipedia.org/wiki/DPLL_algorithm
  - https://www.researchgate.net/publication/242384772_Implementations_of_the_DPLL_Algorithm
"""
from typing import Any, Literal


def dpll_satisfiable(expr) -> dict[Any, Any] | Literal[False]:
    """
    Check satisfiability of a propositional sentence.
    It returns a model rather than True when it succeeds

    >>> from sympy.abc import A, B
    >>> from sympy.logic.algorithms.dpll import dpll_satisfiable
    >>> dpll_satisfiable(A & ~B)
    {A: True, B: False}
    >>> dpll_satisfiable(A & ~A)
    False

    """
    ...

def dpll(clauses, symbols, model) -> Literal[False]:
    """
    Compute satisfiability in a partial model.
    Clauses is an array of conjuncts.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import dpll
    >>> dpll([A, B, D], [A, B], {D: False})
    False

    """
    ...

def dpll_int_repr(clauses, symbols, model) -> Literal[False]:
    """
    Compute satisfiability in a partial model.
    Arguments are expected to be in integer representation

    >>> from sympy.logic.algorithms.dpll import dpll_int_repr
    >>> dpll_int_repr([{1}, {2}, {3}], {1, 2}, {3: False})
    False

    """
    ...

def pl_true_int_repr(clause, model=...) -> bool | None:
    """
    Lightweight version of pl_true.
    Argument clause represents the set of args of an Or clause. This is used
    inside dpll_int_repr, it is not meant to be used directly.

    >>> from sympy.logic.algorithms.dpll import pl_true_int_repr
    >>> pl_true_int_repr({1, 2}, {1: False})
    >>> pl_true_int_repr({1, 2}, {1: False, 2: False})
    False

    """
    ...

def unit_propagate(clauses, symbol) -> list[Any]:
    """
    Returns an equivalent set of clauses
    If a set of clauses contains the unit clause l, the other clauses are
    simplified by the application of the two following rules:

      1. every clause containing l is removed
      2. in every clause that contains ~l this literal is deleted

    Arguments are expected to be in CNF.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import unit_propagate
    >>> unit_propagate([A | B, D | ~B, B], B)
    [D, B]

    """
    ...

def unit_propagate_int_repr(clauses, s) -> list[Any]:
    """
    Same as unit_propagate, but arguments are expected to be in integer
    representation

    >>> from sympy.logic.algorithms.dpll import unit_propagate_int_repr
    >>> unit_propagate_int_repr([{1, 2}, {3, -2}, {2}], 2)
    [{3}]

    """
    ...

def find_pure_symbol(symbols, unknown_clauses) -> tuple[Any, bool] | tuple[None, None]:
    """
    Find a symbol and its value if it appears only as a positive literal
    (or only as a negative) in clauses.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import find_pure_symbol
    >>> find_pure_symbol([A, B, D], [A|~B,~B|~D,D|A])
    (A, True)

    """
    ...

def find_pure_symbol_int_repr(symbols, unknown_clauses) -> tuple[Any, Literal[True]] | tuple[Any, Literal[False]] | tuple[None, None]:
    """
    Same as find_pure_symbol, but arguments are expected
    to be in integer representation

    >>> from sympy.logic.algorithms.dpll import find_pure_symbol_int_repr
    >>> find_pure_symbol_int_repr({1,2,3},
    ...     [{1, -2}, {-2, -3}, {3, 1}])
    (1, True)

    """
    ...

def find_unit_clause(clauses, model) -> tuple[Any | bool, Any | bool] | tuple[None, None]:
    """
    A unit clause has only 1 variable that is not bound in the model.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import find_unit_clause
    >>> find_unit_clause([A | B | D, B | ~D, A | ~B], {A:True})
    (B, False)

    """
    ...

def find_unit_clause_int_repr(clauses, model) -> tuple[Any, Literal[False]] | tuple[Any, Literal[True]] | tuple[None, None]:
    """
    Same as find_unit_clause, but arguments are expected to be in
    integer representation.

    >>> from sympy.logic.algorithms.dpll import find_unit_clause_int_repr
    >>> find_unit_clause_int_repr([{1, 2, 3},
    ...     {2, -3}, {1, -2}], {1: True})
    (2, False)

    """
    ...

