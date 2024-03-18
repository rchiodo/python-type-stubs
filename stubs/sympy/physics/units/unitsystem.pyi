from typing import Dict as tDict, Set as tSet
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.physics.units.dimensions import _QuantityMapper
from sympy.physics.units.quantities import Quantity
from sympy.physics.units.dimensions import Dimension
from sympy.series.order import Order

"""
Unit system for physical quantities; include definition of constants.
"""
class UnitSystem(_QuantityMapper):
    """
    UnitSystem represents a coherent set of units.

    A unit system is basically a dimension system with notions of scales. Many
    of the methods are defined in the same way.

    It is much better if all base units have a symbol.
    """
    _unit_systems: tDict[str, UnitSystem] = ...
    def __init__(self, base_units, units=..., name=..., descr=..., dimension_system=..., derived_units: tDict[Dimension, Quantity] = ...) -> None:
        ...
    
    def __str__(self) -> str:
        """
        Return the name of the system.

        If it does not exist, then it makes a list of symbols (or names) of
        the base dimensions.
        """
        ...
    
    def __repr__(self) -> str:
        ...
    
    def extend(self, base, units=..., name=..., description=..., dimension_system=..., derived_units: tDict[Dimension, Quantity] = ...) -> UnitSystem:
        """Extend the current system into a new one.

        Take the base and normal units of the current system to merge
        them to the base and normal units given in argument.
        If not provided, name and description are overridden by empty strings.
        """
        ...
    
    def get_dimension_system(self) -> None:
        ...
    
    def get_quantity_dimension(self, unit) -> Expr | Dimension:
        ...
    
    def get_quantity_scale_factor(self, unit):
        ...
    
    @staticmethod
    def get_unit_system(unit_system) -> UnitSystem:
        ...
    
    @staticmethod
    def get_default_unit_system() -> UnitSystem:
        ...
    
    @property
    def dim(self) -> int:
        """
        Give the dimension of the system.

        That is return the number of units forming the basis.
        """
        ...
    
    @property
    def is_consistent(self):
        """
        Check if the underlying dimension system is consistent.
        """
        ...
    
    @property
    def derived_units(self) -> tDict[Dimension, Quantity]:
        ...
    
    def get_dimensional_expr(self, expr) -> Order | type[UndefinedFunction]:
        ...
    
    def get_units_non_prefixed(self) -> tSet[Quantity]:
        """
        Return the units of the system that do not have a prefix.
        """
        ...
    


