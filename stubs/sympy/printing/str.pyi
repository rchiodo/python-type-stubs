from typing import Any
from sympy.printing.printer import Printer, print_function

"""
A Printer for generating readable representation of most SymPy classes.
"""
class StrPrinter(Printer):
    printmethod = ...
    _default_settings: dict[str, Any] = ...
    _relationals: dict[str, str] = ...
    def parenthesize(self, item, level, strict=...) -> str:
        ...
    
    def stringify(self, args, sep, level=...):
        ...
    
    def emptyPrinter(self, expr) -> str:
        ...
    
    _print_MatrixSymbol = ...
    _print_RandomSymbol = ...


@print_function(StrPrinter)
def sstr(expr, **settings) -> str:
    """Returns the expression as a string.

    For large expressions where speed is a concern, use the setting
    order='none'. If abbrev=True setting is used then units are printed in
    abbreviated form.

    Examples
    ========

    >>> from sympy import symbols, Eq, sstr
    >>> a, b = symbols('a b')
    >>> sstr(Eq(a + b, 0))
    'Eq(a + b, 0)'
    """
    ...

class StrReprPrinter(StrPrinter):
    """(internal) -- see sstrrepr"""
    ...


@print_function(StrReprPrinter)
def sstrrepr(expr, **settings) -> str:
    """return expr in mixed str/repr form

       i.e. strings are returned in repr form with quotes, and everything else
       is returned in str form.

       This function could be useful for hooking into sys.displayhook
    """
    ...

