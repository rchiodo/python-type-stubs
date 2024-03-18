from functools import _Wrapped
from typing import Any, Callable


def recurrence_memo(initial) -> Callable[..., _Wrapped[..., Any, ..., Any]]:
    """
    Memo decorator for sequences defined by recurrence

    Examples
    ========

    >>> from sympy.utilities.memoization import recurrence_memo
    >>> @recurrence_memo([1]) # 0! = 1
    ... def factorial(n, prev):
    ...     return n * prev[-1]
    >>> factorial(4)
    24
    >>> factorial(3) # use cache values
    6
    >>> factorial.cache_length() # cache length can be obtained
    5
    >>> factorial.fetch_item(slice(2, 4))
    [2, 6]

    """
    ...

def assoc_recurrence_memo(base_seq) -> Callable[..., _Wrapped[..., Any, ..., Any]]:
    """
    Memo decorator for associated sequences defined by recurrence starting from base

    base_seq(n) -- callable to get base sequence elements

    XXX works only for Pn0 = base_seq(0) cases
    XXX works only for m <= n cases
    """
    ...

