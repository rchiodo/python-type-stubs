
from typing import Any, Callable


def rm_id(isid, new=...) -> Callable[..., Any]:
    ...

def glom(key, count, combine) -> Callable[..., Any]:
    ...

def sort(key, new=...) -> Callable[..., Any]:
    ...

def distribute(A, B) -> Callable[..., Any]:
    ...

def subs(a, b) -> Callable[..., Any]:
    ...

def unpack(expr):
    ...

def flatten(expr, new=...):
    ...

def rebuild(expr):
    ...

