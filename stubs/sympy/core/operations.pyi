from typing import Any, LiteralString, Self
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.series.order import Order

class AssocOp(Basic):
    """ Associative operations, can separate noncommutative and
    commutative parts.

    (a op b) op c == a op (b op c) == a op b op c.

    Base class for Add and Mul.

    This is an abstract base class, concrete derived classes must define
    the attribute `identity`.

    .. deprecated:: 1.7

       Using arguments that aren't subclasses of :class:`~.Expr` in core
       operators (:class:`~.Mul`, :class:`~.Add`, and :class:`~.Pow`) is
       deprecated. See :ref:`non-expr-args-deprecated` for details.

    Parameters
    ==========

    *args :
        Arguments which are operated

    evaluate : bool, optional
        Evaluate the operation. If not passed, refer to ``global_parameters.evaluate``.
    """
    __slots__: tuple[str, ...] = ...
    _args_type: type[Basic] | None = ...
    @cacheit
    def __new__(cls, *args, evaluate=..., _sympify=...) -> Order:
        ...
    
    @classmethod
    def flatten(cls, seq) -> tuple[list[Any], list[Any], None]:
        """Return seq so that none of the elements are of type `cls`. This is
        the vanilla routine that will be used if a class derived from AssocOp
        does not define its own flatten routine."""
        ...
    
    @classmethod
    def make_args(cls, expr) -> tuple[Basic, ...] | tuple[Any]:
        """
        Return a sequence of elements `args` such that cls(*args) == expr

        Examples
        ========

        >>> from sympy import Symbol, Mul, Add
        >>> x, y = map(Symbol, 'xy')

        >>> Mul.make_args(x*y)
        (x, y)
        >>> Add.make_args(x*y)
        (x*y,)
        >>> set(Add.make_args(x*y + y)) == set([y, x*y])
        True

        """
        ...
    
    def doit(self, **hints) -> Self:
        ...
    


class ShortCircuit(Exception):
    ...


class LatticeOp(AssocOp):
    """
    Join/meet operations of an algebraic lattice[1].

    Explanation
    ===========

    These binary operations are associative (op(op(a, b), c) = op(a, op(b, c))),
    commutative (op(a, b) = op(b, a)) and idempotent (op(a, a) = op(a) = a).
    Common examples are AND, OR, Union, Intersection, max or min. They have an
    identity element (op(identity, a) = a) and an absorbing element
    conventionally called zero (op(zero, a) = zero).

    This is an abstract base class, concrete derived classes must declare
    attributes zero and identity. All defining properties are then respected.

    Examples
    ========

    >>> from sympy import Integer
    >>> from sympy.core.operations import LatticeOp
    >>> class my_join(LatticeOp):
    ...     zero = Integer(0)
    ...     identity = Integer(1)
    >>> my_join(2, 3) == my_join(3, 2)
    True
    >>> my_join(2, my_join(3, 4)) == my_join(2, 3, 4)
    True
    >>> my_join(0, 1, 4, 2, 3, 4)
    0
    >>> my_join(1, 2)
    2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lattice_%28order%29
    """
    is_commutative = ...
    def __new__(cls, *args, **options) -> Self:
        ...
    
    @classmethod
    def make_args(cls, expr) -> frozenset[Any]:
        """
        Return a set of args such that cls(*arg_set) == expr.
        """
        ...
    


class AssocOpDispatcher:
    """
    Handler dispatcher for associative operators

    .. notes::
       This approach is experimental, and can be replaced or deleted in the future.
       See https://github.com/sympy/sympy/pull/19463.

    Explanation
    ===========

    If arguments of different types are passed, the classes which handle the operation for each type
    are collected. Then, a class which performs the operation is selected by recursive binary dispatching.
    Dispatching relation can be registered by ``register_handlerclass`` method.

    Priority registration is unordered. You cannot make ``A*B`` and ``B*A`` refer to
    different handler classes. All logic dealing with the order of arguments must be implemented
    in the handler class.

    Examples
    ========

    >>> from sympy import Add, Expr, Symbol
    >>> from sympy.core.add import add

    >>> class NewExpr(Expr):
    ...     @property
    ...     def _add_handler(self):
    ...         return NewAdd
    >>> class NewAdd(NewExpr, Add):
    ...     pass
    >>> add.register_handlerclass((Add, NewAdd), NewAdd)

    >>> a, b = Symbol('a'), NewExpr()
    >>> add(a, b) == NewAdd(a, b)
    True

    """
    def __init__(self, name, doc=...) -> None:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def register_handlerclass(self, classes, typ, on_ambiguity=...) -> None:
        """
        Register the handler class for two classes, in both straight and reversed order.

        Paramteters
        ===========

        classes : tuple of two types
            Classes who are compared with each other.

        typ:
            Class which is registered to represent *cls1* and *cls2*.
            Handler method of *self* must be implemented in this class.
        """
        ...
    
    @cacheit
    def __call__(self, *args, _sympify=..., **kwargs) -> Any:
        """
        Parameters
        ==========

        *args :
            Arguments which are operated
        """
        ...
    
    @cacheit
    def dispatch(self, handlers) -> type:
        """
        Select the handler class, and return its handler method.
        """
        ...
    
    @property
    def __doc__(self) -> str:
        ...
    


