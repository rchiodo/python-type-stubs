from sympy.printing.pretty.stringpict import prettyForm
from sympy.printing.printer import Printer, print_function

pprint_use_unicode = ...
pprint_try_use_unicode = ...
class PrettyPrinter(Printer):
    """Printer, which converts an expression into 2D ASCII-art figure."""
    printmethod = ...
    _default_settings = ...
    def __init__(self, settings=...) -> None:
        ...
    
    def emptyPrinter(self, expr) -> prettyForm:
        ...
    
    def doprint(self, expr):
        ...
    
    _print_RandomSymbol = ...
    _print_Infinity = ...
    _print_NegativeInfinity = ...
    _print_EmptySet = ...
    _print_Naturals = ...
    _print_Naturals0 = ...
    _print_Integers = ...
    _print_Rationals = ...
    _print_Complexes = ...
    _print_EmptySequence = ...
    _print_SeqPer = ...
    _print_SeqAdd = ...
    _print_SeqMul = ...
    def join(self, delimiter, args) -> prettyForm:
        ...
    
    _print_bell = ...


@print_function(PrettyPrinter)
def pretty(expr, **settings):
    """Returns a string containing the prettified form of expr.

    For information on keyword arguments see pretty_print function.

    """
    ...

def pretty_print(expr, **kwargs) -> None:
    """Prints expr in pretty form.

    pprint is just a shortcut for this function.

    Parameters
    ==========

    expr : expression
        The expression to print.

    wrap_line : bool, optional (default=True)
        Line wrapping enabled/disabled.

    num_columns : int or None, optional (default=None)
        Number of columns before line breaking (default to None which reads
        the terminal width), useful when using SymPy without terminal.

    use_unicode : bool or None, optional (default=None)
        Use unicode characters, such as the Greek letter pi instead of
        the string pi.

    full_prec : bool or string, optional (default="auto")
        Use full precision.

    order : bool or string, optional (default=None)
        Set to 'none' for long expressions if slow; default is None.

    use_unicode_sqrt_char : bool, optional (default=True)
        Use compact single-character square root symbol (when unambiguous).

    root_notation : bool, optional (default=True)
        Set to 'False' for printing exponents of the form 1/n in fractional form.
        By default exponent is printed in root form.

    mat_symbol_style : string, optional (default="plain")
        Set to "bold" for printing MatrixSymbols using a bold mathematical symbol face.
        By default the standard face is used.

    imaginary_unit : string, optional (default="i")
        Letter to use for imaginary unit when use_unicode is True.
        Can be "i" (default) or "j".
    """
    ...

pprint = ...
def pager_print(expr, **settings) -> None:
    """Prints expr using the pager, in pretty form.

    This invokes a pager command using pydoc. Lines are not wrapped
    automatically. This routine is meant to be used with a pager that allows
    sideways scrolling, like ``less -S``.

    Parameters are the same as for ``pretty_print``. If you wish to wrap lines,
    pass ``num_columns=None`` to auto-detect the width of the terminal.

    """
    ...

