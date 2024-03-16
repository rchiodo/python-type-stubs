from typing import Any
from sympy.core.sympify import CantSympify
from sympy.polys.compatibility import IPolys
from sympy.polys.domains.domainelement import DomainElement
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public

"""Sparse polynomial rings. """
@public
def ring(symbols, domain, order=...) -> Any:
    """Construct a polynomial ring returning ``(ring, x_1, ..., x_n)``.

    Parameters
    ==========

    symbols : str
        Symbol/Expr or sequence of str, Symbol/Expr (non-empty)
    domain : :class:`~.Domain` or coercible
    order : :class:`~.MonomialOrder` or coercible, optional, defaults to ``lex``

    Examples
    ========

    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.orderings import lex

    >>> R, x, y, z = ring("x,y,z", ZZ, lex)
    >>> R
    Polynomial ring in x, y, z over ZZ with lex order
    >>> x + y + z
    x + y + z
    >>> type(_)
    <class 'sympy.polys.rings.PolyElement'>

    """
    ...

@public
def xring(symbols, domain, order=...) -> tuple[PolyRing | Any, Any]:
    """Construct a polynomial ring returning ``(ring, (x_1, ..., x_n))``.

    Parameters
    ==========

    symbols : str
        Symbol/Expr or sequence of str, Symbol/Expr (non-empty)
    domain : :class:`~.Domain` or coercible
    order : :class:`~.MonomialOrder` or coercible, optional, defaults to ``lex``

    Examples
    ========

    >>> from sympy.polys.rings import xring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.orderings import lex

    >>> R, (x, y, z) = xring("x,y,z", ZZ, lex)
    >>> R
    Polynomial ring in x, y, z over ZZ with lex order
    >>> x + y + z
    x + y + z
    >>> type(_)
    <class 'sympy.polys.rings.PolyElement'>

    """
    ...

@public
def vring(symbols, domain, order=...) -> PolyRing | Any:
    """Construct a polynomial ring and inject ``x_1, ..., x_n`` into the global namespace.

    Parameters
    ==========

    symbols : str
        Symbol/Expr or sequence of str, Symbol/Expr (non-empty)
    domain : :class:`~.Domain` or coercible
    order : :class:`~.MonomialOrder` or coercible, optional, defaults to ``lex``

    Examples
    ========

    >>> from sympy.polys.rings import vring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.orderings import lex

    >>> vring("x,y,z", ZZ, lex)
    Polynomial ring in x, y, z over ZZ with lex order
    >>> x + y + z # noqa:
    x + y + z
    >>> type(_)
    <class 'sympy.polys.rings.PolyElement'>

    """
    ...

@public
def sring(exprs, *symbols, **options) -> tuple[PolyRing | Any, Any] | tuple[PolyRing | Any, list[Any]]:
    """Construct a ring deriving generators and domain from options and input expressions.

    Parameters
    ==========

    exprs : :class:`~.Expr` or sequence of :class:`~.Expr` (sympifiable)
    symbols : sequence of :class:`~.Symbol`/:class:`~.Expr`
    options : keyword arguments understood by :class:`~.Options`

    Examples
    ========

    >>> from sympy import sring, symbols

    >>> x, y, z = symbols("x,y,z")
    >>> R, f = sring(x + 2*y + 3*z)
    >>> R
    Polynomial ring in x, y, z over ZZ with lex order
    >>> f
    x + 2*y + 3*z
    >>> type(_)
    <class 'sympy.polys.rings.PolyElement'>

    """
    ...

_ring_cache: dict[Any, Any] = ...
class PolyRing(DefaultPrinting, IPolys):
    """Multivariate distributed polynomial ring. """
    def __new__(cls, symbols, domain, order=...) -> Self | Any:
        ...
    
    def __getnewargs__(self) -> tuple[Any, Any, Any]:
        ...
    
    def __getstate__(self) -> dict[str, Any]:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def clone(self, symbols=..., domain=..., order=...) -> Self:
        ...
    
    def monomial_basis(self, i) -> tuple[Any, ...]:
        """Return the ith-basis element. """
        ...
    
    @property
    def zero(self):
        ...
    
    @property
    def one(self):
        ...
    
    def domain_new(self, element, orig_domain=...):
        ...
    
    def ground_new(self, coeff):
        ...
    
    def term_new(self, monom, coeff):
        ...
    
    def ring_new(self, element) -> PolyElement:
        ...
    
    __call__ = ...
    def from_dict(self, element, orig_domain=...):
        ...
    
    def from_terms(self, element, orig_domain=...):
        ...
    
    def from_list(self, element):
        ...
    
    def from_expr(self, expr):
        ...
    
    def index(self, gen) -> int:
        """Compute index of ``gen`` in ``self.gens``. """
        ...
    
    def drop(self, *gens) -> Self:
        """Remove specified generators from this ring. """
        ...
    
    def __getitem__(self, key) -> Self:
        ...
    
    def to_ground(self) -> Self:
        ...
    
    def to_domain(self) -> Any:
        ...
    
    def to_field(self) -> FracField | Any:
        ...
    
    @property
    def is_univariate(self) -> bool:
        ...
    
    @property
    def is_multivariate(self) -> bool:
        ...
    
    def add(self, *objs):
        """
        Add a sequence of polynomials or containers of polynomials.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> R, x = ring("x", ZZ)
        >>> R.add([ x**2 + 2*i + 3 for i in range(4) ])
        4*x**2 + 24
        >>> _.factor_list()
        (4, [(x**2 + 6, 1)])

        """
        ...
    
    def mul(self, *objs):
        """
        Multiply a sequence of polynomials or containers of polynomials.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> R, x = ring("x", ZZ)
        >>> R.mul([ x**2 + 2*i + 3 for i in range(4) ])
        x**8 + 24*x**6 + 206*x**4 + 744*x**2 + 945
        >>> _.factor_list()
        (1, [(x**2 + 3, 1), (x**2 + 5, 1), (x**2 + 7, 1), (x**2 + 9, 1)])

        """
        ...
    
    def drop_to_ground(self, *gens) -> Self:
        r"""
        Remove specified generators from the ring and inject them into
        its domain.
        """
        ...
    
    def compose(self, other) -> Self:
        """Add the generators of ``other`` to ``self``"""
        ...
    
    def add_gens(self, symbols) -> Self:
        """Add the elements of ``symbols`` as generators to ``self``"""
        ...
    
    def symmetric_poly(self, n):
        """
        Return the elementary symmetric polynomial of degree *n* over
        this ring's generators.
        """
        ...
    


class PolyElement(DomainElement, DefaultPrinting, CantSympify, dict):
    """Element of multivariate distributed polynomial ring. """
    def new(self, init) -> Self:
        ...
    
    def parent(self):
        ...
    
    def __getnewargs__(self) -> tuple[Any, list[tuple[Any, Any]]]:
        ...
    
    _hash = ...
    def __hash__(self) -> int:
        ...
    
    def copy(self) -> Self:
        """Return a copy of polynomial self.

        Polynomials are mutable; if one is interested in preserving
        a polynomial, and one plans to use inplace operations, one
        can copy the polynomial. This method makes a shallow copy.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> R, x, y = ring('x, y', ZZ)
        >>> p = (x + y)**2
        >>> p1 = p.copy()
        >>> p2 = p
        >>> p[R.zero_monom] = 3
        >>> p
        x**2 + 2*x*y + y**2 + 3
        >>> p1
        x**2 + 2*x*y + y**2
        >>> p2
        x**2 + 2*x*y + y**2 + 3

        """
        ...
    
    def set_ring(self, new_ring) -> Self:
        ...
    
    def as_expr(self, *symbols) -> Order:
        ...
    
    def as_expr_dict(self) -> dict[Any, Any]:
        ...
    
    def clear_denoms(self) -> tuple[Any, Self]:
        ...
    
    def strip_zero(self) -> None:
        """Eliminate monomials with zero coefficient. """
        ...
    
    def __eq__(p1, p2) -> bool:
        """Equality test for polynomials.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p1 = (x + y)**2 + (x - y)**2
        >>> p1 == 4*x*y
        False
        >>> p1 == 2*(x**2 + y**2)
        True

        """
        ...
    
    def __ne__(p1, p2) -> bool:
        ...
    
    def almosteq(p1, p2, tolerance=...) -> bool:
        """Approximate equality test for polynomials. """
        ...
    
    def sort_key(self) -> tuple[int, list[Any]]:
        ...
    
    def __lt__(p1, p2) -> bool:
        ...
    
    def __le__(p1, p2) -> bool:
        ...
    
    def __gt__(p1, p2) -> bool:
        ...
    
    def __ge__(p1, p2) -> bool:
        ...
    
    def drop(self, gen):
        ...
    
    def drop_to_ground(self, gen):
        ...
    
    def to_dense(self) -> list[Any] | list[list[Any]]:
        ...
    
    def to_dict(self) -> dict[Any, Any]:
        ...
    
    def str(self, printer, precedence, exp_pattern, mul_symbol) -> LiteralString:
        ...
    
    @property
    def is_generator(self) -> bool:
        ...
    
    @property
    def is_ground(self) -> bool:
        ...
    
    @property
    def is_monomial(self) -> bool:
        ...
    
    @property
    def is_term(self) -> bool:
        ...
    
    @property
    def is_negative(self):
        ...
    
    @property
    def is_positive(self):
        ...
    
    @property
    def is_nonnegative(self):
        ...
    
    @property
    def is_nonpositive(self):
        ...
    
    @property
    def is_zero(f) -> bool:
        ...
    
    @property
    def is_one(f):
        ...
    
    @property
    def is_monic(f):
        ...
    
    @property
    def is_primitive(f):
        ...
    
    @property
    def is_linear(f) -> bool:
        ...
    
    @property
    def is_quadratic(f) -> bool:
        ...
    
    @property
    def is_squarefree(f) -> Literal[True]:
        ...
    
    @property
    def is_irreducible(f) -> Literal[True]:
        ...
    
    @property
    def is_cyclotomic(f):
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def __pos__(self) -> Self:
        ...
    
    def __add__(p1, p2) -> Self | PolyElement | NotImplementedType:
        """Add two polynomials.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> (x + y)**2 + (x - y)**2
        2*x**2 + 2*y**2

        """
        ...
    
    def __radd__(p1, n) -> Self | NotImplementedType:
        ...
    
    def __sub__(p1, p2) -> Self | NotImplementedType:
        """Subtract polynomial p2 from p1.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p1 = x + y**2
        >>> p2 = x*y + y**2
        >>> p1 - p2
        -x*y + x

        """
        ...
    
    def __rsub__(p1, n) -> NotImplementedType:
        """n - p1 with n convertible to the coefficient domain.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y
        >>> 4 - p
        -x - y + 4

        """
        ...
    
    def __mul__(p1, p2) -> NotImplementedType:
        """Multiply two polynomials.

        Examples
        ========

        >>> from sympy.polys.domains import QQ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', QQ)
        >>> p1 = x + y
        >>> p2 = x - y
        >>> p1*p2
        x**2 - y**2

        """
        ...
    
    def __rmul__(p1, p2) -> NotImplementedType:
        """p2 * p1 with p2 in the coefficient domain of p1.

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y
        >>> 4 * p
        4*x + 4*y

        """
        ...
    
    def __pow__(self, n) -> Self:
        """raise polynomial to power `n`

        Examples
        ========

        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.rings import ring

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y**2
        >>> p**3
        x**3 + 3*x**2*y**2 + 3*x*y**4 + y**6

        """
        ...
    
    def square(self):
        """square of a polynomial

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y**2
        >>> p.square()
        x**2 + 2*x*y**2 + y**4

        """
        ...
    
    def __divmod__(p1, p2) -> tuple[Any, Any] | tuple[list[Any], Any] | NotImplementedType | tuple[Self, Self]:
        ...
    
    def __rdivmod__(p1, p2) -> NotImplementedType:
        ...
    
    def __mod__(p1, p2) -> NotImplementedType | Self:
        ...
    
    def __rmod__(p1, p2) -> NotImplementedType:
        ...
    
    def __truediv__(p1, p2) -> list[Any] | NotImplementedType | Self:
        ...
    
    def __rtruediv__(p1, p2) -> NotImplementedType:
        ...
    
    __floordiv__ = ...
    __rfloordiv__ = ...
    def div(self, fv) -> tuple[Any, Any] | tuple[list[Any], Any]:
        """Division algorithm, see [CLO] p64.

        fv array of polynomials
           return qv, r such that
           self = sum(fv[i]*qv[i]) + r

        All polynomials are required not to be Laurent polynomials.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> f = x**3
        >>> f0 = x - y**2
        >>> f1 = x - y
        >>> qv, r = f.div((f0, f1))
        >>> qv[0]
        x**2 + x*y**2 + y**4
        >>> qv[1]
        0
        >>> r
        y**6

        """
        ...
    
    def rem(self, G):
        ...
    
    def quo(f, G) -> list[Any]:
        ...
    
    def exquo(f, G) -> list[Any]:
        ...
    
    def degree(f, x=...) -> float | Literal[0]:
        """
        The leading degree in ``x`` or the main variable.

        Note that the degree of 0 is negative infinity (``float('-inf')``)

        """
        ...
    
    def degrees(f) -> tuple[Any, ...]:
        """
        A tuple containing leading degrees in all variables.

        Note that the degree of 0 is negative infinity (``float('-inf')``)

        """
        ...
    
    def tail_degree(f, x=...) -> float | Literal[0]:
        """
        The tail degree in ``x`` or the main variable.

        Note that the degree of 0 is negative infinity (``float('-inf')``)

        """
        ...
    
    def tail_degrees(f) -> tuple[Any, ...]:
        """
        A tuple containing tail degrees in all variables.

        Note that the degree of 0 is negative infinity (``float('-inf')``)

        """
        ...
    
    def leading_expv(self) -> None:
        """Leading monomial tuple according to the monomial ordering.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y, z = ring('x, y, z', ZZ)
        >>> p = x**4 + x**3*y + x**2*z**2 + z**7
        >>> p.leading_expv()
        (4, 0, 0)

        """
        ...
    
    def coeff(self, element):
        """
        Returns the coefficient that stands next to the given monomial.

        Parameters
        ==========

        element : PolyElement (with ``is_monomial = True``) or 1

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y, z = ring("x,y,z", ZZ)
        >>> f = 3*x**2*y - x*y*z + 7*z**3 + 23

        >>> f.coeff(x**2*y)
        3
        >>> f.coeff(x*y)
        0
        >>> f.coeff(1)
        23

        """
        ...
    
    def const(self):
        """Returns the constant coefficient. """
        ...
    
    @property
    def LC(self):
        ...
    
    @property
    def LM(self):
        ...
    
    def leading_monom(self):
        """
        Leading monomial as a polynomial element.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> (3*x*y + y**2).leading_monom()
        x*y

        """
        ...
    
    @property
    def LT(self) -> tuple[Any, Any]:
        ...
    
    def leading_term(self):
        """Leading term as a polynomial element.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> (3*x*y + y**2).leading_term()
        3*x*y

        """
        ...
    
    def coeffs(self, order=...) -> list[Any]:
        """Ordered list of polynomial coefficients.

        Parameters
        ==========

        order : :class:`~.MonomialOrder` or coercible, optional

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.orderings import lex, grlex

        >>> _, x, y = ring("x, y", ZZ, lex)
        >>> f = x*y**7 + 2*x**2*y**3

        >>> f.coeffs()
        [2, 1]
        >>> f.coeffs(grlex)
        [1, 2]

        """
        ...
    
    def monoms(self, order=...) -> list[Any]:
        """Ordered list of polynomial monomials.

        Parameters
        ==========

        order : :class:`~.MonomialOrder` or coercible, optional

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.orderings import lex, grlex

        >>> _, x, y = ring("x, y", ZZ, lex)
        >>> f = x*y**7 + 2*x**2*y**3

        >>> f.monoms()
        [(2, 3), (1, 7)]
        >>> f.monoms(grlex)
        [(1, 7), (2, 3)]

        """
        ...
    
    def terms(self, order=...) -> list[Any]:
        """Ordered list of polynomial terms.

        Parameters
        ==========

        order : :class:`~.MonomialOrder` or coercible, optional

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> from sympy.polys.orderings import lex, grlex

        >>> _, x, y = ring("x, y", ZZ, lex)
        >>> f = x*y**7 + 2*x**2*y**3

        >>> f.terms()
        [((2, 3), 2), ((1, 7), 1)]
        >>> f.terms(grlex)
        [((1, 7), 1), ((2, 3), 2)]

        """
        ...
    
    def itercoeffs(self) -> Iterator[Any]:
        """Iterator over coefficients of a polynomial. """
        ...
    
    def itermonoms(self) -> Iterator[Any]:
        """Iterator over monomials of a polynomial. """
        ...
    
    def iterterms(self) -> Iterator[tuple[Any, Any]]:
        """Iterator over terms of a polynomial. """
        ...
    
    def listcoeffs(self) -> list[Any]:
        """Unordered list of polynomial coefficients. """
        ...
    
    def listmonoms(self) -> list[Any]:
        """Unordered list of polynomial monomials. """
        ...
    
    def listterms(self) -> list[tuple[Any, Any]]:
        """Unordered list of polynomial terms. """
        ...
    
    def imul_num(p, c) -> Self | None:
        """multiply inplace the polynomial p by an element in the
        coefficient ring, provided p is not one of the generators;
        else multiply not inplace

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring('x, y', ZZ)
        >>> p = x + y**2
        >>> p1 = p.imul_num(3)
        >>> p1
        3*x + 3*y**2
        >>> p1 is p
        True
        >>> p = x
        >>> p1 = p.imul_num(3)
        >>> p1
        3*x
        >>> p1 is p
        False

        """
        ...
    
    def content(f):
        """Returns GCD of polynomial's coefficients. """
        ...
    
    def primitive(f) -> tuple[Any, Self]:
        """Returns content and a primitive polynomial. """
        ...
    
    def monic(f) -> Self:
        """Divides all coefficients by the leading coefficient. """
        ...
    
    def mul_ground(f, x) -> Self:
        ...
    
    def mul_monom(f, monom) -> Self:
        ...
    
    def mul_term(f, term) -> Self:
        ...
    
    def quo_ground(f, x) -> Self:
        ...
    
    def quo_term(f, term) -> Self:
        ...
    
    def trunc_ground(f, p) -> Self:
        ...
    
    rem_ground = ...
    def extract_ground(self, g) -> tuple[Any, Self, Any]:
        ...
    
    def max_norm(f):
        ...
    
    def l1_norm(f) -> int:
        ...
    
    def deflate(f, *G) -> tuple[tuple[Any, ...], list[Self]] | tuple[tuple[Any, ...], list[Any]]:
        ...
    
    def inflate(f, J):
        ...
    
    def lcm(self, g):
        ...
    
    def gcd(f, g) -> Self:
        ...
    
    def cofactors(f, g) -> tuple[Any, Any, Any] | tuple[Self, Self, Self]:
        ...
    
    def cancel(self, g) -> tuple[Self, Any] | tuple[Any | Self | PolyElement, Any | Self | PolyElement]:
        """
        Cancel common factors in a rational function ``f/g``.

        Examples
        ========

        >>> from sympy.polys import ring, ZZ
        >>> R, x,y = ring("x,y", ZZ)

        >>> (2*x**2 - 2).cancel(x**2 - 2*x + 1)
        (2*x + 2, x - 1)

        """
        ...
    
    def canonical_unit(f):
        ...
    
    def diff(f, x):
        """Computes partial derivative in ``x``.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ

        >>> _, x, y = ring("x,y", ZZ)
        >>> p = x + x**2*y**3
        >>> p.diff(x)
        2*x*y**3 + 1

        """
        ...
    
    def __call__(f, *values):
        ...
    
    def evaluate(self, x, a=...):
        ...
    
    def subs(self, x, a=...) -> Self:
        ...
    
    def symmetrize(self) -> tuple[Self, Any, list[Any]] | tuple[Any, Self | Any, list[tuple[Any, Any]]]:
        r"""
        Rewrite *self* in terms of elementary symmetric polynomials.

        Explanation
        ===========

        If this :py:class:`~.PolyElement` belongs to a ring of $n$ variables,
        we can try to write it as a function of the elementary symmetric
        polynomials on $n$ variables. We compute a symmetric part, and a
        remainder for any part we were not able to symmetrize.

        Examples
        ========

        >>> from sympy.polys.rings import ring
        >>> from sympy.polys.domains import ZZ
        >>> R, x, y = ring("x,y", ZZ)

        >>> f = x**2 + y**2
        >>> f.symmetrize()
        (x**2 - 2*y, 0, [(x, x + y), (y, x*y)])

        >>> f = x**2 - y**2
        >>> f.symmetrize()
        (x**2 - 2*y, -2*y**2, [(x, x + y), (y, x*y)])

        Returns
        =======

        Triple ``(p, r, m)``
            ``p`` is a :py:class:`~.PolyElement` that represents our attempt
            to express *self* as a function of elementary symmetric
            polynomials. Each variable in ``p`` stands for one of the
            elementary symmetric polynomials. The correspondence is given
            by ``m``.

            ``r`` is the remainder.

            ``m`` is a list of pairs, giving the mapping from variables in
            ``p`` to elementary symmetric polynomials.

            The triple satisfies the equation ``p.compose(m) + r == self``.
            If the remainder ``r`` is zero, *self* is symmetric. If it is
            nonzero, we were not able to represent *self* as symmetric.

        See Also
        ========

        sympy.polys.polyfuncs.symmetrize

        References
        ==========

        .. [1] Lauer, E. Algorithms for symmetrical polynomials, Proc. 1976
            ACM Symp. on Symbolic and Algebraic Computing, NY 242-247.
            https://dl.acm.org/doi/pdf/10.1145/800205.806342

        """
        ...
    
    def compose(f, x, a=...):
        ...
    
    def coeff_wrt(self, x, deg):
        """
        Coefficient of ``self`` with respect to ``x**deg``.

        Treating ``self`` as a univariate polynomial in ``x`` this finds the
        coefficient of ``x**deg`` as a polynomial in the other generators.

        Parameters
        ==========

        x : generator or generator index
            The generator or generator index to compute the expression for.
        deg : int
            The degree of the monomial to compute the expression for.

        Returns
        =======

        :py:class:`~.PolyElement`
            The coefficient of ``x**deg`` as a polynomial in the same ring.

        Examples
        ========

        >>> from sympy.polys import ring, ZZ
        >>> R, x, y, z = ring("x, y, z", ZZ)

        >>> p = 2*x**4 + 3*y**4 + 10*z**2 + 10*x*z**2
        >>> deg = 2
        >>> p.coeff_wrt(2, deg) # Using the generator index
        10*x + 10
        >>> p.coeff_wrt(z, deg) # Using the generator
        10*x + 10
        >>> p.coeff(z**2) # shows the difference between coeff and coeff_wrt
        10

        See Also
        ========

        coeff, coeffs

        """
        ...
    
    def prem(self, g, x=...) -> Self:
        """
        Pseudo-remainder of the polynomial ``self`` with respect to ``g``.

        The pseudo-quotient ``q`` and pseudo-remainder ``r`` with respect to
        ``z`` when dividing ``f`` by ``g`` satisfy ``m*f = g*q + r``,
        where ``deg(r,z) < deg(g,z)`` and
        ``m = LC(g,z)**(deg(f,z) - deg(g,z)+1)``.

        See :meth:`pdiv` for explanation of pseudo-division.


        Parameters
        ==========

        g : :py:class:`~.PolyElement`
            The polynomial to divide ``self`` by.
        x : generator or generator index, optional
            The main variable of the polynomials and default is first generator.

        Returns
        =======

        :py:class:`~.PolyElement`
            The pseudo-remainder polynomial.

        Raises
        ======

        ZeroDivisionError : If ``g`` is the zero polynomial.

        Examples
        ========

        >>> from sympy.polys import ring, ZZ
        >>> R, x, y = ring("x, y", ZZ)

        >>> f = x**2 + x*y
        >>> g = 2*x + 2
        >>> f.prem(g) # first generator is chosen by default if it is not given
        -4*y + 4
        >>> f.rem(g) # shows the differnce between prem and rem
        x**2 + x*y
        >>> f.prem(g, y) # generator is given
        0
        >>> f.prem(g, 1) # generator index is given
        0

        See Also
        ========

        pdiv, pquo, pexquo, sympy.polys.domains.ring.Ring.rem

        """
        ...
    
    def pdiv(self, g, x=...) -> tuple[Any, Self] | tuple[Any, Any]:
        """
        Computes the pseudo-division of the polynomial ``self`` with respect to ``g``.

        The pseudo-division algorithm is used to find the pseudo-quotient ``q``
        and pseudo-remainder ``r`` such that ``m*f = g*q + r``, where ``m``
        represents the multiplier and ``f`` is the dividend polynomial.

        The pseudo-quotient ``q`` and pseudo-remainder ``r`` are polynomials in
        the variable ``x``, with the degree of ``r`` with respect to ``x``
        being strictly less than the degree of ``g`` with respect to ``x``.

        The multiplier ``m`` is defined as
        ``LC(g, x) ^ (deg(f, x) - deg(g, x) + 1)``,
        where ``LC(g, x)`` represents the leading coefficient of ``g``.

        It is important to note that in the context of the ``prem`` method,
        multivariate polynomials in a ring, such as ``R[x,y,z]``, are treated
        as univariate polynomials with coefficients that are polynomials,
        such as ``R[x,y][z]``. When dividing ``f`` by ``g`` with respect to the
        variable ``z``, the pseudo-quotient ``q`` and pseudo-remainder ``r``
        satisfy ``m*f = g*q + r``, where ``deg(r, z) < deg(g, z)``
        and ``m = LC(g, z)^(deg(f, z) - deg(g, z) + 1)``.

        In this function, the pseudo-remainder ``r`` can be obtained using the
        ``prem`` method, the pseudo-quotient ``q`` can
        be obtained using the ``pquo`` method, and
        the function ``pdiv`` itself returns a tuple ``(q, r)``.


        Parameters
        ==========

        g : :py:class:`~.PolyElement`
            The polynomial to divide ``self`` by.
        x : generator or generator index, optional
            The main variable of the polynomials and default is first generator.

        Returns
        =======

        :py:class:`~.PolyElement`
            The pseudo-division polynomial (tuple of ``q`` and ``r``).

        Raises
        ======

        ZeroDivisionError : If ``g`` is the zero polynomial.

        Examples
        ========

        >>> from sympy.polys import ring, ZZ
        >>> R, x, y = ring("x, y", ZZ)

        >>> f = x**2 + x*y
        >>> g = 2*x + 2
        >>> f.pdiv(g) # first generator is chosen by default if it is not given
        (2*x + 2*y - 2, -4*y + 4)
        >>> f.div(g) # shows the difference between pdiv and div
        (0, x**2 + x*y)
        >>> f.pdiv(g, y) # generator is given
        (2*x**3 + 2*x**2*y + 6*x**2 + 2*x*y + 8*x + 4, 0)
        >>> f.pdiv(g, 1) # generator index is given
        (2*x**3 + 2*x**2*y + 6*x**2 + 2*x*y + 8*x + 4, 0)

        See Also
        ========

        prem
            Computes only the pseudo-remainder more efficiently than
            `f.pdiv(g)[1]`.
        pquo
            Returns only the pseudo-quotient.
        pexquo
            Returns only an exact pseudo-quotient having no remainder.
        div
            Returns quotient and remainder of f and g polynomials.

        """
        ...
    
    def pquo(self, g, x=...):
        """
        Polynomial pseudo-quotient in multivariate polynomial ring.

        Examples
        ========
        >>> from sympy.polys import ring, ZZ
        >>> R, x,y = ring("x,y", ZZ)

        >>> f = x**2 + x*y
        >>> g = 2*x + 2*y
        >>> h = 2*x + 2
        >>> f.pquo(g)
        2*x
        >>> f.quo(g) # shows the difference between pquo and quo
        0
        >>> f.pquo(h)
        2*x + 2*y - 2
        >>> f.quo(h) # shows the difference between pquo and quo
        0

        See Also
        ========

        prem, pdiv, pexquo, sympy.polys.domains.ring.Ring.quo

        """
        ...
    
    def pexquo(self, g, x=...):
        """
        Polynomial exact pseudo-quotient in multivariate polynomial ring.

        Examples
        ========
        >>> from sympy.polys import ring, ZZ
        >>> R, x,y = ring("x,y", ZZ)

        >>> f = x**2 + x*y
        >>> g = 2*x + 2*y
        >>> h = 2*x + 2
        >>> f.pexquo(g)
        2*x
        >>> f.exquo(g) # shows the differnce between pexquo and exquo
        Traceback (most recent call last):
        ...
        ExactQuotientFailed: 2*x + 2*y does not divide x**2 + x*y
        >>> f.pexquo(h)
        Traceback (most recent call last):
        ...
        ExactQuotientFailed: 2*x + 2 does not divide x**2 + x*y

        See Also
        ========

        prem, pdiv, pquo, sympy.polys.domains.ring.Ring.exquo

        """
        ...
    
    def subresultants(self, g, x=...) -> list[int] | list[Any] | list[Any | PolyElement]:
        """
        Computes the subresultant PRS of two polynomials ``self`` and ``g``.

        Parameters
        ==========

        g : :py:class:`~.PolyElement`
            The second polynomial.
        x : generator or generator index
            The variable with respect to which the subresultant sequence is computed.

        Returns
        =======

        R : list
            Returns a list polynomials representing the subresultant PRS.

        Examples
        ========

        >>> from sympy.polys import ring, ZZ
        >>> R, x, y = ring("x, y", ZZ)

        >>> f = x**2*y + x*y
        >>> g = x + y
        >>> f.subresultants(g) # first generator is chosen by default if not given
        [x**2*y + x*y, x + y, y**3 - y**2]
        >>> f.subresultants(g, 0) # generator index is given
        [x**2*y + x*y, x + y, y**3 - y**2]
        >>> f.subresultants(g, y) # generator is given
        [x**2*y + x*y, x + y, x**3 + x**2]

        """
        ...
    
    def half_gcdex(f, g):
        ...
    
    def gcdex(f, g):
        ...
    
    def resultant(f, g):
        ...
    
    def discriminant(f):
        ...
    
    def decompose(f):
        ...
    
    def shift(f, a):
        ...
    
    def sturm(f):
        ...
    
    def gff_list(f):
        ...
    
    def sqf_norm(f):
        ...
    
    def sqf_part(f):
        ...
    
    def sqf_list(f, all=...):
        ...
    
    def factor_list(f):
        ...
    


