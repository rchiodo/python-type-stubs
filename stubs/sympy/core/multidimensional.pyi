
from functools import _Wrapped
from typing import Any, Callable


def apply_on_element(f, args, kwargs, n) -> list[list[Any] | Any]:
    ...

def iter_copy(structure) -> list[Any]:
    ...

def structure_copy(structure) -> list[Any]:
    ...

class vectorize:
    def __init__(self, *mdargs) -> None:
        ...

    def __call__(self, f: Any) -> _Wrapped[..., Any, ..., list[list[Any] | Any] | Any]:
        ...
    


