from typing import Any


def lra_satask(proposition, assumptions=..., context=...) -> bool | None:
    """
    Function to evaluate the proposition with assumptions using SAT algorithm
    in conjunction with an Linear Real Arithmetic theory solver.

    Used to handle inequalities. Should eventually be depreciated and combined
    into satask, but infinity handling and other things need to be implemented
    before that can happen.
    """
    ...

WHITE_LIST = ...
def check_satisfiability(prop, _prop, factbase) -> bool | None:
    ...

pred_to_pos_neg_zero = ...
def get_all_pred_and_expr_from_enc_cnf(enc_cnf) -> tuple[set[Any], set[Any]]:
    ...

def extract_pred_from_old_assum(all_exprs) -> list[Any]:
    """
    Returns a list of relevant new assumption predicate
    based on any old assumptions.

    Raises an UnhandledInput exception if any of the assumptions are
    unhandled.

    Ignored predicate:
    - commutative
    - complex
    - algebraic
    - transcendental
    - extended_real
    - real
    - all matrix predicate
    - rational
    - irrational

    Example
    =======
    >>> from sympy.assumptions.lra_satask import extract_pred_from_old_assum
    >>> from sympy import symbols
    >>> x, y = symbols("x y", positive=True)
    >>> extract_pred_from_old_assum([x, y, 2])
    [Q.positive(x), Q.positive(y)]
    """
    ...

