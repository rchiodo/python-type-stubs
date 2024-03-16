from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.utilities import public

"""Implementation of :class:`RealField` class. """
@public
class RealField(Field, CharacteristicZero, SimpleDomain):
    """Real numbers up to the given precision. """
    rep = ...
    is_RR = ...
    is_Exact = ...
    is_Numerical = ...
    is_PID = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    _default_precision = ...
    @property
    def has_default_precision(self) -> Any:
        ...
    
    @property
    def precision(self) -> Any:
        ...
    
    @property
    def dps(self) -> Any:
        ...
    
    @property
    def tolerance(self) -> Any:
        ...
    
    def __init__(self, prec=..., dps=..., tol=...) -> None:
        ...
    
    @property
    def tp(self) -> Any:
        ...
    
    def dtype(self, arg) -> Any:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def to_sympy(self, element) -> Float:
        """Convert ``element`` to SymPy number. """
        ...
    
    def from_sympy(self, expr) -> Any:
        """Convert SymPy's number to ``dtype``. """
        ...
    
    def from_ZZ(self, element, base) -> Any:
        ...
    
    def from_ZZ_python(self, element, base) -> Any:
        ...
    
    def from_ZZ_gmpy(self, element, base) -> Any:
        ...
    
    def from_QQ(self, element, base) -> Any:
        ...
    
    def from_QQ_python(self, element, base) -> Any:
        ...
    
    def from_QQ_gmpy(self, element, base) -> Any:
        ...
    
    def from_AlgebraicField(self, element, base) -> Any:
        ...
    
    def from_RealField(self, element, base) -> Any:
        ...
    
    def from_ComplexField(self, element, base) -> Any | None:
        ...
    
    def to_rational(self, element, limit=...) -> Any:
        """Convert a real number to rational number. """
        ...
    
    def get_ring(self) -> Self:
        """Returns a ring associated with ``self``. """
        ...
    
    def get_exact(self) -> Any:
        """Returns an exact domain associated with ``self``. """
        ...
    
    def gcd(self, a, b) -> Any:
        """Returns GCD of ``a`` and ``b``. """
        ...
    
    def lcm(self, a, b):
        """Returns LCM of ``a`` and ``b``. """
        ...
    
    def almosteq(self, a, b, tolerance=...) -> Any:
        """Check if ``a`` and ``b`` are almost equal. """
        ...
    
    def is_square(self, a):
        """Returns ``True`` if ``a >= 0`` and ``False`` otherwise. """
        ...
    
    def exsqrt(self, a) -> None:
        """Non-negative square root for ``a >= 0`` and ``None`` otherwise.

        Explanation
        ===========
        The square root may be slightly inaccurate due to floating point
        rounding error.
        """
        ...
    


RR = ...
