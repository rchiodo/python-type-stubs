"""
The classes used here are for the internal use of assumptions system
only and should not be used anywhere else as these do not possess the
signatures common to SymPy objects. For general use of logic constructs
please refer to sympy.logic classes And, Or, Not, etc.
"""
from typing import Any, Self

from sympy.core.logic import And


class Literal:
    """
    The smallest element of a CNF object.

    Parameters
    ==========

    lit : Boolean expression

    is_Not : bool

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import Literal
    >>> from sympy.abc import x
    >>> Literal(Q.even(x))
    Literal(Q.even(x), False)
    >>> Literal(~Q.even(x))
    Literal(Q.even(x), True)
    """
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
    """
    A low-level implementation for Or
    """
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
    """
    A low-level implementation for And
    """
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
    """
    Generates the Negation Normal Form of any boolean expression in terms
    of AND, OR, and Literal objects.

    Examples
    ========

    >>> from sympy import Q, Eq
    >>> from sympy.assumptions.cnf import to_NNF
    >>> from sympy.abc import x, y
    >>> expr = Q.even(x) & ~Q.positive(x)
    >>> to_NNF(expr)
    (Literal(Q.even(x), False) & Literal(Q.positive(x), True))

    Supported boolean objects are converted to corresponding predicates.

    >>> to_NNF(Eq(x, y))
    Literal(Q.eq(x, y), False)

    If ``composite_map`` argument is given, ``to_NNF`` decomposes the
    specified predicate into a combination of primitive predicates.

    >>> cmap = {Q.nonpositive: Q.negative | Q.zero}
    >>> to_NNF(Q.nonpositive, cmap)
    (Literal(Q.negative, False) | Literal(Q.zero, False))
    >>> to_NNF(Q.nonpositive(x), cmap)
    (Literal(Q.negative(x), False) | Literal(Q.zero(x), False))
    """
    ...

def distribute_AND_over_OR(expr) -> CNF | None:
    """
    Distributes AND over OR in the NNF expression.
    Returns the result( Conjunctive Normal Form of expression)
    as a CNF object.
    """
    ...

class CNF:
    """
    Class to represent CNF of a Boolean expression.
    Consists of set of clauses, which themselves are stored as
    frozenset of Literal objects.

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import CNF
    >>> from sympy.abc import x
    >>> cnf = CNF.from_prop(Q.real(x) & ~Q.zero(x))
    >>> cnf.clauses
    {frozenset({Literal(Q.zero(x), True)}),
    frozenset({Literal(Q.negative(x), False),
    Literal(Q.positive(x), False), Literal(Q.zero(x), False)})}
    """
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
        """
        Converts CNF object to SymPy's boolean expression
        retaining the form of expression.
        """
        ...
    


class EncodedCNF:
    """
    Class for encoding the CNF expression.
    """
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
    


