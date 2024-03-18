from typing import Any, Callable, Generator


def treeapply(tree, join, leaf=...):
    ...

def greedy(tree, objective=..., **kwargs):
    ...

def allresults(tree, leaf=...) -> Callable[..., Generator[Any, Any, None]]:
    ...

def brute(tree, objective=..., **kwargs) -> Callable[..., Any]:
    ...

