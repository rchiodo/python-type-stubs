from typing import Any, Literal
from sympy.core.basic import Basic
from sympy.core.logic import And
from sympy.core.relational import Equality, Ne, Relational
from sympy.integrals.integrals import Integral
import sympy.integrals.laplace as _laplace
from sympy.core.function import Function, UndefinedFunction
from sympy.functions.elementary.trigonometric import cos, sin
from sympy.series.order import Order

class IntegralTransformError(NotImplementedError):
    def __init__(self, transform, function, msg) -> None:
        ...
    


class IntegralTransform(Function):
    @property
    def function(self) -> Basic:
        ...
    
    @property
    def function_variable(self) -> Basic:
        ...
    
    @property
    def transform_variable(self) -> Basic:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    def doit(self, **hints) -> Order | tuple[Any | Order, *tuple[Any, ...]] | tuple[Any | Order, Any | And]:
        ...
    
    @property
    def as_integral(self):
        ...
    


_noconds = ...
class MellinTransform(IntegralTransform):
    _name = ...


def mellin_transform(f, x, s, **hints):
    ...

class MellinTransformStripError(ValueError):
    ...


_allowed = ...
class InverseMellinTransform(IntegralTransform):
    _name = ...
    _none_sentinel = ...
    _c = ...
    def __new__(cls, F, s, x, a, b, **opts) -> type[UndefinedFunction]:
        ...
    
    @property
    def fundamental_strip(self) -> tuple[Basic | None, Basic | None]:
        ...
    


def inverse_mellin_transform(F, s, x, strip, **hints):
    ...

class FourierTypeTransform(IntegralTransform):
    def a(self):
        ...
    
    def b(self):
        ...
    


class FourierTransform(FourierTypeTransform):
    _name = ...
    def a(self) -> Literal[1]:
        ...
    
    def b(self):
        ...
    


def fourier_transform(f, x, k, **hints):
    ...

class InverseFourierTransform(FourierTypeTransform):
    _name = ...
    def a(self) -> Literal[1]:
        ...
    
    def b(self):
        ...
    


def inverse_fourier_transform(F, k, x, **hints):
    ...

class SineCosineTypeTransform(IntegralTransform):
    def a(self):
        ...
    
    def b(self):
        ...
    


class SineTransform(SineCosineTypeTransform):
    _name = ...
    _kern = sin
    def a(self):
        ...
    
    def b(self):
        ...
    


def sine_transform(f, x, k, **hints):
    ...

class InverseSineTransform(SineCosineTypeTransform):
    _name = ...
    _kern = sin
    def a(self):
        ...
    
    def b(self):
        ...
    


def inverse_sine_transform(F, k, x, **hints):
    ...

class CosineTransform(SineCosineTypeTransform):
    _name = ...
    _kern = cos
    def a(self):
        ...
    
    def b(self):
        ...
    


def cosine_transform(f, x, k, **hints):
    ...

class InverseCosineTransform(SineCosineTypeTransform):
    _name = ...
    _kern = cos
    def a(self):
        ...
    
    def b(self):
        ...
    


def inverse_cosine_transform(F, k, x, **hints):
    ...

class HankelTypeTransform(IntegralTransform):
    def doit(self, **hints) -> tuple[Any | Equality | Relational | Ne, Any] | tuple[Any, Any]:
        ...
    
    @property
    def as_integral(self) -> Equality | Relational | Ne | Integral:
        ...
    


class HankelTransform(HankelTypeTransform):
    _name = ...


def hankel_transform(f, r, k, nu, **hints):
    ...

class InverseHankelTransform(HankelTypeTransform):
    _name = ...


def inverse_hankel_transform(F, k, r, nu, **hints):
    ...

LaplaceTransform = _laplace.LaplaceTransform
laplace_transform = ...
laplace_correspondence = ...
laplace_initial_conds = ...
InverseLaplaceTransform = _laplace.InverseLaplaceTransform
inverse_laplace_transform = ...
