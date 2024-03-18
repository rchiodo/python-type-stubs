"""Implementation of DPLL algorithm

Features:
  - Clause learning
  - Watch literal scheme
  - VSIDS heuristic

References:
  - https://en.wikipedia.org/wiki/DPLL_algorithm
"""
from typing import Any, Generator, Literal


def dpll_satisfiable(expr, all_models=..., use_lra_theory=...) -> Generator[bool, None, None] | Generator[Any | Literal[False], Any, None] | dict[Any, Any] | Literal[False]:
    """
    Check satisfiability of a propositional sentence.
    It returns a model rather than True when it succeeds.
    Returns a generator of all models if all_models is True.

    Examples
    ========

    >>> from sympy.abc import A, B
    >>> from sympy.logic.algorithms.dpll2 import dpll_satisfiable
    >>> dpll_satisfiable(A & ~B)
    {A: True, B: False}
    >>> dpll_satisfiable(A & ~A)
    False

    """
    ...

class SATSolver:
    """
    Class for representing a SAT solver capable of
     finding a model to a boolean theory in conjunctive
     normal form.
    """
    def __init__(self, clauses, variables, var_settings, symbols=..., heuristic=..., clause_learning=..., INTERVAL=..., lra_theory=...) -> None:
        ...
    


class Level:
    """
    Represents a single level in the DPLL algorithm, and contains
    enough information for a sound backtracking procedure.
    """
    def __init__(self, decision, flipped=...) -> None:
        ...
    


