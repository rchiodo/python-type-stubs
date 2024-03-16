from sympy.core.expr import AtomicExpr

"""
Physical quantities.
"""
class Quantity(AtomicExpr):
    """
    Physical quantity: can be a unit of measure, a constant or a generic quantity.
    """
    is_commutative = ...
    is_real = ...
    is_number = ...
    is_nonzero = ...
    is_physical_constant = ...
    _diff_wrt = ...
    def __new__(cls, name, abbrev=..., latex_repr=..., pretty_unicode_repr=..., pretty_ascii_repr=..., mathml_presentation_repr=..., is_prefixed=..., **assumptions) -> Self:
        ...
    
    def set_global_dimension(self, dimension) -> None:
        ...
    
    def set_global_relative_scale_factor(self, scale_factor, reference_quantity) -> None:
        """
        Setting a scale factor that is valid across all unit system.
        """
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def dimension(self) -> Expr | Dimension:
        ...
    
    @property
    def abbrev(self):
        """
        Symbol representing the unit name.

        Prepend the abbreviation with the prefix symbol if it is defines.
        """
        ...
    
    @property
    def scale_factor(self):
        """
        Overall magnitude of the quantity as compared to the canonical units.
        """
        ...
    
    def convert_to(self, other, unit_system=...) -> Add | Quantity:
        """
        Convert the quantity to another quantity of same dimensions.

        Examples
        ========

        >>> from sympy.physics.units import speed_of_light, meter, second
        >>> speed_of_light
        speed_of_light
        >>> speed_of_light.convert_to(meter/second)
        299792458*meter/second

        >>> from sympy.physics.units import liter
        >>> liter.convert_to(meter**3)
        meter**3/1000
        """
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        """Return free symbols from quantity."""
        ...
    
    @property
    def is_prefixed(self) -> bool:
        """Whether or not the quantity is prefixed. Eg. `kilogram` is prefixed, but `gram` is not."""
        ...
    


class PhysicalConstant(Quantity):
    """Represents a physical constant, eg. `speed_of_light` or `avogadro_constant`."""
    is_physical_constant = ...


