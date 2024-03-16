from typing import Self
from sympy.codegen.ast import FunctionCall, Node, String, Token
from sympy.core.basic import Basic

"""
AST nodes specific to the C family of languages
"""
void = ...
restrict = ...
volatile = ...
static = ...
def alignof(arg) -> FunctionCall:
    """ Generate of FunctionCall instance for calling 'alignof' """
    ...

def sizeof(arg) -> FunctionCall:
    """ Generate of FunctionCall instance for calling 'sizeof'

    Examples
    ========

    >>> from sympy.codegen.ast import real
    >>> from sympy.codegen.cnodes import sizeof
    >>> from sympy import ccode
    >>> ccode(sizeof(real))
    'sizeof(double)'
    """
    ...

class CommaOperator(Basic):
    """ Represents the comma operator in C """
    def __new__(cls, *args) -> Self:
        ...
    


class Label(Node):
    """ Label for use with e.g. goto statement.

    Examples
    ========

    >>> from sympy import ccode, Symbol
    >>> from sympy.codegen.cnodes import Label, PreIncrement
    >>> print(ccode(Label('foo')))
    foo:
    >>> print(ccode(Label('bar', [PreIncrement(Symbol('a'))])))
    bar:
    ++(a);

    """
    _fields = ...
    defaults = ...
    _construct_name = String


class goto(Token):
    """ Represents goto in C """
    _fields = ...
    _construct_label = Label


class PreDecrement(Basic):
    """ Represents the pre-decrement operator

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cnodes import PreDecrement
    >>> from sympy import ccode
    >>> ccode(PreDecrement(x))
    '--(x)'

    """
    nargs = ...


class PostDecrement(Basic):
    """ Represents the post-decrement operator

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cnodes import PostDecrement
    >>> from sympy import ccode
    >>> ccode(PostDecrement(x))
    '(x)--'

    """
    nargs = ...


class PreIncrement(Basic):
    """ Represents the pre-increment operator

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cnodes import PreIncrement
    >>> from sympy import ccode
    >>> ccode(PreIncrement(x))
    '++(x)'

    """
    nargs = ...


class PostIncrement(Basic):
    """ Represents the post-increment operator

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cnodes import PostIncrement
    >>> from sympy import ccode
    >>> ccode(PostIncrement(x))
    '(x)++'

    """
    nargs = ...


class struct(Node):
    """ Represents a struct in C """
    _fields = ...
    defaults = ...
    _construct_name = String


class union(struct):
    """ Represents a union in C """
    __slots__ = ...


