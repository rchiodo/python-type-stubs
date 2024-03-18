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

"""Laplace Transforms"""
_LT_level = ...
def DEBUG_WRAP(func) -> Callable[..., Any]:
    ...

@DEBUG_WRAP
def expand_dirac_delta(expr) -> tuple[Any, dict[Any, Any]] | tuple[Any | Order, dict[Any, Any | Order]] | tuple[Any | Mul, dict[Any, Any]]:
    """
    Expand an expression involving DiractDelta to get it as a linear
    combination of DiracDelta functions.
    """
    ...

def laplace_correspondence(f, fdict, /) -> Expr:
    """
    This helper function takes a function `f` that is the result of a
    ``laplace_transform`` or an ``inverse_laplace_transform``.  It replaces all
    unevaluated ``LaplaceTransform(y(t), t, s)`` by `Y(s)` for any `s` and
    all ``InverseLaplaceTransform(Y(s), s, t)`` by `y(t)` for any `t` if
    ``fdict`` contains a correspondence ``{y: Y}``.

    Parameters
    ==========

    f : sympy expression
        Expression containing unevaluated ``LaplaceTransform`` or
        ``LaplaceTransform`` objects.
    fdict : dictionary
        Dictionary containing one or more function correspondences,
        e.g., ``{x: X, y: Y}`` meaning that ``X`` and ``Y`` are the
        Laplace transforms of ``x`` and ``y``, respectively.

    Examples
    ========

    >>> from sympy import laplace_transform, diff, Function
    >>> from sympy import laplace_correspondence, inverse_laplace_transform
    >>> from sympy.abc import t, s
    >>> y = Function("y")
    >>> Y = Function("Y")
    >>> z = Function("z")
    >>> Z = Function("Z")
    >>> f = laplace_transform(diff(y(t), t, 1) + z(t), t, s, noconds=True)
    >>> laplace_correspondence(f, {y: Y, z: Z})
    s*Y(s) + Z(s) - y(0)
    >>> f = inverse_laplace_transform(Y(s), s, t)
    >>> laplace_correspondence(f, {y: Y})
    y(t)
    """
    ...

def laplace_initial_conds(f, t, fdict, /):
    """
    This helper function takes a function `f` that is the result of a
    ``laplace_transform``.  It takes an fdict of the form ``{y: [1, 4, 2]}``,
    where the values in the list are the initial value, the initial slope, the
    initial second derivative, etc., of the function `y(t)`, and replaces all
    unevaluated initial conditions.

    Parameters
    ==========

    f : sympy expression
        Expression containing initial conditions of unevaluated functions.
    t : sympy expression
        Variable for which the initial conditions are to be applied.
    fdict : dictionary
        Dictionary containing a list of initial conditions for every
        function, e.g., ``{y: [0, 1, 2], x: [3, 4, 5]}``. The order
        of derivatives is ascending, so `0`, `1`, `2` are `y(0)`, `y'(0)`,
        and `y''(0)`, respectively.

    Examples
    ========

    >>> from sympy import laplace_transform, diff, Function
    >>> from sympy import laplace_correspondence, laplace_initial_conds
    >>> from sympy.abc import t, s
    >>> y = Function("y")
    >>> Y = Function("Y")
    >>> f = laplace_transform(diff(y(t), t, 3), t, s, noconds=True)
    >>> g = laplace_correspondence(f, {y: Y})
    >>> laplace_initial_conds(g, t, {y: [2, 4, 8, 16, 32]})
    s**3*Y(s) - 2*s**2 - 4*s - 8
    """
    ...

class LaplaceTransform(IntegralTransform):
    """
    Class representing unevaluated Laplace transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Laplace transforms, see the :func:`laplace_transform`
    docstring.

    If this is called with ``.doit()``, it returns the Laplace transform as an
    expression. If it is called with ``.doit(noconds=False)``, it returns a
    tuple containing the same expression, a convergence plane, and conditions.
    """
    _name = ...
    def doit(self, **hints) -> Order | tuple[Any | Order, Any | Max, Any | And]:
        """
        Try to evaluate the transform in closed form.

        Explanation
        ===========

        Standard hints are the following:
        - ``noconds``:  if True, do not return convergence conditions. The
        default setting is `True`.
        - ``simplify``: if True, it simplifies the final result. The
        default setting is `False`.
        """
        ...
    


def laplace_transform(f, t, s, legacy_matrix=..., **hints) -> tuple[MatrixBase, Any | Max, Any | And] | MatrixBase | tuple[Any, Any, Any]:
    r"""
    Compute the Laplace Transform `F(s)` of `f(t)`,

    .. math :: F(s) = \int_{0^{-}}^\infty e^{-st} f(t) \mathrm{d}t.

    Explanation
    ===========

    For all sensible functions, this converges absolutely in a
    half-plane

    .. math :: a < \operatorname{Re}(s)

    This function returns ``(F, a, cond)`` where ``F`` is the Laplace
    transform of ``f``, `a` is the half-plane of convergence, and `cond` are
    auxiliary convergence conditions.

    The implementation is rule-based, and if you are interested in which
    rules are applied, and whether integration is attempted, you can switch
    debug information on by setting ``sympy.SYMPY_DEBUG=True``. The numbers
    of the rules in the debug information (and the code) refer to Bateman's
    Tables of Integral Transforms [1].

    The lower bound is `0-`, meaning that this bound should be approached
    from the lower side. This is only necessary if distributions are involved.
    At present, it is only done if `f(t)` contains ``DiracDelta``, in which
    case the Laplace transform is computed implicitly as

    .. math ::
        F(s) = \lim_{\tau\to 0^{-}} \int_{\tau}^\infty e^{-st}
        f(t) \mathrm{d}t

    by applying rules.

    If the Laplace transform cannot be fully computed in closed form, this
    function returns expressions containing unevaluated
    :class:`LaplaceTransform` objects.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`. If
    ``noconds=True``, only `F` will be returned (i.e. not ``cond``, and also
    not the plane ``a``).

    .. deprecated:: 1.9
        Legacy behavior for matrices where ``laplace_transform`` with
        ``noconds=False`` (the default) returns a Matrix whose elements are
        tuples. The behavior of ``laplace_transform`` for matrices will change
        in a future release of SymPy to return a tuple of the transformed
        Matrix and the convergence conditions for the matrix as a whole. Use
        ``legacy_matrix=False`` to enable the new behavior.

    Examples
    ========

    >>> from sympy import DiracDelta, exp, laplace_transform
    >>> from sympy.abc import t, s, a
    >>> laplace_transform(t**4, t, s)
    (24/s**5, 0, True)
    >>> laplace_transform(t**a, t, s)
    (gamma(a + 1)/(s*s**a), 0, re(a) > -1)
    >>> laplace_transform(DiracDelta(t)-a*exp(-a*t), t, s, simplify=True)
    (s/(a + s), -re(a), True)

    There are also helper functions that make it easy to solve differential
    equations by Laplace transform. For example, to solve

    .. math :: m x''(t) + d x'(t) + k x(t) = 0

    with initial value `0` and initial derivative `v`:

    >>> from sympy import Function, laplace_correspondence, diff, solve
    >>> from sympy import laplace_initial_conds, inverse_laplace_transform
    >>> from sympy.abc import d, k, m, v
    >>> x = Function('x')
    >>> X = Function('X')
    >>> f = m*diff(x(t), t, 2) + d*diff(x(t), t) + k*x(t)
    >>> F = laplace_transform(f, t, s, noconds=True)
    >>> F = laplace_correspondence(F, {x: X})
    >>> F = laplace_initial_conds(F, t, {x: [0, v]})
    >>> F
    d*s*X(s) + k*X(s) + m*(s**2*X(s) - v)
    >>> Xs = solve(F, X(s))[0]
    >>> Xs
    m*v/(d*s + k + m*s**2)
    >>> inverse_laplace_transform(Xs, s, t)
    2*v*exp(-d*t/(2*m))*sin(t*sqrt((-d**2 + 4*k*m)/m**2)/2)*Heaviside(t)/sqrt((-d**2 + 4*k*m)/m**2)

    References
    ==========

    .. [1] Erdelyi, A. (ed.), Tables of Integral Transforms, Volume 1,
           Bateman Manuscript Prooject, McGraw-Hill (1954), available:
           https://resolver.caltech.edu/CaltechAUTHORS:20140123-101456353

    See Also
    ========

    inverse_laplace_transform, mellin_transform, fourier_transform
    hankel_transform, inverse_hankel_transform

    """
    ...

class InverseLaplaceTransform(IntegralTransform):
    """
    Class representing unevaluated inverse Laplace transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Laplace transforms, see the
    :func:`inverse_laplace_transform` docstring.
    """
    _name = ...
    _none_sentinel = ...
    _c = ...
    def __new__(cls, F, s, x, plane, **opts) -> type[UndefinedFunction]:
        ...
    
    @property
    def fundamental_plane(self) -> Basic | None:
        ...
    
    def doit(self, **hints) -> Order | tuple[Any | Order, Any | And]:
        """
        Try to evaluate the transform in closed form.

        Explanation
        ===========

        Standard hints are the following:
        - ``noconds``:  if True, do not return convergence conditions. The
        default setting is `True`.
        - ``simplify``: if True, it simplifies the final result. The
        default setting is `False`.
        """
        ...
    


def inverse_laplace_transform(F, s, t, plane=..., **hints) -> tuple[Any, Any]:
    r"""
    Compute the inverse Laplace transform of `F(s)`, defined as

    .. math ::
        f(t) = \frac{1}{2\pi i} \int_{c-i\infty}^{c+i\infty} e^{st}
        F(s) \mathrm{d}s,

    for `c` so large that `F(s)` has no singularites in the
    half-plane `\operatorname{Re}(s) > c-\epsilon`.

    Explanation
    ===========

    The plane can be specified by
    argument ``plane``, but will be inferred if passed as None.

    Under certain regularity conditions, this recovers `f(t)` from its
    Laplace Transform `F(s)`, for non-negative `t`, and vice
    versa.

    If the integral cannot be computed in closed form, this function returns
    an unevaluated :class:`InverseLaplaceTransform` object.

    Note that this function will always assume `t` to be real,
    regardless of the SymPy assumption on `t`.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.

    Examples
    ========

    >>> from sympy import inverse_laplace_transform, exp, Symbol
    >>> from sympy.abc import s, t
    >>> a = Symbol('a', positive=True)
    >>> inverse_laplace_transform(exp(-a*s)/s, s, t)
    Heaviside(-a + t)

    See Also
    ========

    laplace_transform
    hankel_transform, inverse_hankel_transform
    """
    ...

