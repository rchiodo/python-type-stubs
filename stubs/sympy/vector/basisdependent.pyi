from typing import TYPE_CHECKING
from sympy.core.decorators import _sympifyit, call_highest_priority
from sympy.core import Add, Mul
from sympy.core.expr import Expr
from sympy.vector.vector import BaseVector

if TYPE_CHECKING:
    ...
class BasisDependent(Expr):
    """
    Super class containing functionality common to vectors and
    dyadics.
    Named so because the representation of these quantities in
    sympy.vector is dependent on the basis they are expressed in.
    """
    zero: BasisDependentZero
    @call_highest_priority('__radd__')
    def __add__(self, other):
        ...
    
    @call_highest_priority('__add__')
    def __radd__(self, other):
        ...
    
    @call_highest_priority('__rsub__')
    def __sub__(self, other):
        ...
    
    @call_highest_priority('__sub__')
    def __rsub__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rmul__')
    def __mul__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__mul__')
    def __rmul__(self, other):
        ...
    
    def __neg__(self):
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rtruediv__')
    def __truediv__(self, other):
        ...
    
    @call_highest_priority('__truediv__')
    def __rtruediv__(self, other) -> TypeError:
        ...
    
    def evalf(self, n=..., subs=..., maxn=..., chop=..., strict=..., quad=..., verbose=...) -> BasisDependentZero:
        """
        Implements the SymPy evalf routine for this quantity.

        evalf's documentation
        =====================

        """
        ...
    
    n = ...
    def simplify(self, **kwargs):
        """
        Implements the SymPy simplify routine for this quantity.

        simplify's documentation
        ========================

        """
        ...
    
    def trigsimp(self, **opts):
        """
        Implements the SymPy trigsimp routine, for this quantity.

        trigsimp's documentation
        ========================

        """
        ...
    
    def as_numer_denom(self) -> tuple[Self, Any]:
        """
        Returns the expression as a tuple wrt the following
        transformation -

        expression -> a/b -> a, b

        """
        ...
    
    def factor(self, *args, **kwargs):
        """
        Implements the SymPy factor routine, on the scalar parts
        of a basis-dependent expression.

        factor's documentation
        ========================

        """
        ...
    
    def as_coeff_Mul(self, rational=...) -> tuple[Any, Self]:
        """Efficiently extract the coefficient of a product."""
        ...
    
    def as_coeff_add(self, *deps) -> tuple[Literal[0], tuple[Any, ...]]:
        """Efficiently extract the coefficient of a summation."""
        ...
    
    def diff(self, *args, **kwargs):
        """
        Implements the SymPy diff routine, for vectors.

        diff's documentation
        ========================

        """
        ...
    
    def doit(self, **hints):
        """Calls .doit() on each term in the Dyadic"""
        ...
    


class BasisDependentAdd(BasisDependent, Add):
    """
    Denotes sum of basis dependent quantities such that they cannot
    be expressed as base or Mul instances.
    """
    def __new__(cls, *args, **options) -> BasisDependentZero | Order:
        ...
    


class BasisDependentMul(BasisDependent, Mul):
    """
    Denotes product of base- basis dependent quantity with a scalar.
    """
    def __new__(cls, *args, **options) -> Order | BasisDependentZero:
        ...
    


class BasisDependentZero(BasisDependent):
    """
    Class to denote a zero basis dependent instance.
    """
    components: dict[BaseVector, Expr] = ...
    _latex_form: str
    def __new__(cls) -> Self:
        ...
    
    def __hash__(self) -> int:
        ...
    
    @call_highest_priority('__req__')
    def __eq__(self, other) -> bool:
        ...
    
    __req__ = ...
    @call_highest_priority('__radd__')
    def __add__(self, other):
        ...
    
    @call_highest_priority('__add__')
    def __radd__(self, other):
        ...
    
    @call_highest_priority('__rsub__')
    def __sub__(self, other):
        ...
    
    @call_highest_priority('__sub__')
    def __rsub__(self, other):
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def normalize(self) -> Self:
        """
        Returns the normalized version of this vector.
        """
        ...
    


