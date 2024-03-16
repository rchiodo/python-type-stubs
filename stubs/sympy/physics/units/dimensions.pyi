from sympy.core.basic import Basic
from sympy.core.expr import Expr

"""
Definition of physical dimensions.

Unit systems will be constructed on top of these dimensions.

Most of the examples in the doc use MKS system and are presented from the
computer point of view: from a human point, adding length to time is not legal
in MKS but it is in natural system; for a computer in natural system there is
no time dimension (but a velocity dimension instead) - in the basis - so the
question of adding time to length has no meaning.
"""
class _QuantityMapper:
    _quantity_scale_factors_global: dict[Expr, Expr] = ...
    _quantity_dimensional_equivalence_map_global: dict[Expr, Expr] = ...
    _quantity_dimension_global: dict[Expr, Expr] = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def set_quantity_dimension(self, quantity, dimension) -> None:
        """
        Set the dimension for the quantity in a unit system.

        If this relation is valid in every unit system, use
        ``quantity.set_global_dimension(dimension)`` instead.
        """
        ...
    
    def set_quantity_scale_factor(self, quantity, scale_factor) -> None:
        """
        Set the scale factor of a quantity relative to another quantity.

        It should be used only once per quantity to just one other quantity,
        the algorithm will then be able to compute the scale factors to all
        other quantities.

        In case the scale factor is valid in every unit system, please use
        ``quantity.set_global_relative_scale_factor(scale_factor)`` instead.
        """
        ...
    
    def get_quantity_dimension(self, unit) -> Expr | Dimension:
        ...
    
    def get_quantity_scale_factor(self, unit):
        ...
    


class Dimension(Expr):
    """
    This class represent the dimension of a physical quantities.

    The ``Dimension`` constructor takes as parameters a name and an optional
    symbol.

    For example, in classical mechanics we know that time is different from
    temperature and dimensions make this difference (but they do not provide
    any measure of these quantites.

        >>> from sympy.physics.units import Dimension
        >>> length = Dimension('length')
        >>> length
        Dimension(length)
        >>> time = Dimension('time')
        >>> time
        Dimension(time)

    Dimensions can be composed using multiplication, division and
    exponentiation (by a number) to give new dimensions. Addition and
    subtraction is defined only when the two objects are the same dimension.

        >>> velocity = length / time
        >>> velocity
        Dimension(length/time)

    It is possible to use a dimension system object to get the dimensionsal
    dependencies of a dimension, for example the dimension system used by the
    SI units convention can be used:

        >>> from sympy.physics.units.systems.si import dimsys_SI
        >>> dimsys_SI.get_dimensional_dependencies(velocity)
        {Dimension(length, L): 1, Dimension(time, T): -1}
        >>> length + length
        Dimension(length)
        >>> l2 = length**2
        >>> l2
        Dimension(length**2)
        >>> dimsys_SI.get_dimensional_dependencies(l2)
        {Dimension(length, L): 2}

    """
    _op_priority = ...
    _dimensional_dependencies = ...
    is_commutative = ...
    is_number = ...
    is_positive = ...
    is_real = ...
    def __new__(cls, name, symbol=...) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def symbol(self):
        ...
    
    def __str__(self) -> str:
        """
        Display the string representation of the dimension.
        """
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def __add__(self, other) -> Self:
        ...
    
    def __radd__(self, other) -> Self:
        ...
    
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    def __pow__(self, other) -> Dimension:
        ...
    
    def __mul__(self, other) -> Dimension | Self:
        ...
    
    def __rmul__(self, other) -> Dimension | Self:
        ...
    
    def __truediv__(self, other) -> Dimension | Self:
        ...
    
    def __rtruediv__(self, other):
        ...
    
    def has_integer_powers(self, dim_sys) -> bool:
        """
        Check if the dimension object has only integer powers.

        All the dimension powers should be integers, but rational powers may
        appear in intermediate steps. This method may be used to check that the
        final result is well-defined.
        """
        ...
    


class DimensionSystem(Basic, _QuantityMapper):
    r"""
    DimensionSystem represents a coherent set of dimensions.

    The constructor takes three parameters:

    - base dimensions;
    - derived dimensions: these are defined in terms of the base dimensions
      (for example velocity is defined from the division of length by time);
    - dependency of dimensions: how the derived dimensions depend
      on the base dimensions.

    Optionally either the ``derived_dims`` or the ``dimensional_dependencies``
    may be omitted.
    """
    def __new__(cls, base_dims, derived_dims=..., dimensional_dependencies=...) -> Self:
        ...
    
    @property
    def base_dims(self) -> Basic:
        ...
    
    @property
    def derived_dims(self) -> Basic:
        ...
    
    @property
    def dimensional_dependencies(self) -> Basic:
        ...
    
    def get_dimensional_dependencies(self, name, mark_dimensionless=...) -> dict[Dimension, int] | dict[Any, int]:
        ...
    
    def equivalent_dims(self, dim1, dim2) -> bool:
        ...
    
    def extend(self, new_base_dims, new_derived_dims=..., new_dim_deps=...) -> DimensionSystem:
        ...
    
    def is_dimensionless(self, dimension) -> bool:
        """
        Check if the dimension object really has a dimension.

        A dimension should have at least one component with non-zero power.
        """
        ...
    
    @property
    def list_can_dims(self) -> tuple[Any, ...]:
        """
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.

        List all canonical dimension names.
        """
        ...
    
    @property
    def inv_can_transf_matrix(self):
        """
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.

        Compute the inverse transformation matrix from the base to the
        canonical dimension basis.

        It corresponds to the matrix where columns are the vector of base
        dimensions in canonical basis.

        This matrix will almost never be used because dimensions are always
        defined with respect to the canonical basis, so no work has to be done
        to get them in this basis. Nonetheless if this matrix is not square
        (or not invertible) it means that we have chosen a bad basis.
        """
        ...
    
    @property
    def can_transf_matrix(self):
        """
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.

        Return the canonical transformation matrix from the canonical to the
        base dimension basis.

        It is the inverse of the matrix computed with inv_can_transf_matrix().
        """
        ...
    
    def dim_can_vector(self, dim) -> Matrix:
        """
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.

        Dimensional representation in terms of the canonical base dimensions.
        """
        ...
    
    def dim_vector(self, dim):
        """
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.


        Vector representation in terms of the base dimensions.
        """
        ...
    
    def print_dim_base(self, dim):
        """
        Give the string expression of a dimension in term of the basis symbols.
        """
        ...
    
    @property
    def dim(self) -> int:
        """
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.

        Give the dimension of the system.

        That is return the number of dimensions forming the basis.
        """
        ...
    
    @property
    def is_consistent(self):
        """
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.

        Check if the system is well defined.
        """
        ...
    


