from types import NotImplementedType
from typing import Any, Generator, LiteralString
from sympy.polys.polyutils import IntegerPowerable

"""Computations with ideals of polynomial rings."""
class Ideal(IntegerPowerable):
    """
    Abstract base class for ideals.

    Do not instantiate - use explicit constructors in the ring class instead:

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> QQ.old_poly_ring(x).ideal(x+1)
    <x + 1>

    Attributes

    - ring - the ring this ideal belongs to

    Non-implemented methods:

    - _contains_elem
    - _contains_ideal
    - _quotient
    - _intersect
    - _union
    - _product
    - is_whole_ring
    - is_zero
    - is_prime, is_maximal, is_primary, is_radical
    - is_principal
    - height, depth
    - radical

    Methods that likely should be overridden in subclasses:

    - reduce_element
    """
    def is_whole_ring(self):
        """Return True if ``self`` is the whole ring."""
        ...
    
    def is_zero(self):
        """Return True if ``self`` is the zero ideal."""
        ...
    
    def is_prime(self):
        """Return True if ``self`` is a prime ideal."""
        ...
    
    def is_maximal(self):
        """Return True if ``self`` is a maximal ideal."""
        ...
    
    def is_radical(self):
        """Return True if ``self`` is a radical ideal."""
        ...
    
    def is_primary(self):
        """Return True if ``self`` is a primary ideal."""
        ...
    
    def is_principal(self):
        """Return True if ``self`` is a principal ideal."""
        ...
    
    def radical(self):
        """Compute the radical of ``self``."""
        ...
    
    def depth(self):
        """Compute the depth of ``self``."""
        ...
    
    def height(self):
        """Compute the height of ``self``."""
        ...
    
    def __init__(self, ring) -> None:
        ...
    
    def contains(self, elem):
        """
        Return True if ``elem`` is an element of this ideal.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).ideal(x+1, x-1).contains(3)
        True
        >>> QQ.old_poly_ring(x).ideal(x**2, x**3).contains(x)
        False
        """
        ...
    
    def subset(self, other) -> bool:
        """
        Returns True if ``other`` is is a subset of ``self``.

        Here ``other`` may be an ideal.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> I = QQ.old_poly_ring(x).ideal(x+1)
        >>> I.subset([x**2 - 1, x**2 + 2*x + 1])
        True
        >>> I.subset([x**2 + 1, x + 1])
        False
        >>> I.subset(QQ.old_poly_ring(x).ideal(x**2 - 1))
        True
        """
        ...
    
    def quotient(self, J, **opts):
        r"""
        Compute the ideal quotient of ``self`` by ``J``.

        That is, if ``self`` is the ideal `I`, compute the set
        `I : J = \{x \in R | xJ \subset I \}`.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import QQ
        >>> R = QQ.old_poly_ring(x, y)
        >>> R.ideal(x*y).quotient(R.ideal(x))
        <y>
        """
        ...
    
    def intersect(self, J):
        """
        Compute the intersection of self with ideal J.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import QQ
        >>> R = QQ.old_poly_ring(x, y)
        >>> R.ideal(x).intersect(R.ideal(y))
        <x*y>
        """
        ...
    
    def saturate(self, J):
        r"""
        Compute the ideal saturation of ``self`` by ``J``.

        That is, if ``self`` is the ideal `I`, compute the set
        `I : J^\infty = \{x \in R | xJ^n \subset I \text{ for some } n\}`.
        """
        ...
    
    def union(self, J):
        """
        Compute the ideal generated by the union of ``self`` and ``J``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).ideal(x**2 - 1).union(QQ.old_poly_ring(x).ideal((x+1)**2)) == QQ.old_poly_ring(x).ideal(x+1)
        True
        """
        ...
    
    def product(self, J):
        r"""
        Compute the ideal product of ``self`` and ``J``.

        That is, compute the ideal generated by products `xy`, for `x` an element
        of ``self`` and `y \in J`.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x, y).ideal(x).product(QQ.old_poly_ring(x, y).ideal(y))
        <x*y>
        """
        ...
    
    def reduce_element(self, x):
        """
        Reduce the element ``x`` of our ring modulo the ideal ``self``.

        Here "reduce" has no specific meaning: it could return a unique normal
        form, simplify the expression a bit, or just do nothing.
        """
        ...
    
    def __add__(self, e):
        ...
    
    __radd__ = ...
    def __mul__(self, e) -> NotImplementedType:
        ...
    
    __rmul__ = ...
    def __eq__(self, e) -> bool:
        ...
    
    def __ne__(self, e) -> bool:
        ...
    


class ModuleImplementedIdeal(Ideal):
    """
    Ideal implementation relying on the modules code.

    Attributes:

    - _module - the underlying module
    """
    def __init__(self, ring, module) -> None:
        ...
    
    @property
    def gens(self) -> Generator[Any, None, None]:
        """
        Return generators for ``self``.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x, y
        >>> list(QQ.old_poly_ring(x, y).ideal(x, y, x**2 + y).gens)
        [DMP_Python([[1], []], QQ), DMP_Python([[1, 0]], QQ), DMP_Python([[1], [], [1, 0]], QQ)]
        """
        ...
    
    def is_zero(self):
        """
        Return True if ``self`` is the zero ideal.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).ideal(x).is_zero()
        False
        >>> QQ.old_poly_ring(x).ideal().is_zero()
        True
        """
        ...
    
    def is_whole_ring(self):
        """
        Return True if ``self`` is the whole ring, i.e. one generator is a unit.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ, ilex
        >>> QQ.old_poly_ring(x).ideal(x).is_whole_ring()
        False
        >>> QQ.old_poly_ring(x).ideal(3).is_whole_ring()
        True
        >>> QQ.old_poly_ring(x, order=ilex).ideal(2 + x).is_whole_ring()
        True
        """
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def in_terms_of_generators(self, e):
        """
        Express ``e`` in terms of the generators of ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> I = QQ.old_poly_ring(x).ideal(x**2 + 1, x)
        >>> I.in_terms_of_generators(1)  # doctest: +SKIP
        [DMP_Python([1], QQ), DMP_Python([-1, 0], QQ)]
        """
        ...
    
    def reduce_element(self, x, **options):
        ...
    


