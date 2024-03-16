from typing import Any
from sympy.assumptions.cnf import AND, OR, Literal
from sympy.core.cache import cacheit

"""
Do NOT manually edit this file.
Instead, run ./bin/ask_update.py.
"""
@cacheit
def get_all_known_facts() -> set[frozenset[OR | AND | Literal]]:
    """
    Known facts between unary predicates as CNF clauses.
    """
    ...

@cacheit
def get_all_known_matrix_facts() -> set[frozenset[OR | AND | Literal]]:
    """
    Known facts between unary predicates for matrices as CNF clauses.
    """
    ...

@cacheit
def get_all_known_number_facts() -> set[frozenset[OR | AND | Literal]]:
    """
    Known facts between unary predicates for numbers as CNF clauses.
    """
    ...

@cacheit
def get_known_facts_dict() -> dict[Any, Any]:
    """
    Logical relations between unary predicates as dictionary.

    Each key is a predicate, and item is two groups of predicates.
    First group contains the predicates which are implied by the key, and
    second group contains the predicates which are rejected by the key.

    """
    ...

