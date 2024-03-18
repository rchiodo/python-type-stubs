from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.matrices.expressions.matexpr import MatrixExpr

class Adjoint(MatrixExpr):
    """
    The Hermitian adjoint of a matrix expression.

    This is a symbolic object that simply stores its argument without
    evaluating it. To actually compute the adjoint, use the ``adjoint()``
    function.

    Examples
    ========

    >>> from sympy import MatrixSymbol, Adjoint, adjoint
    >>> A = MatrixSymbol('A', 3, 5)
    >>> B = MatrixSymbol('B', 5, 3)
    >>> Adjoint(A*B)
    Adjoint(A*B)
    >>> adjoint(A*B)
    Adjoint(B)*Adjoint(A)
    >>> adjoint(A*B) == Adjoint(A*B)
    False
    >>> adjoint(A*B) == Adjoint(A*B).doit()
    True
    """
    is_Adjoint = ...
    def doit(self, **hints) -> type[UndefinedFunction]:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    


