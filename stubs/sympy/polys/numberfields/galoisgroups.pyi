from typing import Any
from sympy.polys.numberfields.galois_resolvents import GaloisGroupException
from sympy.utilities import public

"""
Compute Galois groups of polynomials.

We use algorithms from [1], with some modifications to use lookup tables for
resolvents.

References
==========

.. [1] Cohen, H. *A Course in Computational Algebraic Number Theory*.

"""
class MaxTriesException(GaloisGroupException):
    ...


def tschirnhausen_transformation(T, max_coeff=..., max_tries=..., history=..., fixed_order=...) -> tuple[Any, Any]:
    r"""
    Given a univariate, monic, irreducible polynomial over the integers, find
    another such polynomial defining the same number field.

    Explanation
    ===========

    See Alg 6.3.4 of [1].

    Parameters
    ==========

    T : Poly
        The given polynomial
    max_coeff : int
        When choosing a transformation as part of the process,
        keep the coeffs between plus and minus this.
    max_tries : int
        Consider at most this many transformations.
    history : set, None, optional (default=None)
        Pass a set of ``Poly.rep``'s in order to prevent any of these
        polynomials from being returned as the polynomial ``U`` i.e. the
        transformation of the given polynomial *T*. The given poly *T* will
        automatically be added to this set, before we try to find a new one.
    fixed_order : bool, default True
        If ``True``, work through candidate transformations A(x) in a fixed
        order, from small coeffs to large, resulting in deterministic behavior.
        If ``False``, the A(x) are chosen randomly, while still working our way
        up from small coefficients to larger ones.

    Returns
    =======

    Pair ``(A, U)``

        ``A`` and ``U`` are ``Poly``, ``A`` is the
        transformation, and ``U`` is the transformed polynomial that defines
        the same number field as *T*. The polynomial ``A`` maps the roots of
        *T* to the roots of ``U``.

    Raises
    ======

    MaxTriesException
        if could not find a polynomial before exceeding *max_tries*.

    """
    ...

def has_square_disc(T) -> bool:
    """Convenience to check if a Poly or dup has square discriminant. """
    ...

@public
def galois_group(f, *gens, by_name=..., max_tries=..., randomize=..., **args) -> Any:
    r"""
    Compute the Galois group for polynomials *f* up to degree 6.

    Examples
    ========

    >>> from sympy import galois_group
    >>> from sympy.abc import x
    >>> f = x**4 + 1
    >>> G, alt = galois_group(f)
    >>> print(G)
    PermutationGroup([
    (0 1)(2 3),
    (0 2)(1 3)])

    The group is returned along with a boolean, indicating whether it is
    contained in the alternating group $A_n$, where $n$ is the degree of *T*.
    Along with other group properties, this can help determine which group it
    is:

    >>> alt
    True
    >>> G.order()
    4

    Alternatively, the group can be returned by name:

    >>> G_name, _ = galois_group(f, by_name=True)
    >>> print(G_name)
    S4TransitiveSubgroups.V

    The group itself can then be obtained by calling the name's
    ``get_perm_group()`` method:

    >>> G_name.get_perm_group()
    PermutationGroup([
    (0 1)(2 3),
    (0 2)(1 3)])

    Group names are values of the enum classes
    :py:class:`sympy.combinatorics.galois.S1TransitiveSubgroups`,
    :py:class:`sympy.combinatorics.galois.S2TransitiveSubgroups`,
    etc.

    Parameters
    ==========

    f : Expr
        Irreducible polynomial over :ref:`ZZ` or :ref:`QQ`, whose Galois group
        is to be determined.
    gens : optional list of symbols
        For converting *f* to Poly, and will be passed on to the
        :py:func:`~.poly_from_expr` function.
    by_name : bool, default False
        If ``True``, the Galois group will be returned by name.
        Otherwise it will be returned as a :py:class:`~.PermutationGroup`.
    max_tries : int, default 30
        Make at most this many attempts in those steps that involve
        generating Tschirnhausen transformations.
    randomize : bool, default False
        If ``True``, then use random coefficients when generating Tschirnhausen
        transformations. Otherwise try transformations in a fixed order. Both
        approaches start with small coefficients and degrees and work upward.
    args : optional
        For converting *f* to Poly, and will be passed on to the
        :py:func:`~.poly_from_expr` function.

    Returns
    =======

    Pair ``(G, alt)``
        The first element ``G`` indicates the Galois group. It is an instance
        of one of the :py:class:`sympy.combinatorics.galois.S1TransitiveSubgroups`
        :py:class:`sympy.combinatorics.galois.S2TransitiveSubgroups`, etc. enum
        classes if *by_name* was ``True``, and a :py:class:`~.PermutationGroup`
        if ``False``.

        The second element is a boolean, saying whether the group is contained
        in the alternating group $A_n$ ($n$ the degree of *T*).

    Raises
    ======

    ValueError
        if *f* is of an unsupported degree.

    MaxTriesException
        if could not complete before exceeding *max_tries* in those steps
        that involve generating Tschirnhausen transformations.

    See Also
    ========

    .Poly.galois_group

    """
    ...

