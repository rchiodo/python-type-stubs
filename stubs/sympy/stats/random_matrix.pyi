from typing import Self
from sympy import Basic
from sympy.stats.rv import PSpace

class RandomMatrixPSpace(PSpace):
    """
    Represents probability space for
    random matrices. It contains the mechanics
    for handling the API calls for random matrices.
    """
    def __new__(cls, sym, model=...) -> Self:
        ...
    
    @property
    def model(self) -> Basic | None:
        ...
    
    def compute_density(self, expr, *args):
        ...
    


