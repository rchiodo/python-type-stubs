from typing import Any, Callable
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.core.logic import And
from sympy.core.mul import Mul
from sympy.functions.elementary.miscellaneous import Max
from sympy.integrals.transforms import IntegralTransform
from sympy.matrices.matrixbase import MatrixBase
from sympy.series.order import Order

_LT_level = ...
def DEBUG_WRAP(func) -> Callable[..., Any]:
    ...

@DEBUG_WRAP
def expand_dirac_delta(expr) -> tuple[Any, dict[Any, Any]] | tuple[Any | Order, dict[Any, Any | Order]] | tuple[Any | Mul, dict[Any, Any]]:
    ...

def laplace_correspondence(f, fdict, /) -> Expr:
    ...

def laplace_initial_conds(f, t, fdict, /):
    ...

class LaplaceTransform(IntegralTransform):
    _name = ...
    def doit(self, **hints) -> Order | tuple[Any | Order, Any | Max, Any | And]:
        ...
    


def laplace_transform(f, t, s, legacy_matrix=..., **hints) -> tuple[MatrixBase, Any | Max, Any | And] | MatrixBase | tuple[Any, Any, Any]:
    ...

class InverseLaplaceTransform(IntegralTransform):
    _name = ...
    _none_sentinel = ...
    _c = ...
    def __new__(cls, F, s, x, plane, **opts) -> type[UndefinedFunction]:
        ...
    
    @property
    def fundamental_plane(self) -> Basic | None:
        ...
    
    def doit(self, **hints) -> Order | tuple[Any | Order, Any | And]:
        ...
    


def inverse_laplace_transform(F, s, t, plane=..., **hints) -> tuple[Any, Any]:
    ...

