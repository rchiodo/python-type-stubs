from contextlib import contextmanager
from threading import local
from typing import Any, Generator

"""Thread-safe global parameters"""
class _global_parameters(local):
    """
    Thread-local global parameters.

    Explanation
    ===========

    This class generates thread-local container for SymPy's global parameters.
    Every global parameters must be passed as keyword argument when generating
    its instance.
    A variable, `global_parameters` is provided as default instance for this class.

    WARNING! Although the global parameters are thread-local, SymPy's cache is not
    by now.
    This may lead to undesired result in multi-threading operations.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.core.cache import clear_cache
    >>> from sympy.core.parameters import global_parameters as gp

    >>> gp.evaluate
    True
    >>> x+x
    2*x

    >>> log = []
    >>> def f():
    ...     clear_cache()
    ...     gp.evaluate = False
    ...     log.append(x+x)
    ...     clear_cache()
    >>> import threading
    >>> thread = threading.Thread(target=f)
    >>> thread.start()
    >>> thread.join()

    >>> print(log)
    [x + x]

    >>> gp.evaluate
    True
    >>> x+x
    2*x

    References
    ==========

    .. [1] https://docs.python.org/3/library/threading.html

    """
    def __init__(self, **kwargs) -> None:
        ...
    
    def __setattr__(self, name, value) -> None:
        ...
    


global_parameters = ...
class evaluate:
    """ Control automatic evaluation

    Explanation
    ===========

    This context manager controls whether or not all SymPy functions evaluate
    by default.

    Note that much of SymPy expects evaluated expressions.  This functionality
    is experimental and is unlikely to function as intended on large
    expressions.

    Examples
    ========

    >>> from sympy import evaluate
    >>> from sympy.abc import x
    >>> print(x + x)
    2*x
    >>> with evaluate(False):
    ...     print(x + x)
    x + x
    """
    def __init__(self, x) -> None:
        ...
    
    def __enter__(self) -> None:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...
    


@contextmanager
def distribute(x) -> Generator[None, Any, None]:
    """ Control automatic distribution of Number over Add

    Explanation
    ===========

    This context manager controls whether or not Mul distribute Number over
    Add. Plan is to avoid distributing Number over Add in all of sympy. Once
    that is done, this contextmanager will be removed.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.core.parameters import distribute
    >>> print(2*(x + 1))
    2*x + 2
    >>> with distribute(False):
    ...     print(2*(x + 1))
    2*(x + 1)
    """
    ...

