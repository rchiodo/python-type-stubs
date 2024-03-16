from typing import Any, Literal, Self, Tuple as tTuple
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import Function, FunctionClass, UndefinedFunction
from sympy.core.kind import Kind
from sympy.core.numbers import Integer
from sympy.series.order import Order

class ExpBase(Function):
    unbranched = ...
    _singularities = ...
    @property
    def kind(self) -> Kind:
        ...
    
    def inverse(self, argindex=...) -> type[log]:
        """
        Returns the inverse function of ``exp(x)``.
        """
        ...
    
    def as_numer_denom(self) -> tuple[Self, Any] | tuple[Any, Self]:
        """
        Returns this with a positive exponent as a 2-tuple (a fraction).

        Examples
        ========

        >>> from sympy import exp
        >>> from sympy.abc import x
        >>> exp(-x).as_numer_denom()
        (1, exp(x))
        >>> exp(x).as_numer_denom()
        (exp(x), 1)
        """
        ...
    
    @property
    def exp(self) -> Basic:
        """
        Returns the exponent of the function.
        """
        ...
    
    def as_base_exp(self) -> tuple[Self, Any | Order]:
        """
        Returns the 2-tuple (base, exponent).
        """
        ...
    


class exp_polar(ExpBase):
    r"""
    Represent a *polar number* (see g-function Sphinx documentation).

    Explanation
    ===========

    ``exp_polar`` represents the function
    `Exp: \mathbb{C} \rightarrow \mathcal{S}`, sending the complex number
    `z = a + bi` to the polar number `r = exp(a), \theta = b`. It is one of
    the main functions to construct polar numbers.

    Examples
    ========

    >>> from sympy import exp_polar, pi, I, exp

    The main difference is that polar numbers do not "wrap around" at `2 \pi`:

    >>> exp(2*pi*I)
    1
    >>> exp_polar(2*pi*I)
    exp_polar(2*I*pi)

    apart from that they behave mostly like classical complex numbers:

    >>> exp_polar(2)*exp_polar(3)
    exp_polar(5)

    See Also
    ========

    sympy.simplify.powsimp.powsimp
    polar_lift
    periodic_argument
    principal_branch
    """
    is_polar = ...
    is_comparable = ...
    def as_base_exp(self) -> tuple[Self, Any] | tuple[ExpBase, Any | Order]:
        ...
    


class ExpMeta(FunctionClass):
    def __instancecheck__(cls, instance) -> bool:
        ...
    


class exp(ExpBase, metaclass=ExpMeta):
    """
    The exponential function, :math:`e^x`.

    Examples
    ========

    >>> from sympy import exp, I, pi
    >>> from sympy.abc import x
    >>> exp(x)
    exp(x)
    >>> exp(x).diff(x)
    exp(x)
    >>> exp(I*pi)
    -1

    Parameters
    ==========

    arg : Expr

    See Also
    ========

    log
    """
    def fdiff(self, argindex=...) -> Self:
        """
        Returns the first derivative of this function.
        """
        ...
    
    @classmethod
    def eval(cls, arg):
        ...
    
    @property
    def base(self):
        """
        Returns the base of the exponential function.
        """
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        """
        Calculates the next term in the Taylor series expansion.
        """
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]:
        """
        Returns this function as a 2-tuple representing a complex number.

        Examples
        ========

        >>> from sympy import exp, I
        >>> from sympy.abc import x
        >>> exp(x).as_real_imag()
        (exp(re(x))*cos(im(x)), exp(re(x))*sin(im(x)))
        >>> exp(1).as_real_imag()
        (E, 0)
        >>> exp(I).as_real_imag()
        (cos(1), sin(1))
        >>> exp(1+I).as_real_imag()
        (E*cos(1), E*sin(1))

        See Also
        ========

        sympy.functions.elementary.complexes.re
        sympy.functions.elementary.complexes.im
        """
        ...
    


def match_real_imag(expr) -> tuple[Any, Literal[0]] | tuple[Any, Any] | tuple[None, None]:
    r"""
    Try to match expr with $a + Ib$ for real $a$ and $b$.

    ``match_real_imag`` returns a tuple containing the real and imaginary
    parts of expr or ``(None, None)`` if direct matching is not possible. Contrary
    to :func:`~.re()`, :func:`~.im()``, and ``as_real_imag()``, this helper will not force things
    by returning expressions themselves containing ``re()`` or ``im()`` and it
    does not expand its argument either.

    """
    ...

class log(Function):
    r"""
    The natural logarithm function `\ln(x)` or `\log(x)`.

    Explanation
    ===========

    Logarithms are taken with the natural base, `e`. To get
    a logarithm of a different base ``b``, use ``log(x, b)``,
    which is essentially short-hand for ``log(x)/log(b)``.

    ``log`` represents the principal branch of the natural
    logarithm. As such it has a branch cut along the negative
    real axis and returns values having a complex argument in
    `(-\pi, \pi]`.

    Examples
    ========

    >>> from sympy import log, sqrt, S, I
    >>> log(8, 2)
    3
    >>> log(S(8)/3, 2)
    -log(3)/log(2) + 3
    >>> log(-1 + I*sqrt(3))
    log(2) + 2*I*pi/3

    See Also
    ========

    exp

    """
    args: tTuple[Expr]
    _singularities = ...
    def fdiff(self, argindex=...):
        """
        Returns the first derivative of the function.
        """
        ...
    
    def inverse(self, argindex=...) -> type[exp]:
        r"""
        Returns `e^x`, the inverse function of `\log(x)`.
        """
        ...
    
    @classmethod
    def eval(cls, arg, base=...):
        ...
    
    def as_base_exp(self) -> tuple[Self, Any]:
        """
        Returns this function in the form (base, exponent).
        """
        ...
    
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms):
        r"""
        Returns the next term in the Taylor series expansion of `\log(1+x)`.
        """
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Self, Any] | tuple[Any, type[UndefinedFunction] | Any] | tuple[type[UndefinedFunction] | Any, type[UndefinedFunction] | Any]:
        """
        Returns this function as a complex coordinate.

        Examples
        ========

        >>> from sympy import I, log
        >>> from sympy.abc import x
        >>> log(x).as_real_imag()
        (log(Abs(x)), arg(x))
        >>> log(I).as_real_imag()
        (0, pi/2)
        >>> log(1 + I).as_real_imag()
        (log(sqrt(2)), pi/4)
        >>> log(I*x).as_real_imag()
        (log(Abs(x)), arg(I*x))

        """
        ...
    


class LambertW(Function):
    r"""
    The Lambert W function $W(z)$ is defined as the inverse
    function of $w \exp(w)$ [1]_.

    Explanation
    ===========

    In other words, the value of $W(z)$ is such that $z = W(z) \exp(W(z))$
    for any complex number $z$.  The Lambert W function is a multivalued
    function with infinitely many branches $W_k(z)$, indexed by
    $k \in \mathbb{Z}$.  Each branch gives a different solution $w$
    of the equation $z = w \exp(w)$.

    The Lambert W function has two partially real branches: the
    principal branch ($k = 0$) is real for real $z > -1/e$, and the
    $k = -1$ branch is real for $-1/e < z < 0$. All branches except
    $k = 0$ have a logarithmic singularity at $z = 0$.

    Examples
    ========

    >>> from sympy import LambertW
    >>> LambertW(1.2)
    0.635564016364870
    >>> LambertW(1.2, -1).n()
    -1.34747534407696 - 4.41624341514535*I
    >>> LambertW(-1).is_real
    False

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lambert_W_function
    """
    _singularities = ...
    @classmethod
    def eval(cls, x, k=...) -> Self | type[UndefinedFunction] | Integer | None:
        ...
    
    def fdiff(self, argindex=...):
        """
        Return the first derivative of this function.
        """
        ...
    


