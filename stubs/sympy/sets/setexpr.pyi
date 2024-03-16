from sympy.core import Expr
from sympy.core.decorators import _sympifyit, call_highest_priority

class SetExpr(Expr):
    """An expression that can take on values of a set.

    Examples
    ========

    >>> from sympy import Interval, FiniteSet
    >>> from sympy.sets.setexpr import SetExpr

    >>> a = SetExpr(Interval(0, 5))
    >>> b = SetExpr(FiniteSet(1, 10))
    >>> (a + b).set
    Union(Interval(1, 6), Interval(10, 15))
    >>> (2*a + b).set
    Interval(1, 20)
    """
    _op_priority = ...
    def __new__(cls, setarg) -> Self:
        ...
    
    set = ...
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__radd__')
    def __add__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__add__')
    def __radd__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rmul__')
    def __mul__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__mul__')
    def __rmul__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rsub__')
    def __sub__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__sub__')
    def __rsub__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rpow__')
    def __pow__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__pow__')
    def __rpow__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__rtruediv__')
    def __truediv__(self, other) -> SetExpr:
        ...
    
    @_sympifyit('other', NotImplemented)
    @call_highest_priority('__truediv__')
    def __rtruediv__(self, other) -> SetExpr:
        ...
    


