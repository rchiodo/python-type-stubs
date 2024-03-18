from typing import Any, Self, Tuple as tTuple
from sympy.core.function import Function, UndefinedFunction
from sympy.core.numbers import Float, Integer, Rational
from sympy.series.order import Order

_sym = ...
class carmichael(Function):
    @staticmethod
    def is_perfect_square(n) -> bool:
        ...
    
    @staticmethod
    def divides(p, n):
        ...
    
    @staticmethod
    def is_prime(n) -> bool:
        ...
    
    @staticmethod
    def is_carmichael(n) -> bool:
        ...
    
    @staticmethod
    def find_carmichael_numbers_in_range(x, y) -> list[int]:
        ...
    
    @staticmethod
    def find_first_n_carmichaels(n) -> list[Any]:
        ...
    


class fibonacci(Function):
    @classmethod
    def eval(cls, n, sym=...) -> Integer | None:
        ...
    


class lucas(Function):
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class tribonacci(Function):
    @classmethod
    def eval(cls, n, sym=...) -> Integer | None:
        ...
    


class bernoulli(Function):
    args: tTuple[Integer]
    _cache = ...
    _highest = ...
    @classmethod
    def eval(cls, n, x=...) -> Self | Rational | Integer | Float | Any | None:
        ...
    


class bell(Function):
    @classmethod
    def eval(cls, n, k_sym=..., symbols=...) -> Integer | None:
        ...
    


class harmonic(Function):
    @classmethod
    def eval(cls, n, m=...) -> Self | type[UndefinedFunction] | Order | None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    


class euler(Function):
    @classmethod
    def eval(cls, n, x=...) -> Integer | Any | None:
        ...
    


class catalan(Function):
    @classmethod
    def eval(cls, n) -> Rational | Integer | None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    


class genocchi(Function):
    @classmethod
    def eval(cls, n, x=...) -> Self | Any | None:
        ...
    


class andre(Function):
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class partition(Function):
    is_integer = ...
    is_nonnegative = ...
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class divisor_sigma(Function):
    is_integer = ...
    is_positive = ...
    @classmethod
    def eval(cls, n, k=...) -> Order | None:
        ...
    


class udivisor_sigma(Function):
    is_integer = ...
    is_positive = ...
    @classmethod
    def eval(cls, n, k=...) -> Order | None:
        ...
    


class legendre_symbol(Function):
    is_integer = ...
    is_prime = ...
    @classmethod
    def eval(cls, a, p) -> None:
        ...
    


class jacobi_symbol(Function):
    is_integer = ...
    is_prime = ...
    @classmethod
    def eval(cls, m, n) -> None:
        ...
    


class kronecker_symbol(Function):
    is_integer = ...
    is_prime = ...
    @classmethod
    def eval(cls, a, n) -> None:
        ...
    


class mobius(Function):
    is_integer = ...
    is_prime = ...
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class primenu(Function):
    is_integer = ...
    is_nonnegative = ...
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class primeomega(Function):
    is_integer = ...
    is_nonnegative = ...
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class totient(Function):
    is_integer = ...
    is_positive = ...
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class reduced_totient(Function):
    is_integer = ...
    is_positive = ...
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class primepi(Function):
    is_integer = ...
    is_nonnegative = ...
    @classmethod
    def eval(cls, n) -> None:
        ...
    


class _MultisetHistogram(tuple):
    ...


_N = ...
_ITEMS = ...
_M = ...
def nP(n, k=..., replacement=...) -> Integer:
    ...

def nC(n, k=..., replacement=...) -> int | type[UndefinedFunction]:
    ...

def stirling(n, k, d=..., kind=..., signed=...) -> type[UndefinedFunction] | Integer:
    ...

def nT(n, k=...):
    ...

class motzkin(Function):
    @staticmethod
    def is_motzkin(n) -> bool:
        ...
    
    @staticmethod
    def find_motzkin_numbers_in_range(x, y) -> list[Any]:
        ...
    
    @staticmethod
    def find_first_n_motzkins(n) -> list[int]:
        ...
    
    @classmethod
    def eval(cls, n) -> Integer:
        ...
    


def nD(i=..., brute=..., *, n=..., m=...):
    ...

