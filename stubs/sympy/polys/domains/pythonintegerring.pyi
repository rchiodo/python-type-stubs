from sympy.polys.domains.groundtypes import PythonInteger
from sympy.polys.domains.integerring import IntegerRing
from sympy.utilities import public

"""Implementation of :class:`PythonIntegerRing` class. """
@public
class PythonIntegerRing(IntegerRing):
    """Integer ring based on Python's ``int`` type.

    This will be used as :ref:`ZZ` if ``gmpy`` and ``gmpy2`` are not
    installed. Elements are instances of the standard Python ``int`` type.
    """
    dtype = PythonInteger
    zero = dtype(0)
    one = dtype(1)
    alias = ...
    def __init__(self) -> None:
        """Allow instantiation of this domain. """
        ...
    
    def to_sympy(self, a) -> Integer:
        """Convert ``a`` to a SymPy object. """
        ...
    
    def from_sympy(self, a) -> PythonInteger:
        """Convert SymPy's Integer to ``dtype``. """
        ...
    
    def from_FF_python(K1, a, K0):
        """Convert ``ModularInteger(int)`` to Python's ``int``. """
        ...
    
    def from_ZZ_python(K1, a, K0):
        """Convert Python's ``int`` to Python's ``int``. """
        ...
    
    def from_QQ(K1, a, K0) -> None:
        """Convert Python's ``Fraction`` to Python's ``int``. """
        ...
    
    def from_QQ_python(K1, a, K0) -> None:
        """Convert Python's ``Fraction`` to Python's ``int``. """
        ...
    
    def from_FF_gmpy(K1, a, K0) -> PythonInteger:
        """Convert ``ModularInteger(mpz)`` to Python's ``int``. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0) -> PythonInteger:
        """Convert GMPY's ``mpz`` to Python's ``int``. """
        ...
    
    def from_QQ_gmpy(K1, a, K0) -> PythonInteger | None:
        """Convert GMPY's ``mpq`` to Python's ``int``. """
        ...
    
    def from_RealField(K1, a, K0) -> PythonInteger | None:
        """Convert mpmath's ``mpf`` to Python's ``int``. """
        ...
    
    def gcdex(self, a, b) -> tuple[Literal[0], Literal[1], Literal[0]] | tuple[Any | int, Any | int, Any | Literal[0]]:
        """Compute extended GCD of ``a`` and ``b``. """
        ...
    
    def gcd(self, a, b) -> int:
        """Compute GCD of ``a`` and ``b``. """
        ...
    
    def lcm(self, a, b) -> int:
        """Compute LCM of ``a`` and ``b``. """
        ...
    
    def sqrt(self, a):
        """Compute square root of ``a``. """
        ...
    
    def factorial(self, a) -> int:
        """Compute factorial of ``a``. """
        ...
    


