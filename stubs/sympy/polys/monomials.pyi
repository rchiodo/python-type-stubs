from sympy.polys.polyutils import PicklableWithSlots
from sympy.utilities import public

"""Tools and arithmetics for monomials of distributed polynomials. """
@public
def itermonomials(variables, max_degrees, min_degrees=...) -> Generator[Any | Order, Any, None]:
    r"""
    ``max_degrees`` and ``min_degrees`` are either both integers or both lists.
    Unless otherwise specified, ``min_degrees`` is either ``0`` or
    ``[0, ..., 0]``.

    A generator of all monomials ``monom`` is returned, such that
    either
    ``min_degree <= total_degree(monom) <= max_degree``,
    or
    ``min_degrees[i] <= degree_list(monom)[i] <= max_degrees[i]``,
    for all ``i``.

    Case I. ``max_degrees`` and ``min_degrees`` are both integers
    =============================================================

    Given a set of variables $V$ and a min_degree $N$ and a max_degree $M$
    generate a set of monomials of degree less than or equal to $N$ and greater
    than or equal to $M$. The total number of monomials in commutative
    variables is huge and is given by the following formula if $M = 0$:

        .. math::
            \frac{(\#V + N)!}{\#V! N!}

    For example if we would like to generate a dense polynomial of
    a total degree $N = 50$ and $M = 0$, which is the worst case, in 5
    variables, assuming that exponents and all of coefficients are 32-bit long
    and stored in an array we would need almost 80 GiB of memory! Fortunately
    most polynomials, that we will encounter, are sparse.

    Consider monomials in commutative variables $x$ and $y$
    and non-commutative variables $a$ and $b$::

        >>> from sympy import symbols
        >>> from sympy.polys.monomials import itermonomials
        >>> from sympy.polys.orderings import monomial_key
        >>> from sympy.abc import x, y

        >>> sorted(itermonomials([x, y], 2), key=monomial_key('grlex', [y, x]))
        [1, x, y, x**2, x*y, y**2]

        >>> sorted(itermonomials([x, y], 3), key=monomial_key('grlex', [y, x]))
        [1, x, y, x**2, x*y, y**2, x**3, x**2*y, x*y**2, y**3]

        >>> a, b = symbols('a, b', commutative=False)
        >>> set(itermonomials([a, b, x], 2))
        {1, a, a**2, b, b**2, x, x**2, a*b, b*a, x*a, x*b}

        >>> sorted(itermonomials([x, y], 2, 1), key=monomial_key('grlex', [y, x]))
        [x, y, x**2, x*y, y**2]

    Case II. ``max_degrees`` and ``min_degrees`` are both lists
    ===========================================================

    If ``max_degrees = [d_1, ..., d_n]`` and
    ``min_degrees = [e_1, ..., e_n]``, the number of monomials generated
    is:

    .. math::
        (d_1 - e_1 + 1) (d_2 - e_2 + 1) \cdots (d_n - e_n + 1)

    Let us generate all monomials ``monom`` in variables $x$ and $y$
    such that ``[1, 2][i] <= degree_list(monom)[i] <= [2, 4][i]``,
    ``i = 0, 1`` ::

        >>> from sympy import symbols
        >>> from sympy.polys.monomials import itermonomials
        >>> from sympy.polys.orderings import monomial_key
        >>> from sympy.abc import x, y

        >>> sorted(itermonomials([x, y], [2, 4], [1, 2]), reverse=True, key=monomial_key('lex', [x, y]))
        [x**2*y**4, x**2*y**3, x**2*y**2, x*y**4, x*y**3, x*y**2]
    """
    ...

def monomial_count(V, N):
    r"""
    Computes the number of monomials.

    The number of monomials is given by the following formula:

    .. math::

        \frac{(\#V + N)!}{\#V! N!}

    where `N` is a total degree and `V` is a set of variables.

    Examples
    ========

    >>> from sympy.polys.monomials import itermonomials, monomial_count
    >>> from sympy.polys.orderings import monomial_key
    >>> from sympy.abc import x, y

    >>> monomial_count(2, 2)
    6

    >>> M = list(itermonomials([x, y], 2))

    >>> sorted(M, key=monomial_key('grlex', [y, x]))
    [1, x, y, x**2, x*y, y**2]
    >>> len(M)
    6

    """
    ...

def monomial_mul(A, B) -> tuple[Any, ...]:
    """
    Multiplication of tuples representing monomials.

    Examples
    ========

    Lets multiply `x**3*y**4*z` with `x*y**2`::

        >>> from sympy.polys.monomials import monomial_mul

        >>> monomial_mul((3, 4, 1), (1, 2, 0))
        (4, 6, 1)

    which gives `x**4*y**5*z`.

    """
    ...

def monomial_div(A, B) -> tuple[Any, ...] | None:
    """
    Division of tuples representing monomials.

    Examples
    ========

    Lets divide `x**3*y**4*z` by `x*y**2`::

        >>> from sympy.polys.monomials import monomial_div

        >>> monomial_div((3, 4, 1), (1, 2, 0))
        (2, 2, 1)

    which gives `x**2*y**2*z`. However::

        >>> monomial_div((3, 4, 1), (1, 2, 2)) is None
        True

    `x*y**2*z**2` does not divide `x**3*y**4*z`.

    """
    ...

def monomial_ldiv(A, B) -> tuple[Any, ...]:
    """
    Division of tuples representing monomials.

    Examples
    ========

    Lets divide `x**3*y**4*z` by `x*y**2`::

        >>> from sympy.polys.monomials import monomial_ldiv

        >>> monomial_ldiv((3, 4, 1), (1, 2, 0))
        (2, 2, 1)

    which gives `x**2*y**2*z`.

        >>> monomial_ldiv((3, 4, 1), (1, 2, 2))
        (2, 2, -1)

    which gives `x**2*y**2*z**-1`.

    """
    ...

def monomial_pow(A, n) -> tuple[Any, ...]:
    """Return the n-th pow of the monomial. """
    ...

def monomial_gcd(A, B) -> tuple[Any, ...]:
    """
    Greatest common divisor of tuples representing monomials.

    Examples
    ========

    Lets compute GCD of `x*y**4*z` and `x**3*y**2`::

        >>> from sympy.polys.monomials import monomial_gcd

        >>> monomial_gcd((1, 4, 1), (3, 2, 0))
        (1, 2, 0)

    which gives `x*y**2`.

    """
    ...

def monomial_lcm(A, B) -> tuple[Any, ...]:
    """
    Least common multiple of tuples representing monomials.

    Examples
    ========

    Lets compute LCM of `x*y**4*z` and `x**3*y**2`::

        >>> from sympy.polys.monomials import monomial_lcm

        >>> monomial_lcm((1, 4, 1), (3, 2, 0))
        (3, 4, 1)

    which gives `x**3*y**4*z`.

    """
    ...

def monomial_divides(A, B) -> bool:
    """
    Does there exist a monomial X such that XA == B?

    Examples
    ========

    >>> from sympy.polys.monomials import monomial_divides
    >>> monomial_divides((1, 2), (3, 4))
    True
    >>> monomial_divides((1, 2), (0, 2))
    False
    """
    ...

def monomial_max(*monoms) -> tuple[Any, ...]:
    """
    Returns maximal degree for each variable in a set of monomials.

    Examples
    ========

    Consider monomials `x**3*y**4*z**5`, `y**5*z` and `x**6*y**3*z**9`.
    We wish to find out what is the maximal degree for each of `x`, `y`
    and `z` variables::

        >>> from sympy.polys.monomials import monomial_max

        >>> monomial_max((3,4,5), (0,5,1), (6,3,9))
        (6, 5, 9)

    """
    ...

def monomial_min(*monoms) -> tuple[Any, ...]:
    """
    Returns minimal degree for each variable in a set of monomials.

    Examples
    ========

    Consider monomials `x**3*y**4*z**5`, `y**5*z` and `x**6*y**3*z**9`.
    We wish to find out what is the minimal degree for each of `x`, `y`
    and `z` variables::

        >>> from sympy.polys.monomials import monomial_min

        >>> monomial_min((3,4,5), (0,5,1), (6,3,9))
        (0, 3, 1)

    """
    ...

def monomial_deg(M) -> int:
    """
    Returns the total degree of a monomial.

    Examples
    ========

    The total degree of `xy^2` is 3:

    >>> from sympy.polys.monomials import monomial_deg
    >>> monomial_deg((1, 2))
    3
    """
    ...

def term_div(a, b, domain) -> tuple[tuple[Any, ...], Any] | None:
    """Division of two terms in over a ring/field. """
    ...

class MonomialOps:
    """Code generator of fast monomial arithmetic functions. """
    def __init__(self, ngens) -> None:
        ...
    
    def mul(self):
        ...
    
    def pow(self):
        ...
    
    def mulpow(self):
        ...
    
    def ldiv(self):
        ...
    
    def div(self):
        ...
    
    def lcm(self):
        ...
    
    def gcd(self):
        ...
    


@public
class Monomial(PicklableWithSlots):
    """Class representing a monomial, i.e. a product of powers. """
    __slots__ = ...
    def __init__(self, monom, gens=...) -> None:
        ...
    
    def rebuild(self, exponents, gens=...) -> Self:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[int]:
        ...
    
    def __getitem__(self, item):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    def as_expr(self, *gens) -> Order:
        """Convert a monomial instance to a SymPy expression. """
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __mul__(self, other) -> Self:
        ...
    
    def __truediv__(self, other) -> Self:
        ...
    
    __floordiv__ = ...
    def __pow__(self, other) -> Self:
        ...
    
    def gcd(self, other) -> Self:
        """Greatest common divisor of monomials. """
        ...
    
    def lcm(self, other) -> Self:
        """Least common multiple of monomials. """
        ...
    


