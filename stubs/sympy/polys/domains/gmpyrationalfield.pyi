from typing import Any
from sympy.core.numbers import Rational
from sympy.polys.domains.groundtypes import _GMPYRational, GMPYRational
from sympy.polys.domains.rationalfield import RationalField
from sympy.utilities import public

"""Implementation of :class:`GMPYRationalField` class. """
@public
class GMPYRationalField(RationalField):
    """Rational field based on GMPY's ``mpq`` type.

    This will be the implementation of :ref:`QQ` if ``gmpy`` or ``gmpy2`` is
    installed. Elements will be of type ``gmpy.mpq``.
    """
    dtype = GMPYRational
    zero = dtype(0)
    one = dtype(1)
    tp = type(one)
    alias = ...
    def __init__(self) -> None:
        ...
    
    def get_ring(self) -> Any:
        """Returns ring associated with ``self``. """
        ...
    
    def to_sympy(self, a) -> Rational:
        """Convert ``a`` to a SymPy object. """
        ...
    
    def from_sympy(self, a) -> _GMPYRational:
        """Convert SymPy's Integer to ``dtype``. """
        ...
    
    def from_ZZ_python(K1, a, K0) -> _GMPYRational:
        """Convert a Python ``int`` object to ``dtype``. """
        ...
    
    def from_QQ_python(K1, a, K0) -> _GMPYRational:
        """Convert a Python ``Fraction`` object to ``dtype``. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0) -> _GMPYRational:
        """Convert a GMPY ``mpz`` object to ``dtype``. """
        ...
    
    def from_QQ_gmpy(K1, a, K0):
        """Convert a GMPY ``mpq`` object to ``dtype``. """
        ...
    
    def from_GaussianRationalField(K1, a, K0) -> _GMPYRational | None:
        """Convert a ``GaussianElement`` object to ``dtype``. """
        ...
    
    def from_RealField(K1, a, K0) -> _GMPYRational:
        """Convert a mpmath ``mpf`` object to ``dtype``. """
        ...
    
    def exquo(self, a, b):
        """Exact quotient of ``a`` and ``b``, implies ``__truediv__``.  """
        ...
    
    def quo(self, a, b):
        """Quotient of ``a`` and ``b``, implies ``__truediv__``. """
        ...
    
    def rem(self, a, b) -> dtype:
        """Remainder of ``a`` and ``b``, implies nothing.  """
        ...
    
    def div(self, a, b) -> tuple[Any, dtype]:
        """Division of ``a`` and ``b``, implies ``__truediv__``. """
        ...
    
    def numer(self, a):
        """Returns numerator of ``a``. """
        ...
    
    def denom(self, a):
        """Returns denominator of ``a``. """
        ...
    
    def factorial(self, a) -> _GMPYRational:
        """Returns factorial of ``a``. """
        ...
    


