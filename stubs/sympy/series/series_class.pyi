from typing import Any, Generator
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.cache import cacheit

"""
Contains the base class for series
Made using sequences in mind
"""
class SeriesBase(Expr):
    """Base Class for series"""
    @property
    def interval(self):
        """The interval on which the series is defined"""
        ...
    
    @property
    def start(self):
        """The starting point of the series. This point is included"""
        ...
    
    @property
    def stop(self):
        """The ending point of the series. This point is included"""
        ...
    
    @property
    def length(self):
        """Length of the series expansion"""
        ...
    
    @property
    def variables(self) -> tuple[()]:
        """Returns a tuple of variables that are bounded"""
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        """
        This method returns the symbols in the object, excluding those
        that take on a specific value (i.e. the dummy symbols).
        """
        ...
    
    @cacheit
    def term(self, pt):
        """Term at point pt of a series"""
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __getitem__(self, index) -> list[Any] | None:
        ...
    


