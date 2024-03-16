"""Definitions of monomial orderings. """
__all__ = ["lex", "grlex", "grevlex", "ilex", "igrlex", "igrevlex"]
class MonomialOrder:
    """Base class for monomial orderings. """
    alias: str | None = ...
    is_global: bool | None = ...
    is_default = ...
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __call__(self, monomial):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    


class LexOrder(MonomialOrder):
    """Lexicographic order of monomials. """
    alias = ...
    is_global = ...
    is_default = ...
    def __call__(self, monomial):
        ...
    


class GradedLexOrder(MonomialOrder):
    """Graded lexicographic order of monomials. """
    alias = ...
    is_global = ...
    def __call__(self, monomial) -> tuple[int, Any]:
        ...
    


class ReversedGradedLexOrder(MonomialOrder):
    """Reversed graded lexicographic order of monomials. """
    alias = ...
    is_global = ...
    def __call__(self, monomial) -> tuple[int, tuple[Any, ...]]:
        ...
    


class ProductOrder(MonomialOrder):
    """
    A product order built from other monomial orders.

    Given (not necessarily total) orders O1, O2, ..., On, their product order
    P is defined as M1 > M2 iff there exists i such that O1(M1) = O2(M2),
    ..., Oi(M1) = Oi(M2), O{i+1}(M1) > O{i+1}(M2).

    Product orders are typically built from monomial orders on different sets
    of variables.

    ProductOrder is constructed by passing a list of pairs
    [(O1, L1), (O2, L2), ...] where Oi are MonomialOrders and Li are callables.
    Upon comparison, the Li are passed the total monomial, and should filter
    out the part of the monomial to pass to Oi.

    Examples
    ========

    We can use a lexicographic order on x_1, x_2 and also on
    y_1, y_2, y_3, and their product on {x_i, y_i} as follows:

    >>> from sympy.polys.orderings import lex, grlex, ProductOrder
    >>> P = ProductOrder(
    ...     (lex, lambda m: m[:2]), # lex order on x_1 and x_2 of monomial
    ...     (grlex, lambda m: m[2:]) # grlex on y_1, y_2, y_3
    ... )
    >>> P((2, 1, 1, 0, 0)) > P((1, 10, 0, 2, 0))
    True

    Here the exponent `2` of `x_1` in the first monomial
    (`x_1^2 x_2 y_1`) is bigger than the exponent `1` of `x_1` in the
    second monomial (`x_1 x_2^10 y_2^2`), so the first monomial is greater
    in the product ordering.

    >>> P((2, 1, 1, 0, 0)) < P((2, 1, 0, 2, 0))
    True

    Here the exponents of `x_1` and `x_2` agree, so the grlex order on
    `y_1, y_2, y_3` is used to decide the ordering. In this case the monomial
    `y_2^2` is ordered larger than `y_1`, since for the grlex order the degree
    of the monomial is most important.
    """
    def __init__(self, *args) -> None:
        ...
    
    def __call__(self, monomial) -> tuple[Any, ...]:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    @property
    def is_global(self) -> bool | None:
        ...
    


class InverseOrder(MonomialOrder):
    """
    The "inverse" of another monomial order.

    If O is any monomial order, we can construct another monomial order iO
    such that `A >_{iO} B` if and only if `B >_O A`. This is useful for
    constructing local orders.

    Note that many algorithms only work with *global* orders.

    For example, in the inverse lexicographic order on a single variable `x`,
    high powers of `x` count as small:

    >>> from sympy.polys.orderings import lex, InverseOrder
    >>> ilex = InverseOrder(lex)
    >>> ilex((5,)) < ilex((0,))
    True
    """
    def __init__(self, O) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __call__(self, monomial) -> tuple[Any, ...]:
        ...
    
    @property
    def is_global(self) -> bool | None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


lex = ...
grlex = ...
grevlex = ...
ilex = ...
igrlex = ...
igrevlex = ...
_monomial_key = ...
def monomial_key(order=..., gens=...) -> Callable[..., Any] | LexOrder:
    """
    Return a function defining admissible order on monomials.

    The result of a call to :func:`monomial_key` is a function which should
    be used as a key to :func:`sorted` built-in function, to provide order
    in a set of monomials of the same length.

    Currently supported monomial orderings are:

    1. lex       - lexicographic order (default)
    2. grlex     - graded lexicographic order
    3. grevlex   - reversed graded lexicographic order
    4. ilex, igrlex, igrevlex - the corresponding inverse orders

    If the ``order`` input argument is not a string but has ``__call__``
    attribute, then it will pass through with an assumption that the
    callable object defines an admissible order on monomials.

    If the ``gens`` input argument contains a list of generators, the
    resulting key function can be used to sort SymPy ``Expr`` objects.

    """
    ...

class _ItemGetter:
    """Helper class to return a subsequence of values."""
    def __init__(self, seq) -> None:
        ...
    
    def __call__(self, m) -> tuple[Any, ...]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


def build_product_order(arg, gens) -> ProductOrder:
    """
    Build a monomial order on ``gens``.

    ``arg`` should be a tuple of iterables. The first element of each iterable
    should be a string or monomial order (will be passed to monomial_key),
    the others should be subsets of the generators. This function will build
    the corresponding product order.

    For example, build a product of two grlex orders:

    >>> from sympy.polys.orderings import build_product_order
    >>> from sympy.abc import x, y, z, t

    >>> O = build_product_order((("grlex", x, y), ("grlex", z, t)), [x, y, z, t])
    >>> O((1, 2, 3, 4))
    ((3, (1, 2)), (7, (3, 4)))

    """
    ...

