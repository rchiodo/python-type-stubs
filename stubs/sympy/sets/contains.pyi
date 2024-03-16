from sympy.logic.boolalg import Boolean

class Contains(Boolean):
    """
    Asserts that x is an element of the set S.

    Examples
    ========

    >>> from sympy import Symbol, Integer, S, Contains
    >>> Contains(Integer(2), S.Integers)
    True
    >>> Contains(Integer(-2), S.Naturals)
    False
    >>> i = Symbol('i', integer=True)
    >>> Contains(i, S.Naturals)
    Contains(i, Naturals)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Element_%28mathematics%29
    """
    def __new__(cls, x, s, evaluate=...) -> Boolean | Self:
        ...
    
    @property
    def binary_symbols(self) -> set[Any | Basic]:
        ...
    
    def as_set(self) -> Basic:
        ...
    


