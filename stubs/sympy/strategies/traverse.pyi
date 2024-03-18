"""Strategies to Traverse a Tree."""
from typing import Any, Callable


def top_down(rule, fns=...) -> Callable[[Any], Any]:
    """Apply a rule down a tree running it on the top nodes first."""
    ...

def bottom_up(rule, fns=...) -> Callable[[Any], Any]:
    """Apply a rule down a tree running it on the bottom nodes first."""
    ...

def top_down_once(rule, fns=...) -> Callable[[Any], Any]:
    """Apply a rule down a tree - stop on success."""
    ...

def bottom_up_once(rule, fns=...) -> Callable[[Any], Any]:
    """Apply a rule up a tree - stop on success."""
    ...

def sall(rule, fns=...) -> Callable[..., Any]:
    """Strategic all - apply rule to args."""
    ...

