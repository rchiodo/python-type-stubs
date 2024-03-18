from inspect import Parameter
from itertools import islice
from typing import Any, Callable, Generator, LiteralString, Self, ValuesView


class MDNotImplementedError(NotImplementedError):
    """ A NotImplementedError for multiple dispatch """
    ...


def ambiguity_warn(dispatcher, ambiguities) -> None:
    """ Raise warning when ambiguity is detected

    Parameters
    ----------
    dispatcher : Dispatcher
        The dispatcher on which the ambiguity was detected
    ambiguities : set
        Set of type signature pairs that are ambiguous within this dispatcher

    See Also:
        Dispatcher.add
        warning_text
    """
    ...

class RaiseNotImplementedError:
    """Raise ``NotImplementedError`` when called."""
    def __init__(self, dispatcher) -> None:
        ...
    
    def __call__(self, *args, **kwargs):
        ...
    


def ambiguity_register_error_ignore_dup(dispatcher, ambiguities) -> None:
    """
    If super signature for ambiguous types is duplicate types, ignore it.
    Else, register instance of ``RaiseNotImplementedError`` for ambiguous types.

    Parameters
    ----------
    dispatcher : Dispatcher
        The dispatcher on which the ambiguity was detected
    ambiguities : set
        Set of type signature pairs that are ambiguous within this dispatcher

    See Also:
        Dispatcher.add
        ambiguity_warn
    """
    ...

_unresolved_dispatchers: set[Dispatcher] = ...
_resolve = ...
def halt_ordering() -> None:
    ...

def restart_ordering(on_ambiguity=...) -> None:
    ...

class Dispatcher:
    """ Dispatch methods based on type signature

    Use ``dispatch`` to add implementations

    Examples
    --------

    >>> from sympy.multipledispatch import dispatch
    >>> @dispatch(int)
    ... def f(x):
    ...     return x + 1

    >>> @dispatch(float)
    ... def f(x) noqa: F811
    ...     return x - 1

    >>> f(3)
    4
    >>> f(3.0)
    2.0
    """
    __slots__ = ...
    def __init__(self, name, doc=...) -> None:
        ...
    
    def register(self, *types, **kwargs) -> Callable[..., Any]:
        """ Register dispatcher with new implementation

        >>> from sympy.multipledispatch.dispatcher import Dispatcher
        >>> f = Dispatcher('f')
        >>> @f.register(int)
        ... def inc(x):
        ...     return x + 1

        >>> @f.register(float)
        ... def dec(x):
        ...     return x - 1

        >>> @f.register(list)
        ... @f.register(tuple)
        ... def reverse(x):
        ...     return x[::-1]

        >>> f(1)
        2

        >>> f(1.0)
        0.0

        >>> f([1, 2, 3])
        [3, 2, 1]
        """
        ...
    
    @classmethod
    def get_func_params(cls, func) -> ValuesView[Parameter] | None:
        ...
    
    @classmethod
    def get_func_annotations(cls, func) -> tuple[Any, ...] | None:
        """ Get annotations of function positional parameters
        """
        ...
    
    def add(self, signature, func, on_ambiguity=...) -> None:
        """ Add new types/method pair to dispatcher

        >>> from sympy.multipledispatch import Dispatcher
        >>> D = Dispatcher('add')
        >>> D.add((int, int), lambda x, y: x + y)
        >>> D.add((float, float), lambda x, y: x + y)

        >>> D(1, 2)
        3
        >>> D(1, 2.0)
        Traceback (most recent call last):
        ...
        NotImplementedError: Could not find signature for add: <int, float>

        When ``add`` detects a warning it calls the ``on_ambiguity`` callback
        with a dispatcher/itself, and a set of ambiguous type signature pairs
        as inputs.  See ``ambiguity_warn`` for an example.
        """
        ...
    
    def reorder(self, on_ambiguity=...) -> None:
        ...
    
    def __call__(self, *args, **kwargs):
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def dispatch(self, *types) -> None:
        """ Deterimine appropriate implementation for this type signature

        This method is internal.  Users should call this object as a function.
        Implementation resolution occurs within the ``__call__`` method.

        >>> from sympy.multipledispatch import dispatch
        >>> @dispatch(int)
        ... def inc(x):
        ...     return x + 1

        >>> implementation = inc.dispatch(int)
        >>> implementation(3)
        4

        >>> print(inc.dispatch(float))
        None

        See Also:
            ``sympy.multipledispatch.conflict`` - module to determine resolution order
        """
        ...
    
    def dispatch_iter(self, *types) -> Generator[Any, Any, None]:
        ...
    
    def resolve(self, types) -> None:
        """ Deterimine appropriate implementation for this type signature

        .. deprecated:: 0.4.4
            Use ``dispatch(*types)`` instead
        """
        ...
    
    def __getstate__(self) -> dict[str, Any]:
        ...
    
    def __setstate__(self, d) -> None:
        ...
    
    @property
    def __doc__(self) -> str:
        ...
    
    def help(self, *args, **kwargs) -> None:
        """ Print docstring for the function corresponding to inputs """
        ...
    
    def source(self, *args, **kwargs) -> None:
        """ Print source code for the function corresponding to inputs """
        ...
    


def source(func) -> str:
    ...

class MethodDispatcher(Dispatcher):
    """ Dispatch methods based on type signature

    See Also:
        Dispatcher
    """
    @classmethod
    def get_func_params(cls, func) -> islice[Parameter] | None:
        ...
    
    def __get__(self, instance, owner) -> Self:
        ...
    
    def __call__(self, *args, **kwargs):
        ...
    


def str_signature(sig) -> LiteralString:
    """ String representation of type signature

    >>> from sympy.multipledispatch.dispatcher import str_signature
    >>> str_signature((int, float))
    'int, float'
    """
    ...

def warning_text(name, amb):
    """ The text for ambiguity warnings """
    ...

