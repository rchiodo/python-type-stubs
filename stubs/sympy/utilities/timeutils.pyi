
from typing import Any, Callable


_scales = ...
_units = ...
def timed(func, setup=..., limit=...) -> tuple[int, float, float, str]:
    ...

_do_timings = ...
_timestack = ...
def timethis(name) -> Callable[..., Any | Callable[..., Any]]:
    ...

