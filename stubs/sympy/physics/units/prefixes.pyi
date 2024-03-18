from typing import Any, Self
from sympy.core.expr import Expr

"""
Module defining unit prefixe class and some constants.

Constant dict for SI and binary prefixes are defined as PREFIXES and
BIN_PREFIXES.
"""
class Prefix(Expr):
    """
    This class represent prefixes, with their name, symbol and factor.

    Prefixes are used to create derived units from a given unit. They should
    always be encapsulated into units.

    The factor is constructed from a base (default is 10) to some power, and
    it gives the total multiple or fraction. For example the kilometer km
    is constructed from the meter (factor 1) and the kilo (10 to the power 3,
    i.e. 1000). The base can be changed to allow e.g. binary prefixes.

    A prefix multiplied by something will always return the product of this
    other object times the factor, except if the other object:

    - is a prefix and they can be combined into a new prefix;
    - defines multiplication with prefixes (which is the case for the Unit
      class).
    """
    _op_priority = ...
    is_commutative = ...
    def __new__(cls, name, abbrev, exponent, base=..., latex_repr=...) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def abbrev(self):
        ...
    
    @property
    def scale_factor(self):
        ...
    
    @property
    def base(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __mul__(self, other) -> Prefix:
        ...
    
    def __truediv__(self, other) -> Prefix:
        ...
    
    def __rtruediv__(self, other) -> Prefix:
        ...
    


def prefix_unit(unit, prefixes) -> list[Any]:
    """
    Return a list of all units formed by unit and the given prefixes.

    You can use the predefined PREFIXES or BIN_PREFIXES, but you can also
    pass as argument a subdict of them if you do not want all prefixed units.

        >>> from sympy.physics.units.prefixes import (PREFIXES,
        ...                                                 prefix_unit)
        >>> from sympy.physics.units import m
        >>> pref = {"m": PREFIXES["m"], "c": PREFIXES["c"], "d": PREFIXES["d"]}
        >>> prefix_unit(m, pref)  # doctest: +SKIP
        [millimeter, centimeter, decimeter]
    """
    ...

yotta = ...
zetta = ...
exa = ...
peta = ...
tera = ...
giga = ...
mega = ...
kilo = ...
hecto = ...
deca = ...
deci = ...
centi = ...
milli = ...
micro = ...
nano = ...
pico = ...
femto = ...
atto = ...
zepto = ...
yocto = ...
PREFIXES = ...
kibi = ...
mebi = ...
gibi = ...
tebi = ...
pebi = ...
exbi = ...
BIN_PREFIXES = ...
