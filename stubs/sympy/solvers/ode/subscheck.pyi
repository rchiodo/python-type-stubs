from typing import Any, Literal


def sub_func_doit(eq, func, new):
    ...

def checkodesol(ode, sol, func=..., order=..., solve_for_func=...):
    ...

def checksysodesol(eqs, sols, func=...) -> tuple[Literal[True], list[Any]] | tuple[Literal[False], list[Any]]:
    ...

