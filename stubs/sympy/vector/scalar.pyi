from sympy.core import AtomicExpr

class BaseScalar(AtomicExpr):
    """
    A coordinate symbol/base scalar.

    Ideally, users should not instantiate this class.

    """
    def __new__(cls, index, system, pretty_str=..., latex_str=...) -> Self:
        ...
    
    is_commutative = ...
    is_symbol = ...
    @property
    def free_symbols(self) -> set[Self]:
        ...
    
    _diff_wrt = ...
    precedence = ...
    @property
    def system(self):
        ...
    


