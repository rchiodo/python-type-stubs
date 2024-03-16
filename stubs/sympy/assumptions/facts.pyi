from typing import Any
from sympy.core.cache import cacheit
from sympy.core.logic import And

"""
Known facts in assumptions module.

This module defines the facts between unary predicates in ``get_known_facts()``,
and supports functions to generate the contents in
``sympy.assumptions.ask_generated`` file.
"""
@cacheit
def get_composite_predicates() -> dict[Any, Any]:
    ...

@cacheit
def get_known_facts(x=...) -> And:
    """
    Facts between unary predicates.

    Parameters
    ==========

    x : Symbol, optional
        Placeholder symbol for unary facts. Default is ``Symbol('x')``.

    Returns
    =======

    fact : Known facts in conjugated normal form.

    """
    ...

@cacheit
def get_number_facts(x=...) -> And:
    """
    Facts between unary number predicates.

    Parameters
    ==========

    x : Symbol, optional
        Placeholder symbol for unary facts. Default is ``Symbol('x')``.

    Returns
    =======

    fact : Known facts in conjugated normal form.

    """
    ...

@cacheit
def get_matrix_facts(x=...) -> And:
    """
    Facts between unary matrix predicates.

    Parameters
    ==========

    x : Symbol, optional
        Placeholder symbol for unary facts. Default is ``Symbol('x')``.

    Returns
    =======

    fact : Known facts in conjugated normal form.

    """
    ...

def generate_known_facts_dict(keys, fact) -> dict[Any, Any]:
    """
    Computes and returns a dictionary which contains the relations between
    unary predicates.

    Each key is a predicate, and item is two groups of predicates.
    First group contains the predicates which are implied by the key, and
    second group contains the predicates which are rejected by the key.

    All predicates in *keys* and *fact* must be unary and have same placeholder
    symbol.

    Parameters
    ==========

    keys : list of AppliedPredicate instances.

    fact : Fact between predicates in conjugated normal form.

    Examples
    ========

    >>> from sympy import Q, And, Implies
    >>> from sympy.assumptions.facts import generate_known_facts_dict
    >>> from sympy.abc import x
    >>> keys = [Q.even(x), Q.odd(x), Q.zero(x)]
    >>> fact = And(Implies(Q.even(x), ~Q.odd(x)),
    ...     Implies(Q.zero(x), Q.even(x)))
    >>> generate_known_facts_dict(keys, fact)
    {Q.even: ({Q.even}, {Q.odd}),
     Q.odd: ({Q.odd}, {Q.even, Q.zero}),
     Q.zero: ({Q.even, Q.zero}, {Q.odd})}
    """
    ...

@cacheit
def get_known_facts_keys() -> list[Any]:
    """
    Return every unary predicates registered to ``Q``.

    This function is used to generate the keys for
    ``generate_known_facts_dict``.

    """
    ...

def single_fact_lookup(known_facts_keys, known_facts_cnf) -> dict[Any, Any]:
    ...

def ask_full_inference(proposition, assumptions, known_facts_cnf) -> bool | None:
    """
    Method for inferring properties about objects.

    """
    ...

