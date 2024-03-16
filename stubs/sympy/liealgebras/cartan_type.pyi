from sympy.core import Atom

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
    
    def series(self) -> Callable[[], ...]:
        """
        Returns the type of the Lie algebra
        """
        ...
    


