from enum import Enum
from typing import Any

from sympy.combinatorics.perm_groups import PermutationGroup

r"""
Construct transitive subgroups of symmetric groups, useful in Galois theory.

Besides constructing instances of the :py:class:`~.PermutationGroup` class to
represent the transitive subgroups of $S_n$ for small $n$, this module provides
*names* for these groups.

In some applications, it may be preferable to know the name of a group,
rather than receive an instance of the :py:class:`~.PermutationGroup`
class, and then have to do extra work to determine which group it is, by
checking various properties.

Names are instances of ``Enum`` classes defined in this module. With a name in
hand, the name's ``get_perm_group`` method can then be used to retrieve a
:py:class:`~.PermutationGroup`.

The names used for groups in this module are taken from [1].

References
==========

.. [1] Cohen, H. *A Course in Computational Algebraic Number Theory*.

"""
class S1TransitiveSubgroups(Enum):
    """
    Names for the transitive subgroups of S1.
    """
    S1 = ...
    def get_perm_group(self) -> PermutationGroup:
        ...
    


class S2TransitiveSubgroups(Enum):
    """
    Names for the transitive subgroups of S2.
    """
    S2 = ...
    def get_perm_group(self) -> PermutationGroup:
        ...
    


class S3TransitiveSubgroups(Enum):
    """
    Names for the transitive subgroups of S3.
    """
    A3 = ...
    S3 = ...
    def get_perm_group(self) -> PermutationGroup | None:
        ...
    


class S4TransitiveSubgroups(Enum):
    """
    Names for the transitive subgroups of S4.
    """
    C4 = ...
    V = ...
    D4 = ...
    A4 = ...
    S4 = ...
    def get_perm_group(self) -> PermutationGroup | None:
        ...
    


class S5TransitiveSubgroups(Enum):
    """
    Names for the transitive subgroups of S5.
    """
    C5 = ...
    D5 = ...
    M20 = ...
    A5 = ...
    S5 = ...
    def get_perm_group(self) -> PermutationGroup | None:
        ...
    


class S6TransitiveSubgroups(Enum):
    """
    Names for the transitive subgroups of S6.
    """
    C6 = ...
    S3 = ...
    D6 = ...
    A4 = ...
    G18 = ...
    A4xC2 = ...
    S4m = ...
    S4p = ...
    G36m = ...
    G36p = ...
    S4xC2 = ...
    PSL2F5 = ...
    G72 = ...
    PGL2F5 = ...
    A6 = ...
    S6 = ...
    def get_perm_group(self) -> PermutationGroup | None:
        ...
    


def four_group() -> PermutationGroup:
    """
    Return a representation of the Klein four-group as a transitive subgroup
    of S4.
    """
    ...

def M20() -> PermutationGroup:
    """
    Return a representation of the metacyclic group M20, a transitive subgroup
    of S5 that is one of the possible Galois groups for polys of degree 5.

    Notes
    =====

    See [1], Page 323.

    """
    ...

def S3_in_S6() -> PermutationGroup:
    """
    Return a representation of S3 as a transitive subgroup of S6.

    Notes
    =====

    The representation is found by viewing the group as the symmetries of a
    triangular prism.

    """
    ...

def A4_in_S6() -> PermutationGroup:
    """
    Return a representation of A4 as a transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def S4m() -> PermutationGroup:
    """
    Return a representation of the S4- transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def S4p() -> PermutationGroup:
    """
    Return a representation of the S4+ transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def A4xC2() -> PermutationGroup:
    """
    Return a representation of the (A4 x C2) transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def S4xC2() -> PermutationGroup:
    """
    Return a representation of the (S4 x C2) transitive subgroup of S6.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def G18() -> PermutationGroup:
    """
    Return a representation of the group G18, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with C2.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def G36m() -> PermutationGroup:
    """
    Return a representation of the group G36-, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with C2^2.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def G36p() -> PermutationGroup:
    """
    Return a representation of the group G36+, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with C4.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def G72() -> PermutationGroup:
    """
    Return a representation of the group G72, a transitive subgroup of S6
    isomorphic to the semidirect product of C3^2 with D4.

    Notes
    =====

    See [1], Page 325.

    """
    ...

def PSL2F5() -> PermutationGroup:
    r"""
    Return a representation of the group $PSL_2(\mathbb{F}_5)$, as a transitive
    subgroup of S6, isomorphic to $A_5$.

    Notes
    =====

    This was computed using :py:func:`~.find_transitive_subgroups_of_S6`.

    """
    ...

def PGL2F5() -> PermutationGroup:
    r"""
    Return a representation of the group $PGL_2(\mathbb{F}_5)$, as a transitive
    subgroup of S6, isomorphic to $S_5$.

    Notes
    =====

    See [1], Page 325.

    """
    ...

def find_transitive_subgroups_of_S6(*targets, print_report=...) -> dict[Any, Any]:
    r"""
    Search for certain transitive subgroups of $S_6$.

    The symmetric group $S_6$ has 16 different transitive subgroups, up to
    conjugacy. Some are more easily constructed than others. For example, the
    dihedral group $D_6$ is immediately found, but it is not at all obvious how
    to realize $S_4$ or $S_5$ *transitively* within $S_6$.

    In some cases there are well-known constructions that can be used. For
    example, $S_5$ is isomorphic to $PGL_2(\mathbb{F}_5)$, which acts in a
    natural way on the projective line $P^1(\mathbb{F}_5)$, a set of order 6.

    In absence of such special constructions however, we can simply search for
    generators. For example, transitive instances of $A_4$ and $S_4$ can be
    found within $S_6$ in this way.

    Once we are engaged in such searches, it may then be easier (if less
    elegant) to find even those groups like $S_5$ that do have special
    constructions, by mere search.

    This function locates generators for transitive instances in $S_6$ of the
    following subgroups:

    * $A_4$
    * $S_4^-$ ($S_4$ not contained within $A_6$)
    * $S_4^+$ ($S_4$ contained within $A_6$)
    * $A_4 \times C_2$
    * $S_4 \times C_2$
    * $G_{18}   = C_3^2 \rtimes C_2$
    * $G_{36}^- = C_3^2 \rtimes C_2^2$
    * $G_{36}^+ = C_3^2 \rtimes C_4$
    * $G_{72}   = C_3^2 \rtimes D_4$
    * $A_5$
    * $S_5$

    Note: Each of these groups also has a dedicated function in this module
    that returns the group immediately, using generators that were found by
    this search procedure.

    The search procedure serves as a record of how these generators were
    found. Also, due to randomness in the generation of the elements of
    permutation groups, it can be called again, in order to (probably) get
    different generators for the same groups.

    Parameters
    ==========

    targets : list of :py:class:`~.S6TransitiveSubgroups` values
        The groups you want to find.

    print_report : bool (default False)
        If True, print to stdout the generators found for each group.

    Returns
    =======

    dict
        mapping each name in *targets* to the :py:class:`~.PermutationGroup`
        that was found

    References
    ==========

    .. [2] https://en.wikipedia.org/wiki/Projective_linear_group#Exceptional_isomorphisms
    .. [3] https://en.wikipedia.org/wiki/Automorphisms_of_the_symmetric_and_alternating_groups#PGL%282,5%29

    """
    ...

