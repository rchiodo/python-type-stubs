from types import NotImplementedType
from typing import Any, Callable, Literal, Never, Self
from sympy.external.gmpy import GROUND_TYPES
from sympy.core.sympify import CantSympify
from sympy.polys.polyutils import PicklableWithSlots
from sympy.polys.domains import Domain

"""OO layer for several polynomial representations. """
_flint_domains: tuple[Domain, ...]
if GROUND_TYPES == 'flint':
    _flint_domains = ...
else:
    flint = ...
    _flint_domains = ...
class DMP(CantSympify):
    """Dense Multivariate Polynomials over `K`. """
    __slots__ = ...
    def __new__(cls, rep, dom, lev=...) -> DUP_Flint | DMP_Python:
        ...
    
    @classmethod
    def new(cls, rep, dom, lev) -> DUP_Flint | DMP_Python:
        ...
    
    @property
    def rep(f):
        """Get the representation of ``f``. """
        ...
    
    def to_best(f) -> DUP_Flint | DMP_Python | DMP | Self:
        """Convert to DUP_Flint if possible.

        This method should be used when the domain or level is changed and it
        potentially becomes possible to convert from DMP_Python to DUP_Flint.
        """
        ...
    
    @classmethod
    def from_dict(cls, rep, lev, dom) -> DUP_Flint | DMP_Python:
        ...
    
    @classmethod
    def from_list(cls, rep, lev, dom) -> DUP_Flint | DMP_Python:
        """Create an instance of ``cls`` given a list of native coefficients. """
        ...
    
    @classmethod
    def from_sympy_list(cls, rep, lev, dom) -> DUP_Flint | DMP_Python:
        """Create an instance of ``cls`` given a list of SymPy coefficients. """
        ...
    
    @classmethod
    def from_monoms_coeffs(cls, monoms, coeffs, lev, dom) -> Self:
        ...
    
    def convert(f, dom) -> Self | DUP_Flint:
        """Convert ``f`` to a ``DMP`` over the new domain. """
        ...
    
    @classmethod
    def zero(cls, lev, dom) -> DUP_Flint | DMP_Python:
        ...
    
    @classmethod
    def one(cls, lev, dom) -> DUP_Flint | DMP_Python:
        ...
    
    def __repr__(f) -> str:
        ...
    
    def __hash__(f) -> int:
        ...
    
    def __getnewargs__(self) -> tuple[Any, Any, Any]:
        ...
    
    def ground_new(f, coeff):
        """Construct a new ground instance of ``f``. """
        ...
    
    def unify_DMP(f, g) -> tuple[Self | Any | DUP_Flint, DMP | Any | DUP_Flint | Self]:
        """Unify and return ``DMP`` instances of ``f`` and ``g``. """
        ...
    
    def to_dict(f, zero=...) -> dict[tuple[Literal[0]], Any] | dict[Any, Any]:
        """Convert ``f`` to a dict representation with native coefficients. """
        ...
    
    def to_sympy_dict(f, zero=...) -> dict[tuple[Literal[0]], Any] | dict[Any, Any]:
        """Convert ``f`` to a dict representation with SymPy coefficients. """
        ...
    
    def to_sympy_list(f) -> list[Any]:
        """Convert ``f`` to a list representation with SymPy coefficients. """
        ...
    
    def to_list(f):
        """Convert ``f`` to a list representation with native coefficients. """
        ...
    
    def to_tuple(f):
        """
        Convert ``f`` to a tuple representation with native coefficients.

        This is needed for hashing.
        """
        ...
    
    def to_ring(f) -> Self | DUP_Flint:
        """Make the ground domain a ring. """
        ...
    
    def to_field(f) -> Self | DUP_Flint:
        """Make the ground domain a field. """
        ...
    
    def to_exact(f) -> Self | DUP_Flint:
        """Make the ground domain exact. """
        ...
    
    def slice(f, m, n, j=...):
        """Take a continuous subsequence of terms of ``f``. """
        ...
    
    def coeffs(f, order=...) -> list[Any]:
        """Returns all non-zero coefficients from ``f`` in lex order. """
        ...
    
    def monoms(f, order=...) -> list[Any]:
        """Returns all non-zero monomials from ``f`` in lex order. """
        ...
    
    def terms(f, order=...) -> list[tuple[Any, Any]]:
        """Returns all non-zero terms from ``f`` in lex order. """
        ...
    
    def all_coeffs(f) -> list[Any]:
        """Returns all coefficients from ``f``. """
        ...
    
    def all_monoms(f) -> list[tuple[Literal[0]]] | list[tuple[Any]]:
        """Returns all monomials from ``f``. """
        ...
    
    def all_terms(f) -> list[tuple[tuple[Literal[0]], Any]] | list[tuple[tuple[Any], Any]]:
        """Returns all terms from a ``f``. """
        ...
    
    def lift(f):
        """Convert algebraic coefficients to rationals. """
        ...
    
    def deflate(f):
        """Reduce degree of `f` by mapping `x_i^m` to `y_i`. """
        ...
    
    def inject(f, front=...):
        """Inject ground domain generators into ``f``. """
        ...
    
    def eject(f, dom, front=...):
        """Eject selected generators into the ground domain. """
        ...
    
    def exclude(f) -> tuple[Any, Any]:
        r"""
        Remove useless generators from ``f``.

        Returns the removed generators and the new excluded ``f``.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMP
        >>> from sympy.polys.domains import ZZ

        >>> DMP([[[ZZ(1)]], [[ZZ(1)], [ZZ(2)]]], ZZ).exclude()
        ([2], DMP_Python([[1], [1, 2]], ZZ))

        """
        ...
    
    def permute(f, P):
        r"""
        Returns a polynomial in `K[x_{P(1)}, ..., x_{P(n)}]`.

        Examples
        ========

        >>> from sympy.polys.polyclasses import DMP
        >>> from sympy.polys.domains import ZZ

        >>> DMP([[[ZZ(2)], [ZZ(1), ZZ(0)]], [[]]], ZZ).permute([1, 0, 2])
        DMP_Python([[[2], []], [[1, 0], []]], ZZ)

        >>> DMP([[[ZZ(2)], [ZZ(1), ZZ(0)]], [[]]], ZZ).permute([1, 2, 0])
        DMP_Python([[[1], []], [[2, 0], []]], ZZ)

        """
        ...
    
    def terms_gcd(f):
        """Remove GCD of terms from the polynomial ``f``. """
        ...
    
    def abs(f):
        """Make all coefficients in ``f`` positive. """
        ...
    
    def neg(f):
        """Negate all coefficients in ``f``. """
        ...
    
    def add_ground(f, c):
        """Add an element of the ground domain to ``f``. """
        ...
    
    def sub_ground(f, c):
        """Subtract an element of the ground domain from ``f``. """
        ...
    
    def mul_ground(f, c):
        """Multiply ``f`` by a an element of the ground domain. """
        ...
    
    def quo_ground(f, c):
        """Quotient of ``f`` by a an element of the ground domain. """
        ...
    
    def exquo_ground(f, c):
        """Exact quotient of ``f`` by a an element of the ground domain. """
        ...
    
    def add(f, g) -> Self:
        """Add two multivariate polynomials ``f`` and ``g``. """
        ...
    
    def sub(f, g) -> Self:
        """Subtract two multivariate polynomials ``f`` and ``g``. """
        ...
    
    def mul(f, g) -> Self:
        """Multiply two multivariate polynomials ``f`` and ``g``. """
        ...
    
    def sqr(f):
        """Square a multivariate polynomial ``f``. """
        ...
    
    def pow(f, n):
        """Raise ``f`` to a non-negative power ``n``. """
        ...
    
    def pdiv(f, g) -> tuple[Self, Self]:
        """Polynomial pseudo-division of ``f`` and ``g``. """
        ...
    
    def prem(f, g) -> Self:
        """Polynomial pseudo-remainder of ``f`` and ``g``. """
        ...
    
    def pquo(f, g) -> Self:
        """Polynomial pseudo-quotient of ``f`` and ``g``. """
        ...
    
    def pexquo(f, g) -> Self:
        """Polynomial exact pseudo-quotient of ``f`` and ``g``. """
        ...
    
    def div(f, g) -> tuple[Self, Self] | tuple[DUP_Flint, DUP_Flint]:
        """Polynomial division with remainder of ``f`` and ``g``. """
        ...
    
    def rem(f, g) -> Self:
        """Computes polynomial remainder of ``f`` and ``g``. """
        ...
    
    def quo(f, g) -> Self:
        """Computes polynomial quotient of ``f`` and ``g``. """
        ...
    
    def exquo(f, g) -> DUP_Flint | Self:
        """Computes polynomial exact quotient of ``f`` and ``g``. """
        ...
    
    def degree(f, j=...):
        """Returns the leading degree of ``f`` in ``x_j``. """
        ...
    
    def degree_list(f):
        """Returns a list of degrees of ``f``. """
        ...
    
    def total_degree(f):
        """Returns the total degree of ``f``. """
        ...
    
    def homogenize(f, s) -> DUP_Flint | DMP_Python:
        """Return homogeneous polynomial of ``f``"""
        ...
    
    def homogeneous_order(f) -> int | None:
        """Returns the homogeneous order of ``f``. """
        ...
    
    def LC(f):
        """Returns the leading coefficient of ``f``. """
        ...
    
    def TC(f):
        """Returns the trailing coefficient of ``f``. """
        ...
    
    def nth(f, *N):
        """Returns the ``n``-th coefficient of ``f``. """
        ...
    
    def max_norm(f):
        """Returns maximum norm of ``f``. """
        ...
    
    def l1_norm(f):
        """Returns l1 norm of ``f``. """
        ...
    
    def l2_norm_squared(f):
        """Return squared l2 norm of ``f``. """
        ...
    
    def clear_denoms(f):
        """Clear denominators, but keep the ground domain. """
        ...
    
    def integrate(f, m=..., j=...):
        """Computes the ``m``-th order indefinite integral of ``f`` in ``x_j``. """
        ...
    
    def diff(f, m=..., j=...):
        """Computes the ``m``-th order derivative of ``f`` in ``x_j``. """
        ...
    
    def eval(f, a, j=...):
        """Evaluates ``f`` at the given point ``a`` in ``x_j``. """
        ...
    
    def half_gcdex(f, g) -> tuple[DUP_Flint, DUP_Flint] | tuple[Self, Self]:
        """Half extended Euclidean algorithm, if univariate. """
        ...
    
    def gcdex(f, g) -> tuple[Self, Self, Self]:
        """Extended Euclidean algorithm, if univariate. """
        ...
    
    def invert(f, g) -> Self | DUP_Flint:
        """Invert ``f`` modulo ``g``, if possible. """
        ...
    
    def revert(f, n):
        """Compute ``f**(-1)`` mod ``x**n``. """
        ...
    
    def subresultants(f, g) -> list[DUP_Flint] | list[Self]:
        """Computes subresultant PRS sequence of ``f`` and ``g``. """
        ...
    
    def resultant(f, g, includePRS=...) -> tuple[DUP_Flint | DMP_Python | Any | list[list[Any]] | list[Any], list[DUP_Flint]] | tuple[DUP_Flint | DMP_Python | Any | list[list[Any]] | list[Any], list[Self]] | DUP_Flint | DMP_Python | tuple[Any, list[Any]] | tuple[list[list[Any]], list[Any]] | tuple[list[list[Any]] | Any | list[Any], list[Any]] | list[list[Any]] | list[Any]:
        """Computes resultant of ``f`` and ``g`` via PRS. """
        ...
    
    def discriminant(f):
        """Computes discriminant of ``f``. """
        ...
    
    def cofactors(f, g) -> tuple[Any | DUP_Flint, DUP_Flint | Any | Self, Any] | tuple[Self, Self, Self]:
        """Returns GCD of ``f`` and ``g`` and their cofactors. """
        ...
    
    def gcd(f, g) -> Self:
        """Returns polynomial GCD of ``f`` and ``g``. """
        ...
    
    def lcm(f, g) -> Self | DUP_Flint:
        """Returns polynomial LCM of ``f`` and ``g``. """
        ...
    
    def cancel(f, g, include=...) -> tuple[DUP_Flint | Any, Any] | tuple[Self, Self] | tuple[Any, Any, Self | Any | DUP_Flint, Any]:
        """Cancel common factors in a rational function ``f/g``. """
        ...
    
    def trunc(f, p):
        """Reduce ``f`` modulo a constant ``p``. """
        ...
    
    def monic(f):
        """Divides all coefficients by ``LC(f)``. """
        ...
    
    def content(f):
        """Returns GCD of polynomial coefficients. """
        ...
    
    def primitive(f):
        """Returns content and a primitive form of ``f``. """
        ...
    
    def compose(f, g) -> Self:
        """Computes functional composition of ``f`` and ``g``. """
        ...
    
    def decompose(f):
        """Computes functional decomposition of ``f``. """
        ...
    
    def shift(f, a):
        """Efficiently compute Taylor shift ``f(x + a)``. """
        ...
    
    def transform(f, p, q) -> Self:
        """Evaluate functional transformation ``q**n * f(p/q)``."""
        ...
    
    def sturm(f):
        """Computes the Sturm sequence of ``f``. """
        ...
    
    def cauchy_upper_bound(f):
        """Computes the Cauchy upper bound on the roots of ``f``. """
        ...
    
    def cauchy_lower_bound(f):
        """Computes the Cauchy lower bound on the nonzero roots of ``f``. """
        ...
    
    def mignotte_sep_bound_squared(f):
        """Computes the squared Mignotte bound on root separations of ``f``. """
        ...
    
    def gff_list(f):
        """Computes greatest factorial factorization of ``f``. """
        ...
    
    def norm(f):
        """Computes ``Norm(f)``."""
        ...
    
    def sqf_norm(f):
        """Computes square-free norm of ``f``. """
        ...
    
    def sqf_part(f):
        """Computes square-free part of ``f``. """
        ...
    
    def sqf_list(f, all=...):
        """Returns a list of square-free factors of ``f``. """
        ...
    
    def sqf_list_include(f, all=...):
        """Returns a list of square-free factors of ``f``. """
        ...
    
    def factor_list(f):
        """Returns a list of irreducible factors of ``f``. """
        ...
    
    def factor_list_include(f):
        """Returns a list of irreducible factors of ``f``. """
        ...
    
    def intervals(f, all=..., eps=..., inf=..., sup=..., fast=..., sqf=...):
        """Compute isolating intervals for roots of ``f``. """
        ...
    
    def refine_root(f, s, t, eps=..., steps=..., fast=...):
        """
        Refine an isolating interval to the given precision.

        ``eps`` should be a rational number.

        """
        ...
    
    def count_real_roots(f, inf=..., sup=...):
        """Return the number of real roots of ``f`` in ``[inf, sup]``. """
        ...
    
    def count_complex_roots(f, inf=..., sup=...):
        """Return the number of complex roots of ``f`` in ``[inf, sup]``. """
        ...
    
    @property
    def is_zero(f):
        """Returns ``True`` if ``f`` is a zero polynomial. """
        ...
    
    @property
    def is_one(f):
        """Returns ``True`` if ``f`` is a unit polynomial. """
        ...
    
    @property
    def is_ground(f):
        """Returns ``True`` if ``f`` is an element of the ground domain. """
        ...
    
    @property
    def is_sqf(f):
        """Returns ``True`` if ``f`` is a square-free polynomial. """
        ...
    
    @property
    def is_monic(f):
        """Returns ``True`` if the leading coefficient of ``f`` is one. """
        ...
    
    @property
    def is_primitive(f):
        """Returns ``True`` if the GCD of the coefficients of ``f`` is one. """
        ...
    
    @property
    def is_linear(f):
        """Returns ``True`` if ``f`` is linear in all its variables. """
        ...
    
    @property
    def is_quadratic(f):
        """Returns ``True`` if ``f`` is quadratic in all its variables. """
        ...
    
    @property
    def is_monomial(f):
        """Returns ``True`` if ``f`` is zero or has only one term. """
        ...
    
    @property
    def is_homogeneous(f):
        """Returns ``True`` if ``f`` is a homogeneous polynomial. """
        ...
    
    @property
    def is_irreducible(f):
        """Returns ``True`` if ``f`` has no factors over its domain. """
        ...
    
    @property
    def is_cyclotomic(f):
        """Returns ``True`` if ``f`` is a cyclotomic polynomial. """
        ...
    
    def __abs__(f):
        ...
    
    def __neg__(f):
        ...
    
    def __add__(f, g) -> Self | NotImplementedType:
        ...
    
    def __radd__(f, g) -> Self | NotImplementedType:
        ...
    
    def __sub__(f, g) -> Self | NotImplementedType:
        ...
    
    def __rsub__(f, g):
        ...
    
    def __mul__(f, g) -> Self | NotImplementedType:
        ...
    
    def __rmul__(f, g) -> Self | NotImplementedType:
        ...
    
    def __truediv__(f, g) -> DUP_Flint | Self | NotImplementedType:
        ...
    
    def __rtruediv__(f, g) -> DUP_Flint | Self | NotImplementedType:
        ...
    
    def __pow__(f, n):
        ...
    
    def __divmod__(f, g) -> tuple[Self, Self] | tuple[DUP_Flint, DUP_Flint]:
        ...
    
    def __mod__(f, g) -> Self:
        ...
    
    def __floordiv__(f, g) -> Self | NotImplementedType:
        ...
    
    def __eq__(f, g) -> bool:
        ...
    
    def eq(f, g, strict=...):
        ...
    
    def ne(f, g, strict=...) -> bool:
        ...
    
    def __lt__(f, g) -> bool:
        ...
    
    def __le__(f, g) -> bool:
        ...
    
    def __gt__(f, g) -> bool:
        ...
    
    def __ge__(f, g) -> bool:
        ...
    
    def __bool__(f) -> bool:
        ...
    


class DMP_Python(DMP):
    """Dense Multivariate Polynomials over `K`. """
    __slots__ = ...
    def per(f, rep) -> Self:
        """Create a DMP out of the given representation. """
        ...
    
    def ground_new(f, coeff) -> Self:
        """Construct a new ground instance of ``f``. """
        ...
    
    def unify(f, g) -> tuple[Any, Any, Callable[..., Self], Any, Any] | tuple[Any, Any, Callable[..., Self], Any | list[Any] | list[list[Any]], Any | list[Any] | list[list[Any]]]:
        """Unify representations of two multivariate polynomials. """
        ...
    
    def to_DUP_Flint(f) -> DUP_Flint:
        """Convert ``f`` to a Flint representation. """
        ...
    
    def to_list(f) -> list[Any]:
        """Convert ``f`` to a list representation with native coefficients. """
        ...
    
    def to_tuple(f) -> tuple[Any, ...]:
        """Convert ``f`` to a tuple representation with native coefficients. """
        ...
    
    def deflate(f) -> tuple[tuple[Literal[1], ...] | tuple[Any, ...], Self]:
        """Reduce degree of `f` by mapping `x_i^m` to `y_i`. """
        ...
    
    def inject(f, front=...) -> Self:
        """Inject ground domain generators into ``f``. """
        ...
    
    def eject(f, dom, front=...) -> Self:
        """Eject selected generators into the ground domain. """
        ...
    
    def terms_gcd(f) -> tuple[tuple[Literal[0], ...] | tuple[Any, ...], Self]:
        """Remove GCD of terms from the polynomial ``f``. """
        ...
    
    def abs(f) -> Self:
        """Make all coefficients in ``f`` positive. """
        ...
    
    def neg(f) -> Self:
        """Negate all coefficients in ``f``. """
        ...
    
    def sqr(f) -> Self:
        """Square a multivariate polynomial ``f``. """
        ...
    
    def degree_list(f) -> tuple[Any, ...]:
        """Returns a list of degrees of ``f``. """
        ...
    
    def total_degree(f) -> int:
        """Returns the total degree of ``f``. """
        ...
    
    def LC(f):
        """Returns the leading coefficient of ``f``. """
        ...
    
    def TC(f):
        """Returns the trailing coefficient of ``f``. """
        ...
    
    def max_norm(f):
        """Returns maximum norm of ``f``. """
        ...
    
    def l1_norm(f) -> int:
        """Returns l1 norm of ``f``. """
        ...
    
    def l2_norm_squared(f) -> int:
        """Return squared l2 norm of ``f``. """
        ...
    
    def clear_denoms(f) -> tuple[Any, Self]:
        """Clear denominators, but keep the ground domain. """
        ...
    
    def discriminant(f) -> DUP_Flint | DMP_Python | list[list[Any]] | list[Any]:
        """Computes discriminant of ``f``. """
        ...
    
    def monic(f) -> Self:
        """Divides all coefficients by ``LC(f)``. """
        ...
    
    def content(f):
        """Returns GCD of polynomial coefficients. """
        ...
    
    def primitive(f) -> tuple[Any, Self]:
        """Returns content and a primitive form of ``f``. """
        ...
    
    def norm(f) -> DUP_Flint | DMP_Python:
        """Computes ``Norm(f)``."""
        ...
    
    def sqf_norm(f) -> tuple[int, Self, DUP_Flint | DMP_Python]:
        """Computes square-free norm of ``f``. """
        ...
    
    def sqf_part(f) -> Self:
        """Computes square-free part of ``f``. """
        ...
    
    def sqf_list(f, all=...) -> tuple[Any, list[tuple[Self, Any]]]:
        """Returns a list of square-free factors of ``f``. """
        ...
    
    def sqf_list_include(f, all=...) -> list[tuple[Self, Literal[1]]]:
        """Returns a list of square-free factors of ``f``. """
        ...
    
    def factor_list(f) -> tuple[Any, list[tuple[Self, Any]]]:
        """Returns a list of irreducible factors of ``f``. """
        ...
    
    def factor_list_include(f) -> list[tuple[Self, Any | Literal[1]]]:
        """Returns a list of irreducible factors of ``f``. """
        ...
    
    def count_real_roots(f, inf=..., sup=...) -> int:
        """Return the number of real roots of ``f`` in ``[inf, sup]``. """
        ...
    
    def count_complex_roots(f, inf=..., sup=...) -> int:
        """Return the number of complex roots of ``f`` in ``[inf, sup]``. """
        ...
    
    @property
    def is_zero(f) -> bool:
        """Returns ``True`` if ``f`` is a zero polynomial. """
        ...
    
    @property
    def is_one(f) -> bool:
        """Returns ``True`` if ``f`` is a unit polynomial. """
        ...
    
    @property
    def is_ground(f) -> bool:
        """Returns ``True`` if ``f`` is an element of the ground domain. """
        ...
    
    @property
    def is_sqf(f) -> bool:
        """Returns ``True`` if ``f`` is a square-free polynomial. """
        ...
    
    @property
    def is_monic(f):
        """Returns ``True`` if the leading coefficient of ``f`` is one. """
        ...
    
    @property
    def is_primitive(f):
        """Returns ``True`` if the GCD of the coefficients of ``f`` is one. """
        ...
    
    @property
    def is_linear(f) -> bool:
        """Returns ``True`` if ``f`` is linear in all its variables. """
        ...
    
    @property
    def is_quadratic(f) -> bool:
        """Returns ``True`` if ``f`` is quadratic in all its variables. """
        ...
    
    @property
    def is_monomial(f) -> bool:
        """Returns ``True`` if ``f`` is zero or has only one term. """
        ...
    
    @property
    def is_homogeneous(f) -> bool:
        """Returns ``True`` if ``f`` is a homogeneous polynomial. """
        ...
    
    @property
    def is_irreducible(f) -> bool:
        """Returns ``True`` if ``f`` has no factors over its domain. """
        ...
    
    @property
    def is_cyclotomic(f) -> bool:
        """Returns ``True`` if ``f`` is a cyclotomic polynomial. """
        ...
    


class DUP_Flint(DMP):
    """Dense Multivariate Polynomials over `K`. """
    lev = ...
    __slots__ = ...
    def __reduce__(self) -> tuple[type[Self], tuple[Any, Any, int]]:
        ...
    
    def to_list(f):
        """Convert ``f`` to a list representation with native coefficients. """
        ...
    
    @classmethod
    def from_rep(cls, rep, dom) -> Self:
        """Create a DMP from the given representation. """
        ...
    
    def ground_new(f, coeff) -> Self:
        """Construct a new ground instance of ``f``. """
        ...
    
    def unify(f, g):
        """Unify representations of two polynomials. """
        ...
    
    def to_DMP_Python(f) -> DMP_Python:
        """Convert ``f`` to a Python native representation. """
        ...
    
    def to_tuple(f) -> tuple[Any, ...]:
        """Convert ``f`` to a tuple representation with native coefficients. """
        ...
    
    def deflate(f) -> tuple[tuple[Literal[1]], Self] | tuple[tuple[Any], Self]:
        """Reduce degree of `f` by mapping `x_i^m` to `y_i`. """
        ...
    
    def inject(f, front=...):
        """Inject ground domain generators into ``f``. """
        ...
    
    def eject(f, dom, front=...):
        """Eject selected generators into the ground domain. """
        ...
    
    def terms_gcd(f) -> tuple[tuple[Literal[0], ...] | tuple[Any, ...], DUP_Flint]:
        """Remove GCD of terms from the polynomial ``f``. """
        ...
    
    def abs(f) -> DUP_Flint:
        """Make all coefficients in ``f`` positive. """
        ...
    
    def neg(f) -> Self:
        """Negate all coefficients in ``f``. """
        ...
    
    def sqr(f) -> Self:
        """Square a multivariate polynomial ``f``. """
        ...
    
    def degree_list(f) -> tuple[float | Any]:
        """Returns a list of degrees of ``f``. """
        ...
    
    def total_degree(f) -> float:
        """Returns the total degree of ``f``. """
        ...
    
    def LC(f):
        """Returns the leading coefficient of ``f``. """
        ...
    
    def TC(f):
        """Returns the trailing coefficient of ``f``. """
        ...
    
    def max_norm(f):
        """Returns maximum norm of ``f``. """
        ...
    
    def l1_norm(f) -> int:
        """Returns l1 norm of ``f``. """
        ...
    
    def l2_norm_squared(f) -> int:
        """Return squared l2 norm of ``f``. """
        ...
    
    def clear_denoms(f) -> tuple[Any, Self]:
        """Clear denominators, but keep the ground domain. """
        ...
    
    def discriminant(f) -> DUP_Flint | DMP_Python | list[list[Any]] | list[Any]:
        """Computes discriminant of ``f``. """
        ...
    
    def monic(f) -> Self:
        """Divides all coefficients by ``LC(f)``. """
        ...
    
    def content(f):
        """Returns GCD of polynomial coefficients. """
        ...
    
    def primitive(f) -> tuple[Any, Self]:
        """Returns content and a primitive form of ``f``. """
        ...
    
    def norm(f):
        """Computes ``Norm(f)``."""
        ...
    
    def sqf_norm(f):
        """Computes square-free norm of ``f``. """
        ...
    
    def sqf_part(f) -> Self | DUP_Flint:
        """Computes square-free part of ``f``. """
        ...
    
    def sqf_list(f, all=...) -> tuple[Any, list[tuple[DUP_Flint, Any]]]:
        """Returns a list of square-free factors of ``f``. """
        ...
    
    def sqf_list_include(f, all=...) -> list[tuple[DUP_Flint, Literal[1]]]:
        """Returns a list of square-free factors of ``f``. """
        ...
    
    def factor_list(f) -> tuple[Any, list[tuple[Self, Any]]]:
        """Returns a list of irreducible factors of ``f``. """
        ...
    
    def factor_list_include(f) -> list[tuple[DUP_Flint, Any | Literal[1]]]:
        """Returns a list of irreducible factors of ``f``. """
        ...
    
    def count_real_roots(f, inf=..., sup=...) -> int:
        """Return the number of real roots of ``f`` in ``[inf, sup]``. """
        ...
    
    def count_complex_roots(f, inf=..., sup=...) -> int:
        """Return the number of complex roots of ``f`` in ``[inf, sup]``. """
        ...
    
    @property
    def is_zero(f) -> bool:
        """Returns ``True`` if ``f`` is a zero polynomial. """
        ...
    
    @property
    def is_one(f):
        """Returns ``True`` if ``f`` is a unit polynomial. """
        ...
    
    @property
    def is_ground(f):
        """Returns ``True`` if ``f`` is an element of the ground domain. """
        ...
    
    @property
    def is_linear(f):
        """Returns ``True`` if ``f`` is linear in all its variables. """
        ...
    
    @property
    def is_quadratic(f):
        """Returns ``True`` if ``f`` is quadratic in all its variables. """
        ...
    
    @property
    def is_monomial(f) -> bool:
        """Returns ``True`` if ``f`` is zero or has only one term. """
        ...
    
    @property
    def is_monic(f):
        """Returns ``True`` if the leading coefficient of ``f`` is one. """
        ...
    
    @property
    def is_primitive(f):
        """Returns ``True`` if the GCD of the coefficients of ``f`` is one. """
        ...
    
    @property
    def is_homogeneous(f) -> bool:
        """Returns ``True`` if ``f`` is a homogeneous polynomial. """
        ...
    
    @property
    def is_sqf(f) -> bool:
        """Returns ``True`` if ``f`` is a square-free polynomial. """
        ...
    
    @property
    def is_irreducible(f) -> bool:
        """Returns ``True`` if ``f`` has no factors over its domain. """
        ...
    
    @property
    def is_cyclotomic(f) -> bool:
        """Returns ``True`` if ``f`` is a cyclotomic polynomial. """
        ...
    


def init_normal_DMF(num, den, lev, dom) -> DMF:
    ...

class DMF(PicklableWithSlots, CantSympify):
    """Dense Multivariate Fractions over `K`. """
    __slots__ = ...
    def __init__(self, rep, dom, lev=...) -> None:
        ...
    
    @classmethod
    def new(cls, rep, dom, lev=...) -> Self:
        ...
    
    def ground_new(self, rep) -> Self:
        ...
    
    def __repr__(f) -> str:
        ...
    
    def __hash__(f) -> int:
        ...
    
    def poly_unify(f, g) -> tuple[Any | int, Any, Callable[..., Any | Self], tuple[Any | list[Any], Any | list[Any]], Any] | tuple[Any | int, Any, Callable[..., Any | Self], tuple[Any | list[Any] | list[list[Any]], Any | list[Any] | list[list[Any]]], Any | list[Any] | list[list[Any]]]:
        """Unify a multivariate fraction and a polynomial. """
        ...
    
    def frac_unify(f, g) -> tuple[Any | int, Any, Callable[..., Any | Self], tuple[Any | list[Any], Any | list[Any]], tuple[Any | list[Any], Any | list[Any]]] | tuple[Any | int, Any, Callable[..., Any | Self], tuple[Any | list[Any] | list[list[Any]], Any | list[Any] | list[list[Any]]], tuple[Any | list[Any] | list[list[Any]], Any | list[Any] | list[list[Any]]]]:
        """Unify representations of two multivariate fractions. """
        ...
    
    def per(f, num, den, cancel=..., kill=...) -> Self:
        """Create a DMF out of the given representation. """
        ...
    
    def half_per(f, rep, kill=...) -> DUP_Flint | DMP_Python:
        """Create a DMP out of the given representation. """
        ...
    
    @classmethod
    def zero(cls, lev, dom) -> Self:
        ...
    
    @classmethod
    def one(cls, lev, dom) -> Self:
        ...
    
    def numer(f) -> DUP_Flint | DMP_Python:
        """Returns the numerator of ``f``. """
        ...
    
    def denom(f) -> DUP_Flint | DMP_Python:
        """Returns the denominator of ``f``. """
        ...
    
    def cancel(f) -> Self:
        """Remove common factors from ``f.num`` and ``f.den``. """
        ...
    
    def neg(f) -> Self:
        """Negate all coefficients in ``f``. """
        ...
    
    def add_ground(f, c) -> Self | NotImplementedType:
        """Add an element of the ground domain to ``f``. """
        ...
    
    def add(f, g) -> Self:
        """Add two multivariate fractions ``f`` and ``g``. """
        ...
    
    def sub(f, g) -> Self:
        """Subtract two multivariate fractions ``f`` and ``g``. """
        ...
    
    def mul(f, g) -> Self:
        """Multiply two multivariate fractions ``f`` and ``g``. """
        ...
    
    def pow(f, n) -> Self:
        """Raise ``f`` to a non-negative power ``n``. """
        ...
    
    def quo(f, g) -> Self:
        """Computes quotient of fractions ``f`` and ``g``. """
        ...
    
    exquo = ...
    def invert(f, check=...) -> Self:
        """Computes inverse of a fraction ``f``. """
        ...
    
    @property
    def is_zero(f) -> bool:
        """Returns ``True`` if ``f`` is a zero fraction. """
        ...
    
    @property
    def is_one(f) -> bool:
        """Returns ``True`` if ``f`` is a unit fraction. """
        ...
    
    def __neg__(f) -> Self:
        ...
    
    def __add__(f, g) -> Self | NotImplementedType:
        ...
    
    def __radd__(f, g) -> Self | NotImplementedType:
        ...
    
    def __sub__(f, g) -> Self | NotImplementedType:
        ...
    
    def __rsub__(f, g) -> DMF | NotImplementedType:
        ...
    
    def __mul__(f, g) -> Self | NotImplementedType:
        ...
    
    def __rmul__(f, g) -> Self | NotImplementedType:
        ...
    
    def __pow__(f, n) -> Self:
        ...
    
    def __truediv__(f, g) -> Self | NotImplementedType:
        ...
    
    def __rtruediv__(self, g):
        ...
    
    def __eq__(f, g) -> bool:
        ...
    
    def __ne__(f, g) -> bool:
        ...
    
    def __lt__(f, g) -> bool:
        ...
    
    def __le__(f, g) -> bool:
        ...
    
    def __gt__(f, g) -> bool:
        ...
    
    def __ge__(f, g) -> bool:
        ...
    
    def __bool__(f) -> bool:
        ...
    


def init_normal_ANP(rep, mod, dom) -> ANP:
    ...

class ANP(CantSympify):
    """Dense Algebraic Number Polynomials over a field. """
    __slots__ = ...
    def __new__(cls, rep, mod, dom) -> Self:
        ...
    
    @classmethod
    def new(cls, rep, mod, dom) -> Self:
        ...
    
    def __reduce__(self) -> tuple[type[ANP], tuple[Any, Any, Any]]:
        ...
    
    @property
    def rep(self):
        ...
    
    @property
    def mod(self):
        ...
    
    def to_DMP(self):
        ...
    
    def mod_to_DMP(self):
        ...
    
    def per(f, rep) -> Self:
        ...
    
    def __repr__(f) -> str:
        ...
    
    def __hash__(f) -> int:
        ...
    
    def convert(f, dom) -> Self:
        """Convert ``f`` to a ``ANP`` over a new domain. """
        ...
    
    def unify(f, g) -> tuple[Any, Callable[..., Self], Any, Any, Any] | tuple[Any, Callable[..., ANP], Any | list[Any], Any | list[Any], Any | list[Any]]:
        """Unify representations of two algebraic numbers. """
        ...
    
    def unify_ANP(f, g) -> tuple[Any, Any, Any, Any]:
        """Unify and return ``DMP`` instances of ``f`` and ``g``. """
        ...
    
    @classmethod
    def zero(cls, mod, dom) -> ANP:
        ...
    
    @classmethod
    def one(cls, mod, dom) -> ANP:
        ...
    
    def to_dict(f):
        """Convert ``f`` to a dict representation with native coefficients. """
        ...
    
    def to_sympy_dict(f) -> dict[tuple[Literal[0]], Any] | dict[Any, Any] | dict[Never, Any]:
        """Convert ``f`` to a dict representation with SymPy coefficients. """
        ...
    
    def to_list(f):
        """Convert ``f`` to a list representation with native coefficients. """
        ...
    
    def mod_to_list(f):
        """Return ``f.mod`` as a list with native coefficients. """
        ...
    
    def to_sympy_list(f) -> list[Any]:
        """Convert ``f`` to a list representation with SymPy coefficients. """
        ...
    
    def to_tuple(f):
        """
        Convert ``f`` to a tuple representation with native coefficients.

        This is needed for hashing.
        """
        ...
    
    @classmethod
    def from_list(cls, rep, mod, dom) -> ANP:
        ...
    
    def add_ground(f, c) -> Self:
        """Add an element of the ground domain to ``f``. """
        ...
    
    def sub_ground(f, c) -> Self:
        """Subtract an element of the ground domain from ``f``. """
        ...
    
    def mul_ground(f, c) -> Self:
        """Multiply ``f`` by an element of the ground domain. """
        ...
    
    def quo_ground(f, c) -> Self:
        """Quotient of ``f`` by an element of the ground domain. """
        ...
    
    def neg(f) -> Self:
        ...
    
    def add(f, g) -> Self:
        ...
    
    def sub(f, g) -> Self:
        ...
    
    def mul(f, g) -> Self:
        ...
    
    def pow(f, n) -> Self:
        """Raise ``f`` to a non-negative power ``n``. """
        ...
    
    def exquo(f, g) -> Self:
        ...
    
    def div(f, g) -> tuple[Self, ANP]:
        ...
    
    def quo(f, g) -> Self:
        ...
    
    def rem(f, g) -> ANP:
        ...
    
    def LC(f):
        """Returns the leading coefficient of ``f``. """
        ...
    
    def TC(f):
        """Returns the trailing coefficient of ``f``. """
        ...
    
    @property
    def is_zero(f):
        """Returns ``True`` if ``f`` is a zero algebraic number. """
        ...
    
    @property
    def is_one(f):
        """Returns ``True`` if ``f`` is a unit algebraic number. """
        ...
    
    @property
    def is_ground(f):
        """Returns ``True`` if ``f`` is an element of the ground domain. """
        ...
    
    def __pos__(f) -> Self:
        ...
    
    def __neg__(f) -> Self:
        ...
    
    def __add__(f, g) -> Self | NotImplementedType:
        ...
    
    def __radd__(f, g) -> Self | NotImplementedType:
        ...
    
    def __sub__(f, g) -> Self | NotImplementedType:
        ...
    
    def __rsub__(f, g) -> Self | NotImplementedType:
        ...
    
    def __mul__(f, g) -> Self | NotImplementedType:
        ...
    
    def __rmul__(f, g) -> Self | NotImplementedType:
        ...
    
    def __pow__(f, n) -> Self:
        ...
    
    def __divmod__(f, g) -> tuple[Self, ANP]:
        ...
    
    def __mod__(f, g) -> ANP:
        ...
    
    def __truediv__(f, g) -> Self | NotImplementedType:
        ...
    
    def __eq__(f, g) -> bool:
        ...
    
    def __ne__(f, g) -> bool:
        ...
    
    def __lt__(f, g) -> bool:
        ...
    
    def __le__(f, g) -> bool:
        ...
    
    def __gt__(f, g) -> bool:
        ...
    
    def __ge__(f, g) -> bool:
        ...
    
    def __bool__(f) -> bool:
        ...
    


