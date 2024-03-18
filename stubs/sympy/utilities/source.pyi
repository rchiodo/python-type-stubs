"""
This module adds several functions for interactive source code inspection.
"""
from typing import Any, Literal


def get_class(lookup_view) -> Any | str:
    """
    Convert a string version of a class name to the object.

    For example, get_class('sympy.core.Basic') will return
    class Basic located in module sympy.core
    """
    ...

def get_mod_func(callback) -> tuple[Any, Literal['']] | tuple[Any, Any]:
    """
    splits the string path to a class into a string path to the module
    and the name of the class.

    Examples
    ========

    >>> from sympy.utilities.source import get_mod_func
    >>> get_mod_func('sympy.core.basic.Basic')
    ('sympy.core.basic', 'Basic')

    """
    ...

