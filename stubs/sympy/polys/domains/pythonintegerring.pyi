from typing import Any, Literal
from sympy.core.numbers import Integer
from sympy.polys.domains.groundtypes import PythonInteger
from sympy.polys.domains.integerring import IntegerRing
from sympy.utilities import public

@public
class PythonIntegerRing(IntegerRing):
    dtype = PythonInteger
    zero = dtype(0)
    one = dtype(1)
    alias = ...
    def __init__(self) -> None:
        ...
    
    def to_sympy(self, a) -> Integer:
        ...
    
    def from_sympy(self, a) -> PythonInteger:
        ...
    
    def from_FF_python(K1, a, K0):
        ...
    
    def from_ZZ_python(K1, a, K0):
        ...
    
    def from_QQ(K1, a, K0) -> None:
        ...
    
    def from_QQ_python(K1, a, K0) -> None:
        ...
    
    def from_FF_gmpy(K1, a, K0) -> PythonInteger:
        ...
    
    def from_ZZ_gmpy(K1, a, K0) -> PythonInteger:
        ...
    
    def from_QQ_gmpy(K1, a, K0) -> PythonInteger | None:
        ...
    
    def from_RealField(K1, a, K0) -> PythonInteger | None:
        ...
    
    def gcdex(self, a, b) -> tuple[Literal[0], Literal[1], Literal[0]] | tuple[Any | int, Any | int, Any | Literal[0]]:
        ...
    
    def gcd(self, a, b) -> int:
        ...
    
    def lcm(self, a, b) -> int:
        ...
    
    def sqrt(self, a):
        ...
    
    def factorial(self, a) -> int:
        ...
    


