from functools import _Wrapped
from typing import Any, Callable


def recurrence_memo(initial) -> Callable[..., _Wrapped[..., Any, ..., Any]]:
    ...

def assoc_recurrence_memo(base_seq) -> Callable[..., _Wrapped[..., Any, ..., Any]]:
    ...

