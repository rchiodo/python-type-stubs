from typing import Any
from sympy.printing.codeprinter import CodePrinter

"""
Fortran code printer

The FCodePrinter converts single SymPy expressions into single Fortran
expressions, using the functions defined in the Fortran 77 standard where
possible. Some useful pointers to Fortran can be found on wikipedia:

https://en.wikipedia.org/wiki/Fortran

Most of the code below is based on the "Professional Programmer\'s Guide to
Fortran77" by Clive G. Page:

https://www.star.le.ac.uk/~cgp/prof77.html

Fortran is a case-insensitive language. This might cause trouble because
SymPy is case sensitive. So, fcode adds underscores to variable names when
it is necessary to make them different for Fortran.
"""
known_functions = ...
class FCodePrinter(CodePrinter):
    """A printer to convert SymPy expressions to strings of Fortran code"""
    printmethod = ...
    language = ...
    type_aliases = ...
    type_mappings = ...
    type_modules = ...
    _default_settings: dict[str, Any] = ...
    _operators = ...
    _relationals = ...
    def __init__(self, settings=...) -> None:
        ...
    
    def indent_code(self, code) -> str | list[Any]:
        """Accepts a string of code or a list of code lines"""
        ...
    


