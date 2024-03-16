from typing import Any
from sympy.core import Basic, Expr, Float
from sympy.printing.codeprinter import CodePrinter

"""
Mathematica code printer
"""
known_functions = ...
class MCodePrinter(CodePrinter):
    """A printer to convert Python expressions to
    strings of the Wolfram's Mathematica code
    """
    printmethod = ...
    language = ...
    _default_settings: dict[str, Any] = ...
    _number_symbols: set[tuple[Expr, Float]] = ...
    _not_supported: set[Basic] = ...
    def __init__(self, settings=...) -> None:
        """Register function mappings supplied by user"""
        ...
    
    _print_tuple = ...
    _print_Tuple = ...
    _print_MinMaxBase = ...


def mathematica_code(expr, **settings) -> str | tuple[set[tuple[Any, str]], set[Any], str]:
    r"""Converts an expr to a string of the Wolfram Mathematica code

    Examples
    ========

    >>> from sympy import mathematica_code as mcode, symbols, sin
    >>> x = symbols('x')
    >>> mcode(sin(x).series(x).removeO())
    '(1/120)*x^5 - 1/6*x^3 + x'
    """
    ...

