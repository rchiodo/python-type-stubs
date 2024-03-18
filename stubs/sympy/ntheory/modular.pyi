from typing import Any


def symmetric_residue(a, m):
    ...

def crt(m, v, symmetric=..., check=...) -> tuple[int, int] | None:
    ...

def crt1(m) -> tuple[float, list[Any], list[Any]]:
    ...

def crt2(m, v, mm, e, s, symmetric=...) -> tuple[int, int]:
    ...

def solve_congruence(*remainder_modulus_pairs, **hint) -> tuple[Any, Any | int] | None:
    ...

