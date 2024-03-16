from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.utilities import public

"""Implementation of :class:`ComplexField` class. """
@public
class ComplexField(Field, CharacteristicZero, SimpleDomain):
    """Complex numbers up to the given precision. """
    rep = ...
    is_CC = ...
    is_Exact = ...
    is_Numerical = ...
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
    
    def dtype(self, x, y=...) -> Any:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def to_sympy(self, element):
        """Convert ``element`` to SymPy number. """
        ...
    
    def from_sympy(self, expr) -> Any:
        """Convert SymPy's number to ``dtype``. """
        ...
    
    def from_ZZ(self, element, base) -> Any:
        ...
    
    def from_ZZ_gmpy(self, element, base) -> Any:
        ...
    
    def from_ZZ_python(self, element, base) -> Any:
        ...
    
    def from_QQ(self, element, base) -> Any:
        ...
    
    def from_QQ_python(self, element, base):
        ...
    
    def from_QQ_gmpy(self, element, base) -> Any:
        ...
    
    def from_GaussianIntegerRing(self, element, base) -> Any:
        ...
    
    def from_GaussianRationalField(self, element, base) -> Any:
        ...
    
    def from_AlgebraicField(self, element, base) -> Any:
        ...
    
    def from_RealField(self, element, base) -> Any:
        ...
    
    def from_ComplexField(self, element, base) -> Any:
        ...
    
    def get_ring(self):
        """Returns a ring associated with ``self``. """
        ...
    
    def get_exact(self) -> GaussianRationalField:
        """Returns an exact domain associated with ``self``. """
        ...
    
    def is_negative(self, element) -> Literal[False]:
        """Returns ``False`` for any ``ComplexElement``. """
        ...
    
    def is_positive(self, element) -> Literal[False]:
        """Returns ``False`` for any ``ComplexElement``. """
        ...
    
    def is_nonnegative(self, element) -> Literal[False]:
        """Returns ``False`` for any ``ComplexElement``. """
        ...
    
    def is_nonpositive(self, element) -> Literal[False]:
        """Returns ``False`` for any ``ComplexElement``. """
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
    
    def is_square(self, a) -> Literal[True]:
        """Returns ``True``. Every complex number has a complex square root."""
        ...
    
    def exsqrt(self, a):
        r"""Returns the principal complex square root of ``a``.

        Explanation
        ===========
        The argument of the principal square root is always within
        $(-\frac{\pi}{2}, \frac{\pi}{2}]$. The square root may be
        slightly inaccurate due to floating point rounding error.
        """
        ...
    


CC = ...
