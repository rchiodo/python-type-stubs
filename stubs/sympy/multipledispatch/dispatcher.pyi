from inspect import Parameter
from itertools import islice
from typing import Any, Callable, Generator, LiteralString, Self, ValuesView


class MDNotImplementedError(NotImplementedError):
    ...


def ambiguity_warn(dispatcher, ambiguities) -> None:
    ...

class RaiseNotImplementedError:
    def __init__(self, dispatcher) -> None:
        ...
    
    def __call__(self, *args, **kwargs):
        ...
    


def ambiguity_register_error_ignore_dup(dispatcher, ambiguities) -> None:
    ...

_unresolved_dispatchers: set[Dispatcher] = ...
_resolve = ...
def halt_ordering() -> None:
    ...

def restart_ordering(on_ambiguity=...) -> None:
    ...

class Dispatcher:
    __slots__ = ...
    def __init__(self, name, doc=...) -> None:
        ...
    
    def register(self, *types, **kwargs) -> Callable[..., Any]:
        ...
    
    @classmethod
    def get_func_params(cls, func) -> ValuesView[Parameter] | None:
        ...
    
    @classmethod
    def get_func_annotations(cls, func) -> tuple[Any, ...] | None:
        ...
    
    def add(self, signature, func, on_ambiguity=...) -> None:
        ...
    
    def reorder(self, on_ambiguity=...) -> None:
        ...
    
    def __call__(self, *args, **kwargs):
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def dispatch(self, *types) -> None:
        ...
    
    def dispatch_iter(self, *types) -> Generator[Any, Any, None]:
        ...
    
    def resolve(self, types) -> None:
        ...
    
    def __getstate__(self) -> dict[str, Any]:
        ...
    
    def __setstate__(self, d) -> None:
        ...
    
    @property
    def __doc__(self) -> str:
        ...
    
    def help(self, *args, **kwargs) -> None:
        ...
    
    def source(self, *args, **kwargs) -> None:
        ...
    


def source(func) -> str:
    ...

class MethodDispatcher(Dispatcher):
    @classmethod
    def get_func_params(cls, func) -> islice[Parameter] | None:
        ...
    
    def __get__(self, instance, owner) -> Self:
        ...
    
    def __call__(self, *args, **kwargs):
        ...
    


def str_signature(sig) -> LiteralString:
    ...

def warning_text(name, amb):
    ...

