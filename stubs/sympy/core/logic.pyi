from typing import Any, Optional, Self

"""Logic expressions handling

NOTE
----

at present this is mainly needed for facts.py, feel free however to improve
this stuff for general purpose.
"""
FuzzyBool = Optional[bool]
def fuzzy_bool(x) -> bool | None:
    """Return True, False or None according to x.

    Whereas bool(x) returns True or False, fuzzy_bool allows
    for the None value and non-false values (which become None), too.

    Examples
    ========

    >>> from sympy.core.logic import fuzzy_bool
    >>> from sympy.abc import x
    >>> fuzzy_bool(x), fuzzy_bool(None)
    (None, None)
    >>> bool(x), bool(None)
    (True, False)

    """
    ...

def fuzzy_and(args) -> bool | None:
    """Return True (all True), False (any False) or None.

    Examples
    ========

    >>> from sympy.core.logic import fuzzy_and
    >>> from sympy import Dummy

    If you had a list of objects to test the commutivity of
    and you want the fuzzy_and logic applied, passing an
    iterator will allow the commutativity to only be computed
    as many times as necessary. With this list, False can be
    returned after analyzing the first symbol:

    >>> syms = [Dummy(commutative=False), Dummy()]
    >>> fuzzy_and(s.is_commutative for s in syms)
    False

    That False would require less work than if a list of pre-computed
    items was sent:

    >>> fuzzy_and([s.is_commutative for s in syms])
    False
    """
    ...

def fuzzy_not(v) -> bool:
    """
    Not in fuzzy logic

    Return None if `v` is None else `not v`.

    Examples
    ========

    >>> from sympy.core.logic import fuzzy_not
    >>> fuzzy_not(True)
    False
    >>> fuzzy_not(None)
    >>> fuzzy_not(False)
    True

    """
    ...

def fuzzy_or(args) -> bool | None:
    """
    Or in fuzzy logic. Returns True (any True), False (all False), or None

    See the docstrings of fuzzy_and and fuzzy_not for more info.  fuzzy_or is
    related to the two by the standard De Morgan's law.

    >>> from sympy.core.logic import fuzzy_or
    >>> fuzzy_or([True, False])
    True
    >>> fuzzy_or([True, None])
    True
    >>> fuzzy_or([False, False])
    False
    >>> print(fuzzy_or([False, None]))
    None

    """
    ...

def fuzzy_xor(args) -> bool | None:
    """Return None if any element of args is not True or False, else
    True (if there are an odd number of True elements), else False."""
    ...

def fuzzy_nand(args) -> bool | None:
    """Return False if all args are True, True if they are all False,
    else None."""
    ...

class Logic:
    """Logical expression"""
    op_2class: dict[str, type[Logic]] = ...
    def __new__(cls, *args) -> Self:
        ...
    
    def __getnewargs__(self):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(a, b) -> bool:
        ...
    
    def __ne__(a, b) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __cmp__(self, other) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    @staticmethod
    def fromstring(text) -> Not | bool | Logic:
        """Logic from string with space around & and | but none after !.

           e.g.

           !a & b | c
        """
        ...
    


class AndOr_Base(Logic):
    def __new__(cls, *args) -> bool | Self:
        ...
    
    @classmethod
    def flatten(cls, args) -> tuple[Any, ...]:
        ...
    


class And(AndOr_Base):
    op_x_notx = ...
    def expand(self) -> bool | Or | Self:
        ...
    


class Or(AndOr_Base):
    op_x_notx = ...


class Not(Logic):
    def __new__(cls, arg) -> Self | bool:
        ...
    
    @property
    def arg(self):
        ...
    


