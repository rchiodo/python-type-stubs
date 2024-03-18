from typing import Any
from sympy.core.numbers import Integer, Rational
from sympy.polys.domains.rationalfield import RationalField
from sympy.utilities import public

"""Implementation of :class:`PythonRationalField` class. """
@public
class PythonRationalField(RationalField):
    """Rational field based on :ref:`MPQ`.

    This will be used as :ref:`QQ` if ``gmpy`` and ``gmpy2`` are not
    installed. Elements are instances of :ref:`MPQ`.
    """
    dtype = ...
    zero = ...
    one = ...
    alias = ...
    def __init__(self) -> None:
        ...
    
    def get_ring(self) -> Any:
        """Returns ring associated with ``self``. """
        ...
    
    def to_sympy(self, a) -> Rational | Integer:
        """Convert `a` to a SymPy object. """
        ...
    
    def from_sympy(self, a) -> Any:
        """Convert SymPy's Rational to `dtype`. """
        ...
    
    def from_ZZ_python(K1, a, K0) -> Any:
        """Convert a Python `int` object to `dtype`. """
        ...
    
    def from_QQ_python(K1, a, K0):
        """Convert a Python `Fraction` object to `dtype`. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0) -> Any:
        """Convert a GMPY `mpz` object to `dtype`. """
        ...
    
    def from_QQ_gmpy(K1, a, K0) -> Any:
        """Convert a GMPY `mpq` object to `dtype`. """
        ...
    
    def from_RealField(K1, a, K0) -> Any:
        """Convert a mpmath `mpf` object to `dtype`. """
        ...
    
    def numer(self, a):
        """Returns numerator of `a`. """
        ...
    
    def denom(self, a):
        """Returns denominator of `a`. """
        ...
    


