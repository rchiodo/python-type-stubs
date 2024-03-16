from sympy.utilities import public

"""
Solving solvable quintics - An implementation of DS Dummit's paper

Paper :
https://www.ams.org/journals/mcom/1991-57-195/S0025-5718-1991-1079014-X/S0025-5718-1991-1079014-X.pdf

Mathematica notebook:
http://www.emba.uvm.edu/~ddummit/quintics/quintics.nb

"""
x = ...
@public
class PolyQuintic:
    """Special functions for solvable quintics"""
    def __init__(self, poly) -> None:
        ...
    
    @property
    def f20(self) -> Any:
        ...
    
    @property
    def b(self) -> tuple[list[Any], list[int], list[int], list[int], list[int]]:
        ...
    
    @property
    def o(self) -> list[int]:
        ...
    
    @property
    def a(self) -> list[int]:
        ...
    
    @property
    def c(self) -> list[int]:
        ...
    
    @property
    def F(self):
        ...
    
    def l0(self, theta):
        ...
    
    def T(self, theta, d) -> list[int]:
        ...
    
    def order(self, theta, d):
        ...
    
    def uv(self, theta, d) -> tuple[Any, Any]:
        ...
    
    @property
    def zeta(self) -> list[Any]:
        ...
    


