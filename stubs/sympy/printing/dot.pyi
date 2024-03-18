__all__ = ['dotprint']
from typing import Any


default_styles = ...
slotClasses = ...
def purestr(x, with_args=...) -> tuple[str | Any, tuple[()] | tuple[Any, ...]] | str:
    ...

def styleof(expr, styles=...) -> dict[Any, Any]:
    ...

def attrprint(d, delimiter=...) -> str:
    ...

def dotnode(expr, styles=..., labelfunc=..., pos=..., repeat=...) -> str:
    ...

def dotedges(expr, atom=..., pos=..., repeat=...) -> list[Any] | list[str]:
    ...

template = ...
_graphstyle = ...
def dotprint(expr, styles=..., atom=..., maxdepth=..., repeat=..., labelfunc=..., **kwargs) -> str:
    ...

