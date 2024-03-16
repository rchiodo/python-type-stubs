from typing import Any, Literal, Self, Tuple as tTuple
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import Function, UndefinedFunction
from sympy.core.relational import Equality, Ne, Relational
from sympy.core.symbol import Dummy, Symbol
from sympy.integrals.integrals import Integral
from sympy.series.order import Order

class re(Function):
    """
    Returns real part of expression. This function performs only
    elementary analysis and so it will fail to decompose properly
    more complicated expressions. If completely simplified result
    is needed then use ``Basic.as_real_imag()`` or perform complex
    expansion on instance of this function.

    Examples
    ========

    >>> from sympy import re, im, I, E, symbols
    >>> x, y = symbols('x y', real=True)
    >>> re(2*E)
    2*E
    >>> re(2*I + 17)
    17
    >>> re(2*I)
    0
    >>> re(im(x) + x*I + 2)
    2
    >>> re(5 + I + 2)
    7

    Parameters
    ==========

    arg : Expr
        Real or complex expression.

    Returns
    =======

    expr : Expr
        Real part of expression.

    See Also
    ========

    im
    """
    args: tTuple[Expr]
    is_extended_real = ...
    unbranched = ...
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> type[UndefinedFunction] | None:
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Self, Any]:
        """
        Returns the real number with a zero imaginary part.

        """
        ...
    


class im(Function):
    """
    Returns imaginary part of expression. This function performs only
    elementary analysis and so it will fail to decompose properly more
    complicated expressions. If completely simplified result is needed then
    use ``Basic.as_real_imag()`` or perform complex expansion on instance of
    this function.

    Examples
    ========

    >>> from sympy import re, im, E, I
    >>> from sympy.abc import x, y
    >>> im(2*E)
    0
    >>> im(2*I + 17)
    2
    >>> im(x*I)
    re(x)
    >>> im(re(x) + y)
    im(y)
    >>> im(2 + 3*I)
    3

    Parameters
    ==========

    arg : Expr
        Real or complex expression.

    Returns
    =======

    expr : Expr
        Imaginary part of expression.

    See Also
    ========

    re
    """
    args: tTuple[Expr]
    is_extended_real = ...
    unbranched = ...
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> None:
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Self, Any]:
        """
        Return the imaginary part with a zero real part.

        """
        ...
    


class sign(Function):
    """
    Returns the complex sign of an expression:

    Explanation
    ===========

    If the expression is real the sign will be:

        * $1$ if expression is positive
        * $0$ if expression is equal to zero
        * $-1$ if expression is negative

    If the expression is imaginary the sign will be:

        * $I$ if im(expression) is positive
        * $-I$ if im(expression) is negative

    Otherwise an unevaluated expression will be returned. When evaluated, the
    result (in general) will be ``cos(arg(expr)) + I*sin(arg(expr))``.

    Examples
    ========

    >>> from sympy import sign, I

    >>> sign(-1)
    -1
    >>> sign(0)
    0
    >>> sign(-3*I)
    -I
    >>> sign(1 + I)
    sign(1 + I)
    >>> _.evalf()
    0.707106781186548 + 0.707106781186548*I

    Parameters
    ==========

    arg : Expr
        Real or imaginary expression.

    Returns
    =======

    expr : Expr
        Complex sign of expression.

    See Also
    ========

    Abs, conjugate
    """
    is_complex = ...
    _singularities = ...
    def doit(self, **hints) -> Self:
        ...
    
    @classmethod
    def eval(cls, arg) -> sign | None:
        ...
    


class Abs(Function):
    """
    Return the absolute value of the argument.

    Explanation
    ===========

    This is an extension of the built-in function ``abs()`` to accept symbolic
    values.  If you pass a SymPy expression to the built-in ``abs()``, it will
    pass it automatically to ``Abs()``.

    Examples
    ========

    >>> from sympy import Abs, Symbol, S, I
    >>> Abs(-1)
    1
    >>> x = Symbol('x', real=True)
    >>> Abs(-x)
    Abs(x)
    >>> Abs(x**2)
    x**2
    >>> abs(-x) # The Python built-in
    Abs(x)
    >>> Abs(3*x + 2*I)
    sqrt(9*x**2 + 4)
    >>> Abs(8*I)
    8

    Note that the Python built-in will return either an Expr or int depending on
    the argument::

        >>> type(abs(-1))
        <... 'int'>
        >>> type(abs(S.NegativeOne))
        <class 'sympy.core.numbers.One'>

    Abs will always return a SymPy object.

    Parameters
    ==========

    arg : Expr
        Real or complex expression.

    Returns
    =======

    expr : Expr
        Absolute value returned can be an expression or integer depending on
        input arg.

    See Also
    ========

    sign, conjugate
    """
    args: tTuple[Expr]
    is_extended_real = ...
    is_extended_negative = ...
    is_extended_nonnegative = ...
    unbranched = ...
    _singularities = ...
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        """
        Get the first derivative of the argument to Abs().

        """
        ...
    
    @classmethod
    def eval(cls, arg):
        ...
    


class arg(Function):
    r"""
    Returns the argument (in radians) of a complex number. The argument is
    evaluated in consistent convention with ``atan2`` where the branch-cut is
    taken along the negative real axis and ``arg(z)`` is in the interval
    $(-\pi,\pi]$. For a positive number, the argument is always 0; the
    argument of a negative number is $\pi$; and the argument of 0
    is undefined and returns ``nan``. So the ``arg`` function will never nest
    greater than 3 levels since at the 4th application, the result must be
    nan; for a real number, nan is returned on the 3rd application.

    Examples
    ========

    >>> from sympy import arg, I, sqrt, Dummy
    >>> from sympy.abc import x
    >>> arg(2.0)
    0
    >>> arg(I)
    pi/2
    >>> arg(sqrt(2) + I*sqrt(2))
    pi/4
    >>> arg(sqrt(3)/2 + I/2)
    pi/6
    >>> arg(4 + 3*I)
    atan(3/4)
    >>> arg(0.8 + 0.6*I)
    0.643501108793284
    >>> arg(arg(arg(arg(x))))
    nan
    >>> real = Dummy(real=True)
    >>> arg(arg(arg(real)))
    nan

    Parameters
    ==========

    arg : Expr
        Real or complex expression.

    Returns
    =======

    value : Expr
        Returns arc tangent of arg measured in radians.

    """
    is_extended_real = ...
    is_real = ...
    is_finite = ...
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> type[UndefinedFunction] | Self | None:
        ...
    


class conjugate(Function):
    """
    Returns the *complex conjugate* [1]_ of an argument.
    In mathematics, the complex conjugate of a complex number
    is given by changing the sign of the imaginary part.

    Thus, the conjugate of the complex number
    :math:`a + ib` (where $a$ and $b$ are real numbers) is :math:`a - ib`

    Examples
    ========

    >>> from sympy import conjugate, I
    >>> conjugate(2)
    2
    >>> conjugate(I)
    -I
    >>> conjugate(3 + 2*I)
    3 - 2*I
    >>> conjugate(5 - I)
    5 + I

    Parameters
    ==========

    arg : Expr
        Real or complex expression.

    Returns
    =======

    arg : Expr
        Complex conjugate of arg as real, imaginary or mixed expression.

    See Also
    ========

    sign, Abs

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Complex_conjugation
    """
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> None:
        ...
    
    def inverse(self) -> type[conjugate]:
        ...
    


class transpose(Function):
    """
    Linear map transposition.

    Examples
    ========

    >>> from sympy import transpose, Matrix, MatrixSymbol
    >>> A = MatrixSymbol('A', 25, 9)
    >>> transpose(A)
    A.T
    >>> B = MatrixSymbol('B', 9, 22)
    >>> transpose(B)
    B.T
    >>> transpose(A*B)
    B.T*A.T
    >>> M = Matrix([[4, 5], [2, 1], [90, 12]])
    >>> M
    Matrix([
    [ 4,  5],
    [ 2,  1],
    [90, 12]])
    >>> transpose(M)
    Matrix([
    [4, 2, 90],
    [5, 1, 12]])

    Parameters
    ==========

    arg : Matrix
         Matrix or matrix expression to take the transpose of.

    Returns
    =======

    value : Matrix
        Transpose of arg.

    """
    @classmethod
    def eval(cls, arg) -> None:
        ...
    


class adjoint(Function):
    """
    Conjugate transpose or Hermite conjugation.

    Examples
    ========

    >>> from sympy import adjoint, MatrixSymbol
    >>> A = MatrixSymbol('A', 10, 5)
    >>> adjoint(A)
    Adjoint(A)

    Parameters
    ==========

    arg : Matrix
        Matrix or matrix expression to take the adjoint of.

    Returns
    =======

    value : Matrix
        Represents the conjugate transpose or Hermite
        conjugation of arg.

    """
    @classmethod
    def eval(cls, arg) -> type[UndefinedFunction] | None:
        ...
    


class polar_lift(Function):
    """
    Lift argument to the Riemann surface of the logarithm, using the
    standard branch.

    Examples
    ========

    >>> from sympy import Symbol, polar_lift, I
    >>> p = Symbol('p', polar=True)
    >>> x = Symbol('x')
    >>> polar_lift(4)
    4*exp_polar(0)
    >>> polar_lift(-4)
    4*exp_polar(I*pi)
    >>> polar_lift(-I)
    exp_polar(-I*pi/2)
    >>> polar_lift(I + 2)
    polar_lift(2 + I)

    >>> polar_lift(4*x)
    4*polar_lift(x)
    >>> polar_lift(4*p)
    4*p

    Parameters
    ==========

    arg : Expr
        Real or complex expression.

    See Also
    ========

    sympy.functions.elementary.exponential.exp_polar
    periodic_argument
    """
    is_polar = ...
    is_comparable = ...
    @classmethod
    def eval(cls, arg) -> Order | None:
        ...
    


class periodic_argument(Function):
    r"""
    Represent the argument on a quotient of the Riemann surface of the
    logarithm. That is, given a period $P$, always return a value in
    $(-P/2, P/2]$, by using $\exp(PI) = 1$.

    Examples
    ========

    >>> from sympy import exp_polar, periodic_argument
    >>> from sympy import I, pi
    >>> periodic_argument(exp_polar(10*I*pi), 2*pi)
    0
    >>> periodic_argument(exp_polar(5*I*pi), 4*pi)
    pi
    >>> from sympy import exp_polar, periodic_argument
    >>> from sympy import I, pi
    >>> periodic_argument(exp_polar(5*I*pi), 2*pi)
    pi
    >>> periodic_argument(exp_polar(5*I*pi), 3*pi)
    -pi
    >>> periodic_argument(exp_polar(5*I*pi), pi)
    0

    Parameters
    ==========

    ar : Expr
        A polar number.

    period : Expr
        The period $P$.

    See Also
    ========

    sympy.functions.elementary.exponential.exp_polar
    polar_lift : Lift argument to the Riemann surface of the logarithm
    principal_branch
    """
    @classmethod
    def eval(cls, ar, period) -> type[UndefinedFunction] | Literal[0] | None:
        ...
    


def unbranched_argument(arg) -> type[UndefinedFunction]:
    '''
    Returns periodic argument of arg with period as infinity.

    Examples
    ========

    >>> from sympy import exp_polar, unbranched_argument
    >>> from sympy import I, pi
    >>> unbranched_argument(exp_polar(15*I*pi))
    15*pi
    >>> unbranched_argument(exp_polar(7*I*pi))
    7*pi

    See also
    ========

    periodic_argument
    '''
    ...

class principal_branch(Function):
    """
    Represent a polar number reduced to its principal branch on a quotient
    of the Riemann surface of the logarithm.

    Explanation
    ===========

    This is a function of two arguments. The first argument is a polar
    number `z`, and the second one a positive real number or infinity, `p`.
    The result is ``z mod exp_polar(I*p)``.

    Examples
    ========

    >>> from sympy import exp_polar, principal_branch, oo, I, pi
    >>> from sympy.abc import z
    >>> principal_branch(z, oo)
    z
    >>> principal_branch(exp_polar(2*pi*I)*3, 2*pi)
    3*exp_polar(0)
    >>> principal_branch(exp_polar(2*pi*I)*3*z, 2*pi)
    3*principal_branch(z, 2*pi)

    Parameters
    ==========

    x : Expr
        A polar number.

    period : Expr
        Positive real number or infinity.

    See Also
    ========

    sympy.functions.elementary.exponential.exp_polar
    polar_lift : Lift argument to the Riemann surface of the logarithm
    periodic_argument
    """
    is_polar = ...
    is_comparable = ...
    @classmethod
    def eval(self, x, period) -> type[UndefinedFunction] | None:
        ...
    


def polarify(eq, subs=..., lift=...) -> type[UndefinedFunction] | Symbol | Equality | Relational | Ne | Integral | tuple[Any | Symbol | Basic | Equality | Relational | Ne | Integral, dict[Dummy, Any | Symbol | Basic]]:
    """
    Turn all numbers in eq into their polar equivalents (under the standard
    choice of argument).

    Note that no attempt is made to guess a formal convention of adding
    polar numbers, expressions like $1 + x$ will generally not be altered.

    Note also that this function does not promote ``exp(x)`` to ``exp_polar(x)``.

    If ``subs`` is ``True``, all symbols which are not already polar will be
    substituted for polar dummies; in this case the function behaves much
    like :func:`~.posify`.

    If ``lift`` is ``True``, both addition statements and non-polar symbols are
    changed to their ``polar_lift()``ed versions.
    Note that ``lift=True`` implies ``subs=False``.

    Examples
    ========

    >>> from sympy import polarify, sin, I
    >>> from sympy.abc import x, y
    >>> expr = (-x)**y
    >>> expr.expand()
    (-x)**y
    >>> polarify(expr)
    ((_x*exp_polar(I*pi))**_y, {_x: x, _y: y})
    >>> polarify(expr)[0].expand()
    _x**_y*exp_polar(_y*I*pi)
    >>> polarify(x, lift=True)
    polar_lift(x)
    >>> polarify(x*(1+y), lift=True)
    polar_lift(x)*polar_lift(y + 1)

    Adds are treated carefully:

    >>> polarify(1 + sin((1 + I)*x))
    (sin(_x*polar_lift(1 + I)) + 1, {_x: x})
    """
    ...

def unpolarify(eq, subs=..., exponents_only=...) -> bool | Basic:
    """
    If `p` denotes the projection from the Riemann surface of the logarithm to
    the complex line, return a simplified version `eq'` of `eq` such that
    `p(eq') = p(eq)`.
    Also apply the substitution subs in the end. (This is a convenience, since
    ``unpolarify``, in a certain sense, undoes :func:`polarify`.)

    Examples
    ========

    >>> from sympy import unpolarify, polar_lift, sin, I
    >>> unpolarify(polar_lift(I + 2))
    2 + I
    >>> unpolarify(sin(polar_lift(I + 7)))
    sin(7 + I)
    """
    ...

