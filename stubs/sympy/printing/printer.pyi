import inspect
from typing import Any, Type
from contextlib import contextmanager

"""Printing subsystem driver

SymPy's printing system works the following way: Any expression can be
passed to a designated Printer who then is responsible to return an
adequate representation of that expression.

**The basic concept is the following:**

1.  Let the object print itself if it knows how.
2.  Take the best fitting method defined in the printer.
3.  As fall-back use the emptyPrinter method for the printer.

Which Method is Responsible for Printing?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The whole printing process is started by calling ``.doprint(expr)`` on the printer
which you want to use. This method looks for an appropriate method which can
print the given expression in the given style that the printer defines.
While looking for the method, it follows these steps:

1.  **Let the object print itself if it knows how.**

    The printer looks for a specific method in every object. The name of that method
    depends on the specific printer and is defined under ``Printer.printmethod``.
    For example, StrPrinter calls ``_sympystr`` and LatexPrinter calls ``_latex``.
    Look at the documentation of the printer that you want to use.
    The name of the method is specified there.

    This was the original way of doing printing in sympy. Every class had
    its own latex, mathml, str and repr methods, but it turned out that it
    is hard to produce a high quality printer, if all the methods are spread
    out that far. Therefore all printing code was combined into the different
    printers, which works great for built-in SymPy objects, but not that
    good for user defined classes where it is inconvenient to patch the
    printers.

2.  **Take the best fitting method defined in the printer.**

    The printer loops through expr classes (class + its bases), and tries
    to dispatch the work to ``_print_<EXPR_CLASS>``

    e.g., suppose we have the following class hierarchy::

            Basic
            |
            Atom
            |
            Number
            |
        Rational

    then, for ``expr=Rational(...)``, the Printer will try
    to call printer methods in the order as shown in the figure below::

        p._print(expr)
        |
        |-- p._print_Rational(expr)
        |
        |-- p._print_Number(expr)
        |
        |-- p._print_Atom(expr)
        |
        `-- p._print_Basic(expr)

    if ``._print_Rational`` method exists in the printer, then it is called,
    and the result is returned back. Otherwise, the printer tries to call
    ``._print_Number`` and so on.

3.  **As a fall-back use the emptyPrinter method for the printer.**

    As fall-back ``self.emptyPrinter`` will be called with the expression. If
    not defined in the Printer subclass this will be the same as ``str(expr)``.

.. _printer_example:

Example of Custom Printer
^^^^^^^^^^^^^^^^^^^^^^^^^

In the example below, we have a printer which prints the derivative of a function
in a shorter form.

.. code-block:: python

    from sympy.core.symbol import Symbol
    from sympy.printing.latex import LatexPrinter, print_latex
    from sympy.core.function import UndefinedFunction, Function


    class MyLatexPrinter(LatexPrinter):
        \"\"\"Print derivative of a function of symbols in a shorter form.
        \"\"\"
        def _print_Derivative(self, expr):
            function, *vars = expr.args
            if not isinstance(type(function), UndefinedFunction) or \\
               not all(isinstance(i, Symbol) for i in vars):
                return super()._print_Derivative(expr)

            # If you want the printer to work correctly for nested
            # expressions then use self._print() instead of str() or latex().
            # See the example of nested modulo below in the custom printing
            # method section.
            return "{}_{{{}}}".format(
                self._print(Symbol(function.func.__name__)),
                            ''.join(self._print(i) for i in vars))


    def print_my_latex(expr):
        \"\"\" Most of the printers define their own wrappers for print().
        These wrappers usually take printer settings. Our printer does not have
        any settings.
        \"\"\"
        print(MyLatexPrinter().doprint(expr))


    y = Symbol("y")
    x = Symbol("x")
    f = Function("f")
    expr = f(x, y).diff(x, y)

    # Print the expression using the normal latex printer and our custom
    # printer.
    print_latex(expr)
    print_my_latex(expr)

The output of the code above is::

    \\frac{\\partial^{2}}{\\partial x\\partial y}  f{\\left(x,y \\right)}
    f_{xy}

.. _printer_method_example:

Example of Custom Printing Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the example below, the latex printing of the modulo operator is modified.
This is done by overriding the method ``_latex`` of ``Mod``.

>>> from sympy import Symbol, Mod, Integer, print_latex

>>> # Always use printer._print()
>>> class ModOp(Mod):
...     def _latex(self, printer):
...         a, b = [printer._print(i) for i in self.args]
...         return r"\\operatorname{Mod}{\\left(%s, %s\\right)}" % (a, b)

Comparing the output of our custom operator to the builtin one:

>>> x = Symbol('x')
>>> m = Symbol('m')
>>> print_latex(Mod(x, m))
x \\bmod m
>>> print_latex(ModOp(x, m))
\\operatorname{Mod}{\\left(x, m\\right)}

Common mistakes
~~~~~~~~~~~~~~~
It's important to always use ``self._print(obj)`` to print subcomponents of
an expression when customizing a printer. Mistakes include:

1.  Using ``self.doprint(obj)`` instead:

    >>> # This example does not work properly, as only the outermost call may use
    >>> # doprint.
    >>> class ModOpModeWrong(Mod):
    ...     def _latex(self, printer):
    ...         a, b = [printer.doprint(i) for i in self.args]
    ...         return r"\\operatorname{Mod}{\\left(%s, %s\\right)}" % (a, b)

    This fails when the ``mode`` argument is passed to the printer:

    >>> print_latex(ModOp(x, m), mode='inline')  # ok
    $\\operatorname{Mod}{\\left(x, m\\right)}$
    >>> print_latex(ModOpModeWrong(x, m), mode='inline')  # bad
    $\\operatorname{Mod}{\\left($x$, $m$\\right)}$

2.  Using ``str(obj)`` instead:

    >>> class ModOpNestedWrong(Mod):
    ...     def _latex(self, printer):
    ...         a, b = [str(i) for i in self.args]
    ...         return r"\\operatorname{Mod}{\\left(%s, %s\\right)}" % (a, b)

    This fails on nested objects:

    >>> # Nested modulo.
    >>> print_latex(ModOp(ModOp(x, m), Integer(7)))  # ok
    \\operatorname{Mod}{\\left(\\operatorname{Mod}{\\left(x, m\\right)}, 7\\right)}
    >>> print_latex(ModOpNestedWrong(ModOpNestedWrong(x, m), Integer(7)))  # bad
    \\operatorname{Mod}{\\left(ModOpNestedWrong(x, m), 7\\right)}

3.  Using ``LatexPrinter()._print(obj)`` instead.

    >>> from sympy.printing.latex import LatexPrinter
    >>> class ModOpSettingsWrong(Mod):
    ...     def _latex(self, printer):
    ...         a, b = [LatexPrinter()._print(i) for i in self.args]
    ...         return r"\\operatorname{Mod}{\\left(%s, %s\\right)}" % (a, b)

    This causes all the settings to be discarded in the subobjects. As an
    example, the ``full_prec`` setting which shows floats to full precision is
    ignored:

    >>> from sympy import Float
    >>> print_latex(ModOp(Float(1) * x, m), full_prec=True)  # ok
    \\operatorname{Mod}{\\left(1.00000000000000 x, m\\right)}
    >>> print_latex(ModOpSettingsWrong(Float(1) * x, m), full_prec=True)  # bad
    \\operatorname{Mod}{\\left(1.0 x, m\\right)}

"""
@contextmanager
def printer_context(printer, **kwargs) -> Generator[None, Any, None]:
    ...

class Printer:
    """ Generic printer

    Its job is to provide infrastructure for implementing new printers easily.

    If you want to define your custom Printer or your custom printing method
    for your custom class then see the example above: printer_example_ .
    """
    _global_settings: dict[str, Any] = ...
    _default_settings: dict[str, Any] = ...
    printmethod: str = ...
    def __init__(self, settings=...) -> None:
        ...
    
    @classmethod
    def set_global_settings(cls, **settings) -> None:
        """Set system-wide printing settings. """
        ...
    
    @property
    def order(self) -> Any:
        ...
    
    def doprint(self, expr) -> str:
        """Returns printer's representation for expr (as a string)"""
        ...
    
    def emptyPrinter(self, expr) -> str:
        ...
    


class _PrintFunction:
    """
    Function wrapper to replace ``**settings`` in the signature with printer defaults
    """
    def __init__(self, f, print_cls: Type[Printer]) -> None:
        ...
    
    def __reduce__(self):
        ...
    
    def __call__(self, *args, **kwargs):
        ...
    
    @property
    def __signature__(self) -> inspect.Signature:
        ...
    


def print_function(print_cls) -> Callable[..., _PrintFunction]:
    """ A decorator to replace kwargs with the printer settings in __signature__ """
    ...

