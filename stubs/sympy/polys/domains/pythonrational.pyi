"""
Rational number type based on Python integers.

The PythonRational class from here has been moved to
sympy.external.pythonmpq

This module is just left here for backwards compatibility.
"""
from sympy.core.numbers import Integer, Rational


PythonRational = ...
def sympify_pythonrational(arg) -> Rational | Integer:
    ...

