from typing import Any, Callable, Self
from sympy.core import Atom
from sympy.liealgebras.type_a import TypeA
from sympy.liealgebras.type_b import TypeB
from sympy.liealgebras.type_c import TypeC
from sympy.liealgebras.type_d import TypeD
from sympy.liealgebras.type_e import TypeE
from sympy.liealgebras.type_f import TypeF
from sympy.liealgebras.type_g import TypeG

class CartanType_generator:
    """
    Constructor for actually creating things
    """
    def __call__(self, *args) -> TypeA | TypeB | TypeC | TypeD | TypeE | TypeF | TypeG | None:
        ...
    


CartanType = ...
class Standard_Cartan(Atom):
    """
    Concrete base class for Cartan types such as A4, etc
    """
    def __new__(cls, series, n) -> Self:
        ...
    
    def rank(self):
        """
        Returns the rank of the Lie algebra
        """
        ...
    
    def series(self) -> Callable[[], Any]:
        """
        Returns the type of the Lie algebra
        """
        ...
    


