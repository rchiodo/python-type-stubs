from typing import Any
from sympy.printing.printer import Printer, print_function

"""
A Printer for generating executable code.

The most important function here is srepr that returns a string so that the
relation eval(srepr(expr))=expr holds in an appropriate environment.
"""
class ReprPrinter(Printer):
    printmethod = ...
    _default_settings: dict[str, Any] = ...
    def reprify(self, args, sep):
        """
        Prints each item in `args` and joins them with `sep`.
        """
        ...
    
    def emptyPrinter(self, expr) -> str | LiteralString:
        """
        The fallback printer.
        """
        ...
    


@print_function(ReprPrinter)
def srepr(expr, **settings) -> str:
    """return expr in repr form"""
    ...

