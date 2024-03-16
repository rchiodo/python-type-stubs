import sys
from typing import Any, Literal

_small_trailing = ...
def bit_scan1(x, n=...) -> None:
    ...

def bit_scan0(x, n=...) -> None:
    ...

def remove(x, f) -> tuple[Literal[0], Literal[0]] | tuple[Any, Any | None] | tuple[Any, int]:
    ...

def factorial(x) -> int:
    """Return x!."""
    ...

def sqrt(x) -> int:
    """Integer square root of x."""
    ...

def sqrtrem(x) -> tuple[int, int]:
    """Integer square root of x and remainder."""
    ...

if sys.version_info[: 2] >= (3, 9):
    gcd = ...
    lcm = ...
else:
    def gcd(*args) -> int:
        """gcd of multiple integers."""
        ...
    
    def lcm(*args) -> int:
        """lcm of multiple integers."""
        ...
    
def gcdext(a, b) -> tuple[Literal[0], Literal[0], Literal[0]] | tuple[Any, Any, Any] | tuple[Any, Any | int, Any | int]:
    ...

def is_square(x) -> bool:
    """Return True if x is a square number."""
    ...

def invert(x, m):
    """Modular inverse of x modulo m.

    Returns y such that x*y == 1 mod m.

    Uses ``math.pow`` but reproduces the behaviour of ``gmpy2.invert``
    which raises ZeroDivisionError if no inverse exists.
    """
    ...

def legendre(x, y) -> Literal[0, 1, -1]:
    """Legendre symbol (x / y).

    Following the implementation of gmpy2,
    the error is raised only when y is an even number.
    """
    ...

def jacobi(x, y) -> int:
    """Jacobi symbol (x / y)."""
    ...

def kronecker(x, y) -> int:
    """Kronecker symbol (x / y)."""
    ...

def iroot(y, n) -> tuple[Any, Literal[True]] | tuple[int, bool] | tuple[Literal[1], Literal[False]] | tuple[Any | int, Any]:
    ...

def is_fermat_prp(n, a) -> Literal[False]:
    ...

def is_euler_prp(n, a) -> Literal[False]:
    ...

def is_strong_prp(n, a) -> bool:
    ...

def is_fibonacci_prp(n, p, q) -> Literal[False]:
    ...

def is_lucas_prp(n, p, q) -> bool:
    ...

def is_selfridge_prp(n) -> bool:
    ...

def is_strong_lucas_prp(n, p, q) -> bool:
    ...

def is_strong_selfridge_prp(n) -> bool:
    ...

def is_bpsw_prp(n) -> bool:
    ...

def is_strong_bpsw_prp(n) -> bool:
    ...

