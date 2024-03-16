def is_valid(x) -> bool:
    """Check if a floating point number is valid"""
    ...

def rescale(y, W, H, mi, ma) -> list[Any]:
    """Rescale the given array `y` to fit into the integer values
    between `0` and `H-1` for the values between ``mi`` and ``ma``.
    """
    ...

def linspace(start, stop, num) -> list[Any]:
    ...

def textplot_str(expr, a, b, W=..., H=...) -> Generator[str, Any, None]:
    """Generator for the lines of the plot"""
    ...

def textplot(expr, a, b, W=..., H=...) -> None:
    r"""
    Print a crude ASCII art plot of the SymPy expression 'expr' (which
    should contain a single symbol, e.g. x or something else) over the
    interval [a, b].

    Examples
    ========

    >>> from sympy import Symbol, sin
    >>> from sympy.plotting import textplot
    >>> t = Symbol('t')
    >>> textplot(sin(t)*t, 0, 15)
     14 |                                                  ...
        |                                                     .
        |                                                 .
        |                                                      .
        |                                                .
        |                            ...
        |                           /   .               .
        |                          /
        |                         /      .
        |                        .        .            .
    1.5 |----.......--------------------------------------------
        |....       \           .          .
        |            \         /                      .
        |             ..      /             .
        |               \    /                       .
        |                ....
        |                                    .
        |                                     .     .
        |
        |                                      .   .
    -11 |_______________________________________________________
         0                          7.5                        15
    """
    ...

