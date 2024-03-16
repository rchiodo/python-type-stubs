from contextlib import contextmanager
from typing import Any, Callable, Generator, Self
from sympy.core.basic import Basic
from sympy.logic.boolalg import Boolean

"""A module which implements predicates and assumption context."""
class AssumptionsContext(set):
    """
    Set containing default assumptions which are applied to the ``ask()``
    function.

    Explanation
    ===========

    This is used to represent global assumptions, but you can also use this
    class to create your own local assumptions contexts. It is basically a thin
    wrapper to Python's set, so see its documentation for advanced usage.

    Examples
    ========

    The default assumption context is ``global_assumptions``, which is initially empty:

    >>> from sympy import ask, Q
    >>> from sympy.assumptions import global_assumptions
    >>> global_assumptions
    AssumptionsContext()

    You can add default assumptions:

    >>> from sympy.abc import x
    >>> global_assumptions.add(Q.real(x))
    >>> global_assumptions
    AssumptionsContext({Q.real(x)})
    >>> ask(Q.real(x))
    True

    And remove them:

    >>> global_assumptions.remove(Q.real(x))
    >>> print(ask(Q.real(x)))
    None

    The ``clear()`` method removes every assumption:

    >>> global_assumptions.add(Q.positive(x))
    >>> global_assumptions
    AssumptionsContext({Q.positive(x)})
    >>> global_assumptions.clear()
    >>> global_assumptions
    AssumptionsContext()

    See Also
    ========

    assuming

    """
    def add(self, *assumptions) -> None:
        """Add assumptions."""
        ...
    


global_assumptions = ...
class AppliedPredicate(Boolean):
    """
    The class of expressions resulting from applying ``Predicate`` to
    the arguments. ``AppliedPredicate`` merely wraps its argument and
    remain unevaluated. To evaluate it, use the ``ask()`` function.

    Examples
    ========

    >>> from sympy import Q, ask
    >>> Q.integer(1)
    Q.integer(1)

    The ``function`` attribute returns the predicate, and the ``arguments``
    attribute returns the tuple of arguments.

    >>> type(Q.integer(1))
    <class 'sympy.assumptions.assume.AppliedPredicate'>
    >>> Q.integer(1).function
    Q.integer
    >>> Q.integer(1).arguments
    (1,)

    Applied predicates can be evaluated to a boolean value with ``ask``:

    >>> ask(Q.integer(1))
    True

    """
    __slots__ = ...
    def __new__(cls, predicate, *args) -> Self:
        ...
    
    @property
    def arg(self) -> Basic:
        """
        Return the expression used by this assumption.

        Examples
        ========

        >>> from sympy import Q, Symbol
        >>> x = Symbol('x')
        >>> a = Q.integer(x + 1)
        >>> a.arg
        x + 1

        """
        ...
    
    @property
    def function(self) -> Basic:
        """
        Return the predicate.
        """
        ...
    
    @property
    def arguments(self) -> tuple[Basic, ...]:
        """
        Return the arguments which are applied to the predicate.
        """
        ...
    
    @property
    def binary_symbols(self) -> set[Basic] | set[Any]:
        ...
    


class PredicateMeta(type):
    def __new__(cls, clsname, bases, dct) -> type:
        ...
    
    @property
    def __doc__(cls):
        ...
    


class Predicate(Boolean, metaclass=PredicateMeta):
    """
    Base class for mathematical predicates. It also serves as a
    constructor for undefined predicate objects.

    Explanation
    ===========

    Predicate is a function that returns a boolean value [1].

    Predicate function is object, and it is instance of predicate class.
    When a predicate is applied to arguments, ``AppliedPredicate``
    instance is returned. This merely wraps the argument and remain
    unevaluated. To obtain the truth value of applied predicate, use the
    function ``ask``.

    Evaluation of predicate is done by multiple dispatching. You can
    register new handler to the predicate to support new types.

    Every predicate in SymPy can be accessed via the property of ``Q``.
    For example, ``Q.even`` returns the predicate which checks if the
    argument is even number.

    To define a predicate which can be evaluated, you must subclass this
    class, make an instance of it, and register it to ``Q``. After then,
    dispatch the handler by argument types.

    If you directly construct predicate using this class, you will get
    ``UndefinedPredicate`` which cannot be dispatched. This is useful
    when you are building boolean expressions which do not need to be
    evaluated.

    Examples
    ========

    Applying and evaluating to boolean value:

    >>> from sympy import Q, ask
    >>> ask(Q.prime(7))
    True

    You can define a new predicate by subclassing and dispatching. Here,
    we define a predicate for sexy primes [2] as an example.

    >>> from sympy import Predicate, Integer
    >>> class SexyPrimePredicate(Predicate):
    ...     name = "sexyprime"
    >>> Q.sexyprime = SexyPrimePredicate()
    >>> @Q.sexyprime.register(Integer, Integer)
    ... def _(int1, int2, assumptions):
    ...     args = sorted([int1, int2])
    ...     if not all(ask(Q.prime(a), assumptions) for a in args):
    ...         return False
    ...     return args[1] - args[0] == 6
    >>> ask(Q.sexyprime(5, 11))
    True

    Direct constructing returns ``UndefinedPredicate``, which can be
    applied but cannot be dispatched.

    >>> from sympy import Predicate, Integer
    >>> Q.P = Predicate("P")
    >>> type(Q.P)
    <class 'sympy.assumptions.assume.UndefinedPredicate'>
    >>> Q.P(1)
    Q.P(1)
    >>> Q.P.register(Integer)(lambda expr, assump: True)
    Traceback (most recent call last):
      ...
    TypeError: <class 'sympy.assumptions.assume.UndefinedPredicate'> cannot be dispatched.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Predicate_%28mathematical_logic%29
    .. [2] https://en.wikipedia.org/wiki/Sexy_prime

    """
    is_Atom = ...
    def __new__(cls, *args, **kwargs) -> UndefinedPredicate | Self:
        ...
    
    @property
    def name(self) -> str:
        ...
    
    @classmethod
    def register(cls, *types, **kwargs):
        """
        Register the signature to the handler.
        """
        ...
    
    @classmethod
    def register_many(cls, *types, **kwargs) -> Callable[..., None]:
        """
        Register multiple signatures to same handler.
        """
        ...
    
    def __call__(self, *args) -> AppliedPredicate:
        ...
    
    def eval(self, args, assumptions=...) -> None:
        """
        Evaluate ``self(*args)`` under the given assumptions.

        This uses only direct resolution methods, not logical inference.
        """
        ...
    


class UndefinedPredicate(Predicate):
    """
    Predicate without handler.

    Explanation
    ===========

    This predicate is generated by using ``Predicate`` directly for
    construction. It does not have a handler, and evaluating this with
    arguments is done by SAT solver.

    Examples
    ========

    >>> from sympy import Predicate, Q
    >>> Q.P = Predicate('P')
    >>> Q.P.func
    <class 'sympy.assumptions.assume.UndefinedPredicate'>
    >>> Q.P.name
    Str('P')

    """
    handler = ...
    def __new__(cls, name, handlers=...) -> Self:
        ...
    
    @property
    def name(self) -> Basic:
        ...
    
    def __getnewargs__(self) -> tuple[Basic]:
        ...
    
    def __call__(self, expr) -> AppliedPredicate:
        ...
    
    def add_handler(self, handler) -> None:
        ...
    
    def remove_handler(self, handler) -> None:
        ...
    
    def eval(self, args, assumptions=...) -> Any | None:
        ...
    


@contextmanager
def assuming(*assumptions) -> Generator[None, Any, None]:
    """
    Context manager for assumptions.

    Examples
    ========

    >>> from sympy import assuming, Q, ask
    >>> from sympy.abc import x, y
    >>> print(ask(Q.integer(x + y)))
    None
    >>> with assuming(Q.integer(x), Q.integer(y)):
    ...     print(ask(Q.integer(x + y)))
    True
    """
    ...

