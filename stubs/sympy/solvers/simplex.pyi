
from typing import Any


class UnboundedLPError(Exception):
    ...


class InfeasibleLPError(Exception):
    ...


def lpmin(f, constr) -> tuple[Any, dict[Any, None]]:
    ...

def lpmax(f, constr) -> tuple[Any, dict[Any, None]]:
    ...

def linprog(c, A=..., b=..., A_eq=..., b_eq=..., bounds=...) -> tuple[Any, Any | list[None]]:
    ...

def show_linprog(c, A=..., b=..., A_eq=..., b_eq=..., bounds=...) -> tuple[Any, list[Any]]:
    ...

