from typing import Any
from sympy.core.numbers import Integer
from sympy.polys.domains.groundtypes import _GMPYInteger, GMPYInteger
from sympy.polys.domains.integerring import IntegerRing
from sympy.utilities import public

"""Implementation of :class:`GMPYIntegerRing` class. """
@public
class GMPYIntegerRing(IntegerRing):
    """Integer ring based on GMPY's ``mpz`` type.

    This will be the implementation of :ref:`ZZ` if ``gmpy`` or ``gmpy2`` is
    installed. Elements will be of type ``gmpy.mpz``.
    """
    dtype = GMPYInteger
    zero = dtype(0)
    one = dtype(1)
    tp = type(one)
    alias = ...
    def __init__(self) -> None:
        """Allow instantiation of this domain. """
        ...
    
    def to_sympy(self, a) -> Integer:
        """Convert ``a`` to a SymPy object. """
        ...
    
    def from_sympy(self, a) -> _GMPYInteger:
        """Convert SymPy's Integer to ``dtype``. """
        ...
    
    def from_FF_python(K1, a, K0):
        """Convert ``ModularInteger(int)`` to GMPY's ``mpz``. """
        ...
    
    def from_ZZ_python(K1, a, K0) -> _GMPYInteger:
        """Convert Python's ``int`` to GMPY's ``mpz``. """
        ...
    
    def from_QQ(K1, a, K0) -> _GMPYInteger | None:
        """Convert Python's ``Fraction`` to GMPY's ``mpz``. """
        ...
    
    def from_QQ_python(K1, a, K0) -> _GMPYInteger | None:
        """Convert Python's ``Fraction`` to GMPY's ``mpz``. """
        ...
    
    def from_FF_gmpy(K1, a, K0):
        """Convert ``ModularInteger(mpz)`` to GMPY's ``mpz``. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0):
        """Convert GMPY's ``mpz`` to GMPY's ``mpz``. """
        ...
    
    def from_QQ_gmpy(K1, a, K0) -> None:
        """Convert GMPY ``mpq`` to GMPY's ``mpz``. """
        ...
    
    def from_RealField(K1, a, K0) -> _GMPYInteger | None:
        """Convert mpmath's ``mpf`` to GMPY's ``mpz``. """
        ...
    
    def from_GaussianIntegerRing(K1, a, K0) -> None:
        ...
    
    def gcdex(self, a, b) -> tuple[Any, Any, Any]:
        """Compute extended GCD of ``a`` and ``b``. """
        ...
    
    def gcd(self, a, b):
        """Compute GCD of ``a`` and ``b``. """
        ...
    
    def lcm(self, a, b):
        """Compute LCM of ``a`` and ``b``. """
        ...
    
    def sqrt(self, a):
        """Compute square root of ``a``. """
        ...
    
    def factorial(self, a) -> int:
        """Compute factorial of ``a``. """
        ...
    


