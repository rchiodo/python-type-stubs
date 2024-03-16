import flint
from sympy.external.gmpy import GROUND_TYPES
from sympy.utilities.decorator import doctest_depends_on
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.utilities import public

"""Implementation of :class:`FiniteField` class. """
if GROUND_TYPES == 'flint':
    ...
else:
    flint = ...
@public
@doctest_depends_on(modules=['python', 'gmpy'])
class FiniteField(Field, SimpleDomain):
    r"""Finite field of prime order :ref:`GF(p)`

    A :ref:`GF(p)` domain represents a `finite field`_ `\mathbb{F}_p` of prime
    order as :py:class:`~.Domain` in the domain system (see
    :ref:`polys-domainsintro`).

    A :py:class:`~.Poly` created from an expression with integer
    coefficients will have the domain :ref:`ZZ`. However, if the ``modulus=p``
    option is given then the domain will be a finite field instead.

    >>> from sympy import Poly, Symbol
    >>> x = Symbol('x')
    >>> p = Poly(x**2 + 1)
    >>> p
    Poly(x**2 + 1, x, domain='ZZ')
    >>> p.domain
    ZZ
    >>> p2 = Poly(x**2 + 1, modulus=2)
    >>> p2
    Poly(x**2 + 1, x, modulus=2)
    >>> p2.domain
    GF(2)

    It is possible to factorise a polynomial over :ref:`GF(p)` using the
    modulus argument to :py:func:`~.factor` or by specifying the domain
    explicitly. The domain can also be given as a string.

    >>> from sympy import factor, GF
    >>> factor(x**2 + 1)
    x**2 + 1
    >>> factor(x**2 + 1, modulus=2)
    (x + 1)**2
    >>> factor(x**2 + 1, domain=GF(2))
    (x + 1)**2
    >>> factor(x**2 + 1, domain='GF(2)')
    (x + 1)**2

    It is also possible to use :ref:`GF(p)` with the :py:func:`~.cancel`
    and :py:func:`~.gcd` functions.

    >>> from sympy import cancel, gcd
    >>> cancel((x**2 + 1)/(x + 1))
    (x**2 + 1)/(x + 1)
    >>> cancel((x**2 + 1)/(x + 1), domain=GF(2))
    x + 1
    >>> gcd(x**2 + 1, x + 1)
    1
    >>> gcd(x**2 + 1, x + 1, domain=GF(2))
    x + 1

    When using the domain directly :ref:`GF(p)` can be used as a constructor
    to create instances which then support the operations ``+,-,*,**,/``

    >>> from sympy import GF
    >>> K = GF(5)
    >>> K
    GF(5)
    >>> x = K(3)
    >>> y = K(2)
    >>> x
    3 mod 5
    >>> y
    2 mod 5
    >>> x * y
    1 mod 5
    >>> x / y
    4 mod 5

    Notes
    =====

    It is also possible to create a :ref:`GF(p)` domain of **non-prime**
    order but the resulting ring is **not** a field: it is just the ring of
    the integers modulo ``n``.

    >>> K = GF(9)
    >>> z = K(3)
    >>> z
    3 mod 9
    >>> z**2
    0 mod 9

    It would be good to have a proper implementation of prime power fields
    (``GF(p**n)``) but these are not yet implemented in SymPY.

    .. _finite field: https://en.wikipedia.org/wiki/Finite_field
    """
    rep = ...
    alias = ...
    is_FF = ...
    is_Numerical = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    dom = ...
    mod = ...
    def __init__(self, mod, symmetric=...) -> None:
        ...
    
    @property
    def tp(self) -> Any | type[cls]:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        """Returns ``True`` if two domains are equivalent. """
        ...
    
    def characteristic(self) -> Any | None:
        """Return the characteristic of this domain. """
        ...
    
    def get_field(self) -> Self:
        """Returns a field associated with ``self``. """
        ...
    
    def to_sympy(self, a) -> Integer:
        """Convert ``a`` to a SymPy object. """
        ...
    
    def from_sympy(self, a) -> Any | cls:
        """Convert SymPy's Integer to SymPy's ``Integer``. """
        ...
    
    def to_int(self, a) -> int:
        """Convert ``val`` to a Python ``int`` object. """
        ...
    
    def is_positive(self, a) -> bool:
        """Returns True if ``a`` is positive. """
        ...
    
    def is_nonnegative(self, a) -> Literal[True]:
        """Returns True if ``a`` is non-negative. """
        ...
    
    def is_negative(self, a) -> Literal[False]:
        """Returns True if ``a`` is negative. """
        ...
    
    def is_nonpositive(self, a) -> bool:
        """Returns True if ``a`` is non-positive. """
        ...
    
    def from_FF(K1, a, K0=...) -> Any | cls:
        """Convert ``ModularInteger(int)`` to ``dtype``. """
        ...
    
    def from_FF_python(K1, a, K0=...) -> Any | cls:
        """Convert ``ModularInteger(int)`` to ``dtype``. """
        ...
    
    def from_ZZ(K1, a, K0=...) -> Any | cls:
        """Convert Python's ``int`` to ``dtype``. """
        ...
    
    def from_ZZ_python(K1, a, K0=...) -> Any | cls:
        """Convert Python's ``int`` to ``dtype``. """
        ...
    
    def from_QQ(K1, a, K0=...) -> Any | cls | None:
        """Convert Python's ``Fraction`` to ``dtype``. """
        ...
    
    def from_QQ_python(K1, a, K0=...) -> Any | cls | None:
        """Convert Python's ``Fraction`` to ``dtype``. """
        ...
    
    def from_FF_gmpy(K1, a, K0=...) -> Any | cls:
        """Convert ``ModularInteger(mpz)`` to ``dtype``. """
        ...
    
    def from_ZZ_gmpy(K1, a, K0=...) -> Any | cls:
        """Convert GMPY's ``mpz`` to ``dtype``. """
        ...
    
    def from_QQ_gmpy(K1, a, K0=...) -> Any | cls | None:
        """Convert GMPY's ``mpq`` to ``dtype``. """
        ...
    
    def from_RealField(K1, a, K0) -> Any | cls | None:
        """Convert mpmath's ``mpf`` to ``dtype``. """
        ...
    
    def is_square(self, a) -> bool:
        """Returns True if ``a`` is a quadratic residue modulo p. """
        ...
    
    def exsqrt(self, a) -> Any | cls | Literal[0] | None:
        """Square root modulo p of ``a`` if it is a quadratic residue.

        Explanation
        ===========
        Always returns the square root that is no larger than ``p // 2``.
        """
        ...
    


GF = ...
