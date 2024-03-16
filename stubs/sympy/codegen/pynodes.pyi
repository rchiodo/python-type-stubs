from sympy.codegen.abstract_nodes import List as AbstractList
from sympy.codegen.ast import Token

class List(AbstractList):
    ...


class NumExprEvaluate(Token):
    """represents a call to :class:`numexpr`s :func:`evaluate`"""
    _fields = ...


