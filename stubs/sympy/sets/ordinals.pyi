from types import NotImplementedType
from typing import Literal, Self
from sympy.core import Basic

class OmegaPower(Basic):
    """
    Represents ordinal exponential and multiplication terms one of the
    building blocks of the :class:`Ordinal` class.
    In ``OmegaPower(a, b)``, ``a`` represents exponent and ``b`` represents multiplicity.
    """
    def __new__(cls, a, b) -> Self:
        ...
    
    @property
    def exp(self) -> Basic:
        ...
    
    @property
    def mult(self) -> Basic:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    


class Ordinal(Basic):
    """
    Represents ordinals in Cantor normal form.

    Internally, this class is just a list of instances of OmegaPower.

    Examples
    ========
    >>> from sympy import Ordinal, OmegaPower
    >>> from sympy.sets.ordinals import omega
    >>> w = omega
    >>> w.is_limit_ordinal
    True
    >>> Ordinal(OmegaPower(w + 1, 1), OmegaPower(3, 2))
    w**(w + 1) + w**3*2
    >>> 3 + w
    w
    >>> (w + 1) * w
    w**2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Ordinal_arithmetic
    """
    def __new__(cls, *terms) -> Self:
        ...
    
    @property
    def terms(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def leading_term(self) -> Basic:
        ...
    
    @property
    def trailing_term(self) -> Basic:
        ...
    
    @property
    def is_successor_ordinal(self) -> Literal[False]:
        ...
    
    @property
    def is_limit_ordinal(self) -> bool:
        ...
    
    @property
    def degree(self):
        ...
    
    @classmethod
    def convert(cls, integer_value) -> OrdinalZero | Ordinal:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __add__(self, other) -> NotImplementedType | Self | Ordinal:
        ...
    
    def __radd__(self, other) -> NotImplementedType | OrdinalZero | Ordinal:
        ...
    
    def __mul__(self, other) -> NotImplementedType | OrdinalZero | Ordinal:
        ...
    
    def __rmul__(self, other) -> NotImplementedType | OrdinalZero | Ordinal:
        ...
    
    def __pow__(self, other) -> NotImplementedType | Ordinal:
        ...
    


class OrdinalZero(Ordinal):
    """The ordinal zero.

    OrdinalZero can be imported as ``ord0``.
    """
    ...


class OrdinalOmega(Ordinal):
    """The ordinal omega which forms the base of all ordinals in cantor normal form.

    OrdinalOmega can be imported as ``omega``.

    Examples
    ========

    >>> from sympy.sets.ordinals import omega
    >>> omega + omega
    w*2
    """
    def __new__(cls) -> Self:
        ...
    
    @property
    def terms(self) -> tuple[OmegaPower]:
        ...
    


ord0 = ...
omega = ...
