
from typing import Any


def rsolve_poly(coeffs, f, n, shift=..., **hints):
    ...

def rsolve_ratio(coeffs, f, n, **hints) -> tuple[Any, Any] | None:
    ...

def rsolve_hyper(coeffs, f, n, **hints):
    ...

def rsolve(f, y, init=...):
    ...

