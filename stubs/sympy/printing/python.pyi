from sympy.printing.repr import ReprPrinter
from sympy.printing.str import StrPrinter

STRPRINT = ...
class PythonPrinter(ReprPrinter, StrPrinter):
    """A printer which converts an expression into its Python interpretation."""
    def __init__(self, settings=...) -> None:
        ...
    


def python(expr, **settings) -> str:
    """Return Python interpretation of passed expression
    (can be passed to the exec() function without any modifications)"""
    ...

def print_python(expr, **settings) -> None:
    """Print output of python() function"""
    ...

