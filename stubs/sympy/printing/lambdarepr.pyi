from typing import Any
from sympy.printing.pycode import MpmathPrinter, PythonCodePrinter

__all__ = ['PythonCodePrinter', 'MpmathPrinter', 'NumPyPrinter', 'LambdaPrinter', 'NumPyPrinter', 'IntervalPrinter', 'lambdarepr']
class LambdaPrinter(PythonCodePrinter):
    """
    This printer converts expressions into strings that can be used by
    lambdify.
    """
    printmethod = ...


class NumExprPrinter(LambdaPrinter):
    printmethod = ...
    _numexpr_functions = ...
    module = ...
    def blacklisted(self, expr):
        ...
    
    _print_ImmutableDenseMatrix = ...
    _print_Dict = ...
    def doprint(self, expr) -> str | tuple[set[tuple[Any, str]], set[Any], str]:
        ...
    


class IntervalPrinter(MpmathPrinter, LambdaPrinter):
    """Use ``lambda`` printer but print numbers as ``mpi`` intervals. """
    ...


def lambdarepr(expr, **settings) -> str | tuple[set[tuple[Any, str]], set[Any], str]:
    """
    Returns a string usable for lambdifying.
    """
    ...

