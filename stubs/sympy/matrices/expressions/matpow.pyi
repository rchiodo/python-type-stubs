from sympy.matrices.expressions.matexpr import MatrixExpr

class MatPow(MatrixExpr):
    def __new__(cls, base, exp, evaluate=..., **options) -> Basic | Identity | Inverse | Any | MatPow | Self:
        ...
    
    @property
    def base(self) -> Basic:
        ...
    
    @property
    def exp(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    
    def doit(self, **hints) -> Basic | Identity | Inverse | Any | MatPow:
        ...
    


