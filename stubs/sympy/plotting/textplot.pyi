from typing import Any, Generator


def is_valid(x) -> bool:
    ...

def rescale(y, W, H, mi, ma) -> list[Any]:
    ...

def linspace(start, stop, num) -> list[Any]:
    ...

def textplot_str(expr, a, b, W=..., H=...) -> Generator[str, Any, None]:
    ...

def textplot(expr, a, b, W=..., H=...) -> None:
    ...

