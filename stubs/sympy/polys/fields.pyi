from typing import Any
from sympy.core.sympify import CantSympify
from sympy.polys.domains.domainelement import DomainElement
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public

"""Sparse rational function fields. """
@public
def field(symbols, domain, order=...) -> Any:
    """Construct new rational function field returning (field, x1, ..., xn). """
    ...

@public
def xfield(symbols, domain, order=...) -> tuple[FracField | Any, Any]:
    """Construct new rational function field returning (field, (x1, ..., xn)). """
    ...

@public
def vfield(symbols, domain, order=...) -> FracField | Any:
    """Construct new rational function field and inject generators into global namespace. """
    ...

@public
def sfield(exprs, *symbols, **options) -> tuple[FracField | Any, Any] | tuple[FracField | Any, list[Any]]:
    """Construct a field deriving generators and domain
    from options and input expressions.

    Parameters
    ==========

    exprs   : py:class:`~.Expr` or sequence of :py:class:`~.Expr` (sympifiable)

    symbols : sequence of :py:class:`~.Symbol`/:py:class:`~.Expr`

    options : keyword arguments understood by :py:class:`~.Options`

    Examples
    ========

    >>> from sympy import exp, log, symbols, sfield

    >>> x = symbols("x")
    >>> K, f = sfield((x*log(x) + 4*x**2)*exp(1/x + log(x)/3)/x**2)
    >>> K
    Rational function field in x, exp(1/x), log(x), x**(1/3) over ZZ with lex order
    >>> f
    (4*x**2*(exp(1/x)) + x*(exp(1/x))*(log(x)))/((x**(1/3))**5)
    """
    ...

_field_cache: dict[Any, Any] = ...
class FracField(DefaultPrinting):
    """Multivariate distributed rational function field. """
    def __new__(cls, symbols, domain, order=...) -> Self | Any:
        ...
    
    def __getnewargs__(self) -> tuple[Any, Any, Any]:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def index(self, gen):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def raw_new(self, numer, denom=...):
        ...
    
    def new(self, numer, denom=...):
        ...
    
    def domain_new(self, element):
        ...
    
    def ground_new(self, element):
        ...
    
    def field_new(self, element) -> FracElement:
        ...
    
    __call__ = ...
    def from_expr(self, expr):
        ...
    
    def to_domain(self) -> Any:
        ...
    
    def to_ring(self) -> PolyRing | Any:
        ...
    


class FracElement(DomainElement, DefaultPrinting, CantSympify):
    """Element of multivariate distributed rational function field. """
    def __init__(self, numer, denom=...) -> None:
        ...
    
    def raw_new(f, numer, denom) -> Self:
        ...
    
    def new(f, numer, denom) -> Self:
        ...
    
    def to_poly(f) -> Any:
        ...
    
    def parent(self):
        ...
    
    def __getnewargs__(self) -> tuple[Any, Any, Any]:
        ...
    
    _hash = ...
    def __hash__(self) -> int:
        ...
    
    def copy(self) -> Self:
        ...
    
    def set_field(self, new_field) -> Self:
        ...
    
    def as_expr(self, *symbols):
        ...
    
    def __eq__(f, g) -> bool:
        ...
    
    def __ne__(f, g) -> bool:
        ...
    
    def __bool__(f) -> bool:
        ...
    
    def sort_key(self) -> tuple[Any, Any]:
        ...
    
    def __lt__(f1, f2) -> bool:
        ...
    
    def __le__(f1, f2) -> bool:
        ...
    
    def __gt__(f1, f2) -> bool:
        ...
    
    def __ge__(f1, f2) -> bool:
        ...
    
    def __pos__(f) -> Self:
        """Negate all coefficients in ``f``. """
        ...
    
    def __neg__(f) -> Self:
        """Negate all coefficients in ``f``. """
        ...
    
    def __add__(f, g) -> Self | FracElement | NotImplementedType | PolyElement:
        """Add rational functions ``f`` and ``g``. """
        ...
    
    def __radd__(f, c) -> Self | NotImplementedType:
        ...
    
    def __sub__(f, g) -> Self | FracElement | NotImplementedType:
        """Subtract rational functions ``f`` and ``g``. """
        ...
    
    def __rsub__(f, c) -> Self | NotImplementedType:
        ...
    
    def __mul__(f, g) -> Self | FracElement | NotImplementedType:
        """Multiply rational functions ``f`` and ``g``. """
        ...
    
    def __rmul__(f, c) -> Self | NotImplementedType:
        ...
    
    def __truediv__(f, g) -> Self | FracElement | NotImplementedType:
        """Computes quotient of fractions ``f`` and ``g``. """
        ...
    
    def __rtruediv__(f, c) -> Self | NotImplementedType:
        ...
    
    def __pow__(f, n) -> Self:
        """Raise ``f`` to a non-negative power ``n``. """
        ...
    
    def diff(f, x) -> Self:
        """Computes partial derivative in ``x``.

        Examples
        ========

        >>> from sympy.polys.fields import field
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y, z = field("x,y,z", ZZ)
        >>> ((x**2 + y)/(z + 1)).diff(x)
        2*x/(z + 1)

        """
        ...
    
    def __call__(f, *values):
        ...
    
    def evaluate(f, x, a=...):
        ...
    
    def subs(f, x, a=...) -> Self:
        ...
    
    def compose(f, x, a=...):
        ...
    


