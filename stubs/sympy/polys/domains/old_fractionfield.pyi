from sympy.polys.domains.field import Field
from sympy.polys.domains.compositedomain import CompositeDomain
from sympy.polys.polyclasses import DMF
from sympy.utilities import public

"""Implementation of :class:`FractionField` class. """
@public
class FractionField(Field, CompositeDomain):
    """A class for representing rational function fields. """
    dtype = DMF
    is_Frac = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    def __init__(self, dom, *gens) -> None:
        ...
    
    def set_domain(self, dom) -> Self:
        """Make a new fraction field with given domain. """
        ...
    
    def new(self, element) -> dtype:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        """Returns ``True`` if two domains are equivalent. """
        ...
    
    def to_sympy(self, a):
        """Convert ``a`` to a SymPy object. """
        ...
    
    def from_sympy(self, a):
        """Convert SymPy's expression to ``dtype``. """
        ...
    
    def from_ZZ(K1, a, K0):
        """Convert a Python ``int`` object to ``dtype``. """
        ...
    
    def from_ZZ_python(K1, a, K0):
        """Convert a Python ``int`` object to ``dtype``. """
        ...
    
    def from_QQ_python(K1, a, K0):
        """Convert a Python ``Fraction`` object to ``dtype``. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpz`` object to ``dtype``. """
        ...
    
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpq`` object to ``dtype``. """
        ...
    
    def from_RealField(K1, a, K0):
        """Convert a mpmath ``mpf`` object to ``dtype``. """
        ...
    
    def from_GlobalPolynomialRing(K1, a, K0):
        """Convert a ``DMF`` object to ``dtype``. """
        ...
    
    def from_FractionField(K1, a, K0) -> None:
        """
        Convert a fraction field element to another fraction field.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMF
        >>> from sympy.polys.domains import ZZ, QQ
        >>> from sympy.abc import x

        >>> f = DMF(([ZZ(1), ZZ(2)], [ZZ(1), ZZ(1)]), ZZ)

        >>> QQx = QQ.old_frac_field(x)
        >>> ZZx = ZZ.old_frac_field(x)

        >>> QQx.from_FractionField(f, ZZx)
        DMF([1, 2], [1, 1], QQ)

        """
        ...
    
    def get_ring(self) -> Any:
        """Returns a ring associated with ``self``. """
        ...
    
    def poly_ring(self, *gens):
        """Returns a polynomial ring, i.e. `K[X]`. """
        ...
    
    def frac_field(self, *gens):
        """Returns a fraction field, i.e. `K(X)`. """
        ...
    
    def is_positive(self, a):
        """Returns True if ``a`` is positive. """
        ...
    
    def is_negative(self, a):
        """Returns True if ``a`` is negative. """
        ...
    
    def is_nonpositive(self, a):
        """Returns True if ``a`` is non-positive. """
        ...
    
    def is_nonnegative(self, a):
        """Returns True if ``a`` is non-negative. """
        ...
    
    def numer(self, a):
        """Returns numerator of ``a``. """
        ...
    
    def denom(self, a):
        """Returns denominator of ``a``. """
        ...
    
    def factorial(self, a) -> dtype:
        """Returns factorial of ``a``. """
        ...
    


