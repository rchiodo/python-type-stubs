
from typing import Any, Callable, Generator


def identity(x) -> Generator[Any, Any, None]:
    ...

def exhaust(brule) -> Callable[..., Generator[Any, Any, None]]:
    ...

def onaction(brule, fn) -> Callable[..., Generator[Any, Any, None]]:
    ...

def debug(brule, file=...) -> Callable[..., Generator[Any, Any, None]]:
    ...

def multiplex(*brules) -> Callable[..., Generator[Any, Any, None]]:
    ...

def condition(cond, brule) -> Callable[..., Generator[Any, Any, None]]:
    ...

def sfilter(pred, brule) -> Callable[..., Generator[Any, Any, None]]:
    ...

def notempty(brule) -> Callable[..., Generator[Any, Any, None]]:
    ...

def do_one(*brules) -> Callable[..., Generator[Any, Any, None]]:
    ...

def chain(*brules) -> Callable[..., Generator[Any, Any, None]]:
    ...

def yieldify(rl) -> Callable[..., Generator[Any, Any, None]]:
    ...

