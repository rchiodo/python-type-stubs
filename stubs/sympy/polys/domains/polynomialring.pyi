from sympy.polys.domains.ring import Ring
from sympy.polys.domains.compositedomain import CompositeDomain
from sympy.utilities import public

"""Implementation of :class:`PolynomialRing` class. """
@public
class PolynomialRing(Ring, CompositeDomain):
    """A class for representing multivariate polynomial rings. """
    is_Poly = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    def __init__(self, domain_or_ring, symbols=..., order=...) -> None:
        ...
    
    def new(self, element) -> PolyElement:
        ...
    
    @property
    def zero(self):
        ...
    
    @property
    def one(self):
        ...
    
    @property
    def order(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        """Returns `True` if two domains are equivalent. """
        ...
    
    def is_unit(self, a) -> Literal[False]:
        """Returns ``True`` if ``a`` is a unit of ``self``"""
        ...
    
    def canonical_unit(self, a):
        ...
    
    def to_sympy(self, a):
        """Convert `a` to a SymPy object. """
        ...
    
    def from_sympy(self, a):
        """Convert SymPy's expression to `dtype`. """
        ...
    
    def from_ZZ(K1, a, K0):
        """Convert a Python `int` object to `dtype`. """
        ...
    
    def from_ZZ_python(K1, a, K0):
        """Convert a Python `int` object to `dtype`. """
        ...
    
    def from_QQ(K1, a, K0):
        """Convert a Python `Fraction` object to `dtype`. """
        ...
    
    def from_QQ_python(K1, a, K0):
        """Convert a Python `Fraction` object to `dtype`. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0):
        """Convert a GMPY `mpz` object to `dtype`. """
        ...
    
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY `mpq` object to `dtype`. """
        ...
    
    def from_GaussianIntegerRing(K1, a, K0):
        """Convert a `GaussianInteger` object to `dtype`. """
        ...
    
    def from_GaussianRationalField(K1, a, K0):
        """Convert a `GaussianRational` object to `dtype`. """
        ...
    
    def from_RealField(K1, a, K0):
        """Convert a mpmath `mpf` object to `dtype`. """
        ...
    
    def from_ComplexField(K1, a, K0):
        """Convert a mpmath `mpf` object to `dtype`. """
        ...
    
    def from_AlgebraicField(K1, a, K0) -> PolyElement | None:
        """Convert an algebraic number to ``dtype``. """
        ...
    
    def from_PolynomialRing(K1, a, K0) -> None:
        """Convert a polynomial to ``dtype``. """
        ...
    
    def from_FractionField(K1, a, K0) -> None:
        """Convert a rational function to ``dtype``. """
        ...
    
    def from_GlobalPolynomialRing(K1, a, K0) -> None:
        """Convert from old poly ring to ``dtype``. """
        ...
    
    def get_field(self) -> Any:
        """Returns a field associated with `self`. """
        ...
    
    def is_positive(self, a):
        """Returns True if `LC(a)` is positive. """
        ...
    
    def is_negative(self, a):
        """Returns True if `LC(a)` is negative. """
        ...
    
    def is_nonpositive(self, a):
        """Returns True if `LC(a)` is non-positive. """
        ...
    
    def is_nonnegative(self, a):
        """Returns True if `LC(a)` is non-negative. """
        ...
    
    def gcdex(self, a, b):
        """Extended GCD of `a` and `b`. """
        ...
    
    def gcd(self, a, b):
        """Returns GCD of `a` and `b`. """
        ...
    
    def lcm(self, a, b):
        """Returns LCM of `a` and `b`. """
        ...
    
    def factorial(self, a):
        """Returns factorial of `a`. """
        ...
    


