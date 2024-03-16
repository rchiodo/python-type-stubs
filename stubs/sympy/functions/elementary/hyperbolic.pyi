from typing import Any, Self
from sympy.core import cacheit
from sympy.core.basic import Basic
from sympy.core.function import Function, UndefinedFunction
from sympy.core.logic import FuzzyBool
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.functions.elementary.exponential import log
from sympy.series.order import Order

class HyperbolicFunction(Function):
    """
    Base class for hyperbolic functions.

    See Also
    ========

    sinh, cosh, tanh, coth
    """
    unbranched = ...


class sinh(HyperbolicFunction):
    r"""
    ``sinh(x)`` is the hyperbolic sine of ``x``.

    The hyperbolic sine function is $\frac{e^x - e^{-x}}{2}$.

    Examples
    ========

    >>> from sympy import sinh
    >>> from sympy.abc import x
    >>> sinh(x)
    sinh(x)

    See Also
    ========

    cosh, tanh, asinh
    """
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        """
        Returns the first derivative of this function.
        """
        ...
    
    def inverse(self, argindex=...) -> type[asinh]:
        """
        Returns the inverse of this function.
        """
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        """
        Returns the next term in the Taylor series expansion.
        """
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        """
        Returns this function as a complex coordinate.
        """
        ...
    


class cosh(HyperbolicFunction):
    r"""
    ``cosh(x)`` is the hyperbolic cosine of ``x``.

    The hyperbolic cosine function is $\frac{e^x + e^{-x}}{2}$.

    Examples
    ========

    >>> from sympy import cosh
    >>> from sympy.abc import x
    >>> cosh(x)
    cosh(x)

    See Also
    ========

    sinh, tanh, acosh
    """
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        ...
    
    @classmethod
    def eval(cls, arg) -> Self | type[UndefinedFunction] | Pow | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        ...
    


class tanh(HyperbolicFunction):
    r"""
    ``tanh(x)`` is the hyperbolic tangent of ``x``.

    The hyperbolic tangent function is $\frac{\sinh(x)}{\cosh(x)}$.

    Examples
    ========

    >>> from sympy import tanh
    >>> from sympy.abc import x
    >>> tanh(x)
    tanh(x)

    See Also
    ========

    sinh, cosh, atanh
    """
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[atanh]:
        """
        Returns the inverse of this function.
        """
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | type[UndefinedFunction] | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        ...
    


class coth(HyperbolicFunction):
    r"""
    ``coth(x)`` is the hyperbolic cotangent of ``x``.

    The hyperbolic cotangent function is $\frac{\cosh(x)}{\sinh(x)}$.

    Examples
    ========

    >>> from sympy import coth
    >>> from sympy.abc import x
    >>> coth(x)
    coth(x)

    See Also
    ========

    sinh, cosh, acoth
    """
    def fdiff(self, argindex=...):
        ...
    
    def inverse(self, argindex=...) -> type[acoth]:
        """
        Returns the inverse of this function.
        """
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | type[UndefinedFunction] | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any | Order | Self, Any] | tuple[Self, Any] | tuple[Any, Any]:
        ...
    


class ReciprocalHyperbolicFunction(HyperbolicFunction):
    """Base class for reciprocal functions of hyperbolic functions. """
    _reciprocal_of = ...
    _is_even: FuzzyBool = ...
    _is_odd: FuzzyBool = ...
    @classmethod
    def eval(cls, arg) -> Self | Mul:
        ...
    
    def as_real_imag(self, deep=..., **hints):
        ...
    


class csch(ReciprocalHyperbolicFunction):
    r"""
    ``csch(x)`` is the hyperbolic cosecant of ``x``.

    The hyperbolic cosecant function is $\frac{2}{e^x - e^{-x}}$

    Examples
    ========

    >>> from sympy import csch
    >>> from sympy.abc import x
    >>> csch(x)
    csch(x)

    See Also
    ========

    sinh, cosh, tanh, sech, asinh, acosh
    """
    _reciprocal_of = sinh
    _is_odd = ...
    def fdiff(self, argindex=...):
        """
        Returns the first derivative of this function
        """
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        """
        Returns the next term in the Taylor series expansion
        """
        ...
    


class sech(ReciprocalHyperbolicFunction):
    r"""
    ``sech(x)`` is the hyperbolic secant of ``x``.

    The hyperbolic secant function is $\frac{2}{e^x + e^{-x}}$

    Examples
    ========

    >>> from sympy import sech
    >>> from sympy.abc import x
    >>> sech(x)
    sech(x)

    See Also
    ========

    sinh, cosh, tanh, coth, csch, asinh, acosh
    """
    _reciprocal_of = cosh
    _is_even = ...
    def fdiff(self, argindex=...):
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    


class InverseHyperbolicFunction(Function):
    """Base class for inverse hyperbolic functions."""
    ...


class asinh(InverseHyperbolicFunction):
    """
    ``asinh(x)`` is the inverse hyperbolic sine of ``x``.

    The inverse hyperbolic sine function.

    Examples
    ========

    >>> from sympy import asinh
    >>> from sympy.abc import x
    >>> asinh(x).diff(x)
    1/sqrt(x**2 + 1)
    >>> asinh(1)
    log(1 + sqrt(2))

    See Also
    ========

    acosh, atanh, sinh
    """
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> log | Mul | Basic | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[sinh]:
        """
        Returns the inverse of this function.
        """
        ...
    


class acosh(InverseHyperbolicFunction):
    """
    ``acosh(x)`` is the inverse hyperbolic cosine of ``x``.

    The inverse hyperbolic cosine function.

    Examples
    ========

    >>> from sympy import acosh
    >>> from sympy.abc import x
    >>> acosh(x).diff(x)
    1/(sqrt(x - 1)*sqrt(x + 1))
    >>> acosh(1)
    0

    See Also
    ========

    asinh, atanh, cosh
    """
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg):
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[cosh]:
        """
        Returns the inverse of this function.
        """
        ...
    


class atanh(InverseHyperbolicFunction):
    """
    ``atanh(x)`` is the inverse hyperbolic tangent of ``x``.

    The inverse hyperbolic tangent function.

    Examples
    ========

    >>> from sympy import atanh
    >>> from sympy.abc import x
    >>> atanh(x).diff(x)
    1/(1 - x**2)

    See Also
    ========

    asinh, acosh, tanh
    """
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | Basic | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[tanh]:
        """
        Returns the inverse of this function.
        """
        ...
    


class acoth(InverseHyperbolicFunction):
    """
    ``acoth(x)`` is the inverse hyperbolic cotangent of ``x``.

    The inverse hyperbolic cotangent function.

    Examples
    ========

    >>> from sympy import acoth
    >>> from sympy.abc import x
    >>> acoth(x).diff(x)
    1/(1 - x**2)

    See Also
    ========

    asinh, acosh, coth
    """
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        ...
    
    _eval_rewrite_as_tractable = ...
    def inverse(self, argindex=...) -> type[coth]:
        """
        Returns the inverse of this function.
        """
        ...
    


class asech(InverseHyperbolicFunction):
    """
    ``asech(x)`` is the inverse hyperbolic secant of ``x``.

    The inverse hyperbolic secant function.

    Examples
    ========

    >>> from sympy import asech, sqrt, S
    >>> from sympy.abc import x
    >>> asech(x).diff(x)
    -1/(x*sqrt(1 - x**2))
    >>> asech(1).diff(x)
    0
    >>> asech(1)
    0
    >>> asech(S(2))
    I*pi/3
    >>> asech(-sqrt(2))
    3*I*pi/4
    >>> asech((sqrt(6) - sqrt(2)))
    I*pi/12

    See Also
    ========

    asinh, atanh, cosh, acoth

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hyperbolic_function
    .. [2] https://dlmf.nist.gov/4.37
    .. [3] https://functions.wolfram.com/ElementaryFunctions/ArcSech/

    """
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms) -> type[UndefinedFunction]:
        ...
    
    def inverse(self, argindex=...) -> type[sech]:
        """
        Returns the inverse of this function.
        """
        ...
    
    _eval_rewrite_as_tractable = ...


class acsch(InverseHyperbolicFunction):
    """
    ``acsch(x)`` is the inverse hyperbolic cosecant of ``x``.

    The inverse hyperbolic cosecant function.

    Examples
    ========

    >>> from sympy import acsch, sqrt, I
    >>> from sympy.abc import x
    >>> acsch(x).diff(x)
    -1/(x**2*sqrt(1 + x**(-2)))
    >>> acsch(1).diff(x)
    0
    >>> acsch(1)
    log(1 + sqrt(2))
    >>> acsch(I)
    -I*pi/2
    >>> acsch(-2*I)
    I*pi/6
    >>> acsch(I*(sqrt(6) - sqrt(2)))
    -5*I*pi/12

    See Also
    ========

    asinh

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hyperbolic_function
    .. [2] https://dlmf.nist.gov/4.37
    .. [3] https://functions.wolfram.com/ElementaryFunctions/ArcCsch/

    """
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> log | Mul | None:
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms) -> type[UndefinedFunction]:
        ...
    
    def inverse(self, argindex=...) -> type[csch]:
        """
        Returns the inverse of this function.
        """
        ...
    
    _eval_rewrite_as_tractable = ...


