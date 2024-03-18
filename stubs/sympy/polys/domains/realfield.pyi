from typing import Any, Self
from sympy.core.numbers import Float
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.utilities import public

@public
class RealField(Field, CharacteristicZero, SimpleDomain):
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
        ...
    
    def from_sympy(self, expr) -> Any:
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
        ...
    
    def get_ring(self) -> Self:
        ...
    
    def get_exact(self) -> Any:
        ...
    
    def gcd(self, a, b) -> Any:
        ...
    
    def lcm(self, a, b):
        ...
    
    def almosteq(self, a, b, tolerance=...) -> Any:
        ...
    
    def is_square(self, a):
        ...
    
    def exsqrt(self, a) -> None:
        ...
    


RR = ...
