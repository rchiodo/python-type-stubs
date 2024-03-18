from typing import Any, Literal
from sympy.core.basic import Basic
from sympy.core.logic import And
from sympy.core.relational import Equality, Ne, Relational
from sympy.integrals.integrals import Integral
import sympy.integrals.laplace as _laplace
from sympy.core.function import Function, UndefinedFunction
from sympy.functions.elementary.trigonometric import cos, sin
from sympy.series.order import Order

""" Integral Transforms """
class IntegralTransformError(NotImplementedError):
    """
    Exception raised in relation to problems computing transforms.

    Explanation
    ===========

    This class is mostly used internally; if integrals cannot be computed
    objects representing unevaluated transforms are usually returned.

    The hint ``needeval=True`` can be used to disable returning transform
    objects, and instead raise this exception if an integral cannot be
    computed.
    """
    def __init__(self, transform, function, msg) -> None:
        ...
    


class IntegralTransform(Function):
    """
    Base class for integral transforms.

    Explanation
    ===========

    This class represents unevaluated transforms.

    To implement a concrete transform, derive from this class and implement
    the ``_compute_transform(f, x, s, **hints)`` and ``_as_integral(f, x, s)``
    functions. If the transform cannot be computed, raise :obj:`IntegralTransformError`.

    Also set ``cls._name``. For instance,

    >>> from sympy import LaplaceTransform
    >>> LaplaceTransform._name
    'Laplace'

    Implement ``self._collapse_extra`` if your function returns more than just a
    number and possibly a convergence condition.
    """
    @property
    def function(self) -> Basic:
        """ The function to be transformed. """
        ...
    
    @property
    def function_variable(self) -> Basic:
        """ The dependent variable of the function to be transformed. """
        ...
    
    @property
    def transform_variable(self) -> Basic:
        """ The independent transform variable. """
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        """
        This method returns the symbols that will exist when the transform
        is evaluated.
        """
        ...
    
    def doit(self, **hints) -> Order | tuple[Any | Order, *tuple[Any, ...]] | tuple[Any | Order, Any | And]:
        """
        Try to evaluate the transform in closed form.

        Explanation
        ===========

        This general function handles linearity, but apart from that leaves
        pretty much everything to _compute_transform.

        Standard hints are the following:

        - ``simplify``: whether or not to simplify the result
        - ``noconds``: if True, do not return convergence conditions
        - ``needeval``: if True, raise IntegralTransformError instead of
                        returning IntegralTransform objects

        The default values of these hints depend on the concrete transform,
        usually the default is
        ``(simplify, noconds, needeval) = (True, False, False)``.
        """
        ...
    
    @property
    def as_integral(self):
        ...
    


_noconds = ...
class MellinTransform(IntegralTransform):
    """
    Class representing unevaluated Mellin transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Mellin transforms, see the :func:`mellin_transform`
    docstring.
    """
    _name = ...


def mellin_transform(f, x, s, **hints):
    r"""
    Compute the Mellin transform `F(s)` of `f(x)`,

    .. math :: F(s) = \int_0^\infty x^{s-1} f(x) \mathrm{d}x.

    For all "sensible" functions, this converges absolutely in a strip
      `a < \operatorname{Re}(s) < b`.

    Explanation
    ===========

    The Mellin transform is related via change of variables to the Fourier
    transform, and also to the (bilateral) Laplace transform.

    This function returns ``(F, (a, b), cond)``
    where ``F`` is the Mellin transform of ``f``, ``(a, b)`` is the fundamental strip
    (as above), and ``cond`` are auxiliary convergence conditions.

    If the integral cannot be computed in closed form, this function returns
    an unevaluated :class:`MellinTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`. If ``noconds=False``,
    then only `F` will be returned (i.e. not ``cond``, and also not the strip
    ``(a, b)``).

    Examples
    ========

    >>> from sympy import mellin_transform, exp
    >>> from sympy.abc import x, s
    >>> mellin_transform(exp(-x), x, s)
    (gamma(s), (0, oo), True)

    See Also
    ========

    inverse_mellin_transform, laplace_transform, fourier_transform
    hankel_transform, inverse_hankel_transform
    """
    ...

class MellinTransformStripError(ValueError):
    """
    Exception raised by _rewrite_gamma. Mainly for internal use.
    """
    ...


_allowed = ...
class InverseMellinTransform(IntegralTransform):
    """
    Class representing unevaluated inverse Mellin transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Mellin transforms, see the
    :func:`inverse_mellin_transform` docstring.
    """
    _name = ...
    _none_sentinel = ...
    _c = ...
    def __new__(cls, F, s, x, a, b, **opts) -> type[UndefinedFunction]:
        ...
    
    @property
    def fundamental_strip(self) -> tuple[Basic | None, Basic | None]:
        ...
    


def inverse_mellin_transform(F, s, x, strip, **hints):
    r"""
    Compute the inverse Mellin transform of `F(s)` over the fundamental
    strip given by ``strip=(a, b)``.

    Explanation
    ===========

    This can be defined as

    .. math:: f(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} x^{-s} F(s) \mathrm{d}s,

    for any `c` in the fundamental strip. Under certain regularity
    conditions on `F` and/or `f`,
    this recovers `f` from its Mellin transform `F`
    (and vice versa), for positive real `x`.

    One of `a` or `b` may be passed as ``None``; a suitable `c` will be
    inferred.

    If the integral cannot be computed in closed form, this function returns
    an unevaluated :class:`InverseMellinTransform` object.

    Note that this function will assume x to be positive and real, regardless
    of the SymPy assumptions!

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.

    Examples
    ========

    >>> from sympy import inverse_mellin_transform, oo, gamma
    >>> from sympy.abc import x, s
    >>> inverse_mellin_transform(gamma(s), s, x, (0, oo))
    exp(-x)

    The fundamental strip matters:

    >>> f = 1/(s**2 - 1)
    >>> inverse_mellin_transform(f, s, x, (-oo, -1))
    x*(1 - 1/x**2)*Heaviside(x - 1)/2
    >>> inverse_mellin_transform(f, s, x, (-1, 1))
    -x*Heaviside(1 - x)/2 - Heaviside(x - 1)/(2*x)
    >>> inverse_mellin_transform(f, s, x, (1, oo))
    (1/2 - x**2/2)*Heaviside(1 - x)/x

    See Also
    ========

    mellin_transform
    hankel_transform, inverse_hankel_transform
    """
    ...

class FourierTypeTransform(IntegralTransform):
    """ Base class for Fourier transforms."""
    def a(self):
        ...
    
    def b(self):
        ...
    


class FourierTransform(FourierTypeTransform):
    """
    Class representing unevaluated Fourier transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Fourier transforms, see the :func:`fourier_transform`
    docstring.
    """
    _name = ...
    def a(self) -> Literal[1]:
        ...
    
    def b(self):
        ...
    


def fourier_transform(f, x, k, **hints):
    r"""
    Compute the unitary, ordinary-frequency Fourier transform of ``f``, defined
    as

    .. math:: F(k) = \int_{-\infty}^\infty f(x) e^{-2\pi i x k} \mathrm{d} x.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`FourierTransform` object.

    For other Fourier transform conventions, see the function
    :func:`sympy.integrals.transforms._fourier_transform`.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import fourier_transform, exp
    >>> from sympy.abc import x, k
    >>> fourier_transform(exp(-x**2), x, k)
    sqrt(pi)*exp(-pi**2*k**2)
    >>> fourier_transform(exp(-x**2), x, k, noconds=False)
    (sqrt(pi)*exp(-pi**2*k**2), True)

    See Also
    ========

    inverse_fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    """
    ...

class InverseFourierTransform(FourierTypeTransform):
    """
    Class representing unevaluated inverse Fourier transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Fourier transforms, see the
    :func:`inverse_fourier_transform` docstring.
    """
    _name = ...
    def a(self) -> Literal[1]:
        ...
    
    def b(self):
        ...
    


def inverse_fourier_transform(F, k, x, **hints):
    r"""
    Compute the unitary, ordinary-frequency inverse Fourier transform of `F`,
    defined as

    .. math:: f(x) = \int_{-\infty}^\infty F(k) e^{2\pi i x k} \mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseFourierTransform` object.

    For other Fourier transform conventions, see the function
    :func:`sympy.integrals.transforms._fourier_transform`.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import inverse_fourier_transform, exp, sqrt, pi
    >>> from sympy.abc import x, k
    >>> inverse_fourier_transform(sqrt(pi)*exp(-(pi*k)**2), k, x)
    exp(-x**2)
    >>> inverse_fourier_transform(sqrt(pi)*exp(-(pi*k)**2), k, x, noconds=False)
    (exp(-x**2), True)

    See Also
    ========

    fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    """
    ...

class SineCosineTypeTransform(IntegralTransform):
    """
    Base class for sine and cosine transforms.
    Specify cls._kern.
    """
    def a(self):
        ...
    
    def b(self):
        ...
    


class SineTransform(SineCosineTypeTransform):
    """
    Class representing unevaluated sine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute sine transforms, see the :func:`sine_transform`
    docstring.
    """
    _name = ...
    _kern = sin
    def a(self):
        ...
    
    def b(self):
        ...
    


def sine_transform(f, x, k, **hints):
    r"""
    Compute the unitary, ordinary-frequency sine transform of `f`, defined
    as

    .. math:: F(k) = \sqrt{\frac{2}{\pi}} \int_{0}^\infty f(x) \sin(2\pi x k) \mathrm{d} x.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`SineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import sine_transform, exp
    >>> from sympy.abc import x, k, a
    >>> sine_transform(x*exp(-a*x**2), x, k)
    sqrt(2)*k*exp(-k**2/(4*a))/(4*a**(3/2))
    >>> sine_transform(x**(-a), x, k)
    2**(1/2 - a)*k**(a - 1)*gamma(1 - a/2)/gamma(a/2 + 1/2)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    """
    ...

class InverseSineTransform(SineCosineTypeTransform):
    """
    Class representing unevaluated inverse sine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse sine transforms, see the
    :func:`inverse_sine_transform` docstring.
    """
    _name = ...
    _kern = sin
    def a(self):
        ...
    
    def b(self):
        ...
    


def inverse_sine_transform(F, k, x, **hints):
    r"""
    Compute the unitary, ordinary-frequency inverse sine transform of `F`,
    defined as

    .. math:: f(x) = \sqrt{\frac{2}{\pi}} \int_{0}^\infty F(k) \sin(2\pi x k) \mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseSineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import inverse_sine_transform, exp, sqrt, gamma
    >>> from sympy.abc import x, k, a
    >>> inverse_sine_transform(2**((1-2*a)/2)*k**(a - 1)*
    ...     gamma(-a/2 + 1)/gamma((a+1)/2), k, x)
    x**(-a)
    >>> inverse_sine_transform(sqrt(2)*k*exp(-k**2/(4*a))/(4*sqrt(a)**3), k, x)
    x*exp(-a*x**2)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    """
    ...

class CosineTransform(SineCosineTypeTransform):
    """
    Class representing unevaluated cosine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute cosine transforms, see the :func:`cosine_transform`
    docstring.
    """
    _name = ...
    _kern = cos
    def a(self):
        ...
    
    def b(self):
        ...
    


def cosine_transform(f, x, k, **hints):
    r"""
    Compute the unitary, ordinary-frequency cosine transform of `f`, defined
    as

    .. math:: F(k) = \sqrt{\frac{2}{\pi}} \int_{0}^\infty f(x) \cos(2\pi x k) \mathrm{d} x.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`CosineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import cosine_transform, exp, sqrt, cos
    >>> from sympy.abc import x, k, a
    >>> cosine_transform(exp(-a*x), x, k)
    sqrt(2)*a/(sqrt(pi)*(a**2 + k**2))
    >>> cosine_transform(exp(-a*sqrt(x))*cos(a*sqrt(x)), x, k)
    a*exp(-a**2/(2*k))/(2*k**(3/2))

    See Also
    ========

    fourier_transform, inverse_fourier_transform,
    sine_transform, inverse_sine_transform
    inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    """
    ...

class InverseCosineTransform(SineCosineTypeTransform):
    """
    Class representing unevaluated inverse cosine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse cosine transforms, see the
    :func:`inverse_cosine_transform` docstring.
    """
    _name = ...
    _kern = cos
    def a(self):
        ...
    
    def b(self):
        ...
    


def inverse_cosine_transform(F, k, x, **hints):
    r"""
    Compute the unitary, ordinary-frequency inverse cosine transform of `F`,
    defined as

    .. math:: f(x) = \sqrt{\frac{2}{\pi}} \int_{0}^\infty F(k) \cos(2\pi x k) \mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseCosineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import inverse_cosine_transform, sqrt, pi
    >>> from sympy.abc import x, k, a
    >>> inverse_cosine_transform(sqrt(2)*a/(sqrt(pi)*(a**2 + k**2)), k, x)
    exp(-a*x)
    >>> inverse_cosine_transform(1/sqrt(k), k, x)
    1/sqrt(x)

    See Also
    ========

    fourier_transform, inverse_fourier_transform,
    sine_transform, inverse_sine_transform
    cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    """
    ...

class HankelTypeTransform(IntegralTransform):
    """
    Base class for Hankel transforms.
    """
    def doit(self, **hints) -> tuple[Any | Equality | Relational | Ne, Any] | tuple[Any, Any]:
        ...
    
    @property
    def as_integral(self) -> Equality | Relational | Ne | Integral:
        ...
    


class HankelTransform(HankelTypeTransform):
    """
    Class representing unevaluated Hankel transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Hankel transforms, see the :func:`hankel_transform`
    docstring.
    """
    _name = ...


def hankel_transform(f, r, k, nu, **hints):
    r"""
    Compute the Hankel transform of `f`, defined as

    .. math:: F_\nu(k) = \int_{0}^\infty f(r) J_\nu(k r) r \mathrm{d} r.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`HankelTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import hankel_transform, inverse_hankel_transform
    >>> from sympy import exp
    >>> from sympy.abc import r, k, m, nu, a

    >>> ht = hankel_transform(1/r**m, r, k, nu)
    >>> ht
    2*k**(m - 2)*gamma(-m/2 + nu/2 + 1)/(2**m*gamma(m/2 + nu/2))

    >>> inverse_hankel_transform(ht, k, r, nu)
    r**(-m)

    >>> ht = hankel_transform(exp(-a*r), r, k, 0)
    >>> ht
    a/(k**3*(a**2/k**2 + 1)**(3/2))

    >>> inverse_hankel_transform(ht, k, r, 0)
    exp(-a*r)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    inverse_hankel_transform
    mellin_transform, laplace_transform
    """
    ...

class InverseHankelTransform(HankelTypeTransform):
    """
    Class representing unevaluated inverse Hankel transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Hankel transforms, see the
    :func:`inverse_hankel_transform` docstring.
    """
    _name = ...


def inverse_hankel_transform(F, k, r, nu, **hints):
    r"""
    Compute the inverse Hankel transform of `F` defined as

    .. math:: f(r) = \int_{0}^\infty F_\nu(k) J_\nu(k r) k \mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseHankelTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import hankel_transform, inverse_hankel_transform
    >>> from sympy import exp
    >>> from sympy.abc import r, k, m, nu, a

    >>> ht = hankel_transform(1/r**m, r, k, nu)
    >>> ht
    2*k**(m - 2)*gamma(-m/2 + nu/2 + 1)/(2**m*gamma(m/2 + nu/2))

    >>> inverse_hankel_transform(ht, k, r, nu)
    r**(-m)

    >>> ht = hankel_transform(exp(-a*r), r, k, 0)
    >>> ht
    a/(k**3*(a**2/k**2 + 1)**(3/2))

    >>> inverse_hankel_transform(ht, k, r, 0)
    exp(-a*r)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform
    mellin_transform, laplace_transform
    """
    ...

LaplaceTransform = _laplace.LaplaceTransform
laplace_transform = ...
laplace_correspondence = ...
laplace_initial_conds = ...
InverseLaplaceTransform = _laplace.InverseLaplaceTransform
inverse_laplace_transform = ...
